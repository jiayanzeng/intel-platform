# PROGRESS-v0.25.md — append-only execution record

This file records v0.25 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-30 · ACTIVATE — v0.25 admitted with a valid live contract

- owner: Codex
- commit: 822aa54
- result: PASS. Before the activation commit, the supplied runbook's declared
  scope was translated from its non-executable YAML draft into the required
  Markdown table, and the manifest-retention remeasurement was assigned to
  Step 1. No task objective, gate, acceptance criterion, or permission changed.
- worktree acceptance: PASS. Before activation the only worktree item was the
  operator-supplied untracked
  `docs/cycles/TASKS-v0.25-EXECUTION.md`. Implementation commit `822aa54`
  contains only that runbook, the `AGENTS.md` v0.25 declaration, and this
  progress-log skeleton.
- entering-ref acceptance: PASS with one entering-hypothesis correction.
  Before activation, HEAD was post-push audit
  `947822c8ff85d256f20a38f1f91f5eb85326af7c` on branch
  `codex/v0.23-action-migration`, not on local `main`; local `main` remained
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. Read-only remote inspection
  resolved `main` and peeled `v0.15.8` to closing commit
  `64002678672a601804e5f67886c73fffb4d212c8`, with annotated tag object
  `dc5abe0690e77cef671896102382427721d97321`. No ref changed.
- lifecycle acceptance: PASS. `cycle-check` reports active v0.25 open with
  twenty-two closed execution runbooks and three historical runbooks.
  `checklist-audit` passes **191 checked / 3 retracted / 191 matched / 0
  exemptions**. `progress-check` correctly reported that the new skeleton had
  no dated entry before this audit record existed.
- scope acceptance: PASS. The activation commit is the scope anchor, so its
  `activation..HEAD` diff is empty. The static release-intent rule accepts the
  complete declared release-authority set.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and drafted-gate measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.
