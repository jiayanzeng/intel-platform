# PROGRESS-v0.36.md — append-only execution record

This file records v0.36 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-08-03 · ACTIVATE — v0.36 preparatory cycle activation

- owner: Codex
- runbook: `docs/cycles/TASKS-v0.36-EXECUTION.md`
- commit: f44681c1dce0c5c2efc0d3fb4a30900fdb4163f5
- result: PASS for the runbook-defined activation after the Step 0e ordering
  exception. The pre-activation `ci-local` lifecycle lane rejected the
  v0.36-specific task path while v0.35 remained declared and treated the
  untracked v0.36 runbook as an older incomplete cycle. Activation therefore
  committed first; AUTONOMY remains a separate subsequent implementation.
- author-contract correction: PASS. The supplied runbook had no
  machine-readable declared-scope table, used a noncanonical deferred heading
  while omitting all 24 immediately prior trigger subjects, and omitted the
  governed artifact byte-boundary authority. The activation commit adds the
  required scope metadata and exact release-authority set, carries forward all
  prior subjects/triggers, retains the supplied v0.36-specific deferred rows,
  and carries the existing `453741` / `1048576` boundaries byte-identically.
- retention acceptance: PASS. With the new runbook/progress pair staged in the
  Git-derived set, the unchanged checker required
  `docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-4]}{.md,.*.md,-*.md}`
  and rejected the prior boundary through v0.33. The committed pattern retains
  exactly v0.35-v0.36 and excludes execution cycles through v0.34.
- lifecycle acceptance: EXPECTED PENDING at activation. After scope,
  retention, carry-forward, and boundary corrections, the real checker
  reported only its pre-commit activation-anchor conditions plus the required
  stale-observation population: four Architecture rows and 32 active deferral
  rows do not yet name v0.36. E0 owns their dated measurement and rewrite.
- golden-E2E delta: **0**. The sandboxed first run was a loopback-bind
  permission non-result; the permission-complete identical command passed
  **11/11**.
- protected/publisher/ref acceptance: PASS. Activation did not change a
  protected byte, production source, dependency, publisher/scheduler
  configuration, version authority, tag, or remote ref. The operator-supplied
  amendment remains untracked and untouched.
