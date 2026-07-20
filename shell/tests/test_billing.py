"""Tests for billing: pure event application + the signed webhook endpoint."""

from __future__ import annotations

import hashlib
import hmac
import json

import httpx
import pytest
from fastapi.testclient import TestClient

from intel_shell import billing
from intel_shell.app import create_app
from intel_shell.config import Subscription, SubscriptionStore
from intel_shell.core_client import CoreClient

SECRET = "whsec_test"


def _store():
    return SubscriptionStore(
        [
            Subscription(client="acme-research", sectors=("science", "technology"),
                         api_key="ak_acme_7f3d9c"),
            Subscription(client="quant-desk", sectors=("finance",),
                         api_key="ak_quant_2b81aa"),
        ]
    )


# --- pure apply_event -----------------------------------------------------------


def test_update_changes_sectors():
    store = _store()
    r = billing.apply_event(
        store,
        {"type": "subscription.updated",
         "data": {"client": "acme-research", "sectors": ["science"]}},
    )
    assert r["action"] == "updated"
    assert store.get("acme-research").sectors == ("science",)


def test_create_provisions_new_client_with_key_hash():
    store = _store()
    r = billing.apply_event(
        store,
        {"type": "subscription.created",
         "data": {"client": "new-co", "sectors": ["finance"], "key_hash": "abc123"}},
    )
    assert r["action"] == "created"
    sub = store.get("new-co")
    assert sub.sectors == ("finance",)
    assert sub.key_hash == "abc123"


def test_delete_removes_client():
    store = _store()
    r = billing.apply_event(
        store, {"type": "subscription.deleted", "data": {"client": "quant-desk"}}
    )
    assert r["action"] == "removed"
    assert store.get("quant-desk") is None


def test_unknown_event_type_is_ignored():
    store = _store()
    r = billing.apply_event(store, {"type": "invoice.paid", "data": {"client": "x"}})
    assert r["action"] == "ignored"


def test_unknown_sectors_are_dropped_when_allowlist_given():
    store = _store()
    r = billing.apply_event(
        store,
        {"type": "subscription.updated",
         "data": {"client": "acme-research", "sectors": ["science", "made-up"]}},
        known_sectors=["science", "technology", "finance"],
    )
    assert store.get("acme-research").sectors == ("science",)
    assert any("made-up" in n for n in r.get("notes", []))


def test_malformed_event_raises_billing_error():
    store = _store()
    with pytest.raises(billing.BillingError):
        billing.apply_event(store, {"type": "subscription.updated", "data": {}})
    with pytest.raises(billing.BillingError):
        billing.apply_event(store, {"data": {"client": "x"}})  # no type


# --- the webhook endpoint -------------------------------------------------------


def _fake_core_handler(request: httpx.Request) -> httpx.Response:
    if request.url.path == "/sectors":
        return httpx.Response(200, json=[
            {"id": "science", "display_name": "Science", "sources": []},
            {"id": "technology", "display_name": "Technology", "sources": []},
            {"id": "finance", "display_name": "Finance", "sources": []},
        ])
    if request.url.path == "/view":
        return httpx.Response(200, json={"signals": [], "edges": []})
    return httpx.Response(404, text="no fake")


def _app(store, secret=SECRET):
    core = CoreClient("http://core", transport=httpx.MockTransport(_fake_core_handler))
    return TestClient(create_app(core, store, billing_secret=secret))


def _signed(body: dict) -> tuple[bytes, dict]:
    raw = json.dumps(body).encode()
    sig = hmac.new(SECRET.encode(), raw, hashlib.sha256).hexdigest()
    return raw, {"x-signature": sig}


def test_webhook_disabled_without_secret():
    c = _app(_store(), secret=None)
    raw, headers = _signed({"type": "subscription.deleted", "data": {"client": "x"}})
    assert c.post("/v1/billing/webhook", content=raw, headers=headers).status_code == 503


def test_webhook_rejects_bad_signature():
    c = _app(_store())
    raw = json.dumps({"type": "subscription.deleted", "data": {"client": "x"}}).encode()
    r = c.post("/v1/billing/webhook", content=raw, headers={"x-signature": "nope"})
    assert r.status_code == 401


def test_webhook_applies_signed_event_and_affects_auth():
    store = _store()
    c = _app(store)
    # Downgrade acme to science-only via a signed event.
    raw, headers = _signed(
        {"type": "subscription.updated",
         "data": {"client": "acme-research", "sectors": ["science"]}}
    )
    r = c.post("/v1/billing/webhook", content=raw, headers=headers)
    assert r.status_code == 200
    assert r.json()["results"][0]["action"] == "updated"
    # The change is live: /v1/signals now reports the reduced sector list.
    s = c.get("/v1/signals", headers={"Authorization": "Bearer ak_acme_7f3d9c"})
    assert s.json()["sectors"] == ["science"]


def test_webhook_batch_events():
    store = _store()
    c = _app(store)
    raw, headers = _signed({"events": [
        {"type": "subscription.deleted", "data": {"client": "quant-desk"}},
        {"type": "subscription.created",
         "data": {"client": "new-co", "sectors": ["finance"], "key_hash": "zzz"}},
    ]})
    r = c.post("/v1/billing/webhook", content=raw, headers=headers)
    assert r.status_code == 200
    assert r.json()["received"] == 2
    assert store.get("quant-desk") is None
    assert store.get("new-co").sectors == ("finance",)


def test_webhook_persists_to_disk(tmp_path):
    # A store bound to a path should write the change through.
    path = tmp_path / "subs.json"
    path.write_text(json.dumps({"subscriptions": [
        {"client": "acme-research", "sectors": ["science", "technology"],
         "key_hash": "h"}
    ]}))
    from intel_shell.config import load_subscription_store
    store = load_subscription_store(str(path))
    c = _app(store)
    raw, headers = _signed(
        {"type": "subscription.updated",
         "data": {"client": "acme-research", "sectors": ["technology"]}}
    )
    assert c.post("/v1/billing/webhook", content=raw, headers=headers).status_code == 200
    on_disk = json.loads(path.read_text())
    acme = next(s for s in on_disk["subscriptions"] if s["client"] == "acme-research")
    assert acme["sectors"] == ["technology"]
    assert "api_key" not in acme  # never written back in the clear
