"""T6: key rotation/revocation (T6a) and the store backends (T6c).

The store contract test is parametrized across BOTH backends, which is the
point: if JSON and SQLite ever disagree about what the store *means*, one of
them is a bug, and this is where it surfaces.
"""

from __future__ import annotations

import json
import os
import time

import pytest

from intel_shell import billing, config
from intel_shell.config import (
    SqliteSubscriptionStore,
    Subscription,
    SubscriptionStore,
)
from intel_shell.security import hash_token

OLD_KEY = "ak_acme_7f3d9c"
NEW_KEY = "ak_acme_rolled_1"


# --------------------------------------------------------------------------
# Both backends, one contract
# --------------------------------------------------------------------------


@pytest.fixture(params=["json", "sqlite"])
def store(request, tmp_path):
    """A persistent store of each supported backend, seeded identically."""
    subs = [
        Subscription(client="acme-research", sectors=("science", "technology"),
                     key_hash=hash_token(OLD_KEY)),
        Subscription(client="quant-desk", sectors=("finance",),
                     key_hash=hash_token("ak_quant_2b81aa")),
    ]
    if request.param == "json":
        s = SubscriptionStore(subs, path=str(tmp_path / "subs.json"))
    else:
        s = SqliteSubscriptionStore(subs, str(tmp_path / "subs.db"))
    s.save()
    return s


def _reopen(store):
    """Round-trip through the backend, so we test what actually persisted."""
    if isinstance(store, SqliteSubscriptionStore):
        return SqliteSubscriptionStore.open(store._path)
    return SubscriptionStore(config.load_subscriptions(store._path), path=store._path)


def test_store_contract_reads(store):
    assert {s.client for s in store.all()} == {"acme-research", "quant-desk"}
    assert store.get("acme-research").sectors == ("science", "technology")
    assert store.get("nobody") is None
    assert store.resolve_token(OLD_KEY).client == "acme-research"
    assert store.resolve_token("ak_wrong") is None


def test_store_contract_upsert_and_remove_persist(store):
    store.upsert("new-co", ("finance",), key_hash=hash_token("ak_new"))
    store.upsert("acme-research", ("science",))  # entitlement change only
    assert store.remove("quant-desk") is True
    assert store.remove("quant-desk") is False
    store.save()

    back = _reopen(store)
    assert {s.client for s in back.all()} == {"acme-research", "new-co"}
    assert back.get("acme-research").sectors == ("science",)
    # An entitlement change must not disturb the client's key.
    assert back.resolve_token(OLD_KEY).client == "acme-research"
    assert back.resolve_token("ak_new").client == "new-co"


def test_raw_key_never_persisted(store, tmp_path):
    """HC4 across both backends: a legacy raw key is hashed on save, never written."""
    store.upsert("legacy", ())
    store._subs = [
        Subscription(client="legacy", sectors=("science",), api_key="ak_plaintext")
        if s.client == "legacy" else s
        for s in store._subs
    ]
    store.save()

    blob = open(store._path, "rb").read()
    assert b"ak_plaintext" not in blob
    assert b"ak_acme_7f3d9c" not in blob
    # ...and the key still works, because the hash of it was stored.
    assert _reopen(store).resolve_token("ak_plaintext").client == "legacy"


# --------------------------------------------------------------------------
# T6a — rotation, grace, revocation
# --------------------------------------------------------------------------


def test_rotation_grace_window_honors_both_keys_then_expires(store):
    now = time.time()
    store.rotate_key("acme-research", hash_token(NEW_KEY), retire_after=now + 3600)
    store.save()
    back = _reopen(store)

    # During the grace window both keys resolve...
    assert back.resolve_token(NEW_KEY).client == "acme-research"
    assert back.resolve_token(OLD_KEY).client == "acme-research"
    # ...and the moment it closes, the old one is refused while the new one lives.
    later = now + 7200
    assert back.resolve_token(NEW_KEY, now=later).client == "acme-research"
    assert back.resolve_token(OLD_KEY, now=later) is None


def test_rotation_without_grace_revokes_old_key_immediately(store):
    store.rotate_key("acme-research", hash_token(NEW_KEY))  # no retire_after
    store.save()
    back = _reopen(store)
    assert back.resolve_token(NEW_KEY).client == "acme-research"
    assert back.resolve_token(OLD_KEY) is None  # a leaked key must die now, not later


def test_expired_grace_entries_are_pruned_on_save(store):
    store.rotate_key("acme-research", hash_token(NEW_KEY), retire_after=time.time() - 1)
    store.save()  # save() prunes what has already expired
    back = _reopen(store)
    assert back.get("acme-research").retiring == ()
    assert back.resolve_token(OLD_KEY) is None


def test_revoke_named_hash(store):
    old_hash = hash_token(OLD_KEY)
    assert store.revoke_key("acme-research", old_hash) is True
    assert store.revoke_key("acme-research", old_hash) is False  # already gone
    store.save()
    assert _reopen(store).resolve_token(OLD_KEY) is None


def test_rotation_only_affects_the_named_client(store):
    store.rotate_key("acme-research", hash_token(NEW_KEY))
    store.save()
    assert _reopen(store).resolve_token("ak_quant_2b81aa").client == "quant-desk"


# --------------------------------------------------------------------------
# T6a — the same thing, driven by a neutral webhook event
# --------------------------------------------------------------------------


def test_key_rotated_event_applies_grace():
    store = SubscriptionStore([
        Subscription(client="acme-research", sectors=("science",),
                     key_hash=hash_token(OLD_KEY)),
    ])
    deadline = time.time() + 600
    result = billing.apply_event(store, {
        "type": "subscription.key_rotated",
        "data": {"client": "acme-research", "key_hash": hash_token(NEW_KEY),
                 "retire_after": deadline},
    })
    assert result["action"] == "key_rotated"
    assert store.resolve_token(NEW_KEY).client == "acme-research"
    assert store.resolve_token(OLD_KEY).client == "acme-research"
    assert store.resolve_token(OLD_KEY, now=deadline + 1) is None


def test_key_rotated_event_rejects_a_raw_key():
    """A provider has no business sending us the key itself."""
    store = SubscriptionStore([Subscription(client="acme", key_hash="h")])
    with pytest.raises(billing.BillingError):
        billing.apply_event(store, {
            "type": "subscription.key_rotated",
            "data": {"client": "acme", "key_hash": "new", "api_key": "ak_oops"},
        })


def test_key_rotated_event_for_unknown_client_is_a_noop():
    store = SubscriptionStore([])
    result = billing.apply_event(store, {
        "type": "subscription.key_rotated",
        "data": {"client": "ghost", "key_hash": "abc"},
    })
    assert result["action"] == "noop"


# --------------------------------------------------------------------------
# T6c — migration preserves hashes and sectors byte-exact
# --------------------------------------------------------------------------


def test_json_to_sqlite_migration_preserves_hashes_and_sectors(tmp_path):
    src = tmp_path / "subs.json"
    src.write_text(json.dumps({"subscriptions": [
        {"client": "acme-research", "sectors": ["science", "technology"],
         "key_hash": hash_token(OLD_KEY)},
        {"client": "quant-desk", "sectors": ["finance"],
         "key_hash": hash_token("ak_quant_2b81aa")},
    ]}))
    dest = tmp_path / "subs.db"

    import tools.migrate_subscriptions as migrate
    rc = migrate.main([str(src), "--to", f"sqlite:///{dest}"])
    assert rc == 0

    before = config.load_subscriptions(str(src))
    after = config.load_subscriptions(f"sqlite:///{dest}")
    assert [(s.client, s.sectors, s.effective_hash()) for s in before] == \
           [(s.client, s.sectors, s.effective_hash()) for s in after]
    # And the keys still work against the migrated store.
    assert SqliteSubscriptionStore.open(str(dest)).resolve_token(OLD_KEY).client \
        == "acme-research"


# --------------------------------------------------------------------------
# T9.6 — the default config path must not depend on the process CWD
# --------------------------------------------------------------------------


def test_default_subscriptions_path_is_repo_anchored_not_cwd(tmp_path, monkeypatch):
    """Launched from anywhere (a systemd unit, /, a tmp dir), the shell must
    still find its subscriptions — previously it silently found none and 401'd
    every request.
    """
    monkeypatch.chdir(tmp_path)  # anywhere but the repo root
    monkeypatch.delenv("SUBSCRIPTIONS_PATH", raising=False)

    path = config.default_subscriptions_path()
    assert os.path.isabs(path)
    assert os.path.exists(path)

    store = config.load_subscription_store(path)
    assert store.resolve_token("ak_acme_7f3d9c").client == "acme-research"


def test_explicit_subscriptions_path_still_wins(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    custom = tmp_path / "mine.json"
    custom.write_text(json.dumps({"subscriptions": [
        {"client": "only-me", "sectors": ["finance"], "key_hash": hash_token("k")},
    ]}))
    store = config.load_subscription_store(str(custom))
    assert [s.client for s in store.all()] == ["only-me"]
