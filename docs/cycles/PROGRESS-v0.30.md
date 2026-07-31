# PROGRESS-v0.30.md — append-only execution record

This file records v0.30 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-31 · ACTIVATE — v0.30 preparatory cycle activation

- owner: Codex
- commit: bea40e64849015fdfc9b471f2adb7ab3ce4fcbf7
- result: PASS for the runbook-defined preparatory activation. The sole
  pre-activation worktree item was the operator-supplied untracked
  `docs/cycles/TASKS-v0.30-EXECUTION.md`; tracked and staged diffs were empty.
  The implementation commit contains only that runbook, the `AGENTS.md`
  declaration moving the active cycle to v0.30, this progress skeleton, and
  the required `repomix.config.json` retention edit.
- entering-ref acceptance: PASS. Before activation, HEAD was v0.29 audit
  commit `d824be06582dfb76b9fe4b5d70ff33f4a505d6cc`, whose immediate parent was
  v0.29 closure commit `20ddf90bb2b1d8654b410cdafe8f67e6d006a115`.
  The local remote-tracking `origin/main` and peeled v0.17.0 tag both resolved
  to `4af2841816dd3e43fb8423153b91aa22ccb87537`; HEAD was 44 commits ahead
  and zero behind that remote-tracking ref. Local `main` remained at
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. No ref moved, and no mutable
  `origin/main` hash was added to `STATE.md`'s header.
- retention rejection acceptance: PASS. With active v0.30 present and before
  the retention edit, the real checker emitted exactly:
  `cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.30 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-7]}{.md,.*.md,-*.md}'; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-6]}{.md,.*.md,-*.md}']`.
  The implementation then changed only that final retained range.
- lifecycle acceptance: EXPECTED PENDING at the preparatory checkpoint. After
  the activation commit, `cycle-check` rejected exactly the three
  trigger-bearing `ARCHITECTURE.md` rows because they still named v0.29.
  The activation section explicitly assigns their measured v0.30 rewrite to
  E0; no other lifecycle defect was reported. Before this entry existed,
  `progress-check` correctly rejected the empty progress skeleton.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the clean
  rebuild, the complete 20-job matrix, both constrained Python populations,
  both protected-artifact timing runs, and the activation-tree export.
- golden-E2E delta: NOT MEASURED; E0 owns the first post-activation golden
  measurement.
- publisher/ref acceptance: PASS. Activation used only repository and local
  Git inspection. It issued no publisher request, ran no scheduler, and
  created, moved, or deleted no ref.
