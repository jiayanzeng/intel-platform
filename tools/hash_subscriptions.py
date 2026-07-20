#!/usr/bin/env python3
"""Migrate a subscriptions.json from raw `api_key` to hashed `key_hash`.

The raw keys never need to live on disk once the platform speaks hashes. Run
this once against your plaintext config and keep only the output:

    PYTHONPATH=shell python3 tools/hash_subscriptions.py \
        config/subscriptions.json --out config/subscriptions.hashed.json

If you set API_KEY_PEPPER in the environment, the same pepper must be set
wherever the shell runs (it is mixed into every hash). Records that already
carry a `key_hash` are passed through untouched.
"""

from __future__ import annotations

import argparse
import json
import sys

from intel_shell.security import API_KEY_PEPPER, hash_token


def migrate(raw: dict) -> dict:
    out = []
    for s in raw.get("subscriptions", []):
        rec = {"client": s["client"], "sectors": list(s.get("sectors", []))}
        if s.get("key_hash"):
            rec["key_hash"] = s["key_hash"]
        elif s.get("api_key"):
            rec["key_hash"] = hash_token(s["api_key"])
        else:
            print(f"warning: {s.get('client')!r} has no api_key or key_hash",
                  file=sys.stderr)
        out.append(rec)
    return {"subscriptions": out}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", help="path to a plaintext subscriptions.json")
    ap.add_argument("--out", default=None, help="output path (default: stdout)")
    args = ap.parse_args(argv)

    with open(args.input, "r", encoding="utf-8") as f:
        raw = json.load(f)

    migrated = migrate(raw)
    text = json.dumps(migrated, indent=2) + "\n"

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        pepper_note = " (with pepper)" if API_KEY_PEPPER else ""
        print(f"wrote {args.out}{pepper_note}", file=sys.stderr)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
