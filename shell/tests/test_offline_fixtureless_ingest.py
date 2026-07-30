"""Regression for G4's measured structured partial-failure disposition."""

from __future__ import annotations

import json

import httpx

from intel_shell import pipeline
from intel_shell.config import Subscription
from intel_shell.core_client import CoreClient


OFFLINE_FINANCE_INGEST = {
    "fetched": 1,
    "new": 1,
    "results": [
        {
            "sector": "finance",
            "source_id": "filings-digest",
            "ok": True,
            "documents": 1,
            "error": None,
        },
        {
            "sector": "finance",
            "source_id": "sec-edgar-usgaap",
            "ok": False,
            "documents": 0,
            "error": (
                "http: no fixture configured and binary built without "
                "the 'net' feature"
            ),
        },
    ],
}

EMPTY_FINANCE_VIEW = {
    "window_end": "2026-07-29",
    "documents_analyzed": 1,
    "kept_doc_ids": ["filings-digest::finance-001"],
    "mentions": 0,
    "near_duplicates": [],
    "signals": [],
    "edges": [],
    "discovered": [],
}


def test_offline_fixtureless_source_is_reported_and_pipeline_continues(
    monkeypatch, tmp_path, capsys
) -> None:
    requests: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request.url.path)
        if request.url.path == "/ingest":
            assert request.method == "POST"
            assert json.loads(request.content) == {"sectors": ["finance"]}
            return httpx.Response(200, json=OFFLINE_FINANCE_INGEST)
        if request.url.path == "/view":
            assert dict(request.url.params) == {"sectors": "finance"}
            return httpx.Response(200, json=EMPTY_FINANCE_VIEW)
        if request.url.path == "/signals/record":
            assert json.loads(request.content) == {
                "client": "quant-desk",
                "window_end": "2026-07-29",
                "signals": [],
            }
            return httpx.Response(200, json={"recorded": 0})
        raise AssertionError(f"unexpected core request {request.method} {request.url}")

    core = CoreClient(
        "http://core",
        transport=httpx.MockTransport(handler),
    )
    subscription = Subscription(
        client="quant-desk",
        sectors=("finance",),
        api_key="quant-test-key",
    )
    monkeypatch.setattr(
        pipeline.config,
        "load_subscriptions",
        lambda _path: [subscription],
    )
    monkeypatch.setattr(pipeline, "embed_from_env", lambda: None)
    monkeypatch.setattr(pipeline, "CoreClient", lambda *_args, **_kwargs: core)

    status = pipeline.run(
        "quant-desk",
        None,
        str(tmp_path),
        "http://core",
        llm_enrich=False,
    )
    output = capsys.readouterr()

    assert status == 0
    assert (
        "fetch  [finance / filings-digest] 1 document(s)"
        in output.out
    )
    assert (
        "error  [finance / sec-edgar-usgaap] http: no fixture configured "
        "and binary built without the 'net' feature"
        in output.out
    )
    assert "archive: +1 new this run (1 fetched)" in output.out
    assert "== analyze ==" in output.out
    assert requests == ["/ingest", "/view", "/signals/record"]
    assert (tmp_path / "brief-2026-07-29.md").is_file()
