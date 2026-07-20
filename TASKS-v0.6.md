# TASKS.md — intel-platform v0.6 work order

**Audience:** an autonomous coding agent (Claude Opus 4.8 / Claude Code, or equivalent) with a shell, a Rust toolchain, and network access. **Read `STATE.md` and `README.md` in full before writing any code.** This document is the authoritative task list; STATE.md §4 is its source.

**Starting point:** v0.5. 11 Rust tests + 31 shell tests green. Core untouched since v0.4. v0.5 added (shell-only): hashed API keys (`security.py`), billing webhook (`billing.py`, `POST /v1/billing/webhook`, `SubscriptionStore`), scheduler (`scheduler.py`, `deploy/`).

---

## 0. Environment prerequisites (verify before T1)

- Rust **1.75+** (`rustup` preferred; this was the blocker last cycle — the previous sandbox had no toolchain).
- Python **3.12**, venv, `pip install -r shell/requirements.txt`.
- Network to crates.io / pypi. Live arXiv access only needed for T4's optional smoke test.
- Optional for T7: an OpenAI-compatible endpoint (vLLM box or DeepSeek API) reachable from the machine.
- Shell note: if the container shell is `dash`, avoid brace expansion; write explicit loops.

---

## 1. Hard constraints — apply to EVERY task, no exceptions

- **HC1 — License gating stays in core.** IndexOnly excerpt withholding is enforced in Rust (`crates/store` / `cored` responses). No change may create a path where the shell can emit gated text to an end user. The internal `/retrieve` and `/docs` endpoints intentionally serve full bodies (LLM context = analysis, not redistribution) — do not "fix" that.
- **HC2 — Sector filtering stays in core SQL.** The shell *decides* entitlements (API key → client → sectors); the core *enforces* the sector filter in SQL as defense in depth. Never move filtering into Python.
- **HC3 — The core never calls an LLM.** The shell embeds queries/documents and posts vectors to the core. Keep it that way.
- **HC4 — No raw secrets on disk.** Subscriptions persist `key_hash` (HMAC-SHA256), never raw `api_key`. All secret comparisons constant-time (`hmac.compare_digest`). Webhook bodies verified by HMAC before parsing side effects.
- **HC5 — Backward compatibility.** Public API shapes (`/v1/*`) unchanged unless a task explicitly says otherwise. Sector-only `/ingest` requests must behave byte-identically after T3. Legacy raw-`api_key` subscription records must still resolve.
- **HC6 — Zero-warning builds, green baseline.** `cargo check --workspace` with 0 warnings; all existing tests stay green. New behavior ⇒ new tests.
- **HC7 — Sourcing policy.** No paid commercial data-gatekeeper APIs. Free official channels only. LLM APIs are exempt (they process already-ingested documents).
- **HC8 — Compliance in live fetching.** robots gate + polite rate limiter (`crates/compliance`) must be honored on every network request, including between OAI-PMH pages (arXiv asks ~3s between requests; honor 503 `Retry-After`).
- **HC9 — Atomic persistence.** Any state written to disk (cursors excepted — those live in SQLite) uses write-temp-then-`os.replace` (shell) or a transaction (core).
- **HC10 — The seam is a contract.** Any change to a `cored` endpoint requires, in the same task: `shell/intel_shell/core_client.py`, `examples/coreClient.ts`, README's "core API contract" section, and STATE.md all updated together.
- **HC11 — Doc hygiene.** Finish every task by updating STATE.md (§3 verified, §4 next steps) and README where user-facing. At the end of the whole cycle, bump versions (`Cargo.toml` workspace if core changed, `shell/intel_shell/__init__.py`) and regenerate the repomix XML.

## 2. Operating rules for the executing agent

- Run the full baseline (T1) before touching code; run the full suite after every task.
- One task per "commit-sized" change; do not interleave tasks.
- If a task's decision gate says "skip," document the decision in STATE.md rather than forcing it.
- Do not refactor opportunistically outside a task's stated scope, especially in `crates/`.

---

## 3. Tasks (dependency order)

### T1 — Toolchain bring-up & baseline verification  [P0, no code changes intended]
**Do:** Install Rust; `cargo check --workspace` (expect 0 warnings), `cargo test` (expect 11: core 3, enrich 2, extract 3, retrieve 3), `PYTHONPATH=shell python3 -m pytest shell/tests` (expect 31). Record exact rustc/cargo versions in STATE.md.
**Gate:** If a newer rustc introduces warnings/deprecations, fix minimally and list every touched line in STATE.md.
**Done when:** all counts green and recorded; no functional diffs.

### T2 — `cargo update` + evaluate `feed-rs` swap in `crates/ingest`  [P2, optional by design]
**Do:** `cargo update`; re-run baseline. Then *evaluate* replacing the hand-rolled RSS/Atom parsing in `crates/ingest/src/rss.rs` with `feed-rs`.
**Constraints:** `Source` trait signature and the registry's one-match-arm-per-source-type structure unchanged. `net.rs` stays behind `--features net`. Fixture-driven determinism preserved.
**Testing objective:** a parse-equivalence test — for each fixture in `fixtures/` (techwire, osdaily, finance), the swapped parser must yield identical document ids, titles, timestamps, and license assignments to the current parser's committed expectations.
**Decision gate:** if `feed-rs` drags heavy transitive deps, breaks determinism, or changes any field, **skip the swap** and record why. `cargo update` alone still counts as completing T2.
**Done when:** baseline green post-update; swap either merged with equivalence test green, or documented-skipped.

### T3 — Core: per-source ingest → true per-source cadence  [P1, core + shell]
The v0.5 scheduler's finest grain is per *sector* because `POST /ingest` takes only a sector list. Two feeds in one sector cannot run on independent clocks.
**Do (core):** extend `/ingest` to accept an optional `sources: [string]` (source ids as named in `config/core.json`) alongside `sectors`. Semantics: `sources` present ⇒ run exactly those sources (each still validated against the requesting sector entitlement passed in the call); absent ⇒ current sector behavior, unchanged.
**Do (shell):** `CoreClient.ingest(...)` gains `sources=None`; `scheduler.build_jobs` fans out per-source jobs when `config/schedule.json` specifies `sources` with per-source cadence (schema already anticipates this — see the `sources` map with per-name intervals); per-sector remains the fallback. Update `examples/coreClient.ts` (HC10).
**Testing objectives:**
- Rust: registry unit test — source-id filtering selects exactly the named connectors; unknown id ⇒ structured error, not a panic.
- Rust: `/ingest` handler test — sector-only request produces identical results to pre-change (HC5 regression guard).
- Shell: scheduler test — a schedule with two sources in one sector at different intervals yields two independent jobs with correct `next_run`s.
- E2E: run `cored` live; tick the scheduler such that only one source is due; verify only that source's docs ingested (doc counts + audit rows).
**Done when:** all above green; docs updated per HC10.

### T4 — Core: live arXiv harvesting — resumptionToken paging + high-water marks  [P1, core]
**Do:** in `crates/store`, add a `cursors` table `(source_id TEXT PRIMARY KEY, cursor TEXT, high_water TEXT, updated_at TEXT)`. In `crates/ingest/src/arxiv_oai.rs` (net path): follow `resumptionToken` until the empty-token terminator; persist the token after each page so an interrupted harvest resumes; on completed harvests, store the max `datestamp` seen and use it as `from=` on the next run.
**Constraints:** HC8 strictly (≥3s between pages via the existing limiter; honor 503 `Retry-After`). Offline/fixture mode remains the default; live path stays behind `--features net`. Do **not** add a `/cursors` endpoint unless the shell demonstrably needs visibility — default is not to.
**Testing objectives (all offline, fixture-driven):** add a multi-page OAI fixture chain (page1 → token → page2 → empty token). Unit tests: (a) pagination follows the chain and ingests the union; (b) cursor persisted mid-harvest and resumed correctly after a simulated interrupt; (c) empty token terminates; (d) subsequent harvest issues `from=` = stored high-water mark; (e) rate limiter consulted between pages (inject a counting fake).
**Optional:** one live smoke test against arXiv behind `--features net`, manually invoked, never in CI.
**Done when:** fixture tests green; cursors survive process restart; STATE.md documents the cursor schema.

### T5 — Seam hardening for multi-host  [CONDITIONAL — only if core and shell will run on different hosts]
`CORE_TOKEN` is already implemented on both sides; loopback TCP is the designed default.
**Do (if triggered):** prefer a Unix domain socket for same-host isolation (`CORE_BIND=unix:/run/intel/cored.sock`; shell via httpx UDS transport) — simpler than mTLS. mTLS only for a genuine cross-host split.
**Testing objective:** integration test that the shell completes a full pipeline run over the UDS; TCP path unchanged.
**Gate:** single-host deployment ⇒ mark deferred in STATE.md and move on. Do not build speculative mTLS.

### T6 — Billing/keys follow-ons  [P1, shell-only — core untouched]
Three independent sub-tasks; the neutral event shape consumed by `billing.apply_event` must NOT change (adapters normalize *into* it).
- **T6a — Key rotation/revocation.** Allow a client record to carry multiple hashes (e.g., `key_hashes: [..]`, keeping `key_hash` readable as legacy singular). Add webhook event `subscription.key_rotated` (`data.key_hash` new, optional `data.retire_after` grace). Extend `tools/hash_subscriptions.py` or add a small admin CLI for offline rotation.
  *Tests:* old+new keys both resolve during grace; retired hash rejected; persisted file never contains a raw key.
- **T6b — Real provider adapter.** `shell/intel_shell/adapters/stripe.py` (or the provider actually used): verify the provider's signature scheme (Stripe: `Stripe-Signature: t=…,v1=…` HMAC over `{t}.{body}`, constant-time), then map `customer.subscription.created/updated/deleted` → neutral events. Mount at `POST /v1/billing/stripe` or dispatch by header — the neutral `/v1/billing/webhook` stays as-is.
  *Tests:* signed-fixture round-trip flips sectors; tampered timestamp/signature ⇒ 401; unknown provider event types ignored, not erroring.
- **T6c — Datastore-backed `SubscriptionStore`.** A SQLite implementation behind the same interface (`all/get/resolve_token/upsert/remove/save`), selected by env (e.g., `SUBSCRIPTIONS_PATH=sqlite:///…`). Include a one-shot JSON→SQLite migration path.
  *Tests:* full store contract test run against BOTH backends; migration preserves hashes and sectors byte-exact.
**Done when:** each sub-task's tests green; the existing 31 (now more) all green; README env-var docs updated.

### T7 — Point the LLM at a real endpoint  [P1, ops + verification, minimal code]
**Do:** set `LLM_BASE_URL`/`LLM_API_KEY` (+ `LLM_CHAT_MODEL`/`LLM_EMBED_MODEL`) at the vLLM box or DeepSeek. Run the full pipeline for both clients; exercise `/v1/ask`; run `--llm-enrich` and confirm it now yields substantive entity suggestions (the mock intentionally yields none).
**Testing objective (checklist, not unit tests):** embeddings populate (fusion no longer BM25-only; `retrieval.notes` clean); `/v1/ask` cites real docs and honors `context_suppressed`; **HC1 spot-check: ask a question whose best evidence is an IndexOnly doc and confirm the public answer's snippets/citations never reveal gated text.** Record model names + observed latency in STATE.md.
**Gate:** no endpoint reachable ⇒ defer, do not mock-and-declare-done.

### T8 — Scale swaps  [DEFERRED — design-level only]
Postgres/pgvector, tantivy, LSH near-dup, materialized views: all deliberately behind existing surfaces. **Do not implement this cycle** unless the owner explicitly re-prioritizes; if touched at all, produce a design note only.

### T9 — Known-limitation pick-ups  [P2, each small & independent — do after P1s, skip freely]
1. Canonical-ids at ingestion (proper near-dup fix; today suppression happens at context assembly) — core; test: duplicate ingest maps to one canonical id.
2. `/view` response caching (currently recomputes per request) — core; invalidate on ingest; test: second call cheap, post-ingest call fresh.
3. `Day` month-boundary phantom days — core; unit tests across Jan→Feb and Dec→Jan boundaries.
4. Robots gate: prefix-only matching + one shared limiter → path-pattern matching + per-host limiters — core.
5. FTS append-only triggers → handle UPDATE/DELETE — core; test: edited doc searchable under new text only.
6. `_default_app()` resolves `config/subscriptions.json` relative to CWD — shell; resolve relative to repo root, keep `SUBSCRIPTIONS_PATH` override; test with a changed CWD.

---

## 4. Global definition of done (the whole cycle)

1. `cargo check --workspace`: **0 warnings**. `cargo test`: all green (count > 11 — record the new number). `pytest shell/tests`: all green (count > 31 — record).
2. **Golden E2E regression** (run `cored` + `tools/mock_openai.py`, then the acme pipeline) — expected unless a task legitimately changes it, in which case explain the delta in STATE.md:
   - acme ingests **13** docs (Finance skipped); dedup drops `techwire::tw-004`, keeps `osdaily::osd-004` (hamming 12);
   - signals: **DeepSeek RISING z=10.0** (3-source corroboration), vLLM RISING z≈2.67, NVIDIA+Qwen CORROBORATED, "Helios Labs" EMERGING;
   - immediate re-run: **+0 new**; quant-desk sees only its **1** doc; audit rows carry correct kind strings.
3. Public API spot-checks: bad key ⇒ 401; entitlement-disjoint search (acme 6 hits vs quant 0 for "deepseek"); IndexOnly snippet null in `/v1/search`; brief renders "excerpt withheld"; webhook: unset secret ⇒ 503, bad sig ⇒ 401, signed event flips sectors and persists hashed.
4. Demo credentials for verification: `ak_acme_7f3d9c` (science+technology), `ak_quant_2b81aa` (finance); hashed equivalents in `config/subscriptions.hashed.json`.
5. STATE.md bumped to v0.6 with: verified-in-environment section, per-task outcomes (done / skipped-with-reason / deferred), updated next steps. README + `examples/coreClient.ts` consistent with any contract change (HC10). Versions bumped; repomix XML regenerated.

## 5. Env var reference (current)

**Core:** `CORE_CONFIG` `CORE_ENTITIES` `CORE_DB` `CORE_BIND` `CORE_TOKEN`.
**Shell:** `CORE_URL` `CORE_TOKEN` `SUBSCRIPTIONS_PATH` `LLM_BASE_URL` `LLM_API_KEY` `LLM_CHAT_MODEL`/`LLM_EMBED_MODEL` (fallback `LLM_MODEL`), `API_KEY_PEPPER` (regenerate hashes if changed), `BILLING_WEBHOOK_SECRET` (unset ⇒ webhook 503).
