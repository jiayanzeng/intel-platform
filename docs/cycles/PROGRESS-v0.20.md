# PROGRESS-v0.20.md — append-only execution record

This file records v0.20 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-29 · ACTIVATE — v0.20 admitted

- owner: Codex
- commit: 2a9e1c8
- result: PASS for cycle activation only; E0 remains unchecked. Before
  activation, local `main` was the intentionally unpushed forward publication
  audit `72b6f425114e06b1e148e0aa360e280a690e4f0c`, one commit ahead of
  measured `origin/main`
  `692069ead0b8823d6874d8f2fc0a593d9f26704f`.
- worktree acceptance: PASS. The only pre-activation worktree item was the
  operator-supplied untracked `TASKS-v0.20-EXECUTION.md`; implementation commit
  `2a9e1c8` contains only that runbook, the `AGENTS.md` v0.20 declaration, and
  this new append-only progress-log skeleton.
- lifecycle acceptance: PASS. After the implementation commit,
  `./run cycle-check` reports active v0.20 open with seventeen closed execution
  runbooks. `./run checklist-audit` resolves the entering **158/158** checked
  tasks, reports the same three retractions, and finds zero exemptions.
  `git diff --check` passed.
- G1 activation observation: `cycle-check` passes locally only because the
  measured `origin/main` has not moved from the literal value asserted in the
  current `STATE.md` header. This is evidence for E0's fixed-point gate, not
  evidence that the publication-freshness rule is satisfiable.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and G1–G5 measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.
