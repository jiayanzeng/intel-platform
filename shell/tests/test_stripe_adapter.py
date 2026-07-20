"""T6b: the Stripe adapter — signature scheme + payload normalization.

Two things are being defended here. The obvious one is that a forged signature
is refused. The subtler one is that a *genuine* Stripe-signed body, captured and
replayed later, is also refused — because the timestamp is inside the signed
material precisely so we can check it, and an endpoint that ignores it will
happily re-apply an entitlement change forever.
"""

from __future__ import annotations

import json
import time

import httpx
from fastapi.testclient import TestClient

from intel_shell.adapters import stripe
from intel_shell.app import create_app
from intel_shell.config import Subscription, SubscriptionStore
from intel_shell.core_client import CoreClient
from intel_shell.security import hash_token

SECRET = "whsec_stripe_test"


def _store():
    return SubscriptionStore([
        Subscription(client="acme-research", sectors=("science", "technology"),
                     key_hash=hash_token("ak_acme_7f3d9c")),
    ])


def _fake_core(request: httpx.Request) -> httpx.Response:
    if request.url.path == "/sectors":
        return httpx.Response(200, json=[
            {"id": "science", "display_name": "Science", "sources": []},
            {"id": "technology", "display_name": "Technology", "sources": []},
            {"id": "finance", "display_name": "Finance", "sources": []},
        ])
    return httpx.Response(404, text="no fake")


def _app(store, secret=SECRET):
    core = CoreClient("http://core", transport=httpx.MockTransport(_fake_core))
    return TestClient(create_app(core, store, stripe_secret=secret))


def _event(etype: str, sectors: str = "finance", client: str = "acme-research") -> dict:
    return {
        "id": "evt_1",
        "type": etype,
        "data": {"object": {
            "id": "sub_1",
            "customer": "cus_1",
            "metadata": {"client": client, "sectors": sectors},
            "items": {"data": []},
        }},
    }


def _post(c, body: dict, *, secret=SECRET, timestamp=None, tamper=False):
    raw = json.dumps(body).encode()
    ts = int(time.time()) if timestamp is None else timestamp
    header = stripe.sign(secret, raw, ts)
    if tamper:
        raw = raw.replace(b"finance", b"science")  # signed one body, sending another
    return c.post("/v1/billing/stripe", content=raw,
                  headers={"stripe-signature": header})


# --- the signature scheme itself ------------------------------------------------


def test_valid_signature_verifies():
    raw = b'{"hello":"world"}'
    ts = int(time.time())
    assert stripe.verify_signature(SECRET, raw, stripe.sign(SECRET, raw, ts))


def test_stale_timestamp_is_refused_even_though_the_mac_is_valid():
    """The replay case: a real, correctly-signed body from an hour ago."""
    raw = b'{"hello":"world"}'
    old = int(time.time()) - 3600
    header = stripe.sign(SECRET, raw, old)
    assert stripe.verify_signature(SECRET, raw, header) is False
    # ...and it verifies fine if we pretend it's still then, proving the MAC was
    # never the problem — the freshness check is doing the work.
    assert stripe.verify_signature(SECRET, raw, header, now=old + 5) is True


def test_malformed_or_missing_signature_is_false_not_an_exception():
    raw = b"{}"
    assert stripe.verify_signature(SECRET, raw, None) is False
    assert stripe.verify_signature(SECRET, raw, "garbage") is False
    assert stripe.verify_signature(SECRET, raw, "t=notanumber,v1=abc") is False
    assert stripe.verify_signature(SECRET, raw, "t=123") is False  # no v1


def test_rolled_secret_leaves_several_v1s_and_any_valid_one_passes():
    raw = b"{}"
    ts = int(time.time())
    good = stripe.sign(SECRET, raw, ts).split("v1=")[1]
    header = f"t={ts},v1=deadbeef,v1={good}"
    assert stripe.verify_signature(SECRET, raw, header) is True


# --- mapping into the neutral vocabulary ----------------------------------------


def test_maps_subscription_events_to_neutral_shape():
    events = stripe.to_neutral_events(_event("customer.subscription.updated"))
    assert events == [{"type": "subscription.updated",
                       "data": {"client": "acme-research", "sectors": ["finance"]}}]

    deleted = stripe.to_neutral_events(_event("customer.subscription.deleted"))
    assert deleted == [{"type": "subscription.deleted",
                        "data": {"client": "acme-research"}}]


def test_unknown_event_types_are_ignored_not_errors():
    for etype in ("invoice.paid", "payment_intent.succeeded", "charge.refunded"):
        assert stripe.to_neutral_events(_event(etype)) == []


def test_sectors_can_be_derived_from_purchased_prices():
    ev = _event("customer.subscription.updated", sectors="")
    ev["data"]["object"]["metadata"] = {"client": "acme-research"}
    ev["data"]["object"]["items"] = {"data": [{"price": {"id": "price_sci"}}]}
    events = stripe.to_neutral_events(ev, price_map={"price_sci": ["science"]})
    assert events[0]["data"]["sectors"] == ["science"]


def test_client_falls_back_to_the_stripe_customer_id():
    ev = _event("customer.subscription.updated")
    ev["data"]["object"]["metadata"] = {"sectors": "finance"}
    assert stripe.to_neutral_events(ev)[0]["data"]["client"] == "cus_1"


# --- through the HTTP edge ------------------------------------------------------


def test_signed_stripe_event_flips_sectors():
    store = _store()
    c = _app(store)
    r = _post(c, _event("customer.subscription.updated", sectors="finance"))
    assert r.status_code == 200
    assert r.json()["results"][0]["action"] == "updated"
    assert store.get("acme-research").sectors == ("finance",)


def test_tampered_body_is_401():
    store = _store()
    c = _app(store)
    assert _post(c, _event("customer.subscription.updated"), tamper=True).status_code == 401
    assert store.get("acme-research").sectors == ("science", "technology")  # untouched


def test_stale_timestamp_is_401_at_the_edge():
    store = _store()
    c = _app(store)
    r = _post(c, _event("customer.subscription.updated"),
              timestamp=int(time.time()) - 3600)
    assert r.status_code == 401
    assert store.get("acme-research").sectors == ("science", "technology")


def test_wrong_secret_is_401():
    c = _app(_store())
    assert _post(c, _event("customer.subscription.updated"),
                 secret="whsec_attacker").status_code == 401


def test_disabled_without_secret():
    c = _app(_store(), secret=None)
    assert _post(c, _event("customer.subscription.updated")).status_code == 503


def test_unhandled_stripe_event_is_acknowledged_not_500():
    """A 500 here is how a provider decides to disable your endpoint."""
    c = _app(_store())
    r = _post(c, _event("invoice.paid"))
    assert r.status_code == 200
    assert r.json()["results"][0]["action"] == "ignored"


def test_unknown_sector_from_stripe_is_dropped_by_the_allow_list():
    """Defense in depth: the core's sector list still bounds what billing grants."""
    store = _store()
    c = _app(store)
    r = _post(c, _event("customer.subscription.updated", sectors="finance,atlantis"))
    assert r.status_code == 200
    assert store.get("acme-research").sectors == ("finance",)
    assert "atlantis" in r.json()["results"][0]["notes"][0]
