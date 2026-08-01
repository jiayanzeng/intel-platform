# PROGRESS-v0.34.md — append-only execution record

This file records v0.34 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-08-02 · ACTIVATE — v0.34 preparatory cycle activation

- owner: Codex
- commit: bb4257000cd6a752e807af9f48d0fe871e20d216
- result: PASS for the runbook-defined preparatory activation. The sole
  pre-activation worktree item was the operator-supplied untracked v0.34
  runbook; tracked and staged diffs were empty. The implementation commit
  contains only that runbook, the `AGENTS.md` declaration moving the active
  cycle to v0.34, this progress skeleton, and the required
  `repomix.config.json` retention edit.
- author-contract acceptance: PASS after forward correction. The first staged
  real `cycle-check` exposed three author-side schema defects before the
  runbook's first commit: no deferred measured-observation column, no carried
  `MSRV current-restatement membership` subject, and a G5 action with no
  literal discharging `Step N`. Runbook amendment r1 records the correction;
  the checker was not weakened.
- entering-ref acceptance: PASS. Exact delivered v0.33 HEAD was audit child
  `e0ab6964f76b0a919c5214607ef141eb5b118deb`, whose immediate parent was
  closing implementation `70781081abd42ed9a49e22ed100efdb039a9b762`.
  Direct remote inspection resolved `main` and peeled `v0.17.1` to
  `f02379f03ccdfd1b019413234f2ad014d169fb04`, the tag ref to annotated
  object `14912f134e45277e2b4fd10b7f5bf8b4900ca20d` of Git type `tag`, and the
  closing commit's immediate parent to release commit
  `7a621e39a069a1ef26438e841e7bb1ca2f34165b`.
- retention rejection acceptance: PASS. Before the retention edit the staged
  real checker emitted exactly:
  `cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.34 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-1]}{.md,.*.md,-*.md}' to agree with the tracked retained-cycle set; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],30}{.md,.*.md,-*.md}']`.
  The implementation advances the retained set to v0.32–v0.34.
- delivered-tree acceptance: PASS after two environment non-results. The
  workspace invocation was not an exact-tree measurement because the closed
  v0.33 checker discovered the untracked future runbook. An isolated clone of
  exact audit child `e0ab6964f76b0a919c5214607ef141eb5b118deb` then had a
  DNS-denied dependency bootstrap, followed by an empty-venv shell rejection;
  neither is the passing result. After installing the exact constrained set,
  the same clone passed all **20/20** jobs, checklist **261 checked / 3
  retracted / 261 matched / 261 commits resolved**, registered invariants
  **12 rules / 68 controls**, warning-denied current/net/MSRV lanes, and golden
  **11/11**. Its shell lane collected **348**, passed **347**, and skipped the
  one named, reasoned `on_site` node; E0 owns clean real-workspace populations
  through `tools/test_population.py`.
- artifact acceptance: PASS. Two complete real-workspace verifications matched
  **332 pins / 2 artifacts**, the exact structural State archive, and both
  protected databases in **0.12 s / 0.10 s real**.
- delivered-export acceptance: PASS. Project-root `./run export-check` at exact
  audit child `e0ab6964f76b0a919c5214607ef141eb5b118deb` emitted
  **2,634,692 bytes / 153 files**, confirming the reviewer inference and the
  exact tree identity.
- lifecycle acceptance: EXPECTED PENDING at the preparatory checkpoint. The
  committed activation `cycle-check` rejects exactly **28** stale-cycle
  observations: four trigger-bearing Architecture rows and 24 active deferral
  rows still honestly name v0.33. E0 owns their measured v0.34 rewrite; no
  structural, scope, retention, carry-forward, boundary, or activation-anchor
  defect remains. Artifact boundaries were read directly as `STATE.md`
  **206,530 / 453,741 bytes** and manifest **192,042 / 1,048,576 bytes**.
- test acceptance: NOT RUN as a post-activation 20-job task result; E0 owns the
  complete open-task-box entry point, clean Python populations through the
  repository comparator, every G1–G6 construction, and the mandatory
  standalone golden run.
- golden-E2E delta: **0** on the exact delivered-tree complete gate; E0 owns
  the post-activation standalone measurement.
- publisher/ref acceptance: PASS. Activation used only repository, local Git,
  direct read-only remote Git inspection, and the operator-local export. It
  issued no publisher request, ran no scheduler or model-profile command, and
  created, moved, or deleted no remote ref.
