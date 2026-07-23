#!/usr/bin/env python3
"""T4 checklist, executable: verify REAL model endpoints end to end.

Chat and embeddings may come from different OpenAI-compatible providers. This
is required in practice: DeepSeek and many llama.cpp servers implement chat but
do not implement POST /embeddings.

    cp .env.example .env
    # fill chat profile + independent embedding endpoint
    ./run verify-llm

`./run verify-llm` starts an isolated fixture core before invoking this script.
Direct invocation still assumes cored is already running at CORE_URL.

The final check executes the real public `/v1/ask` path. The model sees full
IndexOnly bodies as internal analysis context, then core `/attest` must prevent
any 16-token gated overlap from reaching the returned answer.
"""

from __future__ import annotations

import re
import sys
import time

from fastapi.testclient import TestClient

from intel_shell import config
from intel_shell.app import app
from intel_shell.core_client import CoreClient, CoreError
from intel_shell.llm import LlmError, chat_from_env, embed_from_env

PASS, FAIL, WARN = "PASS", "FAIL", "WARN"
results: list[tuple[str, str, str]] = []
ATTEST_NGRAM = 16


def check(name: str, status: str, detail: str = "") -> None:
    results.append((name, status, detail))
    print(f"  [{status}] {name}" + (f" — {detail}" if detail else ""))


def _tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _has_gated_overlap(answer: str, docs: list[dict]) -> bool:
    answer_tokens = _tokens(answer)
    answer_ngrams = {
        tuple(answer_tokens[i : i + ATTEST_NGRAM])
        for i in range(len(answer_tokens) - ATTEST_NGRAM + 1)
    }
    if not answer_ngrams:
        return False
    for doc in docs:
        if doc.get("license") != "IndexOnly":
            continue
        body = _tokens(doc.get("body", ""))
        for i in range(len(body) - ATTEST_NGRAM + 1):
            if tuple(body[i : i + ATTEST_NGRAM]) in answer_ngrams:
                return True
    return False


def _embedding_items(batch: list[dict], vectors: list[list[float]]) -> list[dict]:
    return [
        {"doc_id": doc["doc_id"], "vector": vector}
        for doc, vector in zip(batch, vectors)
    ]


def _finish() -> int:
    failed = [r for r in results if r[1] == FAIL]
    passed = [r for r in results if r[1] == PASS]
    required = passed + failed
    warnings = [r for r in results if r[1] == WARN]
    print(f"\n== {len(passed)}/{len(required)} required checks passed"
          f"; {len(warnings)} diagnostic warning(s) ==")
    print("Record model names + observed latency in STATE.md (T4 done-when).")
    return 1 if failed else 0


def main() -> int:
    results.clear()
    core = CoreClient(config.CORE_URL, token=config.CORE_TOKEN)
    chat, embed = chat_from_env(), embed_from_env()

    print("== endpoints (keys redacted) ==")
    if chat is None or embed is None:
        check("chat configuration", PASS if chat else FAIL,
              chat.base_url if chat else "no chat endpoint resolved")
        check("embedding configuration", PASS if embed else FAIL,
              embed.base_url if embed else "no embedding endpoint resolved")
        return _finish()
    print(
        f"  chat: {chat.base_url} "
        f"(model={chat.model}, timeout={chat.timeout_seconds:g}s)"
    )
    print(
        f"  embeddings: {embed.base_url} "
        f"(model={embed.model}, timeout={embed.timeout_seconds:g}s)"
    )

    print("== 1. embeddings populate ==")
    t0 = time.time()
    backfill_ok = False
    try:
        missing = core.embeddings_missing(embed.model)
        if missing:
            batch = missing[:16]
            embedded = embed.embed([d["body"] for d in batch])
            vectors = _embedding_items(batch, embedded)
            core.upsert_embeddings(embed.model, vectors)
        still = core.embeddings_missing(embed.model)
        backfill_ok = len(still) < len(missing) or not missing
        check(
            "embeddings backfill",
            PASS if backfill_ok else FAIL,
            f"{len(missing)} missing -> {len(still)} after one batch",
        )
    except (CoreError, LlmError, KeyError, ValueError) as e:
        check("embeddings backfill", FAIL, str(e))
    check("embed latency", WARN, f"{time.time() - t0:.2f}s")
    if not backfill_ok:
        print("\n== stopping before fusion/public HC1: embedding prerequisite failed ==")
        return _finish()

    print("== 2. fusion is no longer BM25-only ==")
    fusion_ok = False
    try:
        q = "sparse attention"
        vec = embed.embed([q])[0]
        r = core.retrieve(
            q,
            ["science", "technology"],
            k=5,
            model=embed.model,
            query_vector=vec,
        )
        notes = r.get("notes") or r.get("retrieval", {}).get("notes") or []
        notes_ok = not notes
        hits_ok = bool(r.get("context"))
        check("retrieval.notes clean", PASS if notes_ok else FAIL, str(notes))
        check(
            "hybrid hits",
            PASS if hits_ok else FAIL,
            f"{len(r.get('context', []))} context docs",
        )
        fusion_ok = notes_ok and hits_ok
    except (CoreError, LlmError, KeyError, ValueError) as e:
        check("hybrid retrieve", FAIL, str(e))
    if not fusion_ok:
        print("\n== stopping before public HC1: fusion prerequisite failed ==")
        return _finish()

    print("== 3. public HC1 — gated text cannot escape ==")
    try:
        with TestClient(app) as api:
            q = "What is DeepSeek-V4?"
            response = api.get(
                "/v1/ask",
                params={"q": q},
                headers={"Authorization": "Bearer ak_acme_7f3d9c"},
            )
        if response.status_code != 200:
            check(
                "public /v1/ask",
                FAIL,
                f"HTTP {response.status_code}: {response.text[:240]}",
            )
        else:
            body = response.json()
            citations = body.get("citations", [])
            docs = core.docs([c["doc_id"] for c in citations])
            gated = [d for d in docs if d.get("license") == "IndexOnly"]
            answer = body.get("answer", "")
            overlap = _has_gated_overlap(answer, docs)
            check("public /v1/ask", PASS, f"{len(citations)} citation(s)")
            check(
                "IndexOnly context exercised",
                PASS if gated else FAIL,
                f"{len(gated)} gated citation document(s)",
            )
            check(
                "HC1 public answer attested",
                FAIL if overlap else PASS,
                "16-token gated overlap found" if overlap else "no gated overlap",
            )
            print(f"  public answer: {answer[:240]}")
    except (CoreError, LlmError, KeyError, ValueError) as e:
        check("HC1 public spot-check", FAIL, str(e))

    print("\n== 4. --llm-enrich yields SUBSTANTIVE suggestions ==")
    print("  (the mock yields none by design; a real model should propose entities)")
    print("    PYTHONPATH=shell python3 -m intel_shell.pipeline "
          "--client acme-research --llm-enrich")

    return _finish()


def cli() -> int:
    try:
        return main()
    except KeyboardInterrupt:
        print("\nverification interrupted; cleanup follows.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(cli())
