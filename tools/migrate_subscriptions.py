#!/usr/bin/env python3
"""One-shot JSON -> SQLite migration for the subscription store.

    PYTHONPATH=shell python3 tools/migrate_subscriptions.py \
        config/subscriptions.json --to sqlite:///var/lib/intel/subs.db

Then point the shell at it and nothing else changes:

    SUBSCRIPTIONS_PATH=sqlite:///var/lib/intel/subs.db \
        PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787

Hashes and sectors are carried across byte-exact — the migration must never be
an excuse to silently re-hash anything, because re-hashing would invalidate
every client's key. Legacy records that still carry a raw `api_key` are hashed
on the way in (the one intentional transformation), and the raw key is dropped.
"""

from __future__ import annotations

import argparse
import sys

from intel_shell import config


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("source", help="path to the existing subscriptions.json")
    p.add_argument("--to", required=True, help="destination sqlite:///path.db URL")
    args = p.parse_args(argv)

    if not args.to.startswith(config.SQLITE_PREFIX):
        print(f"error: --to must be a {config.SQLITE_PREFIX} URL", file=sys.stderr)
        return 1

    subs = config.load_subscriptions(args.source)
    if not subs:
        print(f"error: no subscriptions found in {args.source}", file=sys.stderr)
        return 1

    dest = config.SqliteSubscriptionStore(subs, config._sqlite_path(args.to))
    dest.save()

    # Read it straight back and prove the hashes survived the trip.
    reread = config.load_subscriptions(args.to)
    for before, after in zip(subs, reread):
        if before.client != after.client or before.sectors != after.sectors:
            print(f"error: mismatch for {before.client}", file=sys.stderr)
            return 1
        if before.effective_hash() != after.effective_hash():
            print(f"error: key hash changed for {before.client}", file=sys.stderr)
            return 1

    print(f"migrated {len(reread)} subscription(s) -> {args.to}")
    for s in reread:
        print(f"  {s.client}: sectors={','.join(s.sectors) or '-'} "
              f"hashes={len(s.active_hashes())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
