#!/usr/bin/env python3
"""Offline key administration: list, rotate, revoke.

The billing webhook can rotate a key when the *provider* drives the change.
This is the other half — when a human does, which is the common case for a
leaked key, a departing integrator, or a routine roll. It speaks to whatever
backend `SUBSCRIPTIONS_PATH` names (JSON file or `sqlite:///…`), so the same
command works in either deployment.

    # what does acme have right now?
    PYTHONPATH=shell python3 tools/admin_keys.py list

    # roll a key, old one keeps working for 24h (no flag-day cutover)
    PYTHONPATH=shell python3 tools/admin_keys.py rotate \
        --client acme-research --new-key ak_acme_NEW --grace 86400

    # leaked key: cut it off right now
    PYTHONPATH=shell python3 tools/admin_keys.py rotate \
        --client acme-research --new-key ak_acme_NEW

    # or refuse one specific hash without issuing a new key
    PYTHONPATH=shell python3 tools/admin_keys.py revoke \
        --client acme-research --hash <hex>

The new key is hashed here and only the hash is stored — print it once, hand it
to the client, and it is gone. If API_KEY_PEPPER is set it must be set here too,
since it is mixed into every hash.
"""

from __future__ import annotations

import argparse
import sys
import time

from intel_shell import config
from intel_shell.security import hash_token


def _fmt_deadline(ts: float) -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))


def cmd_list(store, args) -> int:
    now = time.time()
    for sub in store.all():
        print(f"{sub.client}  sectors={','.join(sub.sectors) or '-'}")
        primary = sub.effective_hash()
        print(f"    primary : {primary or '(none)'}")
        for h in sub.key_hashes:
            if h != primary:
                print(f"    active  : {h}")
        for r in sub.retiring:
            state = "grace" if r.is_active(now) else "EXPIRED"
            print(f"    {state:<8}: {r.key_hash}  until {_fmt_deadline(r.retire_after)}")
    return 0


def cmd_rotate(store, args) -> int:
    if store.get(args.client) is None:
        print(f"error: unknown client '{args.client}'", file=sys.stderr)
        return 1
    new_hash = args.new_hash or hash_token(args.new_key)
    retire_after = time.time() + args.grace if args.grace else None
    store.rotate_key(args.client, new_hash, retire_after=retire_after)
    store.save()
    if retire_after:
        print(f"rotated {args.client}: previous keys valid until "
              f"{_fmt_deadline(retire_after)}")
    else:
        print(f"rotated {args.client}: previous keys revoked immediately")
    print(f"new key_hash: {new_hash}")
    return 0


def cmd_revoke(store, args) -> int:
    if not store.revoke_key(args.client, args.hash):
        print(f"error: no active hash {args.hash} for '{args.client}'", file=sys.stderr)
        return 1
    store.save()
    print(f"revoked {args.hash} for {args.client}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--path", default=None,
                   help="subscriptions path or sqlite:// URL "
                        "(default: $SUBSCRIPTIONS_PATH)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="show every client's active and retiring hashes")

    r = sub.add_parser("rotate", help="install a new primary key")
    r.add_argument("--client", required=True)
    g = r.add_mutually_exclusive_group(required=True)
    g.add_argument("--new-key", help="the new raw key (hashed here, never stored)")
    g.add_argument("--new-hash", help="a pre-computed hash of the new key")
    r.add_argument("--grace", type=float, default=0,
                   help="seconds the OLD keys keep working (default 0 = revoke now)")

    v = sub.add_parser("revoke", help="refuse one specific hash")
    v.add_argument("--client", required=True)
    v.add_argument("--hash", required=True)

    args = p.parse_args(argv)
    store = config.load_subscription_store(args.path)
    return {"list": cmd_list, "rotate": cmd_rotate, "revoke": cmd_revoke}[args.cmd](
        store, args
    )


if __name__ == "__main__":
    raise SystemExit(main())
