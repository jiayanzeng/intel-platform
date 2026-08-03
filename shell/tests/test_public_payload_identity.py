"""Deterministic byte witness for every configured public response route."""

from __future__ import annotations

import hashlib
import hmac
import json
import time

import httpx
from fastapi.testclient import TestClient

from intel_shell.adapters import stripe
from intel_shell.app import create_app
from intel_shell.config import Subscription
from intel_shell.core_client import CoreClient
from tools.domain_manifest import compare, derive_manifest, derive_openapi_manifest


AUTHORIZATIONS = {
    "acme": "Bearer ak_acme_7f3d9c",
    "quant": "Bearer ak_quant_2b81aa",
}
SUBSCRIPTIONS = [
    Subscription(
        client="acme-research",
        sectors=("science", "technology"),
        api_key="ak_acme_7f3d9c",
    ),
    Subscription(
        client="quant-desk",
        sectors=("finance",),
        api_key="ak_quant_2b81aa",
    ),
]
BILLING_SIGNING_FIXTURE = "public-payload-billing-fixture"
STRIPE_SIGNING_FIXTURE = "public-payload-stripe-fixture"
EXPECTED_PAYLOAD_BYTES = 6869
EXPECTED_PAYLOAD_SHA256 = (
    "dfec8ff81d68526dd5468ce22660be9d7678c6a8fdd8e52d6ac921c83371cef3"
)

VIEW = {
    "window_end": "2026-07-04",
    "documents_analyzed": 12,
    "kept_doc_ids": ["osdaily::osd-004", "techwire::tw-005"],
    "mentions": 25,
    "near_duplicates": [
        {
            "dropped_id": "techwire::tw-004",
            "kept_id": "osdaily::osd-004",
            "distance": 12,
        }
    ],
    "signals": [
        {
            "kind": "RisingEntity",
            "headline": "DeepSeek: 5 documents on 2026-07-04 vs baseline 0.0/day",
            "score": 10.0,
            "detail": "burst z-score 10.0; independently corroborated by 3 sources",
            "entity_ids": ["deepseek"],
            "evidence": [
                {
                    "doc_id": "osdaily::osd-004",
                    "title": "DeepSeek opens V4 Pro weights",
                    "url": "https://example.org/osdaily/deepseek-v4-weights",
                    "source_id": "osdaily",
                    "day": "2026-07-04",
                    "license": "IndexOnly",
                    "excerpt": None,
                },
                {
                    "doc_id": "techwire::tw-005",
                    "title": "Helios Labs raises Series A",
                    "url": "https://example.org/techwire/helios-series-a",
                    "source_id": "techwire",
                    "day": "2026-07-04",
                    "license": "CcBy",
                    "excerpt": "Helios Labs, a startup building agentic systems...",
                },
            ],
        }
    ],
    "edges": [
        {
            "a": "deepseek",
            "b": "vllm",
            "a_name": "DeepSeek",
            "b_name": "vLLM",
            "weight": 2,
            "pmi": 0.85,
        }
    ],
    "discovered": [{"surface": "Helios Labs", "doc_ids": ["a", "b"]}],
}
SEARCH = [
    {
        "doc_id": "techwire::tw-001",
        "title": "Rust data pipelines keep displacing JVM stacks",
        "sector": "technology",
        "source_id": "techwire",
        "url": "https://example.org/techwire/rust-pipelines",
        "license": "CcBy",
        "snippet": "[Rust] adoption accelerating ...",
        "rank": -1.2,
    }
]
RETRIEVE = {
    "bm25": ["arxiv-cs::oai:arXiv.org:2607.02201"],
    "vector": ["arxiv-cs::oai:arXiv.org:2607.02201"],
    "fused": ["arxiv-cs::oai:arXiv.org:2607.02201"],
    "notes": [],
    "context": [
        {
            "doc_id": "arxiv-cs::oai:arXiv.org:2607.02201",
            "sector": "science",
            "title": "DeepSeek-V4 Technical Report",
            "body": "A measured sparse routing system coordinates experts.",
            "url": "http://arxiv.org/abs/2607.02201",
            "source_id": "arxiv-cs",
            "day": "2026-07-04",
            "license": "IndexOnly",
            "authors": ["DeepSeek Research"],
            "tags": ["cs.LG"],
        }
    ],
    "suppressed": ["osdaily::osd-004"],
}


class FixedChat:
    model = "fixed-chat"

    def chat(self, _system: str, _user: str) -> str:
        return "FIXED-ANSWER grounded in [1]."


def _core(request: httpx.Request) -> httpx.Response:
    if request.url.path == "/view":
        return httpx.Response(200, json=VIEW)
    if request.url.path == "/search":
        return httpx.Response(200, json=SEARCH)
    if request.url.path == "/retrieve":
        return httpx.Response(200, json=RETRIEVE)
    if request.url.path == "/attest":
        answer = json.loads(request.content)["answer"]
        return httpx.Response(200, json={"clean_answer": answer, "violations": []})
    if request.url.path == "/sectors":
        return httpx.Response(
            200,
            json=[
                {"id": "science", "display_name": "Science", "sources": []},
                {
                    "id": "technology",
                    "display_name": "Technology",
                    "sources": [],
                },
                {"id": "finance", "display_name": "Finance", "sources": []},
            ],
        )
    return httpx.Response(404, text=f"no public-payload fixture for {request.url.path}")


def configured_payload_bytes() -> bytes:
    client = TestClient(
        create_app(
            CoreClient("http://core", transport=httpx.MockTransport(_core)),
            SUBSCRIPTIONS,
            chat=FixedChat(),
            billing_secret=BILLING_SIGNING_FIXTURE,
            stripe_secret=STRIPE_SIGNING_FIXTURE,
        )
    )
    observed: list[dict[str, object]] = []

    def capture(name: str, response) -> None:
        assert response.status_code == 200, (name, response.text)
        observed.append(
            {
                "body": response.content.decode(),
                "content_type": response.headers["content-type"],
                "name": name,
                "status": response.status_code,
            }
        )

    for subscriber, authorization in AUTHORIZATIONS.items():
        headers = {"authorization": authorization}
        capture(f"{subscriber}:signals", client.get("/v1/signals", headers=headers))
        capture(
            f"{subscriber}:search",
            client.get("/v1/search", params={"q": "rust"}, headers=headers),
        )
        capture(f"{subscriber}:brief", client.get("/v1/brief", headers=headers))
        capture(
            f"{subscriber}:ask",
            client.get("/v1/ask", params={"q": "what changed"}, headers=headers),
        )

    webhook_body = json.dumps(
        {"type": "invoice.paid", "data": {"client": "acme-research"}},
        separators=(",", ":"),
    ).encode()
    webhook_signature = hmac.new(
        BILLING_SIGNING_FIXTURE.encode(), webhook_body, hashlib.sha256
    ).hexdigest()
    capture(
        "billing:webhook",
        client.post(
            "/v1/billing/webhook",
            content=webhook_body,
            headers={"x-signature": webhook_signature},
        ),
    )

    stripe_body = json.dumps(
        {"id": "evt_public_payload", "type": "invoice.paid", "data": {}},
        separators=(",", ":"),
    ).encode()
    stripe_signature = stripe.sign(
        STRIPE_SIGNING_FIXTURE, stripe_body, int(time.time())
    )
    capture(
        "billing:stripe",
        client.post(
            "/v1/billing/stripe",
            content=stripe_body,
            headers={"stripe-signature": stripe_signature},
        ),
    )

    return json.dumps(
        observed,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode()


def test_configured_public_payloads_match_release_baseline() -> None:
    payload = configured_payload_bytes()
    assert len(payload) == EXPECTED_PAYLOAD_BYTES
    assert hashlib.sha256(payload).hexdigest() == EXPECTED_PAYLOAD_SHA256
    assert compare(
        derive_manifest("v0.17.4"), derive_openapi_manifest("v0.17.4")
    ) == []
