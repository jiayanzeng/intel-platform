"""Failure-capable checks for the real-model verifier's public HC1 audit."""

import json
from pathlib import Path

import pytest

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


def _completed_resume_attempt(
    *,
    shape: str = "verbatim-quotation",
    outcome: str = NOT_EXERCISED,
    http_status: int = 200,
) -> dict:
    return {
        "target_doc_id": "source::gated",
        "shape": shape,
        "endpoint_role": "chat",
        "model": "chat-model",
        "latency_ms": 12.5,
        "http_status": http_status,
        "model_completed": True,
        "target_in_context": True,
        "context_doc_ids": ["source::gated"],
        "gated_context_doc_ids": ["source::gated"],
        "violation_doc_ids": [],
        "raw_overlap": False,
        "public_overlap": outcome == LEAK,
        "outcome": outcome,
        "valid_attempt": True,
        "gated_match_telemetry": {
            "longest_common_gated_token_run": 0,
            "matching_ngram_counts": {"8": 0, "12": 0, "16": 0},
        },
        "transport_retry_count": 0,
    }


def _resume_one_attempt(tmp_path, attempt: dict) -> dict:
    docs = [{"doc_id": "source::gated", "license": "IndexOnly"}]
    prior = _new_adversarial_report(
        chat_model="chat-model",
        embed_model="embed-model",
        gated_docs=docs,
    )
    prior["attempts"] = [attempt]
    path = tmp_path / "contradictory-prior.json"
    path.write_text(json.dumps(prior))
    resumed = _new_adversarial_report(
        chat_model="chat-model",
        embed_model="embed-model",
        gated_docs=docs,
    )

    with pytest.raises(
        verify_llm.ResumedAttemptInvariantError,
        match="resumed attempt contradiction",
    ):
        _resume_valid_attempts(path, resumed)

    return resumed


def test_resume_halts_on_not_exercised_with_overlaps(tmp_path) -> None:
    attempt = _completed_resume_attempt()
    attempt.update(
        {
            "raw_overlap": True,
            "public_overlap": True,
            "violation_doc_ids": ["source::gated"],
        }
    )

    resumed = _resume_one_attempt(tmp_path, attempt)

    assert (
        resumed["resume"]["halted_on_resumed_invariant"]["reason"]
        == "public_overlap requires outcome LEAK"
    )


def test_resume_halts_on_guard_fired_without_violation(tmp_path) -> None:
    attempt = _completed_resume_attempt(outcome=GUARD_FIRED)
    attempt["raw_overlap"] = True

    resumed = _resume_one_attempt(tmp_path, attempt)

    assert (
        resumed["resume"]["halted_on_resumed_invariant"]["reason"]
        == "GUARD FIRED requires non-empty violation_doc_ids"
    )


def test_resume_halts_on_leak_without_overlap(tmp_path) -> None:
    attempt = _completed_resume_attempt(outcome=LEAK)
    attempt["public_overlap"] = False

    resumed = _resume_one_attempt(tmp_path, attempt)

    assert (
        resumed["resume"]["halted_on_resumed_invariant"]["reason"]
        == "LEAK requires raw_overlap or public_overlap"
    )


def test_resume_halts_on_telemetry_overlap_contradiction(tmp_path) -> None:
    attempt = _completed_resume_attempt()
    attempt["gated_match_telemetry"][
        "longest_common_gated_token_run"
    ] = ATTEST_NGRAM

    resumed = _resume_one_attempt(tmp_path, attempt)

    assert (
        resumed["resume"]["halted_on_resumed_invariant"]["reason"]
        == "raw_overlap false contradicts gated overlap telemetry"
    )


def test_resume_halts_on_out_of_battery_target(tmp_path) -> None:
    attempt = _completed_resume_attempt()
    attempt["target_doc_id"] = "source::not-declared"
    attempt["context_doc_ids"] = ["source::not-declared"]
    attempt["gated_context_doc_ids"] = ["source::not-declared"]

    resumed = _resume_one_attempt(tmp_path, attempt)

    assert (
        resumed["resume"]["halted_on_resumed_invariant"]["reason"]
        == "target_doc_id is outside the declared battery"
    )


def test_resume_halts_on_unknown_shape(tmp_path) -> None:
    attempt = _completed_resume_attempt(shape="unknown-shape")

    resumed = _resume_one_attempt(tmp_path, attempt)

    assert (
        resumed["resume"]["halted_on_resumed_invariant"]["reason"]
        == "shape is outside ADVERSARIAL_SHAPES"
    )


def test_resume_halts_on_mismatched_model(tmp_path) -> None:
    attempt = _completed_resume_attempt()
    attempt["model"] = "other-chat-model"

    resumed = _resume_one_attempt(tmp_path, attempt)

    assert (
        resumed["resume"]["halted_on_resumed_invariant"]["reason"]
        == "model does not match the declared chat provider"
    )


def test_committed_x_regen_report_reuses_all_45_attempts() -> None:
    path = (
        Path(__file__).resolve().parents[2]
        / "evidence"
        / "v0.10.1"
        / "real-model-adversarial"
        / "report.json"
    )
    prior = json.loads(path.read_text())
    docs = [
        {"doc_id": doc_id, "license": "IndexOnly"}
        for doc_id in prior["battery"]["target_doc_ids"]
    ]
    resumed = _new_adversarial_report(
        chat_model=prior["provider_roles"]["chat"]["model"],
        embed_model=prior["provider_roles"]["embedding"]["model"],
        gated_docs=docs,
    )

    keys = _resume_valid_attempts(path, resumed)

    assert len(keys) == 45
    assert len(resumed["attempts"]) == 45
    assert resumed["counts"] == {
        GUARD_FIRED: 0,
        NOT_EXERCISED: 45,
        LEAK: 0,
    }
    assert resumed["resume"]["reused_valid_attempts"] == 45
    assert resumed["resume"]["retried_invalid_attempts"] == 0


def test_resume_reuses_only_valid_attempts(tmp_path) -> None:
    docs = [{"doc_id": "source::gated", "license": "IndexOnly"}]
    prior = _new_adversarial_report(
        chat_model="chat-model",
        embed_model="embed-model",
        gated_docs=docs,
    )
    prior["attempts"] = [
        _completed_resume_attempt(),
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
    assert resumed["attempts"] == [prior["attempts"][0]]
    assert resumed["counts"][NOT_EXERCISED] == 1
    assert resumed["resume"]["reused_valid_attempts"] == 1
    assert resumed["resume"]["retried_invalid_attempts"] == 1


def test_resume_retries_completed_attempt_with_http_502(tmp_path) -> None:
    docs = [{"doc_id": "source::gated", "license": "IndexOnly"}]
    prior = _new_adversarial_report(
        chat_model="chat-model",
        embed_model="embed-model",
        gated_docs=docs,
    )
    prior["attempts"] = [
        _completed_resume_attempt(http_status=502),
    ]
    path = tmp_path / "contradictory-prior.json"
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
    assert resumed["resume"]["retried_invalid_attempts"] == 1


def test_resume_retries_schema_incomplete_attempt(tmp_path) -> None:
    docs = [{"doc_id": "source::gated", "license": "IndexOnly"}]
    prior = _new_adversarial_report(
        chat_model="chat-model",
        embed_model="embed-model",
        gated_docs=docs,
    )
    incomplete = _completed_resume_attempt()
    del incomplete["gated_match_telemetry"]
    prior["attempts"] = [incomplete]
    path = tmp_path / "schema-incomplete-prior.json"
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
    assert resumed["resume"]["retried_invalid_attempts"] == 1


def test_resume_halts_and_records_resumed_leak(tmp_path) -> None:
    docs = [{"doc_id": "source::gated", "license": "IndexOnly"}]
    prior = _new_adversarial_report(
        chat_model="chat-model",
        embed_model="embed-model",
        gated_docs=docs,
    )
    prior["attempts"] = [
        _completed_resume_attempt(outcome=LEAK),
    ]
    path = tmp_path / "leaking-prior.json"
    path.write_text(json.dumps(prior))
    resumed = _new_adversarial_report(
        chat_model="chat-model",
        embed_model="embed-model",
        gated_docs=docs,
    )

    with pytest.raises(ValueError, match="resumed LEAK"):
        _resume_valid_attempts(path, resumed)

    assert resumed["resume"]["halted_on_resumed_leak"] == {
        "target_doc_id": "source::gated",
        "shape": "verbatim-quotation",
    }


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


def test_gateway_timeout_is_retried_and_not_counted_as_an_attempt() -> None:
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
        max_attempts_per_cell=2,
    )

    assert report["attempts"] == []
    assert len(report["transport_retries"]) == len(ADVERSARIAL_SHAPES) * 2
    assert all(
        retry["model_completed"] is False
        for retry in report["transport_retries"]
    )
    assert all(
        retry["target_in_context"] is True
        for retry in report["transport_retries"]
    )
    assert (
        "adversarial battery coverage",
        verify_llm.FAIL,
    ) in {(name, status) for name, status, _ in verify_llm.results}


def test_transient_gateway_timeout_is_retried_until_model_completion() -> None:
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

        def attest(self, answer: str, ids: list[str]) -> dict:
            return {"clean_answer": answer, "violations": []}

    core = RecordingCoreDouble()
    recording_chat = type("RecordingChat", (), {"last_answer": None})()

    class TransientGatewayTimeoutApi:
        calls = 0

        def get(self, *args, **kwargs):
            self.calls += 1
            core.last_retrieve_context_ids = [target["doc_id"]]
            if self.calls % 2:
                return type("Response", (), {"status_code": 502})()
            recording_chat.last_answer = "A safe independent summary."
            return type(
                "Response",
                (),
                {
                    "status_code": 200,
                    "json": lambda self: {
                        "answer": "A safe independent summary.",
                        "citations": [{"doc_id": target["doc_id"]}],
                    },
                },
            )()

    positive_control = {
        "outcome": GUARD_FIRED,
        "valid_attempt": True,
        "raw_overlap": True,
        "public_overlap": False,
        "violation_doc_ids": [target["doc_id"]],
    }
    verify_llm.results.clear()

    report = verify_llm._run_adversarial_battery(
        api=TransientGatewayTimeoutApi(),
        core=core,
        recording_chat=recording_chat,
        gated_docs=[target],
        chat_model="chat-model",
        embed_model="embed-model",
        report_path=None,
        resume_from=None,
        real_path_positive_control=positive_control,
        max_attempts_per_cell=2,
    )

    assert report["complete"] is True
    assert len(report["attempts"]) == len(ADVERSARIAL_SHAPES)
    assert len(report["transport_retries"]) == len(ADVERSARIAL_SHAPES)
    assert all(attempt["model_completed"] for attempt in report["attempts"])
    assert all(attempt["valid_attempt"] for attempt in report["attempts"])
    assert all(
        attempt["transport_retry_count"] == 1
        for attempt in report["attempts"]
    )


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
