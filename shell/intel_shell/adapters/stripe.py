"""Stripe -> neutral billing events.

Two distinct jobs, deliberately separable and separately tested:

1. **Signature verification** (`verify_signature`). Stripe signs with a header
   of the form `t=<unix>,v1=<hex>[,v1=<hex>...]`, where the MAC is taken over
   `"{t}.{raw_body}"` — the timestamp is *inside* the signed material, which is
   what makes it replay-resistant. So verification has to check two things, and
   both matter:
     - the MAC is valid (constant-time compare, and a rolled secret can leave
       several `v1`s present — any valid one passes);
     - the timestamp is recent. Without the freshness check an attacker who
       captured one signed request could replay it forever, and it would verify
       perfectly, because it *is* a genuine Stripe-signed body.
   A malformed header is a clean False, never an exception.

2. **Payload mapping** (`to_neutral_events`). `customer.subscription.*` becomes
   `subscription.*`. Anything else — invoices, payment intents, the long tail of
   Stripe's event catalogue — is ignored rather than erroring: a webhook
   endpoint that 500s on an event type it merely doesn't care about will get
   itself disabled by the provider's retry logic.

Where do *sectors* come from? Stripe knows about prices, not our product model,
so the mapping has to be configured. Two supported ways, in order:
  - `metadata.sectors` on the subscription: `"science,technology"` (simplest;
    set it when you create the subscription);
  - a price/product -> sectors map (`STRIPE_PRICE_SECTORS`, JSON), which is the
    grown-up option: entitlements follow what the customer actually bought.
The client id comes from `metadata.client`, falling back to the Stripe customer
id — so `metadata.client` is what ties a Stripe customer to our client record.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import time

# How far out of date a signed request may be before we refuse it (seconds).
# Stripe's own libraries default to 5 minutes.
DEFAULT_TOLERANCE = 300

STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET")

EVENT_MAP = {
    "customer.subscription.created": "subscription.created",
    "customer.subscription.updated": "subscription.updated",
    "customer.subscription.deleted": "subscription.deleted",
}


def _parse_signature_header(header: str) -> tuple[int | None, list[str]]:
    """Pull the timestamp and every `v1` signature out of a Stripe header."""
    timestamp: int | None = None
    signatures: list[str] = []
    for part in header.split(","):
        if "=" not in part:
            continue
        scheme, _, value = part.strip().partition("=")
        if scheme == "t":
            try:
                timestamp = int(value)
            except ValueError:
                return None, []
        elif scheme == "v1":
            signatures.append(value)
    return timestamp, signatures


def verify_signature(
    secret: str,
    payload: bytes,
    header: str | None,
    tolerance: int = DEFAULT_TOLERANCE,
    now: float | None = None,
) -> bool:
    """Verify a `Stripe-Signature` header over the raw request body."""
    if not header or not secret:
        return False
    timestamp, signatures = _parse_signature_header(header)
    if timestamp is None or not signatures:
        return False

    # Freshness: a captured-and-replayed body is genuinely signed, so the
    # timestamp is the only thing standing between us and a replay.
    current = time.time() if now is None else now
    if tolerance and abs(current - timestamp) > tolerance:
        return False

    signed = b"%d." % timestamp + payload
    expected = hmac.new(secret.encode("utf-8"), signed, hashlib.sha256).hexdigest()
    return any(hmac.compare_digest(expected, s.strip()) for s in signatures)


def sign(secret: str, payload: bytes, timestamp: int) -> str:
    """Produce a `Stripe-Signature` header. Test helper — and the executable
    documentation of the scheme above.
    """
    signed = b"%d." % timestamp + payload
    mac = hmac.new(secret.encode("utf-8"), signed, hashlib.sha256).hexdigest()
    return f"t={timestamp},v1={mac}"


def _price_sector_map() -> dict[str, list[str]]:
    raw = os.environ.get("STRIPE_PRICE_SECTORS")
    if not raw:
        return {}
    try:
        parsed = json.loads(raw)
    except ValueError:
        return {}
    if not isinstance(parsed, dict):
        return {}
    return {
        k: ([v] if isinstance(v, str) else list(v))
        for k, v in parsed.items()
        if isinstance(v, (str, list))
    }


def _sectors_for(obj: dict, price_map: dict[str, list[str]]) -> list[str]:
    """Entitled sectors for a Stripe subscription object."""
    meta = obj.get("metadata") or {}
    raw = meta.get("sectors")
    if isinstance(raw, str) and raw.strip():
        return [s.strip() for s in raw.split(",") if s.strip()]
    if isinstance(raw, list):
        return [str(s) for s in raw]

    # Otherwise derive entitlements from what was actually purchased.
    sectors: list[str] = []
    items = (obj.get("items") or {}).get("data") or []
    for item in items:
        price = item.get("price") or {}
        for key in (price.get("id"), price.get("product"), price.get("lookup_key")):
            for sector in price_map.get(key, []) if key else []:
                if sector not in sectors:
                    sectors.append(sector)
    return sectors


def to_neutral_events(
    payload: dict, price_map: dict[str, list[str]] | None = None
) -> list[dict]:
    """Map one Stripe event into zero or more neutral billing events.

    Zero is a perfectly good answer: an event type we don't handle is ignored,
    not an error.
    """
    etype = payload.get("type")
    if not isinstance(etype, str) or etype not in EVENT_MAP:
        return []

    obj = ((payload.get("data") or {}).get("object")) or {}
    if not isinstance(obj, dict):
        return []

    meta = obj.get("metadata") or {}
    client = meta.get("client") or obj.get("customer")
    if not client:
        return []  # nothing to attach the entitlement to

    neutral = EVENT_MAP[etype]
    if neutral == "subscription.deleted":
        return [{"type": neutral, "data": {"client": str(client)}}]

    pm = _price_sector_map() if price_map is None else price_map
    data: dict = {"client": str(client), "sectors": _sectors_for(obj, pm)}
    # Stripe never sends us a raw API key (it has no idea one exists); a
    # brand-new client's key hash may be carried in metadata if you provision
    # that way.
    if neutral == "subscription.created" and meta.get("key_hash"):
        data["key_hash"] = str(meta["key_hash"])
    return [{"type": neutral, "data": data}]
