# PROGRESS-v0.33.md — append-only execution record

This file records v0.33 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-08-01 · ACTIVATE — v0.33 preparatory cycle activation

- owner: Codex
- commit: 353a17e67c3cac5699f43dd65b15725e3e35d5e1
- result: PASS for the runbook-defined preparatory activation. The sole
  pre-activation worktree item was the operator-supplied untracked r2 runbook;
  tracked and staged diffs were empty. The implementation commit contains only
  the runbook, the `AGENTS.md` declaration moving the active cycle to v0.33,
  this progress skeleton, and the required `repomix.config.json` retention
  edit.
- author-contract acceptance: PASS after forward correction. The first staged
  real `cycle-check` exposed four r2 author defects before activation: unknown
  `conditional` scope class, no measured-observation deferral column, missing
  carry-forward of `MSRV current-restatement membership`, and two action cells
  that named `Steps N–M` instead of executable `Step N` references. r3 records
  the correction at the runbook's top; the checker was not weakened. The
  manifest path is now an `allow` whose use remains prose-constrained to Step 5
  Option B and explicit operator selection.
- entering-ref acceptance: PASS. Before activation, HEAD was exact v0.32 audit
  child `70b7f93c94c67e43f6f4a29ede5823081955f3fa` and its immediate parent was
  closing implementation `86b8db0b4026c23371317c7881dcc9497806c20b`.
  Direct remote inspection—not the closing record—resolved `main` and peeled
  `v0.17.1` to `f02379f03ccdfd1b019413234f2ad014d169fb04`, resolved the
  tag ref to annotated object `14912f134e45277e2b4fd10b7f5bf8b4900ca20d`
  of Git type `tag`, and confirmed the closing commit's immediate parent is
  release commit `7a621e39a069a1ef26438e841e7bb1ca2f34165b`.
- retention rejection acceptance: PASS after staging the new paths so the
  Git-derived reader examined the construction. Before the retention edit the
  real checker emitted exactly:
  `cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.33 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],30}{.md,.*.md,-*.md}' to agree with the tracked retained-cycle set; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9]}{.md,.*.md,-*.md}']`.
  The implementation then changed only the final retained range, advancing the
  retained set to v0.31–v0.33.
- delivered-tree acceptance: PASS with two named environment non-results. An
  isolated local clone of exact delivered v0.32 HEAD cleared lifecycle,
  checklist **254 checked / 3 retracted / 254 matched / 254 commits resolved**,
  registered invariants **12 rules / 61 controls**, warning-denied Rust and net
  tests, Python, and golden **11/11**. Its first net run was not measured because
  the sandbox denied the loopback bind; the permitted rerun passed. Its
  protected-artifact lane was not measured because local-only database bytes are
  intentionally absent from a clone. In the real workspace two complete
  verifications matched **331 pins / 2 artifacts** and both protected databases
  in **0.09 s / 0.10 s real**.
- lifecycle acceptance: EXPECTED PENDING at the preparatory checkpoint. The
  committed activation `cycle-check` rejected exactly **28** stale-cycle
  observations: four trigger-bearing `ARCHITECTURE.md` rows and 24 active
  deferral rows still honestly name v0.32. E0 owns their measured v0.33 rewrite;
  no structural, scope, retention, boundary, or activation-anchor defect
  remained. Artifact boundaries were read directly as `STATE.md` **352,895 /
  453,741 bytes** and manifest **191,395 / 1,048,576 bytes**.
- test acceptance: NOT RUN as a complete 20-job workspace result at this
  preparatory checkpoint; E0 owns the post-activation full entry point, both
  local Python populations through `tools/test_population.py`, the exact
  delivered-export measurement, and every G1–G6 construction.
- golden-E2E delta: NOT MEASURED as a post-activation task result; E0 owns the
  mandatory standalone measurement.
- publisher/ref acceptance: PASS. Activation used only repository, local Git,
  and direct read-only remote Git inspection. It issued no publisher request,
  ran no scheduler or model-profile command, and created, moved, or deleted no
  publication ref.
