# STATE.md — intel-platform handoff

**As of:** 2026-07-20 · **Version:** v0.7.4 (core-shell) · **Status:** **80 Rust workspace tests green with 0 _rustc_ warnings** (`cargo check --workspace --locked --all-targets` under `RUSTFLAGS=-D warnings`, both the offline and `--features net` builds), **17 net-path ingest tests green**, and **69 shell tests green** against a FAKE core (with 1 Starlette deprecation warning). "0 warnings" means **rustc** warnings; clippy and fmt are tracked separately (see below). Golden end-to-end re-verified unchanged in B0.

**v0.7.4 acts on a detailed third-party (Codex) review that found the real root cause of the failed on-site harvest — plus three orchestration bugs and one test-isolation bug, all mine, all now fixed.** The 34-minute silence was *not* a long harvest and *not* the harvest logic; it was the `run` harness failing against an environment condition and then hanging on a control-flow bug:

- **Root cause — a foreign process owned the port.** An orphaned `cored` from another copy of the repo (in the operator's `.Trash`) was still listening on 8788. This checkout's server failed to bind (`Address already in use`) and died.
- **Harness bug 1 — false readiness.** The readiness poll hit `/health` and got a 200 *from the orphan*, so it announced our server ready when ours had died. **Fixed:** `_start_cored` now (a) refuses up front if the port is already serving (`port_is_foreign`), naming the offending PID and the exact `lsof`/`kill` commands, and (b) waits with a **pid-aware** check that fails fast if the process we launched dies.
- **Harness bug 2 — infinite poll under `set -e`.** The ingest ran in a backgrounded subshell that wrote a completion sentinel *after* `curl`; when `curl` timed out non-zero, `set -e` aborted the subshell before the sentinel was written, and the watch loop span forever (~29 of the 34 minutes). **Fixed:** the subshell runs `set +e` and **always** writes the sentinel with curl's exit code; the watch loop is additionally time-bounded.
- **Harness bug 3 — `down` can't reach the orphan.** A pidfile only tracks servers we started. **Fixed:** `cmd_down` now reports a still-held port after cleanup, with the PID and kill command. (Also: `_start_mock_llm` still used `setsid`; switched to `nohup` — another latent macOS break.)
- **Test-isolation bug — parallel temp-DB collision.** `tmp_db()` named the per-test SQLite file from `SystemTime` nanos only; two parallel test threads in the same tick got the same path and clobbered each other (seen as a "fresh" DB already holding another test's rows — `new=4, fetched=7`). **Fixed:** a process-global atomic counter + pid in the name guarantees a distinct path per call. `cargo test` is now deterministic under default parallelism (verified across repeated runs).

**On the "0 warnings" claim — B0 correction, measured 2026-07-20.** It means *rustc* warnings (`-D warnings` on `cargo check`), and that remains true. The prior sentence claiming the test module had been moved last was **false**: `cargo clippy --workspace --locked --all-targets -- -D warnings` exits 101 with one `clippy::items_after_test_module` diagnostic at `crates/store/src/sqlite.rs:537`, naming the five items at lines 749–880 that still follow the test module. Re-running clippy with only that known lint allowed is otherwise clean. The two `clippy::unnecessary_map_or` crate-level allows remain deliberate in `intel-compliance` and `arxiv_oai`: the suggested `Option::is_none_or` is Rust 1.82+, above the offline 1.78 floor. `cargo fmt --all -- --check` also exits non-zero, with diffs in 13 Rust files. CI therefore correctly remains a **report-only** lint job (`continue-on-error`) until T6 fixes the tree and promotes the gate.

**T2 remains UNVERIFIED, and this run did not change that** — no documents were fetched, `data/core.db` held 0 rows, and none of the paging/XML/cursor evidence was produced. The harness bugs that blocked it are fixed, so the next `./run harvest-arxiv` on a box with a free port should finally reach the wire.

**Prior point releases (unchanged, kept for the record):** v0.7.1 per-source robots opt-in (§2.12); v0.7.2 `max_pages` cap + timeouts + progress logging; v0.7.3 removed Python 3.12-only f-strings from `run` (crashed on the on-site 3.11).

1. **arXiv migrated its OAI-PMH endpoint.** `export.arxiv.org/oai2` now **301-redirects** to `oaipmh.arxiv.org/oai` (observed live). `config/core.json` now points at the canonical host directly, which also sidesteps the redirect-origin gap (below) for arXiv specifically.
2. **The harvest was blocked by a robots FALSE POSITIVE, not by the gate working correctly.** `oaipmh.arxiv.org` serves no `robots.txt` (a 404 HTML page). The v0.7 default is fail-closed on 404 (`MissingPolicy::Deny`), which is correct for an *unknown* host but wrong for a cooperative, operator-configured endpoint that publishes no robots.txt *on purpose*. The block was the system refusing exactly the access arXiv built the endpoint to serve. **Fixed in v0.7.1** — see §2.12.
3. **The redirect-origin gap (documented below, still open as T5) is now confirmed live**, not hypothetical: `export.arxiv.org/oai2` 301s to a different origin whose robots.txt the gate would not have read.

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
                          /retrieve /embeddings(/missing) /signals/record /docs
                          crates: core compliance ingest extract enrich analyze
                                  store registry view retrieve
```

**Config split:** `config/core.json` (sectors/sources/licenses) + `config/entities.json` (gazetteer) are core-owned; `config/subscriptions.json` (clients/sectors/keys) and `config/schedule.json` are shell-owned. Demo keys: `ak_acme_7f3d9c` (science+technology), `ak_quant_2b81aa` (finance).

## 2. Load-bearing placement decisions (do not move these casually)

1. **License gating stays in the CORE.** `store.search` nulls snippets for IndexOnly; `/view` hydrates evidence with `excerpt: Option<String>` gated by `License::redistributable()`. Consequence: `briefing.py` can be rewritten arbitrarily and *cannot* leak gated text — it never receives it.
2. **Entitlement DECISION in the shell, sector FILTERING in the core.** A shell bug can grant wrong sectors, never bypass filtering.
3. **The core never calls an LLM.** Shell pulls `GET /embeddings/missing`, calls the provider, `POST /embeddings` vectors back. `/retrieve` accepts `model` + `query_vector`.
4. **Full bodies ARE served on internal `/retrieve` and `/docs`** — passing IndexOnly text to a model as context is analysis, not redistribution; loopback-internal, not public.
5. **`/view`'s `kind` is `format!("{:?}", SignalKind)`**, so the shell can post signals straight back to `/signals/record`.
6. All v0.1–v0.3 invariants unchanged: dedup (hamming ≤16) BEFORE all statistics; mentions per (entity, doc); Corroborated suppressed when Rising; discovery on bodies only; FNV-1a determinism; RRF k=60.
7. **(v0.6) Source selection is core business, not shell business.** `/ingest` takes `{sectors, sources?}`. `sources` names connector ids; **each is still validated against `sectors`**, so a named source outside the caller's entitlement is refused, not run — the sector filter is not a suggestion that a source id can bypass (HC2). Selection lives in `registry::select_sources`, which returns `unknown_ids` as **structured per-id errors rather than panicking**. Omitting `sources` entirely preserves the exact pre-v0.6 behavior (every source in the sectors, in config order) — a regression test pins this (HC5).
8. **(v0.6) Harvest cursors live in the core store, not the shell.** New `cursors(source_id, cursor, high_water, updated_at)` table. `cursor` is the in-flight OAI-PMH `resumptionToken` (checkpointed **after every page**, so an interrupted harvest resumes mid-set instead of restarting); `high_water` is the max `datestamp` of the last *completed* harvest, replayed as `from=` for incremental fetching. High-water advance is **monotonic** (ISO dates ⇒ lexicographic max is chronological max), so a late-arriving old record can't roll the mark backward. Cursors are the documented exception to atomic-JSON persistence (HC9): they belong in SQLite, next to the documents they track. Connectors that don't page (RSS) ignore the seam entirely.

9. **(v0.6/T6) Provider vocabulary is normalized INTO the neutral one, never the other way round.** `billing.apply_event` speaks `subscription.created|updated|deleted|key_rotated` and nothing else. Stripe enters through `adapters/stripe.py`, which verifies Stripe's signature scheme and maps `customer.subscription.*` onto those events. Consequences worth keeping: a second provider is a second adapter, not a change to the store or the entitlement model; and the freshness check on Stripe's signed timestamp is load-bearing, because a *genuine* captured request replayed later carries a perfectly valid MAC — the timestamp is the only thing that refuses it. Keys are compared against a *set* of active hashes, so rotation has a grace window and revocation is just rotation with none.
10. **(v0.6/T9) Dedup identity is a function of the corpus, not of arrival order.** `dedup_near` keeps the earliest document by `(published_day, id)` — a global property. So `canonical_id` is persisted as a **re-materialization of that same rule on every ingest that adds rows**, NOT as a first-seen-wins assignment at insert. This matters more since T3: sources now run on independent clocks, so arrival order genuinely varies, and an incremental assignment would let two runs over the same 13 documents disagree about which copy is canonical. Relatedly, `/retrieve` deliberately does **not** filter by `canonical_id`: it keeps whichever of a near-dup pair *the query* ranked higher. Canonical id is a property of the corpus; relevance is a property of the question, and context assembly is a question about the question. Only the fingerprint is reused there (persisted, no longer recomputed per request).

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
2. **T3 — point the LLM at a real endpoint. DEFERRED: gate not satisfiable, and deliberately NOT mocked-and-declared-done.** Probed this cycle: `api.deepseek.com` and `api.openai.com` both **403 `host_not_allowed`** at the egress proxy; no vLLM listener on 8000/8899/11434; no `LLM_API_KEY`. (`api.anthropic.com` *is* reachable — it answers 401 — but it is not OpenAI-compatible, has no `/v1/embeddings`, and we have no key, so it is not a substitute.) `tools/verify_llm.py` still runs the entire checklist in one command; run it on a box with an endpoint and T3 closes.
3. **T6 — seam hardening for multi-host. DEFERRED: condition still not met.** Core and shell still run on one host (`cored` binds `127.0.0.1:8788`; `deploy/intel-pipeline.service` sets `CORE_URL=http://127.0.0.1:8788`). `CORE_TOKEN` is implemented on both sides. Per the task's own instruction, no speculative UDS and no mTLS were written. **Trigger:** the first genuine cross-host split.
4. **T7 — scale swaps. DEFERRED (design-level), and T5 *removed* LSH from this bucket rather than promoting it.** Postgres remains a **concurrency** trigger (a second writer), not a size one, and may never fire.
5. **T8 — known-limitation pick-ups. All three SKIPPED on their own stated preconditions, which were checked rather than assumed.** (a) Materialize `/view`: the precondition is "if warm-up cost shows up" — the corpus is 12 documents; it has not. (b) One SQLite connection behind a `Mutex`: the trigger is a second writer; there is none. (c) A rebuild tool for pre-v0.6 `Day` encodings: the task says *"check before building it"* — **checked, and no such archive exists.** `/data` is gitignored and archives are never shipped; every DB reachable on this box was created fresh this session from fixtures, on the new encoding. Building the tool would have been building for a hypothetical.

**The recommended top of the v0.8 queue, in order:**

1. **The live arXiv harvest** (T1 above), the moment a box with egress exists. Everything is ready; nothing else can falsify the paging.
2. **Persist the SimHash fingerprint** — the swap T5's measurements actually justify, and the one that replaces LSH on the T8 trigger table. `simhash(title + body)` is a pure function of the document, recomputed for *every* document on *every* dedup pass, and T9.1 runs that pass on every ingest that adds rows. It is **85% of dedup cost at n=10k**. Storing it as a column at ingest changes **no output whatsoever** (same fingerprints ⇒ same drops ⇒ same canonical ids) and is far smaller than an index. *Only after that* is the pairwise scan worth attacking — and by then the honest options (a tighter threshold, or a wider fingerprint at the same absolute distance) both change dedup semantics and must be argued on the merits, not smuggled in as a performance fix.
3. **Turn on `clippy` + `rustfmt` in CI.** Staged but commented out in `.github/workflows/ci.yml`, deliberately: the v0.7 sandbox's apt toolchain ships **neither component**, so neither could be *run* — and committing a gate you have not executed is how a repo ends up with a CI that is red on arrival, which is a CI everyone learns to ignore. Run `rustup component add clippy rustfmt`, then `cargo clippy --workspace --locked --all-targets -- -D warnings` and `cargo fmt --all -- --check`; if clean, uncomment the block.

## 5. Known limitations (documented, not hidden)

- ~~**Robots policy is configured, not discovered.**~~ **RESOLVED in v0.7 (T2)** — see §2.11 and §6b.
- ~~**"Rust 1.75 + `--locked` still builds the offline path."**~~ **FALSE, and it is the most important correction in this document.** The committed `Cargo.lock` is format **v4**, unparseable by cargo before **1.78**, so the claim could never have held — it had simply never been run. **The offline floor is now declared as 1.78**, measured across 1.75/1.76/1.78/1.91 and enforced by CI's `msrv` job. Re-encoding the lock to v3 *does* buy back 1.75 (75 tests green, resolution byte-identical) but cargo ≥ 1.78 rewrites it to v4 on the next lock modification, so that floor cannot be held. **The general lesson: a claimed property that nothing executes is not a property, it is a wish** — the same failure that let `--features net` sit broken for two cycles and that let "robots-compliant" mean "compliant with a policy we wrote ourselves."
- **The `--features net` floor is 1.86, and the error lies about why.** `icu_* 2.2.0` (via `idna_adapter`) declare `rust-version = 1.86`; edition2024 stabilizing in 1.85 is necessary but **not** sufficient. Worse, the failure surfaces at *dependency-download* time as `error: failed to download replaced source registry 'crates-io'`, which sends you looking at the registry instead of at MSRVs. Reproduced again this cycle on 1.75.
- **Correction to a v0.5 note** (unchanged from v0.6): `/v1/ask`'s `context_suppressed` names `techwire::tw-004`, not `osdaily::osd-004`, for the question actually tested. Suppression at context assembly is **rank-aware by design**, so which copy of a syndicated story is dropped depends on which one the query ranked higher. Treat *"one of the pair is suppressed"* as the golden, not a specific id.
- **`Day` values changed scale (T9.3).** `published_day` is days-since-1970. Pre-v0.6 archives spanning a month boundary would need a rebuild — **checked in v0.7: no such archive exists**, so no tool was built (T8.3).
- **`dedup_near` recomputes every fingerprint on every pass.** This — not the quadratic scan — is the real cost: **85% of dedup time at n=10k** (measured; `cargo run --release -p intel-extract --example dedup_bench`). See §6c and the T8 note.
- `/view` is memoized per (sector-set, generation) rather than materialized; a restart re-warms it. Cost is unmeasurable at 12 docs.
- One SQLite connection behind a `Mutex` (fine: the shell is the single caller); `cored` binds loopback by design.
- **HC1 IS NOT ENFORCED ON `/v1/ask`, AND ITS TEST IS VACUOUS. This is the most serious open issue in the project.** The architecture's headline claim — "license gating lives in core, so no shell rewrite can leak gated text" (§2.1) — is **true for `/view`, `/search`, and `/brief`, and false for `/v1/ask`.** On that one endpoint the model is *deliberately* handed the full bodies of IndexOnly documents (`prompts.BODY_CAP = 800` chars each), which is defensible — reading gated text as analysis context is not redistribution. But the model's answer is then returned to the client **verbatim and uninspected** (`app.py: "answer": answer`). The only thing standing between a gated source sentence and a public API response is **one sentence in a system prompt** (`ASK_SYSTEM`: "never reproduce sentences from sources marked IndexOnly"). A prompt is not an invariant. The leak vector here is not a shell rewrite — it is the model's own output, and no core invariant touches it.
  **Worse, the test that "covers" this cannot fail.** The only model in the suite is `tools/mock_openai.py`, a deterministic double **we wrote**, which returns a templated answer and is therefore structurally incapable of reproducing source text. The HC1 spot-check on `/v1/ask` has never been executed against anything able to violate it. This is the same failure mode that let `--features net` sit unbuilt for two cycles and let "robots-compliant" mean "compliant with a policy we wrote ourselves" — *a claimed property that nothing executes* — except that here the property is a **licensing** one. See `TASKS-v0.8.md` T1.
- **The robots gate is checked on the configured origin, but redirects are followed to a different one — NOW CONFIRMED LIVE (still open as T5).** Neither `reqwest::Client` in `crates/ingest/src/net.rs` sets a redirect policy, so reqwest's default applies: **up to 10 redirects, followed silently.** The first on-site harvest hit exactly this: `export.arxiv.org/oai2` **301-redirects** to `oaipmh.arxiv.org/oai`, so a request gated against `export.arxiv.org`'s robots.txt would fetch documents from `oaipmh.arxiv.org`, whose policy was never read. Per RFC 9309 the policy is **per-origin**, so the check must re-run on the final origin (or redirects must be disabled and followed manually). **Worked around for arXiv in v0.7.1** by pointing `config/core.json` at the canonical `oaipmh.arxiv.org/oai` directly (no redirect), but the gap is real for any other source that redirects cross-origin. See `TASKS-v0.8.md` T5.
- **The robots cache does not de-duplicate concurrent misses.** Two simultaneous first-requests to the same origin can both fetch `/robots.txt`. Bounded, harmless (the limiter still spaces them), and not worth a single-flight lock until there is a second writer — same trigger as Postgres.

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

## 8. v0.8 entering baseline — B0 (verified 2026-07-20)

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
- Environment note: port 8788 is held by a `cored` process B0 did not start,
  PID **59269**, executable from this checkout. This sandbox cannot signal it;
  the operator command is `kill 59269`. B0 used ports 8790/8899/8786 instead.
  T2 must not begin until `./run down` followed by
  `lsof -iTCP:8788 -sTCP:LISTEN -n -P` is clear.
