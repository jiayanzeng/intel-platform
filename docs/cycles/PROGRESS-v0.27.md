# PROGRESS-v0.27.md — append-only execution record

This file records v0.27 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-30 · ACTIVATE — v0.27 admitted with its supplied scope table

- owner: Codex
- commit: e53cc729483b161ea59ffdd7d69726c2fb47e98d
- result: PASS. The supplied runbook's declared scope parsed in its original
  executable Markdown-table dialect after the activation anchor existed; no
  translation or scope correction was required.
- worktree acceptance: PASS. Before activation the only worktree item was the
  operator-supplied untracked
  `docs/cycles/TASKS-v0.27-EXECUTION.md`. Implementation commit
  `e53cc729483b161ea59ffdd7d69726c2fb47e98d` contains only that runbook, the
  `AGENTS.md` v0.27 declaration, and this progress-log skeleton. Its immediate
  parent remains the unamended v0.26 post-push audit
  `e0d43ff45243aa6dda627563838f33b3483b6774`.
- entering-ref acceptance: PASS with the runbook's branch-name hypothesis
  corrected. Before activation, HEAD was post-push audit
  `e0d43ff45243aa6dda627563838f33b3483b6774` on branch
  `codex/v0.23-action-migration`, not on local `main`; local `main` remained
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. Read-only remote inspection
  resolved `main` and the peeled v0.16.1 tag to closing commit
  `397d100ae425d5d059cef8a8ddb2ac13cfde52f5`, with annotated tag object
  `ae593e882898b9c49d5e91e2d50b6ca1f02ac49b`; historical
  `refs/heads/candidate/v0.16.0` remained
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394`, and
  `refs/heads/codex/v0.26-evidence-1cd88ac` remained
  `1cd88acd99704cc76c866331e505db446936e469`. No ref changed, and
  `STATE.md`'s header was not given a mutable branch-hash assertion.
- lifecycle acceptance: PASS. `cycle-check` reports active v0.27 open with
  twenty-four closed execution runbooks and three historical runbooks.
  `checklist-audit` passes **208 checked / 3 retracted / 208 matched / 0
  exemptions**. `progress-check` correctly reported that the new skeleton had
  no dated entry before this audit record existed.
- scope acceptance: PASS. The activation commit is the scope anchor, so its
  `activation..HEAD` diff is empty. The static release-intent rule accepts the
  complete declared release-authority set.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and drafted-gate measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- publisher-request acceptance: PASS. Activation invoked repository and
  read-only Git remote ref commands only; it made no request to a publisher
  origin.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.
