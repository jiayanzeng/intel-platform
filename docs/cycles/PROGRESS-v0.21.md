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

### 2026-07-29 · E0 — entering state and six gates measured

- owner: Codex
- commit: 5527d23
- result: PASS. The read-only Gate contained every acceptance surface; only
  runbook status and this append-only entry moved. `STATE.md` remained blob
  `7db364ad67d27b2c0aa7cf448ef7db45e1a29ec0`.
- entering-matrix acceptance: PASS. Clean constrained Python 3.11.4 and 3.12.13
  environments each resolved **21** packages and passed shell **255/255**.
  `./run ci-local` passed **20/20** with **133** workspace tests, **55** net
  tests (**29 + 26**), locked Rust 1.78, zero
  rustc/clippy/fmt/ShellCheck failures, `invariant-scan` **11/11 rules / 23
  controls**, **191/191** pins, protected databases **2/2**, and embedded
  golden **11/11**. Standalone golden passed **11/11**. Project-root
  `export-check` passed **90/90** derived sources, **7/7** required paths, and
  **149** exported paths.
- G1 acceptance: PASS and CONFIRMED. The tag-object pattern returned `[]`; the
  tag-target pattern returned the release commit; the header's unexamined tag
  object was `7a5c9f7396c043f2b89974585fdd4e5146180e86`. A forty-zero tag-object
  assertion in the live phrasing produced zero errors.
- G2 acceptance: PASS and CONFIRMED, count **4**. The four
  zero-match-is-success publication regex rules are the `origin/main`
  prohibition, pending-publication prohibition, tag-object freshness, and
  tag-target freshness. None has a registered planted failure. Required
  checklist evidence fails when a checked box lacks an entry or commit, and
  `progress-check` fails on absent headers, owners, or commits.
- G3 acceptance: PASS as a recorded forward-correction finding. In a disposable
  full-history published clone at `v0.15.4`, `cycle-check` exited **1** with six
  missing-remote-tag messages for `v0.8.0` and `v0.10.2`;
  `checklist-audit`, `progress-check`, `version-check`, and `invariant-scan`
  each exited **0**. The tree has v0.20 R-CLOSE unchecked, no closing record,
  no R-CLOSE progress entry, and a header that still describes publication in
  progress. E0 did not repair it.
- G4 acceptance: PASS and CONFIRMED. Held commits
  `344124819cb3c554f851d0cac3f0f1ed08d1aa10` and
  `72b6f425114e06b1e148e0aa360e280a690e4f0c` were first hosted-verified
  **9:51:54** and **2:20:18** later, respectively; current closing audit
  `8fc21813763c19a90ee17e7b95d1e87330a916b8` is on no remote branch and has
  never been hosted-verified.
- G5 acceptance: PASS and CONFIRMED. The wrong-object/pending construction
  produced exactly one error. With a mismatched measured ref, early return
  reported release-object agreement and masked pending-publication.
- G6 acceptance: PASS and CONFIRMED from v0.20's record. The 240-character
  header-only proximity window was explicitly accepted as conservative bounded
  looseness because it can refuse loudly but cannot create a false pass.
- object/pin acceptance: PASS. Remote `main`, tag object, and peeled target are
  unchanged; manifest validation passed **191/191** and protected databases
  remain **2/2** exact.
- lifecycle acceptance: PASS. `cycle-check` passed after the status update; the
  expected pre-audit `checklist-audit` failure named only E0's not-yet-appended
  progress entry.
- golden-E2E delta: **0**. The post-status standalone run passed **11/11**.

### 2026-07-29 · MATCH-PROOF — publication rules made failure-capable

- owner: Codex
- commit: e260169
- result: PASS. E0 confirmed G1 and G2, and the implementation stayed within
  the declared Gate: publication checkers, their focused tests and executable
  control registry, and status records only.
- total-assertion acceptance: PASS. Both annotated-tag object and peeled-target
  assertions are required; a zero-match header is an error, and every found
  assertion must equal the measured ref. Before the header edit, the corrected
  command exited **1** with exactly `STATE.md: publication assertion required:
  status header must assert the annotated tag object in the required
  unambiguous phrasing`.
- narrow-pattern acceptance: PASS. `[^`\n]` remains unchanged. The rejected
  alternative of admitting intervening backticks would allow an unrelated hash
  to satisfy the assertion and reproduce the silent class after rephrasing.
- planted-failure acceptance: PASS. New R12 invokes the actual
  `check_publication_status` entry point over nine planted cases. Seven
  independent registry mutations disable the mutable-ref prohibition, each
  required/fresh immutable-ref family, pending-publication, missing tag ref,
  missing peeled target, and unavailable ancestry. All seven exact findings
  fired; the full command passed **12/12 registered rules / 30 controls**.
- existing-rule acceptance: PASS. The `origin/main` prohibition and pending
  rule 1 retain their conditions and error behavior. Their focused examples
  pass, and R12 detects a mutation that disables each.
- interpreter acceptance: PASS. Focused `cycle_check` plus `invariant_scan`
  tests passed **47/47** under Python 3.11.4 and independently **47/47** under
  Python 3.12.13.
- lifecycle acceptance: PASS. `cycle-check` passed after the header and status
  updates. The expected pre-audit `checklist-audit` failure named only this
  checked task's not-yet-appended progress entry. `git diff --check` passed.
- golden-E2E delta: **0**. The restricted attempt was a loopback-bind permission
  non-result; the identical permitted run passed **11/11**, and the final
  post-status invocation again passed **11/11**.
- protected artifact delta: **0**. No pin, protected database, crate, app,
  dependency, schema, robots surface, configured source, or public response
  changed.

### 2026-07-29 · PUBLISHED-HEAD — shipped tree measured, rhythm accepted

- owner: Codex
- commit: a01b6e4
- result: PASS with G3 recorded as a forward-correction subject. The Gate was
  limited to a fresh disposable clone, `STATE.md`, `AGENTS.md`, and status
  records; the published tree was not repaired or mutated.
- published-suite acceptance: PASS as a measurement. Fresh clone tag
  `v0.15.4` resolved to object
  `7a5c9f7396c043f2b89974585fdd4e5146180e86` and exact target
  `8c1eff03ff3e67b18176e8bf533de0f9501e0257`. The corrected current cycle
  checker exited **1** with the six recorded missing historical tag-ref
  messages for `v0.10.2` and `v0.8.0`, plus the newly exposed required
  tag-object-assertion message. Every exact message is preserved in the
  runbook execution record.
- remaining-suite acceptance: PASS. Current `checklist-audit` against the
  published root exited **0** with **164/164**; current `progress-check` exited
  **0** at `RE-MEASURE · 5631e70`; published `version-check` exited **0** at
  exact v0.15.4; and current `invariant-scan` against the published registry
  exited **0** with **11/11 rules / 23 controls**.
- G3 acceptance: PASS as a finding, not as a clean tree. Published v0.20 has
  R-CLOSE unchecked, no cycle closing record, no R-CLOSE progress entry, and
  a header describing publication preparation. It was not repaired here.
  Trigger: the next operator-authorized `main` publication after v0.15.4; a
  no-release close leaves the finding open until a later publication.
- G4 acceptance: **Accept**, operator decision dated 2026-07-29. `AGENTS.md`
  now records that a cycle's final append-only audit record is
  hosted-unverified when written after publication and is verified at the
  following publication. Required local gates and append-only evidence support
  it until then.
- no-push acceptance: PASS. Final remote readback left `main` and the peeled
  tag target at `8c1eff03ff3e67b18176e8bf533de0f9501e0257` and tag object at
  `7a5c9f7396c043f2b89974585fdd4e5146180e86`.
- lifecycle acceptance: PASS. Local `cycle-check`, `invariant-scan` **12/12 /
  30**, and `git diff --check` passed. The expected pre-audit
  `checklist-audit` failure named only this checked task's not-yet-appended
  progress entry.
- golden-E2E delta: **0**. Standalone golden passed **11/11**.
- protected artifact delta: **0**. No pin, protected database, crate,
  dependency, schema, robots surface, configured source, or public response
  changed.
