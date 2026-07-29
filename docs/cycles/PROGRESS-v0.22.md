# PROGRESS-v0.22.md — append-only execution record

This file records v0.22 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-29 · ACTIVATE — v0.22 admitted

- owner: Codex
- commit: aa7fee3
- result: PASS for cycle activation only; E0 remains unchecked. Before
  activation, local `main` was the intentionally unpushed v0.21 closing audit
  `188055a21fd6cabf2025bb7ce609c18bf47c4519`, one commit ahead of measured
  remote `main` `b7c4b10eb506923e3ea854a32d1dc3f4c83b0eaa`.
- worktree acceptance: PASS. The only pre-activation worktree item was the
  operator-supplied untracked `docs/cycles/TASKS-v0.22-EXECUTION.md`;
  implementation commit `aa7fee3` contains only that runbook, the `AGENTS.md`
  v0.22 declaration, and this append-only progress-log skeleton.
- runbook-validity acceptance: PASS. Before the runbook's first commit, one
  provenance sentence reproduced the checker's exact cycle-closing heading
  and was rephrased without changing an objective, gate, acceptance criterion,
  or done condition. After the implementation commit, `./run cycle-check`
  reports active v0.22 open with nineteen closed execution runbooks.
- lifecycle acceptance: PASS. `./run checklist-audit` resolves the entering
  **171/171** checked tasks, reports the same three retractions, and finds zero
  exemptions. `git diff --check` passed, and the post-implementation worktree
  was clean.
- release-ref acceptance: PASS. Read-only local and remote measurements agree:
  annotated tag object `f2bfeacc1dc8207841430e3827e7babed5605b47` peels to
  release commit `b7c4b10eb506923e3ea854a32d1dc3f4c83b0eaa`; the activation
  record adds no literal `origin/main` assertion to `STATE.md`'s header.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and G1–G5 measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.
