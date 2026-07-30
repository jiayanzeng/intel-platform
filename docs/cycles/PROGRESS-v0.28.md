# PROGRESS-v0.28.md — append-only execution record

This file records v0.28 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-30 · ACTIVATE — v0.28 admitted with one measured draft correction

- owner: Codex
- commit: c44af842d42cf350aab575ea14c22be508c54bd3
- corrective commit: 18b2c23dbc0e64b06fe9dc178c55ecd6e6256610
- result: PASS after an author-side activation defect was measured and corrected
  without amending, rebasing, or squashing either commit. The supplied draft
  included the checker's reserved cycle-closing heading while every task
  remained unchecked, both as a premature empty template and as literal prose
  inside G2. The first committed `./run cycle-check` exited 1. The dated
  runbook amendment removes the template and rephrases only the reserved token;
  the exact entry point then passed with active v0.28 open, twenty-five closed
  execution runbooks, and three historical runbooks.
- worktree acceptance: PASS with the supplied draft accounted for. Before
  activation, the only worktree item was the operator-supplied untracked
  `docs/cycles/TASKS-v0.28-EXECUTION.md`. Activation commit `c44af84…`
  contains only that runbook, the `AGENTS.md` v0.28 declaration, and this
  progress-log skeleton. The syntax correction is isolated in `18b2c23…`.
- entering-ref acceptance: PASS with the runbook's branch-name hypothesis
  corrected. Before activation, HEAD was post-push audit
  `ddf08d2063f384d6c3d6d5ddef87b65a9167625c` on branch
  `codex/v0.23-action-migration`, not local `main`. The locally recorded
  `origin/main` is its immediate ancestor (`origin/main...ddf08d2` measured
  `0 1`); local `main` remains the stale
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`, 102 commits behind
  `origin/main`. No ref changed, and no mutable branch hash was added to
  `STATE.md`'s header.
- lifecycle acceptance: PASS after the recorded syntax correction.
  `checklist-audit` passed **216 checked / 3 retracted / 216 matched / 0
  exemptions**. Before this entry existed, `progress-check` correctly exited 1
  because the new skeleton had no dated progress entry.
- scope acceptance: PASS. The activation commit is the scope anchor; the
  declared static no-release intent requires no release-authority paths, and
  the active runbook, progress record, and `STATE.md` are standing-allowed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and drafted-gate measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- publisher-request acceptance: PASS. Activation used only repository and local
  Git-object commands; it made no request to a publisher origin.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-30 · ACTIVATE-AMENDMENT — lifecycle fixtures aligned to v0.28

- owner: Codex
- commit: be5b9e1827cd4a2a870512f53b5c1baa94e9f413
- result: PASS. The first permission-complete E0 `./run ci-local` measured two
  shell failures after every preceding Rust, invariant, lifecycle, lint, MSRV,
  and net job passed: the active deferred population was `(2, 15)` while the
  v0.27 fixture expected `(2, 14)`, and v0.28's no-release scope derived zero
  release-authority/forbid overlaps while the v0.27 fixture expected
  `shell/intel_shell/app.py`.
- correction acceptance: PASS. The dated runbook amendment permits only the two
  exact-current-cycle fixture corrections. Focused
  `shell/tests/test_cycle_check.py` passed **45/45**, and `cycle-check` passed
  with v0.28 open. No checker implementation changed. Step 3 remains responsible
  for replacing the temporary exact trigger-population assertion with a derived
  expectation.
- environment acceptance: PASS with one non-result recorded. The first
  sandboxed `ci-local` attempt reached the net lane but its loopback wire server
  was denied by the execution sandbox; the permission-complete rerun passed that
  exact test and the complete net lane before reaching the two lifecycle-fixture
  failures above.
- golden-E2E delta: NOT MEASURED in this corrective checkpoint; E0 restarts and
  owns the complete matrix plus standalone golden.
- publisher-request acceptance: PASS. No publisher or scheduler command ran.
- protected artifact delta: PASS. No protected or pinned file changed.

### 2026-07-30 · E0 — entering state rebuilt and G1–G7 settled

- owner: Codex
- commit: 5d73b2936d3f94883dbc6b2d3a7fb1e84713175a
- result: PASS. Every entering hypothesis and gate answer is recorded in
  `STATE.md` and the runbook's dated E0 amendment; differences from the draft
  are corrections, not silently retained assertions.
- entering-matrix acceptance: PASS. Permission-complete `./run ci-local` passed
  all **20/20** jobs with warning-denied **145** workspace tests, **62** net
  tests, locked Rust 1.78, clean rustc/clippy/fmt/ShellCheck,
  `invariant-scan` **12 rules / 46 controls**, embedded golden, protected
  artifacts, and lifecycle checks. Standalone golden passed **11/11**.
- shell-population acceptance: PASS. Clean constrained Python 3.11.4 and
  3.12.13 lanes each collected/passed **293**, failed zero, and skipped zero.
  `tools/test_population.py` derived `collected=293`, `equivalent=true`, and
  `equivalent_passed=293`.
- artifact acceptance: PASS. Both complete verifications matched **301** pins
  and both protected databases at **0.10 s / 0.10 s real**. The manifest
  measured **174,152 bytes**, below 1 MiB.
- lifecycle/shape acceptance: PASS with drafted values corrected. The
  architecture table measured **11 data / 2 governed** rows, the active
  deferred table **15 governed** rows, and `checklist-audit` **216 checked / 3
  retracted / 216 matched / 0 exemptions**. Entering `STATE.md` measured
  **6,984 lines / 453,741 bytes** and its seven regions measured **12,540 /
  17,273 / 127,922 / 185,799 / 43,650 / 38,748 / 27,809 bytes**.
- G1 acceptance: PASS by execution. Blanking every deferred measured cell while
  retaining a dated column header made `cycle-check` exit **0**. All real
  governed rows carry their own date, so removing a real header token would
  reject zero current rows.
- G2 acceptance: PASS. v0.24–v0.27 each close on `2026-07-30`; a date-only
  discriminator distinguishes at most one cycle on that date.
- G3 acceptance: PASS by execution. The current call discarded derived counts
  and only the temporary lifecycle fixture consumed `(2, 15)`. Setting every
  trigger to `none` derived `(0, 0)` and `cycle-check` exited **0**.
- G4 acceptance: PASS. The exact project-root `./run export-check` passed **99
  derived / 7 required / 182 exported**. The retained export was **4,975,987
  bytes**, **99.52%** of decimal 5 MB with **24,013 bytes** headroom. Raw
  composition was cycle docs **34 / 1,435,284**, observations **13 / 949,344**,
  root **12 / 713,006**, state archive **1 / 297,739**, and other reviewed
  paths **122 / 1,564,264**. The 2026-07-30 external observation remains
  **2,067 chunks / 2,000 limit**. Source inspection confirmed no ceiling.
- G5 acceptance: PASS by execution. Moving closed v0.24 in a throwaway clone
  left both commands at exit **0**, while `cycle-check` closed coverage fell
  **25 → 24** and checklist checked/matched coverage fell **216 → 209**.
  `audit_deferred`'s complete-progress-glob assertion still passed.
- G6 acceptance: PASS. The unstated ordering assumption and
  `incoming.last()`-equivalent implementation are recorded with the bounded
  effect: a misordered window can misreport one diagnostic string, while the
  poll still commits and identity is unchanged.
- G7 acceptance: PASS with no implementation. The public value-domain and named
  response-shape release criteria are enumerated at their exact authorities.
  No bounded detector exists without a machine-readable historical contract;
  their honest prose-adjudicated status remains.
- deferred-table acceptance: PASS. All **15** governed rows now carry
  E0-remeasured observations containing both `v0.28` and `2026-07-30`.
- environment acceptance: PASS with non-results named. Sandboxed loopback,
  dependency-install, population-wrapper, and direct networked Repomix attempts
  were not interpreted as measurements. Their actual entry points passed under
  the required permissions; Repomix was downloaded with scripts disabled
  outside the repository and executed against repository bytes only with
  network denied after explicit operator authorization.
- golden-E2E delta: **0**; embedded and post-record standalone outcomes remain
  byte-identical at **11/11**.
- publisher/ref/protected acceptance: PASS. No publisher request, scheduler,
  model-server session, historical ref movement, protected-byte change,
  dependency change, route change, or public value-domain change occurred.
