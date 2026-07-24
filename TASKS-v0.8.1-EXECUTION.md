# TASKS-v0.8.1-EXECUTION.md — repair-and-close runbook for Codex

This cycle **closes v0.8**. It adds no features. Every step here either makes an
already-claimed property executable, removes a way the project can lie to itself,
or unblocks the one capability (T4) still open.

Task ids continue the v0.8 series; new ids (`G`, `P`, `E`, `R`, `C`) are chosen so
nothing is renumbered. `TASKS-v0.8-EXECUTION.md` stays closed and unedited —
correct it only if B0.1 finds one of its claims false.

**Entering state (asserted, not yet verified).** `main` clean at `6d42a75`;
90 workspace Rust tests, 20 net-path tests, 84 shell tests; clippy/fmt clean;
Rust 1.78 MSRV check green; all twelve v0.8 steps dispositioned; T4 and T7
deferred at their gates. `data/core.db` = 1,764 docs, SHA-256 `db2f186e…1a37a0`.
`data/live-smoke.db` = 2,600 docs (the T2 two-run interruption-resume proof).
**Treat all of the above as a hypothesis until Step 1 measures it.**

**How to run this file.** Top to bottom, one step at a time. Obey `AGENTS.md §5`
after every one: check the gate → implement → run every acceptance criterion and
capture output → run the golden E2E → update `STATE.md` with what you *measured* →
append `PROGRESS-v0.8.md` → tick the box here → commit (one step, one commit).

- **🤖 = Codex executes and self-verifies end to end.** Do not ask the operator to
  run anything marked 🤖.
- **🧑 = exactly one human input is required, named inline.** Everything else in
  that task is still yours.

**Global definition of done.** Golden E2E unchanged unless a step declares
otherwise; 0 rustc warnings on `--workspace` **and** `--features net`; clippy and
fmt clean; all Rust and shell tests green; MSRV floor still 1.78; `STATE.md`
updated with measurements, not intentions.

**A note on why this cycle exists.** v0.8 was executed well: gates held, mock
evidence was never promoted, the T2 repair found the deeper split-write bug rather
than the visible one, and a false clippy claim was caught and corrected at B0.
What v0.8 did *not* do is turn its own central invariant into something a machine
checks. Five of the nine steps below are the project's own §0 rule
(*a claimed property that nothing executes is not a property*) turned on the
project's own regression discipline.

---

## Step 1 · B0.1 — Verify the entering state, and register the protected artifacts 🤖

**Objective.** The cycle-start ritual. Re-measure rather than believe the header
above — including the parts of it that came from your own last report.

**Gate.** If any entering-state claim is false, **record the correction first**
and do not proceed until `STATE.md` reflects reality.

**Steps.**
1. `git log --oneline -5`, `git status --porcelain`; confirm the commit and a
   clean worktree.
2. Full matrix per `AGENTS.md §4`: workspace check/test, net check/test, shell
   pytest, clippy, fmt, locked 1.78 check. Record every count.
3. `./run down`; confirm 8787 / 8788 / 8899 are clear (`lsof -nP -iTCP:<port> -sTCP:LISTEN`).
4. Measure **both** live databases — row count, `PRAGMA integrity_check`, byte
   size, mtime, SHA-256, and the `cursors` row:
   - `data/core.db` (the 1,764-doc protected archive)
   - `data/live-smoke.db` (the 2,600-doc T2 evidence corpus)
5. Run the golden E2E as currently defined (prose, `AGENTS.md §6`) and record
   every number. **Record also how you ran it** — which commands, in which order.
   Step 2 turns that transcript into code, so it must be written down verbatim.

**Acceptance criteria.** Every entering-state number confirmed or corrected in
`STATE.md`. Both DB hashes recorded. The golden E2E procedure written down as an
explicit command sequence.

**Done when** `STATE.md` contains a measured, dated B0.1 block and the golden
procedure is captured in full.

---

## Step 2 · G1 — Make the golden E2E executable 🤖

**This is the highest-value step in the cycle. Do not reorder it.**

**Objective.** `AGENTS.md §6` calls the golden pipeline "the regression anchor"
and every task in v0.8 reported it "unchanged". But nothing in this repository
asserts it. `./run demo` **prints** `documents_analyzed` and the signal scores and
exits 0 regardless of their values; it does not run the second acme re-ingest, the
quant-desk entitlement check, or the `/v1/ask` citation/suppression check at all.
`shell/tests/test_shell.py` contains the golden numbers only as hard-coded *mock
responses* — it asserts nothing about a real pipeline and must not be mistaken for
coverage. So the anchor is currently a human reading printed output against a
paragraph of prose, re-implemented from memory by each agent that runs it.

That is the same failure class as the decorative HC13 checklist that H1 already
fixed, applied to the invariant this project cites most often.

**Gate.** If, while writing the assertions, the real pipeline disagrees with any
number in `AGENTS.md §6`, **stop.** Do not adjust the assertion to match the
observation. Record the divergence — it means either the prose or the corpus has
drifted, and which one is a finding, not a formality.

**Steps.**
1. Add `./run golden`. It must own its own lifecycle: build, fresh `mktemp -d`
   database, start `cored` + mock LLM, run the whole sequence, tear down, `trap`
   on EXIT. It must never touch `data/`.
2. Assert **every** value in `AGENTS.md §6`, each as its own named check with a
   pass/fail line, exiting non-zero on any failure:
   - initial fixture ingest `fetched=13, new=13`
   - `documents_analyzed == 12`
   - near-duplicate: `techwire::tw-004` dropped, `osdaily::osd-004` kept, hamming `12`
   - DeepSeek signal `RISING`, `z == 10.0`, corroborated by 3 sources
   - second acme ingest adds `0`
   - quant-desk sees exactly `1` document
   - `/v1/ask` (acme, mock chat) returns `4` citations with `techwire::tw-004` suppressed
   - all `IndexOnly` search hits return `snippet: null`
   - bad key ⇒ `401`; entitlement-disjoint search: acme 6 hits vs quant 0 for "deepseek"
3. **Failure-capable control (required — `AGENTS.md §0`).** Prove each assertion
   can fail before trusting any of them. Perturb one fixture body so the hamming
   distance moves, run `./run golden`, capture the non-zero exit and the exact
   failing check. Restore the fixture and confirm green. A harness that has never
   failed is not a harness.
4. Rewrite `AGENTS.md §6` to say the golden result is defined by `./run golden`
   and that the prose is a summary of it, not the source of truth. Keep the
   numbers in the prose for humans; add a line stating which artifact wins.
5. Add a `golden` job to `.github/workflows/ci.yml` that runs `./run golden`,
   blocking on push and PR.
6. Replace the per-task golden ritual in `AGENTS.md §5.5` with `./run golden`, so
   no future agent re-implements it by hand.

**Acceptance criteria.** `./run golden` exits 0 on the current tree and prints a
named result per check · the perturbation control exits non-zero and names the
right check · CI job present and blocking · `AGENTS.md §6` updated · full matrix
green · `data/core.db` and `data/live-smoke.db` byte-identical to Step 1.

**Done when** any future agent can establish "the golden E2E is unchanged" with
one command whose exit code means it.

---

## Step 3 · P1 — Stop the harvest from overwriting its own evidence 🤖

**Objective.** `harvest_db_path()` resolves a bare `./run harvest-arxiv` to
`data/live-smoke.db`. That file now holds the 2,600-document two-run corpus that
**is** the T2 interruption-resume proof. The next bare harvest appends to it and
mutates its hash — destroying the evidence for the one live-path claim this
project fought hardest for. This is the `data/core.db` contamination of 2026-07-20
repeated one level up: the isolation target became the thing that needs isolating.

**Gate.** None; this is a straightforward correction. But do **not** delete,
rename, or "clean" `data/live-smoke.db` as part of it. Its current bytes are the
artifact.

**Steps.**
1. Change the bare-harvest default to a fresh, non-colliding path per run —
   e.g. `data/live-<UTC-timestamp>.db`. Print the resolved path prominently
   before the first request. Explicit `CORE_DB=` still wins, unchanged.
2. Add a protected-artifact list (`data/protected.txt` or equivalent) naming
   `data/core.db` and `data/live-smoke.db` with their recorded SHA-256s from
   Step 1. Make `./run` refuse to open any listed file for a live harvest, and
   print the recorded hash and the exact override incantation when it refuses.
3. Add `./run verify-artifacts`: re-hash every protected file and report
   match/mismatch. Wire it into `./run test` so drift is *reported* on every run.
4. Failure-capable control: point a harvest at a protected path and confirm it
   refuses; corrupt a byte in a scratch copy and confirm `verify-artifacts`
   reports the mismatch.
5. Update `AGENTS.md §7` and `README.md` with the new default and the protected
   list.

**Acceptance criteria.** Bare harvest resolves to a fresh timestamped DB ·
protected paths refused with a legible message · `verify-artifacts` detects a
planted mismatch · both protected DBs unchanged at the end of the step ·
`./run golden` unchanged · full matrix green.

**Done when** no default command can silently rewrite a recorded piece of
evidence.

---

## Step 4 · E1 — Close the embedding model-key and dimension hole 🤖

**Objective.** There is a silent-corruption path in the vector leg, and it sits
directly in T4's path.

Measured from the source:

- `embeddings` is keyed `PRIMARY KEY (doc_id, model)`. `dim` is stored but never
  read back or validated.
- `docs_missing_embeddings(model)` is a `LEFT JOIN … WHERE e.doc_id IS NULL` —
  presence only. A row embedded by a *different provider at a different
  dimension* under the same model name reports **not missing**.
- `cosine(a, b)` returns `0.0` when `a.len() != b.len()` instead of erroring.
- `_model_from_env` falls back to the literal string `"default"`, and
  `.env.example` leaves `LLM_EMBED_MODEL` commented out. `./run demo` points the
  embed client at the 32-dimension mock without setting a model name — so the
  mock's vectors land under the key `"default"` too.

Composed: run the demo, then point a real 1024-dimension provider at the same DB
without setting `LLM_EMBED_MODEL`, and every document reports embedded, every
cosine scores 0.0, `retrieval.notes` stays **clean** (notes only fire when no
vector is supplied at all), and the vector leg silently returns noise. That is
graceful degradation that lies, which this architecture explicitly forbids.

And it reaches the verifier: `backfill_ok = len(still) < len(missing) or not
missing`. When `missing == []` the embed call is skipped entirely and the check
returns **PASS with zero real embedding requests**. T4's own headline criterion
can pass without touching a provider.

**Gate.** If making the dimension check strict moves the golden E2E, stop and
record — the mock's 32-dimension vectors are part of the golden path and a
behavior change there is a real finding, not a detail.

**Steps.**
1. **Core.** In `upsert_embeddings`, reject a vector whose dimension differs from
   the existing dimension recorded for that `model`, with a structured error
   naming both dimensions and the model. Do not silently overwrite.
2. **Core.** Make the dimension mismatch in `vector_search` *visible*: either
   filter mismatched rows and emit a `notes` entry counting them, or refuse.
   Returning `0.0` from `cosine` with no diagnostic is the behavior to remove.
   Whichever you choose, the note must appear in `/retrieve` diagnostics.
3. **Core.** Make `docs_missing_embeddings` dimension-aware, or add
   `GET /embeddings/stats?model=` reporting `{count, dim}` so a mismatch is
   queryable before a backfill rather than after.
4. **Shell.** Give the mock a reserved model name (e.g. `mock-embed-32`) and set
   it explicitly in `cmd_demo`, so mock vectors can never collide with a real
   provider's key.
5. **Shell.** Refuse to start `verify-llm` when `LLM_EMBED_MODEL` is unset and the
   resolved embedding endpoint is not loopback — exit 2 with the reason. An
   unnamed embedding model against a real provider is a configuration bug.
   Uncomment and require `LLM_EMBED_MODEL` in `.env.example`.
6. **Verifier.** Change the backfill criterion to: **at least one real embedding
   request was issued** *and* **`still == 0`**. `missing == []` on entry is a
   FAIL for a freshly-ingested fixture DB, not a pass.
7. **Failure-capable controls (all three).** Store 32-dim under a model, then
   attempt 1024-dim — prove the upsert is refused. Plant a mismatched row and
   prove the retrieval note appears. Run the verifier against a pre-embedded DB
   and prove the backfill check now FAILs where it previously passed.

**Acceptance criteria.** All three controls fail before the fix and pass after ·
`/retrieve` surfaces a dimension note · verifier cannot report a green backfill
without a real call · `./run golden` unchanged · full matrix green · HC3 intact
(the core still only stores and compares vectors; it calls nothing).

**Done when** a provider or dimension change is a loud error rather than a silent
ranking failure.

---

## Step 5 · T4L — Bring embeddings in-house before renting them 🧑

**One human input: start a second model server on the LAN box and report the
port. Everything else is yours.**

**Objective.** T4 has been deferred through three external providers — LAN 501,
DeepSeek 404, DMXAPI 503 — and the current plan is to find a fourth. That makes
closing this project depend on someone else's uptime. Before renting another
endpoint, test the hypothesis that the capability is already on the operator's own
hardware.

**The diagnosis.** `POST /v1/embeddings` returning **501 Not Implemented** from a
server on port 8080 reporting model name `default` is the exact signature of
`llama-server` started **without** `--embeddings`. Its error body is literally
*"This server does not support embeddings. Start it with `--embeddings`"*, and it
is returned as 501. That is a launch-flag condition, not a missing capability.
(Known wrinkle: on builds after b5630 the `LLAMA_ARG_EMBEDDINGS` environment
variable stopped taking effect for some users — pass the **CLI flag**, not the
env var.)

**Steps.**
1. **Confirm the diagnosis before acting.** From the operator's box:
   ```
   curl -sS -o /dev/stderr -w '\n%{http_code}\n' \
     http://192.168.0.192:8080/v1/embeddings \
     -H 'content-type: application/json' \
     -d '{"model":"default","input":["probe"]}'
   ```
   Read the **body**, not just the status. If it names `--embeddings`, the
   hypothesis is confirmed. If it says something else, record what it actually
   said and re-plan — do not proceed on a guess.
2. **🧑 Operator input.** Start a *second* `llama-server` instance with a
   dedicated embedding GGUF on a distinct port — do not repurpose the chat
   instance, and do not add `--embeddings` to the chat server (mixing roles gives
   poor vectors and, on current builds, conflicts with `--reranking`):
   ```
   llama-server -m <embedding-model>.gguf --embeddings \
     --host 0.0.0.0 --port 8081 -c 2048
   ```
   Any well-supported embedding GGUF is fine (bge-m3, nomic-embed-text-v1.5,
   Qwen3-Embedding-0.6B). Report the port and the model name back.
3. Configure the split roles explicitly — chat unchanged, embeddings local:
   ```
   LLM_EMBED_BASE_URL=http://192.168.0.192:8081/v1
   LLM_EMBED_MODEL=<the model name the server reports>
   LLM_EMBED_TIMEOUT_SECONDS=30
   ```
   Verify with `./run config` (keys redacted).
4. Probe once, directly, and record the **measured dimension** of the returned
   vector. Write it into `STATE.md`. Step 4's guard now depends on it.
5. **HC13 — what fixtures cannot test here, stated explicitly.** The mock returns
   32-dimension vectors instantly for any input. A real embedding server can:
   truncate or reject inputs longer than its context window (the verifier sends
   **full document bodies**, not abstracts); cap batch size below the verifier's
   16; return `data` out of order or short; stall under load. None of these are
   reachable from a fixture. Record which of them you actually observed, and note
   the ones you did not as untested.

**Gate.** If the second server also fails to serve embeddings, **stop and record
the measured status and body.** Do not fall back to the mock, do not mark T4
passed, and do not go shopping for a fifth provider inside this step — that is a
separate decision for the operator.

**Acceptance criteria.** The 501 diagnosis confirmed or refuted with a captured
body · a reachable embedding endpoint with a recorded model name and measured
dimension, **or** a recorded failure with its body · `./run config` shows the
split roles · DMXAPI's 503 evidence preserved in `STATE.md`, not deleted.

**Done when** the embedding role resolves to a provider under the operator's own
control, or the attempt is recorded as a measured failure with its exact response.

---

## Step 6 · T4P — Build the positive control T4 has always been for 🤖

**Objective.** The runbook states T4's purpose plainly: *"T1 builds the guard;
T4 supplies the first thing able to trip it."* That has still not happened.

The one partial real-model leg (T4W run 1) recorded: 4 citations, all 4 documents
`IndexOnly`, no 16-token overlap in the answer. Every one of those observations is
**also** what you would see if `/attest` were deleted and the model simply chose
to paraphrase. A negative observation from a compliant model is not evidence that
a guard works. The existing overlap tests use doubles — good, and required — but a
double proves the wiring, not that a real model can be made to trip it.

**Gate.** If the real model refuses the adversarial prompt outright — some models
will decline to reproduce a passage verbatim — that is **not** a pass and **not**
a failure of the guard. Record it as "guard not exercised: model declined", and
say so plainly in `STATE.md`. Do not soften the prompt until it produces a leak.

**Steps.**
1. Add an adversarial leg to `tools/verify_llm.py`, after the existing HC1 check:
   - pick an `IndexOnly` document known to be in the retrieved context;
   - ask the real chat model, through the real public `/v1/ask` path, a question
     engineered so that a verbatim ≥16-token span is the natural answer (quote
     the opening sentence, transcribe the passage exactly, and so on);
   - assert the response equals the core's `ATTEST_REFUSAL` constant.
2. Surface the evidence. `/attest` already returns `violations`; `/v1/ask`
   currently discards it. Have the verifier call `/attest` **directly** with the
   raw model output and the same context ids, and report
   `violations: [doc_id, …]` — so the record shows the guard *fired*, not merely
   that nothing leaked.
3. Report a three-way outcome, never a binary: `GUARD FIRED` (violation detected,
   refusal returned) · `NOT EXERCISED` (model declined or paraphrased) ·
   `LEAK` (overlap present in the returned answer — a HC1 emergency, exit non-zero
   and stop the run).
4. Keep the independent Python `_has_gated_overlap` oracle. It is deliberately a
   second implementation of the core rule and can catch a core bug; add a comment
   saying so, so a future agent does not "de-duplicate" it into the core.
5. Failure-capable control: feed the leg a canned answer containing a real
   16-token `IndexOnly` span and confirm `LEAK` is reported and the run exits
   non-zero.

**Acceptance criteria.** Adversarial leg present and exercised against the real
model · outcome recorded as one of the three states with the `violations` payload
· `LEAK` control fires · `./run golden` unchanged · full matrix green.

**Done when** `STATE.md` can say whether HC1's guard has ever been tripped by a
real model — in whichever direction the measurement went.

---

## Step 7 · T4 — Close it, in one uninterrupted run 🤖

**Objective.** Everything T4 needed is now in place. Run the whole checklist once,
end to end, and either close it or record precisely where it stopped.

**Gate.** Every required check must pass **in the same run**. A green check from
an earlier run does not carry forward. If any stage fails, record the measurement
and stop — the fail-fast behavior T4H built is the intended outcome, not a
regression to work around.

**Steps.**
1. `./run down`; confirm 8787 / 8788 / 8899 clear. `./run verify-artifacts`.
2. `./run config` — capture the resolved non-secret roles.
3. `./run verify-llm` — one run, no interruption.
4. Required in that single run: real embedding backfill to **0 missing** with at
   least one real request (Step 4) · `retrieval.notes` clean · hybrid context
   returned · real `/v1/ask` succeeds · `IndexOnly` document present in context ·
   the adversarial leg reports `GUARD FIRED` or `NOT EXERCISED`, never `LEAK`.
5. Record chat and embedding model names, measured dimension, and per-stage
   latency in `STATE.md`.
6. `./run golden`; `./run verify-artifacts`; full matrix; then commit the T4
   closure **alone**.

**Acceptance criteria.** All required checks green in one run, with model names
and latencies recorded · protected artifacts unchanged · golden unchanged.

**Done when** T4 is checked with real-model evidence, or deferred again with the
exact stage and response body that stopped it.

---

## Step 8 · R1 — Resolve the version drift and make it self-checking 🧑

**One human input: the release decision in (a). Everything else is yours.**

**Objective.** The cycle is called v0.8. `apps/cored/Cargo.toml` says `0.7.4`,
`shell/intel_shell/__init__.py` says `0.7.4`, the FastAPI app reports `0.7.4`,
and `STATE.md`'s header says v0.7.4. You were right not to bump these silently.
But the ambiguity is now load-bearing: a running binary cannot tell an operator
which cycle's code it is.

**Steps.**
1. **🧑 Operator decision**, one of:
   - **(a) Cycle name only.** v0.8 names an execution cycle; artifact versions
     track releases and stay at 0.7.4. Add one sentence to `ARCHITECTURE.md`
     stating the two numbering schemes and their relationship.
   - **(b) Cut v0.8.0.** Bump all three version strings, add `CHANGELOG.md`
     covering v0.8 (T1/T2/T3/T5/T6 done; T4/T7 deferred with their gates), tag
     the commit.
   *Recommendation: (b).* v0.8 changed harvest durability, HC1 enforcement, and
   fingerprint persistence. That is a release, and leaving it unnamed makes the
   evidence log harder to read a year from now.
2. **Either way**, add `./run version-check`: assert the Rust package version, the
   Python `__version__`, and the FastAPI `version=` string are identical, and that
   `STATE.md`'s header matches. Exit non-zero otherwise. Wire it into `./run test`
   and CI.
   Three hand-maintained copies of one string, reconciled by eye, is another
   claimed property nothing executes.
3. Failure-capable control: change one of the three, confirm `version-check`
   fails and names which file disagrees. Restore.

**Acceptance criteria.** Decision recorded in `STATE.md` with its rationale ·
`version-check` present, wired in, and proven to fail on a planted mismatch ·
if (b): all three strings bumped, changelog present, tag created · golden
unchanged · full matrix green.

**Done when** the version a running binary reports is unambiguous and machine-checked.

---

## Step 9 · C1 — Make CI cover the interpreter that actually breaks 🤖

**Objective.** v0.7.3 shipped because `./run` used Python 3.12-only f-string
syntax that crashed on the on-site 3.11. CI's `shell` job still runs **3.12 only**.
The exact class of bug that already reached the operator once is still unguarded —
found by a human, on the third try, on a live box.

Related: `bash -n run` checks syntax only. The 29-minute poll hang was a `set -e`
subshell control-flow bug, which `bash -n` cannot see and `shellcheck` can.

**Steps.**
1. Add a Python version matrix to the CI `shell` job: `["3.11", "3.12"]`.
2. Add a CI step that byte-compiles the harness under the floor interpreter
   (`python3.11 -m py_compile` over `tools/` and `shell/`), so a 3.12-only
   construct in a *script* — not just a module — fails CI.
3. Add `shellcheck ./run` as a CI step. Fix what it finds, or `# shellcheck
   disable=` each finding with a one-line reason. Do not blanket-disable.
4. State the floor: add one line to `AGENTS.md §4` recording Python 3.11 as the
   supported minimum, matching the on-site box.
5. Failure-capable control: plant a 3.12-only construct, confirm the 3.11 job
   fails, remove it.

**Acceptance criteria.** Both Python versions green in CI · planted 3.12-only
construct fails the 3.11 job · shellcheck step present and clean (or documented
disables) · Python floor recorded · golden unchanged · full matrix green.

**Done when** the on-site interpreter is exercised by CI rather than by the
operator.

---

## Step 10 · Draft `TASKS-v0.9-EXECUTION.md` 🤖

**Objective.** Only after Steps 1–9. Open with a fresh B0 entering-state
verification and measurable decision gates, per house pattern.

**Explicitly keep deferred, each with its unchanged trigger:**

| Item | Trigger that has not fired |
|---|---|
| T7 robots single-flight | a second concurrent harvester |
| Postgres | a second writer |
| pgvector | corpus scale beyond SQLite's comfort, measured |
| Multi-host seam hardening (UDS/mTLS) | an actual host split |
| `/view` materialization | measured warm-up cost crossing a defined SLO |

`/view` is the only one with a cheap, honest next move that is *not*
implementation: benchmark cold/warm `/view` latency against a **disposable copy**
of the 1,764-row archive, define the SLO, and record the number. Measuring is not
implementing, and it converts "we'll know when it matters" into a threshold.

**Do not** open v0.9 with new ingestion sources or new product surface while
`live-smoke` evidence handling, provider configuration, and release numbering are
still settling.

---

## Cycle checklist

- [x] **B0.1** — entering state re-measured; both protected DB hashes recorded; golden procedure captured verbatim
- [x] **G1** — `./run golden` asserts every documented number; perturbation control fails correctly; CI job blocking
- [x] **P1** — bare harvest cannot overwrite `live-smoke.db`; protected-artifact list + `verify-artifacts`
- [x] **E1** — embedding dimension/model-key collision closed in core, shell, and verifier; three controls proven
- [x] **T4L** — 501 diagnosis confirmed; dedicated LAN embedding model measured at 768 dimensions; split roles configured
- [x] **T4P** — real Gemma adversarial leg reported NOT EXERCISED with no violations; GUARD FIRED and LEAK controls preserved
- [x] **T4** — closed in one uninterrupted real-model run: 6/6 required checks; models, dimension, and stage latencies recorded
- [x] **R1** — release decision recorded; `version-check` wired in and proven to fail on mismatch
- [x] **C1** — CI runs Python 3.11 and 3.12; shellcheck on `run`; floor recorded
- [ ] **v0.9** — runbook drafted; deferred items kept deferred with their triggers

---

## Standing prohibitions for this cycle

- Do **not** touch `Cargo.lock` to resolve anything (HC12). Do not hand-edit its format.
- Do **not** raise the offline MSRV floor above 1.78. If a fix requires 1.82+
  (`Option::is_none_or`), keep the existing `#[allow]` and say why.
- Do **not** move license gating, sector filtering, or `/attest` out of the core
  (HC1, HC2). Do not let the core call a model (HC3).
- Do **not** globally flip the robots policy or re-enable automatic redirects.
- Do **not** delete or rewrite `data/core.db` or `data/live-smoke.db`.
- Do **not** promote mock evidence to real-model evidence, in either direction.
- Do **not** batch status updates. `AGENTS.md §5`, every step, no exceptions.
- If a gate trips: record the measurement and stop. A gate you silence is worse
  than a task you skip.

---

## Provenance of this runbook

Written against the `repomix` pack of the tree at `6d42a75` and the Codex session
transcript through 2026-07-24. Nothing in it was executed — no build, no test, no
network call was made while writing it. Every claim about the source above is a
**read** of that pack, and reads go stale:

- The `./run demo` non-assertion, the `harvest_db_path` default, the
  `cosine`/`dim`/`docs_missing_embeddings` behavior, the `backfill_ok` expression,
  the CI Python version, and the three version strings were each read directly
  from the packed source and are quoted from it.
- The entering-state test counts, commit hash, and DB hashes are **Codex's
  reported measurements**, not mine. Step 1 exists to re-measure them.
- The llama.cpp `--embeddings` diagnosis is a **hypothesis with a decisive test**
  (Step 5.1), inferred from the 501 status, the port, and the reported model name.
  Confirm it against the response body before acting on it.

Treat this document the way `AGENTS.md §0` says to treat `STATE.md`: as a claim
until something executes it.
