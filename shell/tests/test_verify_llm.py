"""Failure-capable checks for the real-model verifier's public HC1 audit."""

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
