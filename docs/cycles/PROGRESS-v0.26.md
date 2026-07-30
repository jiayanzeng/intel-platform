# PROGRESS-v0.26.md — append-only execution record

This file records v0.26 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-30 · ACTIVATE — v0.26 admitted with its supplied scope table

- owner: Codex
- commit: a90d080e1da18e8f16549b53c542b54259d74920
- result: PASS. The supplied runbook's declared scope parsed in its original
  executable Markdown-table dialect after the activation anchor existed; no
  translation or scope correction was required.
- worktree acceptance: PASS. Before activation the only worktree item was the
  operator-supplied untracked
  `docs/cycles/TASKS-v0.26-EXECUTION.md`. Implementation commit
  `a90d080e1da18e8f16549b53c542b54259d74920` contains only that runbook, the
  `AGENTS.md` v0.26 declaration, and this progress-log skeleton. Its immediate
  parent remains the unamended v0.25 post-push audit
  `12d0601e202efe36c6a36d42254bf39f3d12744d`.
- entering-ref acceptance: PASS with one entering-hypothesis correction.
  Before activation, HEAD was post-push audit
  `12d0601e202efe36c6a36d42254bf39f3d12744d` on branch
  `codex/v0.23-action-migration`, not on local `main`; local `main` remained
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. Read-only remote inspection
  resolved `main` and the peeled v0.16.0 tag to closing commit
  `c66c2b02191e3ca3126dddc3c004b175899b414e`, with annotated tag object
  `54f8cb2f89ed53d9e0b485f6cd46924a51e41813`; historical
  `refs/heads/candidate/v0.16.0` remained
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394`. No ref changed, and
  `STATE.md`'s header was not given a mutable branch-hash assertion.
- lifecycle acceptance: PASS. `cycle-check` reports active v0.26 open with
  twenty-three closed execution runbooks and three historical runbooks.
  `checklist-audit` passes **198 checked / 3 retracted / 198 matched / 0
  exemptions**. `progress-check` correctly reported that the new skeleton had
  no dated entry before this audit record existed.
- scope acceptance: PASS. The activation commit is the scope anchor, so its
  `activation..HEAD` diff is empty. The static release-intent rule accepts the
  complete declared release-authority set.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and drafted-gate measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- publisher-request acceptance: PASS. Activation invoked repository and GitHub
  ref/lifecycle commands only; it made no request to a publisher origin.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-30 · ACTIVATE-CORRECTION — trigger-table count made current

- owner: Codex
- commit: b6806e4b714a9eb0c42619834c4ac5f56985a9a8
- result: PASS. The first clean Python 3.11 E0 shell lane executed the live
  trigger-freshness control and found that v0.26 has **13** trigger-bearing
  rows while the exact current-table test still asserted **12**.
- fail-before acceptance: PASS. The clean constrained lane collected **284**,
  passed **283**, failed the exact
  `test_current_trigger_freshness_tables_are_complete` assertion, and skipped
  **0**. The observed count was `(2, 13)` against expected `(2, 12)`; this was
  a gate finding, not a passing shell measurement.
- gate-scope acceptance: PASS. The dated runbook amendment widens E0's gate
  only for `shell/tests/test_cycle_check.py`, which the full-matrix acceptance
  criterion already exercises and declared scope already permits. No objective,
  acceptance criterion, done condition, production permission, publisher
  permission, or trigger changed.
- focused acceptance: PASS. The unchanged failure-capable entry point now
  expects `(2, 13)` and passes **1/1**.
- lifecycle acceptance: PASS. `cycle-check` accepts the amended open v0.26
  runbook and its original activation anchor.
- scope acceptance: PASS. Only the active runbook and the exact shell
  lifecycle-count test changed. No production source, manifest, dependency,
  schema, protected artifact, public surface, configured source, or ref
  changed.
- complete-matrix acceptance: NOT YET CLAIMED. E0 restarts its clean Python
  lane after this correction and owns the complete entering result.
- golden-E2E delta: NOT MEASURED; no claim.
- publisher-request acceptance: PASS. The correction ran only a local focused
  lifecycle test and `cycle-check`; no publisher request occurred.
