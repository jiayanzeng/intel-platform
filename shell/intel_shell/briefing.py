"""The subscriber-facing brief renderer (was crates/brief/src/render.rs).

All product copy and formatting is now Python — reword a section, reorder,
add one, A/B the voice: shell-only changes.

The license gate does NOT live here anymore, and that is deliberate: the
core's /view endpoint already withholds excerpts for non-redistributable
sources (evidence arrives with `excerpt: null`). This renderer can only
print what the core chose to reveal — a rewrite of this file cannot leak.
"""

from __future__ import annotations

KIND_TAG = {
    "RisingEntity": "RISING",
    "Corroborated": "CORROBORATED",
    "EmergingEntity": "EMERGING",
}


def render_brief(client: str, sectors: list[str], view: dict, new_n: int = 0) -> str:
    lines: list[str] = []
    out = lines.append

    window = view.get("window_end") or "n/a"
    drops = view.get("near_duplicates", [])

    out("# Intelligence Brief")
    out(
        f"client: {client} | sectors: {', '.join(sorted(sectors))} | "
        f"window ending {window}"
    )
    out(
        f"corpus: {view.get('documents_analyzed', 0)} documents analyzed "
        f"(+{new_n} ingested this run, {len(drops)} near-duplicate(s) collapsed)"
    )
    out("")

    out("## Top signals")
    signals = view.get("signals", [])
    if not signals:
        out("(no signals above thresholds in this window)")
    for i, sig in enumerate(signals[:8], start=1):
        tag = KIND_TAG.get(sig["kind"], sig["kind"])
        out(f"{i}. [{tag}] {sig['headline']}  (score {sig['score']:.2f})")
        if sig.get("detail"):
            out(f"   {sig['detail']}")
        evidence = sig.get("evidence", [])
        for ev in evidence[:3]:
            day = ev.get("day") or "n/a"
            out(f"   - [{ev['source_id']}] {ev['title']} ({day})")
            if ev.get("url"):
                out(f"     {ev['url']}")
            if ev.get("excerpt") is not None:
                out(f"     \"{ev['excerpt']}\"")
            else:
                out(
                    f"     excerpt withheld ({ev['license']} license) — "
                    "serving derived signal only"
                )
        if len(evidence) > 3:
            out(f"   ... and {len(evidence) - 3} more evidence document(s)")
        out("")

    out("## Entity association graph (top edges)")
    edges = view.get("edges", [])
    if not edges:
        out("(no co-occurrences yet)")
    for e in edges[:8]:
        out(
            f"  {e['a_name']} <-> {e['b_name']}   "
            f"weight {e['weight']}   pmi {e['pmi']:.2f}"
        )
    out("")

    emerging = [s for s in signals if s["kind"] == "EmergingEntity"]
    if emerging:
        out("## Gazetteer growth queue")
        for s in emerging:
            out(f"  {s['headline']} — {s['detail']}")
        out("")

    out(
        "---\nEvery signal above links to source documents with full provenance. "
        "Excerpts appear only where the source license permits redistribution; "
        "all other value is derived analysis, which is the product."
    )
    return "\n".join(lines) + "\n"
