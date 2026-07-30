# PROGRESS-v0.29.md — append-only execution record

This file records v0.29 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-31 · ACTIVATE — v0.29 admitted after two measured draft corrections

- owner: Codex
- commit: 1cf49cf8e1574b7ac6ac1c43ca16ee8794da7e38
- corrective commit: b3228b1ed018e09693f0760a7faaa6d5df5bf788
- result: PASS after two author-side activation defects were measured and
  corrected without amending, rebasing, or squashing either commit. The draft
  repeated the reserved cycle-closing token in prose while every task remained
  unchecked, and it refreshed only the deferred governed table while all three
  trigger-bearing architecture rows still named v0.28. The first committed
  `./run cycle-check` exited 1 and named both defect classes. The dated
  amendment removes the reserved token from prose, records reviewer errors five
  and six, discloses Step 8's corrected preservation count, and remeasures the
  three architecture rows for v0.29. The exact entry point then passed with
  active v0.29 open, twenty-six closed execution runbooks, and three historical
  runbooks.
- worktree acceptance: PASS with the supplied draft accounted for. Before
  activation, the sole worktree item was the operator-supplied untracked
  `docs/cycles/TASKS-v0.29-EXECUTION.md`. Activation commit `1cf49cf…`
  contains that runbook, the `AGENTS.md` v0.29 declaration, the progress
  skeleton, and the runbook-mandated `repomix.config.json` retention edit. The
  runbook's contradictory three-file/same-activation wording is reconciled by
  its dated amendment; no other path entered the activation commit.
- entering-ref acceptance: PASS with the drafted branch relationship corrected.
  Before activation, HEAD was v0.28 audit record
  `d9ecea493d3bc254051a0fa87fafe0b244cb0d19` on
  `codex/v0.23-action-migration`, whose immediate parent was recorded v0.28
  closure `ec8eaa2ab7c8c23d5a923a08ae36ab7692b4b664`. Locally recorded
  `origin/main` and the peeled v0.17.0 tag both resolved to
  `4af2841816dd3e43fb8423153b91aa22ccb87537`; HEAD was 23 commits ahead
  and zero behind that remote-tracking ref. Local `main` remained stale at
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. No ref moved, and no mutable
  `origin/main` hash was added to `STATE.md`'s header.
- retention acceptance: PASS. Activation moved the tracked ignore glob from
  `2[0-5]` to `2[0-6]`. On corrective tree `b3228b1…`, the exact project-root
  `./run export-check` passed **99 derived / 7 required / 152 exported** at
  **2,411,393 bytes**, retaining exactly v0.27, v0.28, and v0.29 beneath the
  **3,000,000-byte** ceiling.
- lifecycle acceptance: PASS after the recorded corrections.
  `checklist-audit` passed **224 checked / 3 retracted / 224 matched / 0
  exemptions**. Before this entry existed, `progress-check` correctly exited 1
  because the new skeleton contained no dated progress entry.
- artifact acceptance: PASS at the preparatory checkpoint. Manifest validation
  reported schema 2 with **2 artifacts / 316 pinned files**; two complete
  `verify-artifacts` runs matched every pin and both protected databases at
  **0.09 s / 0.09 s real**. The manifest measured **182,780 bytes** and no
  protected or pinned byte changed.
- scope acceptance: PASS. The activation commit is the scope anchor; the
  declared no-release intent requires no release-authority path at activation.
  The compatibility correction used only the declared `ARCHITECTURE.md`
  permission plus the standing runbook path.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the clean
  rebuild, complete 20-job matrix, and both constrained Python populations.
- golden-E2E delta: NOT MEASURED; no claim.
- publisher-request acceptance: PASS. Activation used repository, local Git,
  protected-byte verification, and the operator-local export only; it made no
  request to a publisher origin and ran no scheduler.

### 2026-07-31 · ACTIVATE-AMENDMENT — scope fixture aligned to v0.29

- owner: Codex
- commit: b92902edf861e4a3a21eba509519c0b9b46b2870
- result: PASS. The first permission-complete E0 `./run ci-local` passed
  release/cycle/checklist checks, registered invariants **12/49**, evidence,
  warning-denied workspace and net Rust lanes, clippy, fmt, and locked Rust
  1.78 before the shell lane collected **303**, passed **302**, and failed the
  v0.28 exact-current-cycle assertion that release-authority/forbid overlap
  must be empty.
- correction acceptance: PASS. The active v0.29 table intentionally makes
  `shell/intel_shell/__init__.py` and `shell/intel_shell/app.py` both release
  authorities and matches both with the broad shell-source forbid; documented
  release-authority precedence is unchanged. The fixture now derives that
  overlap independently with Python's standard `fnmatchcase` over the parsed
  table and the separately enumerated release-authority paths. No expected
  overlap value is hardcoded and no production checker behavior changed.
- focused acceptance: PASS. Constrained Python 3.11 ran
  `shell/tests/test_cycle_check.py` at **50/50**, and the real
  `cycle-check` entry point passed with active v0.29 open.
- environment acceptance: PASS with one non-result recorded. The first
  sandboxed full CI attempt reached the net lane but could not bind its
  loopback wire-test server. The permission-complete rerun passed that lane and
  exposed the fixture failure above; it is the result used for the correction.
- golden-E2E delta: NOT MEASURED in this compatibility checkpoint; E0 restarts
  from this committed correction and owns the complete matrix plus standalone
  golden.
- publisher/protected acceptance: PASS. No publisher or scheduler command ran,
  and no protected or pinned file changed.
