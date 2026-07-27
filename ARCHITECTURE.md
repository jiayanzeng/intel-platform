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
                /attest /embeddings(/missing,/stats) /signals/record /docs
  crates        core compliance ingest extract enrich analyze
                store registry view retrieve
```

The design intent: **source-side invariants live in the core so product-layer
iteration cannot bypass them.** `briefing.py` can be rebuilt from scratch and
still cannot leak gated text, because it never receives gated text. The
shell-owned public answer path is the recorded A4 exception: the shipped shell
attests it correctly, but an arbitrary rewrite is not constrained until public
egress crosses a core-owned boundary. That exact boundary is why the placement
decisions below are load-bearing.

## 2. Config ownership

| file | owner | holds |
|---|---|---|
| `config/core.json` | core | sectors, sources, licenses |
| `config/entities.json` | core | gazetteer |
| `config/subscriptions.json` (or `sqlite:///…`) | shell | clients, sectors, keys |
| `config/schedule.json` | shell | per-source and per-sector cadence |
| `config/protected-artifacts.json` | evidence control | immutable artifact facts and chained admissions |

Core-owned config describes *what exists and how it may be used*; shell-owned
config describes *who may see it and when to fetch it*. Do not cross these.

**HC9 — persistence scope is explicit.** HC9 governs shell-owned
configuration: atomic JSON is the default, and any new SQLite-backed shell
configuration needs a recorded reason. The core archive is SQLite by design.
The recorded SQLite scopes are:

- **Harvest cursors:** live beside documents so a page and its continuation
  state commit in one transaction.
- **Subscriptions:** shell-owned configuration may explicitly select
  `sqlite:///…` for transactional billing, key rotation, and revocation;
  atomic JSON remains the default.
- **Core store tables:** `documents`, `embeddings`, and `signals_history`
  are archive/query state, not shell-owned configuration.

**Protected-artifact admission is an executable append-only chain.** Manifest
schema v2 requires every artifact's current SHA-256 to equal its newest
admission record, and each new record's `prior_sha256` to equal the preceding
record's SHA-256. Every record also names the admitting task/date, captured
wire command and output reference, operator approval, and whether it is
retroactive. Validate the record chain with
`python3 tools/evidence_artifacts.py validate`; then prove the recorded bytes
and corpus facts with `./run verify-artifacts`. The two initial v0.10/A2
records are explicitly retroactive references to prior wire/B0 evidence, not
new harvest claims.

## 3. Load-bearing placement decisions (do not move casually)

Condensed from `STATE.md §2`.

1. **License gating lives in the core.** `store.search` nulls snippets for
   `IndexOnly`; `/view` hydrates evidence with `excerpt: Option<String>` gated by
   `License::redistributable()`; `/attest` refuses a model answer that overlaps
   gated context. The shipped shell receives bodies only on the internal
   model-context seam and checks the answer before return. A4 proved that the
   shell remains in this path's trusted computing base: a receipt cannot tell
   the core which retrieval actually supplied a shell-owned prompt or force a
   rewritten shell to call `/attest`. Supporting an untrusted shell requires a
   non-bypassable, core-owned public-response boundary; HC3 still keeps the
   model call itself out of core.
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
6. **Harvest pages and cursors are one core-store transaction.**
   `cursors(source_id, cursor, high_water, pending_high_water, updated_at)`:
   each parsed page's documents, global canonical-id rematerialization, next
   `resumptionToken`, and pending max datestamp commit atomically. An
   interruption can therefore neither advance past documents still in memory
   nor forget a prior page's newer datestamp. Only a final-page commit clears
   the token/pending value and advances completed `high_water`, which remains
   monotonic (ISO dates ⇒ lexicographic max is chronological max).
7. **Provider vocabulary normalizes *into* the neutral event set, never out.**
   Billing speaks `subscription.created|updated|deleted|key_rotated`; Stripe
   enters through `adapters/stripe.py`. A second provider is a second adapter, not
   a change to the store or entitlement model.
8. **Dedup identity is a corpus property.** `canonical_id` is re-materialized
   from the global rule (earliest by `(published_day, id)`) inside the same
   SQLite transaction on every store write path that adds, changes, or removes
   rows. The 64-bit `simhash(title + body)` is materialized at ingest or
   migration and refreshed on document updates; `/view` and canonical
   assignment consume that persisted value, and a missing value is an error
   rather than an invitation to hide a failed migration by recomputing.
   `/retrieve` keeps whichever near-dup the *query* ranked higher — relevance is
   a property of the question, not the corpus. Only the persisted fingerprint
   is reused there.

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
| `/embeddings/missing` | GET | sector-filtered backfill work queue | internal |
| `/embeddings/stats` | GET | stored vector count/dimension for one model key | internal |
| `/embeddings` | POST | vectors posted back by the shell | internal |
| `/signals/record` | POST | shell posts signals back | internal |
| `/docs` | GET | sector-filtered full documents | internal |
| `/attest` | POST | `{answer, context_doc_ids}` ⇒ `{clean_answer, violations[]}` | **enforces HC1** |

The public surface is the shell's `/v1/*`. The core is structurally loopback-only:
startup resolves `CORE_BIND`, checks every resulting address, and refuses before
binding if any address is not loopback. `/retrieve` and `/docs` carry full bodies
only for analysis, and the shipped shell sends model output through `/attest`
before `/v1/ask` returns it. This prevents copied IndexOnly context on the shipped
path, but does not constrain an arbitrary rewrite that omits the call or supplies
a false scope (A4 accepted risk). Every endpoint that returns document bodies
takes an explicit sector set whose predicate is enforced in core SQL;
`/embeddings/missing` has no maintenance exception.

## 6. Invariant map (which invariant lives where, and why)

| invariant | enforced in | why there |
|---|---|---|
| HC1 no gated text public | core (`/search`, `/view`); core + trusted shipped shell (`/attest` for `/v1/ask`) | source gating is unconditional; answer attestation is enforced on the shipped path, but a rewritten shell can still bypass or falsify that handoff until public egress crosses a core-owned boundary (A4 remains open) |
| HC2 sector filtering | core SQL, including `/docs` and `/embeddings/missing` | every body-returning query requires an explicit sector set and fails closed when it is empty, so a shell bug cannot bypass filtering |
| HC3 no LLM in core | core (by omission) | keeps the engine deterministic and offline-testable |
| HC8 politeness | core `AppState` | a TTL / limiter that doesn't outlive the request is theatre |
| HC9 persistence scope | shell configuration + core store | shell config defaults to atomic JSON; the three recorded SQLite scopes above are explicit |
| HC12 lock discipline | CI (`--locked`, MSRV job) | the lock *is* the build; its format is part of MSRV |
| HC13 fixtures ≠ wire | tests + live-run policy | three bugs came from believing otherwise |
| corpus identity atomicity | core store transaction + private canonical-distance constant | every durability unit that adds, changes, or removes documents rematerializes global canonical identity before the same commit; production callers cannot supply a different threshold |
| repository absence claims | registered `invariant-scan` rules in local/hosted CI | each scoped claim has executable source coverage and a captured planted failure; prose-only absence is not accepted |
| routine model-profile authorization | shipped L1 controller allowlist + pure fail-closed guards + repository pins | the current controller can construct only the five-container/read-only command set and refuses unsafe observed state, but an edited controller can rewrite this client-side boundary; the server-enforced L2 forced-command wrapper remains open and scheduled |

The last row is defense for the shipped controller, not a server-side security
invariant. L1 and its repository pins detect or refuse the current implementation;
they do not authorize future controller edits. Likewise, the HC1 row still
describes the trusted shipped shell and does not close A4.

## 7. The decision-log discipline

Non-trivial "why not X" decisions are recorded in `STATE.md §6` with the
measurement that settled them, and a struck reason is *removed* rather than kept
(a dead reason is worse than none). `feed-rs`, `texting_robots`, and LSH banding
are all *correctly absent*, and the log says why, with numbers. New dependency or
scale decisions follow the three-clause gate in `AGENTS.md §3`.

## 8. Execution cycles and artifact releases

An execution-cycle name is a planning and evidence namespace, not an artifact
version. Completing `TASKS-vX.Y-EXECUTION.md` does not by itself create, imply,
or move a `vX.Y.Z` release.

Release identity is chosen explicitly at the cycle-closing release task after
the measured diff is classified:

- runtime, storage, or public/API behavior requires the corresponding minor
  release;
- operations and evidence-only changes may use a patch release;
- a cycle with no shipped change may close with no release.

For an actual release, the authoritative mapping is the annotated Git tag to
its exact release commit. The Rust package, Python package, public FastAPI
literal, `STATE.md` header, and newest `CHANGELOG.md` release must agree with
that tag. A separate append-only progress audit may follow the tagged commit;
it records the release commit hash and does not move the tag. A no-release
close instead names the intentionally unreleased commits and leaves every
version source and tag unchanged.
