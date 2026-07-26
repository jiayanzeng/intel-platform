"""Failure-capable checks for the real-model verifier's public HC1 audit."""

import json

import tools.verify_llm as verify_llm
from intel_shell.config import Subscription
from intel_shell.llm import LlmError
from tools.verify_llm import (
    ADVERSARIAL_SHAPES,
    ATTEST_NGRAM,
    ATTEST_REFUSAL,
    GUARD_FIRED,
    LEAK,
    NOT_EXERCISED,
    _adversarial_prompt,
    _aggregate_adversarial_outcomes,
    _embedding_items,
    _finish,
    _has_gated_overlap,
    _new_adversarial_report,
    _RecordingCore,
    _record_adversarial_outcome,
    _resume_valid_attempts,
    run_classifier_control,
)


def test_verifier_uses_the_real_missing_queue_doc_id_shape() -> None:
    batch = [{"doc_id": "source::one", "title": "one", "body": "body"}]

    assert _embedding_items(batch, [[0.25, 0.75]]) == [
        {"doc_id": "source::one", "vector": [0.25, 0.75]}
    ]


def test_verifier_detects_a_deliberate_public_gated_overlap() -> None:
    gated = " ".join(f"gated{i}" for i in range(ATTEST_NGRAM + 4))
    docs = [{"license": "IndexOnly", "body": gated}]
    leaking_answer = "analysis " + gated + " conclusion"

    assert _has_gated_overlap(leaking_answer, docs) is True


def test_adversarial_leak_control_fails_the_verifier(capsys) -> None:
    gated = " ".join(f"gated{i}" for i in range(ATTEST_NGRAM + 4))
    leaking_answer = "verbatim " + gated
    docs = [
        {
            "doc_id": "source::gated",
            "license": "IndexOnly",
            "body": gated,
        }
    ]
    verify_llm.results.clear()

    outcome = _record_adversarial_outcome(
        public_answer=leaking_answer,
        raw_answer=leaking_answer,
        docs=docs,
        attestation={"clean_answer": leaking_answer, "violations": []},
    )

    assert outcome == LEAK
    assert _finish() == 1
    output = capsys.readouterr().out
    assert "[FAIL] adversarial HC1 guard" in output
    assert "LEAK" in output
    assert "source::gated" in output


def test_adversarial_guard_fired_records_violation(capsys) -> None:
    gated = " ".join(f"gated{i}" for i in range(ATTEST_NGRAM + 4))
    docs = [
        {
            "doc_id": "source::gated",
            "license": "IndexOnly",
            "body": gated,
        }
    ]
    verify_llm.results.clear()

    outcome = _record_adversarial_outcome(
        public_answer=ATTEST_REFUSAL,
        raw_answer=gated,
        docs=docs,
        attestation={
            "clean_answer": ATTEST_REFUSAL,
            "violations": [{"doc_id": "source::gated"}],
        },
    )

    assert outcome == GUARD_FIRED
    assert verify_llm.results[-1][1] == verify_llm.PASS
    output = capsys.readouterr().out
    assert "GUARD FIRED" in output
    assert "violations: ['source::gated']" in output


def test_adversarial_paraphrase_is_not_exercised(capsys) -> None:
    gated = " ".join(f"gated{i}" for i in range(ATTEST_NGRAM + 4))
    docs = [
        {
            "doc_id": "source::gated",
            "license": "IndexOnly",
            "body": gated,
        }
    ]
    paraphrase = "The model summarized the passage without quoting it."
    verify_llm.results.clear()

    outcome = _record_adversarial_outcome(
        public_answer=paraphrase,
        raw_answer=paraphrase,
        docs=docs,
        attestation={"clean_answer": paraphrase, "violations": []},
    )

    assert outcome == NOT_EXERCISED
    assert verify_llm.results[-1][1] == verify_llm.WARN
    assert "NOT EXERCISED" in capsys.readouterr().out


def test_adversarial_battery_is_declared_as_five_distinct_shapes() -> None:
    ids = [shape["id"] for shape in ADVERSARIAL_SHAPES]
    assert ids == [
        "verbatim-quotation",
        "sentence-continuation",
        "translation-round-trip",
        "formatted-extraction",
        "chunked-reconstruction",
    ]
    prompts = {
        _adversarial_prompt(shape, {"title": "Target title"})
        for shape in ADVERSARIAL_SHAPES
    }
    assert len(prompts) == 5


def test_adversarial_aggregate_is_not_exercised_only_when_every_attempt_is() -> None:
    assert _aggregate_adversarial_outcomes(
        [{"outcome": NOT_EXERCISED}, {"outcome": NOT_EXERCISED}]
    ) == NOT_EXERCISED
    assert _aggregate_adversarial_outcomes(
        [{"outcome": NOT_EXERCISED}, {"outcome": GUARD_FIRED}]
    ) == GUARD_FIRED
    assert _aggregate_adversarial_outcomes(
        [{"outcome": GUARD_FIRED}, {"outcome": LEAK}]
    ) == LEAK
    assert verify_llm._adversarial_aggregate_status(
        NOT_EXERCISED,
        {
            "outcome": GUARD_FIRED,
            "valid_attempt": True,
            "raw_overlap": True,
            "public_overlap": False,
            "violation_doc_ids": ["source::gated"],
        },
    ) == verify_llm.WARN


def test_adversarial_aggregate_missing_positive_control_is_failure() -> None:
    assert verify_llm._adversarial_aggregate_status(
        NOT_EXERCISED,
        None,
    ) == verify_llm.FAIL
    assert verify_llm._adversarial_aggregate_status(
        NOT_EXERCISED,
        {"outcome": NOT_EXERCISED},
    ) == verify_llm.FAIL


def test_gated_match_telemetry_reports_graduated_near_misses() -> None:
    gated = " ".join(f"token{index}" for index in range(24))
    answer = " ".join(f"token{index}" for index in range(5, 20))
    telemetry = verify_llm._gated_match_telemetry(
        answer,
        [{"license": "IndexOnly", "body": gated}],
    )

    assert telemetry == {
        "longest_common_gated_token_run": 15,
        "matching_ngram_counts": {"8": 8, "12": 4, "16": 0},
    }


def test_real_path_positive_control_fires_the_deployed_handler() -> None:
    gated = " ".join(f"gated{index}" for index in range(24)) + "."
    target = {
        "doc_id": "source::gated",
        "sector": "science",
        "title": "Gated source",
        "body": gated,
        "url": "https://example.test/gated",
        "source_id": "source",
        "day": "2026-07-26",
        "license": "IndexOnly",
        "authors": [],
        "tags": [],
    }

    class CoreDouble:
        def retrieve(self, *args, **kwargs) -> dict:
            return {
                "bm25": [target["doc_id"]],
                "vector": [target["doc_id"]],
                "fused": [target["doc_id"]],
                "notes": [],
                "context": [target],
                "suppressed": [],
            }

        def docs(self, ids: list[str]) -> list[dict]:
            return [target] if target["doc_id"] in ids else []

        def attest(self, answer: str, ids: list[str]) -> dict:
            assert ids == [target["doc_id"]]
            assert gated.rstrip(".") in answer
            return {
                "clean_answer": ATTEST_REFUSAL,
                "violations": [{"doc_id": target["doc_id"]}],
            }

    class EmbedDouble:
        model = "embed-model"

        def embed(self, texts: list[str]) -> list[list[float]]:
            return [[0.0, 1.0] for _ in texts]

    control = verify_llm._run_real_path_positive_control(
        core=CoreDouble(),
        subscriptions=[
            Subscription(
                client="acme-research",
                sectors=("science", "technology"),
                api_key="ak_acme_7f3d9c",
            )
        ],
        embed=EmbedDouble(),
        gated_docs=[target],
    )

    assert control["outcome"] == GUARD_FIRED
    assert control["model_completed"] is True
    assert control["target_in_context"] is True
    assert control["raw_overlap"] is True
    assert control["public_overlap"] is False
    assert control["gated_match_telemetry"]["matching_ngram_counts"]["16"] > 0


def test_classifier_control_demonstrates_all_three_values(capsys) -> None:
    assert run_classifier_control() == 0
    output = capsys.readouterr().out
    assert "tools/mock_openai.py --leak plus core refusal" in output
    assert "deliberately unattested public path" in output
    assert GUARD_FIRED in output
    assert NOT_EXERCISED in output
    assert LEAK in output


def test_resume_reuses_only_valid_attempts(tmp_path) -> None:
    docs = [{"doc_id": "source::gated", "license": "IndexOnly"}]
    prior = _new_adversarial_report(
        chat_model="chat-model",
        embed_model="embed-model",
        gated_docs=docs,
    )
    prior["attempts"] = [
        {
            "target_doc_id": "source::gated",
            "shape": "verbatim-quotation",
            "target_in_context": True,
            "model_completed": True,
            "valid_attempt": True,
            "outcome": NOT_EXERCISED,
        },
        {
            "target_doc_id": "source::gated",
            "shape": "chunked-reconstruction",
            "target_in_context": True,
            "model_completed": False,
            "valid_attempt": False,
            "outcome": NOT_EXERCISED,
        },
    ]
    path = tmp_path / "prior.json"
    path.write_text(json.dumps(prior))
    resumed = _new_adversarial_report(
        chat_model="chat-model",
        embed_model="embed-model",
        gated_docs=docs,
    )

    keys = _resume_valid_attempts(path, resumed)

    assert keys == {("source::gated", "verbatim-quotation")}
    assert len(resumed["attempts"]) == 1
    assert resumed["counts"][NOT_EXERCISED] == 1
    assert resumed["resume"]["reused_valid_attempts"] == 1
    assert resumed["resume"]["retried_invalid_attempts"] == 1


def test_resume_retries_a_completed_flag_it_cannot_verify(tmp_path) -> None:
    docs = [{"doc_id": "source::gated", "license": "IndexOnly"}]
    prior = _new_adversarial_report(
        chat_model="chat-model",
        embed_model="embed-model",
        gated_docs=docs,
    )
    prior["attempts"] = [
        {
            "target_doc_id": "source::gated",
            "shape": "verbatim-quotation",
            "target_in_context": True,
            "model_completed": False,
            "valid_attempt": True,
            "outcome": NOT_EXERCISED,
        },
        {
            "target_doc_id": "source::gated",
            "shape": "chunked-reconstruction",
            "target_in_context": True,
            "valid_attempt": True,
            "outcome": NOT_EXERCISED,
        },
    ]
    path = tmp_path / "stale-prior.json"
    path.write_text(json.dumps(prior))
    resumed = _new_adversarial_report(
        chat_model="chat-model",
        embed_model="embed-model",
        gated_docs=docs,
    )

    keys = _resume_valid_attempts(path, resumed)

    assert keys == set()
    assert resumed["attempts"] == []
    assert resumed["resume"]["reused_valid_attempts"] == 0
    assert resumed["resume"]["retried_invalid_attempts"] == 2


def test_gateway_timeout_is_not_a_valid_attempt() -> None:
    target = {
        "doc_id": "source::gated",
        "title": "Gated source",
        "license": "IndexOnly",
        "body": " ".join(f"gated{index}" for index in range(24)),
    }

    class RecordingCoreDouble:
        last_retrieve_context_ids: list[str] = []

        def docs(self, ids: list[str]) -> list[dict]:
            return [target] if ids else []

    core = RecordingCoreDouble()

    class GatewayTimeoutApi:
        def get(self, *args, **kwargs):
            core.last_retrieve_context_ids = [target["doc_id"]]
            return type("Response", (), {"status_code": 502})()

    recording_chat = type("RecordingChat", (), {"last_answer": None})()
    verify_llm.results.clear()

    report = verify_llm._run_adversarial_battery(
        api=GatewayTimeoutApi(),
        core=core,
        recording_chat=recording_chat,
        gated_docs=[target],
        chat_model="chat-model",
        embed_model="embed-model",
        report_path=None,
        resume_from=None,
    )

    assert all(attempt["model_completed"] is False for attempt in report["attempts"])
    assert all(attempt["target_in_context"] is True for attempt in report["attempts"])
    assert all(attempt["valid_attempt"] is False for attempt in report["attempts"])
    assert (
        "adversarial battery coverage",
        verify_llm.FAIL,
    ) in {(name, status) for name, status, _ in verify_llm.results}


def test_recording_core_retains_context_when_downstream_work_fails() -> None:
    class Delegate:
        def retrieve(self, *args, **kwargs) -> dict:
            return {
                "context": [
                    {"doc_id": "source::target"},
                    {"doc_id": "source::other"},
                ]
            }

        def health(self) -> dict:
            return {"ok": True}

    core = _RecordingCore(Delegate())

    assert core.retrieve("query", ["science"])["context"]
    assert core.last_retrieve_context_ids == [
        "source::target",
        "source::other",
    ]
    assert core.health() == {"ok": True}


def test_verifier_ignores_short_or_redistributable_overlap() -> None:
    short = " ".join(f"token{i}" for i in range(ATTEST_NGRAM - 1))
    assert _has_gated_overlap(short, [{"license": "IndexOnly", "body": short}]) is False

    long = " ".join(f"public{i}" for i in range(ATTEST_NGRAM + 4))
    assert _has_gated_overlap(long, [{"license": "CcBy", "body": long}]) is False


def test_verifier_stops_after_failed_embedding_prerequisite(
    monkeypatch,
    capsys,
) -> None:
    class FailingEmbed:
        base_url = "https://embed.test/v1"
        model = "embed-model"
        timeout_seconds = 3.0

        def __init__(self) -> None:
            self.calls = 0

        def embed(self, texts: list[str]) -> list[list[float]]:
            self.calls += 1
            raise LlmError("embeddings endpoint error: HTTP 503")

    class CallableChat:
        base_url = "https://chat.test/v1"
        model = "chat-model"
        timeout_seconds = 3.0

        def chat(self, system: str, user: str) -> str:
            raise AssertionError("chat must not run after embedding failure")

    class FixtureCore:
        def embeddings_missing(self, model: str) -> list[dict]:
            return [{"doc_id": "source::one", "body": "fixture body"}]

    embed = FailingEmbed()
    monkeypatch.setattr(verify_llm, "CoreClient", lambda *args, **kwargs: FixtureCore())
    monkeypatch.setattr(verify_llm, "chat_from_env", lambda: CallableChat())
    monkeypatch.setattr(verify_llm, "embed_from_env", lambda: embed)

    def forbidden_public_api(app):
        raise AssertionError("public API must not run after embedding failure")

    monkeypatch.setattr(verify_llm, "TestClient", forbidden_public_api)

    assert verify_llm.main() == 1
    assert embed.calls == 1
    assert "stopping before fusion/public HC1" in capsys.readouterr().out


def test_verifier_rejects_a_fresh_database_that_is_already_preembedded(
    monkeypatch,
    capsys,
) -> None:
    class ForbiddenEmbed:
        base_url = "https://embed.test/v1"
        model = "shared-model"
        timeout_seconds = 3.0

        def embed(self, texts: list[str]) -> list[list[float]]:
            raise AssertionError(
                "fusion/public stages must not run after a zero-request backfill"
            )

    class CallableChat:
        base_url = "https://chat.test/v1"
        model = "chat-model"
        timeout_seconds = 3.0

    class PreembeddedCore:
        def embeddings_missing(self, model: str) -> list[dict]:
            return []

    monkeypatch.setattr(
        verify_llm,
        "CoreClient",
        lambda *args, **kwargs: PreembeddedCore(),
    )
    monkeypatch.setattr(verify_llm, "chat_from_env", lambda: CallableChat())
    monkeypatch.setattr(verify_llm, "embed_from_env", lambda: ForbiddenEmbed())

    assert verify_llm.main() == 1
    output = capsys.readouterr().out
    assert "[FAIL] embeddings backfill" in output
    assert "0 real embedding request" in output
    assert "stopping before fusion/public HC1" in output


def test_verifier_interrupt_exits_cleanly(monkeypatch, capsys) -> None:
    def interrupted() -> int:
        raise KeyboardInterrupt

    monkeypatch.setattr(verify_llm, "main", interrupted)

    assert verify_llm.cli([]) == 130
    captured = capsys.readouterr()
    assert "verification interrupted; cleanup follows." in captured.err
    assert "Traceback" not in captured.err
