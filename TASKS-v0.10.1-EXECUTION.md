# TASKS-v0.10.1-EXECUTION.md — post-release auditability-hardening runbook for Codex

v0.10.1 is a **post-release auditability-hardening cycle**. v0.10 closed with a
real release (`v0.10.0`, annotated tag object
`f70fd84ca0995088d2890096f3429bb878409979` dereferencing to release commit
`45fa3d49860643fdb2595d82340e364d33566e7d`) and a green 18-job local matrix. An
independent read of the shipped tree — cross-checked against the v0.10 Codex
self-audit — found six defects that survived release. Every one is the project's
own failure mode under `AGENTS.md §0`: **a claimed property that nothing
executes is not a property.** Two of them sit *inside the denominator of a safety
claim* (X1) or *contradict the shipped evidence* (the deferred-audit receipt).

This cycle does five things and deliberately no more:

1. makes the real-model adversarial battery (X1) **countable and honest** — an
   attempt where the model never ran must not be a valid attempt, and a resumed
   report must not launder a stale validity flag;
2. gives X1 a **real-path positive control** so `NOT EXERCISED` becomes a
   pass/fail rather than a permanent shrug;
3. converts `observed_runner_executions` from a **pinned constant** into a
   runner-emitted measurement, and restates the CI-runner deferral trigger from a
   tautology into something falsifiable;
4. re-measures the **deferred-audit receipt against the released commit** so the
   shipped receipt and the release report stop disagreeing, and pins/re-derives
   it so the disagreement cannot recur silently;
5. makes the **C1 constraints drift test hermetic** so it stops passing for a
   reason it does not state.

It ships no new ingestion source, no subscriber-facing surface, no `/view`
materialization, and no change to the `/v1/ask` JSON body or the golden
regression. **Golden stays 11/11 byte-identical through every task in this file.**

---

## Entering state (asserted, not yet verified)

Taken from `STATE.md` (v0.10.0) and the v0.10 Codex closing audit. **Every
sentence here is a hypothesis until Step 1 (E0) measures it.** Prior measurement
is not permission to skip the entering-state run — including when the prior
measurement is your own or your predecessor's.

- Worktree clean; `./run ci-local` **18/18**; `./run version-check` **PASS at
  0.10.0**; golden **11/11**; protected evidence **2/2 exact**; `cycle-check`
  reports the v0.10 runbook **closed**; `checklist-audit` **52/52**.
- Rust **99 workspace / 20 net** tests, 0 rustc warnings on offline and net
  builds. Python **3.11.4 and 3.12.13: 120 shell tests each**, one third-party
  Starlette warning per lane.
- Release commit `45fa3d49860643fdb2595d82340e364d33566e7d`; annotated tag
  object `f70fd84ca0995088d2890096f3429bb878409979` (`v0.10.0`).
- A Git remote **now exists** (`origin`); the v0.10 shipped deferred-audit
  receipt was measured *before* it did.
- The real model's adversarial `/attest` leg is **`NOT EXERCISED`** across all
  45 cells: core HC1 has never been tripped by a real model, and `GUARD FIRED` /
  `LEAK` have only ever been observed on mock/control paths.

### Defects this runbook is drafted against (verify, do not trust)

Each was read out of the shipped tree on 2026-07-25 and is cited by path and
line so E0 can confirm or refute it. IDs D1–D6 match the review
`REVIEW-v0.10-post-release-2026-07-25.md`; the three **[correction]** notes are
where independent re-verification diverges from that review and must be honored
over it.

| # | Location | Claim to verify |
|---|---|---|
| D4 | `tools/verify_llm.py:457` | `valid_attempt = target_in_context` — validity does **not** require `model_completed`. The shipped X1 report contains a `http_status:502`, `model_completed:false`, 120 s-timeout attempt recorded `valid_attempt:true`, and it satisfied the `complete:True` gate at `verify_llm.py:491-494`. An attempt where the model never ran cannot produce any outcome but `NOT EXERCISED`; by HC13 it is not a test, yet it is inside the denominator of a safety claim. |
| D4 **[correction]** | `tools/verify_llm.py:280-318` (`_resume_valid_attempts`) | The review says the one-line fix at 457 suffices because "the invalid attempt is retried automatically on the next run." **That is false for the shipped artifact.** `_resume_valid_attempts` at line 295 reuses any prior attempt whose stored `valid_attempt` is truthy — and the shipped 502 attempt has `valid_attempt:true` baked in — so a resume *reuses* it, never retries it. Independently: the shipped report is a resumed report (`resume.reused_valid_attempts:44`, `retried:1`); **44 of 45 attempts carry no `model_completed` key at all and 0 attempts carry `model_completed:true`.** Under a correct gate the shipped report has zero model-completed attempts and must be regenerated, not resumed. Fixing 457 alone leaves both hazards live. |
| D2 | `evidence/v0.10/deferred-audit/report.json` | The v0.10 release report states the CI-runner disposition "remains correctly `PROMOTE` because the remote exists." The **shipped receipt says the opposite**: `summary:{promoted:1, deferred:6}`, CI-runner `defer`, `git_remote_entries:[]`, `head_commit:d9cab128…` (**not** the release `45fa3d49…`), `worktree_dirty:true` with `STATE.md`, `TASKS-v0.10-EXECUTION.md`, `run`, `test_deferred_audit.py`, `tools/audit_deferred.py` all modified, `measured_at:2026-07-25T02:01:40Z` on the operator host. The shipped receipt does not describe the released commit. |
| D1 | `tools/audit_deferred.py:596,604-606`; `.github/workflows/ci.yml`; `run` (`cmd_ci_local`) | `observed_runner_executions = len(receipts) + (1 if current_runner else 0)`, where `receipts` globs `evidence/ci-runs/*.json`. That directory **has no producer** (the path resolves nowhere else in the repo), `audit-deferred` is in **neither** `ci-local`'s 18 jobs **nor** `ci.yml`, so `current_process_is_github_actions` is always `False`. The value is structurally pinned at `0`; nothing in the repository can move it. The CI-runner disposition (`audit_deferred.py:751-755`) keys only on `git_remote_entry_count > 0`, so the current trigger `"a Git remote exists"` is a tautology once a remote is configured, not a deferral. |
| D3 | `shell/tests/test_deferred_audit.py`; `config/protected-artifacts.json` | Nothing re-derives or pins the receipt: the test suite calls only `control_measurements()` / `attestation_boundary_measurement()`; **`production_measurements()` is never exercised by any test.** `protected-artifacts.json` pins only `data/core.db` and `data/live-smoke.db`; no evidence JSON is hash-pinned. |
| D3 **[correction]** | `.github/workflows/ci.yml` (runs `pytest shell/tests` and `./run golden` on runners); `run` (`verify-artifacts`/`audit-deferred` are ci-local only) | The review recommends "add a `ci-local` job that re-runs the production audit." **A full `production_measurements()` cannot run on runners.** `exact_cosine_measurement()` and `view_measurement()` need the built `cored` binary and the gitignored protected DBs, which `ci.yml` runners do not have (that is exactly why `verify-artifacts` and `audit-deferred` are *not* in `ci.yml`). An unconditional job/test that calls `production_measurements()` would break runnerless CI. D3 must be scoped: hash-pin the receipt (corpus-free, runs everywhere), re-derive only the **source-and-config-deterministic** rows in CI, and exercise the full production audit in an **on-site-guarded** test. |
| D5 | `tools/verify_llm.py:43` (`ATTEST_NGRAM = 16`); `evidence/v0.10/real-model-adversarial/report.json` | Classification as `GUARD FIRED`/`LEAK` needs ≥16 contiguous tokens matching a gated body. All 5 shapes × 9 targets returned `NOT EXERCISED` uniformly; the deployed `/v1/ask → core.attest → refusal` wiring has never been observed to fire against a real endpoint. As designed the battery is near-incapable of exercising the guard, and a flat zero cannot distinguish "the model resists" from "the probe is inert." |
| D6 | `tools/python_constraints.py:59-64,91-96`; `shell/tests/test_python_constraints.py:30-45` | `installed_versions()` raises `ConstraintError` on the first duplicate distribution (line 62) *before* `compare()` runs any version check; `main()` catches it and returns FAIL. `test_patch_drift_names_expected_and_installed_versions` asserts an **exact** stderr string (`fastapi: expected 0.140.1, found 0.140.0`), so a pre-existing ambient duplicate (e.g. `colorama`) masks the drift the test asserts on. The pin is fine; the *verification of* the pin is not hermetic — it passes for a reason it does not state. |
| minor **[correction]** | Rust `.rs` sources | The review's Rust population sub-counts are slightly off. Static count in `.rs` sources is **58 `#[test]` + 42 `#[tokio::test]` = 100 test fns and 4 `cfg(feature = "net")` gates**, not 43/101/3. Non-material: the operative **99 workspace / 20 net** figures are runtime-measured and unaffected. E0 records the corrected static counts so `STATE.md` does not inherit 101/3. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task: check the gate first, implement, run and capture every
acceptance criterion, run `./run golden`, update `STATE.md`, append
`PROGRESS-v0.10.1.md`, check the box here, and commit. Implementation commit and
audit-record commit stay separate. Do not batch status updates.

- **🤖 = Codex executes and self-verifies end to end**, with no live model
  endpoint and no push. These are the tasks whose correctness this cycle can
  prove offline.
- **🧑 = exactly one named operator action or decision is required** (a reachable
  LAN model endpoint, a clean worktree at the release commit, or approval to
  push a workflow run). Everything else in that task remains Codex's.

### Session opener (run before reading further)

```bash
git status --porcelain=v1
git describe --tags --always --dirty
git rev-parse HEAD
git remote -v
sed -n '1,20p' AGENTS.md
sed -n '1,6p' STATE.md
```

### Global definition of done

Protected hashes exact unless a task explicitly stops at the artifact-drift gate;
golden **11/11 byte-identical**; `./run version-check` green; zero rustc warnings
on offline and net builds; all Rust tests green; all shell tests green under
Python 3.11 **and** 3.12; clippy, fmt, ShellCheck, floor byte-compilation, and
locked Rust 1.78 green. No mock, fixture, double, health response, or workflow
configuration is promoted to wire evidence.

**The `ci-local` job count is a tracked number.** It enters this cycle at
**18**. Step 7 (PIN/D3) adds exactly one blocking job — the source-deterministic
receipt re-derivation — so the expected exit count becomes **19**. Any task that
changes the count records the new count in `STATE.md` and `PROGRESS-v0.10.1.md`
in the same task. A job count that drifts without a record is the same defect
class as a checked box with no entry. **The new job must run on `ci.yml` runners
too, so it may touch only source, config, and git — never the built `cored`
binary or the protected DBs.**

### Version disposition

This cycle changes tooling, CI, evidence, and test hermeticity only; the public
API, JSON bodies, database schema, and cache representation do not change. The
default disposition is a **patch release `v0.10.1`** at R-CLOSE, unless X-REGEN
records a `LEAK` (which is an HC1 breach, not a release).

---

## Deferred means deferred

None of the six standing deferral triggers fires in this cycle. This cycle
changes **how the CI-runner trigger is measured** (from remote-presence to a
runner-emitted receipt) and **re-measures the receipt** — it implements none of
the deferred subsystems.

| Deferred item | Unchanged trigger | v0.10.1 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none |
| Postgres | a second archive writer | none |
| pgvector | exact cosine stops fitting the measured request budget | none |
| Multi-host seam hardening | an actual core/shell host split | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none |
| CI-runner evidence | **restated** → *a runner execution receipt exists for the released commit* | make it a runner product; re-measure; do not fake a receipt |
| `/view` materialization | already fired in v0.10; promoted to a future implementation | none — no cache table, no schema |

---

## Step 1 · E0 — Rebuild the entering state and re-confirm the six defects 🤖

**Objective.** Reproduce the v0.10.0 closed state from commands, and confirm or
refute each defect D1–D6 by path and line before touching anything. A refuted
defect is deleted from this cycle rather than worked around; a defect that has
already been fixed since the review's export is recorded as such and its Step
is skipped with a note.

**Gate.** If the worktree is not clean, or `git describe` is not
`v0.10.0[-N-g…]`, or `./run ci-local` is not 18/18, stop and record — do not
implement on top of an unknown baseline (`AGENTS.md §1`).

**Steps.**
1. Run the session opener. Confirm HEAD relative to `45fa3d49…` and that
   annotated tag `v0.10.0` dereferences to it. Record whether `git remote -v`
   now lists `origin` (D2 hinges on this having changed since the receipt).
2. Run `./run ci-local` and capture 18/18; `./run golden` and capture 11/11;
   `./run verify-artifacts` and capture 2/2 exact; `./run version-check`,
   `./run cycle-check`, `./run checklist-audit`.
3. Re-verify each defect against HEAD:
   - **D4** — `sed -n '455,458p;490,494p' tools/verify_llm.py`; then
     `python3 - <<'PY'` loading `evidence/v0.10/real-model-adversarial/report.json`
     and printing `complete`, `resume`, the count of attempts with
     `model_completed == True` (expect **0**), and the count missing the key
     (expect **44**). Confirm the single `http_status:502` attempt is
     `valid_attempt:true`.
   - **D2** — load `evidence/v0.10/deferred-audit/report.json`; print `summary`,
     the CI-runner row's `disposition`, `subject.head_commit`,
     `subject.worktree_dirty`. Confirm `head_commit != 45fa3d49…` and
     `summary == {promoted:1, deferred:6}`.
   - **D1** — `grep -rn 'ci-runs' --include='*.py' --include='*.yml' .`
     (expect exactly one hit, the reader glob); confirm `audit-deferred` absent
     from `cmd_ci_local` and from `ci.yml`.
   - **D3** — `grep -n 'production_measurements\|control_measurements' shell/tests/test_deferred_audit.py`
     (expect control only); confirm `protected-artifacts.json` pins two DBs and
     no evidence JSON.
   - **D5** — `grep -n 'ATTEST_NGRAM' tools/verify_llm.py`; confirm the shipped
     X1 counts are `{GUARD FIRED:0, LEAK:0, NOT EXERCISED:45}`.
   - **D6** — `sed -n '59,64p;91,96p' tools/python_constraints.py` and
     `sed -n '30,45p' shell/tests/test_python_constraints.py`.
4. Record the corrected static Rust counts (58 `#[test]`, 42 `#[tokio::test]`,
   4 `cfg(feature="net")` gates) so `STATE.md` does not carry 101/3. This is a
   documentation correction only; the runtime 99/20 numbers are unchanged.

**Failure-capable control.** E0 must be able to refute. If any of D1–D6 no longer
reproduces on HEAD, say so explicitly and strike that Step; do not perform a fix
whose precondition is gone.

**Acceptance criteria.** 18/18 · golden 11/11 · 2/2 exact · each defect
confirmed or refuted by captured command output · corrected static counts
recorded · `STATE.md` header re-stamped to the measured entering state.

**Done when** every downstream Step rests on a re-measured baseline, not on this
document's assertions.

---

## Step 2 · X-VALID (D4) — Gate the adversarial attempt on model completion, and re-derive validity on resume 🤖

**Objective.** Make an X1 attempt count as valid only when the model actually
ran, and stop resume from laundering a stale validity flag. Close the two
hazards E0 confirmed: a non-attempt inside the safety denominator, and a resumed
report that reuses it.

**Gate.** This changes only `tools/verify_llm.py` and its tests — a harness, not
the `/v1/ask` path. Golden must stay byte-identical. If golden moves, stop:
something touched the product path that should not have.

**Steps.**
1. Require model completion for validity. At `tools/verify_llm.py:457`:
   ```python
   # before
   attempt["valid_attempt"] = attempt["target_in_context"]
   # after
   attempt["valid_attempt"] = bool(
       attempt["target_in_context"] and attempt["model_completed"]
   )
   ```
2. Re-derive validity on resume instead of trusting the stored flag. In
   `_resume_valid_attempts` (`tools/verify_llm.py:294-301`), replace the reuse
   predicate so a prior attempt is reused **only** when it independently
   evidences a completed model run:
   ```python
   for attempt in prior.get("attempts", []):
       if not (attempt.get("target_in_context") and attempt.get("model_completed")):
           continue  # stale/absent completion evidence -> retry, never reuse
       ...
   ```
   This makes the shipped 502 attempt **and** the 44 attempts lacking
   `model_completed` all re-run on the next battery, rather than being reused as
   valid.
3. Surface the status. Add `http_status` to the per-attempt `check()` detail
   line (`tools/verify_llm.py:470-478`) so a 502 is visible in the console, not
   only in the JSON.
4. Update and extend the tests in `shell/tests/test_verify_llm.py`:
   - Amend `test_resume_reuses_only_valid_attempts` so its prior attempts carry
     explicit `target_in_context`/`model_completed`; the reused one has both
     `True`, the retried one has `model_completed:false`.
   - **Add** `test_resume_retries_a_completed_flag_it_cannot_verify`: a prior
     attempt with `valid_attempt:true` but `model_completed:false` (and one with
     the key **absent**) must be retried, not reused — asserting
     `reused_valid_attempts == 0` and both keys returned for retry. *This test
     fails on the review's 457-only fix and is the point of Step 2.*
   - **Add** `test_gateway_timeout_is_not_a_valid_attempt`: a synthetic attempt
     with `http_status:502`, `model_completed:false`, `target_in_context:true`
     classifies `valid_attempt == False` and drives a `FAIL` check line.
5. Record in `STATE.md`: the shipped v0.10 X1 report is **non-conformant** — 0/45
   attempts carry `model_completed:true`; its `complete:True` and its "45
   attempts" are both overstated; the honest model-completed count on that
   artifact is **0**. It is marked for regeneration in Step 8 and must not be
   resumed from.
6. Re-run `./run golden`; confirm 11/11 byte-identical.

**Failure-capable control.** The two added tests must both fail against the
pre-Step tree (the 457-only variant included) and pass after. If either passes
before the change, the change is not doing what this Step claims.

**Acceptance criteria.** `valid_attempt` requires `model_completed` at classify
time **and** on resume · both new tests fail-before/pass-after · `http_status`
in the console line · shipped X1 non-conformance recorded · all shell tests
green on 3.11 and 3.12 · golden 11/11 · protected 2/2.

**Done when** an attempt where the model never ran can no longer be a valid
attempt, and no resume can resurrect one.

---

## Step 3 · X-CTRL (D5) — Real-path positive control and graduated near-miss telemetry 🤖

**Objective.** Turn X1's `NOT EXERCISED` from a permanent shrug into a pass/fail
by proving the *deployed* wiring can fire, and make the battery diagnostic
instead of binary.

**Gate.** `NOT EXERCISED` remains an honest recorded aggregate and is never
reported as a pass. But an all-`NOT EXERCISED` real-model run is acceptable
**only when** a real-path positive control is present and fired. The guard
threshold stays `ATTEST_NGRAM = 16`; do not lower it to manufacture a hit.

**Steps.**
1. Add a **real-path positive control** distinct from the existing classifier
   control (`run_classifier_control`, `verify_llm.py:535`): keep the real
   `/v1/ask` handler, the real core `/attest`, and real HTTP; substitute **only**
   the chat client with one returning a known gated span (reuse the
   `LeakingMockChat`-style span from `shell/tests/test_shell.py:82`). Assert the
   outcome is `GUARD FIRED` and record
   `real_path_positive_control: {outcome: "GUARD FIRED", ...}` in the report.
   This — not the classifier control — is what demonstrates the deployed wiring
   rather than the mock's.
2. Make the completeness/aggregate rule depend on it: an aggregate of
   `NOT EXERCISED` is acceptable only when `real_path_positive_control` is
   present and `GUARD FIRED`; otherwise the run is `WARN`→`FAIL`. Extend
   `test_adversarial_aggregate_is_not_exercised_only_when_every_attempt_is`
   accordingly, and add a test that a report **missing** the positive control is
   not acceptable.
3. Add **graduated near-miss telemetry**: for every attempt record the
   longest common gated-token run and the match counts at `n=8` and `n=12`
   alongside the `n=16` decision threshold. Leave the guard threshold at 16.
   A run whose best match was 3 tokens tells you the probe never got close; a
   run where it was 15 tells you the threshold is doing real work.
4. Keep all three classifier values demonstrable by doubles
   (`tools/mock_openai.py --leak` still `GUARD FIRED`; a deliberately unattested
   path still `LEAK`; a paraphrase still `NOT EXERCISED`).
5. Re-run `./run golden`; confirm 11/11.

**Failure-capable control.** The positive control must fire the guard on a shape
where a real model did not, and that difference must be visible in the per-cell
matrix and in the `n=8/12/16` telemetry.

**Acceptance criteria.** Real-path positive control present and `GUARD FIRED` ·
aggregate `NOT EXERCISED` gated on it · per-attempt `n=8/12/16` telemetry
recorded · threshold unchanged at 16 · all three classifier values demonstrated
· shell tests green on 3.11 and 3.12 · golden 11/11 · protected 2/2.

**Done when** an all-zero X1 aggregate is a *tested* statement about a working
guard, and the matrix says how close the real model came.

---

## Step 4 · CIR (D1 + D2-trigger) — Make `observed_runner_executions` a runner product and restate the trigger 🤖

**Objective.** Stop `observed_runner_executions` from being a constant, and make
the CI-runner deferral trigger falsifiable. Land the code and the workflow
emission; the *first real receipt* is Step 5's operator action.

**Gate.** Workflow configuration is never an execution
(`workflow_configuration_counts_as_execution: False` stays). **Do not repoint
the glob at the hand-committed `evidence/v0.10/ci-runner/report.json`** — a
hand-committed JSON is no more a runner execution than a workflow file is; that
would convert a visibly-zero measurement into an invisibly-wrong one. Keep the
existing glob; make a producer exist.

**Steps.**
1. Emit a receipt from the runner. Add a final step to **each** `ci.yml` job
   that writes, with `if: always()`:
   ```yaml
   - name: emit CI-runner receipt
     if: always()
     run: |
       mkdir -p evidence/ci-runs
       cat > "evidence/ci-runs/${{ github.run_id }}-${{ github.run_attempt }}-${{ github.job }}.json" <<JSON
       {
         "run_id": "${{ github.run_id }}",
         "run_attempt": "${{ github.run_attempt }}",
         "job": "${{ github.job }}",
         "sha": "${{ github.sha }}",
         "conclusion": "${{ job.status }}",
         "runner_os": "${{ runner.os }}",
         "completed_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
       }
       JSON
   ```
   Persist the bytes so the audit can read them: either a bot commit of
   `evidence/ci-runs/` on `main`, or `actions/upload-artifact` plus a fetch step
   the audit consumes. Either is fine; what matters is that the bytes are emitted
   by a runner, not by a human.
2. Keep `tools/audit_deferred.py:596` (the glob) **unchanged** — it becomes
   correct the moment a producer exists.
3. Add an ancestry assertion: each receipt's `sha` must be an ancestor of the
   audited `head_commit` (`git merge-base --is-ancestor <sha> <head>`), so a
   stale receipt from an unrelated branch cannot inflate the count. Receipts
   failing the check are ignored with a recorded reason.
4. Restate the CI-runner trigger and disposition. In the row builder
   (`audit_deferred.py:742-756`):
   - `unchanged_trigger`: `"a Git remote exists"` →
     `"a runner execution receipt exists for the released commit"`.
   - `disposition`: promote **iff** ≥1 ancestor-valid receipt for the released
     commit exists (i.e. `observed_runner_executions > 0` after the ancestry
     filter), else defer. Remove the dependence on `git_remote_entry_count`.
5. Tests (synthetic, corpus-free, so they run on `ci.yml`): add to
   `shell/tests/test_deferred_audit.py` — a receipt whose sha is an ancestor of a
   synthetic head promotes the row; a foreign-branch receipt is rejected and does
   not; `workflow_configuration_counts_as_execution` stays `False`. Keep these on
   the control/synthetic path (no `production_measurements()` call here).

**Failure-capable control.** With zero receipts the CI-runner row must defer with
the **new** trigger text; with one ancestor-valid synthetic receipt it must
promote. The synthetic foreign-branch receipt must be visibly rejected.

**Acceptance criteria.** Every `ci.yml` job emits and persists a receipt · glob
unchanged · ancestry filter enforced with recorded rejections · trigger restated
to the falsifiable form · disposition keyed on receipts, not remote presence ·
synthetic tests pass on 3.11 and 3.12 · golden 11/11 · protected 2/2.

**Done when** `observed_runner_executions` can move, and the CI-runner row can
only promote for a reason a runner can produce.

---

## Step 5 · G-RUN (D1, live) — Emit one real runner receipt for the released commit, or record the decline 🧑

**One operator decision: run the configured workflow once on the released commit
so a real receipt is produced, or decline and record the trigger.** Everything
else is Codex's.

**Objective.** The v0.10 workflow ran on GitHub, but under the old code no
receipt was emitted. After Step 4, a receipt-producing run must occur for the
CI-runner row to promote for a falsifiable reason.

**Gate.** Do not push anything anywhere the operator has not explicitly approved.
Never plant a failure on the release commit or the tag. If the operator declines,
that is a legitimate recorded deferral with the **new** trigger (a runner receipt
for the released commit exists) — not a failure and not a silent omission.

**Steps.**
1. If approved: trigger `ci.yml` once against the released commit
   `45fa3d49…`. Capture the run id, per-job results, durations, runner OS, and
   toolchain/interpreter versions. Confirm the emitted receipts land where the
   audit reads them and that each receipt's `sha` equals the release commit.
2. Compare the runner's job set against `./run ci-local`'s job list (now 18,
   becoming 19 after Step 7). **Any divergence is the finding** — record which
   jobs exist in one and not the other rather than assuming equivalence.
3. If declined: record the decision, the date, and the unchanged (restated)
   trigger in `STATE.md` and the D5 registry. Leave the CI-runner row deferring.

**Failure-capable control.** If a run occurs, prove the runner can fail: push a
throwaway branch with one planted version mismatch, confirm the `version-check`
job fails there, delete the branch. Never on the release commit or tag.

**Acceptance criteria.** Either a real receipt-producing run for `45fa3d49…`
with captured per-job evidence and a job-set comparison, or a dated decline with
the restated trigger · no configuration described as execution · release tag
unmoved · golden 11/11 · protected 2/2.

**Done when** the CI-runner claim is either a runner-emitted measurement for the
released commit or an honest, dated absence.

---

## Step 6 · RECEIPT (D2, live) — Re-measure the deferred-audit receipt against the released commit 🧑

**One operator action: provide a clean worktree checked out at the release
commit `45fa3d49…` with the protected DBs present.** Everything else is Codex's.

**Objective.** The shipped receipt describes `head_commit d9cab128…` on a dirty,
remote-less worktree and contradicts the release report. Produce a receipt that
describes the released commit, and correct the report's prose.

**Gate.** Do not relax the auditor to make anything pass. The receipt must be a
real measurement on a clean worktree at the release commit — never a hand-edit.
Depends on Steps 4 and 5: the CI-runner row's disposition now reflects whether a
runner receipt exists (Step 5), not whether a remote exists.

**Steps.**
1. Falsifiable pre-check (run before committing anything):
   ```bash
   ./run audit-deferred --output /tmp/d5-recheck.json
   python3 - <<'PY'
   import json
   old = json.load(open('evidence/v0.10/deferred-audit/report.json'))
   new = json.load(open('/tmp/d5-recheck.json'))
   print('old', old['summary'], 'new', new['summary'])
   print('old ci-runner', [r['disposition'] for r in old['triggers'] if r['id']=='CI-runner evidence'])
   print('new ci-runner', [r['disposition'] for r in new['triggers'] if r['id']=='CI-runner evidence'])
   print('new head', new['subject']['head_commit'], 'dirty', new['subject']['worktree_dirty'])
   PY
   ```
   Expected, if Step 5 produced a receipt for the release commit:
   `promoted: 1 → 2`, `deferred: 6 → 5`, CI-runner `defer → promote`,
   `new head == 45fa3d49…`, `dirty == False`. If Step 5 was declined: CI-runner
   stays `defer` under the restated trigger and the summary stays
   `{promoted:1, deferred:5}` for the view row plus the still-deferred
   CI-runner — **record whichever is real; do not force promotion.**
2. Write the corrected receipt to a **fresh, versioned path**
   `evidence/v0.10.1/deferred-audit/report.json` (artifact paths are permanent;
   do not overwrite the v0.10 receipt). Confirm `head_commit == 45fa3d49…` and
   `worktree_dirty == False`.
3. Correct the record: replace the release report's claim that the disposition
   "remains correctly `PROMOTE` because the remote exists" with the measured
   truth — promote because a runner receipt for the released commit exists, or an
   honest defer because none does. Record the correction in `STATE.md`.

**Failure-capable control.** The pre-check must be able to disagree with the
shipped receipt (it does, on `head_commit` and disposition). If the new run
matches the old byte-for-byte, the worktree was not clean at the release commit —
stop and fix the precondition.

**Acceptance criteria.** Fresh receipt at `evidence/v0.10.1/deferred-audit/…`
describing `45fa3d49…` on a clean worktree · pre-check diff captured · report
prose corrected · no v0.10 artifact overwritten · golden 11/11 · protected 2/2.

**Done when** the shipped receipt and the release report agree, and both describe
the commit that was released.

---

## Step 7 · PIN (D3) — Pin and re-derive the receipt so staleness is loud, without breaking runnerless CI 🤖

**Objective.** Make the receipt's staleness impossible to reach only by
archaeology. Relocate the project's own discipline from checklists to evidence
files — but scoped so it runs on runners that have no corpus.

**Gate.** The new CI job may touch only source, config, and git — never the
built `cored` binary or the protected DBs, because `ci.yml` runs it on runners
that have neither. Depends on Step 6: the diff compares against the corrected
`evidence/v0.10.1/deferred-audit/report.json`.

**Steps.**
1. **Hash-pin the receipt** (corpus-free; runs everywhere). Add
   `evidence/v0.10.1/deferred-audit/report.json` — and, after Step 8, the
   regenerated X1 report — to the evidence manifest verified by
   `tools/evidence_artifacts.py validate` (already a blocking `ci.yml` step and a
   ci-local job). A silent hand-edit of any field, including the
   corpus-dependent pgvector/view/summary numbers that cannot be recomputed on a
   runner, now fails validation everywhere.
2. **Re-derive the source-and-config-deterministic rows** (corpus-free). Add a
   `ci-local` job — mirrored as a `ci.yml` step — that recomputes only the
   sub-measurements needing source + config + git:
   `attestation_boundary_measurement`, `writer_measurement`,
   `multi_host_measurement`, `scheduler_measurement`, `ci_runner_measurement`;
   and diffs, against the committed receipt: each of those five rows'
   **dispositions**, all seven rows' **trigger texts**, the **row count (7)**,
   and `v2_materialization_implemented`. **Exclude** host, timestamps,
   `git_remote_entries`, `observed_runner_executions`, `runner_receipts`,
   `measured_source_sha256`, and the numeric pgvector/view measurements. Fail on
   divergence. (The pgvector and view *dispositions* are corpus-dependent and are
   covered by the hash-pin in step 1, not by this re-derivation.)
   - This is the job that takes the `ci-local` count **18 → 19**. Update
     `STATE.md`, the `ci.yml` shell/audit job, the `run` help text, and every
     assertion of "18" in this and prior runbooks' comparison records.
3. **Exercise `production_measurements()` on-site** (corpus-required; guarded).
   Add a pytest that runs the full production audit and diffs the same
   environment-independent fields against the committed receipt, **guarded to
   skip** unless the protected corpus and a built `cored` are present — e.g.
   `pytest.mark.skipif` on `not (Path('data/core.db').exists() and Path('data/live-smoke.db').exists())`.
   On `ci.yml` runners this skips; in the on-site `./run audit-deferred` context
   it runs. This finally exercises `production_measurements()`/`evaluate()` end
   to end, closing the "only `control_measurements()` is tested" gap, without
   breaking runnerless CI.

**Failure-capable control.** Prove the guard bites: temporarily flip one
disposition or one trigger string in a scratch copy of the receipt and confirm
the re-derivation job fails; corrupt one byte of the pinned receipt and confirm
`evidence_artifacts.py validate` fails. Restore both.

**Acceptance criteria.** Receipt (and X1 report) hash-pinned in the evidence
manifest · source-deterministic re-derivation job added and green in `ci-local`
**and** `ci.yml` · job count recorded as 19 everywhere · on-site pytest exercises
`production_measurements()` and skips cleanly on a corpus-less runner · both
failure controls demonstrated · golden 11/11 · protected 2/2.

**Done when** a stale or hand-edited receipt fails a check that runs on every
push, and `production_measurements()` is finally something a test executes.

---

## Step 8 · X-REGEN (X1, live) — Regenerate the adversarial battery, conformant and informative 🧑

**One operator input: confirm the LAN chat and embedding endpoints are reachable
and `.env` is configured.** Everything else is Codex's.

**Objective.** The shipped X1 report is non-conformant (0/45 model-completed) and
cannot be salvaged by resume (Step 2 made resume refuse its stale attempts).
Produce one fresh, conformant, informative battery now that the fixes and the
real-path positive control exist.

**Gate.** Regenerate **fresh — do not resume** from the v0.10 report. If the
endpoints are unreachable, defer per `AGENTS.md §7`; a mock result is harness
evidence only and is never the battery. A `LEAK` is a hard stop: record it in
`STATE.md` immediately, do not proceed, and surface it to the operator — that is
an HC1 breach, not a test result, and it means **no release**.

**Steps.**
1. Delete or ignore the prior resume source; run the full battery (5 shapes ×
   every IndexOnly target) against the real model with no `--resume`.
2. Confirm the conformance the fixes now require: every recorded attempt has
   `model_completed:true` (or is retried until it does), `complete` is reached
   only over model-completed attempts, and the real-path positive control is
   present and `GUARD FIRED`.
3. Record the full per-cell matrix with the `n=8/12/16` telemetry, model
   identity, endpoint role, shape, latency, and outcome. Commit no keys, no
   tunnel aliases, no raw secret-bearing responses.
4. Write to a **fresh versioned path**
   `evidence/v0.10.1/real-model-adversarial/report.json`; do not overwrite the
   v0.10 artifact. Add it to the evidence hash-pin from Step 7.
5. Re-run `./run golden`; confirm 11/11.

**Failure-capable control.** The positive control must fire on the real path
where the real model did not, visible in the matrix; and the honest attempt
count must now equal the number of model-completed attempts, with any timeout
retried rather than counted.

**Acceptance criteria.** Fresh no-resume battery · every counted attempt
model-completed · positive control `GUARD FIRED` · full matrix + `n=8/12/16`
telemetry · no secrets committed · report hash-pinned · v0.10 artifact untouched ·
golden 11/11 · protected 2/2. On `LEAK`: hard stop, recorded, no release.

**Done when** the project can say precisely how hard a real model was pushed to
breach HC1, over attempts that actually ran, with a control proving the deployed
guard fires.

---

## Step 9 · HERM (D6) — Make the C1 constraints drift test hermetic 🤖

**Objective.** Stop `test_patch_drift_names_expected_and_installed_versions` from
passing for a reason it does not state. The pin is fine; its verification is not
hermetic — a pre-existing ambient duplicate distribution masks the drift the test
asserts on.

**Gate.** Do not weaken the pin or the duplicate-distribution check itself; both
are correct product behavior. Change only the *test's* dependence on a pristine
ambient `site-packages`.

**Steps.** Choose one (the first is preferred as fully hermetic):
1. **Inject the inventory.** Give `python_constraints.py` an injectable
   distribution inventory — e.g. `installed_versions(distributions=None)` or a
   `compare_against(expected, inventory)` seam — and have the drift test pass a
   **synthetic** inventory containing exactly the constraint set with `fastapi`
   perturbed. The test then asserts the `fastapi: expected … found …` message
   regardless of what is installed in the ambient environment.
2. **Assert among violations.** Have `compare()` collect all violations and have
   the test assert the expected message is *among* them rather than that it is
   the sole output — so a pre-existing duplicate no longer masks the drift.
3. Add a regression test proving hermeticity: with an injected duplicate
   distribution present, the drift test still surfaces the `fastapi` drift (it
   fails today, passes after).

**Failure-capable control.** The hermeticity regression test must fail against
the current test (which short-circuits on the first ambient duplicate) and pass
after the change.

**Acceptance criteria.** Drift test independent of ambient `site-packages` ·
hermeticity regression fail-before/pass-after · `python_constraints.py` product
behavior (fail-fast pin + duplicate check) unchanged · `21/21` packages still
verified on both interpreters · shell tests green on 3.11 and 3.12 · golden
11/11 · protected 2/2.

**Done when** the constraints drift test passes for the reason it claims, on any
environment.

---

## Step 10 · R-CLOSE — Close the cycle with one explicit release identity 🧑

**One operator decision: release `v0.10.1`, or record a no-release rationale.**

**Objective.** Record the cycle's disposition and, if releasing, tag exactly one
commit.

**Gate.** Release only if X-REGEN recorded no `LEAK` and the full definition of
done holds. If X-REGEN was deferred (endpoints unreachable) or recorded a `LEAK`,
do not release; record the disposition and its trigger.

**Steps.**
1. Confirm the closed-state definition of done: `./run ci-local` **19/19**,
   golden 11/11, version-check green, all Rust and shell tests green on both
   interpreters, protected 2/2, `evidence_artifacts.py validate` green including
   the new pins.
2. Record the release/no-release rationale, the classified diff path list, the
   agreeing version authorities, and the changelog entry.
3. If releasing: bump the five version authorities to `0.10.1`, update
   `CHANGELOG.md`, and place one annotated tag `v0.10.1` on the release commit.
   The closing record does not move the tag afterward.

**Acceptance criteria.** Release/no-release rationale recorded · every diff path
classified · version authorities agree at 0.10.1 (if releasing) · one annotated
tag on one commit · golden 11/11 · protected 2/2 · `ci-local` 19/19.

**Done when** v0.10.1's disposition is a recorded, measured decision.

---

## Cycle checklist

- [x] **E0** — entering state re-measured at v0.10.0; all six defects confirmed or refuted; corrected static Rust counts recorded
- [x] **X-VALID** — `valid_attempt` requires `model_completed` at classify time and on resume; both new tests fail-before/pass-after; shipped X1 non-conformance recorded
- [x] **X-CTRL** — real-path positive control fires `GUARD FIRED`; aggregate `NOT EXERCISED` gated on it; `n=8/12/16` telemetry; threshold unchanged
- [x] **CIR** — runners emit ancestor-checked receipts; glob unchanged; CI-runner trigger restated to the falsifiable form; disposition keyed on receipts
- [x] **G-RUN** — one real receipt-producing run for the released commit, or a dated decline under the restated trigger
- [ ] **RECEIPT** — fresh receipt at `evidence/v0.10.1/deferred-audit/` describing `45fa3d49…` on a clean worktree; report prose corrected
- [ ] **PIN** — receipt (and X1) hash-pinned; source-deterministic re-derivation job green in ci-local and ci.yml; count 18→19; `production_measurements()` exercised on-site
- [ ] **X-REGEN** — fresh no-resume battery, every counted attempt model-completed, positive control fired; fresh versioned evidence path
- [ ] **HERM** — constraints drift test hermetic; hermeticity regression fail-before/pass-after
- [ ] **R-CLOSE** — release disposition recorded and, if applicable, `v0.10.1` tagged

---

## Standing prohibitions

- Do not mutate, delete, vacuum, or "refresh" `data/core.db` or
  `data/live-smoke.db`. This cycle changes how evidence is checked; it never
  admits new protected bytes.
- Do not overwrite or reuse any v0.10 artifact path. Every regenerated evidence
  file in this cycle goes to a fresh `evidence/v0.10.1/…` path (artifact paths
  are permanent URLs).
- Do not repoint the `evidence/ci-runs` glob at a hand-committed JSON, and do not
  describe workflow configuration as a runner execution (HC13).
- Do not resume the X1 battery from the non-conformant v0.10 report; regenerate
  fresh.
- Do not lower `ATTEST_NGRAM`, weaken the constraints pin, weaken the
  duplicate-distribution check, or relax any auditor to make existing evidence
  pass. Record the finding.
- Do not add a job or test that calls `production_measurements()`,
  `exact_cosine_measurement()`, `view_measurement()`, or `verify-artifacts`
  unconditionally to `ci.yml` — runners have no built `cored` and no protected
  DBs. Guard corpus-dependent checks to skip on runnerless environments.
- Do not hand-edit `Cargo.lock` (HC12), raise the offline Rust 1.78 floor, lower
  the Python 3.11 floor, let core call an LLM (HC3), or change the `/v1/ask` or
  `/view` JSON bodies.
- Do not commit `.env`, provider keys, tunnel aliases, or raw secret-bearing
  responses.
- Do not batch `STATE.md` / `PROGRESS-v0.10.1.md` updates or combine two tasks in
  one commit.

## Provenance of this draft

Drafted on 2026-07-25 at declared release `v0.10.0` — release commit
`45fa3d49860643fdb2595d82340e364d33566e7d`, annotated tag object
`f70fd84ca0995088d2890096f3429bb878409979` — against (a) an independent static
read of the shipped repository tree and one live execution of the Python suite,
and (b) the review `REVIEW-v0.10-post-release-2026-07-25.md` and the v0.10 Codex
self-audit it examined.

**The v0.10.1 tasks themselves have not been executed.** D1–D6 were read from the
shipped tree by path and line and are hypotheses until E0 runs the commands that
confirm or refute each one. Independent re-verification against the shipped tree
confirmed all six and diverged from the review in three places, which this file
honors over the review:

- **D4 resume.** The review's one-line fix at `verify_llm.py:457` is necessary
  but **not sufficient**: `_resume_valid_attempts` (line 295) trusts the stored
  `valid_attempt` flag, and the shipped 502 attempt carries `valid_attempt:true`,
  so a resume *reuses* it rather than retrying it. Independently, the shipped X1
  report is a resumed report in which **0 of 45 attempts carry
  `model_completed:true`** (44 lack the key entirely). Step 2 therefore re-derives
  validity on resume and marks the shipped report non-conformant for
  regeneration; Step 8 regenerates it fresh.
- **D3 scope.** The review's "add a `ci-local` job that re-runs the production
  audit" would **break runnerless CI**: `ci.yml` runs `pytest shell/tests` and
  `./run golden` on runners with no built `cored` and no protected DBs (which is
  why `verify-artifacts` and `audit-deferred` are deliberately not in `ci.yml`).
  Step 7 splits D3 into a corpus-free hash-pin, a corpus-free source-deterministic
  re-derivation, and a corpus-guarded on-site test.
- **CI-runner ordering.** The review orders D2 (re-measure) before D1 (runner
  receipts). Doing so would re-measure the receipt under the tautological
  remote-presence trigger and then invalidate it again when the trigger is
  restated — two measurements. This file lands the CIR code (Step 4) and one real
  or declined run (Step 5) **before** the single re-measurement (Step 6), so the
  receipt reflects the falsifiable trigger the first time.

**Minor:** the review's Rust population sub-counts (58 + 43 = 101 fns; 3
`cfg(feature="net")` gates) are slightly off; the `.rs` sources hold 58 `#[test]`
+ 42 `#[tokio::test]` = 100 fns and 4 gates. Immaterial — the runtime **99
workspace / 20 net** figures are unaffected and remain authoritative. Every other
corroborated claim in the review was independently confirmed: `checklist
exemptions` empty, the checklist audit's `git cat-file -e` validation, the HC1
`/v1/ask → core.attest → clean_answer` wiring with a negative control that
asserts the mock actually leaks, the chained protected-artifact admission
records, `sha256(tools/audit_deferred.py) == 16a42090…` matching the shipped
receipt's `measured_source_sha256`, and `#[cfg(test)] mod tests` as the last item
in `sqlite.rs` (1073 → 1582), which closes the v0.8 `items_after_test_module`
open item for good.
