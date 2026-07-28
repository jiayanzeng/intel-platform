from __future__ import annotations

from intel_shell import pipeline
from intel_shell.config import Subscription
from intel_shell.core_client import CoreError


class CandidateChat:
    model = "candidate-test"

    def chat(self, _system: str, _user: str) -> str:
        return (
            '{"entities":['
            '{"name":"Known Name","kind":"Org"},'
            '{"name":"Novel Entity","kind":"Org"}'
            "]}"
        )


class FakeCore:
    def __init__(self, fail_comparison: bool = False):
        self.fail_comparison = fail_comparison
        self.compared: list[str] | None = None

    def view(self, _sectors: list[str]) -> dict:
        return {
            "window_end": "2026-07-28",
            "documents_analyzed": 1,
            "kept_doc_ids": ["technology::one"],
            "mentions": 0,
            "near_duplicates": [],
            "signals": [],
            "edges": [],
            "discovered": [],
        }

    def record_signals(
        self, _client: str, _window_end: str | None, _signals: list[dict]
    ) -> dict:
        return {"recorded": 0}

    def docs(self, _ids: list[str], _sectors: list[str]) -> list[dict]:
        return [
            {
                "doc_id": "technology::one",
                "title": "Candidate document",
                "body": "Candidate body",
            }
        ]

    def unknown_entities(self, names: list[str]) -> list[str]:
        self.compared = names
        if self.fail_comparison:
            raise CoreError("gazetteer unavailable")
        return ["Novel Entity"]


def test_pipeline_uses_core_entity_comparison_and_fails_closed(
    monkeypatch, tmp_path, capsys
) -> None:
    subscription = Subscription(
        client="candidate-client",
        sectors=("technology",),
        api_key="candidate-key",
    )
    monkeypatch.setattr(
        pipeline.config, "load_subscriptions", lambda _path: [subscription]
    )
    monkeypatch.setattr(pipeline, "embed_from_env", lambda: None)
    monkeypatch.setattr(pipeline, "chat_from_env", CandidateChat)
    monkeypatch.setattr(
        pipeline.briefing,
        "render_brief",
        lambda *_args, **_kwargs: "candidate brief",
    )

    core = FakeCore()
    monkeypatch.setattr(pipeline, "CoreClient", lambda *_args, **_kwargs: core)
    assert (
        pipeline.run(
            "candidate-client",
            None,
            str(tmp_path),
            "http://core",
            llm_enrich=True,
            skip_ingest=True,
        )
        == 0
    )
    output = capsys.readouterr()
    assert core.compared == ["Known Name", "Novel Entity"]
    assert "Novel Entity  (seen 1x)" in output.out
    assert "Known Name  (seen" not in output.out

    failing_core = FakeCore(fail_comparison=True)
    monkeypatch.setattr(
        pipeline, "CoreClient", lambda *_args, **_kwargs: failing_core
    )
    assert (
        pipeline.run(
            "candidate-client",
            None,
            str(tmp_path),
            "http://core",
            llm_enrich=True,
            skip_ingest=True,
        )
        == 1
    )
    output = capsys.readouterr()
    assert failing_core.compared == ["Known Name", "Novel Entity"]
    assert "entity comparison failed: gazetteer unavailable" in output.err
