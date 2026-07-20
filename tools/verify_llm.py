#!/usr/bin/env python3
"""T7 checklist, executable: verify a REAL LLM endpoint end to end.

T7 could not be completed in the build sandbox (no OpenAI-compatible endpoint is
reachable from it, and mocking it would be lying). This script is the deferred
work made cheap: point it at the real box and it runs the whole T7 checklist and
tells you which parts pass.

    LLM_BASE_URL=http://vllm-box:8000/v1 LLM_API_KEY=... \
    LLM_CHAT_MODEL=... LLM_EMBED_MODEL=... \
    PYTHONPATH=shell python3 tools/verify_llm.py

Assumes `cored` is already running (CORE_URL, default 127.0.0.1:8788).

The check that actually matters is the last one. Everything else is plumbing;
HC1 is the product's central promise, and an LLM in the loop is exactly where it
would break — the model sees full IndexOnly bodies as context (that is analysis,
and allowed), so the only question that counts is whether any of that gated text
can escape into what a subscriber reads.
"""

from __future__ import annotations

import sys
import time

from intel_shell import config
from intel_shell.core_client import CoreClient, CoreError
from intel_shell.llm import chat_from_env, embed_from_env

PASS, FAIL, WARN = "PASS", "FAIL", "WARN"
results: list[tuple[str, str, str]] = []


def check(name: str, status: str, detail: str = "") -> None:
    results.append((name, status, detail))
    print(f"  [{status}] {name}" + (f" — {detail}" if detail else ""))


def main() -> int:
    core = CoreClient(config.CORE_URL, token=config.CORE_TOKEN)
    chat, embed = chat_from_env(), embed_from_env()

    print("== endpoint ==")
    if chat is None or embed is None:
        print("error: set LLM_BASE_URL (and LLM_API_KEY if required)", file=sys.stderr)
        return 1
    print(f"  base: {config.os.environ.get('LLM_BASE_URL')}")

    print("== 1. embeddings populate ==")
    t0 = time.time()
    try:
        missing = core.embeddings_missing(embed.model)
        if missing:
            vectors = [
                {"doc_id": d["id"], "vector": embed.embed([d["body"]])[0]}
                for d in missing[:16]
            ]
            core.embeddings_upsert(embed.model, vectors)
        still = core.embeddings_missing(embed.model)
        check("embeddings backfill", PASS if len(still) < len(missing) or not missing
              else FAIL, f"{len(missing)} missing -> {len(still)} after one batch")
    except CoreError as e:
        check("embeddings backfill", FAIL, str(e))
    check("embed latency", WARN, f"{time.time() - t0:.2f}s for one batch")

    print("== 2. fusion is no longer BM25-only ==")
    try:
        q = "sparse attention"
        vec = embed.embed([q])[0]
        r = core.retrieve(q, ["science", "technology"], k=5,
                          model=embed.model, query_vector=vec)
        notes = r.get("notes") or r.get("retrieval", {}).get("notes") or []
        check("retrieval.notes clean", PASS if not notes else WARN, str(notes))
        check("hybrid hits", PASS if r.get("context") else FAIL,
              f"{len(r.get('context', []))} context docs")
    except CoreError as e:
        check("hybrid retrieve", FAIL, str(e))

    print("== 3. HC1 — gated text must not escape into a subscriber answer ==")
    print("  Ask a question whose BEST evidence is an IndexOnly document.")
    print("  The model may READ the full body (analysis); the public answer must")
    print("  not reproduce it. Inspect the output below by eye:")
    try:
        q = "What is DeepSeek-V4?"
        vec = embed.embed([q])[0]
        r = core.retrieve(q, ["science", "technology"], k=5,
                          model=embed.model, query_vector=vec)
        gated = [d for d in r.get("context", [])
                 if d.get("license") == "IndexOnly"]
        check("IndexOnly doc is in context", PASS if gated else WARN,
              f"{len(gated)} gated doc(s) used as context")
        print("\n  --- verify by eye: no verbatim sentence from a gated body ---")
        print("  (run the public API and diff the answer against the source body)")
        print("    curl -H 'Authorization: Bearer ak_acme_7f3d9c' \\")
        print("         'localhost:8787/v1/ask?q=What+is+DeepSeek-V4'")
    except CoreError as e:
        check("HC1 spot-check setup", FAIL, str(e))

    print("\n== 4. --llm-enrich yields SUBSTANTIVE suggestions ==")
    print("  (the mock yields none by design; a real model should propose entities)")
    print("    PYTHONPATH=shell python3 -m intel_shell.pipeline "
          "--client acme-research --llm-enrich")

    failed = [r for r in results if r[1] == FAIL]
    print(f"\n== {len(results) - len(failed)}/{len(results)} automated checks passed ==")
    print("Record model names + observed latency in STATE.md (T7 done-when).")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
