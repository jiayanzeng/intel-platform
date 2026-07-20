# T8 — Scale swaps: design note (NOT implemented)

T8 is explicitly design-level this cycle. Nothing here is built; this records
*where* each swap lands and what would trigger it, so the decision is cheap when
the trigger actually fires. Building any of it now would be speculative — the
system currently serves a single node with ~14 documents and two clients.

The reason these are all still deferrable is the seam: each swap sits behind an
existing method surface, so none of them is a rewrite.

## The trigger, per swap

| Swap | Replaces | Trigger — build it when… | Where it lands |
|---|---|---|---|
| **Postgres** | SQLite | a second writer appears (multiple `cored` instances, or the shell writing directly). SQLite's one-writer model is not a bottleneck we are anywhere near; it is a *correctness* wall the moment concurrency arrives | `crates/store` — `SqliteStore`'s method surface is already the port; add `PgStore` behind the same signatures |
| **pgvector** | brute-force cosine in `store::nearest` | cosine over the whole archive stops fitting in the request budget — order 10⁵–10⁶ docs. Below that, brute force is *faster* than an index lookup and exactly correct | same crate; the shell already computes vectors and POSTs them, so nothing above the store changes |
| **tantivy** | FTS5 BM25 | search QPS or index size outgrows FTS5, or we need per-field boosting / custom analyzers FTS5 can't express | `crates/store::search` — returns `Vec<SearchHit>` either way |
| ~~**LSH / minhash banding**~~ **SKIPPED — measured, v0.7/T5** | the O(n²) scan in `dedup_near` | **never, at the current threshold.** Exact recall at hamming ≤ 16 on a 64-bit fingerprint forces ≥17 bands of ~3.8 bits, which prunes 24% of pairs and runs **246× slower** than the scan. And the scan is only **14.6%** of dedup time at n=10k anyway — *fingerprinting* is 85%. See below. | — |
| **Persist the SimHash fingerprint** *(the swap that replaces LSH on this list)* | recomputing `simhash()` for every doc on every dedup pass | **now-ish** — it is already 85% of dedup cost at n=10k and grows linearly with the corpus | `crates/store` (a column) + `crates/extract::dedup_near` (take fingerprints, don't compute them). Output is bit-identical. |
| **Materialized `/view`** | recompute per request | it already did — see T9.2. `/view` is now memoized per (sector-set, generation). The *next* step, if a single process can't hold it, is to materialize into a table keyed by generation | `apps/cored` — the cache is already generation-keyed, so this is a storage change, not a logic change |

## What would actually be load-bearing

Two of these are not really "scale" at all, and are worth separating out:

- **Postgres is a concurrency decision, not a size decision.** The archive could
  reach tens of GB on SQLite without trouble. What SQLite cannot do is admit a
  second writer. So the trigger is an architectural event (a second `cored`, a
  worker pool), not a row count — and if that event never happens, this swap
  never needs to.
- **~~LSH is the one with a real asymptotic problem.~~ MEASURED IN v0.7 — AND
  THIS WAS WRONG ON BOTH COUNTS.** The claim was that `dedup_near`'s pairwise
  scan is the hot spot and the first swap that will matter. T5 of v0.7 built the
  thing and measured it (`cargo run --release -p intel-extract --example
  dedup_bench`). Both halves of the claim fail:

  1. **The quadratic scan is not the bottleneck.** At n = 10,000 the pairwise
     hamming scan is **126 ms — 14.6%** of dedup time. The other **85%** is
     SimHash *fingerprinting*, which `dedup_near` recomputes for every document
     on every call. The quadratic term does not overtake the linear one until
     roughly n > 100k, because a hamming comparison is one XOR and a popcount
     (~1 ns) while fingerprinting a 2 KB body costs ~70 µs. We were about to
     optimize the cheap half.

  2. **Banding cannot prune at this threshold anyway.** `dedup_max_distance` is
     **16** on a **64-bit** fingerprint. Exact recall requires, by pigeonhole,
     more bands than the distance — b ≥ 17 — so bands are 64/17 ≈ **3.8 bits**
     wide. A 4-bit band has 16 possible values, so an average bucket holds n/16
     of the corpus and nearly everything collides with nearly everything.
     Measured: banding still compares **76% of all pairs** (a 24% prune) and
     runs **246× slower** than the scan it replaces (30,962 ms vs 126 ms at
     n = 10k). At n = 20k it does not finish — the candidate set alone tries to
     allocate ~4.5 GB. Recall *is* exactly 100%, as the math promises; the
     index is correct and useless.

     The general rule, which is the part worth keeping: **an LSH band's
     selectivity depends on the threshold as a *fraction* of fingerprint width,
     not its absolute value.** 16/64 = 25% divergence is far outside the regime
     where any exact Hamming index beats a linear scan. Widening the fingerprint
     does not help if the threshold widens with it; it only helps if the
     *absolute* distance stays at 16 (e.g. 16/128 = 12.5%), and that is a
     different similarity rule — it changes which documents are duplicates,
     which is corpus corruption, not an optimization.

  **What to do instead — the real swap, with the real trigger:** persist the
  fingerprint. `simhash(title + body)` is a pure function of the document and is
  already described in `crates/extract/src/lib.rs` as something "the persistent
  store relies on" being stable — but it is recomputed from scratch on every
  dedup pass. Storing it as a column at ingest removes ~85% of dedup's cost at
  n = 10k, changes no output whatsoever (same fingerprints ⇒ same drops, same
  canonical ids), and is a far smaller change than an index. **Only after that
  is the pairwise scan worth attacking** — and by then the honest options are a
  tighter threshold or a wider fingerprint, both of which change dedup semantics
  and need to be argued on the merits, not smuggled in as a performance fix.

## What NOT to do

Do not pre-emptively introduce Postgres "so we're ready." The invariants that
make this system trustworthy — license gating in core, sector filtering in SQL,
dedup before statistics — are enforced in Rust *above* the storage layer, and
they are what a rewrite would put at risk. The storage is the replaceable part;
that is the whole point of the arrangement, and it is only true for as long as
nobody smears business logic into it.
