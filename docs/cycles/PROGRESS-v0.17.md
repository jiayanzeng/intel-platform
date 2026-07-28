# PROGRESS-v0.17.md — append-only execution record

This file records v0.17 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-28 · ACTIVATE — v0.17 admitted

- owner: Codex
- commit: 9aa74c4
- result: PASS for cycle activation only; E0 remains unchecked. The session
  opener measured local `main` and `origin/main` aligned at
  `cdae3c922a2156701c0df0ceb4f45fc937fa7f20`.
- worktree acceptance: PASS. Before activation the only worktree change was the
  operator-supplied untracked `TASKS-v0.17-EXECUTION.md`; the activation commit
  contains only that runbook, the `AGENTS.md` v0.17 declaration, and this new
  append-only progress log.
- published-tag acceptance: PASS. Annotated `v0.15.0` remains tag object
  `b7ee3445728e1816e1622c9498ffc2f165ed5dd5`, dereferencing exactly to release
  commit `8f97205a3ed4fe82f6a5ede2febce7a5d82d9f81`.
- lifecycle acceptance: PASS. `./run cycle-check` reports active v0.17 open
  with fourteen closed execution runbooks. `./run checklist-audit` resolves the
  entering 137 checked tasks, reports the same three retractions, and finds zero
  exemptions. `git diff --check` passed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and F1–F5 measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.
