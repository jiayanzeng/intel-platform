# STATE.md — intel-platform handoff

**As of:** 2026-07-24 · **Version:** v0.7.4 (core-shell) · **Status:** **92 Rust workspace tests green with 0 _rustc_ warnings** (`cargo check --workspace --locked --all-targets` under `RUSTFLAGS=-D warnings`, both the offline and `--features net` builds), **20 net-path ingest tests green**, and **88 shell tests green** against failure-capable doubles (with 1 Starlette deprecation warning). Clippy and fmt are clean on pinned Rust 1.91.1 and blocking in CI; the locked offline graph is also clean under Rust 1.78.0. B0.1 re-measured the complete entering state and registered both evidence databases by exact SHA-256. **G1 is complete:** `./run golden` owns a disposable cross-language lifecycle, asserts all eleven regression anchors, fails demonstrably on fixture drift, and runs as a blocking CI job. **P1 is complete:** bare live harvests resolve to unique timestamp/PID databases, both evidence databases are refused as targets, and their hashes are verified by `./run verify-artifacts` and `./run test`. **E1 is complete:** one embedding model key has exactly one stored dimension, mismatched legacy rows are visible in retrieval diagnostics, and a fresh verifier run cannot pass without a real embedding request whose dimension matches stored statistics. HC1 is structurally enforced on `/v1/ask` by core `/attest`; cross-origin redirects are manually re-gated before the next request; `/view` consumes persisted SimHash fingerprints with a verified legacy backfill. **T2 is complete:** two capped live arXiv runs proved durable interruption-resume. **T4C/T4H are complete:** split provider profiles are secret-safe, loopback core calls ignore ambient proxies, real-model verification owns an isolated fixture DB, required stages fail fast, and provider waits are explicitly bounded. **T4L is complete:** an SSH-forwarded live probe confirmed the chat server's exact 501 `--embeddings` diagnosis and measured the dedicated `embeddinggemma-300M-Q8_0.gguf` server at 768 dimensions; `.env` now resolves both direct LAN roles explicitly. **T4P's verifier implementation and failure controls are complete, but its live exercise is deferred:** the adversarial public path reports `GUARD FIRED`, `NOT EXERCISED`, or `LEAK` and preserves `/attest` violations, but no real model has tripped it yet. **T4 remains deferred at embedding backfill:** its last required uninterrupted run ingested 13 fresh fixtures, then the then-configured DMXAPI embedding endpoint returned HTTP 503 in 0.16s; the new local embedding role has not yet been exercised by that full run. T7 single-flight remains deferred because the shipped scheduler is one synchronous writer.

**v0.7.4 acts on a detailed third-party (Codex) review that found the real root cause of the failed on-site harvest — plus three orchestration bugs and one test-isolation bug, all mine, all now fixed.** The 34-minute silence was *not* a long harvest and *not* the harvest logic; it was the `run` harness failing against an environment condition and then hanging on a control-flow bug:

- **Root cause — a foreign process owned the port.** An orphaned `cored` from another copy of the repo (in the operator's `.Trash`) was still listening on 8788. This checkout's server failed to bind (`Address already in use`) and died.
- **Harness bug 1 — false readiness.** The readiness poll hit `/health` and got a 200 *from the orphan*, so it announced our server ready when ours had died. **Fixed:** `_start_cored` now (a) refuses up front if the port is already serving (`port_is_foreign`), naming the offending PID and the exact `lsof`/`kill` commands, and (b) waits with a **pid-aware** check that fails fast if the process we launched dies.
- **Harness bug 2 — infinite poll under `set -e`.** The ingest ran in a backgrounded subshell that wrote a completion sentinel *after* `curl`; when `curl` timed out non-zero, `set -e` aborted the subshell before the sentinel was written, and the watch loop span forever (~29 of the 34 minutes). **Fixed:** the subshell runs `set +e` and **always** writes the sentinel with curl's exit code; the watch loop is additionally time-bounded.
- **Harness bug 3 — `down` can't reach the orphan.** A pidfile only tracks servers we started. **Fixed:** `cmd_down` now reports a still-held port after cleanup, with the PID and kill command. (Also: `_start_mock_llm` still used `setsid`; switched to `nohup` — another latent macOS break.)
- **Test-isolation bug — parallel temp-DB collision.** `tmp_db()` named the per-test SQLite file from `SystemTime` nanos only; two parallel test threads in the same tick got the same path and clobbered each other (seen as a "fresh" DB already holding another test's rows — `new=4, fetched=7`). **Fixed:** a process-global atomic counter + pid in the name guarantees a distinct path per call. `cargo test` is now deterministic under default parallelism (verified across repeated runs).

**On the "0 warnings" claim — B0 correction and T6 resolution, measured 2026-07-20.** "0 warnings" originally meant *rustc* warnings (`-D warnings` on `cargo check`), and that remains true. B0 proved the prior claim that the test module had been moved last was **false**: clippy exited 101 on `clippy::items_after_test_module`, and fmt found diffs in 13 Rust files. T6 moved the SQLite vector layer before the test module and applied rustfmt in the separate lint-fix commit `097b017`. After that fix, `cargo clippy --workspace --locked --all-targets -- -D warnings` and `cargo fmt --all -- --check` both exit 0. The two `clippy::unnecessary_map_or` crate-level allows remain deliberate in `intel-compliance` and `arxiv_oai`: the suggested `Option::is_none_or` is Rust 1.82+, above the offline 1.78 floor. CI's lint job is now explicitly blocking (`continue-on-error: false`).

**T2 interruption-resume is complete on the live wire (2026-07-23).** The original 2026-07-20 capped run cleared its token because `complete()` ran after the cap. A strengthened fake reproduced that failure before the repair; injected commit and SQLite-trigger failures then proved the atomic page guard can fail and rolls documents and cursor back together. On 2026-07-23, live run 1 fetched 1,300 real arXiv records and durably stored token `verb%3DListRecords%26metadataPrefix%3Doai_dc%26from%3D2026-07-21%26until%3D2026-07-22%26set%3Dcs%26skip%3D522`. After stopping and restarting `cored`, live run 2's first request carried that exact token and added the next 1,300 records; its next token advanced to `from%3D2026-07-22...skip%3D88`. Both runs reported `ok=true`, 0 parse errors, and a real `Unavailable(allow)` robots disposition with 0.500s effective crawl delay. No 503/Retry-After was observed. `data/core.db` remained byte-identical.

**T4 real-model verification remains DEFERRED at its embedding gate (updated 2026-07-23).** The operator first exercised two chat candidates as shared providers: the LAN server returned **501 Not Implemented** from `POST /v1/embeddings`, DeepSeek returned **404 Not Found**, and a later Codex LAN retry failed with **No route to host**. After T4C split the roles, the operator configured DMXAPI embeddings and ran the isolated verifier twice. Both runs ingested 13 fresh fixtures; both DMXAPI calls returned **503 Service Unavailable**, so embedding backfill and hybrid fusion failed. The first run nevertheless completed the independent LAN-chat/public-HC1 leg: `/v1/ask` returned 4 citations, all 4 cited documents were IndexOnly, and no 16-token gated overlap escaped. The verifier correctly summarized **3/5 required checks passed**, which is partial evidence, not T4 completion. The second run repeated the 503s and then stalled in chat until the operator interrupted it after 1m41s, exposing a separate verifier fail-fast/timeout defect. A fresh Codex one-vector probe independently reproduced the DMXAPI 503. T4C's deterministic mock control remains harness evidence only; it is not substituted for the failed real embedding role.

**Protected archive correction (measured before and after T4C on 2026-07-23).** Between the T2 handoff and T4C preflight, the operator reported running a bare zero-document arXiv harvest against `data/core.db`. Direct measurement found the logical corpus unchanged at **1,764 rows, 0 NULL `simhash`, 0 NULL `canonical_id`, integrity `ok`**, but the file was no longer byte-identical: SHA-256 is now `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`, size **6,729,728 bytes**, mtime `2026-07-23 20:08:13 +0800`, and the `arxiv-cs` cursor row is `cursor=NULL`, `high_water=2026-07-20`, `pending_high_water=NULL`, `updated_at=2026-07-23 12:08:13`. T4C made no further change to that file; its golden and verifier runs used temporary databases. Bare future harvests now resolve to `data/live-smoke.db`.

**Prior point releases (unchanged, kept for the record):** v0.7.1 per-source robots opt-in (§2.12); v0.7.2 `max_pages` cap + timeouts + progress logging; v0.7.3 removed Python 3.12-only f-strings from `run` (crashed on the on-site 3.11).

1. **arXiv migrated its OAI-PMH endpoint.** `export.arxiv.org/oai2` now **301-redirects** to `oaipmh.arxiv.org/oai` (observed live). `config/core.json` now points at the canonical host directly, which also sidesteps the redirect-origin gap (below) for arXiv specifically.
2. **The harvest was blocked by a robots FALSE POSITIVE, not by the gate working correctly.** `oaipmh.arxiv.org` serves no `robots.txt` (a 404 HTML page). The v0.7 default is fail-closed on 404 (`MissingPolicy::Deny`), which is correct for an *unknown* host but wrong for a cooperative, operator-configured endpoint that publishes no robots.txt *on purpose*. The block was the system refusing exactly the access arXiv built the endpoint to serve. **Fixed in v0.7.1** — see §2.12.
3. **The redirect-origin gap was confirmed live and is now resolved in v0.8/T5.** `export.arxiv.org/oai2` 301s to a different origin whose robots.txt the old automatic redirect path would not have read. Both clients now disable automatic redirects, and document redirects are followed manually only after the next origin passes the full robots gate.

**And a process note that matters more than the code:** the on-site tester, working with a different AI assistant, produced a status report concluding *"T2 is verified... blocked by the system's own high-security policy... performing as designed in a live adversarial environment."* Every clause of that is wrong — T2 fetched nothing, the block was a false positive, and arXiv is the least adversarial source imaginable. It is the exact failure this project was built to resist (**a claimed property that nothing executed**), and it is worth recording that the failure mode is attractive enough that a capable assistant reached for it unprompted. The fix for the class is unchanged: report what the wire actually did, and treat "blocked" as a non-result until documents land.

**What changed in v0.7.1:**
- **Per-source robots policy (§2.12).** A new optional `robots_on_missing` on each source, default `"deny"` (the conservative fail-closed behavior for every existing source), set to `"allow"` for `arxiv-cs`. Opting in reinterprets **only** a 404; it does **not** override an explicit `Disallow` and does **not** touch the unreachable/5xx path, both of which still fail closed. Threaded `SourceCfg → source struct → gate() → RobotsCache::allowed()`. +4 tests (79 total), incl. "opting in still obeys an explicit disallow." **This replaces, correctly, the global `MissingPolicy::Deny → RfcAllowAll` sed the on-site tester tried — which both weakened the gate for all sources and, because the default lives in a `#[default]` attribute and not the literal string, silently did nothing.**
- **`./run` portability fixes** for the on-site box: `setsid` → `nohup` (setsid is not on macOS), and the arXiv reachability probe now **derives its URL from config and follows redirects** (`-L`) instead of hardcoding `export.arxiv.org/oai2`, so an endpoint move can't re-break the check. The harvest step now reports PASS/NOT-VERIFIED from the actual fetched count rather than declaring success on a request that returned zero.

**The theme of v0.7 was "stop trusting fixtures." The theme it *turned into* was "stop trusting our own notes."** Two claims this document made about itself were false, and both were found by building the thing that checks them:

1. **`robots.txt` had never been read.** The gate did correct RFC-9309 path matching against **policy we configured, not policy we fetched** — so "robots-compliant" meant "compliant with a policy we wrote ourselves," which is not a claim worth making. **T2 closes this** (§2.11).
2. **"Rust 1.75 + `--locked` still builds the offline path" (v0.6.2, §5) was FALSE from the moment it was written — and the obvious fix is a trap.** v0.6.2 committed `Cargo.lock` at **format v4**, which cargo *cannot parse* before **1.78**; `cargo +1.75 check --locked` dies at the lockfile, long before it reaches any dependency's MSRV. The claim had simply never been run. T4's MSRV job is what caught it.
   The tempting fix — re-encode the lock as v3 — **does work** (measured: 1.75 builds, 75 tests green, resolution byte-identical). **It is also not stable:** cargo 1.91 rewrites the lock back to v4 the moment it has to modify it, so v3 is a hand-edit that the next `cargo add` silently undoes. *A floor that holds only until someone touches the lock is not a floor.* **So v0.7 declares the floor that is true AND sustainable: offline ≥ 1.78** (measured on 1.75/1.76/1.78/1.91), enforced by CI. The lesson generalizes twice over: *the lockfile format is part of the MSRV surface, not just the dependency graph* — and *a claimed property that nothing executes is not a property.* This is the **third** time this project has been bitten by that exact failure (`--features net` unbuilt for two cycles; robots policy never fetched; this).

**What changed in v0.7:**
- **T2 — real `robots.txt` discovery (§2.11).** `RobotsGate::parse()` (a zero-dependency RFC-9309 parser: UA-group selection, `Allow`/`Disallow`, wildcards, `$`, `Crawl-delay`), plus `RobotsCache` — per-origin, TTL'd, bounded, **fail-closed**. `texting_robots` was evaluated and **skipped** (§6b); the hand-rolled parser was then proven equivalent to it across **368 verdicts on 16 robots.txt bodies, 0 divergences**.
- **T4 — CI (`.github/workflows/ci.yml`).** Five jobs: `core` (locked, `-D warnings`), **`net`** (the path that sat broken for two cycles precisely because nothing built it), **`msrv`** (the 1.75 floor — the job that caught the false claim above), `shell`, and a scheduled **`drift`** reporter that runs `cargo update --dry-run` and dumps every declared `rust-version` in the resolved graph, so ecosystem movement is *news* rather than a broken build.
- **T5 — LSH banding: SKIPPED, and the design note it came from is now corrected (§6c).** Built, measured, rejected. It is 246× *slower* than the scan it replaces.

## 1. Architecture

```text
SHELL (Python, product)   app.py /v1/* · auth.py keys→sectors · llm.py chat+embed
                          prompts.py · briefing.py · pipeline.py · enrichment.py
                          scheduler.py — per-SOURCE and per-sector cadence (v0.6)
        │  CoreClient (core_client.py) — the ONLY door; httpx, injectable transport
        ▼  minimal JSON API, 127.0.0.1:8788, optional x-core-token
CORE (Rust, engine)       apps/cored: /health /sectors /ingest /view /search
                          /retrieve /attest /embeddings(/missing)
                          /signals/record /docs
                          crates: core compliance ingest extract enrich analyze
                                  store registry view retrieve
```

**Config split:** `config/core.json` (sectors/sources/licenses) + `config/entities.json` (gazetteer) are core-owned; `config/subscriptions.json` (clients/sectors/keys) and `config/schedule.json` are shell-owned. Demo keys: `ak_acme_7f3d9c` (science+technology), `ak_quant_2b81aa` (finance).

## 2. Load-bearing placement decisions (do not move these casually)

1. **License gating stays in the CORE.** `store.search` nulls snippets for IndexOnly; `/view` hydrates evidence with `excerpt: Option<String>` gated by `License::redistributable()`; `/attest` refuses a model answer sharing a measured 16-token normalized phrase with IndexOnly context. Consequence: `briefing.py` never receives gated text, and `/v1/ask` cannot return copied gated context without the core replacing the entire answer with a constant refusal.
2. **Entitlement DECISION in the shell, sector FILTERING in the core.** A shell bug can grant wrong sectors, never bypass filtering.
3. **The core never calls an LLM.** Shell pulls `GET /embeddings/missing`, calls the provider, `POST /embeddings` vectors back. `/retrieve` accepts `model` + `query_vector`; `/attest` only inspects a string the shell hands it.
4. **Full bodies ARE served on internal `/retrieve` and `/docs`** — passing IndexOnly text to a model as context is analysis, not redistribution; loopback-internal, not public.
5. **`/view`'s `kind` is `format!("{:?}", SignalKind)`**, so the shell can post signals straight back to `/signals/record`.
6. All v0.1–v0.3 invariants unchanged: dedup (hamming ≤16) BEFORE all statistics; mentions per (entity, doc); Corroborated suppressed when Rising; discovery on bodies only; FNV-1a determinism; RRF k=60.
7. **(v0.6) Source selection is core business, not shell business.** `/ingest` takes `{sectors, sources?}`. `sources` names connector ids; **each is still validated against `sectors`**, so a named source outside the caller's entitlement is refused, not run — the sector filter is not a suggestion that a source id can bypass (HC2). Selection lives in `registry::select_sources`, which returns `unknown_ids` as **structured per-id errors rather than panicking**. Omitting `sources` entirely preserves the exact pre-v0.6 behavior (every source in the sectors, in config order) — a regression test pins this (HC5).
8. **(v0.6, hardened v0.8/T2) Harvest cursors live in the core store, not the shell.** The `cursors(source_id, cursor, high_water, pending_high_water, updated_at)` row is committed in the **same SQLite transaction** as each parsed page's documents and canonical-id rematerialization. `cursor` is the next OAI-PMH `resumptionToken`; `pending_high_water` retains the max datestamp seen across capped/restarted pages; only a final-page commit clears both and advances completed `high_water`. This prevents either half of the old split-write failure: advancing past documents still in memory, or losing an earlier page's maximum datestamp after restart. High-water advance remains monotonic (ISO dates ⇒ lexicographic max is chronological max). Cursors are the documented exception to atomic-JSON persistence (HC9): they belong in SQLite beside the documents they track. Connectors that don't page (RSS) ignore the seam entirely.

9. **(v0.6/T6) Provider vocabulary is normalized INTO the neutral one, never the other way round.** `billing.apply_event` speaks `subscription.created|updated|deleted|key_rotated` and nothing else. Stripe enters through `adapters/stripe.py`, which verifies Stripe's signature scheme and maps `customer.subscription.*` onto those events. Consequences worth keeping: a second provider is a second adapter, not a change to the store or the entitlement model; and the freshness check on Stripe's signed timestamp is load-bearing, because a *genuine* captured request replayed later carries a perfectly valid MAC — the timestamp is the only thing that refuses it. Keys are compared against a *set* of active hashes, so rotation has a grace window and revocation is just rotation with none.
10. **(v0.6/T9) Dedup identity is a function of the corpus, not of arrival order.** `dedup_near` keeps the earliest document by `(published_day, id)` — a global property. So `canonical_id` is persisted as a **re-materialization of that same rule on every ingest that adds rows**, NOT as a first-seen-wins assignment at insert. This matters more since T3: sources now run on independent clocks, so arrival order genuinely varies, and an incremental assignment would let two runs over the same 13 documents disagree about which copy is canonical. Relatedly, `/retrieve` deliberately does **not** filter by `canonical_id`: it keeps whichever of a near-dup pair *the query* ranked higher. Canonical id is a property of the corpus; relevance is a property of the question, and context assembly is a question about the question. T3 now materializes `simhash(title + body)` at ingest/migration, refreshes it on document update, and makes `/view` and canonical assignment consume the persisted value; a missing value is an error, not a silent hot-path recompute.

**2.11 — robots.txt is DISCOVERED, and the two gates compose one way only (T2, v0.7).**
There are now two robots checks, and the order and direction matter:

- The **publisher's** policy, fetched from their real `/robots.txt` (`RobotsCache`, in `crates/compliance`). Per-origin, TTL 24h, bounded to 512 origins, and the fetch itself goes through the same per-host politeness limiter — it would be a strange kind of respect to skip the rate limit for the one file that describes how to be respectful.
- The **operator's** configured deny-list (`RobotsGate::new(&["/private","/admin"])`), which applies *on top* and can only ever refuse **more**. A publisher blessing `/private` does not oblige us to crawl it.

Three decisions inside this that are easy to get wrong and are therefore pinned:

- **Fail-closed, and the 4xx/5xx distinction is not cosmetic.** RFC 9309 gives three outcomes, not two. **2xx** ⇒ the body governs (an *empty* body is a valid allow-all, and is **not** the same thing as a 404). **5xx / DNS / TLS / timeout** ⇒ "Unreachable" (§2.3.1.4): we do not know the policy, so we take nothing. **4xx** ⇒ "Unavailable" (§2.3.1.3): the RFC permits full access, and here we **knowingly diverge** — `MissingPolicy::Deny` is the default, because we fetch a small operator-configured set of publishers rather than discovering the open web, and the cost of wrongly fetching from someone who never published a policy is a compliance incident while the cost of wrongly *not* fetching is a log line. `MissingPolicy::RfcAllowAll` is available and named, so the divergence is a choice rather than a buried `else`.
- **A fixture read is not a request.** `gate()` takes a `Reach` (`Network` | `Fixture`). A fixture-backed source never fetches `robots.txt` — an "offline, deterministic" run that quietly phones example.org for permission to read a file already on disk would be both a surprise and a lie about what offline means. Tested directly: `a_fixture_fetch_never_asks_the_publisher_for_permission` asserts **zero** fetches even on a `net` build with a cache wired in.
- **A published `Crawl-delay` can only slow us down.** `apply_crawl_delay` adopts a publisher's stated cadence only if it is *slower* than our own floor (2 rps). A `robots.txt` must not be able to talk us into hammering a server faster than we would have gone anyway.

**Consequence, and it is the reason this could not just be dropped into the handler:** politeness state is now **process-scoped**, not request-scoped. `HostLimiters` and `RobotsCache` moved into `AppState`. They used to be rebuilt inside `/ingest`, which meant two ingests a second apart each started with a clean limiter and neither waited for the other — and a per-request robots cache would have re-fetched every publisher's `robots.txt` on *every ingest*, i.e. a "compliance" feature that made us a **worse** citizen than before. A TTL only means something if the cache outlives the request.

**2.12 — the 404 disposition is PER-SOURCE, and the operator's config is the opt-in (v0.7.1).**
v0.7 made the 404 decision cache-wide (`MissingPolicy::Deny`, with an `RfcAllowAll` override on the whole cache). The first live harvest proved that granularity wrong: arXiv's OAI-PMH host serves no robots.txt, and one blanket policy forces a false choice — fail closed and block a cooperative source, or open the 404 door for *every* source at once. Neither is right.

So the disposition now lives on the **source**, threaded `SourceCfg.robots_on_missing → {RssSource, ArxivOaiSource} → gate(…, on_missing) → RobotsCache::allowed(…, on_missing)`. Three properties are load-bearing and pinned:

- **Default is `Deny`, and a typo fails closed.** `MissingPolicy::from_config_str` maps `"allow"` (and synonyms) to `RfcAllowAll` and *everything else, including absent and misspelled,* to `Deny`. A source you forget to annotate, or annotate wrong, is conservative — never accidentally permissive. Every source except `arxiv-cs` is `Deny` today.
- **Opting in reinterprets ABSENCE ONLY.** `robots_on_missing: "allow"` changes the 404 case and nothing else. An explicit `Disallow` from a real robots.txt is still obeyed (tested: `opting_in_does_not_bypass_an_explicit_arxiv_disallow`), and an `Unreachable` origin (5xx/timeout) still fails closed. "Allow if absent" must never quietly become "ignore robots.txt."
- **The justification is the architecture's own principle, applied.** Entitlement decisions live with the operator, not in the fetch layer; the publisher's robots.txt is a *technical* access policy layered on top. An operator configuring `arxiv-cs` against a standards-compliant, harvest-designed endpoint *is* the opt-in. Encoding that as one auditable per-source line is the correct shape — as opposed to a global flip, which is what the on-site tester reached for (and which, being applied to a `#[default]`-attribute default via `sed` on the literal string, changed a doc comment and nothing else).



**Toolchain matrix (v0.7 — every cell RUN, none inferred). The 1.75 and 1.76 rows are new, and they are why §5's floor claim changed:**

| toolchain | `check`/`test --workspace --locked` | `-p cored --features net` |
|---|---|---|
| 1.75.0 (stock Ubuntu 24.04 `rustc`) | ❌ `lock file version 4 requires -Znext-lockfile-bump` | ❌ `failed to download replaced source registry` (the edition2024 masquerade) |
| 1.76.0 | ❌ same lockfile parse failure | ❌ |
| **1.78.0 — the floor** | **0 warnings, 75 green** | ❌ |
| **1.91.1 (pinned)** | **0 warnings, 75 green** | ✅ **clean, `--locked`, `-D warnings`** |

- **The v0.6.2 lockfile bug, measured.** Against the committed **v4** lock, cargo **1.75 and 1.76 cannot even parse it** — v4 needs cargo ≥ 1.78. v0.6.2's "verified green on 1.75" was therefore impossible; it had never been run.
- **And the fix that looked obvious is a trap, which is worth more than the fix.** Re-encoding the lock to **v3** genuinely restores 1.75 (verified: **75 green**, and the package set diffed **byte-identical** — same names, versions, checksums, so it is a format change and not a resolution change). But **cargo 1.91 rewrites the lock back to v4 as soon as it modifies it** — confirmed here by bumping `cored`'s version and watching a plain `cargo check` silently re-emit v4. v3 is a hand-edit with a half-life. **We therefore ship the sustainable floor (1.78) rather than the flattering one (1.75)**, and CI enforces it.
- `cargo check --workspace --locked --all-targets` with `RUSTFLAGS=-D warnings`: **0 warnings**. Same for `-p cored --features net --locked --all-targets`.
- `cargo test`: **75 green** — compliance **26** (was 7), ingest **14** (was 7), core 7, cored 7, registry 4, retrieve 3, extract 3, enrich 2, store 9. `cargo test -p intel-ingest --features net --locked`: 14 green.
- `pytest shell/tests`: **69 green**, unchanged — T2 is entirely below the seam, and the shell suite still needs no Rust toolchain.
- **T4's own testing objective, executed:** a deliberate warning (`let x = 1;` unused) introduced into `crates/extract` makes `RUSTFLAGS="-D warnings" cargo check --locked` exit **101**. The gate bites. Restored; clean.
- **Golden E2E re-verified live from a clean DB after T2 — every number identical:** acme ingests **13** (Finance skipped), dedup drops `techwire::tw-004` keeping `osdaily::osd-004` (hamming **12**) ⇒ **12 analyzed**; **DeepSeek RISING z=10.0** corroborated by 3 sources (arxiv-cs, osdaily, techwire); vLLM RISING z≈**2.67**; NVIDIA + Qwen **CORROBORATED**; **"Helios Labs" EMERGING**; immediate re-run **+0 new**; quant-desk sees only its **1** doc.
- **Public API spot-checks live:** bad key ⇒ **401**; entitlement-disjoint search (**acme 6 hits vs quant 0** for "deepseek"); all 4 IndexOnly hits return `snippet: null`; the brief renders "excerpt withheld" (10 occurrences).
- **T2 live-path proof, offline:** the `RobotsFetcher` seam is driven by a fake through every branch — 200-with-body, 200-empty, 404, 500, unreachable, malformed HTML-served-as-200 — so fail-closed is *tested*, not asserted. TTL expiry is tested deterministically with `tokio::time::pause()`, not by sleeping.

## 4. Next steps

**Done in v0.7:** ~~T2 (real robots.txt)~~ · ~~T4 (CI + MSRV enforcement)~~ · **T5 built, measured, and rejected** (§6c).
**Deferred in v0.7, each with the gate that deferred it:**

1. **T1 — the first live arXiv harvest. DEFERRED: no egress. Verified, not assumed.** `curl -sI https://export.arxiv.org/oai2?verb=Identify` ⇒ **HTTP 403, `x-deny-reason: host_not_allowed`** — the sandbox proxy refuses the host, exactly as in v0.6. The task's own gate is explicit ("no egress ⇒ defer and say so; **do not mock a live harvest and mark it done** — the entire value of this task is that it is not a mock"), so nothing was faked. **This is now the single highest-value item in the project, and it is not a code problem:** `--features net` builds, paging + cursors are implemented and unit-tested, the limiter and `Retry-After` handling exist, and **as of T2 the robots gate will do a real fetch before the first request**. On any box that can reach arXiv: `cargo build -p cored --features net --locked`, drop the `"fixture"` key from `arxiv-cs` in `config/core.json`, `POST /ingest {"sectors":["science"],"sources":["arxiv-cs"]}`. **HC13 stands: fixtures prove the state machine, not the wire.** The things that genuinely cannot be tested here are a real `503 Retry-After` under load, observed ≥3s page spacing on the wire, real-world XML edge cases, and cursor durability across a real interrupt.
2. **T4 (v0.7/T3) — point the LLM at a real endpoint. DEFERRED at the credential/configuration gate, and deliberately NOT mocked-and-declared-done.** Re-probed 2026-07-20: DeepSeek and OpenAI now both return unauthenticated **401**, so egress is available; however `LLM_BASE_URL` and `LLM_API_KEY` are absent and no local vLLM listener exists on 8000/8899/11434. `./run verify-llm` exits 2 before model work. A configured endpoint and credential from the operator are still required; then `tools/verify_llm.py` runs the checklist.
3. **T6 — seam hardening for multi-host. DEFERRED: condition still not met.** Core and shell still run on one host (`cored` binds `127.0.0.1:8788`; `deploy/intel-pipeline.service` sets `CORE_URL=http://127.0.0.1:8788`). `CORE_TOKEN` is implemented on both sides. Per the task's own instruction, no speculative UDS and no mTLS were written. **Trigger:** the first genuine cross-host split.
4. **T7 — scale swaps. DEFERRED (design-level), and T5 *removed* LSH from this bucket rather than promoting it.** Postgres remains a **concurrency** trigger (a second writer), not a size one, and may never fire.
5. **T8 — known-limitation pick-ups. All three SKIPPED on their own stated preconditions, which were checked rather than assumed.** (a) Materialize `/view`: the precondition is "if warm-up cost shows up" — the corpus is 12 documents; it has not. (b) One SQLite connection behind a `Mutex`: the trigger is a second writer; there is none. (c) A rebuild tool for pre-v0.6 `Day` encodings: the task says *"check before building it"* — **checked, and no such archive exists.** `/data` is gitignored and archives are never shipped; every DB reachable on this box was created fresh this session from fixtures, on the new encoding. Building the tool would have been building for a hypothetical.

**The recommended top of the v0.8 queue, in order:**

1. **The live arXiv harvest** (T1 above), the moment a box with egress exists. Everything is ready; nothing else can falsify the paging.
2. ~~**Persist the SimHash fingerprint.**~~ **COMPLETED in v0.8/T3.** The column and ingest write already existed when the step began, but `/view` still recomputed every fingerprint and no pre-column migration existed. Dedup now accepts persisted fingerprints, document updates refresh them, and the backfill was verified over a disposable pre-column copy of all 1,764 live rows with zero fingerprint or canonical-id mismatches. The golden result did not move.
3. ~~**Turn on `clippy` + `rustfmt` in CI.**~~ **COMPLETED in v0.8/T6.** The job was not commented out; it was report-only, and B0 measured one clippy diagnostic plus 13 files of fmt drift. T6 fixed those findings in `097b017`, verified both commands clean, then promoted the job to blocking in the separate gate commit.

## 5. Known limitations (documented, not hidden)

- ~~**Robots policy is configured, not discovered.**~~ **RESOLVED in v0.7 (T2)** — see §2.11 and §6b.
- ~~**"Rust 1.75 + `--locked` still builds the offline path."**~~ **FALSE, and it is the most important correction in this document.** The committed `Cargo.lock` is format **v4**, unparseable by cargo before **1.78**, so the claim could never have held — it had simply never been run. **The offline floor is now declared as 1.78**, measured across 1.75/1.76/1.78/1.91 and enforced by CI's `msrv` job. Re-encoding the lock to v3 *does* buy back 1.75 (75 tests green, resolution byte-identical) but cargo ≥ 1.78 rewrites it to v4 on the next lock modification, so that floor cannot be held. **The general lesson: a claimed property that nothing executes is not a property, it is a wish** — the same failure that let `--features net` sit broken for two cycles and that let "robots-compliant" mean "compliant with a policy we wrote ourselves."
- **The `--features net` floor is 1.86, and the error lies about why.** `icu_* 2.2.0` (via `idna_adapter`) declare `rust-version = 1.86`; edition2024 stabilizing in 1.85 is necessary but **not** sufficient. Worse, the failure surfaces at *dependency-download* time as `error: failed to download replaced source registry 'crates-io'`, which sends you looking at the registry instead of at MSRVs. Reproduced again this cycle on 1.75.
- **Correction to a v0.5 note** (unchanged from v0.6): `/v1/ask`'s `context_suppressed` names `techwire::tw-004`, not `osdaily::osd-004`, for the question actually tested. Suppression at context assembly is **rank-aware by design**, so which copy of a syndicated story is dropped depends on which one the query ranked higher. Treat *"one of the pair is suppressed"* as the golden, not a specific id.
- **`Day` values changed scale (T9.3).** `published_day` is days-since-1970. Pre-v0.6 archives spanning a month boundary would need a rebuild — **checked in v0.7: no such archive exists**, so no tool was built (T8.3).
- ~~**`dedup_near` recomputes every fingerprint on every pass.**~~ **RESOLVED in v0.8/T3.** The store materializes the fingerprint and `/view` passes it into `dedup_near`; a deliberately violating test double proves the function consumes the supplied value rather than recomputing it.
- `/view` is memoized per (sector-set, generation) rather than materialized; a restart re-warms it. Cost is unmeasurable at 12 docs.
- One SQLite connection behind a `Mutex` (fine: the shell is the single caller); `cored` binds loopback by design.
- ~~**HC1 was not enforced on `/v1/ask`, and its test was vacuous.**~~
  **RESOLVED in v0.8/T1.** The model still receives capped IndexOnly bodies as
  internal analysis context, but its answer now goes to core `POST /attest`
  with the exact context document ids before any public response. The core
  checks normalized 16-token overlap only against `IndexOnly` bodies and
  replaces the entire answer with a constant refusal on any violation; `CcBy`
  quotation remains allowed. `tools/mock_openai.py --leak` deliberately emits
  a source sentence. Both the shell test and a real Rust↔HTTP↔Python E2E proved
  that sentence cannot pass, while the ordinary golden answer is unchanged.
- ~~**The robots gate was checked only on the configured origin while reqwest followed redirects automatically.**~~ **RESOLVED in v0.8/T5.** Both HTTP clients now set `Policy::none()`. Document redirects are resolved manually with the full gate before each next request; robots-file redirects fail closed. A failure-capable cross-origin 302 test makes the second body available, configures that origin to disallow it, proves both robots policies were fetched, and proves the second document request never happened. A same-origin redirect makes two document requests with exactly one robots fetch.
- **The robots cache does not de-duplicate concurrent misses.** Two simultaneous first-requests to the same origin can both fetch `/robots.txt`. Bounded, harmless (the limiter still spaces them). **T7 rechecked the trigger on 2026-07-20 and deferred the lock:** the supported scheduler remains one synchronous writer and the deployment unit is one-shot; revisit only when a second concurrent harvester actually exists.

## 6. Decision log

### 6a. Why `feed-rs` was NOT adopted (v0.6/T2)

The task set a three-clause gate; the swap tripped **all three** in v0.6.1, and the gate was **re-run** in v0.6.2 because clause 1 was a statement about a toolchain we had just changed. A decision log that keeps a dead reason is worse than no decision log.

1. ~~**It doesn't build on our toolchain.**~~ **STRUCK — no longer true.** `feed-rs 2.x` builds clean on 1.91.
2. **Footprint. STILL TRIPS.** 56 unique transitive crates, against 16 for the entirety of `intel-ingest`. It drags `chrono`, `quick-xml`, `regex`, `url`, `aho-corasick`, `mediatype`, `serde_json` to parse two small formats `roxmltree` already parses.
3. **Parse-equivalence breaks. STILL TRIPS.** `feed_rs::model` types timestamps as `Option<DateTime<Utc>>` (chrono, not our ordinal `Day`) and differs on id fallback. Adopting it would **silently move document ids** — the one thing a swap in this crate must never do.

**Decision unchanged: skipped**, now resting on cost and correctness rather than on a compiler we no longer run.

### 6b. Why `texting_robots` was NOT adopted (v0.7/T2)

The same three-clause shape, run against the crate the task named as "the noted drop-in."

1. **Builds on 1.91? PASSES.** It compiles cleanly.
2. **Transitive footprint? FAILS, and disqualifyingly.** It resolves **45 transitive crates** into `intel-compliance`, which today has **one** dependency (`tokio`) — 7 crates in its whole tree. Worse than the count: it pulls `url` → `idna` → `idna_adapter` → **`icu_collections` / `icu_normalizer` / `icu_properties` / `icu_provider` 2.2.0, all declaring `rust-version = 1.86`.** Those are *the exact crates* that walled this project for two cycles (§5). And `intel-compliance` is a **non-optional dependency of `intel-ingest`, which is in the default build graph** — so adopting it would have dragged the icu chain into the **offline** build and silently raised the offline MSRV from 1.75 to 1.86, destroying the very property v0.6.2 fought for and `rust-toolchain.toml` still promises. *We would have re-created the disaster we had just finished cleaning up, in the name of compliance.*
3. **Does it change any existing allow/deny outcome? NO — and this is the clause that paid for the whole evaluation.** Rather than take the dependency, `texting_robots` was used **out of tree, once, as a differential oracle** against the hand-rolled parser: **16 `robots.txt` bodies × 22 paths + crawl-delay = 368 verdicts, 0 divergences.** Wildcards, `$` anchors, `Allow` exceptions, equal-specificity ties, longest-UA-token-wins, a `User-agent` line after a rule starting a *new* group, empty `Disallow:` meaning allow-all, comments-only files, rules before any UA line, and an HTML error page served as a 200 — all agree.

**Decision: skipped.** We shipped a **zero-new-dependency** parser (`async-trait` was already in the graph; the `Cargo.lock` diff is **one line and zero new crates**, versus 45) that is *proven* equivalent to the battle-tested one. The correctness assurance was the valuable part of the crate; the dependency was the expensive part. We took the first and left the second.

### 6c. Why LSH banding was BUILT, MEASURED, and REJECTED (v0.7/T5)

`docs/T8-scale-design-note.md` called LSH "the swap most likely to be needed first." That was a **hypothesis about where the time goes**, and T5's gate demanded exact recall at hamming ≤ 16. So it was built and measured (`cargo run --release -p intel-extract --example dedup_bench`, committed). **Both halves of the hypothesis are false.**

| n | simhash (linear) | pairwise scan (quadratic) | scan share | banded LSH | pairs still compared | recall |
|---|---|---|---|---|---|---|
| 1,000 | 69.6 ms | 1.3 ms | 1.8% | 90.2 ms | 76.2% | 100% |
| 5,000 | 359.7 ms | 31.7 ms | 8.1% | 5,801 ms | 76.1% | 100% |
| **10,000** | **734.3 ms** | **125.9 ms** | **14.6%** | **30,962 ms** | **76.1%** | **100%** |
| 20,000 | 1,473.9 ms | 509.8 ms | 25.7% | **OOM (~4.5 GB)** | — | — |

1. **The quadratic scan is not the bottleneck.** At n = 10k it is **14.6%** of dedup time. The other **85%** is *fingerprinting* — `dedup_near` recomputes `simhash()` for every document on every call. A hamming comparison is one XOR and a popcount (~1 ns); fingerprinting a 2 KB body costs ~70 µs. The quadratic term does not overtake the linear one until roughly **n > 100k**. We were about to optimize the cheap half.
2. **Banding cannot prune at this threshold anyway — and this is arithmetic, not implementation.** `dedup_max_distance` is **16** on a **64-bit** fingerprint. Exact recall requires, by pigeonhole, *more bands than the distance* (b ≥ 17), so bands are 64/17 ≈ **3.8 bits** wide. A 4-bit band has 16 possible values, so an average bucket holds n/16 of the corpus and nearly everything collides with nearly everything. Measured: it still compares **76% of all pairs** and runs **246× slower** than the scan it replaces. Recall *is* exactly 100%, as the math promises — **the index is correct and useless.** At n = 20k the candidate set alone tries to allocate ~4.5 GB and aborts.

**The rule worth keeping:** *an LSH band's selectivity depends on the threshold as a **fraction** of fingerprint width, not its absolute value.* 16/64 = 25% divergence is far outside the regime where any exact Hamming index beats a linear scan. Widening the fingerprint does not help if the threshold widens with it; it helps only if the *absolute* distance stays at 16 (e.g. 16/128), and that is **a different similarity rule** — it changes which documents are duplicates, which is corpus corruption, not an optimization. T5's gate says stop, and it was right to.

**Decision: not merged.** The design note has been corrected in place, and the swap it should have named — **persist the fingerprint** — is now the recommendation in §4.

## 7. Run reference

```bash
# toolchain (v0.6.2): offline needs >= 1.75; --features net needs >= 1.86.
# Ubuntu 24.04 ships both, no rustup required:
apt-get install -y rustc-1.91 cargo-1.91
export PATH=/usr/lib/rust-1.91/bin:$PATH
cargo build -p cored --features net --locked            # live HTTP; builds since v0.6.2

cargo run -p cored                                     # core on :8788
pip install -r shell/requirements.txt
PYTHONPATH=shell python3 -m intel_shell.pipeline --client acme-research
PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787   # public API on :8787

# with the mock LLM (embeddings + /v1/ask):
python3 tools/mock_openai.py &
LLM_BASE_URL=http://127.0.0.1:8899/v1 PYTHONPATH=shell python3 -m intel_shell.pipeline

cargo test && PYTHONPATH=shell python3 -m pytest shell/tests   # 49 Rust + 69 shell

# v0.6 — per-source ingest (the `sources` filter is optional; omit it for whole sectors):
curl -X POST localhost:8788/ingest -H 'content-type: application/json' \
     -d '{"sectors":["technology"],"sources":["techwire"]}'
PYTHONPATH=shell python3 -m intel_shell.scheduler --dry-run   # per-source + per-sector jobs
PYTHONPATH=shell python3 -m intel_shell.scheduler --once      # run due jobs (cron/systemd)

# v0.5 — hashed keys + billing webhook:
PYTHONPATH=shell python3 tools/hash_subscriptions.py config/subscriptions.json \
  --out config/subscriptions.hashed.json
SUBSCRIPTIONS_PATH=config/subscriptions.hashed.json BILLING_WEBHOOK_SECRET=whsec_… \
  PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787

# v0.6 (T6) — key rotation, Stripe, SQLite-backed subscriptions:
PYTHONPATH=shell python3 tools/admin_keys.py list
PYTHONPATH=shell python3 tools/admin_keys.py rotate \
  --client acme-research --new-key ak_NEW --grace 86400   # omit --grace = revoke now
PYTHONPATH=shell python3 tools/migrate_subscriptions.py config/subscriptions.json \
  --to sqlite:///var/lib/intel/subs.db
SUBSCRIPTIONS_PATH=sqlite:///var/lib/intel/subs.db STRIPE_WEBHOOK_SECRET=whsec_… \
  PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787   # POST /v1/billing/stripe

# T7, when a real LLM endpoint exists (this is the whole deferred checklist):
LLM_BASE_URL=http://vllm-box:8000/v1 LLM_API_KEY=… \
  PYTHONPATH=shell python3 tools/verify_llm.py
```

**Env — core:** `CORE_CONFIG` `CORE_ENTITIES` `CORE_DB` `CORE_BIND` `CORE_TOKEN`.
**Env — shell:** `CORE_URL` `CORE_TOKEN` `SUBSCRIPTIONS_PATH` (a path, or `sqlite:///…`) `LLM_BASE_URL` `LLM_API_KEY` `LLM_CHAT_MODEL`/`LLM_EMBED_MODEL`, `API_KEY_PEPPER`, `BILLING_WEBHOOK_SECRET`; **new in T6:** `STRIPE_WEBHOOK_SECRET` (unset ⇒ `/v1/billing/stripe` returns 503), `STRIPE_PRICE_SECTORS` (JSON price→sectors map, so entitlements follow what was purchased).

**Note (T9.6):** the default subscriptions path is now anchored to the repo root rather than the process CWD — `uvicorn intel_shell.app:app` launched from anywhere but the repo root used to silently find zero clients and 401 every request.

**Scheduler config (`config/schedule.json`) — v0.6 shape:** a job's `sources` map is now **source id → cadence** (true per-feed clocks: `techwire` every 900s and `osdaily` every 1800s, though both live in `technology`), and the new `sectors` map is **sector id → cadence** for whole-sector jobs. A job with neither runs a single full pipeline.

## 8. v0.8 measured execution

### B0 — entering baseline (verified 2026-07-20)

Every result below was run on the pinned Rust/Cargo 1.91.1 toolchain after
`cargo clean` removed 758.4 MiB of build output; none is inferred from the prior
handoff.

- `RUSTFLAGS="-D warnings" cargo check --workspace --locked --all-targets`:
  exit 0, 0 rustc warnings.
- `RUSTFLAGS="-D warnings" cargo test --workspace --locked`: exit 0, **80
  passed** (cored 7, compliance 28, core 7, enrich 2, extract 3, ingest 17,
  registry 4, retrieve 3, store 9; analyze/view and doc-tests 0).
- `RUSTFLAGS="-D warnings" cargo check -p cored --features net --locked
  --all-targets`: exit 0, 0 rustc warnings.
- `RUSTFLAGS="-D warnings" cargo test -p intel-ingest --features net --locked`:
  exit 0, **17 passed**.
- `PYTHONPATH=shell .venv/bin/python -m pytest shell/tests -q`: exit 0, **69
  passed**, with 1 `StarletteDeprecationWarning` from FastAPI's `TestClient`.
- Clippy/fmt inventory: clippy exits 101 on the one
  `items_after_test_module` diagnostic described above; allowing only that lint
  makes the remaining workspace clippy run clean. The two intentional
  `unnecessary_map_or` allows remain. `cargo fmt --all -- --check` exits 1 with
  diffs in 13 Rust files. CI is report-only, not commented out; the stale
  "commented out" descriptions elsewhere in this file and `TASKS-v0.8.md` are
  recorded as false here and remain for the ordered T6 documentation fix. T6
  owns the lint/fmt corrections and gate promotion.
- Golden E2E, run through the real Rust↔HTTP↔Python seam with the deterministic
  mock model and a fresh temporary fixture DB: initial ingest **13 new**; acme
  **13 → 12 analyzed**; `techwire::tw-004` dropped for `osdaily::osd-004` at
  hamming **12**; DeepSeek **RISING z = 10.0**, corroborated by arxiv-cs,
  osdaily, and techwire; immediate re-ingest **+0**; quant-desk **1 document**;
  `/v1/ask?q=What is DeepSeek-V4?` returned **4 citations** and suppressed
  `techwire::tw-004`. No golden delta.
- DB isolation is explicit. `./run demo` creates `$DEMO_DIR/demo.db` under
  `mktemp -d`; B0 additionally used
  `/private/tmp/intel-platform-b0-golden-20260720.db` (14 fixture documents
  after both clients). The live archive remains `data/core.db`: read-only checks
  before and after the golden run showed **1,764 documents**, 6,729,728 bytes,
  and mtime `2026-07-20 09:22:16 +0800`. All future live smoke runs use
  `CORE_DB=data/live-smoke.db` and must not write the golden fixture DB or the
  1,764-document archive.
- Environment note: at B0, port 8788 was held by a `cored` process B0 did not
  start, PID **59269**, executable from this checkout. The operator stopped it;
  T2's preflight then confirmed `./run down` followed by
  `lsof -iTCP:8788 -sTCP:LISTEN -n -P` was clear.

### T2 — live interruption-resume gate tripped (2026-07-20)

- Preflight: port 8788 clear; `data/live-smoke.db` absent; `data/core.db` at
  **1,764 documents**, 6,729,728 bytes, mtime `2026-07-20 09:22:16 +0800`,
  SHA-256 `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
- Run 1 command: `HARVEST_MAX_PAGES=1 CORE_DB=data/live-smoke.db ./run
  harvest-arxiv`, with the generated window `2026-07-17` through `2026-07-20`.
  The live response was `fetched=1300, new=1300, ok=true, error=null`; the log
  reported page 1 with 1,300 documents, more pages following, then cap 1.
  Real OAI-PMH XML therefore parsed without an observed error on that page.
- Gate measurement immediately after run 1:
  `source_id='arxiv-cs', cursor=NULL, high_water='2026-07-20'`. This fails the
  first acceptance criterion. A capped run was treated as completion.
- Root cause: the page loop calls `checkpoint(next)`, breaks on `max_pages`,
  then the common post-loop path calls `complete(max_datestamp)`. The test
  `max_pages_bounds_one_run_and_checkpoints_the_rest` proves only that the fake
  observed the intermediate checkpoint call; it does not assert the final
  `resume_token`, so the subsequent clear cannot make the test fail.
- Run 2: **not run by design**. With the token already cleared and high-water
  advanced, it would be an incremental request, not resume-from-interruption.
  Treating it as resume evidence would violate the task's explicit gate.
- `503 Retry-After`: not observed; no 503/retry line appeared in run 1.
- Isolation and regression: `data/live-smoke.db` contains the 1,300 live rows;
  `data/core.db` retained the exact pre-run count, size, mtime, and SHA-256.
  The full fixture golden E2E was re-run and unchanged: acme **13 → 12**,
  `techwire::tw-004` dropped for `osdaily::osd-004` at hamming **12**, DeepSeek
  **RISING z=10.0**, re-ingest **+0**, quant-desk **1 document**, and `/v1/ask`
  **4 citations** with `techwire::tw-004` suppressed.

### T2 corrective attempt — durable locally, live reproof blocked (2026-07-22)

- The old cap guard was made failure-capable before the repair. The unchanged
  production code then failed the strengthened assertion: checkpoint history
  contained `oai_page2.xml`, but final `resume_token("arxiv-cs")` was `None`
  because the common completion path cleared it.
- The persistence seam now exposes one fallible page commit. `SqliteStore`
  atomically inserts the page documents, rematerializes canonical ids, records
  the next token, and accumulates `pending_high_water`. A final page promotes
  `max(existing high_water, pending pages, final page)` and clears the in-flight
  fields. Cursor-write failures are no longer swallowed by `cored`.
- Failure controls executed: the in-memory cursor double injected a page-commit
  error and proved no token advance; a SQLite `BEFORE INSERT` trigger aborted
  the cursor upsert after the document insert and proved the transaction left
  **0 documents and 0 cursor rows**; a close/reopen test preserved the page-2
  token and a page-1 datestamp newer than page 2, then completed at the correct
  earlier maximum. An old cursor table was reopened and gained the new pending
  column.
- Local acceptance: warning-denied workspace and net checks passed; **90
  workspace tests**, **20 net ingest tests**, and **70 shell tests** passed (the
  existing one Starlette deprecation warning remains); clippy and fmt passed.
  The locked offline workspace also checked clean under Rust **1.78.0** with
  `-D warnings`, so the MSRV floor did not move.
- Live preflight: `./run down` succeeded and port 8788 was clear. The previous
  disposable smoke DB was preserved at
  `/private/tmp/intel-platform-live-smoke-before-t2r-20260722.db`; a fresh
  `data/live-smoke.db` was used. The sandboxed probe returned HTTP `000000` and
  was not counted. With network permission, arXiv's Identify endpoint returned
  200 and the real robots decision was `Unavailable(allow)` with effective
  crawl delay 0.500s, but the first `ListRecords` request for 2026-07-19 through
  2026-07-22 timed out. Result: `fetched=0`, `new=0`, `ok=false`, no parsed XML
  page, no cursor row, and every HC13 box unchecked. Run 2 was not executed;
  503/Retry-After was not observed. **T2 remains blocked, not passed.**
- Full golden E2E used fresh temporary DB
  `/private/tmp/intel-t2r-golden.gB0kZ9/golden.db` and remained exact: initial
  ingest **13**, acme re-ingest **+0**, analyzed **12**,
  `techwire::tw-004` dropped for `osdaily::osd-004` at hamming **12**, DeepSeek
  **RISING z=10.0**, quant-desk **1 document**, and ordinary `/v1/ask` with **4
  citations** and `techwire::tw-004` suppressed. The DB ended at 14 rows with 0
  NULL fingerprints/canonical ids. `data/core.db` retained **1,764 rows** and
  SHA-256 `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
- Verification environment note: the first sandboxed golden could not bind
  loopback; the permitted run then exposed macOS system-proxy discovery routing
  Python `httpx` loopback through `httpcore._sync.http_proxy` despite no proxy
  environment variables. Direct curl proved cored stayed healthy. The recorded
  golden set `NO_PROXY/no_proxy=127.0.0.1,localhost`; no application behavior
  was changed. Ports 8788 and 8899 were clear after teardown.

### T2 closed — interruption-resume proven on the live wire (2026-07-23)

- Preflight: the worktree was clean at `2b036d9`; `./run down` succeeded and
  port 8788 was clear. The 2026-07-22 zero-row timeout artifact was preserved at
  `/private/tmp/intel-platform-live-smoke-t2-timeout-20260722.db`, and both live
  runs used a fresh `data/live-smoke.db`. The sandboxed reachability probe again
  returned HTTP `000000` and was not counted; the permitted commands reached
  arXiv Identify with HTTP 200.
- Run 1 command: `HARVEST_MAX_PAGES=1 CORE_DB=data/live-smoke.db ./run
  harvest-arxiv`, generated window `2026-07-19` through `2026-07-22`. It fetched
  and added **1,300** real records, reported `ok=true`, parsed the page without
  an observed error, reported that more pages followed, and stopped at cap 1.
  SQLite then held 1,300 documents and the non-NULL next token
  `verb%3DListRecords%26metadataPrefix%3Doai_dc%26from%3D2026-07-21%26until%3D2026-07-22%26set%3Dcs%26skip%3D522`,
  with `high_water=NULL` and `pending_high_water=2026-07-21`.
- Run 1's logs/config were preserved under
  `/private/tmp/intel-platform-t2-run1-20260723-*`. `cored` was stopped, port
  8788 was independently confirmed clear, and the identical capped command was
  run again. **Run 2's first request carried the exact run-1 token**, so it
  resumed rather than fetching the fresh first page. It fetched and added the
  next **1,300** real records with `ok=true`; the store reached **2,600** rows
  and 2,487 analyzed documents. The next durable token advanced to
  `verb%3DListRecords%26metadataPrefix%3Doai_dc%26from%3D2026-07-22%26until%3D2026-07-22%26set%3Dcs%26skip%3D88`,
  with `high_water=NULL` and `pending_high_water=2026-07-22`. Run 2 evidence is
  preserved under `/private/tmp/intel-platform-t2-run2-20260723-*`.
- Both runs emitted the real robots verdict `Unavailable(allow)` and an
  effective crawl delay of 0.500s. Across the two live pages the harness
  reported no XML parse error. A 503/Retry-After response was **not observed**;
  it was not forced. The smoke DB has 0 NULL fingerprints and 0 NULL canonical
  ids.
- Full acceptance on the resulting tree: warning-denied offline and net checks
  passed; **90 workspace tests**, **20 net ingest tests**, and **70 shell tests**
  passed (the existing one Starlette deprecation warning remains); clippy and
  fmt passed. The locked offline workspace checked clean under Rust **1.78.0**
  with `-D warnings`.
- Full golden E2E used fresh temporary DB
  `/private/tmp/intel-platform-t2-golden.gyEOy7/golden.db` and remained exact:
  initial ingest **13**, acme re-ingest **+0**, analyzed **12**,
  `techwire::tw-004` dropped for `osdaily::osd-004` at hamming **12**, DeepSeek
  **RISING z=10.0**, quant-desk **1 document**, and ordinary `/v1/ask` with **4
  citations**, no retrieval degradation notes, and `techwire::tw-004`
  suppressed. The temporary DB ended at 14 rows with 0 NULL fingerprints or
  canonical ids. Before and after the live runs and golden, `data/core.db`
  remained **1,764 rows** with SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
- Teardown: `cored` and the mock model were stopped; ports 8788 and 8899 were
  clear. The live gate did not trip, so T2 is complete.

### H1 — harvest evidence hardened (verified 2026-07-20)

- `RobotsCache::allowed` now emits one behavior-neutral, greppable decision line
  containing origin, exact disposition (`Body(allow|deny)`,
  `Unavailable(allow|deny)`, or `Unreachable(deny)`), path, allow/deny outcome,
  and effective crawl-delay. It performs only reads and logging; the returned
  allow/deny value and subsequent `apply_crawl_delay` path are unchanged.
- `run`'s robots evidence grep now matches only `robots:` /
  `effective-crawl-delay`; it no longer includes the broad `arxiv` alternative
  that mislabeled page progress as robots evidence.
- The HC13 checklist is computed from the captured ingest JSON, numbered page
  lines, and the SQLite cursor-row query. It has no static `[ ]` claims.
- Positive live run, fresh `data/live-smoke.db`, window 2026-07-17 through
  2026-07-20: **1,764 fetched/new**, page 1 = 1,300 and page 2 = 1,764, 0 parse
  errors. The robots section contained only the real lines
  `robots: https://oaipmh.arxiv.org -> Unavailable(allow) ...
  effective-crawl-delay=0.500s`. All four evidence boxes were checked:
  documents > 0, pages > 1, source result parse-clean, and cursor row present.
- Negative control on the disposable smoke DB: its high-water was set beyond
  the configured window, and the real endpoint returned `fetched=0, new=0,
  ok=true` with one zero-document page. The harness reported **NOT VERIFIED**
  and all four boxes were unchecked, including the cursor-row box despite a
  stale row being present. The successful 1,764-document snapshot was restored
  afterward; the T2 failure snapshot is preserved at
  `/private/tmp/intel-platform-t2-blocked-live-smoke.db`.
- Verification: `bash -n run` passed; targeted clippy for compliance + net
  ingest passed under `-D warnings`; workspace check/test passed with 0 rustc
  warnings and **80 tests**; net check/test passed with 0 rustc warnings and
  **17 tests**; shell **69 passed** with the existing 1 deprecation warning.
  Fmt's known B0 inventory remains the same 13 files; T6 still owns it.
- Golden E2E was re-run after the change and is byte-identical in every anchor:
  acme **13 → 12**, `techwire::tw-004` dropped for `osdaily::osd-004` at
  hamming **12**, DeepSeek **RISING z=10.0**, re-ingest **+0**, quant-desk **1
  document**, and `/v1/ask` **4 citations** with `techwire::tw-004` suppressed.
  `data/core.db` remained 1,764 documents with SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
- H1 intentionally does **not** repair T2's capped-run completion bug. T2
  remains blocked exactly as recorded above.

### T6 — clippy + fmt promoted to a blocking gate (verified 2026-07-20)

- The lint fix and gate are separate as required. Commit `097b017` contains
  only Rust formatting plus relocation of `row_to_document`, the embeddings
  `impl SqliteStore`, and vector helpers before the final `#[cfg(test)] mod
  tests`; no behavior or invariant changed. The gate/status change is the
  following commit.
- `cargo clippy --workspace --locked --all-targets -- -D warnings`: exit 0.
  `items_after_test_module` no longer fires. The two deliberate
  `unnecessary_map_or` allows remain because replacing them with
  `Option::is_none_or` would require Rust 1.82, above the offline 1.78 floor.
- `cargo fmt --all -- --check`: exit 0. `.github/workflows/ci.yml` now names the
  lint job blocking and sets `continue-on-error: false`; the prior report-only
  and "commented out" descriptions have been corrected.
- Full regression matrix after the lint fix: warning-denied workspace check
  exit 0; **80 workspace tests passed**; warning-denied net check exit 0; **17
  net ingest tests passed**; shell **69 passed** with the existing single
  third-party Starlette deprecation warning.
- Golden E2E used fresh temporary DB
  `/private/tmp/intel-platform-t6-golden.VdLRbK/golden.db` and was unchanged:
  acme **13 → 12**, `techwire::tw-004` dropped for `osdaily::osd-004` at
  hamming **12**, DeepSeek **RISING z=10.0**, re-ingest **+0**, quant-desk **1
  document**, and `/v1/ask` **4 citations** with `techwire::tw-004` suppressed.
- Before and after the golden run, `data/core.db` remained **1,764 documents**,
  6,729,728 bytes, mtime `2026-07-20 09:22:16 +0800`, SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
  Ports 8788, 8790, 8786, and 8899 were clear after teardown.

### T1 — HC1 structurally enforced on `/v1/ask` (verified 2026-07-20)

- Decision-gate corpus: read-only `data/core.db`, **1,764 IndexOnly live arXiv
  documents**. Normalization is lowercase alphanumeric token runs, matching the
  shipped Rust implementation. Clean trials comprised ten explicitly written
  analytical answers (including the normal golden mock answer) against every
  document, plus one answer per four-document context that repeats only the
  already-public citation titles. That yields **17,640 single-document clean
  trials** and **4,851 four-document clean trials**. Leak trials used one
  substantive complete sentence (at least 12 tokens, wholly visible inside the
  800-character model context) from **1,763 documents**; token lengths were min
  16, p10 25, median 33, max 76. One record,
  `arxiv-cs::oai:arXiv.org:2510.24819`, has no punctuation-delimited 12-token
  sentence in its visible prefix and was recorded rather than silently counted.
- Measured sweep (rates are hits / trials; `four-doc FPR` is the operational
  selection column):

  | n | single-doc FPR | four-doc FPR | seeded-leak TPR |
  |---:|---:|---:|---:|
  | 2 | 0.172619 | 0.490414 | 1.000000 |
  | 3 | 0.005442 | 0.109050 | 1.000000 |
  | 4 | 0.000000 | 0.078747 | 1.000000 |
  | 5 | 0.000000 | 0.053185 | 1.000000 |
  | 6 | 0.000000 | 0.030097 | 1.000000 |
  | 7 | 0.000000 | 0.018347 | 1.000000 |
  | 8 | 0.000000 | 0.010513 | 1.000000 |
  | 9 | 0.000000 | 0.006390 | 1.000000 |
  | 10 | 0.000000 | 0.004535 | 1.000000 |
  | 11 | 0.000000 | 0.002474 | 1.000000 |
  | 12 | 0.000000 | 0.001237 | 1.000000 |
  | 13 | 0.000000 | 0.001031 | 1.000000 |
  | 14 | 0.000000 | 0.000618 | 1.000000 |
  | 15 | 0.000000 | 0.000206 | 1.000000 |
  | **16** | **0.000000** | **0.000000** | **1.000000** |
  | 17 | 0.000000 | 0.000000 | 0.999433 |
  | 18 | 0.000000 | 0.000000 | 0.999433 |
  | 19 | 0.000000 | 0.000000 | 0.998298 |
  | 20 | 0.000000 | 0.000000 | 0.997731 |

- **Selected `n = 16`, measured rather than assumed.** It is the only tested
  point with zero false positives in all 4,851 operational clean trials and
  100% recall across all 1,763 seeded sentences. `n = 15` retains one false
  positive; at `n = 17`, recall begins to fall. The anticipated `n ≈ 8` would
  have falsely refused 1.0513% of the four-document clean trials and was
  rejected.
- `intel_core::attest_answer` returns the original answer byte-for-byte when
  clean, ignores redistributable licenses, and on any IndexOnly overlap returns
  the constant `Answer withheld because it reproduced non-redistributable
  source text.` plus document-id-only violations. `POST /attest` fails closed on
  unknown context ids and accepts at most the same eight documents as retrieval.
  The core still does not call an LLM.
- The failure-capable double is real: `tools/mock_openai.py --leak` extracts a
  substantive IndexOnly sentence from the exact prompt. The shell negative
  control first asserted that the sentence was present in the model answer;
  `/v1/ask` then returned only the refusal. A second E2E against real cored,
  real HTTP, the shell API, and leaking mode produced the same refusal.
- Acceptance matrix: core tests cover IndexOnly refusal, CcBy pass-through, and
  unmangled analytical output; a cored test executes the handler against a real
  store; shell executes the leaking mock. Warning-denied workspace check passed
  with **84 Rust tests**; net check passed with **17 net tests**; shell **70
  passed** with the existing one Starlette deprecation warning; clippy and fmt
  both passed.
- Normal golden E2E used fresh temporary DB
  `/private/tmp/intel-platform-t1-golden.oD23lB/golden.db` and remained exact:
  acme **13 → 12**, `techwire::tw-004` dropped for `osdaily::osd-004` at hamming
  **12**, DeepSeek **RISING z=10.0**, re-ingest **+0**, quant-desk **1 document**,
  and `/v1/ask` retained its ordinary mock answer, **4 citations**, and
  `techwire::tw-004` suppression. `data/core.db` remained 1,764 documents,
  6,729,728 bytes, mtime `2026-07-20 09:22:16 +0800`, and SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
  All local ports were clear after teardown.

### T5 — redirects re-gated before each origin (verified 2026-07-20)

- Design 1 was selected deliberately: both reqwest clients set
  `redirect(Policy::none())`. The document path resolves `Location` manually,
  permits only HTTP(S), bounds the chain at 10 redirects, and runs the existing
  publisher-policy + operator-deny + politeness gate before every request. A
  robots-file redirect is not followed and therefore fails closed.
- Failure-capable cross-origin test: the fake page server returned
  `https://first.test/start` → 302
  `https://second.test/blocked` and had a successful second body ready. The
  robots fake returned allow for the first origin and `Disallow: /blocked` for
  the second. Measured calls were both origins' `/robots.txt`, but only the
  first document URL; result was `RobotsDisallowed` for the second URL. The
  forbidden request therefore never occurred.
- Same-origin test: `https://same.test/start` → `/final` returned `finished`;
  page calls were start + final, while the robots fake recorded exactly one
  `/robots.txt` fetch. The process-scoped cache prevented redundant policy I/O.
- Fixture gate stayed exact: the existing failure-capable
  `a_fixture_fetch_never_asks_the_publisher_for_permission` test passed with
  both the fake's call count and `RobotsCache::fetches()` at **0**. RSS and OAI
  fixture branches remain separate from `net::get_text`.
- The first full workspace test run exposed a separate pre-existing isolation
  defect and was **not counted as a pass**: store test
  `duplicate_ingest_maps_to_one_canonical_id` found 3 rows instead of 2.
  `tmp_store()` still used timestamp-only filenames; the correctly qualified
  test passed alone (1/1), confirming a parallel collision. The test helper now
  includes pid + process-global atomic sequence + timestamp, matching cored's
  proven isolation shape. A full parallel store run then passed 9/9, followed
  by the complete workspace passing 84/84. No production store code changed.
- Final acceptance matrix: warning-denied workspace and net checks passed;
  **84 workspace tests**, **19 net ingest tests**, and **70 shell tests** passed
  (the existing one third-party Starlette deprecation remains); clippy and fmt
  passed. No dependency or MSRV change.
- Golden E2E used fresh temporary DB
  `/private/tmp/intel-platform-t5-golden.qNIV2J/golden.db` and was byte-identical:
  acme **13 → 12**, `techwire::tw-004` dropped for `osdaily::osd-004` at hamming
  **12**, DeepSeek **RISING z=10.0**, re-ingest **+0**, quant-desk **1 document**,
  and `/v1/ask` retained the ordinary mock answer, **4 citations**, and
  `techwire::tw-004` suppression. `data/core.db` remained 1,764 documents,
  6,729,728 bytes, mtime `2026-07-20 09:22:16 +0800`, and SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
  All local ports were clear after teardown.

### T3 — SimHash persisted and consumed (verified 2026-07-20)

- **Entering-state correction:** the runbook's statement that the 1,764-row
  `data/core.db` had no fingerprint column was false. Direct SQLite measurement
  returned **1,764 rows, 0 NULL `simhash`, 0 NULL `canonical_id`**, and
  `pragma_table_info` found `simhash`. The schema, ingest-time write, canonical
  assignment, and one stored-equals-fresh test were already present. What was
  actually missing was a pre-column migration, update-time fingerprint refresh,
  and use of the stored value by `/view`; `dedup_near` still recomputed it.
- `dedup_near` now accepts `(Document, u64)` pairs. Core sector filtering loads
  persisted pairs from the store, and a NULL fingerprint is an error rather than
  a fallback recompute. A deliberately violating double gives two unrelated
  documents the same supplied fingerprint: they collapse at distance 0, proving
  the consumer uses the supplied value. `update_document` now refreshes the
  fingerprint from the changed title/body.
- `SqliteStore::open` now upgrades a table without `simhash` and backfills every
  NULL from the same title-plus-body function. The backfill is transactional and
  suspends/recreates the external-content FTS update trigger so unchanged text is
  not deleted/reinserted. The first targeted compile failed on a lifetime in the
  new verifier and was fixed; the next targeted test exposed the FTS-trigger
  interaction as `database disk image is malformed`. That failure was not
  counted as a pass. The transactional trigger suspension fixed it, and the
  unchanged targeted command then passed **14/14** tests across extract/store/view.
- Migration proof used disposable copy
  `/private/tmp/intel-platform-t3.qbNTxc/precolumn.db`. Before migration it had
  **1,764 rows** and no `simhash` column. After opening it through the shipped
  migration: **1,764 stored fingerprints, 0 fresh-compute mismatches, 0 canonical
  mismatches** against `data/core.db`, the column was present, and both NULL
  counts were 0. The verifier also measured the actual archive directly:
  **1,764 stored fingerprints, 0 mismatches**.
- Final matrix: warning-denied workspace and net checks passed; **86 workspace
  tests**, **19 net ingest tests**, and **70 shell tests** passed (the existing
  third-party Starlette deprecation warning remains); clippy and fmt passed. No
  dependency, lockfile, MSRV, sector, license, or robots-policy change.
- Golden E2E used fresh temporary DB
  `/private/tmp/intel-platform-t3-golden.gYgAMo/final.db` and was unchanged:
  acme **13 → 12**, `techwire::tw-004` dropped for `osdaily::osd-004` at hamming
  **12**, DeepSeek **RISING z=10.0**, re-ingest **+0**, quant-desk **1 document**,
  and `/v1/ask` retained the ordinary mock answer, **4 citations**, and
  `techwire::tw-004` suppression. The fixture DB finished at 14 rows with 0 NULL
  fingerprints/canonical ids. `data/core.db` retained **1,764 rows**, 6,729,728
  bytes, mtime `2026-07-20 09:22:16 +0800`, and SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
  Ports 8788, 8790, 8786, and 8899 were clear after teardown.

### T4 — real model deferred at credential gate (measured 2026-07-20)

- Environment checks returned absent for both `LLM_BASE_URL` and
  `LLM_API_KEY`; an assignment-only repository scan found no `LLM_API_KEY` value.
  `lsof` found no listeners on the documented local-model ports 8000, 8899, or
  11434.
- Fresh no-credential network probes corrected the previous cycle's egress
  result: DeepSeek `/v1/models` returned **401** and OpenAI `/v1/models` returned
  **401**. Both hosts are reachable today, but neither is usable without a key.
  `./run verify-llm` exited **2** with its request to set `LLM_BASE_URL` and
  `LLM_API_KEY`.
- Gate outcome: **DEFERRED, not passed.** `verify_llm.py` was not green against a
  real endpoint and the real-model HC1 spot-check was not run. The deterministic
  mock was used only for the mandatory regression golden; it is not T4 evidence.
- Golden E2E used fresh temporary DB
  `/private/tmp/intel-platform-t4-golden.x5mEQL/golden.db` and was unchanged:
  acme **13 → 12**, `techwire::tw-004` dropped for `osdaily::osd-004` at hamming
  **12**, DeepSeek **RISING z=10.0**, re-ingest **+0**, quant-desk **1 document**,
  and `/v1/ask` retained the ordinary mock answer, **4 citations**, and
  `techwire::tw-004` suppression. The fixture DB finished at 14 rows with 0 NULL
  fingerprints/canonical ids. `data/core.db` retained **1,764 rows**, 6,729,728
  bytes, mtime `2026-07-20 09:22:16 +0800`, and SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
  Ports 8788, 8790, 8786, and 8899 were clear after teardown.

### T7 — robots single-flight skipped at one-writer gate (measured 2026-07-20)

- `config/schedule.json` expands to five jobs (two source ingests, one sector
  ingest, one refresh, and one full pipeline), confirmed by
  `python3 -m intel_shell.scheduler --dry-run`. They are not five workers:
  `Scheduler.tick` invokes each due `job.action()` synchronously in one `for`
  loop. Both supported drivers preserve that topology: the in-process mode is
  one loop, and `deploy/intel-pipeline.service` is one `Type=oneshot` process
  running `scheduler --once`.
- Scheduler tests passed **8/8**. `lsof data/core.db` found no active holder at
  the decision point. A separate `pgrep` diagnostic could not enumerate
  processes because this Mac lacks the queried sysmond service (exit 3); that
  failed diagnostic is recorded and is not being presented as evidence.
- Gate outcome: **SKIPPED/DEFERRED as required.** The supported deployment still
  has exactly one synchronous writer, so the second-concurrent-harvest trigger
  has not fired. No single-flight lock or concurrency test was added; either
  would be speculative and would violate the task's decision gate.
- Golden E2E used fresh temporary DB
  `/private/tmp/intel-platform-t7-golden.HPED3p/golden.db` and was unchanged:
  acme **13 → 12**, `techwire::tw-004` dropped for `osdaily::osd-004` at hamming
  **12**, DeepSeek **RISING z=10.0**, re-ingest **+0**, quant-desk **1 document**,
  and `/v1/ask` retained the ordinary mock answer, **4 citations**, and
  `techwire::tw-004` suppression. The fixture DB finished at 14 rows with 0 NULL
  fingerprints/canonical ids. `data/core.db` retained **1,764 rows**, 6,729,728
  bytes, mtime `2026-07-20 09:22:16 +0800`, and SHA-256
  `ddb2c7fb81038b670104fb8d619e7cd15a021f3e9028ba6be59f0604fafc8f3a`.
  Ports 8788, 8790, 8786, and 8899 were clear after teardown.

### T4C — reproducible split-provider configuration (verified 2026-07-23)

- `./run` now loads a root `.env`; `.env` and `.env.*` are ignored while the
  secret-free `.env.example` is committed. `LLM_CHAT_PROFILE=lan|online`
  selects independent chat settings, `LLM_EMBED_*` selects an embedding
  provider separately, and the legacy shared `LLM_BASE_URL` variables remain a
  fallback. `./run config` prints resolved endpoints/models with keys redacted.
- Failure-capable tests configured an intentionally wrong legacy endpoint and
  proved both LAN and online chat profiles plus the embedding role overrode it.
  A proxy-sensitive transport then raised unless a loopback `CoreClient` used
  `trust_env=False`; the loopback case passed and the remote control retained
  `trust_env=True`. A verifier test injected a 16-token IndexOnly overlap and
  proved the public guard detects it, while a CC-BY/short-overlap control passed.
- `./run verify-llm` now builds and starts `cored` on a fresh temporary fixture
  database, requires the 13-document ingest, runs embeddings/fusion/public HC1,
  and tears down. Missing configuration exited **2** with a concise error and no
  traceback. The real LAN retry started that isolated core and ingested all 13
  fixtures, then measured **No route to host** for embeddings and chat and
  failed honestly. A deterministic mock control then passed **6/6 required
  checks**: embeddings **13 missing → 0**, clean retrieval notes, 5 hybrid
  context documents, public ask with 5 citations including 5 IndexOnly
  documents, and no 16-token gated overlap. The mock result validates the
  harness, not T4.
- Harvest safety is now explicit: `./run config` measured a bare harvest target
  of `data/live-smoke.db`; `CORE_DB=data/named-smoke.db ./run config` measured
  the explicit override unchanged. `bash -n run` passed. The ignored local
  `.env` selects the supplied LAN URL and also stores the DeepSeek chat URL with
  both key fields blank; embeddings remain deliberately unset. `.env.example`
  matched no API-key-shaped secret.
- Final matrix: warning-denied workspace and net checks passed; **90 workspace
  tests**, **20 net ingest tests**, and **77 shell tests** passed (the existing
  third-party Starlette deprecation warning remains); clippy and fmt passed;
  locked Rust **1.78.0** offline check passed with warnings denied.
- Golden E2E used
  `/private/tmp/intel-platform-t4c-final-golden.UCwRAP/golden.db` and remained
  exact: initial fixture ingest **13**; acme re-ingest **+0**; **12** analyzed;
  `techwire::tw-004` dropped for `osdaily::osd-004` at hamming **12**; DeepSeek
  **RISING z=10.0**; a second acme run again added **0**; quant-desk saw exactly
  **1 document**; public `/v1/ask` returned the ordinary mock answer with **4
  citations**, no retrieval degradation notes, and `techwire::tw-004`
  suppressed. The temporary DB ended at **14 rows, 0 NULL fingerprints, 0 NULL
  canonical ids**, integrity `ok`; ports 8788 and 8899 were clear after
  teardown.
- Gate outcome: **T4C complete; T4 still deferred.** The operator's LAN 501 and
  DeepSeek 404 embedding responses, followed by the Codex LAN reachability
  failure, mean no real embedding backfill or real public HC1 pass occurred.
  No mock or BM25-only result was promoted to real-model evidence.

### T4W — split-provider wire gate recorded (verified 2026-07-23)

- Resolved non-secret roles were LAN chat at
  `http://192.168.0.192:8080/v1`, model `default`, and DMXAPI embeddings at
  `https://www.dmxapi.cn/v1`, model `openAI`. Keys remained redacted.
- Operator run 1 created an isolated fixture DB and ingested **13/13** fresh
  documents. Both embedding operations returned HTTP **503**, so backfill and
  hybrid retrieval failed. The real LAN chat request did complete: public
  `/v1/ask` returned **4 citations**, all 4 cited documents were `IndexOnly`,
  and the returned answer contained no 16-token gated overlap. Verifier result:
  **3/5 required checks passed**, one latency diagnostic. This is a partial
  real HC1 pass and an overall T4 failure.
- Operator run 2 independently repeated the embedding 503 at 0.14s and the
  fusion failure, then blocked in the public chat request. The operator
  interrupted it after **1m41s**; Starlette/AnyIO printed a
  `KeyboardInterrupt` traceback before cleanup stopped the core. That outcome is
  a verifier control-flow/timeout defect, not provider success and not a second
  HC1 result.
- A fresh Codex probe sourced the ignored `.env`, printed only the redacted
  endpoint/model, and made one embedding request. It independently returned
  HTTP **503 Service Unavailable** from
  `https://www.dmxapi.cn/v1/embeddings`. T4's embedding gate therefore remains
  tripped; no mock, BM25-only result, or independent chat success was promoted
  to completion.
- Documentation-only acceptance matrix: warning-denied workspace and net
  checks passed; **90 workspace tests**, **20 net ingest tests**, and **77 shell
  tests** passed (the existing Starlette deprecation warning remains); clippy,
  fmt, `bash -n run`, and the locked Rust **1.78.0** offline check passed.
- Complete golden E2E used
  `/private/tmp/intel-platform-t4w-golden.5nqKKI/golden.db` and remained exact:
  initial fixture ingest **13**; acme re-ingest **+0**; **12** analyzed;
  `techwire::tw-004` dropped for `osdaily::osd-004` at hamming **12**; DeepSeek
  **RISING z=10.0**; second acme run **+0**; quant-desk exactly **1 document**;
  public `/v1/ask` **4 citations**, no retrieval notes, and
  `techwire::tw-004` suppressed. The DB ended **14/0/0**, integrity `ok`; ports
  8788 and 8899 were clear.
- `data/core.db` remained **1,764/0/0**, integrity `ok`, and SHA-256
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`.
  This step made no runtime, dependency, lockfile, policy, or protected-corpus
  change.

### T4H — verifier fail-fast and provider timeouts (verified 2026-07-23)

- The failure-capable controls were run before implementation and failed in the
  intended ways: role-specific timeout assertions observed the hard-coded
  120 seconds, malformed/non-positive timeouts were accepted, and a 503
  embedding double reached a public-API constructor wired to raise. The
  unchanged targeted command reported **6 failed, 7 passed**. Those same
  controls pass after the repair.
- `ChatClient` and `EmbedClient` now resolve positive
  `LLM_CHAT_TIMEOUT_SECONDS` / `LLM_EMBED_TIMEOUT_SECONDS`, falling back to
  `LLM_TIMEOUT_SECONDS` and then the existing 120-second library default.
  Role-specific tests override a deliberately wrong shared value; a legacy
  shared-timeout test configures both roles; `0`, `-1`, and `not-a-number` are
  refused. The local ignored `.env` and `.env.example` set both roles to
  **30 seconds**, and `./run config` prints those values with keys redacted.
- Verifier stages are strict prerequisites. A failed embedding backfill returns
  immediately before fusion and public HC1; a failed fusion returns before
  chat. The 503 negative control exposes a callable chat double and a public
  API constructor that fail the test if reached. It now exits 1 after exactly
  one embedding call. Manual interruption is also converted to exit 130 with a
  concise message at the script boundary.
- Live negative control against the still-configured DMXAPI provider: fresh
  isolated core, **13/13** fixtures, HTTP **503** at embedding stage in **0.17s**,
  then `stopping before fusion/public HC1`; summary **0/1**, no LAN chat call,
  no traceback, and clean teardown. The wrapper command completed in **2.4s**.
  This is a cleaner T4 failure, not progress through the gate.
- Deterministic success control used a separate `/dev/null` env file and the
  mock on loopback with 5-second role timeouts. It passed **6/6**: embeddings
  **13 → 0 missing**, clean retrieval notes, 5 hybrid context documents, public
  ask 5 citations, 5 IndexOnly documents, and no gated overlap. The mock remains
  harness evidence only.
- Final matrix: warning-denied workspace and net checks passed; **90 workspace
  tests**, **20 net ingest tests**, and **84 shell tests** passed (the existing
  Starlette deprecation warning remains); clippy, fmt, `bash -n run`, Python
  bytecode compilation, and the locked Rust **1.78.0** check passed.
- Complete golden E2E used
  `/private/tmp/intel-platform-t4h-final-golden.jF8Ser/golden.db` and remained exact:
  initial **13**; acme **+0**, **12 analyzed**; `techwire::tw-004` dropped for
  `osdaily::osd-004` at hamming **12**; DeepSeek **RISING z=10.0**; second acme
  **+0**; quant-desk **1**; public ask **4 citations**, no retrieval notes, and
  `techwire::tw-004` suppressed. The DB ended **14/0/0**, integrity `ok`; ports
  8787/8788/8899 were clear.
- `data/core.db` remained **1,764/0/0**, integrity `ok`, and SHA-256
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`.
  T4 remains deferred; no dependency, lockfile, sector, license, robots, dedup,
  or protected-corpus invariant changed.

## 9. v0.8.1 measured execution

### B0.1 — entering baseline (verified 2026-07-24)

- **Entering-state correction recorded before proceeding:** `git log --oneline
  -5` confirmed `HEAD` at `6d42a75` (`fix: bound real-model verification`), but
  `git status --porcelain` returned
  `?? TASKS-v0.8.1-EXECUTION.md`. The runbook's clean-worktree assertion was
  therefore false: the operator-added v0.8.1 runbook was present and untracked,
  exactly as reported in the task request. No other worktree change was present.
- Toolchains measured: pinned `rustc/cargo 1.91.1`, floor
  `rustc/cargo 1.78.0`, and Python **3.11.4** in both the system interpreter and
  `.venv`.
- Full matrix: warning-denied workspace check exit 0; **90 workspace tests**
  passed; warning-denied `cored --features net` check exit 0; **20 net ingest
  tests** passed; **84 shell tests** passed with the existing one third-party
  Starlette deprecation warning; clippy and fmt exit 0; locked warning-denied
  Rust **1.78.0** workspace check exit 0.
- `./run down` completed, and `lsof -nP -iTCP:<port> -sTCP:LISTEN` confirmed
  ports **8787, 8788, and 8899 clear** before the artifact measurements.
- Protected artifact measurements:
  - `data/core.db`: **1,764 documents**, 0 NULL `simhash`, 0 NULL
    `canonical_id`, integrity `ok`; **6,729,728 bytes**; mtime
    `2026-07-23 20:08:13 +0800`; SHA-256
    `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`;
    cursor row `arxiv-cs | NULL | 2026-07-20 | NULL |
    2026-07-23 12:08:13`.
  - `data/live-smoke.db`: **2,600 documents**, 0 NULL `simhash`, 0 NULL
    `canonical_id`, integrity `ok`; **9,490,432 bytes**; mtime
    `2026-07-23 07:45:38 +0800`; SHA-256
    `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`;
    cursor row `arxiv-cs |
    verb%3DListRecords%26metadataPrefix%3Doai_dc%26from%3D2026-07-22%26until%3D2026-07-22%26set%3Dcs%26skip%3D88
    | NULL | 2026-07-22 | 2026-07-22 23:45:38`.
- The golden ran on disposable database
  `/private/tmp/intel-platform-b0.1-golden.L0tF8n/full-golden.db`. The first
  sandboxed bind was refused by the execution environment (`Operation not
  permitted`) and was not counted; the permitted local-only run completed
  normally. Exact measured result: initial ingest **fetched=13, new=13**; first
  acme pipeline re-ingest **+0**; **12 documents analyzed**;
  `techwire::tw-004` dropped for `osdaily::osd-004` at hamming **12**; DeepSeek
  **RISING, z=10.0**, corroborated by **3 sources**; second acme ingest **+0**;
  quant-desk **1 document**; `/v1/ask` returned **4 citations**, suppressed
  `techwire::tw-004`, and had clean retrieval notes; acme search for `deepseek`
  returned **6 hits** versus quant-desk **0**, with every `IndexOnly` snippet
  NULL; a bad key returned **401**. The disposable DB ended at **14 rows**, 0
  NULL fingerprints/canonical ids, integrity `ok`.
- The explicit command sequence used for that golden, in order, was:

  ```bash
  export ENV_FILE=/dev/null
  export CORE_DB=/private/tmp/intel-platform-b0.1-golden.L0tF8n/full-golden.db
  export SUBSCRIPTIONS_PATH=config/subscriptions.hashed.json
  export LLM_CHAT_PROFILE=
  export LLM_CHAT_BASE_URL=http://127.0.0.1:8899/v1
  export LLM_EMBED_BASE_URL=http://127.0.0.1:8899/v1
  export LLM_BASE_URL=http://127.0.0.1:8899/v1
  export NO_PROXY=127.0.0.1,localhost
  export no_proxy=127.0.0.1,localhost
  ./run up
  curl -fsS -X POST http://127.0.0.1:8788/ingest \
    -H 'content-type: application/json' \
    -d '{"sectors":["science","technology"]}'
  PYTHONPATH=shell .venv/bin/python -m intel_shell.pipeline \
    --client acme-research
  curl -fsS 'http://127.0.0.1:8788/view?sectors=science,technology'
  PYTHONPATH=shell .venv/bin/python -m intel_shell.pipeline \
    --client acme-research
  PYTHONPATH=shell .venv/bin/python -m intel_shell.pipeline \
    --client quant-desk
  PYTHONPATH=shell .venv/bin/python -m uvicorn intel_shell.app:app \
    --host 127.0.0.1 --port 8787
  curl -fsS -H 'Authorization: Bearer ak_acme_7f3d9c' --get \
    --data-urlencode 'q=What is DeepSeek-V4?' \
    http://127.0.0.1:8787/v1/ask
  curl -fsS -H 'Authorization: Bearer ak_acme_7f3d9c' --get \
    --data-urlencode 'q=deepseek' http://127.0.0.1:8787/v1/search
  curl -fsS -H 'Authorization: Bearer ak_quant_2b81aa' --get \
    --data-urlencode 'q=deepseek' http://127.0.0.1:8787/v1/search
  curl -sS -o /dev/null -w '%{http_code}\n' \
    -H 'Authorization: Bearer bad-key' http://127.0.0.1:8787/v1/signals
  ./run down
  ```

  The API server was backgrounded solely so the four public requests could
  execute in the same captured run; teardown killed it before `./run down`.
- After the golden, both protected hashes matched the values above and all
  three local ports were clear. No source, license, robots, dedup, dependency,
  lockfile, or protected-database bytes changed.

### G1 — golden E2E made executable (verified 2026-07-24)

- `./run golden` now builds the offline core, creates a fresh `mktemp -d`
  database and brief-output directory, starts the real Rust HTTP core,
  deterministic 32-dimensional mock model, and public FastAPI shell, executes
  all subscriber flows over loopback HTTP, and tears down all three services
  plus the temporary directory on EXIT. It never points a write at `data/`.
- `tools/golden_e2e.py` prints and enforces **11 named checks**: initial
  fetched/new 13/13; acme pipeline completion; 12 analyzed; exact near-duplicate
  ids and hamming 12; DeepSeek RISING at 10.0 from three sources; second acme
  ingest +0; quant-desk 1; public ask 4 citations with `techwire::tw-004`
  suppressed; all IndexOnly search snippets NULL; acme/quant DeepSeek hits 6/0;
  and bad-key 401. The restored-tree command exited 0 with **11/11**.
- Failure-capable control executed before trusting the harness: 20 unique words
  were temporarily appended to the `techwire::tw-004` fixture body. The
  unchanged command exited **1** with **7/11** passing and explicitly named
  `near-duplicate drops techwire::tw-004, keeps osdaily::osd-004 at hamming 12`
  as failed. Dependent checks also caught 13 analyzed, no duplicate pair,
  DeepSeek z=12.0, and 5 citations/no suppression. The fixture was restored
  byte-for-byte; the next run returned 11/11.
- Mock readiness now probes a real embedding POST and remains pid-aware; public
  API readiness is also pid-aware. The first implementation run exposed a
  missing `PYTHONPATH=shell` export and failed loudly before assertions; that
  was repaired and is not counted as a pass. A later attempt to neutralize
  ambient core authentication by exporting an empty `CORE_TOKEN` correctly
  produced HTTP 401; the deterministic harness now **unsets** the token instead,
  matching the normal token-off state, and the following 11/11 run is the one
  counted.
- `AGENTS.md §5.5` now requires the command rather than a hand-reimplemented
  ritual, and §6 names its assertions as authoritative over the human summary.
  `.github/workflows/ci.yml` has a separate `golden E2E (blocking)` push/PR job
  with `continue-on-error: false`.
- Final matrix: warning-denied offline and net checks passed; **90 workspace
  tests**, **20 net ingest tests**, and **84 shell tests** passed (the existing
  one Starlette warning remains); clippy, fmt, `bash -n run`, Python bytecode
  compilation, and the locked warning-denied Rust **1.78.0** check passed.
- Both protected hashes remained exact:
  `data/core.db`
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and `data/live-smoke.db`
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`.
  Ports 8787/8788/8899 were clear after teardown. No dependency, lockfile,
  source, policy, license, sector, dedup, or protected-corpus change occurred.

### P1 — live-harvest evidence paths protected (verified 2026-07-24)

- `harvest_db_path()` now gives a bare command a fresh
  `data/live-<UTC timestamp>-<pid>.db` and adds a numeric suffix if that path
  already exists. `ENV_FILE=/dev/null ./run config` measured
  `data/live-20260724T064350Z-16718.db`; an explicit
  `CORE_DB=data/named-smoke.db` remained unchanged.
- `config/protected-artifacts.sha256` records the complete B0.1 hashes for
  `data/core.db` and `data/live-smoke.db`. The live-harvest command resolves and
  prints its destination **before the reachability request**, compares
  canonicalized paths, and refuses any protected entry.
- Failure-capable path controls: `CORE_DB=data/core.db` and
  `CORE_DB=./data/live-smoke.db` both exited **2 before network access**, named
  the artifact and manifest, printed its full recorded SHA-256, and supplied an
  exact fresh `CORE_DB=data/live-…db ./run harvest-arxiv` incantation.
- `./run verify-artifacts` measured **2/2 MATCH**. A disposable byte-for-byte
  copy of `data/core.db` was then appended with `planted-mismatch`; verification
  against a disposable manifest exited **1**, reporting expected
  `db2f186e…1a37a0` versus actual
  `2223a92b24024ba80ce288e6c4550287336fdfcabf71d7db0f7701406c62e183`
  and **0/1 match**. The real manifest immediately returned 2/2 again.
- `ENV_FILE=/dev/null ./run test` now begins with the artifact check and
  measured 2/2 exact matches before **90 workspace**, **20 net**, and **84 shell
  tests** passed. The standalone final matrix also passed warning-denied
  offline/net checks, the same test counts, clippy, fmt, `bash -n run`, and the
  locked warning-denied Rust **1.78.0** check.
- `./run golden` remained **11/11**. Final real hashes are still
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`;
  ports 8787/8788/8899 were clear. No protected bytes were deleted, renamed, or
  rewritten, and no dependency, lockfile, source, license, robots, sector, or
  dedup behavior changed.

### E1 — embedding model keys enforce one dimension (verified 2026-07-24)

- The pre-fix controls all failed in the intended way. Store accepted a
  1,024-dimensional vector after a 32-dimensional vector under
  `shared-model` (`Ok(1)`); `/retrieve` returned `notes: []` for a planted
  32-versus-1,024 mismatch; and a freshly ingested but pre-embedded verifier
  database printed a green `0 missing -> 0` backfill before reaching a
  failure-capable later-stage double. Those are the three silent-success paths
  E1 was required to remove.
- `SqliteStore::upsert_embeddings` now validates an entire write against the
  dimension already stored for its model key before inserting anything. Its
  structured `DimensionMismatch` error names the model plus existing and
  received dimensions. The 32→1,024 control now fails the write, reports
  `shared-model`, `32`, and `1024`, and leaves the count at one.
- Vector search filters rows whose recorded/blob dimension differs from the
  query and returns a mismatch count. `/retrieve` turns that count into a
  visible note; the planted control reports one ignored stored embedding for
  `shared-model` against query dimension 1,024 and returns no vector hits.
  `GET /embeddings/stats?model=` reports count, common dimension, and whether
  legacy rows contain inconsistent dimensions.
- The mock roles now use reserved explicit names (`mock-chat` and
  `mock-embed-32`). `verify-llm` exits **2 before starting services** when a
  non-loopback embedding endpoint has no `LLM_EMBED_MODEL`; the measured
  control named the ambiguous model-key risk. `.env.example` requires an
  explicit embedding model.
- A fresh verifier database now passes backfill only after at least one provider
  request, zero remaining missing documents, and stored statistics matching the
  returned dimension. The pre-embedded control now prints **FAIL**, reports
  zero real requests, and stops before fusion/public HC1. A corrected isolated
  mock success control (with ambient proxy bypassed for loopback) passed **6/6**:
  13 missing → 0, one request, provider/stored dimension 32, clean retrieval
  notes, five hybrid context documents, five public citations, five IndexOnly
  citation documents, and no gated overlap. This is harness evidence only, not
  real-provider evidence.
- `./run golden` remained exactly **11/11**, so E1's strict dimension guard did
  not trip its decision gate. Final matrix: warning-denied offline and net
  checks passed; **92 workspace tests**, **20 net tests**, and **85 shell
  tests** passed; clippy, fmt, `bash -n run`, Python bytecode compilation, and
  locked warning-denied Rust **1.78.0** check passed.
- `./run verify-artifacts` remained **2/2 MATCH**. Final hashes are
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`;
  port 8788 was clear. HC3 is intact: core only stores and compares vectors and
  makes no provider calls. No dependency, lockfile, source, license, robots,
  sector, dedup, or protected-corpus behavior changed.

### T4L — local embedding attempt deferred at transport gate (measured 2026-07-24)

- The operator supplied two distinct Docker launch commands: chat on
  `192.168.0.192:8080` using
  `gemma-4-26B-A4B-it-UD-IQ4_XS.gguf` without `--embeddings`, and a dedicated
  embedding process on port 8081 using
  `embeddinggemma-300M-Q8_0.gguf` with the required `--embeddings` CLI flag.
  These are operator-supplied launch parameters, not evidence that either API
  served a request.
- Four live probes were executed. `POST :8080/v1/embeddings`,
  `GET :8081/v1/models`, and `POST :8081/v1/embeddings` each returned curl
  exit **7**, status **000**, `Couldn't connect to server`, in 1–2 ms. A
  separate bounded `GET :8081/health` retry returned the same exit 7/status
  000. No HTTP response body existed. Therefore the historical 501
  `--embeddings` diagnosis was neither confirmed nor refuted in this attempt,
  and the embedding endpoint's API-reported model name and vector dimension
  remain unmeasured.
- A later operator-requested LAN retry ruled out an address/proxy mistake. The
  Codex host's active `en0` address measured **192.168.0.105/24**, and ARP
  resolved `192.168.0.192` to `5c:b4:7e:cd:45:92` on that interface. Requests
  to both `/health` and `/v1/models` were repeated with `curl --noproxy '*'`;
  ports 8080 and 8081 still returned exit **7** / status **000** immediately.
  ICMP reported `No route to host`, while the ARP entry proves the target was
  visible at layer 2. The remaining evidence is therefore server-side: neither
  published TCP port accepted a connection during the retry window.
- The T4L decision gate is **tripped and the step is deferred**. No fallback
  provider or mock was tried. `./run config` still resolves LAN chat
  `http://192.168.0.192:8080/v1`, model `default`, but retains the previously
  configured DMXAPI embedding role `https://www.dmxapi.cn/v1`, model `openAI`;
  that provider's measured 503 evidence above is preserved. The local role was
  not written into configuration because its endpoint never became reachable.
- Output-preserving checks remained green: `./run golden` passed **11/11**;
  `./run verify-artifacts` passed **2/2**; warning-denied offline and net checks
  passed; **92 workspace**, **20 net**, and **85 shell** tests passed; clippy,
  fmt, and locked warning-denied Rust **1.78.0** check passed. The first
  sandboxed MSRV attempt could not write rustup metadata and was not counted;
  the permitted rerun completed successfully.
- Final protected hashes remained
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`;
  local ports 8787/8788/8899 were clear. Documentation only; no runtime,
  dependency, lockfile, policy, provider configuration, or protected-corpus
  change occurred.

### T4P — adversarial HC1 verifier built; live exercise deferred (measured 2026-07-24)

- `tools/verify_llm.py` now wraps the resolved chat client while the real public
  `/v1/ask` handler runs, capturing the exact raw model answer passed to core
  `/attest` without adding raw or gated text to the public response. The
  verifier then calls `/attest` directly with that raw answer and the same
  citation document ids, and reports the returned `violations` ids.
- The adversarial question targets a retrieved IndexOnly document by title and
  asks for its opening sentence verbatim. Classification is exactly
  `GUARD FIRED` (raw overlap, violations present, and both direct/public clean
  answers equal the constant refusal), `NOT EXERCISED` (the model declined or
  paraphrased), or `LEAK` (overlap reached the public answer or the raw overlap
  was not consistently refused). `LEAK` is a required-check failure. The
  Python overlap oracle remains deliberately independent from core `/attest`,
  so it can expose a core regression rather than merely repeat it.
- Failure-capable control: before the implementation, the targeted test failed
  collection because the adversarial classifier did not exist. Afterward, a
  canned answer containing a real 20-token IndexOnly span, paired with a
  deliberately broken no-violation attestation result, reported **LEAK**,
  named `source::gated`, and made `_finish()` exit **1**. Separate controls
  report `GUARD FIRED` with `violations: ['source::gated']` and
  `NOT EXERCISED` as a warning.
- Full-path deterministic controls used isolated fixture databases. The normal
  mock passed **6/6 required checks** and reported `NOT EXERCISED`, zero
  violations. The deliberately leaking mock passed **7/7 required checks**:
  public `/v1/ask` returned the core refusal and the adversarial leg reported
  **GUARD FIRED**, with violation
  `arxiv-cs::oai:arXiv.org:2607.01455`. Both are failure-capable harness
  evidence only, not evidence about a real model.
- The real-model acceptance remains **deferred**. Fresh `GET /v1/models`
  probes to LAN chat port 8080 and embedding port 8081 both returned curl exit
  **7**, status **000**, `Couldn't connect to server`, with no HTTP body.
  Therefore no real model received the adversarial prompt, and the record
  cannot yet say that core HC1 has been tripped by a real model.
- `./run golden` remained exactly **11/11** and protected artifacts remained
  **2/2**. Final matrix: warning-denied offline/net checks passed; **92
  workspace**, **20 net**, and **88 shell** tests passed; clippy, fmt,
  `bash -n run`, Python bytecode compilation, and locked warning-denied Rust
  **1.78.0** check passed. Protected hashes stayed
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`;
  ports 8787/8788/8899 were clear. No dependency, lockfile, policy, public
  response shape, or protected-corpus change occurred.

### T4 — uninterrupted closure run deferred at embedding backfill (measured 2026-07-24)

- Preflight completed in order: `./run down`; ports 8787/8788/8899 clear;
  protected artifacts **2/2 MATCH**; and `./run config` resolved LAN chat at
  `http://192.168.0.192:8080/v1`, model `default`, timeout 30s, plus DMXAPI
  embeddings at `https://www.dmxapi.cn/v1`, model `openAI`, timeout 30s. Keys
  remained redacted.
- One `./run verify-llm` run was executed without interruption. Its isolated
  database ingested **13 fetched / 13 new** fixtures. The first and only
  provider stage returned `503 Service Unavailable` from
  `https://www.dmxapi.cn/v1/embeddings` after **0.16s**. The verifier reported
  embedding backfill **FAIL**, stopped with **0/1 required checks** and one
  latency warning, tore down its core, and exited 1.
- The T4 gate is **tripped and T4 remains deferred**. In this run there was no
  successful embedding request or measured dimension, no zero-missing result,
  no fusion/retrieval result, no chat latency, no public `/v1/ask`, no
  IndexOnly context check, and no adversarial `GUARD FIRED` /
  `NOT EXERCISED` outcome. Earlier partial LAN-chat evidence and mock controls
  do not carry forward into this run.
- The provider's HTTP response body was **not exposed by the current
  `EmbedClient` error path**; the captured output contains the exact status,
  URL, and httpx status reference, but no body. No second provider request was
  made after the gate tripped. Therefore the runbook's requested body evidence
  is explicitly absent rather than inferred or fabricated.
- Mandatory post-task regression checks remained green: `./run golden`
  **11/11**, protected artifacts **2/2**, warning-denied offline/net checks,
  **92 workspace**, **20 net**, and **88 shell** tests, clippy, fmt,
  `bash -n run`, Python bytecode compilation, and locked warning-denied Rust
  **1.78.0** check. Protected hashes remained
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`.
  No runtime, dependency, lockfile, provider configuration, or
  protected-corpus change occurred.

### T4L — local embedding role confirmed over live SSH-forwarded wire (verified 2026-07-24)

- The operator demonstrated both LAN health endpoints returning HTTP 200 from
  `192.168.0.105`, while Codex's command runner and in-app browser remained
  unable to route private-LAN addresses. A user-owned SSH local forward mapped
  chat to `127.0.0.1:18080` and embeddings to `127.0.0.1:18081`; these are
  transport-only aliases for the real servers, not mock endpoints.
- Both forwarded `/health` and `/v1/models` endpoints returned HTTP **200**.
  Chat reported `gemma-4-26B-A4B-it-UD-IQ4_XS.gguf`, completion capability,
  context 32,768. Embeddings reported
  `embeddinggemma-300M-Q8_0.gguf`, context 2,048, metadata width 768.
- The required diagnosis is now confirmed from the body, not inferred:
  `POST :18080/v1/embeddings` returned HTTP **501** and
  `{"error":{"code":501,"message":"This server does not support embeddings. Start it with \`--embeddings\`","type":"not_supported_error"}}`.
  The dedicated `POST :18081/v1/embeddings` returned HTTP **200**, one item at
  index 0, model `embeddinggemma-300M-Q8_0.gguf`, and an actually measured
  vector length of **768**.
- The ignored `.env` now resolves the production roles directly:
  LAN chat `http://192.168.0.192:8080/v1` with the reported Gemma model, and
  LAN embeddings `http://192.168.0.192:8081/v1` with the reported
  EmbeddingGemma model; both timeouts remain 30s. `./run config` printed these
  exact non-secret values. DMXAPI's prior 503 evidence remains above.
- HC13 boundary at this step: the short one-item wire request proved endpoint,
  shape, index, and dimension. Full-document context-window behavior, a
  13-document batch, short/out-of-order responses, and load stalls were not
  exercised here and remain for the uninterrupted T4 verifier; they are not
  inferred from the one-item success.
- Post-task verification remained green: `./run golden` **11/11**, protected
  artifacts **2/2**, warning-denied offline/net checks, **92 workspace**,
  **20 net**, and **88 shell** tests, clippy, fmt, `bash -n run`, and locked
  warning-denied Rust **1.78.0** check. Protected hashes remained exact.
