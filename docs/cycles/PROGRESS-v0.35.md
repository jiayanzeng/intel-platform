# PROGRESS-v0.35.md — append-only execution record

This file records v0.35 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-08-02 · ACTIVATE — v0.35 preparatory cycle activation

- owner: Codex
- commit: 5d51d4106e31a4f67215c6e8e66c19488ff29a46
- result: PASS for the runbook-defined preparatory activation. The sole
  pre-activation worktree item was the operator-supplied untracked v0.35
  runbook; the tracked tree was clean. The implementation commit contains that
  runbook, the `AGENTS.md` declaration moving the active cycle to v0.35, this
  progress skeleton, and the required `repomix.config.json` retention edit.
- author-contract acceptance: PASS after forward correction. The staged real
  `cycle-check` exposed one author-side schema defect before the runbook's first
  commit: the governed artifact byte-boundary authority was absent. Runbook
  amendment r1 restores the unchanged `STATE.md` 453,741-byte and
  `config/protected-artifacts.json` 1,048,576-byte authorities. The checker,
  boundaries, and trigger texts were not changed.
- entering-ref acceptance: PASS. Delivered v0.34 HEAD
  `d8d20b81b9ea9027dada74ce047a7cd92815e9f3` has immediate parent closing
  implementation `6a19d31dd00143fc85a5e6c157dceb90ce40e946`. Direct remote
  inspection resolved `main` and peeled `v0.17.1` to
  `f02379f03ccdfd1b019413234f2ad014d169fb04`, the tag ref to annotated object
  `14912f134e45277e2b4fd10b7f5bf8b4900ca20d` of local Git type `tag`, and the
  v0.34 evidence ref to exact candidate
  `1117dc6db6ec0e55e8c8f078ca8059628f9f8262`. The published closing commit's
  immediate parent remains release commit
  `7a621e39a069a1ef26438e841e7bb1ca2f34165b`.
- retention rejection acceptance: PASS. Before the retention edit, the staged
  real checker emitted exactly:
  `cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.35 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-3]}{.md,.*.md,-*.md}' to agree with the tracked retained-cycle set; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-2]}{.md,.*.md,-*.md}']`.
  The implementation advances the retained set to v0.34-v0.35.
- lifecycle acceptance: EXPECTED PENDING at the preparatory checkpoint. After
  the activation commit, the real checker rejects exactly 28 stale-cycle
  observations: four trigger-bearing Architecture rows and 24 active deferral
  rows still honestly name v0.34. Step 1 owns their measured v0.35 rewrite;
  no structural, scope, retention, carry-forward, boundary, amendment, or
  activation-anchor defect remains. Artifact boundaries were read directly as
  `STATE.md` **243,402 / 453,741 bytes** and manifest **192,042 / 1,048,576
  bytes**.
- test acceptance: NOT RUN as a post-activation complete `ci-local` result;
  Step 1 owns the full 20-job entering gate, clean Python populations, exact
  delivered-tree export, and every G1-G7 construction.
- golden-E2E delta: **0**. The sandboxed attempt was a bind-denied environment
  non-result; the identical permission-complete standalone run passed **11/11**.
- publisher/ref acceptance: PASS. Activation used repository-local commands and
  direct read-only remote Git inspection only. It issued no publisher request,
  ran no scheduler, service, or model-profile command, and created, moved, or
  deleted no remote ref.
