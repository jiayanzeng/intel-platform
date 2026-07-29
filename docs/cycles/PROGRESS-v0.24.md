# PROGRESS-v0.24.md — append-only execution record

This file records v0.24 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-29 · ACTIVATE — v0.24 admitted with three validation defects

- owner: Codex
- commit: 46a44b2
- result: FAIL at the first post-commit `cycle-check`. The committed
  declared-scope block used YAML rather than the required Markdown table;
  `Manifest retention/indexing` said `re-measure only` without assigning the
  action to a named Step N; and Step 6's acceptance criterion cited the
  invariant-count increase from Step 3 instead of stating the same-commit
  relation.
- worktree acceptance: PASS. Before activation the only worktree item was the
  operator-supplied untracked
  `docs/cycles/TASKS-v0.24-EXECUTION.md`. Implementation commit `46a44b2`
  contains only that runbook, the `AGENTS.md` v0.24 declaration, and this
  progress-log skeleton.
- entering-ref acceptance: PASS. Before activation, HEAD was the unamended
  post-closing audit
  `ed54112ae69fd990bdbb0ae705e2671fb31678a4`. Read-only remote inspection
  resolved `main` and peeled `v0.15.7` to closing commit
  `e7715fb97b86b91a2a58bc7b73bf99308c2aae9b`, with annotated tag object
  `b579c2c18e4eeb549617ea20a9175b0c26dc621d`. Local `main` remained
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`; no ref changed.
- lifecycle acceptance: FAIL for `cycle-check` with the exact three defects
  above. `checklist-audit` independently passed **184 checked / 3 retracted /
  184 matched / 0 exemptions**. `progress-check` correctly reported that the
  new skeleton had no dated entry before this audit record existed.
- scope acceptance: NOT MEASURED at activation. The static sub-rule could not
  evaluate a declared scope because the committed block did not use its
  accepted schema; an exit 1 on that unparsed construction is not a successful
  firing.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and drafted-gate measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-29 · ACTIVATE-CORRECTION — live contract made valid

- owner: Codex
- commit: 6c5ca4c
- result: PASS. The active runbook carries a dated amendment and now uses the
  checker's Markdown declared-scope table, assigns manifest re-measurement to
  Step 1, and states Step 6's invariant-count acceptance as a same-candidate
  relation with the population-equivalence rule executing.
- scope acceptance: PASS. `./run cycle-check` accepts the `release` intent and
  all declared release-authority coverage. The Python forbid is
  `shell/intel_shell/[a-z]*.py`, leaving
  `shell/intel_shell/app.py` as the sole release-authority overlap described by
  the runbook.
- amendment acceptance: PASS. The machine-readable
  `Step 6 — … — 2026-07-29` disclosure matches the one changed acceptance
  block; `cycle-check` reports no undisclosed objective, acceptance, or
  done-condition edit.
- lifecycle acceptance: PASS. `cycle-check` reports active v0.24 open with
  twenty-one closed execution runbooks and three historical runbooks;
  `checklist-audit` passes **184 checked / 3 retracted / 184 matched / 0
  exemptions**; `progress-check` passes at the preceding ACTIVATE record.
- scope delta: only the active runbook changed. No source, workflow, tool,
  dependency, schema, protected artifact, public surface, or ref changed.
- golden-E2E delta: NOT MEASURED; no claim.
