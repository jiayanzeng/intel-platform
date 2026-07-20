# ARCHITECTURE.md — intel-platform

**This document is authoritative for invariants — what must be true of the
system. It changes rarely and never casually.** For *current status* (test
counts, what shipped last, open gaps) see `STATE.md`. For *how to work here* see
`AGENTS.md`. Where a placement below seems arbitrary, `STATE.md §2` holds the full
reasoning and is the authority.

intel-platform is a market- and technology-intelligence aggregation system built
on a **Core–Shell** split: a performance-critical, invariant-bearing Rust core
(`cored`) behind a freely-iterating Python shell (`intel_shell`).

## 1. The seam

```text
SHELL (Python, product layer — iterate freely)
  app.py        public /v1/* API, auth
  auth.py       api key -> entitled sectors
  llm.py        chat + embed  (the ONLY component that calls a model)
  prompts.py · briefing.py · pipeline.py · enrichment.py · scheduler.py
        |
        |  CoreClient (core_client.py) — the ONE door to the core.
        |  httpx, injectable transport (MockTransport in tests).
        v  minimal JSON API over 127.0.0.1:8788, optional x-core-token
CORE (Rust, engine — stable, invariant-bearing)
  apps/cored    /health /sectors /ingest /view /search /retrieve
                /attest /embeddings(/missing) /signals/record /docs
  crates        core compliance ingest extract enrich analyze
                store registry view retrieve
```

The design intent: **the core holds the invariants so the shell can be rewritten
arbitrarily without endangering them.** `briefing.py` can be rebuilt from scratch
and still cannot leak gated text, because it never receives gated text. That
property is the whole point of the split, and it is why the placement decisions
below are load-bearing.

## 2. Config ownership

| file | owner | holds |
|---|---|---|
| `config/core.json` | core | sectors, sources, licenses |
| `config/entities.json` | core | gazetteer |
| `config/subscriptions.json` (or `sqlite:///…`) | shell | clients, sectors, keys |
| `config/schedule.json` | shell | per-source and per-sector cadence |

Core-owned config describes *what exists and how it may be used*; shell-owned
config describes *who may see it and when to fetch it*. Do not cross these.

## 3. Load-bearing placement decisions (do not move casually)

Condensed from `STATE.md §2`.

1. **License gating lives in the core.** `store.search` nulls snippets for
   `IndexOnly`; `/view` hydrates evidence with `excerpt: Option<String>` gated by
   `License::redistributable()`; `/attest` refuses a model answer that overlaps
   gated context. The shell receives bodies only on the internal model-context
   seam, and the public answer is structurally checked before return.
2. **Entitlement *decision* in the shell; sector *filtering* also in core SQL.**
   Defense in depth: a shell bug can grant wrong sectors, never bypass the filter.
3. **The core never calls an LLM.** Embeddings round-trip through the shell;
   `/retrieve` takes `model` + `query_vector`.
4. **Full bodies are served on internal `/retrieve` and `/docs`** — model context
   is analysis, not redistribution, and these are loopback-internal, not public.
   Any model output derived from that context must pass through `/attest` before
   a public response.
5. **Source selection is core business.** `/ingest` takes `{sectors, sources?}`;
   every named source is validated against `sectors` (a source outside
   entitlement is refused, not run). Omitting `sources` preserves pre-v0.6
   behavior; a regression test pins this.
6. **Harvest cursors live in the core store.** `cursors(source_id, cursor,
   high_water, updated_at)`: `cursor` is the in-flight `resumptionToken`
   (checkpointed after every page ⇒ interrupted harvests resume mid-set);
   `high_water` is the max datestamp of the last completed harvest, replayed as
   `from=` for incremental fetch, advanced **monotonically** (ISO dates ⇒
   lexicographic max is chronological max).
7. **Provider vocabulary normalizes *into* the neutral event set, never out.**
   Billing speaks `subscription.created|updated|deleted|key_rotated`; Stripe
   enters through `adapters/stripe.py`. A second provider is a second adapter, not
   a change to the store or entitlement model.
8. **Dedup identity is a corpus property.** `canonical_id` is re-materialized from
   the global rule (earliest by `(published_day, id)`) on every ingest that adds
   rows. The 64-bit `simhash(title + body)` is materialized at ingest or
   migration and refreshed on document updates; `/view` and canonical assignment
   consume that persisted value, and a missing value is an error rather than an
   invitation to hide a failed migration by recomputing. `/retrieve` keeps
   whichever near-dup the *query* ranked higher — relevance is a property of the
   question, not the corpus. Only the persisted fingerprint is reused there.

## 4. The robots subsystem (two gates, one direction)

- **Publisher policy** — fetched from the real `/robots.txt` (`RobotsCache`,
  `crates/compliance`): per-origin, TTL 24h, bounded to 512 origins, and the fetch
  itself goes through the per-host politeness limiter.
- **Operator deny-list** — `RobotsGate::new(&["/private","/admin"])`, applied on
  top; can only ever refuse **more**.

Pinned dispositions:
- **Fail-closed, and the 4xx/5xx distinction is not cosmetic.** 2xx ⇒ the body
  governs (empty body = valid allow-all ≠ 404). 5xx / DNS / TLS / timeout ⇒
  Unreachable ⇒ take nothing. 4xx ⇒ Unavailable ⇒ **per-source**
  `robots_on_missing` decides, defaulting to Deny; a typo or omission fails
  closed.
- **Opting in reinterprets ABSENCE ONLY.** `robots_on_missing: "allow"` changes
  the 404 case and nothing else; an explicit `Disallow` is still obeyed, and an
  Unreachable origin still fails closed.
- **A fixture read is not a request.** `gate()` takes a `Reach`; a fixture-backed
  source never fetches `robots.txt`. Pinned by test.
- **A published `Crawl-delay` can only slow us down**, never speed us past our own
  floor (2 rps).
- **Politeness is process-scoped (HC8):** `HostLimiters` and `RobotsCache` in
  `AppState`.

**Redirects are re-gated before the next request (v0.8/T5).** Both
`reqwest::Client`s in `crates/ingest/src/net.rs` use `Policy::none()`. Document
redirects are resolved manually (maximum 10 hops), and the full publisher +
operator gate runs before each hop. A cross-origin `Location` therefore causes
the new origin's robots policy to be fetched and honored before document bytes
are requested; a same-origin hop reuses the process-scoped cache. Robots-file
redirects fail closed rather than silently moving to another origin.

## 5. Endpoints (core, loopback 127.0.0.1:8788)

| endpoint | method | purpose | gated? |
|---|---|---|---|
| `/health` | GET | liveness | — |
| `/sectors` | GET | sector list | — |
| `/ingest` | POST | harvest `{sectors, sources?}` | internal |
| `/view` | GET | analyzed corpus; excerpts gated by license | **excerpt gated** |
| `/search` | GET | ranked docs; snippets nulled for IndexOnly | **snippet gated** |
| `/retrieve` | POST | context assembly; full bodies (model context) | internal |
| `/embeddings/missing` | GET | backfill work queue | internal |
| `/embeddings` | POST | vectors posted back by the shell | internal |
| `/signals/record` | POST | shell posts signals back | internal |
| `/docs` | GET | full documents | internal |
| `/attest` | POST | `{answer, context_doc_ids}` ⇒ `{clean_answer, violations[]}` | **enforces HC1** |

The public surface is the shell's `/v1/*`. The core is loopback-only; `/retrieve`
and `/docs` carry full bodies only for analysis, and `/attest` prevents copied
IndexOnly context from reaching `/v1/ask`.

## 6. Invariant map (which invariant lives where, and why)

| invariant | enforced in | why there |
|---|---|---|
| HC1 no gated text public | core (`/search`, `/view`; `/attest` for `/v1/ask`) | the shell is rewritable; an invariant a rewrite can delete is not one |
| HC2 sector filtering | core SQL | a shell bug must not bypass it |
| HC3 no LLM in core | core (by omission) | keeps the engine deterministic and offline-testable |
| HC8 politeness | core `AppState` | a TTL / limiter that doesn't outlive the request is theatre |
| HC9 atomic-JSON persistence | shell + core store | cursors are the one SQLite exception, by their nature |
| HC12 lock discipline | CI (`--locked`, MSRV job) | the lock *is* the build; its format is part of MSRV |
| HC13 fixtures ≠ wire | tests + live-run policy | three bugs came from believing otherwise |

## 7. The decision-log discipline

Non-trivial "why not X" decisions are recorded in `STATE.md §6` with the
measurement that settled them, and a struck reason is *removed* rather than kept
(a dead reason is worse than none). `feed-rs`, `texting_robots`, and LSH banding
are all *correctly absent*, and the log says why, with numbers. New dependency or
scale decisions follow the three-clause gate in `AGENTS.md §3`.
