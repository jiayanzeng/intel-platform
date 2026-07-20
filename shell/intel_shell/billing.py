"""Billing webhook handling: provider events -> entitlement changes.

This is the STATE.md "billing webhook (Stripe et al.) that flips `sectors`
per client" step, and it stays entirely inside the shell. A payment provider
tells us a subscription changed; we translate that into a client's entitled
sector list and persist it. The core is never involved — it keeps receiving an
explicit sector list per request and enforcing it in SQL, so even a spoofed
event can only misgrant sectors, never bypass the core's filtering.

The event shape is deliberately provider-neutral (a thin normalization layer
would sit in front of a real Stripe/Paddle payload):

    {"type": "subscription.updated",
     "data": {"client": "acme-research", "sectors": ["science", "technology"]}}

Supported `type`s: `subscription.created`, `subscription.updated`,
`subscription.deleted`, `subscription.key_rotated`. Signature verification
happens at the HTTP edge (see app.py / security.verify_webhook_signature)
before anything here runs.

`subscription.key_rotated` carries the NEW key's hash — never the key itself,
which we neither need nor want to see:

    {"type": "subscription.key_rotated",
     "data": {"client": "acme-research", "key_hash": "<hex>",
              "retire_after": 1780000000}}   # optional grace deadline

`retire_after` is an absolute unix timestamp: the old key keeps working until
then, so a client can roll a key without a flag-day cutover. Omit it and the
old key stops working immediately — which is what you want for a *leaked* key,
so revocation is just rotation with no grace.

This is the provider-NEUTRAL vocabulary. Real providers (Stripe et al.) are
normalized *into* this shape by an adapter (see `adapters/stripe.py`); nothing
provider-specific belongs in this module.
"""

from __future__ import annotations

from typing import Iterable

from .config import BaseSubscriptionStore

CREATE_EVENTS = {"subscription.created"}
UPDATE_EVENTS = {"subscription.updated"}
DELETE_EVENTS = {"subscription.deleted"}
ROTATE_EVENTS = {"subscription.key_rotated"}
KNOWN_EVENTS = CREATE_EVENTS | UPDATE_EVENTS | DELETE_EVENTS | ROTATE_EVENTS


class BillingError(ValueError):
    """The event payload was structurally invalid (bad request, not a bug)."""


def _require(data: dict, key: str) -> object:
    if key not in data:
        raise BillingError(f"event data missing required field '{key}'")
    return data[key]


def apply_event(
    store: BaseSubscriptionStore,
    event: dict,
    known_sectors: Iterable[str] | None = None,
) -> dict:
    """Apply one billing event to `store` in memory; return a result summary.

    Persistence is the caller's job (so a batch can be saved once). `event`
    must be a dict with a `type` and a `data` object. When `known_sectors` is
    provided, sectors outside that set are dropped with a warning note rather
    than granted — defense in depth against a compromised billing channel,
    on top of the core's own filtering.
    """
    etype = event.get("type")
    if not isinstance(etype, str):
        raise BillingError("event missing string 'type'")
    data = event.get("data")
    if not isinstance(data, dict):
        raise BillingError("event missing object 'data'")

    if etype not in KNOWN_EVENTS:
        return {"action": "ignored", "reason": f"unhandled event type '{etype}'"}

    client = _require(data, "client")
    if not isinstance(client, str) or not client:
        raise BillingError("'client' must be a non-empty string")

    if etype in DELETE_EVENTS:
        removed = store.remove(client)
        return {"action": "removed" if removed else "noop", "client": client}

    if etype in ROTATE_EVENTS:
        new_hash = _require(data, "key_hash")
        if not isinstance(new_hash, str) or not new_hash:
            raise BillingError("'key_hash' must be a non-empty string")
        if "api_key" in data:
            # A provider should never send us the raw key; refusing loudly is
            # better than quietly hashing it and pretending that was fine.
            raise BillingError("'api_key' must not be sent; supply 'key_hash'")
        retire_after = data.get("retire_after")
        if retire_after is not None and not isinstance(retire_after, (int, float)):
            raise BillingError("'retire_after' must be a unix timestamp")
        rotated = store.rotate_key(
            client, new_hash, retire_after=(
                float(retire_after) if retire_after is not None else None
            )
        )
        if rotated is None:
            return {"action": "noop", "client": client,
                    "reason": "unknown client; nothing to rotate"}
        return {
            "action": "key_rotated",
            "client": client,
            "grace": "none (previous keys revoked immediately)"
            if retire_after is None
            else f"previous keys valid until {retire_after}",
        }

    # created / updated both set the entitled sector list.
    raw_sectors = _require(data, "sectors")
    if not isinstance(raw_sectors, list) or not all(
        isinstance(s, str) for s in raw_sectors
    ):
        raise BillingError("'sectors' must be a list of strings")

    notes: list[str] = []
    sectors = tuple(raw_sectors)
    if known_sectors is not None:
        allowed = set(known_sectors)
        filtered = tuple(s for s in sectors if s in allowed)
        dropped = [s for s in sectors if s not in allowed]
        if dropped:
            notes.append(f"dropped unknown sector(s): {', '.join(sorted(set(dropped)))}")
        sectors = filtered

    key_hash = data.get("key_hash") if etype in CREATE_EVENTS else None
    existed = store.get(client) is not None
    store.upsert(client, sectors, key_hash=key_hash)

    result = {
        "action": "updated" if existed else "created",
        "client": client,
        "sectors": list(sectors),
    }
    if notes:
        result["notes"] = notes
    return result
