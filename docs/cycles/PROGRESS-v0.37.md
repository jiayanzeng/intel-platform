# PROGRESS-v0.37.md — append-only execution record

This file records v0.37 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-08-03 · ACTIVATE — v0.37 cycle activation

- owner: Codex
- runbook: `docs/cycles/TASKS-v0.37-EXECUTION.md`
- commit: 5884ef7754431ffe5017dc1f2fde5902aef2ed52
- result: PASS under the runbook's explicit ordering fallback. The
  pre-activation post-push worktree check classified the untracked v0.37
  runbook as an older open cycle and failed with exactly eight unchecked boxes
  plus a missing closing record. Activation therefore precedes completion of
  PUBLISH's repository append, while PUBLISH remains the first active step.
- declaration acceptance: PASS. `cycle-check` now resolves v0.37 solely from
  the AGENTS declaration and finds no active-runbook scope, retention,
  carry-forward, governed-boundary, or publication-record defect. Its only
  post-activation findings are the four Architecture trigger rows that still
  name v0.36; PUBLISH owns their fresh v0.37 measurements.
- author-contract correction: PASS. The supplied runbook omitted the canonical
  `Deferred means deferred` heading, its required action column, 25 immediately
  prior trigger subjects, and both governed artifact byte boundaries. The
  activation commit carries every prior subject, keeps every trigger and both
  byte boundaries unchanged, and rephrases the one cross-step measured-value
  acceptance against its same-worktree authority.
- retention acceptance: PASS. With the v0.37 runbook/progress pair staged in
  the Git-derived set, the configured excluded boundary advanced exactly
  through v0.35 and the retained set was exactly the v0.36-v0.37 task/progress
  pairs. Project-root `export-check` passed at **100 derived / 7 required / 154
  exported / 2,791,496 bytes / 2 retained cycles**.
- excluded boundary: `docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-5]}{.md,.*.md,-*.md}`.
- golden-E2E delta: **0**. The first sandbox-denied loopback bind was a
  non-result; the permission-complete identical command passed **11/11**.
- protected-input acceptance: PASS. The three untracked amendment inputs
  remain untouched and untracked. No production source, dependency, protected
  byte, publisher configuration, version authority, tag, or remote ref moved
  during activation.
