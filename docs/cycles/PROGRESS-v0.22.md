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

### 2026-07-29 · E0 — entering state and drafted gates settled

- owner: Codex
- commit: ee1f4e0
- result: PASS. The complete measured record is in the E0 execution section of
  `TASKS-v0.22-EXECUTION.md`; all five drafted gates are now classified and
  Step 2 is blocked on its named operator decision.
- entering-matrix acceptance: PASS. Clean constrained Python 3.11.4 and 3.12.13
  rebuilds resolved the same 21 packages and each passed shell **258/258** with
  the same one third-party Starlette warning. `./run ci-local` passed
  **20/20**, with **133** workspace tests, **55** net tests (**29 + 26**),
  warning-denied current and locked Rust 1.78 lanes, clean
  clippy/fmt/ShellCheck, `invariant-scan` **12/12 rules / 30 controls**,
  **206/206** pins, protected databases **2/2**, and embedded golden **11/11**.
  The standalone cycle, checklist, progress, version, invariant, artifact, and
  root export checks passed; `export-check` measured 90 derived sources, 7
  required paths, and 151 exported paths.
- G1 acceptance: CONFIRMED. `newest_closed_release` requires release name,
  release commit, and annotated-tag object from the closing section. Only the
  name is knowable before the containing commit. A disposable object
  construction changed both the containing commit when its prior hash was
  inserted and the tag object when the new target was tagged; both fixed-point
  comparisons were `no`. No permutation can make either dependent object name
  itself. The separate early-close clone failed with the four exact
  unavailable-input lines preserved in the runbook record.
- G2 acceptance: both `v0.8.0` and `v0.10.2` are **LOCAL-ONLY**. Their exact
  annotated objects, targets, local refs, and release commits exist; exhaustive
  remote inspection found neither tag nor any recorded object id. No ref or
  closed runbook changed.
- G3 acceptance: REFUTED. `ARCHITECTURE.md` already states the contributor-facing
  operator-local status, command behavior, deliberate local/hosted CI omission,
  and reason. `AGENTS.md` carries the two measured operating rules.
- G4 acceptance: CONFIRMED as an unexamined default. The manifest is 119,353
  bytes/characters at 206 pins; release totals are
  **161 → 176 → 191 → 206**, exactly +15 per cycle, and the full re-hash costs
  **0.10 s real / 0.05 s user / 0.04 s sys**. Existing immutable/append-only
  policy has no dated unbounded-growth acceptance, bound, or revisit trigger.
- G5 acceptance: CONFIRMED. Both third-party warnings are repeatedly recorded
  as non-blocking but neither has a trigger or permanent-acceptance decision.
- identity/integrity acceptance: PASS. Local and remote `v0.15.5` remain exact
  at tag object `f2bfeacc1dc8207841430e3827e7babed5605b47`, peeled release
  commit `b7c4b10eb506923e3ea854a32d1dc3f4c83b0eaa`; all **206/206** pins and
  protected databases **2/2** re-verified. `STATE.md` remained blob
  `03053b14137161423a4f1bca617b8bc85d91e86b`.
- golden-E2E delta: **0**. Mandatory standalone golden passed **11/11** after
  the E0 status edit.

### 2026-07-29 · CLOSE-FIELDS — tagged-closing Option C

- owner: Codex
- commit: 72b9d8f
- result: PASS. The operator answered `C`; implementation commit
  `72b9d8f06c650fafd4d6f3d4216128997a1ffd0b` adopts the two-commit
  tagged-closing protocol. Release commit `R` remains untagged, immediate child
  `C` records `R` without an annotated-tag-object field, and the annotated tag
  targets `C`.
- decision acceptance: PASS. The recorded cost is the option the operator
  selected: the runbook no longer stores the tag-object hash, and closure cites
  authenticated candidate evidence rather than published-head evidence. This
  is accepted because the closing tree contains only values knowable when
  committed, Git binds the tag to that tree and release parent, and a dated
  forward append pins the later tag object, closing commit, and hosted run.
  Published-head CI is forward confirmation, not the closing event.
- fail-before acceptance: PASS. The old checker rejected the selected shape
  with `closing record must contain exactly one annotated tag object; found 0`.
  The corrected checker rejected the pre-change active shape with
  `declared closed cycle must use the tagged-closing protocol and omit the
  Annotated tag object field; record that object in the dated post-push append`.
- failure-control acceptance: PASS. R12 has **13** registered fail-before
  mutations covering the active protocol, annotated-tag type, release parent,
  tagged tree, header assertions, pending status, unavailable refs and
  ancestry, and the complete dated post-push record. Every mutation detects its
  planted failures; the repository passes **12/12 rules / 36 controls**.
- contract acceptance: PASS. `AGENTS.md` and `cycle_check.py` describe the same
  sequence, tagged-tree checks, and required forward-record fields. Legacy
  release records through v0.15.5 retain their existing semantics.
- scope acceptance: PASS. No ref, closed runbook, published tree, crate,
  dependency, schema, protected artifact, database, or public surface changed.
  Only the declared checker, focused tests, invariant registry/harness,
  operating contract, active runbook, and status record changed.
- test acceptance: PASS. Focused `cycle_check` tests passed **34/34** on
  constrained Python 3.11.4 and 3.12.13. `./run ci-local` passed **20/20** with
  **133** workspace tests, **55** net tests (**29 + 26**), shell **266/266**,
  warning-denied current and locked Rust lanes, and clean
  clippy/fmt/ShellCheck gates. The independent Python 3.12.13 shell lane also
  passed **266/266**.
- golden-E2E delta: **0**. Mandatory standalone golden passed **11/11** after
  the status and runbook edits.
- protected artifact delta: **0**. All **206/206** pins and protected databases
  remain unchanged; no protected manifest or artifact path moved.

### 2026-07-29 · TAG-IDENTITY — A / A / E

- owner: Codex
- commit: d7268d4
- result: PASS. Implementation commit
  `d7268d48c58eed02c769238ba1e804234df4ffe2` records the operator's
  `A / A / E` decision: both historical records are right and the remote is
  incomplete; the hosted local-tag-verification skip remains with a removal
  trigger.
- `v0.8.0` acceptance: PASS. Fresh local measurement resolves annotated object
  `314c1dd914a3d8e9193445874a419ed762581e6e` to existing commit
  `bfc8c5af85734583f966ee70d2ec521155432205`; Git reports types `tag` and
  `commit`. Complete remote enumeration contains neither the tag name nor
  either object id.
- `v0.10.2` acceptance: PASS. Fresh local measurement resolves annotated object
  `d821f8b2eb6f39fe4a7d06a88cd61de771c7b0ba` to existing commit
  `7d127abac0b993c9e98294ee1c03ff01153de9d0`; Git reports types `tag` and
  `commit`. Complete remote enumeration contains neither the tag name nor
  either object id.
- claim acceptance: PASS. Both identities are classified as valid local-only
  annotated tags. Publishing the exact objects is an eventual separate
  operator-authorized action; it was not performed in this task.
- retraction acceptance: PASS. The count remains **three**. No release claim,
  closed runbook, historical banner, or checklist retraction changed.
- hosted-skip acceptance: PASS. The flag remains present in hosted CI. Its
  removal trigger is either publication of both exact annotated objects plus a
  passing hosted full-history `cycle-check` without the flag, or forward
  correction of both tag identities and all affected claims if contrary
  evidence emerges.
- scope acceptance: PASS. No tag or remote ref was created, moved, or deleted;
  no closed runbook, dated historical record, published tree, crate,
  dependency, schema, protected database, or public surface changed.
  `cycle-check`, `version-check`, and `git diff --check` passed.
- golden-E2E delta: **0**. Mandatory standalone golden passed **11/11** after
  the status and active-runbook edits.
- protected artifact delta: **0**. All **206/206** pins and protected databases
  remain unchanged.

### 2026-07-29 · RESIDUALS — G3, G4, G5 dispositions

- owner: Codex
- commit: d38030e
- result: PASS. Implementation commit
  `d38030ef4a8a213cd1b0d8c35516e64937ee339c` gives every confirmed
  operational residual a dated disposition in `ARCHITECTURE.md`; refuted G3
  receives no workaround.
- G3 acceptance: **REFUTED**. Contributor-facing `ARCHITECTURE.md` and
  `AGENTS.md` already state that `./run export-check` is operator-local, what it
  verifies, and why local/hosted CI omit it. No duplicate rule, CI job, or
  hosted trigger was added.
- G4 acceptance: **accepted with bounds**. The manifest measures **119,353
  bytes** at **206** pins; release totals are **161 → 176 → 191 → 206**,
  exactly **+15 per cycle**, and E0 measured full verification at **0.10 s real
  / 0.05 s user / 0.04 s sys**. Retention/indexing becomes work at **1 MiB** or
  after two consecutive clean `./run verify-artifacts` runs each take **≥1.00 s
  real**, whichever comes first.
- G5 shell-warning acceptance: **accepted until trigger**. The
  `StarletteDeprecationWarning` becomes work if it becomes an error/failure or
  at the next authorized constraints refresh touching FastAPI, Starlette,
  `httpx`, or `httpx2`; both constrained Python lanes must then be re-measured.
- G5 hosted-warning acceptance: **accepted until trigger**. The GitHub Actions
  Node-runtime annotation becomes work when GitHub names an enforcement date,
  a blocking job warns as an error or fails for that runtime, or an affected
  `actions/*` pin changes; the action must then be upgraded or replaced and
  hosted CI re-measured.
- architecture acceptance: PASS. The operational-residual table contains all
  dated outcomes, and the publication section now describes selected Option C
  instead of a future design subject.
- lifecycle acceptance: PASS. Manifest validation passes all **206/206** pins;
  `cycle-check`, `checklist-audit`, and `progress-check` pass.
- scope acceptance: PASS. No tool logic, crate, dependency, schema, protected
  artifact, database, public surface, or release ref changed.
- golden-E2E delta: **0**. Mandatory standalone golden passed **11/11** after
  the architecture, status, and active-runbook edits.
- protected artifact delta: **0**. No manifest or protected artifact changed;
  protected databases remain **2/2**.

### 2026-07-29 · RE-MEASURE — authenticated v0.22 candidate evidence

- owner: Codex
- commit: 9426ebc
- result: PASS. Implementation commit
  `9426ebcdeead36999fc1c71ce0687557b1f485ce` admits the authenticated Step 5
  evidence without prejudging Step 6 publication.
- hosted-identity acceptance: PASS. Exact candidate
  `10c78119cd10eeb17a01152de6b6f0c322b2b91e` was pushed only to neutral branch
  `candidate/v0.15.5-v0.22`. Before dispatch, remote `ci.yml` blob
  `96e85af978981b7af9bdd8e9e11069f158f35e57` equaled the local blob and direct
  inspection found every expected invocation. Workflow-dispatch run
  `30443692105` attempt **1** used the exact candidate and produced **7/7**
  green executable Linux jobs; report-only dependency drift was skipped.
- count-equality acceptance: PASS. Hosted logs, not job status, report **133**
  workspace tests, **55** net tests (**29 + 26**), `invariant-scan` **12/12
  rules / 36 controls**, R10 **45** exemptions, and golden **11/11**, equal to
  local execution at the same candidate. Hosted Python 3.11.15 and 3.12.13
  each collected **266** shell tests as **265 passed + 1** declared on-site
  protected-corpus skip after resolving **21** packages; local constrained
  Python 3.11.4 and independently rebuilt Python 3.12.13 each passed
  **266/266**. Local `./run ci-local` passed **20/20**.
- hosted-control acceptance: PASS. The hosted **12/12 / 36** result proves Step
  2's expanded R12 planted failures execute on the runner. Hosted lifecycle
  output reports active v0.22 open, **19** closed execution runbooks, **3**
  historical runbooks, checklist **175 checked / 3 retracted / 175 matched / 0
  exemptions**, and progress at `RESIDUALS · d38030e`.
- signed-set acceptance: PASS. Seven receipts and seven Sigstore bundles from
  run `30443692105` attempt 1 verify exact bytes, source digest, neutral source
  ref, repository, workflow signer, and GitHub-hosted runner identity. Rejected
  receipts are **0** and the matrix is complete.
- deferred-audit acceptance: PASS. The required `./run audit-deferred` release
  posture with attestations required passed **5 deferred / 2 promoted / 0**
  implemented deferred subsystems. The committed 34,816-byte report has
  SHA-256
  `7fc1b09004d1cb8e835cf90bd3d11bf68e856c4d56bb2c9564a7fdbf77abced0`;
  its measured exact-cosine p95 is **6.966708 ms** for **2,600** documents
  against the **16.264 ms** A3 anchor.
- protected-evidence acceptance: PASS. The fourteen signed files plus report
  add **15** append-only records, bringing the manifest to **221/221** pins —
  **219/219** evidence plus **2/2** authorization. Schema-v2 validation,
  `verify-artifacts`, and `evidence-report` pass; protected databases remain
  **2/2** exact.
- ref-scope acceptance: PASS. Final readback before the implementation commit
  found remote `main` unchanged at
  `b7c4b10eb506923e3ea854a32d1dc3f4c83b0eaa`, candidate exact, annotated
  `v0.15.5` unchanged, and no `v0.15.6` tag. No publication or product surface
  changed.
- new finding: every executable hosted job reports that actions targeting Node
  20 are forced onto Node 24. The linked GitHub announcement names
  **2026-06-16** as the migration date, so Step 4's named-date trigger had
  already fired. The measured workflow was not changed in Step 5; Step 6 must
  reconcile the expired architecture disposition explicitly.
- golden-E2E delta: **0**. A restricted loopback-bind attempt was a non-result;
  the identical permitted mandatory standalone golden passed **11/11** after
  the status and runbook edits.

### 2026-07-29 · R-CLOSE — v0.15.6 tagged close

- owner: Codex
- commit: a83db73
- result: PASS. Release implementation commit
  `a83db73aac3d5ef1e9a427662340eb1eb8a49df1` prepares v0.15.6 and is the
  untagged immediate parent of the closing tree. The operator selected Option C
  publication because executing the tagged-close protocol is itself the
  trigger.
- closing-evidence acceptance: PASS. Authenticated candidate
  `10c78119cd10eeb17a01152de6b6f0c322b2b91e` and run `30443692105` attempt
  **1** remain separate from the release parent. All **7/7** executable hosted
  jobs passed at that exact candidate. Candidate evidence closes the cycle;
  published-head CI is forward confirmation under the dated Step 12 amendment.
- release-parent acceptance: PASS. `./run ci-local` passed **20/20** with
  **133** workspace tests, **55** net tests (**29 + 26**), shell **266/266** on
  Python 3.11.4, locked Rust 1.78, clean rustc/clippy/fmt/ShellCheck gates, R10
  **45**, and embedded golden **11/11**. Independent Python 3.12.13 passed
  **266/266**. `invariant-scan` passed **12/12 rules / 36 controls** and
  detected all **13** R12 mutations.
- evidence acceptance: PASS. All **221/221** pins (**219/219** evidence +
  **2/2** authorization) and protected databases **2/2** remain exact.
  Root-level `export-check` passed **90** derived sources, **7** required, and
  **151** exported.
- protocol acceptance: PASS. The closed record names the already-existing
  release parent and candidate evidence, omits the not-yet-knowable tag-object
  field, and requires the annotated v0.15.6 tag to target this immediate child
  and move with `main` atomically. Exact tag, closing-commit, and post-push-run
  identities belong only in the first dated forward append.
- publication acceptance: PASS. A no-release close was legitimate but rejected
  because it would leave Option C and G3 unexecuted. Publishing makes the
  closed v0.22 runbook part of the published tree.
- G1 acceptance: PASS. The record identifies v0.22 as the fourth instance of
  the unsatisfiable/no-op/vacuous/self-referential failure family and its second
  fixed point, and corrects v0.21's incomplete ordering diagnosis using E0's
  field enumeration.
- G2 acceptance: PASS. The disposition remains **A / A / E**; historical tags
  remain valid local-only identities, the hosted skip retains its trigger, no
  historical ref moved, and retractions remain **three**.
- residual acceptance: PASS. G3 remains refuted; G4 and the shell warning keep
  their dated measured bounds. The hosted Node trigger is recorded as already
  fired and promoted to v0.23 with the affected actions, fully floating
  `dtolnay/rust-toolchain@master` ref, and trigger-freshness discipline. No
  workflow edit enters v0.22.
- scope acceptance: PASS. Every release diff path is classified exactly once
  in `STATE.md`. No CI workflow, dependency graph, runtime behavior, schema,
  protected database, robots policy, configured source, or public API surface
  changed. All named architectural residuals and the one-real-publisher
  limitation remain open.
- golden-E2E delta: **0**. Mandatory standalone golden passed **11/11** at the
  release parent.
