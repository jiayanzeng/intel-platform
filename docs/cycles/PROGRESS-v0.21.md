# PROGRESS-v0.21.md — append-only execution record

This file records v0.21 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-29 · ACTIVATE — v0.21 admitted

- owner: Codex
- commit: df9abb9
- result: PASS for cycle activation only; E0 remains unchecked. Before
  activation, local `main` was the intentionally unpushed v0.20 closing audit
  `8fc21813763c19a90ee17e7b95d1e87330a916b8`, one commit ahead of measured
  `origin/main` `8c1eff03ff3e67b18176e8bf533de0f9501e0257`.
- worktree acceptance: PASS. The only pre-activation worktree item was the
  operator-supplied untracked `TASKS-v0.21-EXECUTION.md`; implementation commit
  `df9abb9` contains only that runbook, the `AGENTS.md` v0.21 declaration, and
  this new append-only progress-log skeleton.
- runbook-validity acceptance: PASS. Before the runbook's first commit,
  `cycle-check` rejected Step 5's cross-step measured-count reference. The
  acceptance was corrected to require the hosted candidate itself to prove
  every registered rule and declared planted-failure control. Because the
  correction preceded the first committed version, it is not a runbook
  amendment.
- lifecycle acceptance: PASS. After the implementation commit,
  `./run cycle-check` reports active v0.21 open with eighteen closed execution
  runbooks. `./run checklist-audit` resolves the entering **165/165** checked
  tasks, reports the same three retractions, and finds zero exemptions.
  `git diff --check` passed.
- release-ref acceptance: PASS. Local annotated tag object
  `7a5c9f7396c043f2b89974585fdd4e5146180e86` peels to release commit
  `8c1eff03ff3e67b18176e8bf533de0f9501e0257`; the activation record does not
  add a literal `origin/main` assertion to `STATE.md`.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and G1–G6 measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.
