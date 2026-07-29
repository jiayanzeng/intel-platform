# PROGRESS-v0.23.md — append-only execution record

This file records v0.23 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-29 · ACTIVATE — v0.23 admitted with one validation defect

- owner: Codex
- commit: 09cb119
- result: FAIL at the first post-commit `cycle-check`; the committed
  `Manifest retention/indexing` deferral row said `re-measure only` without
  assigning that non-none action to a named Step N. The failure was preserved
  and corrected forward rather than amended.
- worktree acceptance: PASS. Before activation the only worktree item was the
  operator-supplied untracked `docs/cycles/TASKS-v0.23-EXECUTION.md`.
  Implementation commit `09cb119` contains only that runbook, the `AGENTS.md`
  v0.23 declaration, and this progress-log skeleton.
- entering-ref acceptance: PASS. Before activation, local `main` was
  `c9e3394df927aa56f45e2a5205555130717f5f83`, one commit ahead of measured
  remote `main` `15b6d28973058c833a77e9600741d29eda02cdc1`. Annotated tag
  object `47c5b314acd6f7fb42bba2f90312bf1185277c5c` peeled to that same remote
  closing commit. No ref changed.
- lifecycle acceptance: FAIL for `cycle-check` with the exact defect above;
  `checklist-audit` independently passed **177/177** with the same three
  retractions and zero exemptions. `progress-check` correctly reported that
  the new skeleton had no dated entry before this audit record existed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and drafted-gate measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-29 · ACTIVATE-CORRECTION — deferral assignment made executable

- owner: Codex
- commit: 88590f6
- result: PASS. A dated `Runbook amendments` entry preserves the activation
  defect, and the manifest-retention action now names Step 1 as its discharging
  step. No Step objective, gate, acceptance criterion, or done condition
  changed.
- runbook-validity acceptance: PASS. `./run cycle-check` reports active v0.23
  open with twenty closed execution runbooks and three historical runbooks.
- scope acceptance: PASS. The correction changes only this active runbook, a
  standing status path. It does not change `STATE.md`, workflow, source,
  dependency, schema, protected artifact, public surface, or any ref.
- golden-E2E delta: NOT MEASURED; no claim.

### 2026-07-29 · E0 — entering state and six gates measured

- owner: Codex
- commit: 6c2d0d8
- result: PASS. The implementation commit changes only the active runbook's E0
  execution record and checklist box. The first post-status `cycle-check`
  correctly rejected an execution record placed inside Step 1's committed
  `Done when` region; moving the record behind a section boundary restored the
  committed Step text without amending any objective, gate, acceptance
  criterion, or done condition.
- entering-matrix acceptance: PASS. Clean constrained Python **3.11.4** and
  **3.12.13** rebuilds resolved the same **21** packages and each passed shell
  **266/266** with the same one third-party warning. A permitted
  `./run ci-local` passed **20/20** with **133** workspace tests, **55** net
  tests (**29 + 26**), warning-denied current and locked Rust 1.78 lanes, clean
  clippy/fmt/ShellCheck, **12/12 rules / 36 controls**, **221/221** pins,
  protected databases **2/2**, and embedded golden **11/11**. The earlier
  sandbox loopback denial was recorded as a non-result. Standalone
  `export-check` passed **90** derived sources, **7** required paths, and
  **153** exported paths after its sandbox DNS non-result.
- G1 acceptance: PASS at measured **P2**. In a disposable clone of the local
  repository, forcing the recorded `v0.15.6` identity onto release parent
  `a83db73…` made `cycle-check` exit **1** with all four parent/tree agreement
  defects over both the closed runbook and `STATE.md`. The checker demonstrably
  read the constructed tag; the clone was deleted and working refs remained
  byte-identical.
- G2/G3 acceptance: PASS from primary sources read 2026-07-29. The Node 24
  migrations are checkout **v5**, upload-artifact **v6**, and setup-python
  **v6**; current rust-cache v2 and attest-build-provenance v4 resolve to Node
  24 implementations, while rust-toolchain is composite. Floating
  `dtolnay/rust-toolchain@master` resolved to
  `2c7215f132e9ebf062739d9130488b56d53c060c`, dated
  **2026-07-16T09:35:07-07:00**; all **6/6** uses precede attestation.
- G4 acceptance: PASS. The scope grep returned zero lines; all **17** release
  authorities were enumerated without an undefined entry-point count. v0.22's
  literal no-`apps/` contradiction was reproduced from its prohibition and
  release commit's `apps/cored/Cargo.toml` change; the separate `Cargo.lock`
  nuance is recorded.
- G5 acceptance: PASS. Three event triggers were freshly evaluated: manifest
  **127,982 bytes**, verification **0.10 s / 0.09 s**, not fired; shell
  **266/266** in both lanes with one warning and no relevant constraint refresh,
  not fired; Node migration, still fired. The refuted no-trigger row is
  explicitly out of scope, and both promoted obligations were rechecked.
- G6 acceptance: PASS. Reproducible criteria produce **4** checker-reporting
  members and **4** unsatisfiable author-side members with exact overlap **2**.
  Every member is cited to its closed runbook/progress section and classified
  by actual discovery site; the record does not claim they were all found by a
  checker.
- identity/scope acceptance: PASS. Local and remote annotated `v0.15.6` object
  `47c5b314…` peel to closing commit `15b6d289…`, whose first parent is release
  parent `a83db73…`; all **221/221** pins and protected databases **2/2**
  re-verified. `.github/workflows/ci.yml` and `STATE.md` remained entering blobs
  `96e85af9…` and `e36cdc67…`; no working ref changed.
- lifecycle acceptance: PASS after the implementation commit.
  `cycle-check`, `progress-check`, `version-check`, and `invariant-scan` were
  green. The expected pre-audit `checklist-audit` refusal named only E0's
  not-yet-appended progress entry.
- golden-E2E delta: **0**. The first sandboxed post-status run was a loopback
  permission non-result; the identical permitted run passed **11/11**.

### 2026-07-29 · RELEASE-PROSE — release mechanics single-sourced

- owner: Codex
- commit: 0f7cb32
- result: PASS. E0 measured G1 at P2, so the implementation stayed within the
  documentation-only Gate: `AGENTS.md`, `ARCHITECTURE.md`, `STATE.md`, and the
  active runbook. No checker, test, invariant registry, workflow, crate, source,
  dependency, schema, protected artifact, public surface, or ref changed.
- authority acceptance: PASS. `ARCHITECTURE.md` retains architectural release
  classification and version-authority agreement, removes both mechanical
  restatements, and delegates mechanics to `AGENTS.md` R-CLOSE. The sole
  mechanical authority explicitly says releases through v0.15.5 retain the
  prior validation shape and v0.15.6 onward uses the tagged close.
- zero-grep acceptance: PASS. The recorded mechanical-mapping grep over
  `ARCHITECTURE.md` returned exit **1** with empty stdout. No tag-to-commit
  mapping sentence remains there.
- control-scope acceptance: PASS. No literal-scan rule was added because E0's
  forced recorded-identity test made the existing checker reject all four
  wrong parent/tree agreements. The record states honestly that a one-time
  grep reduces rather than deletes the duplicate-prose class and names a
  registered literal scan with detected R12 failure as the recurrence option.
- lifecycle acceptance: PASS. Before the implementation commit, `cycle-check`,
  `progress-check`, `version-check`, and `invariant-scan` passed; the expected
  pre-audit `checklist-audit` refusal named only RELEASE-PROSE's missing progress
  entry. `STATE.md`'s live header records the active open cycle without
  changing the exact published v0.15.6 identity or measured gate counts.
- golden-E2E delta: **0**. Mandatory standalone execution passed **11/11**.

### 2026-07-29 · ACTION-MIGRATION — Node 24 actions and immutable toolchain pin

- owner: Codex
- commit: 81ca649
- result: PASS. Implementation commit
  `81ca6498c825e52c2c2604eec169bd4a4898b6e3` changes the workflow as one
  attributable edit, updates its receipt-control assertion, and narrowly
  corrects the Step 3 Gate before hosted measurement.
- gate-width acceptance: PASS. The original workflow/status-only Gate omitted
  a shell control that required `actions/upload-artifact@v4` once per hosted
  job. Before implementation, the Gate was widened only for that version
  assertion. No production Python or Rust source, dependency, schema, protected
  database, or public surface changed.
- action-major acceptance: PASS. E0's recorded sources selected checkout
  **v5** (**7/7** uses), upload-artifact **v6** (**7/7**), and setup-python
  **v6** (**2/2**). Rust-cache v2 and attest-build-provenance v4 remained
  because E0 measured their Node 24 implementations. For inputs and outputs
  used here, the three migrations are unchanged; the release-note migration
  fact is their Node 24 runtime and required Actions Runner **v2.327.1**.
- immutable-pin acceptance: PASS. All **6/6**
  `dtolnay/rust-toolchain@master` uses now name full commit
  `2c7215f132e9ebf062739d9130488b56d53c060c`, obtained by primary
  `git ls-remote` and dated **2026-07-16T09:35:07-07:00** in E0's disposable
  clone. The pin receives no fixes automatically; revisit on a
  `rust-toolchain.toml` change, an applicable upstream security/correctness
  fix, or the next authorized workflow-maintenance pass, whichever occurs
  first.
- existing-evidence acceptance: PASS with the required boundary. Static
  `verify-artifacts` matched **221/221** existing pins and protected databases
  **2/2**; that proves manifest/byte integrity and says nothing about the new
  signer. Separately, GitHub CLI **2.96.0 (2026-07-02)** re-derived the prior
  v0.22 release-grade set as **7** authenticated identities before verifying
  the new set.
- hosted-signing acceptance: PASS. Candidate
  `81ca6498c825e52c2c2604eec169bd4a4898b6e3` was pushed only to
  `codex/v0.23-action-migration`; remote and local workflow blobs both resolved
  to `48ea726b798f1049e0b29cce1f0c64588861c2dd`. Workflow-dispatch run
  `30456330833` attempt **1** passed all **7/7** executable jobs; report-only
  dependency drift was skipped. Its new **7-receipt / 7-bundle** set verified
  **7 accepted / 0 rejected** with attestations required and the complete
  expected identity set: core, golden, lint, MSRV, net, and shell Python
  3.11/3.12.
- identity acceptance: PASS. Every new bundle binds repository
  `jiayanzeng/intel-platform`, workflow signer
  `jiayanzeng/intel-platform/.github/workflows/ci.yml`, source digest
  `81ca6498c825e52c2c2604eec169bd4a4898b6e3`, neutral source ref
  `refs/heads/codex/v0.23-action-migration`, and a GitHub-hosted runner. The
  set and temporary report remained under `/private/tmp`; they are
  verification-only and were not admitted to the manifest.
- failure/revert acceptance: NOT APPLICABLE after success. The same
  `gh` **2.96.0** verified the prior and new authenticated sets, so no
  action-side or CLI-side failure exists to classify and no action pin was
  reverted or worked around.
- annotation acceptance: PASS. Direct GitHub check-run inspection reported
  annotation count **0** for all seven successful jobs and the skipped
  report-only job. The Node-runtime annotation is absent and no replacement
  annotation exists.
- local-control acceptance: PASS. Targeted receipt control passed **1/1**;
  the full constrained Python 3.11 shell suite passed **266/266** with the one
  accepted third-party warning; `cycle-check` passed; `invariant-scan` passed
  **12/12 rules / 36 controls**. Sandbox-denied loopback/process attempts were
  non-results and identical permitted runs passed.
- ref/scope acceptance: PASS. Remote `main` remained
  `15b6d28973058c833a77e9600741d29eda02cdc1`; no tag, release, protected
  artifact, or manifest entry changed.
- golden-E2E delta: **0**. The sandboxed bind attempt was a non-result; the
  identical permitted standalone run passed **11/11**.

### 2026-07-29 · SCOPE-DECLARED — active-cycle scope made executable

- owner: Codex
- commit: ab79aaa
- result: PASS. Implementation commit
  `ab79aaa87027825c9a07fe5cd9cdff48fba7ef12` adds the v0.23-forward
  declared-scope parser and both enforcement phases, corrects the active
  declaration, registers its planted failure, and changes no workflow,
  production source, dependency, schema, protected artifact, or public
  surface.
- schema acceptance: PASS. One two-column markdown table carries
  `scope_version`, `disposition_intent`, `allow`, `release_authority`, and
  `forbid` rows. Parsing reuses the deferral checker's markdown-cell,
  normalization, and separator conventions; repository-relative Git-style
  globs preserve `*`, `**`, `?`, and character classes in values.
- firing-time acceptance: PASS. The static sub-rule fires at activation for a
  declared or recorded release and requires coverage of all **17** enumerated
  release authorities. The diff sub-rule fires after later commits over
  activation commit `09cb119ba4237f99f652327d8babd51d95517cd7`
  **exclusive** through `HEAD` **inclusive**. A disposable Git fixture passed
  at activation, then rejected `outside.txt` in its next commit.
- standing-set acceptance: PASS. The checker owns the exact standing set:
  `STATE.md`, the active runbook, and the active progress record. A direct
  fixture accepted those three and rejected `AGENTS.md`; the contract file is
  allowed in v0.23 only because the table declares it.
- draft-validation acceptance: CORRECTION REQUIRED and completed. The
  activation YAML draft fit the schema's classes but omitted
  `shell/tests/test_deferred_audit.py`, already changed under Step 3's widened
  Gate, and its `shell/intel_shell/**` forbid overlapped both Python release
  authorities rather than the asserted one. The corrected table adds the test
  and uses `shell/intel_shell/[a-z]*.py`.
- glob/overlap acceptance: PASS with the required weakening. The lower-case
  module glob does not swallow `shell/tests/**` or version-only
  `__init__.py`. Across the **17** authorities, the exact forbid intersection
  is `shell/intel_shell/app.py` alone. Release-authority precedence permits its
  R-CLOSE version edit and weakens path enforcement for exactly that file;
  human diff classification remains required. Literal relocation to
  `__init__.py` is the recorded forward option.
- boundary/contract acceptance: PASS. `AGENTS.md` names the two firing times,
  the exclusive/inclusive endpoints, exact standing paths, glob and precedence
  rules, v0.23-forward boundary, and the interpretive rule that exit 0 from an
  unexamined construction is `not measured`. No pre-v0.23 closed runbook was
  edited or required to carry a scope table.
- fixture acceptance: PASS. The v0.22-shaped scope fixture emitted four exact
  rejections: its release-authority set and changed-path set each rejected
  `apps/cored/Cargo.toml` and `Cargo.lock`. It was an in-memory/temporary
  fixture, not an edit to v0.22.
- planted-failure acceptance: PASS. R12 mutation **14** replaces the shared
  static/diff rejection conditional with false; self-test detected
  `v0.22-release-paths` at `tools/cycle_check.py:1204`.
- committed-diff acceptance: PASS. After the implementation commit,
  `cycle-check` accepted all paths in
  `09cb119ba4237f99f652327d8babd51d95517cd7..HEAD`; the set includes the
  declared workflow, contract, architecture, checker, invariant registry and
  tests plus the three standing status paths.
- measured-count acceptance: PASS in all three required records.
  `invariant-scan` passes **12/12 rules / 37 controls**, with R12
  **14/14**; the same counts appear in `STATE.md`, the active runbook's
  execution/pending-close records, and this progress entry.
- test acceptance: PASS. Focused lifecycle tests pass **39/39**, invariant
  tests **22/22**, and the full constrained Python 3.11 shell suite passes
  **271/271** with the one accepted third-party warning. `cycle-check` passes
  at the committed task gate.
- ref acceptance: PASS. No tag or branch was created, moved, or deleted in
  Step 4; the existing Step 3 candidate branch was not pushed again.
- golden-E2E delta: **0**. Mandatory standalone execution passed **11/11**.
