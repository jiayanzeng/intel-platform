# PROGRESS-v0.10.1.md — append-only execution record

This file records v0.10.1 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-26 · E0-GATE — known dirty inputs corrected before baseline restart

- owner: Codex
- commit: f56d2c40ec1a7a9b3f2bbfcf4037ed151ec469f8
- result: BLOCKED, then corrected without claiming E0 complete. The first
  session opener found the operator-supplied runbook, three modified tracked
  Finder metadata files, and one untracked Finder metadata file. E0's literal
  clean-tree gate therefore stopped before `ci-local` or downstream acceptance.
- gate evidence: `git status --porcelain=v1` named modified `.DS_Store`,
  `crates/.DS_Store`, and `shell/.DS_Store`, plus untracked
  `TASKS-v0.10.1-EXECUTION.md` and `evidence/.DS_Store`. HEAD was
  `6c53d8585d43d46723a83ba1635012b7ab00671f`, described as
  `v0.10.0-1-g6c53d85-dirty`.
- identity evidence: annotated tag object
  `f70fd84ca0995088d2890096f3429bb878409979` dereferenced exactly to release
  commit `45fa3d49860643fdb2595d82340e364d33566e7d`; `origin` was present.
- correction: added `*.DS_Store` to `.gitignore`, removed the three existing
  metadata files from Git tracking without deleting the local files, committed
  the supplied runbook, declared v0.10.1 active, created this progress log, and
  changed one quoted historical authority phrase in the now-inactive v0.10
  runbook to past tense so `cycle-check` would not mistake it for live
  authority.
- runbook review: recorded that CIR must execute the new workflow definition
  while checking out the audited release commit; RECEIPT must run the new
  auditor against an explicit clean release worktree and explicit receipt
  input; Step 6's decline summary is 1 promoted / 6 deferred; historical
  18-job measurements remain immutable when the current count later becomes 19.
- lifecycle acceptance: `./run cycle-check` passed with active v0.10.1 and
  five closed execution runbooks. `./run checklist-audit` resolved the existing
  52/52 checked tasks with zero exemptions.
- test acceptance: NOT RUN at this gate checkpoint. E0 remains unchecked and
  restarts from the clean post-audit tree.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected file was touched.
