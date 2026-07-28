"""LLM entity extraction (was crates/enrich/src/llm.rs, behind a feature flag).

Now an ordinary Python module the pipeline can call with --llm-enrich.
The output feeds the same gazetteer growth loop as the deterministic
discovery in the core: suggestions get human review, then promotion into
config/entities.json.

Production hardening: batch documents, cap concurrency, retry with
backoff, and validate returned JSON against a schema before trusting it.
"""

from __future__ import annotations

import json
from collections import Counter

from . import prompts
from .llm import ChatClient, LlmError


def extract_entities(chat: ChatClient, title: str, body: str) -> list[dict]:
    """Returns [{"name": ..., "kind": ...}, ...] or raises LlmError."""
    content = chat.chat(prompts.ENTITY_SYSTEM, prompts.entity_extraction_prompt(title, body))
    clean = content.strip()
    if clean.startswith("```"):
        clean = clean.removeprefix("```json").removeprefix("```")
        clean = clean.removesuffix("```").strip()
    try:
        data = json.loads(clean)
    except json.JSONDecodeError as e:
        raise LlmError(f"model returned non-JSON: {e}") from e
    ents = data.get("entities", [])
    return [e for e in ents if isinstance(e, dict) and e.get("name")]


def entity_candidates(chat: ChatClient, docs: list[dict]) -> Counter:
    """Count entity names extracted by the model for core-side comparison."""
    candidates: Counter = Counter()
    for d in docs:
        try:
            for e in extract_entities(chat, d.get("title", ""), d.get("body", "")):
                name = e["name"].strip()
                if name:
                    candidates[name] += 1
        except LlmError as err:
            print(f"  enrich: skipped {d.get('doc_id', '?')} ({err})")
    return candidates
