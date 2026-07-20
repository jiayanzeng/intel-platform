"""Provider adapters: real billing payloads -> the shell's neutral event shape.

An adapter's whole job is translation. It verifies the provider's signature
scheme, then maps the provider's vocabulary onto the neutral events that
`billing.apply_event` already understands. The neutral shape does NOT bend to
accommodate a provider — that's the point of having a seam here: swapping
Stripe for Paddle means writing a second adapter, not touching billing.py, the
store, or the entitlement model.
"""

from . import stripe

__all__ = ["stripe"]
