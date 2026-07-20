"""Shell tests against a FAKE core (httpx.MockTransport).

The point being proven: the whole shell — auth, mapping, prompt assembly,
brief rendering — is testable without a Rust toolchain anywhere in sight.
That is what the seam buys.
"""

from __future__ import annotations

import json

import httpx
import pytest
from fastapi.testclient import TestClient

from intel_shell import prompts
from intel_shell.app import create_app
from intel_shell.briefing import render_brief
from intel_shell.config import Subscription
from intel_shell.core_client import CoreClient
from tools.mock_openai import chat_content

# --- canned core responses ------------------------------------------------------

FAKE_VIEW = {
    "window_end": "2026-07-04",
    "documents_analyzed": 12,
    "kept_doc_ids": ["osdaily::osd-004", "techwire::tw-005"],
    "mentions": 25,
    "near_duplicates": [
        {"dropped_id": "techwire::tw-004", "kept_id": "osdaily::osd-004", "distance": 12}
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
                    "excerpt": None,  # gated BY THE CORE
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
        {"a": "deepseek", "b": "vllm", "a_name": "DeepSeek", "b_name": "vLLM",
         "weight": 2, "pmi": 0.85}
    ],
    "discovered": [{"surface": "Helios Labs", "doc_ids": ["a", "b"]}],
}

FAKE_SEARCH = [
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

GATED_SENTENCE = (
    "The newly measured sparse routing system coordinates many specialized experts "
    "while preserving stable token assignments across long analytical workloads at "
    "deployment scale."
)
ATTEST_REFUSAL = (
    "Answer withheld because it reproduced non-redistributable source text."
)

FAKE_RETRIEVE = {
    "bm25": ["arxiv-cs::oai:arXiv.org:2607.02201"],
    "vector": ["arxiv-cs::oai:arXiv.org:2607.02201"],
    "fused": ["arxiv-cs::oai:arXiv.org:2607.02201"],
    "notes": [],
    "context": [
        {
            "doc_id": "arxiv-cs::oai:arXiv.org:2607.02201",
            "sector": "science",
            "title": "DeepSeek-V4 Technical Report",
            "body": GATED_SENTENCE + " x" * 600,
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


def fake_core_handler(request: httpx.Request) -> httpx.Response:
    path = request.url.path
    if path == "/health":
        return httpx.Response(200, json={"status": "ok", "documents": 14, "version": "0.4.0"})
    if path == "/view":
        # the shell must pass the entitled sectors through
        assert "sectors" in dict(request.url.params)
        return httpx.Response(200, json=FAKE_VIEW)
    if path == "/search":
        return httpx.Response(200, json=FAKE_SEARCH)
    if path == "/retrieve":
        body = json.loads(request.content)
        assert body["sectors"], "shell must send explicit sectors"
        return httpx.Response(200, json=FAKE_RETRIEVE)
    if path == "/attest":
        body = json.loads(request.content)
        assert body["context_doc_ids"] == [
            "arxiv-cs::oai:arXiv.org:2607.02201"
        ]
        violations = []
        clean_answer = body["answer"]
        if GATED_SENTENCE in body["answer"]:
            violations.append({"doc_id": body["context_doc_ids"][0]})
            clean_answer = ATTEST_REFUSAL
        return httpx.Response(
            200,
            json={"clean_answer": clean_answer, "violations": violations},
        )
    return httpx.Response(404, text=f"no fake for {path}")


class FakeChat:
    model = "fake-chat"

    def chat(self, system: str, user: str) -> str:
        assert "intelligence platform" in system
        assert "QUESTION:" in user
        return "FAKE-ANSWER grounded in [1]."


class LeakingMockChat:
    model = "mock-leak"

    def chat(self, system: str, user: str) -> str:
        return chat_content(user, leak=True)


SUBS = [
    Subscription(client="acme-research", sectors=("science", "technology"),
                 api_key="ak_acme_7f3d9c"),
    Subscription(client="quant-desk", sectors=("finance",), api_key="ak_quant_2b81aa"),
]


def make_client(chat=None) -> TestClient:
    core = CoreClient("http://core", transport=httpx.MockTransport(fake_core_handler))
    return TestClient(create_app(core, SUBS, chat=chat))


AUTH = {"Authorization": "Bearer ak_acme_7f3d9c"}


# --- tests --------------------------------------------------------------------


def test_missing_key_is_401():
    c = make_client()
    assert c.get("/v1/signals").status_code == 401
    assert c.get("/v1/signals", headers={"Authorization": "Bearer nope"}).status_code == 401


def test_signals_maps_core_view():
    c = make_client()
    r = c.get("/v1/signals", headers=AUTH)
    assert r.status_code == 200
    body = r.json()
    assert body["client"] == "acme-research"
    assert body["sectors"] == ["science", "technology"]
    assert body["near_duplicates_collapsed"] == 1
    assert body["signals"][0]["kind"] == "RisingEntity"
    assert body["graph"][0]["a_name"] == "DeepSeek"


def test_search_passthrough_preserves_license_gate():
    c = make_client()
    r = c.get("/v1/search", params={"q": "rust"}, headers=AUTH)
    assert r.status_code == 200
    hits = r.json()["hits"]
    assert hits[0]["snippet"].startswith("[Rust]")  # CcBy -> snippet served


def test_brief_renders_markdown_and_respects_gate():
    c = make_client()
    r = c.get("/v1/brief", headers=AUTH)
    assert r.status_code == 200
    text = r.text
    assert text.startswith("# Intelligence Brief")
    # IndexOnly evidence: the withheld line appears; CcBy evidence: excerpt appears
    assert "excerpt withheld (IndexOnly license)" in text
    assert '"Helios Labs, a startup building agentic systems..."' in text


def test_ask_503_without_chat_client():
    c = make_client(chat=None)
    r = c.get("/v1/ask", params={"q": "anything"}, headers=AUTH)
    assert r.status_code == 503
    assert "LLM_BASE_URL" in r.json()["detail"]


def test_ask_builds_citations_and_answer():
    c = make_client(chat=FakeChat())
    r = c.get("/v1/ask", params={"q": "what is happening with sparse attention"},
              headers=AUTH)
    assert r.status_code == 200
    body = r.json()
    assert body["answer"].startswith("FAKE-ANSWER")
    assert body["citations"][0]["ref"] == "[1]"
    assert body["citations"][0]["license"] == "IndexOnly"
    assert body["context_suppressed"] == ["osdaily::osd-004"]
    assert body["retrieval"]["fused"] == ["arxiv-cs::oai:arXiv.org:2607.02201"]


def test_ask_refuses_the_deliberately_leaking_mock():
    context, _ = prompts.build_context(FAKE_RETRIEVE["context"])
    leaking_answer = chat_content(
        prompts.build_ask_user("what changed", context), leak=True
    )
    assert GATED_SENTENCE in leaking_answer, "negative control must actually leak"

    c = make_client(chat=LeakingMockChat())
    r = c.get("/v1/ask", params={"q": "what changed"}, headers=AUTH)

    assert r.status_code == 200
    body = r.json()
    assert body["answer"] == ATTEST_REFUSAL
    assert GATED_SENTENCE not in body["answer"]


def test_build_context_caps_body_and_numbers_refs():
    context, citations = prompts.build_context(FAKE_RETRIEVE["context"])
    assert context.startswith("[1] DeepSeek-V4 Technical Report")
    # body capped at BODY_CAP chars
    body_part = context.split("\n", 1)[1]
    assert len(body_part) <= prompts.BODY_CAP + 10
    assert citations[0]["doc_id"] == "arxiv-cs::oai:arXiv.org:2607.02201"


def test_render_brief_footer_and_kind_tags():
    text = render_brief("acme-research", ["science", "technology"], FAKE_VIEW, new_n=3)
    assert "[RISING]" in text
    assert "+3 ingested this run" in text
    assert text.rstrip().endswith("which is the product.")


def test_quant_desk_gets_its_own_sectors():
    c = make_client()
    r = c.get("/v1/signals", headers={"Authorization": "Bearer ak_quant_2b81aa"})
    assert r.status_code == 200
    assert r.json()["sectors"] == ["finance"]
