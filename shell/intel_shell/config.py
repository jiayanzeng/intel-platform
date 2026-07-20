"""Shell configuration: environment + business config (subscriptions).

The config split is the architecture in miniature:
- config/core.json + config/entities.json belong to the CORE (sectors,
  sources, licenses, gazetteer) — the engine's inputs;
- config/subscriptions.json belongs to the SHELL (clients, entitled
  sectors, API keys) — pure business state the core never sees.

v0.5 moved the on-disk record to a `key_hash` (HMAC of the API key) rather than
the raw key, and added a `SubscriptionStore` so the billing webhook can flip a
client's sectors at runtime and persist it.

v0.6 (T6) adds two things on top, both still shell-only:

- **Key rotation with a grace window.** A record can carry *several* active
  hashes (`key_hashes`, primary first; `key_hash` is still read as the legacy
  singular). Rotating installs a new primary and moves the old hashes into
  `retiring`, each with a `retire_after` deadline — so a client's old key keeps
  working until the deadline passes and is refused the moment it does. Rotating
  with no deadline revokes the old keys immediately. Expired entries are pruned
  on save, so the file doesn't grow scar tissue.
- **A pluggable backend.** `SubscriptionStore` (JSON) and
  `SqliteSubscriptionStore` implement one interface, so `SUBSCRIPTIONS_PATH`
  can be a JSON path or `sqlite:///path.db` and nothing else in the shell
  changes. Both mutate in memory and commit on `save()` — atomically (temp file
  + rename for JSON, one transaction for SQLite), which is what lets the webhook
  apply a batch of events and persist once.

The raw API key is never written by either backend, on any path.
"""

from __future__ import annotations

import json
import os
import sqlite3
import sys
import tempfile
import time
from dataclasses import dataclass, field, replace
from pathlib import Path

from .security import hash_token, token_matches


CORE_URL = os.environ.get("CORE_URL", "http://127.0.0.1:8788")
CORE_TOKEN = os.environ.get("CORE_TOKEN")  # optional shared secret

# The repo root, derived from this file's location (shell/intel_shell/config.py
# -> ../../). The default config path is anchored to it rather than to the
# process CWD: `uvicorn intel_shell.app:app` launched from a systemd unit, a
# different directory, or anywhere but the repo root used to silently find no
# subscriptions and 401 every request. An explicit SUBSCRIPTIONS_PATH always
# wins, and a relative one is still honored as-is (relative to CWD), so nothing
# that worked before stops working. (T9.6)
_REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SUBSCRIPTIONS = "config/subscriptions.json"


def default_subscriptions_path() -> str:
    """Where to look for subscriptions when the env doesn't say."""
    anchored = _REPO_ROOT / DEFAULT_SUBSCRIPTIONS
    if anchored.exists():
        return str(anchored)
    return DEFAULT_SUBSCRIPTIONS  # last resort: the old CWD-relative behavior


SUBSCRIPTIONS_PATH = os.environ.get("SUBSCRIPTIONS_PATH") or default_subscriptions_path()

SQLITE_PREFIX = "sqlite://"


@dataclass(frozen=True)
class RetiringKey:
    """A superseded key hash, still honored until `retire_after` (unix ts)."""

    key_hash: str
    retire_after: float

    def is_active(self, now: float) -> bool:
        return now < self.retire_after


@dataclass(frozen=True)
class Subscription:
    client: str
    sectors: tuple[str, ...] = field(default_factory=tuple)
    # Legacy/demo: a raw key may still be present in older config or in tests.
    api_key: str | None = None
    # Legacy singular / current primary. Never the raw key on disk.
    key_hash: str | None = None
    # Additional active hashes (rotation). Primary first when persisted.
    key_hashes: tuple[str, ...] = field(default_factory=tuple)
    # Superseded hashes still inside their grace window.
    retiring: tuple[RetiringKey, ...] = field(default_factory=tuple)

    def effective_hash(self) -> str | None:
        """The client's PRIMARY digest — the one a fresh key would be checked
        against first, and the one persisted as the legacy singular field.

        Prefers a stored `key_hash`, then the first of `key_hashes`, then hashes
        a legacy raw `api_key` on the fly so old config and direct-construction
        tests keep working unchanged.
        """
        if self.key_hash:
            return self.key_hash
        if self.key_hashes:
            return self.key_hashes[0]
        if self.api_key:
            return hash_token(self.api_key)
        return None

    def active_hashes(self, now: float | None = None) -> tuple[str, ...]:
        """Every digest that should currently be accepted for this client:
        the primary, any other active hashes, and any retiring hash whose grace
        window hasn't closed. Expired hashes are simply absent — that is the
        whole of revocation.
        """
        t = time.time() if now is None else now
        out: list[str] = []
        for h in (self.effective_hash(), *self.key_hashes):
            if h and h not in out:
                out.append(h)
        for r in self.retiring:
            if r.is_active(t) and r.key_hash not in out:
                out.append(r.key_hash)
        return tuple(out)

    def matches(self, token: str, now: float | None = None) -> bool:
        """Constant-time check of `token` against every currently-active hash."""
        return any(token_matches(token, h) for h in self.active_hashes(now))

    def pruned(self, now: float | None = None) -> Subscription:
        """Drop retiring hashes whose grace window has closed."""
        t = time.time() if now is None else now
        keep = tuple(r for r in self.retiring if r.is_active(t))
        return self if keep == self.retiring else replace(self, retiring=keep)


def _subscription_from_raw(s: dict) -> Subscription:
    retiring = tuple(
        RetiringKey(key_hash=r["key_hash"], retire_after=float(r["retire_after"]))
        for r in s.get("retiring", [])
        if isinstance(r, dict) and r.get("key_hash") and r.get("retire_after") is not None
    )
    return Subscription(
        client=s["client"],
        sectors=tuple(s.get("sectors", [])),
        api_key=s.get("api_key"),
        key_hash=s.get("key_hash"),
        key_hashes=tuple(s.get("key_hashes", [])),
        retiring=retiring,
    )


def _subscription_to_raw(s: Subscription) -> dict:
    """The on-disk record. Never contains a raw key, on any path."""
    primary = s.effective_hash()
    actives: list[str] = []
    for h in (primary, *s.key_hashes):
        if h and h not in actives:
            actives.append(h)
    return {
        "client": s.client,
        "sectors": list(s.sectors),
        # Legacy singular, still written so an older reader keeps working.
        "key_hash": primary,
        # Canonical set, primary first.
        "key_hashes": actives,
        "retiring": [
            {"key_hash": r.key_hash, "retire_after": r.retire_after}
            for r in s.retiring
        ],
    }


def load_subscriptions(path: str | None = None) -> list[Subscription]:
    """Read subscriptions from a JSON file (or a sqlite:// URL)."""
    p = path or SUBSCRIPTIONS_PATH
    if p.startswith(SQLITE_PREFIX):
        return _sqlite_load(_sqlite_path(p))
    try:
        with open(p, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except FileNotFoundError:
        print(f"warning: subscriptions file not found at {p}; no clients configured",
              file=sys.stderr)
        return []
    return [_subscription_from_raw(s) for s in raw.get("subscriptions", [])]


def subscription_for(subs: list[Subscription], client: str) -> Subscription | None:
    return next((s for s in subs if s.client == client), None)


# ---------------------------------------------------------------------------
# Stores
# ---------------------------------------------------------------------------


class BaseSubscriptionStore:
    """The subscription store contract, backend-agnostic.

    Reads and mutations happen in memory; `save()` is the commit point, so a
    batch of webhook events can be applied and persisted exactly once. Backends
    differ only in what `save()` does — and both must do it atomically (HC9).
    """

    def __init__(self, subscriptions: list[Subscription]):
        self._subs: list[Subscription] = list(subscriptions)

    # -- reads -----------------------------------------------------------------

    def all(self) -> list[Subscription]:
        return list(self._subs)

    def __iter__(self):
        return iter(self._subs)

    def get(self, client: str) -> Subscription | None:
        return subscription_for(self._subs, client)

    def resolve_token(self, token: str, now: float | None = None) -> Subscription | None:
        return next((s for s in self._subs if s.matches(token, now)), None)

    # -- writes ----------------------------------------------------------------

    def upsert(
        self,
        client: str,
        sectors: tuple[str, ...],
        *,
        key_hash: str | None = None,
    ) -> Subscription:
        """Set a client's entitled sectors (creating the client if new).

        A `key_hash` is only applied when provisioning a brand-new client;
        entitlement changes for an existing client never touch its keys.
        """
        existing = self.get(client)
        if existing is None:
            sub = Subscription(client=client, sectors=tuple(sectors), key_hash=key_hash)
            self._subs.append(sub)
        else:
            sub = replace(existing, sectors=tuple(sectors))
            self._subs = [sub if s.client == client else s for s in self._subs]
        return sub

    def rotate_key(
        self,
        client: str,
        new_key_hash: str,
        *,
        retire_after: float | None = None,
    ) -> Subscription | None:
        """Install `new_key_hash` as the client's primary key.

        `retire_after` (an absolute unix timestamp) keeps the *previous* hashes
        working until that moment — the grace window that lets a client roll a
        key without downtime. Omit it and the old hashes are revoked at once.
        Returns None if the client is unknown.
        """
        existing = self.get(client)
        if existing is None:
            return None

        superseded = [h for h in existing.active_hashes() if h != new_key_hash]
        if retire_after is None:
            retiring: tuple[RetiringKey, ...] = ()  # immediate revocation
        else:
            # Keep any still-valid earlier grace entries, then add the ones we
            # just superseded (deduped, latest deadline wins).
            deadlines: dict[str, float] = {
                r.key_hash: r.retire_after
                for r in existing.retiring
                if r.is_active(time.time())
            }
            for h in superseded:
                deadlines[h] = max(retire_after, deadlines.get(h, 0.0))
            retiring = tuple(
                RetiringKey(key_hash=h, retire_after=d) for h, d in deadlines.items()
            )

        sub = replace(
            existing,
            api_key=None,  # any legacy raw key is superseded by the rotation
            key_hash=new_key_hash,
            key_hashes=(),
            retiring=retiring,
        )
        self._subs = [sub if s.client == client else s for s in self._subs]
        return sub

    def revoke_key(self, client: str, key_hash: str) -> bool:
        """Refuse a specific hash from now on — whether it's the primary, an
        additional active hash, or one inside its grace window. Returns True if
        anything was actually removed.
        """
        existing = self.get(client)
        if existing is None:
            return False
        before = existing.active_hashes()
        if key_hash not in before:
            return False
        remaining = [h for h in (existing.effective_hash(), *existing.key_hashes)
                     if h and h != key_hash]
        sub = replace(
            existing,
            api_key=None,
            key_hash=remaining[0] if remaining else None,
            key_hashes=tuple(remaining[1:]),
            retiring=tuple(r for r in existing.retiring if r.key_hash != key_hash),
        )
        self._subs = [sub if s.client == client else s for s in self._subs]
        return True

    def remove(self, client: str) -> bool:
        before = len(self._subs)
        self._subs = [s for s in self._subs if s.client != client]
        return len(self._subs) != before

    def prune(self, now: float | None = None) -> None:
        """Drop grace entries whose window has closed."""
        self._subs = [s.pruned(now) for s in self._subs]

    def save(self) -> None:  # pragma: no cover - overridden
        raise NotImplementedError


class SubscriptionStore(BaseSubscriptionStore):
    """JSON-file backed store (the default).

    Constructed from a plain list with no path it behaves as an in-memory store
    whose `save()` is a no-op — which is exactly what the shell tests want.
    """

    def __init__(self, subscriptions: list[Subscription], path: str | None = None):
        super().__init__(subscriptions)
        self._path = path

    def save(self) -> None:
        """Persist to the bound path atomically (temp file + rename).

        Raw `api_key`s are never written back: every record is stored in hashed
        form, so a save quietly migrates a legacy plaintext file to the hashed
        schema. Closed grace windows are pruned on the way out.
        """
        if not self._path:
            return
        self.prune()
        payload = {"subscriptions": [_subscription_to_raw(s) for s in self._subs]}
        directory = os.path.dirname(os.path.abspath(self._path))
        os.makedirs(directory, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=directory, suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(payload, f, indent=2)
                f.write("\n")
            os.replace(tmp, self._path)
        finally:
            if os.path.exists(tmp):
                os.remove(tmp)


SQLITE_SCHEMA = """
CREATE TABLE IF NOT EXISTS subscriptions (
    client     TEXT PRIMARY KEY,
    sectors    TEXT NOT NULL,   -- JSON array
    key_hash   TEXT,            -- primary digest (legacy singular)
    key_hashes TEXT NOT NULL,   -- JSON array, primary first
    retiring   TEXT NOT NULL,   -- JSON array of {key_hash, retire_after}
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);
"""


def _sqlite_path(url: str) -> str:
    """`sqlite:///abs/path.db` or `sqlite://relative.db` -> filesystem path."""
    rest = url[len(SQLITE_PREFIX):]
    return rest if rest.startswith("/") else rest.lstrip("/") or rest


def _sqlite_connect(path: str) -> sqlite3.Connection:
    directory = os.path.dirname(os.path.abspath(path))
    os.makedirs(directory, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.executescript(SQLITE_SCHEMA)
    return conn


def _sqlite_load(path: str) -> list[Subscription]:
    conn = _sqlite_connect(path)
    try:
        rows = conn.execute(
            "SELECT client, sectors, key_hash, key_hashes, retiring "
            "FROM subscriptions ORDER BY rowid"
        ).fetchall()
    finally:
        conn.close()
    return [
        _subscription_from_raw(
            {
                "client": client,
                "sectors": json.loads(sectors),
                "key_hash": key_hash,
                "key_hashes": json.loads(key_hashes),
                "retiring": json.loads(retiring),
            }
        )
        for client, sectors, key_hash, key_hashes, retiring in rows
    ]


class SqliteSubscriptionStore(BaseSubscriptionStore):
    """SQLite-backed store — same contract, different commit.

    Selected with `SUBSCRIPTIONS_PATH=sqlite:///var/lib/intel/subs.db`. `save()`
    rewrites the table inside a single transaction, so a crash mid-save leaves
    the previous state intact (the SQLite equivalent of the JSON store's
    temp-file-and-rename).
    """

    def __init__(self, subscriptions: list[Subscription], path: str):
        super().__init__(subscriptions)
        self._path = path

    @classmethod
    def open(cls, path: str) -> SqliteSubscriptionStore:
        return cls(_sqlite_load(path), path)

    def save(self) -> None:
        self.prune()
        conn = _sqlite_connect(self._path)
        try:
            with conn:  # one transaction: all rows land, or none do
                conn.execute("DELETE FROM subscriptions")
                conn.executemany(
                    "INSERT INTO subscriptions "
                    "(client, sectors, key_hash, key_hashes, retiring, updated_at) "
                    "VALUES (?, ?, ?, ?, ?, datetime('now'))",
                    [
                        (
                            r["client"],
                            json.dumps(r["sectors"]),
                            r["key_hash"],
                            json.dumps(r["key_hashes"]),
                            json.dumps(r["retiring"]),
                        )
                        for r in (_subscription_to_raw(s) for s in self._subs)
                    ],
                )
        finally:
            conn.close()


def load_subscription_store(path: str | None = None) -> BaseSubscriptionStore:
    """Open the store named by `path` (or `SUBSCRIPTIONS_PATH`).

    A `sqlite://` URL selects the SQLite backend; anything else is a JSON file.
    """
    p = path or SUBSCRIPTIONS_PATH
    if p.startswith(SQLITE_PREFIX):
        return SqliteSubscriptionStore.open(_sqlite_path(p))
    return SubscriptionStore(load_subscriptions(p), path=p)
