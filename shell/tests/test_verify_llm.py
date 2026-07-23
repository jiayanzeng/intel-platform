"""Failure-capable checks for the real-model verifier's public HC1 audit."""

import tools.verify_llm as verify_llm
from intel_shell.llm import LlmError
from tools.verify_llm import ATTEST_NGRAM, _embedding_items, _has_gated_overlap


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


def test_verifier_interrupt_exits_cleanly(monkeypatch, capsys) -> None:
    def interrupted() -> int:
        raise KeyboardInterrupt

    monkeypatch.setattr(verify_llm, "main", interrupted)

    assert verify_llm.cli() == 130
    captured = capsys.readouterr()
    assert "verification interrupted; cleanup follows." in captured.err
    assert "Traceback" not in captured.err
