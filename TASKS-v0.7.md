# TASKS.md — intel-platform v0.7 work order

**Audience:** an autonomous coding agent (Claude Opus 4.8 / Claude Code, or equivalent) with a shell, a Rust toolchain, and network access. **Read `STATE.md` and `README.md` in full before writing any code.** This document is the authoritative task list; STATE.md §4 is its source.

**Starting point:** v0.6.2. 49 Rust tests + 69 shell tests green, 0 warnings. `TASKS-v0.6.md` is fully worked (T1–T9: done, or skipped/deferred with a recorded gate). v0.6.2 moved the toolchain to **Rust 1.91.1**, committed `Cargo.lock`, and — for the first time in the project's life — **`cargo build -p cored --features net` compiles.**

**The theme of this cycle: stop trusting fixtures.** Every invariant in this platform has been verified against deterministic offline fixtures, which is why the golden E2E has been stable for three cycles. But fixtures prove the *state machine*, not the *wire*. Nothing has ever fetched a real document. v0.7 is where the platform touches reality — and reality is where the compliance obligations (HC7, HC8) stop being theoretical.

---

## 0. Environment prerequisites (verify before T1)

- **Rust ≥ 1.86** for `--features net`; ≥ 1.75 still suffices for the offline build. The repo pins **1.91** in `rust-toolchain.toml`. Ubuntu 24.04 packages it directly — `apt-get install rustc-1.91 cargo-1.91`, then `export PATH=/usr/lib/rust-1.91/bin:$PATH`. No rustup, no mirror.
- Python **3.12**, venv, `pip install -r shell/requirements.txt`.
- **Network egress to `export.arxiv.org`** — this is the gating prerequisite for T1, and it is exactly what the v0.6 sandbox lacked (`403 host_not_allowed` at the proxy). *Check it first*: `curl -sI "https://export.arxiv.org/oai2?verb=Identify"` must return 200. If it doesn't, T1 defers and the cycle starts at T2.
- Optional for T3: an OpenAI-compatible endpoint (vLLM box or DeepSeek API) reachable from the machine.
- Shell note: if the container shell is `dash`, avoid brace expansion; write explicit loops.

---

## 1. Hard constraints — apply to EVERY task, no exceptions

HC1–HC11 from `TASKS-v0.6.md` carry over **unchanged** and are not restated here. Re-read them; the two that bite hardest this cycle are:

- **HC1 — License gating stays in core.** A live harvest ingests documents whose licenses we did not author. Gating is enforced in Rust; no live-fetch change may create a path where the shell can emit gated text.
- **HC8 — Compliance in live fetching.** Until v0.7 this was a promise about code paths nothing exercised. From T1 onward it is a promise about **packets we actually send to someone else's server.** Honor the robots gate and the polite rate limiter on *every* request, ≥3s between OAI-PMH pages, and obey `503 Retry-After`.

Two new ones, both earned the hard way:

- **HC12 — Builds are locked.** `Cargo.lock` is committed and CI builds `--locked`. The edition2024 wall existed because an unlocked workspace re-resolved to whatever crates.io published that week. Never delete the lock to "fix" a resolution error; understand the error instead.
- **HC13 — A fixture is a hypothesis, not a proof.** Any task that touches the live path must state, explicitly, what its fixtures *cannot* test (timeouts, partial reads, malformed real-world XML, a 503 mid-harvest, a server that lies about `resumptionToken`) — and must not claim done on fixture evidence alone.

## 2. Operating rules for the executing agent

- Run the full baseline (`cargo check --workspace --locked`, `cargo test`, `pytest shell/tests`) before touching code; run the full suite after every task.
- One task per "commit-sized" change; do not interleave tasks.
- If a task's decision gate says "skip," document the decision in STATE.md rather than forcing it.
- Do not refactor opportunistically outside a task's stated scope, especially in `crates/`.
- **Never point a source at the live web to "see what happens."** Live fetching is gated on T2 for anything that isn't arXiv's OAI-PMH endpoint. See T1's scope note.

---

## 3. Tasks (dependency order)

### T1 — The first live arXiv harvest  [P0 — the whole point of the cycle]

Everything below the seam is ready and has never been used. `--features net` builds, paging and cursors are implemented and unit-tested, the limiter and `Retry-After` handling exist. What has never happened is a single real HTTP request.

**Why arXiv first, and *only* arXiv:** its OAI-PMH interface is an official, documented harvesting API with an explicit politeness contract (~3s between requests, `503 Retry-After`) that the core already implements and tests. That contract is a *stronger* and more specific permission than `robots.txt` inference, so this task is safe to run before T2. **The RSS/HTML sources are NOT in scope** — pointing `techwire`/`osdaily`/`finance` at live URLs before T2 lands would mean fetching from the open web without ever having read a `robots.txt`, which is precisely the compliance gap HC8 exists to close. Leave their `"fixture"` keys alone.

**Do:**
1. `cargo build -p cored --features net --locked`.
2. In `config/core.json`, remove **only** the `"fixture"` key from the `arxiv-cs` source so its `"url"` is fetched live. Keep the set narrow (a single `cs.*` set, a short `from=` window) — the first live harvest should be small enough to read by eye.
3. `POST /ingest {"sectors":["science"],"sources":["arxiv-cs"]}` and watch it.
4. Re-run immediately: the second harvest must issue `from=` = the stored high-water mark and ingest **+0 new**.
5. Interrupt a harvest mid-set (kill `cored` between pages) and restart: it must resume from the persisted `resumptionToken`, not restart the set.

**Testing objectives (the parts fixtures could never reach — HC13):**
- **Politeness, observed on the wire, not in a mock:** log request timestamps; confirm ≥3s spacing between pages against the real endpoint. A counting fake proved the limiter is *called*; this proves it is *obeyed*.
- **A real `503 Retry-After`** if arXiv issues one (it will, under load) — confirm the bounded backoff honors the header rather than hammering.
- **Real-world XML:** arXiv's live records carry fields, encodings, and edge cases the two-page fixture chain does not. Confirm `roxmltree` parsing survives them; record any record that fails to parse rather than dropping it silently.
- **Cursor durability across a real interrupt**, not a simulated one.
- Golden E2E still passes afterward on the fixture sources (the live source is additive; it must not perturb the acme numbers — if it does, that is a real finding and belongs in STATE.md, not a silent delta).

**Decision gate:** no egress to `export.arxiv.org` ⇒ **defer and say so.** Do not mock a live harvest and mark it done — the entire value of this task is that it is not a mock.

**Done when:** a real harvest paged, checkpointed, resumed, and advanced its high-water mark against the real server; observed page spacing recorded in STATE.md; document count and any parse failures recorded.

### T2 — Real `robots.txt` discovery  [P1, core — the gate on all remaining live sources]
Today the robots gate does correct RFC-9309 *path matching* (`*`, `$`, `Allow` exceptions, per-host limiters — T9.4), but it matches against **policy we configured, not policy we fetched**. No `robots.txt` has ever been read. That was harmless while everything was a fixture. It stops being harmless the moment a non-OAI source goes live.

**Do:** in `crates/compliance`, fetch and cache `robots.txt` per host (behind `--features net`, honoring the same limiter), parse it, and feed the result into the existing gate. `texting_robots` is the noted drop-in; evaluate it against the same style of decision gate T2-of-v0.6 used (build on 1.91, transitive footprint, does it change any *existing* allow/deny outcome).

**Constraints:** cache with a TTL and a bounded size; a fetch failure must **fail closed** (no robots.txt ⇒ do not assume permission for a source we haven't been configured to trust). The offline/fixture path must remain fully deterministic and must not attempt any fetch.

**Testing objectives:** unit tests over a fixture `robots.txt` (wildcards, `Allow` exceptions, `Crawl-delay`, an empty file, a 404, a 500); a test that fetch failure denies rather than permits; a test that the configured-policy path is unchanged when no live fetch occurs.

**Done when:** tests green; a live source's first request is preceded by a real `robots.txt` fetch; STATE.md records the cache policy and the fail-closed decision.

### T3 — Point the LLM at a real endpoint  [P1, ops + verification — carried over from v0.6/T7]
Unchanged and still gated. The checklist is already a script: `tools/verify_llm.py` runs the whole thing — embeddings backfill, fusion no longer BM25-only, `retrieval.notes` clean, and the **HC1 spot-check** (ask a question whose best evidence is an IndexOnly doc; confirm the *public* answer never reproduces gated text, even though the model legitimately read it as context).

**Do:** set `LLM_BASE_URL`/`LLM_API_KEY` (+ `LLM_CHAT_MODEL`/`LLM_EMBED_MODEL`), run `tools/verify_llm.py`, run the full pipeline for both clients, exercise `/v1/ask`, run `--llm-enrich` and confirm substantive entity suggestions (the mock intentionally yields none). Record model names + observed latency in STATE.md.
**Gate:** no endpoint reachable ⇒ defer, do not mock-and-declare-done.

### T4 — CI: locked, warning-free, MSRV-enforced  [P1, infra — cheap, and it prevents this cycle's whole backstory]
The project has now been bitten twice by the same class of failure (ecosystem drift breaking a build nobody was building). The lock is committed; the remaining hole is that nothing *checks*.

**Do:** a CI workflow that runs, on the pinned toolchain: `cargo check --workspace --locked` (0 warnings, `-D warnings`), `cargo test --workspace --locked`, `cargo check -p cored --features net --locked`, and `pytest shell/tests`. Add a scheduled job that runs `cargo update --dry-run` and *reports* drift without applying it — the point is to learn about the ecosystem moving **before** it breaks a build, not after.
**Testing objective:** deliberately introduce a warning locally and confirm CI fails.
**Done when:** green on a clean checkout; a `--features net` job is included (it is the one that was silently broken for two cycles precisely because nothing built it).

### T5 — LSH banding for near-dup  [P2, core — the T8 note's one substantive finding]
`docs/T8-scale-design-note.md` concluded that **LSH is the swap most likely to be needed first**: `dedup_near`'s pairwise scan is O(n²) in kept documents, and since T9.1 it re-materializes canonical ids on *every* ingest that adds rows. A live arXiv harvest (T1) is the first thing that will actually grow the corpus, so this is the first cycle where the quadratic term is more than a footnote.

**Do:** SimHash banding (split the 64-bit fingerprint into bands, index by band, compare only within-band candidates) behind the existing `dedup_near` surface.
**Constraints:** the **output must not change** — `dedup_near` keeps the earliest document by `(published_day, id)`, a global property of the corpus (STATE §2.10). LSH is an *index*, not a new rule. Recall must be exact for the hamming ≤16 threshold, or the threshold must be re-derived and the change called out loudly.
**Testing objectives:** the golden corpus still drops `techwire::tw-004` and keeps `osdaily::osd-004` (hamming 12); a property test over synthetic fingerprints showing banded candidate generation misses no pair the exhaustive scan finds; a benchmark showing the scan is sub-quadratic at n = 10k.
**Gate:** if exact recall at hamming ≤16 cannot be preserved, **stop** — a faster dedup that silently changes which document is canonical is a corpus corruption, not an optimization.

### T6 — Seam hardening for multi-host  [CONDITIONAL — carried over from v0.6/T5]
Unchanged. Still conditional on core and shell running on *different hosts*; they still do not. `CORE_TOKEN` is implemented on both sides. If triggered: prefer a Unix domain socket for same-host isolation (`CORE_BIND=unix:/run/intel/cored.sock`); mTLS only for a genuine cross-host split. **Gate:** single-host ⇒ mark deferred and move on. Do not build speculative mTLS.

### T7 — Scale swaps  [DEFERRED — design-level only]
Postgres/pgvector, tantivy, materialized views. `docs/T8-scale-design-note.md` stands: Postgres is a **concurrency** trigger (a second writer), not a size one, and may never fire. Do not implement unless the owner re-prioritizes. Note that T5 above lifts LSH *out* of this bucket, because it now has a concrete trigger.

### T8 — Known-limitation pick-ups  [P2, each small & independent — do after P1s, skip freely]
1. `/view` is memoized per (sector-set, generation) rather than materialized; a restart re-warms it. Materialize on the ingestion schedule if warm-up cost shows up.
2. One SQLite connection behind a `Mutex`. Fine while the shell is the single caller — revisit the moment a second writer exists (that is also the Postgres trigger; see T7).
3. Pre-v0.6 archives spanning a month boundary carry the old `Day` encoding (`y*372 + …`) and should be rebuilt; fresh ingests are unaffected. Ship a one-shot rebuild tool *if* such an archive actually exists — check before building it.

---

## 4. Global definition of done (the whole cycle)

1. `cargo check --workspace --locked`: **0 warnings**. `cargo check -p cored --features net --locked`: **0 warnings**. `cargo test`: all green (≥ 49 — record the new number). `pytest shell/tests`: all green (≥ 69 — record).
2. **Golden E2E regression** (run `cored` + `tools/mock_openai.py`, then the acme pipeline) — unchanged unless a task legitimately changes it, in which case explain the delta in STATE.md:
   - acme ingests **13** docs (Finance skipped); dedup drops `techwire::tw-004`, keeps `osdaily::osd-004` (hamming 12) ⇒ **12 analyzed**;
   - signals: **DeepSeek RISING z=10.0** (3-source corroboration), vLLM RISING z≈2.67, NVIDIA+Qwen CORROBORATED, "Helios Labs" EMERGING;
   - immediate re-run: **+0 new**; quant-desk sees only its **1** doc.
   - *Note:* if T1 puts a live source into the same DB, run the golden regression against a **fixture-only DB**. The golden numbers describe the fixture corpus; do not "update" them to absorb live documents.
3. Public API spot-checks: bad key ⇒ 401; entitlement-disjoint search (acme **6** hits vs quant **0** for "deepseek"); IndexOnly snippet `null` in `/v1/search`; brief renders "excerpt withheld"; webhook: unset secret ⇒ 503, bad sig ⇒ 401, signed event flips sectors and persists hashed.
4. Demo credentials: `ak_acme_7f3d9c` (science+technology), `ak_quant_2b81aa` (finance); hashed equivalents in `config/subscriptions.hashed.json`. Auth is `Authorization: Bearer <key>`.
5. STATE.md bumped to v0.7 with: verified-in-environment section, per-task outcomes (done / skipped-with-reason / deferred), updated next steps. README + `examples/coreClient.ts` consistent with any contract change (HC10). Versions bumped; repomix XML regenerated.

## 5. Env var reference (current)

**Core:** `CORE_CONFIG` `CORE_ENTITIES` `CORE_DB` `CORE_BIND` `CORE_TOKEN`.
**Shell:** `CORE_URL` `CORE_TOKEN` `SUBSCRIPTIONS_PATH` (a path, or `sqlite:///…`) `LLM_BASE_URL` `LLM_API_KEY` `LLM_CHAT_MODEL`/`LLM_EMBED_MODEL` (fallback `LLM_MODEL`), `API_KEY_PEPPER` (regenerate hashes if changed), `BILLING_WEBHOOK_SECRET` (unset ⇒ webhook 503), `STRIPE_WEBHOOK_SECRET` (unset ⇒ `/v1/billing/stripe` 503), `STRIPE_PRICE_SECTORS` (JSON price→sectors map).
