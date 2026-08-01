# PROGRESS-v0.32.md — append-only execution record

This file records v0.32 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-08-01 · ACTIVATE — v0.32 preparatory cycle activation

- owner: Codex
- commit: 9ecc8c1
- result: PASS for the runbook-defined preparatory activation. The sole
  pre-activation worktree item was the operator-supplied untracked
  `docs/cycles/TASKS-v0.32-EXECUTION.md`; tracked and staged diffs were empty.
  The implementation commit contains only that runbook, the `AGENTS.md`
  declaration moving the active cycle to v0.32, this progress skeleton, and
  the required `repomix.config.json` retention edit.
- entering-ref acceptance: PASS. Before activation, HEAD was the v0.31
  post-push audit commit `9625fb1f7a7af2e85bad8418480b5b89093b707b`,
  whose immediate parent was closing commit
  `f02379f03ccdfd1b019413234f2ad014d169fb04`. The local remote-tracking
  `origin/main` and peeled v0.17.1 tag both resolved to that closing commit;
  annotated tag object `14912f134e45277e2b4fd10b7f5bf8b4900ca20d`
  had Git type `tag`; local `main` remained
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. The activation commit was two
  commits ahead of and zero behind remote-tracking `origin/main`. No
  publication ref moved, and no mutable `origin/main` hash was added to
  `STATE.md`'s header.
- retention rejection acceptance: PASS after making the new paths visible to
  the Git-derived reader by staging them. Before the retention edit, the real
  checker emitted exactly:
  `cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.32 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9]}{.md,.*.md,-*.md}' to agree with the tracked retained-cycle set; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-8]}{.md,.*.md,-*.md}']`.
  This matched the predicted line byte-for-byte. An earlier invocation while
  the runbook was still untracked stopped at `cannot derive 3-cycle retention
  set ending at v0.32`; it did not examine the stale-pattern construction and
  is `not measured`, not a prediction mismatch. The implementation then changed
  only the final retained range.
- lifecycle acceptance: EXPECTED PENDING at the preparatory checkpoint. After
  the activation commit, `cycle-check` rejected exactly the four
  trigger-bearing `ARCHITECTURE.md` rows because they still named v0.31. The
  activation section explicitly assigns their measured v0.32 rewrite to E0;
  no other lifecycle defect was reported. Before this entry existed,
  `progress-check` was not interpreted as an acceptance result because the
  progress skeleton contained no task event.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the clean
  rebuild, the complete 20-job matrix, both constrained Python populations,
  both protected-artifact timing runs, and the activation-tree export.
- golden-E2E delta: NOT MEASURED; E0 owns the first post-activation golden
  measurement.
- publisher/ref acceptance: PASS. Activation used only repository and local
  Git inspection. It issued no publisher request, ran no scheduler, and
  created, moved, or deleted no publication ref.
