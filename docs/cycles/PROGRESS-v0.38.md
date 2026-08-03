# PROGRESS-v0.38.md — append-only execution record

This file records v0.38 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

## Operator grants recorded before execution

The operator issued both dormant-step grants in the initiating request. The
grant text is recorded verbatim before either gated step runs:

> Please read agents.md and ARCHITECTURE.md first, then read the newly added file "docs/cycles/TASKS-v0.38-EXECUTION.md" and execute it strictly in accordance with the architectural design and constraints. Before the task begins, I will first authorize you to "publish v0.17.4" and "SEC EDGAR wire and admission."

Under the exact scopes defined by the runbook, the quoted labels activate
Grant A and Grant B; neither is generalized beyond those written bounds.

### 2026-08-04 · ACTIVATE — v0.38 cycle activation

- owner: Codex
- runbook: `TASKS-v0.38-EXECUTION.md`
- commit: e6d68c89aa1cf018c10ad289a42674350e3d7d1e
- result: PASS under the measured ordering fallback. Direct pre-activation
  `cycle-check` treated the untracked v0.38 runbook as an older open cycle and
  failed with exactly **7 unchecked boxes** plus **1 missing closing record**.
  Activation therefore precedes P1's repository record, while Grant A's exact
  remote actions remained the first milestone execution.
- author-contract correction: PASS. The supplied short deferral table omitted
  the prior trigger-bearing population and both governed artifact byte
  authorities; its non-none actions named `Step W1`, which the entry point
  cannot resolve as Step N. The committed runbook restores the derived
  carry-forward population and authorities and renames that heading to
  structurally equivalent **Step 2A**.
- declaration acceptance: PASS. Post-commit `cycle-check` resolves v0.38 from
  the declaration and reports `state=open`, with publication reconciliation,
  scope, trigger freshness, artifact boundaries, State regions, and prior
  closed cycles all accepted.
- retention acceptance: PASS. The pre-change configuration excluded through
  v0.35 and retained v0.36–v0.37. The derived v0.38 boundary excludes through
  v0.36 and the exact retained set is the v0.37–v0.38 task/progress pairs.
  Project-root `export-check` passed at **104 derived / 7 required / 158
  exported / 2,596,652 bytes / 2 retained cycles**.
- governed review-export measurement: tree=`e6d68c89aa1cf018c10ad289a42674350e3d7d1e`; bytes=`2596652`
- artifact acceptance: PASS. Two complete checks matched **2 artifacts / 333
  pinned files** in **0.11 s / 0.11 s real**; neither governed trigger fired.
- protected-input acceptance: PASS. The three historical amendment inputs
  remain untouched and untracked. No dependency, production source, protected
  byte, observation, fixture, or unauthorized ref moved during activation.
- golden-E2E delta: **0**. The first loopback-bind attempt was a sandbox-denied
  non-result; the permission-complete identical command passed **11/11**.
