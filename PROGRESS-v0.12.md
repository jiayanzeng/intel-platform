# PROGRESS-v0.12.md — append-only execution record

This file records v0.12 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-27 · E0-GATE — dirty worktree preserved and v0.12 admitted

- owner: Codex
- commit: a81430ab8a50961d03eff019d3449405312d8280
- result: PASS for cycle activation only; E0 remains unchecked. The mandated
  opener found entering HEAD
  `916b20f8c3dabd743a0568cb14353a0c889e2ab1`, described as
  `v0.11.0-1-g916b20f-dirty`, with local `main` and `origin/main` aligned
  (zero ahead / zero behind). Annotated `v0.11.0` remained tag object
  `fcfa4825e6ffbc06c0ad73e18044965c10786aa8`, peeled to
  `6daeb7e9f2cc0022b5e1a1dcf2ce8702b5be0321`.
- dirty-state inventory: preserved without stashing, reverting, cleaning, or
  staging the operations work. Modified tracked files were `AGENTS.md`,
  `README.md`, `STATE.md`, and `run`; untracked files were this supplied
  runbook, `intel-platform-OPERATIONS.md`,
  `shell/tests/test_model_profiles.py`, and `tools/model_profiles.py`.
  The draft omitted `README.md` from its entering-state list; its diff is
  explained by the same model-profile work (command documentation,
  operations-manual link, and the nine-test count). The other tracked diffs
  contain the standing-authorization block, prior live-evidence record, and
  `./run models` dispatch; the three untracked operations files are their
  implementation, manual, and tests.
- correction: implementation commit
  `a81430ab8a50961d03eff019d3449405312d8280` committed only the supplied
  runbook, the `AGENTS.md` active-cycle header, and the empty append-only
  progress log. The pre-existing `AGENTS.md` operations hunk remained
  unstaged.
- lifecycle acceptance: PASS. `./run cycle-check` reports active v0.12 open
  with nine closed execution runbooks. `./run checklist-audit` resolves the
  entering **88/88** checked tasks with zero exemptions. `git diff --check`
  passed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the
  entering matrix and shell-count disambiguation.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file was
  touched.
