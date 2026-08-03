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

### 2026-08-03 · ACTIVATE — runbook-qualification correction

- owner: Codex
- runbook: `TASKS-v0.37-EXECUTION.md`
- commit: 5884ef7754431ffe5017dc1f2fde5902aef2ed52
- result: CORRECTION. The earlier entry's repository-relative `runbook` value
  is not the basename-qualified form consumed by `checklist-audit`; this
  append-only correction supplies the exact qualifier without changing the
  earlier measurement or implementation identity.
- checklist acceptance: PASS when evaluated with this correction; ACTIVATE
  resolves to the real activation commit.
- golden-E2E delta: **0**, unchanged at **11/11**.

### 2026-08-03 · PUBLISH — exact DR7 publication with one control bound deferred

- owner: Codex
- runbook: `TASKS-v0.37-EXECUTION.md`
- commit: 9474e92a05d78295e0c2dd096195608f35fc1f2b
- result: **PASS for the irreversible publication outcome; EXPLICITLY
  DEFERRED for the refuted historical multi-release checker claim.** Record
  commit `17ef4ec` contains the published State/header update and fresh
  governed observations; the named implementation commit forward-records the
  measured entry-point bound without changing any remote fact.
- DR7 preconditions: PASS immediately before push. Remote `main` was exact
  `f02379f03ccdfd1b019413234f2ad014d169fb04`; both release tags were absent;
  the ancestor check exited 0; local annotated objects
  `16ee7bcb2214859156edbceeb5e314ac1a67f39b` and
  `0fe42d7a6a86e94bb95a93a86b7a4b09917b97f4` peeled to the granted closing
  commits.
- publication acceptance: PASS. A non-force branch push moved only `main` to
  `e068cacc76685791c54ab47c84be6abbd592271d`; the subsequent non-force push
  created only v0.17.2 and v0.17.3. Fresh `ls-remote` resolved all direct and
  peeled refs to the five granted objects. Nothing was deleted or forced.
- hosted acceptance: PASS. Push-triggered run **30824053490**, attempt **1**,
  on exact `e068cacc76685791c54ab47c84be6abbd592271d` concluded success and all
  **9** blocking job identities passed.
- record acceptance: PASS. Both exact five-field post-push records are at
  column zero; the two earlier absence observations remain untouched. The
  current header says published and the v0.17.3 publication-epoch count resets
  to zero.
- lifecycle acceptance: PASS for newest v0.17.3 and **REFUTED as stated for
  both releases**. Direct `cycle-check` passes and reports
  `release=v0.17.3`. Entry-point audit proves `newest_closed_release()` returns
  only that release, so the same run never reads v0.17.2's older record. Fresh
  remote/object measurements independently match v0.17.2, but calling that a
  two-release executable result would be false. The affected historical
  reconciliation control is explicitly deferred under §2; no published claim
  was found false.
- planted-control acceptance: PASS unmodified at **14/14 rules / 81
  controls**. The required/fresh post-push, unpublished-observation precedence,
  and published-missing-record mutants still fail at their control sites.
- artifact acceptance: PASS. Schema v2 validates **2 artifacts / 332 pinned
  files**; consecutive complete checks matched the State archive and both
  databases in **0.10 s / 0.09 s real**.
- progress acceptance: PASS at the executable point. `progress-check` accepted
  the prior ACTIVATE record before this append.
- stop conditions: one author-side acceptance basis was refuted as described;
  no DR7 precondition, hosted run, published-record truth, entitlement,
  licensing, protected byte, dependency, payload, or boundary stop fired.
- golden-E2E delta: **0**. The permission-complete final PUBLISH worktree
  passed **11/11**; the initial sandbox-denied bind was a non-result.
