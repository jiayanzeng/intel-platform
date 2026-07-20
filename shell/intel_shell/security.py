"""Security primitives for the shell: API-key hashing and webhook signatures.

Both are shell-only concerns — the core never sees a raw key or a billing
event, so this is exactly the kind of thing STATE.md said should be a
"shell-side only, core untouched" change.

Two design choices worth stating:

- **API keys are high-entropy secrets, not human passwords.** So the right
  primitive is a fast keyed digest with a constant-time compare, not bcrypt/
  argon2 (those exist to slow down guessing of low-entropy passwords). We use
  HMAC-SHA256 keyed by an optional server-side pepper. With no pepper the key
  is empty and the digest is a plain deterministic SHA-256-class MAC, which is
  what lets us ship a pre-hashed example `subscriptions.json`.
- **Everything that compares a secret uses `hmac.compare_digest`** so a
  timing side-channel can't leak the digest byte by byte.
"""

from __future__ import annotations

import hashlib
import hmac
import os

# Optional server-side secret mixed into every key hash. If set, the raw keys
# on disk (or the hashes in subscriptions.json) are useless without it. If you
# set or change this, you MUST regenerate the hashes in subscriptions.json
# (see tools/hash_subscriptions.py).
API_KEY_PEPPER = os.environ.get("API_KEY_PEPPER", "")

# Shared secret used to verify billing-provider webhook signatures. Unset means
# the billing endpoint is disabled (returns 503), the same way /v1/ask is
# disabled without an LLM endpoint.
BILLING_WEBHOOK_SECRET = os.environ.get("BILLING_WEBHOOK_SECRET")


def hash_token(token: str, pepper: str | None = None) -> str:
    """Return the stored form of an API key: HMAC-SHA256(pepper, token) as hex.

    `pepper=None` falls back to the process-wide `API_KEY_PEPPER` so callers
    don't each have to thread it through; pass an explicit pepper (including
    "") to override.
    """
    key = (API_KEY_PEPPER if pepper is None else pepper).encode("utf-8")
    return hmac.new(key, token.encode("utf-8"), hashlib.sha256).hexdigest()


def token_matches(token: str, key_hash: str, pepper: str | None = None) -> bool:
    """Constant-time check that a presented `token` hashes to `key_hash`."""
    return hmac.compare_digest(hash_token(token, pepper), key_hash)


def verify_webhook_signature(
    secret: str, payload: bytes, signature: str | None
) -> bool:
    """Verify an HMAC-SHA256 webhook signature over the raw request body.

    The header value may be a bare hex digest or carry a ``sha256=`` prefix
    (the convention GitHub, Stripe-lite, and most providers use). Comparison
    is constant-time; a missing or malformed signature is a clean False, never
    an exception.
    """
    if not signature:
        return False
    presented = signature.split("=", 1)[1] if "=" in signature else signature
    expected = hmac.new(secret.encode("utf-8"), payload, hashlib.sha256).hexdigest()
    try:
        return hmac.compare_digest(expected, presented.strip())
    except (ValueError, TypeError):
        return False
