"""Failure-capable checks for the real-model verifier's public HC1 audit."""

import tools.verify_llm as verify_llm
from intel_shell.llm import LlmError
from tools.verify_llm import (
    ATTEST_NGRAM,
    ATTEST_REFUSAL,
    GUARD_FIRED,
    LEAK,
    NOT_EXERCISED,
    _embedding_items,
    _finish,
    _has_gated_overlap,
    _record_adversarial_outcome,
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

    assert verify_llm.cli() == 130
    captured = capsys.readouterr()
    assert "verification interrupted; cleanup follows." in captured.err
    assert "Traceback" not in captured.err
