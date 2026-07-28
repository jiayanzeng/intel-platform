# PROGRESS-v0.15.md — append-only execution record

This file records v0.15 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-28 · E0-GATE — v0.15 admitted

- owner: Codex
- commit: 31916e01098ae9b68d2b6af10877ad91ea6d270f
- result: PASS for cycle activation only; E0 remains unchecked. Read-only
  verification found local `main` and `origin/main` aligned (zero ahead / zero
  behind) at `a75c9cf5defa42e985811b01f9905b6ac99797fd`, described as
  `v0.14.0-3-ga75c9cf`. The only worktree entry was the operator-supplied
  untracked `TASKS-v0.15-EXECUTION.md`.
- published-tag acceptance: PASS. Annotated `v0.14.0` remains tag object
  `dddc1a52d28a1832727a8d8eb5e87fc7168511c6`, dereferencing exactly to release
  commit `4ad4c8d71075731dd87c360e8b0d3d91d80b5518`.
- activation acceptance: PASS. Implementation commit
  `31916e01098ae9b68d2b6af10877ad91ea6d270f` committed only the supplied
  runbook, the `AGENTS.md` v0.15 declaration, and the empty append-only
  progress log.
- lifecycle acceptance: PASS. `./run cycle-check` reports active v0.15 open
  with twelve closed execution runbooks. `./run checklist-audit` resolves the
  entering **121/121** checked tasks, reports the three existing retractions
  separately, and finds zero exemptions. `git diff --check` passed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the full
  entering matrix and H1–H5 reproduction.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file was
  touched.
