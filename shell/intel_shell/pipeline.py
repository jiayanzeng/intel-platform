"""Pipeline orchestration (was apps/pipeline in Rust).

The FLOW is business logic — what runs, in what order, for which client —
so it lives in the shell now. Each step is one core call:

    ingest (entitled sectors)          -> POST /ingest
    embedding backfill (shell embeds)  -> GET /embeddings/missing + POST /embeddings
    intelligence view                  -> GET /view
    audit trail                        -> POST /signals/record
    brief (rendered HERE)              -> briefing.render_brief

Usage (from the repo root, with cored running):
    PYTHONPATH=shell python3 -m intel_shell.pipeline --client acme-research
    PYTHONPATH=shell python3 -m intel_shell.pipeline --client quant-desk --llm-enrich
"""

from __future__ import annotations

import argparse
import os
import sys

from . import briefing, config
from .core_client import CoreClient, CoreError
from .enrichment import gazetteer_suggestions
from .llm import chat_from_env, embed_from_env

EMBED_BATCH = 16


def _signal_payload(view_signals: list[dict]) -> list[dict]:
    """Map the core's hydrated SignalDto back to the audit-record shape
    (evidence as plain doc ids)."""
    return [
        {
            "kind": s["kind"],
            "headline": s["headline"],
            "score": s["score"],
            "entity_ids": s.get("entity_ids", []),
            "evidence": [e["doc_id"] for e in s.get("evidence", [])],
            "detail": s.get("detail", ""),
        }
        for s in view_signals
    ]


def run(client_arg: str | None, subs_path: str | None, data_dir: str,
        core_url: str, llm_enrich: bool, skip_ingest: bool = False) -> int:
    subs = config.load_subscriptions(subs_path)
    if not subs:
        print("error: no subscriptions configured", file=sys.stderr)
        return 1
    client = client_arg or subs[0].client
    sub = config.subscription_for(subs, client)
    if sub is None:
        print(f"error: no subscription for client '{client}'", file=sys.stderr)
        return 1

    core = CoreClient(core_url, token=config.CORE_TOKEN)

    # --- ingest (entitlement-gated: only the client's sectors are fetched) ---
    # A scheduler running per-sector ingest jobs separately can pass
    # skip_ingest=True so this "refresh" run only re-analyzes the archive.
    new_n = 0
    if skip_ingest:
        print(f"== refresh (client: {client}; ingest skipped) ==")
    else:
        print(f"== ingest (client: {client}) ==")
        try:
            ing = core.ingest(list(sub.sectors))
        except CoreError as e:
            print(f"error: {e}", file=sys.stderr)
            return 1
        for r in ing["results"]:
            if r["ok"]:
                print(f"  fetch  [{r['sector']} / {r['source_id']}] {r['documents']} document(s)")
            else:
                print(f"  error  [{r['sector']} / {r['source_id']}] {r['error']}")
        print(f"  archive: +{ing['new']} new this run ({ing['fetched']} fetched)")
        new_n = ing["new"]

    # --- embeddings backfill (the SHELL calls the model; the core stores) -----
    embed = embed_from_env()
    if embed is None:
        print("  embeddings: skipped (LLM_BASE_URL not set)")
    else:
        missing = core.embeddings_missing(embed.model)
        if not missing:
            print(f"  embeddings: up to date (model '{embed.model}')")
        else:
            embedded = 0
            for i in range(0, len(missing), EMBED_BATCH):
                chunk = missing[i : i + EMBED_BATCH]
                texts = [f"{d['title']} {d['body']}" for d in chunk]
                try:
                    vecs = embed.embed(texts)
                except Exception as e:  # noqa: BLE001 — batch fails, run continues
                    print(f"  embeddings: batch failed ({e}); continuing")
                    continue
                items = [
                    {"doc_id": d["doc_id"], "vector": v}
                    for d, v in zip(chunk, vecs)
                ]
                embedded += core.upsert_embeddings(embed.model, items)["upserted"]
            print(f"  embeddings: {embedded} document(s) embedded (model '{embed.model}')")

    # --- intelligence view (dedup -> mentions -> discovery -> signals) --------
    print("== analyze ==")
    view = core.view(list(sub.sectors))
    for drop in view.get("near_duplicates", []):
        print(
            f"  near-dup: dropped {drop['dropped_id']} "
            f"(kept {drop['kept_id']}, hamming {drop['distance']})"
        )
    print(
        f"  {view['documents_analyzed']} doc(s) after de-dup; "
        f"{view['mentions']} mention(s); "
        f"{len(view.get('discovered', []))} discovery candidate(s); "
        f"{len(view.get('signals', []))} signal(s); "
        f"{len(view.get('edges', []))} edge(s)"
    )

    # --- audit trail: record what this client was told, and when ---------------
    signals = view.get("signals", [])
    core.record_signals(client, view.get("window_end"), _signal_payload(signals))
    print(f"  audit: {len(signals)} signal(s) recorded to signals_history")

    # --- optional LLM enrichment (gazetteer growth via a model) -----------------
    if llm_enrich:
        chat = chat_from_env()
        if chat is None:
            print("  llm-enrich: skipped (LLM_BASE_URL not set)")
        else:
            ids = view.get("kept_doc_ids", [])[:10]
            docs = core.docs(ids) if ids else []
            known = {"deepseek", "qwen", "nvidia", "vllm"}  # cheap demo floor
            try:
                with open("config/entities.json", encoding="utf-8") as f:
                    import json as _json

                    gaz = _json.load(f)
                    known = {
                        a.lower()
                        for e in gaz.get("entities", [])
                        for a in [e["name"], *e.get("aliases", [])]
                    }
            except FileNotFoundError:
                pass
            suggestions = gazetteer_suggestions(chat, docs, known)
            if suggestions:
                print("  llm-enrich: gazetteer candidates from the model:")
                for name, n in suggestions.most_common(10):
                    print(f"    {name}  (seen {n}x)")
            else:
                print("  llm-enrich: no unknown entities suggested")

    # --- brief (rendered in the shell; excerpts pre-gated by the core) ----------
    brief = briefing.render_brief(client, list(sub.sectors), view, new_n=new_n)
    print()
    print(brief)

    stamp = view.get("window_end") or "latest"
    os.makedirs(data_dir, exist_ok=True)
    out_path = os.path.join(data_dir, f"brief-{stamp}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(brief)
    print(f"(brief saved to {out_path})")
    return 0


def ingest_only(client_arg: str | None, subs_path: str | None, core_url: str,
                sectors: list[str] | None = None,
                sources: list[str] | None = None) -> int:
    """Fetch just the named sectors, or named sources within them.

    This is the unit a scheduler drives on a per-source cadence: cheap, no
    analysis, no brief. Returns 0 on success, 1 on config/core error.

    `sources`, when given, names specific source ids to run. The client's
    entitled sectors are always passed as the sector allow-list, so the core
    enforces entitlement in SQL — a named source outside the entitlement is
    rejected there, not run.
    """
    subs = config.load_subscriptions(subs_path)
    if not subs:
        print("error: no subscriptions configured", file=sys.stderr)
        return 1
    client = client_arg or subs[0].client
    sub = config.subscription_for(subs, client)
    if sub is None:
        print(f"error: no subscription for client '{client}'", file=sys.stderr)
        return 1

    want = list(sectors) if sectors else list(sub.sectors)
    # Never fetch outside the client's entitlement, even if asked.
    want = [s for s in want if s in sub.sectors]
    if not want:
        print(f"  ingest: no entitled sectors to fetch for {client}")
        return 0

    core = CoreClient(core_url, token=config.CORE_TOKEN)
    scope = f"sources: {', '.join(sources)}" if sources else f"sectors: {', '.join(want)}"
    print(f"== ingest (client: {client}; {scope}) ==")
    try:
        ing = core.ingest(want, sources=sources)
    except CoreError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    for r in ing["results"]:
        status = "fetch" if r["ok"] else "error"
        detail = f"{r['documents']} document(s)" if r["ok"] else r["error"]
        print(f"  {status}  [{r['sector']} / {r['source_id']}] {detail}")
    print(f"  archive: +{ing['new']} new this run ({ing['fetched']} fetched)")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="intel-platform pipeline (shell orchestrator)")
    ap.add_argument("--client", default=None)
    ap.add_argument("--config", default=None, help="path to subscriptions.json")
    ap.add_argument("--data-dir", default="data")
    ap.add_argument("--core-url", default=config.CORE_URL)
    ap.add_argument("--llm-enrich", action="store_true",
                    help="suggest gazetteer candidates via the chat model")
    args = ap.parse_args(argv)
    return run(args.client, args.config, args.data_dir, args.core_url, args.llm_enrich)


if __name__ == "__main__":
    raise SystemExit(main())
