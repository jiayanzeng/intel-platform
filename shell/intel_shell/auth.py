"""Bearer-key auth against the shell-owned subscription config.

THE entitlement decision lives here: token -> (client, entitled sectors).
The core then enforces whatever sector list it is handed, in SQL and in
memory — so the worst a shell bug can do is grant the wrong sectors, never
bypass filtering itself. Two layers, one boundary each.

As of v0.5 keys are compared by HMAC digest with a constant-time check
(`Subscription.matches`), so the raw key never has to live on disk. A legacy
record that still carries a plaintext `api_key` is hashed on the fly, so this
change is transparent to existing config and tests. The remaining production
swaps (OAuth/JWT, a billing webhook flipping `sectors`) are still shell-side
only, core untouched.
"""

from __future__ import annotations

from typing import Iterable

from fastapi import HTTPException

from .config import Subscription


def resolve(
    subscriptions: Iterable[Subscription], authorization: str | None
) -> Subscription:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="missing bearer token")
    token = authorization.removeprefix("Bearer ").strip()
    for sub in subscriptions:
        if sub.matches(token):
            return sub
    raise HTTPException(status_code=401, detail="unknown api key")
