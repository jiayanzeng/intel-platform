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
