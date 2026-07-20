"""Every prompt in the product, in one hot-editable file.

This file is the primary "vibe coding" surface: change the system prompt,
the context format, the citation style — redeploy the shell, core untouched.
"""

from __future__ import annotations

ASK_SYSTEM = (
    "You are the Q&A layer of an intelligence platform. "
    "Answer strictly from the provided context documents; if they are "
    "insufficient, say so plainly. Cite supporting documents inline as [n]. "
    "Synthesize rather than quote: never reproduce more than a short phrase "
    "verbatim, and never reproduce sentences from sources marked IndexOnly."
)

# License nuance, stated plainly: passing IndexOnly text to the model as
# context is analysis (permitted); the system prompt above forbids
# reproducing it verbatim in the answer, and the citations give subscribers
# the pointer to the original. This is the durable shape for paid Q&A over
# mixed-license corpora — confirm specifics with an IP lawyer before
# charging for it.

BODY_CAP = 800  # chars of each document body shown to the model


def build_context(context_docs: list[dict], body_cap: int = BODY_CAP) -> tuple[str, list[dict]]:
    """Numbered context blocks + the citation table that mirrors them.

    `context_docs` come from the core's /retrieve endpoint: fused order,
    near-duplicates already suppressed.
    """
    blocks: list[str] = []
    citations: list[dict] = []
    for n, d in enumerate(context_docs, start=1):
        day = d.get("day") or "n/a"
        body = (d.get("body") or "")[:body_cap]
        blocks.append(
            f"[{n}] {d['title']} (source: {d['source_id']}, date: {day}, "
            f"license: {d['license']})\n{body}\n"
        )
        citations.append(
            {
                "ref": f"[{n}]",
                "doc_id": d["doc_id"],
                "title": d["title"],
                "source_id": d["source_id"],
                "url": d.get("url"),
                "license": d["license"],
            }
        )
    return "\n".join(blocks), citations


def build_ask_user(question: str, context: str) -> str:
    if not context:
        return f"QUESTION: {question}\n\nCONTEXT: (no documents retrieved)"
    return f"QUESTION: {question}\n\nCONTEXT:\n{context}"


# --- LLM enrichment (was crates/enrich/src/llm.rs) ---------------------------

ENTITY_SYSTEM = (
    "You extract structured data. "
    "Respond ONLY with the requested JSON and nothing else."
)


def entity_extraction_prompt(title: str, body: str) -> str:
    return (
        "Extract named entities (organizations, people, models, technologies, "
        "topics) from the text below. JSON form: "
        '{"entities":[{"name":"...","kind":"Org|Person|Model|Tech|Topic"}]}\n\n'
        f"TITLE: {title}\nBODY: {body}"
    )
