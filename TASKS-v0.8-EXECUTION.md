# TASKS-v0.8-EXECUTION.md — ordered runbook for Codex

This is the **execution order** for v0.8, derived from `TASKS-v0.8.md` (which
holds the full rationale for each task) and updated for the state as of
2026-07-20. Task IDs match `TASKS-v0.8.md`; new tasks surfaced from the
2026-07-20 live run carry `B` / `H` ids so nothing is renumbered.

**Entering state (2026-07-20).** v0.7.4: 80 Rust tests, 69 shell tests, 0 rustc
warnings on both build configs. **The live arXiv harvest reached the wire on
2026-07-20** — 1,764 records, two pages, `resumptionToken` paging, 0 parse errors
(see `PROGRESS-v0.8.md`). T2 is therefore nearly closed; the only remaining piece
is interruption-resume. Clippy is report-only in CI, and `sqlite.rs` still trips
`items_after_test_module` despite a `STATE.md` claim it was fixed (T6 reconciles
this).

**How to run this file.** Do the steps top to bottom. Obey `AGENTS.md §5` after
every one (verify → golden E2E → update `STATE.md` → append `PROGRESS-v0.8.md` →
check the box → commit). Owner tags:

- **🤖 = Codex executes and self-verifies end to end.** Do not ask the operator
  to run anything marked 🤖.
- **🧑 = one specific human input is required, named inline.** Everything else in
  that task is still Codex's.

**Global definition of done (from `TASKS-v0.8.md`):** golden E2E unchanged unless
a task declares otherwise; 0 warnings on `--workspace` **and** `--features net`;
all Rust and shell tests green; MSRV floor still 1.78; `STATE.md` updated with
what was *measured*.

---

## Step 1 · B0 — Verify the entering state before changing anything 🤖

**Objective.** Establish the real baseline empirically (the cycle-start ritual:
trust nothing in the summary). Produce the true numbers the rest of the cycle
regresses against.

**Gate.** If any baseline claim in `STATE.md` is false, **record the correction
first** and do not proceed until STATE reflects reality.

**Steps.**
1. Clean build + test, both configs and the shell (commands in `AGENTS.md §4`).
2. Run the golden E2E; record the exact outcome numbers.
3. Run `cargo clippy … -D warnings` and capture the lint list.
4. Determine which DB the golden E2E uses and whether it is the same
   `data/core.db` the live harvest writes (the 2026-07-20 run left 1,764 live
   docs there). **If they share a path, decide isolation now:** live smoke runs
   will use `CORE_DB=data/live-smoke.db` so the 12-doc golden corpus stays clean.

**Acceptance criteria.**
- Rust and shell test counts captured (expected 80 / 69; record actual).
- 0 rustc warnings on both configs (or the discrepancy recorded).
- Golden E2E outcome captured and matching `AGENTS.md §6` (or the delta recorded).
- Clippy inventory captured (expected: `items_after_test_module` ×N in
  `sqlite.rs`, plus the accepted `unnecessary_map_or` allows).
- The golden-vs-live DB question answered in writing.

**Done when** `STATE.md`'s header numbers are the ones you just measured, and the
DB-isolation decision is recorded.

---

## Step 2 · T2 — Close the live harvest: interruption-resume on the wire 🤖
*(needs network egress — available on this MacBook; not doable in the sandbox)*

**Gate result (updated 2026-07-23): PASSED.** The 2026-07-20 run exposed the
unconditional `complete()` bug; the 2026-07-22 attempt repaired the split write
and proved rollback/reopen locally but timed out before a live XML page. The
2026-07-23 reproof completed the exact two-run procedure below. Run 1 fetched
1,300 records and left a non-NULL token ending in `skip%3D522`. After a process
restart, run 2's first request carried that exact token and added the next 1,300
records; its next token advanced to `skip%3D88`. Both runs reported `ok=true`
and no parse error. `data/core.db` stayed byte-identical. See `STATE.md §8` and
`PROGRESS-v0.8.md`.

**Objective.** Prove the one T2 behavior fixtures cannot: that a harvest
interrupted mid-set **resumes from the SQLite cursor** rather than restarting.
Paging, parsing, and multi-page `resumptionToken` were proven live on 2026-07-20;
this is what remains.

**Corrective implementation now present.** A clean cap is no longer allowed to
fake interruption safety. The page's documents and the cursor that advances
past them are one SQLite transaction, with `pending_high_water` retained across
process restart. Guards include an injected commit failure, a cursor-triggered
transaction rollback, and a close/reopen between fixture pages. Do not regress
this back to separate `checkpoint()` / `complete()` calls while retrying the
wire procedure.

**Gate.** "Reached the wire" and "capped at N pages" are progress, not completion.
Completion requires the resume behavior *observed on the wire against real
arXiv*. If arXiv returns a single page for the chosen window, widen it
(`HARVEST_DAYS=10`) rather than declaring resume untested-but-fine.

**Why the obvious test is the wrong one.** The 2026-07-20 run *completed*, so it
called `complete()`, advanced `high_water` to ~2026-07-20, and cleared the resume
token. A plain re-run now harvests *incrementally from the new high-water* and
returns ~0 new docs — which exercises the high-water path, **not** the
interruption-resume path, and is easily mistaken for a passing resume test.

**Steps (Codex runs all of this).**
1. `./run down`; confirm `lsof -i :8788` is clear. *(If a foreign process holds
   the port — the macOS `.Trash` hazard — surface the printed `kill` command;
   this is the one place the operator may need to act.* 🧑*)*
2. Run a **capped** harvest so it stops with a checkpoint, not completion:
   `HARVEST_MAX_PAGES=1 CORE_DB=data/live-smoke.db ./run harvest-arxiv`
   (widen `HARVEST_DAYS` until the window is > 1 page).
3. Capture the cursor row: `sqlite3 data/live-smoke.db 'select source_id, cursor,
   high_water from cursors where source_id="arxiv-cs"'`. Assert `cursor` holds a
   non-empty `resumptionToken` (the *next* page), not NULL.
4. Run again: `HARVEST_MAX_PAGES=1 CORE_DB=data/live-smoke.db ./run harvest-arxiv`.
5. Capture cored.log and the ingest JSON from run 2. Assert the second run's first
   request carried the checkpointed token (continues from page 2+) and the doc
   count reflects continuation, not a restart from page 1.
6. If arXiv issues a real `503 Retry-After` under load, capture that the bounded
   backoff in `net.rs` honored it. Opportunistic — record "not observed" if it
   doesn't happen; do **not** force it.

**Acceptance criteria.**
- Run 1 leaves a non-NULL `cursor` (resumptionToken) in `cursors`.
- Run 2 begins from that token (log evidence) and does **not** re-fetch page 1.
- Real OAI-PMH XML parsed with 0 errors across both runs.
- `data/core.db` (the golden corpus) is untouched by these runs.
- 503/Retry-After: honored-and-captured, or explicitly recorded as not observed.

**Done (2026-07-23).** The cursor row + the two runs' logs show
resume-from-cursor on the wire; the measured evidence is recorded in
`STATE.md §8` and `PROGRESS-v0.8.md`.

---

## Step 3 · H1 — Harden the harvest harness so its evidence is real 🤖

**Objective.** The 2026-07-20 output *looked* like it proved robots handling and
paging, but the evidence was an artifact of a grep, not the run. Fix the harness
so "evidence" means evidence. *(Surfaced by review; not in the original
`TASKS-v0.8.md`.)*

**The two defects.**
- `run:364`'s robots grep pattern is `robots|crawl-delay|disallow|arxiv`. The
  `arxiv` alternative matches the `[arxiv-cs] page N` progress lines, so the
  "robots.txt fetch" section prints page output and reads as robots evidence when
  there is none. `net.rs` never logs an explicit robots verdict, so there is
  nothing real to match.
- `run:381–386` prints a static `[ ]` HC13 checklist that is never checked
  against outcomes — a decorative claim the harness does not execute.

**Steps.**
1. Add one explicit, greppable log line in the robots path
   (`crates/ingest` / `crates/compliance`) recording, per origin, the disposition
   actually taken, e.g. `robots: <origin> -> Body | Unavailable(deny|allow) |
   Unreachable(deny)` plus the effective crawl-delay. This is the real evidence
   the grep should find.
2. Narrow `run:364`'s grep to robots-only tokens (drop `arxiv`).
3. Make the HC13 checklist reflect the run: check each box from the captured
   result (documents fetched > 0; > 1 page seen; parse errors == 0; cursor row
   present) instead of printing static `[ ]`.

**Gate.** Harness-only. It must **not** change any core behavior or the golden
E2E. The `net.rs` log line is a `tracing` / `eprintln` addition and nothing more;
if it starts to touch fetch logic, stop.

**Acceptance criteria.**
- A capped live re-run's "robots" section shows a real disposition line, not page
  output.
- The printed checklist boxes match the run (a zero-doc run shows them unchecked).
- Golden E2E byte-identical; all tests green.

**Done when** re-running the harvest produces evidence that would fail honestly if
the underlying behavior failed.

---

## Step 4 · T6 — Promote clippy + fmt to a real CI gate, and reconcile STATE 🤖

**Objective.** Make "clippy-clean" a gate instead of a report, and fix the
`STATE.md` claim that says it already is when the shipped tree is not.

**The discrepancy to fix.** `STATE.md` (v0.7.4) lists `items_after_test_module`
among clippy lints "fixed structurally (… test module moved last)". It is not: in
`crates/store/src/sqlite.rs` the vector layer (`row_to_document`, the embeddings
`impl SqliteStore`, `vec_to_blob` / `blob_to_vec` / `cosine`, ~lines 749–895)
sits **after** `#[cfg(test)] mod tests` (536–747), which is exactly what trips the
lint six times. The block was almost certainly appended when embeddings were
added, silently undoing the fix — the `--features net` pattern in miniature.

**Steps.**
1. Move the vector-layer block to **before** `#[cfg(test)] mod tests` in
   `sqlite.rs`. Pure relocation, zero behavior change.
2. Resolve any other clippy findings from B0's inventory **except** the
   deliberately-`#![allow]`'d `unnecessary_map_or` (its fix `Option::is_none_or`
   is 1.82+ and would raise the offline floor above 1.78 — keep the allow).
3. Confirm `cargo clippy --workspace --locked --all-targets -- -D warnings` is
   clean and `cargo fmt --all -- --check` passes.
4. Flip the `lint` job in `.github/workflows/ci.yml` from
   `continue-on-error: true` to `false`.
5. **Correct `STATE.md`** so the clippy paragraph matches reality, and update
   `TASKS-v0.8.md` T6's stale wording ("deliberately commented out" — it is
   actually a report-only job now).

**Gate (from `TASKS-v0.8.md` T6).** Land the lint **fix** and the lint **gate** in
**separate commits**. A formatting diff and a behavior change must never share a
commit. If clippy still reports anything you cannot resolve without raising the
MSRV floor, **stop** and record it — do not enable the gate red.

**Acceptance criteria.**
- `items_after_test_module` no longer fires; clippy clean under `-D warnings` on
  1.91 (modulo the recorded `unnecessary_map_or` allow).
- `fmt --check` clean.
- The `lint` job is blocking; two commits (fix, then gate).
- Golden E2E byte-identical; all tests green.
- `STATE.md` and `TASKS-v0.8.md` no longer claim anything the tree contradicts.

**Done when** clippy can no longer drift unnoticed, and the docs match the code.

---

## Step 5 · T1 — Enforce HC1 on `/v1/ask` structurally, not by prompt 🤖
*(the highest-priority item in the project, and fully doable without egress — it
is string inspection; no model is needed to build or test it)*

**Objective.** Today `/v1/ask` (in `app.py`, a GET) hands the model full
`IndexOnly` bodies as context (capped by `prompts.BODY_CAP`), then returns the
model's answer **verbatim and uninspected** (`"answer": answer`). The only thing
between a gated source sentence and a public response is one line in `ASK_SYSTEM`.
A prompt is not an invariant. Make it structural, in the core.

**Where it lands, and why.** A new core endpoint `POST /attest` →
`{answer, context_doc_ids}` ⇒ `{clean_answer, violations[]}`. In the **core**,
because the shell is the rewritable layer and an invariant a rewrite can delete is
not an invariant. The core already holds the gated bodies in SQLite, so it needs
nothing new. **The core still never calls an LLM (HC3)** — it inspects a string it
is handed.

**Mechanism.** Normalized token n-gram overlap: shingle the answer and every
`IndexOnly` context body; a shared n-gram is a violation. Then redact the span or
refuse the answer — pick one and make it structural. The shell calls `/attest`
after `chat.chat` and returns `clean_answer`.

**Decision gate — `n` must be MEASURED, not chosen.** Sweep `n` over the real
corpus: for each `n`, the false-positive rate on answers known clean and the
true-positive rate on answers seeded with verbatim source sentences. **If no `n`
gives clean separation, stop** — a check with a false-positive rate that trains
operators to disable it is worse than none. Report the curve either way.
(Anticipate `n ≈ 8`; do not assume it.)

**Steps.**
1. Add `POST /attest` to `cored` and the shingle/overlap check in a core crate.
2. Add a `--leak` mode to `tools/mock_openai.py` that deliberately reproduces a
   verbatim sentence from the context it was given. *(A guard tested only against
   a double that cannot violate it is not tested — `AGENTS.md §0`.)*
3. Wire the shell: `/v1/ask` calls `/attest` and returns the cleaned answer.
4. Run the `n`-sweep on the real corpus; record the curve; pick `n`.

**Acceptance criteria (all from `TASKS-v0.8.md` T1).**
- Core unit test: an answer containing an `IndexOnly` sentence ⇒ violation.
- Core unit test: an answer containing a `CcBy` sentence ⇒ **no** violation (the
  gate is about license, not quoting).
- Core unit test: a legitimate analytical answer passes through unmangled.
- Shell test: `/v1/ask` with the **leaking** mock ⇒ the public response does
  **not** contain the gated text.
- Golden E2E: `/v1/ask` output unchanged on the existing question (4 citations,
  one near-dup suppressed) — the analytical answer must survive attestation.
- The `n`-sweep curve is recorded in `STATE.md`.

**Done when** a model that *tries* to leak gated text cannot get it through the
public API, the leaking mock proves it, and that test runs in CI. **HC1 flips
from "violated in principle" to structurally enforced.**

---

## Step 6 · T5 — Re-gate robots on the final origin after redirects 🤖

**Objective.** Close the confirmed-live compliance gap: **both** `reqwest::Client`s
in `crates/ingest/src/net.rs` (`HttpRobotsFetcher::new` and `get_text`) set no
redirect policy, so reqwest follows up to 10 redirects to origins whose
`robots.txt` was never read. RFC 9309 scopes policy per-origin. Worked around for
arXiv (canonical host, no redirect); must be fixed before any *other*
cross-origin-redirecting source goes live.

**Design — pick 1 deliberately (from `TASKS-v0.8.md` T5).**
1. `.redirect(Policy::none())` and follow redirects **manually**, re-running the
   robots gate on each hop. Explicit, more code, no surprises. **This is the
   honest one.**
2. Keep automatic redirects, compare final vs requested origin, re-gate and
   discard the body if the new origin disallows. Simpler, but it has already made
   a request the new origin's policy might forbid — the thing this subsystem
   exists to avoid.

Use Design 1 unless you record a specific reason not to.

**Gate.** The fixture path must still issue **zero** fetches (HC13 / "a fixture
read is not a request"). If your redirect handling causes a fixture-backed source
to touch the network, stop.

**Acceptance criteria (from `TASKS-v0.8.md` T5).**
- A fake fetcher that 302s cross-origin ⇒ the second origin's `robots.txt` is
  fetched and honored.
- A same-origin redirect does **not** trigger a redundant fetch.
- The fixture path issues zero fetches.
- **Both** clients in `net.rs` carry the redirect policy (not just one).
- Golden E2E byte-identical; all tests green.

**Done when** a cross-origin redirect can no longer fetch documents under an
unread policy, proven by the fake-fetcher test.

---

## Step 7 · T3 — Persist the SimHash fingerprint 🤖

**Objective.** `dedup_near` recomputes `simhash(title+body)` for every document on
every call — measured at **85%** of dedup cost at n = 10k (the quadratic scan
everyone assumed was the problem is 14.6%). Store the fingerprint as a column at
ingest; have `dedup_near` **take** fingerprints rather than compute them.

**Entering-state correction (measured 2026-07-20).** The claim below was false:
the 2026-07-20 archive did **not** lack the fingerprint column. Direct SQLite
measurement found 1,764 documents, the `simhash` column present, 0 NULL
fingerprints, and 0 NULL canonical ids. The required migration was therefore
verified on a disposable copy of those exact 1,764 rows after removing only the
copy's column; `data/core.db` remained untouched.

**Decision gate — the output must not move, at all.** Same fingerprints ⇒ same
drops ⇒ same canonical ids. If the golden E2E changes by one document, one
`kept_id`, or one hamming distance, **stop**: a faster dedup that changes which
document is canonical is corpus corruption, not an optimization. (Same gate that
killed LSH.)

**Acceptance criteria (from `TASKS-v0.8.md` T3).**
- Golden E2E **byte-identical**.
- A test that a stored fingerprint equals a freshly computed one.
- A migration that backfills a disposable pre-column copy of all 1,764
  `data/core.db` rows, verified against a fresh compute over those same rows.

**Done when** fingerprints are persisted, dedup consumes them, and nothing about
the output moved.

---

## Step 8 · T4 — Point the LLM at a real endpoint 🧑
*(deferred on endpoint configuration/key — requires operator input)*

**Gate result (2026-07-20): DEFERRED, not passed.** DeepSeek and OpenAI are now
reachable (both unauthenticated `/v1/models` probes returned 401), correcting the
prior 403 egress result. But `LLM_BASE_URL` and `LLM_API_KEY` are unset, no local
model listener exists on 8000/8899/11434, and `./run verify-llm` exits 2 asking
for configuration. The real-endpoint checklist and HC1 spot-check were not run;
the mock was not substituted. See `STATE.md §8` and `PROGRESS-v0.8.md`.

**Objective.** Carried from v0.7/T3. `tools/verify_llm.py` runs the whole
checklist in one command: embeddings backfill, fusion no longer BM25-only,
`retrieval.notes` clean.

**Human input required.** A reachable OpenAI-compatible endpoint **and** a key.
v0.7 verified `api.deepseek.com` and `api.openai.com` both 403 at the egress proxy
and no local vLLM exists.

**Gate.** No reachable endpoint and no key ⇒ **defer**; do not declare it done
against the mock. If the operator provides `LLM_BASE_URL` (+ `LLM_API_KEY`), run
`./run verify-llm` and proceed.

**This pairs with T1.** Once both are done, run the HC1 spot-check for real: ask a
question whose best evidence is an `IndexOnly` document and confirm the public
answer never reproduces gated text — with a model that *could* have. T1 builds the
guard; T4 supplies the first thing able to trip it.

**Acceptance criteria.** `verify_llm.py` green against the real endpoint; the live
HC1 spot-check passes with `/attest` active.

**Done when** the shell runs against a real model and the HC1 guard is proven
against one — or, if no endpoint is available, the deferral is recorded with the
gate cited.

---

## Step 9 · T7 — Robots cache single-flight 🤖
*(gated; expected outcome: skip)*

**Gate result (2026-07-20): SKIPPED/DEFERRED.** The configured five jobs run
synchronously through one scheduler loop; the supported systemd deployment is a
single `Type=oneshot` `scheduler --once` process. Scheduler tests passed 8/8 and
no active `data/core.db` holder was observed. The second-concurrent-writer trigger
has not fired, so no single-flight lock or speculative concurrency test was
added. See `STATE.md §8` and `PROGRESS-v0.8.md`.

**Objective.** Two simultaneous first-requests to the same origin can both fetch
`/robots.txt`. Bounded and harmless today (the limiter still spaces them).

**Gate (from `TASKS-v0.8.md` T7).** Same trigger as Postgres: if there is still
exactly one writer, **skip it and say so.** Do not add a single-flight lock to a
system with no concurrency.

**Acceptance criteria.** Either a single-flight implementation *with* a test that
concurrent misses fetch once — **or** a recorded decision that the concurrency
trigger has not fired, so it is deferred.

**Done when** the decision is made and recorded, in whichever direction the
trigger dictates.

---

## Deferred beyond v0.8 (gates that keep them out)

- **Multi-host seam (UDS / mTLS).** One host today; `CORE_TOKEN` exists on both
  sides. No speculative mTLS.
- **Postgres / pgvector / tantivy.** Postgres is a *concurrency* trigger, not a
  size one; pgvector wins only above ~10⁵ docs. See `docs/T8-scale-design-note.md`.
- **Materialize `/view`.** Precondition is measurable warm-up cost; the golden
  corpus is 12 documents. (The live archive is larger — if `/view` warm-up on the
  live DB becomes measurable, revisit *then*, with the number.)

---

## Progress checklist

- [x] **B0** — entering state verified, baseline numbers recorded
- [x] **T2** — atomic resume proven across a process restart by two capped live arXiv runs
- [x] **H1** — harness evidence hardened (real robots line, honest checklist)
- [x] **T6** — clippy/fmt a blocking gate; STATE reconciled
- [x] **T1** — HC1 structural on `/v1/ask` via `/attest` + leaking mock
- [x] **T5** — robots re-gated on the final origin after redirects
- [x] **T3** — SimHash persisted/consumed; migration verified on a pre-column copy of the live archive
- [x] **T4 — DEFERRED** — providers reachable, but no endpoint configuration/key; real checks not run
- [x] **T7 — DEFERRED** — single-flight skipped; supported scheduler remains one synchronous writer
