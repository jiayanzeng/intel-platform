# PROGRESS-v0.10.3.md — append-only execution record

This file records v0.10.3 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-26 · E0-GATE — supplied runbook admitted before baseline restart

- owner: Codex
- commit: f220e695dc93189d9fe919d80e373d96edd55851
- result: BLOCKED, then corrected without claiming E0 complete. The read-only
  opener found only the operator-supplied untracked
  `TASKS-v0.10.3-EXECUTION.md`; `AGENTS.md` still correctly declared the
  latest closed cycle, v0.10.2.
- identity evidence: entering HEAD was
  `6a7070b97bd4bef08345311644fa8815a58cd282`
  (`v0.10.2-1-g6a7070b`), local `main` was four commits ahead / zero behind
  `origin/main` at `817e7f3e7c1878c18f474532df4d50c2b17fcbdc`, and the
  remote tag census contained v0.10.0 and v0.10.1 but no v0.10.2.
- correction: committed the reviewed runbook unchanged, declared v0.10.3
  active, and created this progress log.
- lifecycle acceptance: `./run cycle-check` passed with active v0.10.3 and
  seven closed execution runbooks. `./run checklist-audit` resolved the
  entering 69/69 checked tasks with zero exemptions; `git diff --check`
  passed.
- test acceptance: NOT RUN at this gate checkpoint. E0 remains unchecked and
  restarts from the clean post-audit tree.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected file was touched.

### 2026-07-26 · E0 — entering state rebuilt and G1–G6 confirmed

- owner: Codex
- commit: ac9bf73a41fe62c35b8891253232bf45230a22cf
- result: PASS after the separately recorded cycle activation. Clean HEAD
  `4c70da5760a25fe5781ce7d09d6350cda69187d9` was
  `v0.10.2-3-g4c70da5`; the two activation commits explain local `main` being
  six ahead / zero behind remote `origin/main` at `817e7f3e…`. Local
  annotated v0.10.2 remained exact at tag object `d821f8b2…` and release
  commit `7d127aba…`; the authenticated remote census still had no v0.10.2
  tag.
- baseline acceptance: PASS. The sandboxed first `./run ci-local` attempt was
  an environment non-result because eight controls could not bind loopback or
  run `ps`. The permitted identical rerun passed **19/19** with 99 workspace
  tests, 20 net tests, warning-denied builds, clippy/fmt, locked Rust 1.78,
  156/156 Python 3.11 shell tests, golden 11/11, protected artifacts 2/2,
  three evidence pins, fingerprints, and lifecycle auditors.
- Python acceptance: PASS. The independent Python 3.12.13 lane passed
  156/156, and both interpreter lanes matched 21/21 exact packages.
- artifact acceptance: PASS. Standalone protected verification matched 2/2;
  manifest validation and an independent SHA-256 implementation both matched
  all three pins at 27,786 / `00cf14ae…`, 62,978 / `beec8bfa…`, and 28,968 /
  `4e11a8b3…` bytes/hash.
- defect acceptance: PASS. G1 counts job names and loses matrix identity; G2
  leaves authentication optional and its posture unread; G3 accepts the
  substitution contradiction; G4 pins neither source revision nor committed
  receipt/bundle bytes; G5 hard-codes the wrong task label and scans too
  narrowly; G6's undisclosed Step 2 contract rewrite was recovered by diffing
  Git blob `0eaef257…` against the first committed runbook.
- drafted-expectation correction: the broad G2 grep did not match only tests;
  it also found the option and writer in `tools/audit_deferred.py`, as it must.
  The finding was confirmed by the absence of any requiring invocation in
  `run` or `ci.yml` and any posture reader.
- CLI policy acceptance: PASS. Verbatim `gh attestation verify --help` from
  gh 2.96.0 exposed `--signer-digest`, `--source-digest`, and `--source-ref`;
  the current verifier passes none.
- lifecycle acceptance: PASS. Standalone `version-check`, `cycle-check`,
  `checklist-audit`, and `progress-check` passed; checklist entered at 69/69
  historical tasks with zero exemptions.
- golden-E2E delta: none. Standalone permitted `./run golden` passed 11/11
  with every exact anchor unchanged.
- protected artifact delta: none. Both protected databases and all three
  pinned JSON reports remained byte-exact.

### 2026-07-26 · MATRIX-ID — CI matrix identified instead of counted

- owner: Codex
- commit: da401507bd64ac9a2f07f37fc68b0d5b42fc7291
- result: PASS. Production receipt completeness is the exact seven-member
  `(job, matrix)` identity set: five single-leg jobs plus shell
  `python=3.11` and `python=3.12`. Accepted rows preserve matrix, workflow,
  repository, and event SHA.
- matrix-shape acceptance: PASS. Shell requires exactly one declared matrix
  value; single-leg jobs must omit the field. Missing shell matrix, unknown
  `python=3.13`, and a matrix on `core` each produce a distinct rejection.
- duplicate acceptance: PASS. Duplicate `(job, matrix)` subjects and duplicate
  receipt content digests produce separate findings; either empties the
  accepted set and records zero observed executions.
- failure-capable control: PASS. The selected fail-before set failed **5/5**
  under the old guard: two authenticated copies of the Python 3.11 bytes were
  counted as both shell legs, three malformed matrix shapes promoted, and
  accepted rows lost identity. Pass-after was **5/5**; the duplicated set
  records both duplicate findings, misses Python 3.12, and defers.
- legacy compatibility: PASS without inferred identity. Immutable reports and
  old runner bytes are unchanged. Rederivation explicitly recognizes the old
  count-contract report shape; the production report-creation path cannot
  select it and emits `expected_job_identities`. The pinned v0.10.1 report
  still re-derived with seven rows, five source dispositions, and seven
  triggers.
- workflow acceptance: PASS. The executable source assertion confirms exactly
  one workflow `matrix` field, on the shell job; all single-leg emitters omit
  it.
- Python acceptance: PASS. The focused module passed 28/28 and the full shell
  suite passed 160/160 under both Python 3.11.4 and 3.12.13, with the existing
  single Starlette warning. Python compilation and `git diff --check` passed.
- golden-E2E delta: none. `./run golden` passed 11/11 with every exact anchor
  unchanged.
- protected artifact delta: none. Both protected databases matched 2/2, all
  three JSON pins matched, and manifest validation passed.

### 2026-07-26 · AUTH-REQUIRED — release evidence made authenticated by construction

- owner: Codex
- commit: 919d304ad8f1cac13a373eb55c8952210b30eb11
- result: PASS. Production audits require an explicit `structural` or
  `release` evidence grade. Release grade forces attestation verification and
  requires the bundle directory, expected repository, and expected workflow;
  structural grade refuses authentication arguments and remains the
  token-free wrapper default.
- report-posture acceptance: PASS. New reports stamp top-level
  `evidence_grade` and `attestations_required`. Re-derivation compares both
  fields plus every accepted receipt's verification flag. Existing immutable
  reports retain their bytes and use explicit legacy posture derivation.
- pin-gate acceptance: PASS. Every pinned file now carries a manifest grade.
  A release-grade pin must resolve to a JSON report that declares release,
  requires attestations, and contains non-empty accepted bundle records marked
  verified. All three existing pins retained their exact hashes and sizes.
- failure-capable control: PASS. The selected controls produced **5 failures /
  1 pass** before implementation: the CLI did not require a grade, false
  release and tampered legacy posture re-derived, and the manifest could not
  express or enforce release grade. After implementation all **7/7** selected
  controls passed, including genuine release-grade re-derivation and pin
  validation.
- Python acceptance: PASS. The combined focused suites passed **47/47** and
  the full shell suite passed **167/167** under both Python 3.11.4 and 3.12.13,
  with the existing single Starlette deprecation warning. Python compilation,
  `bash -n run`, and `git diff --check` passed.
- runner acceptance: PASS. The permitted complete `./run ci-local` passed
  **19/19**, including the token-free structural re-derivation, 99 workspace
  tests, 20 net tests, warning-denied builds, clippy/fmt, locked Rust 1.78,
  shell 167/167, persisted fingerprints, and lifecycle checks.
- re-derivation boundary: the immutable v0.10.1 structural receipt passed
  source re-derivation. The v0.10.2 authenticated receipt's direct source
  re-derivation still defers its CI row because its seven raw receipts and
  bundles are absent from the repository; this is the measured G4b input gap
  assigned to EVIDENCE-DURABLE, not an AUTH-REQUIRED pass claim.
- golden-E2E delta: none. Standalone and `ci-local` golden runs passed 11/11
  with every exact anchor unchanged.
- protected artifact delta: none. Both protected databases matched 2/2,
  manifest validation passed, and all three existing JSON pins remained exact.

### 2026-07-26 · RESUME-INVARIANT — contradictory attempts halt instead of retrying

- owner: Codex
- commit: db3f892720d991c893a0adee0b95df9d96df790b
- result: PASS. One shared consistency function is executed by the fresh
  classifier and resume validator. Resume accepts only schema-complete attempts
  whose outcome, overlaps, violation ids, and telemetry can coexist.
- classifier acceptance: PASS. Public overlap implies `LEAK`; raw overlap
  implies `GUARD FIRED` or `LEAK`; `GUARD FIRED` requires raw overlap, forbids
  public overlap, and requires a violation id; `NOT EXERCISED` forbids both
  overlaps; and `LEAK` requires at least one overlap. A 16-token-or-longer
  gated telemetry match contradicts `raw_overlap: false`.
- declaration acceptance: PASS. Every resumed target belongs to the report's
  declared battery, every shape belongs to the five code-declared adversarial
  shapes, and every model matches the report's declared chat provider.
- halt-mode acceptance: PASS. A schema-complete contradiction records target,
  shape, and reason under `halted_on_resumed_invariant`, then raises the
  distinct `ResumedAttemptInvariantError`; it is not silently discarded as
  retryable transport noise. Consistent resumed `LEAK` evidence retains its
  separate emergency halt.
- failure-capable control: PASS. Before implementation, all **7/7**
  contradiction/declaration controls failed while the unchanged-evidence
  control passed **1/1**. After implementation, all **8/8** selected controls
  passed: the audit substitution, missing guard violation, overlap-free leak,
  telemetry contradiction, undeclared target, unknown shape, and mismatched
  model halted, while the committed X-REGEN report reused all 45 attempts.
- unchanged-evidence acceptance: PASS. The immutable X-REGEN receipt remained
  45 `NOT EXERCISED`, zero `GUARD FIRED`, zero `LEAK`, with all **45/45**
  attempts reused and zero retries.
- Python acceptance: PASS. The verifier module passed **31/31** and the full
  shell suite passed **175/175** under both Python 3.11.4 and 3.12.13, with
  the existing single Starlette deprecation warning. Python compilation and
  `git diff --check` passed.
- golden-E2E delta: none. `./run golden` passed 11/11 with every exact anchor
  unchanged.
- protected artifact delta: none. Both protected databases matched 2/2,
  manifest validation passed, and all three pins—including the 62,978-byte
  X-REGEN report—remained exact.

### 2026-07-26 · EVIDENCE-DURABLE — signer revision and raw CI evidence pinned

- owner: Codex
- commit: 382d4b1537b0ae03f06e51fa0561b3ef9d3a03d0
- result: PASS. Authenticated GitHub run **30194678764**, attempt **1**, was
  still retained. Its seven receipts and seven Sigstore bundles were downloaded
  once with the operator's authenticated `gh`, committed under
  `evidence/ci-runs/30194678764-1/`, and hash-pinned.
- source-revision acceptance: PASS. The installed gh 2.96.0 flags captured at
  E0 are now used exactly: `--signer-digest`, `--source-digest`, and
  `--source-ref`, together with repository, signer workflow, and
  `--deny-self-hosted-runners`. Verification also parses the JSON certificate
  and requires one non-empty identity plus exact signer/source digest and ref.
- real bundle acceptance: PASS. All **7/7** persisted pairs verified for
  repository `jiayanzeng/intel-platform`, workflow
  `jiayanzeng/intel-platform/.github/workflows/ci.yml`, source/signer digest
  `817e7f3e7c1878c18f474532df4d50c2b17fcbdc`, source ref
  `refs/heads/main`, and certificate identity
  `https://github.com/jiayanzeng/intel-platform/.github/workflows/ci.yml@refs/heads/main`.
  The direct complete-matrix measurement returned observed **7**, rejected
  **0**. The receipts' checked-out subject is
  `e5af6bc5df8261cc004bd4d3247b70f8cbe930bb`; their event/source commit is
  `817e7f3e…`.
- real negative control: PASS. Verification with the expected source digest
  replaced by forty zeroes exited **1** and reported expected
  `SourceRepositoryDigest` zero versus actual `817e7f3e…`.
- identity/path acceptance: PASS. Accepted rows persist certificate identity,
  signer digest, source digest, and source ref. External measurements retain
  their true absolute `path` plus an explicit `logical_path`; committed rows
  use paths that actually exist in the repository.
- durable-layout acceptance: PASS. The seven legacy run 30187058897 receipts
  moved into `evidence/ci-runs/30187058897-1/`. Seven tracked compatibility
  symlinks preserve the immutable v0.10.1 report's flat recorded paths while
  leaving one stored byte copy. `git ls-tree` found all **21** raw files under
  the two run directories and mode 120000 for all seven aliases.
- pin acceptance: PASS. Manifest schema 2 now reports **24/24** matching file
  pins: three immutable reports, seven legacy receipts, seven authenticated
  receipts, and seven authenticated bundles. Release-grade validation requires
  every recorded receipt/bundle path to be pinned, repository-contained, and
  resolvable, and requires the accepted certificate/source fields to match the
  report policy. `python3 tools/evidence_artifacts.py validate` and
  `./run verify-artifacts` both passed; protected databases remained **2/2**.
- failure-capable controls: PASS. Before implementation, the selected three
  controls failed **3/3**: the runner API lacked source policy, the verifier
  lacked source/certificate output, and release validation accepted unresolved
  paths. After implementation the expanded set passed **4/4**. The focused
  deferred-audit/artifact suites passed **50/50** on both Python 3.11.4 and
  3.12.13.
- compatibility acceptance: PASS. The immutable v0.10.1 deferred report
  re-derived successfully after the layout move, proving its recorded aliases
  resolve without rewriting the pinned report.
- runner acceptance: PASS. A sandboxed `ci-local` attempt was an environment
  non-result because `ps` and loopback binds were denied. The permitted
  identical rerun passed **19/19**: 99 workspace tests, 20 net tests,
  warning-denied builds, clippy/fmt, locked Rust 1.78, shell **178/178**,
  structural re-derivation, persisted fingerprints, protected artifacts, and
  lifecycle checks. The independent Python 3.12 shell lane also passed
  **178/178**. Python compilation and `git diff --check` passed.
- golden-E2E delta: none. The required standalone `./run golden` passed
  **11/11** with every exact anchor unchanged.
- protected artifact delta: none. Both protected databases and all three
  previously pinned report bytes remained exact. The manifest pin count changed
  deliberately from **3** to **24** by admitting the raw CI evidence; no
  product runtime, dependency, lockfile, architecture, provider configuration,
  remote ref, or tag changed.

### 2026-07-26 · LITERAL-NEUTRAL — stale literals and silent amendments refused

- owner: Codex
- commit: a01c47d67bcbbac47cc70772b8f9edcac5fc851e
- result: PASS. New deferred/adversarial report labels derive from the active
  cycle declaration; benchmark labels are cycle-independent. Historical
  evidence paths live once under semantic keys in the validated
  `config/cycle-history.json` registry.
- literal acceptance: PASS. `cycle-check` scans all Python source in `tools/`,
  `run`, and `.github/workflows/*.{yml,yaml}` for concrete
  `TASKS-…` / `PROGRESS-…` names and bare semantic-version cycle literals.
  Direct `rg` found zero concrete cycle literals in those guarded sources.
  Harness help uses cycle-neutral examples, and local/hosted historical
  re-derivation resolves the semantic baseline key.
- runner acceptance: PASS. The hosted Python 3.11 shell job now executes
  `./run cycle-check` on its existing full-history checkout; no new CI job was
  added, so the configured count remains **19**.
- amendment acceptance: PASS. The active runbook's Objective, Acceptance
  criteria, and Done-when blocks are compared with the blob in the commit that
  first added the runbook. A changed, added, or removed field must name its Step
  in one validly dated `## Runbook amendments` entry. Checkbox progress does
  not alter the compared contract.
- failure-capable controls: PASS. Before implementation, a planted tool label,
  a stale harness evidence path, and an undisclosed Acceptance-criteria edit all
  incorrectly passed: **3/3 selected controls failed**. After implementation,
  the lifecycle module passed **7/7**: those three were refused, a planted
  workflow literal was refused, the clean tree passed, and a disclosed dated
  edit passed.
- label acceptance: PASS. The clean production-report test created
  `v1.2.3 RECEIPT` from a synthetic active declaration rather than a source
  literal. The focused report/benchmark/lifecycle/audit suite passed **76/76**.
- closed-cycle annotation: PASS without evidence mutation.
  `PROGRESS-v0.10.2.md` and `STATE.md` gained dated
  `Closed-cycle status correction` banners naming the wrong immutable
  `v0.10.1 RECEIPT` field, its correct v0.10.2 meaning, and the derived fix.
  Direct SHA-256 remained
  `4e11a8b3a3a64b5519469289f5cdf246bf13a0045954aa22c38703bbe6d29d9b`
  at 28,968 bytes; the report and its pin were not edited.
- compatibility acceptance: PASS. The semantic baseline path resolved to the
  immutable deferred report and `./run audit-deferred --rederive` passed with
  seven rows, five source dispositions, seven triggers, legacy grade, and
  attestations false.
- Python acceptance: PASS. Both complete shell lanes passed **183/183** under
  Python 3.11.4 and 3.12.13, with the existing single Starlette deprecation
  warning. Python compilation, `bash -n run`, ShellCheck, and
  `git diff --check` passed.
- repository acceptance: PASS. The final `./run ci-local` passed **19/19**:
  99 workspace tests, 20 net tests, warning-denied builds, clippy/fmt, locked
  Rust 1.78, 183 shell tests, lifecycle checks, evidence re-derivation,
  persisted fingerprints, protected artifacts, and append-only progress.
- golden-E2E delta: none. The required final standalone `./run golden` passed
  **11/11** with every exact anchor unchanged.
- protected artifact delta: none. Both protected databases matched **2/2** and
  all **24/24** file pins matched. No product runtime, dependency, lockfile,
  architecture, protected byte, pinned evidence byte, provider configuration,
  remote ref, or tag changed.

### 2026-07-26 · HOSTED-CYCLE-GATE — separate local tag verification

- owner: Codex
- commit: 8b17b5e00d245ffb964a9bfb2a404bb390fc237f
- result: PASS. Operator-authorized hosted run **30201012362**, attempt **1**,
  audited exact checkout `87fa115bb5279694fb21fcb140545583ba29471a`.
  Six expected jobs passed; the Python 3.11 shell job failed at the newly added
  lifecycle step because the remote clone cannot resolve recorded local-only
  annotated refs. The run is recorded as failed evidence and is not a
  release-grade success.
- gate measurement: PASS. `git ls-remote --tags origin` returned only
  `v0.9.0`, `v0.10.0`, and `v0.10.1`; it confirmed the failing `v0.8.0` and
  `v0.10.2` refs are absent remotely while their release commits are ancestors
  of `origin/main`. Neither local tag moved.
- correction acceptance: PASS. Plain `./run cycle-check` still resolves every
  local annotated-tag object and dereferenced release commit. Hosted CI invokes
  the explicit `--skip-local-tag-verification` mode, which omits only those
  unavailable refs while retaining release-record structure, recorded
  commit-object, lifecycle, source-literal, and amendment checks.
- failure-capable controls: PASS. The lifecycle suite passed **9/9**. Strict
  mode refused a planted unavailable historical tag, hosted mode accepted its
  present release commit, and hosted mode independently refused a nonexistent
  recorded release commit.
- Python acceptance: PASS. Both complete shell lanes passed **185/185** under
  Python 3.11.4 and 3.12.13, with the existing single Starlette deprecation
  warning. `bash -n run` and `git diff --check` passed.
- repository acceptance: PASS. `./run ci-local` passed **19/19**: 99 workspace
  tests, 20 net tests, warning-denied builds, clippy/fmt, locked Rust 1.78,
  185 shell tests, strict lifecycle checking, evidence re-derivation,
  persisted fingerprints, and append-only progress.
- golden-E2E delta: none. The required standalone `./run golden` passed
  **11/11** with every exact anchor unchanged.
- protected artifact delta: none. Both protected databases matched **2/2** and
  all **24/24** file pins matched. No product runtime, dependency, lockfile,
  architecture, protected byte, pinned evidence byte, provider configuration,
  or tag changed. Remote `main` still named the failed candidate audit commit
  at this measurement.

### 2026-07-26 · EVIDENCE-PATH-ADMISSION — indexed durable paths

- owner: Codex
- commit: 17cc2b7615b1ea7861319035f6e89bf43d92085a
- result: PASS. Authenticated hosted run **30201306837**, attempt **1**, passed
  all seven expected jobs at exact candidate
  `725b8820c29fd4e6dac8be1c32b69f59f2a6fc35`. Its seven downloaded receipts
  had seven distinct identities, exact subject/event SHA, and successful
  conclusions. Real source-pinned attestation verification accepted all seven.
- gate measurement: PASS. The clean release-grade preview accepted **7**,
  rejected **0**, and measured **5 deferred / 2 promoted**, but correctly
  recorded its external inputs at absolute temporary paths. The compatibility
  `logical_path` dropped the nested run directory, so the preview was not
  admitted or hand-edited; it could not satisfy release-pin validation.
- path correction: PASS. New `--evidence-repository` keeps subject measurement
  on the explicit clean `--subject-root` while recording receipt and bundle
  paths only when they resolve inside the named Git worktree root, are already
  indexed, and are byte-identical to their index entries. The resulting path is
  the true repository-relative nested path. Untracked and changed-after-stage
  controls are refused.
- real failing-job control: PASS. Hosted run **30201489016** failed only the
  planted core step and still persisted seven signed receipt/bundle pairs. The
  authenticated guard rejected the core `conclusion:"failure"` receipt, named
  the missing core identity, and accepted **0** executions.
- real duplicate-subject control: PASS. Mixed-control attempt **30201602108**
  was canceled before acceptance. Isolated hosted run **30201653302** passed all
  seven jobs and attestations, but both shell receipts claimed `python=3.11`.
  The guard named that duplicate and the missing `python=3.12` identity, then
  accepted **0** executions. Remote/local control refs and the temporary
  worktree were deleted.
- Python acceptance: PASS. Both complete shell lanes passed **187/187** under
  Python 3.11.4 and 3.12.13 with the existing single Starlette deprecation
  warning. Python compilation and `git diff --check` passed.
- repository acceptance: PASS. `./run ci-local` passed **19/19**: 99 workspace
  tests, 20 net tests, warning-denied builds, clippy/fmt, locked Rust 1.78,
  187 shell tests, strict lifecycle checking, evidence re-derivation,
  persisted fingerprints, and append-only progress.
- golden-E2E delta: none. The required standalone `./run golden` passed
  **11/11** with every exact anchor unchanged.
- protected artifact delta: none. Both protected databases matched **2/2** and
  all **24/24** file pins matched. No product runtime, dependency, lockfile,
  architecture, protected byte, pinned evidence byte, provider configuration,
  or tag changed.

### 2026-07-26 · RE-MEASURE — authenticated v0.10.3 receipt

- owner: Codex
- commit: 58f02b1f837c81e556ba1d54f9fed9728947f746
- result: PASS. Operator-authorized hosted run **30202019640**, attempt **1**,
  passed all seven expected jobs against exact candidate
  `a1d8c958b4eaf4fe4add75cc49a7fec341c8f8a5`. The downloaded receipts carried
  seven distinct expected `(job, matrix)` identities, exact subject/event SHA,
  repository, workflow, and successful conclusions.
- authentication acceptance: PASS. Real source-pinned Sigstore verification
  accepted all seven persisted bundles with the CI workflow certificate
  identity, source/signer digest `a1d8c958…`, source ref `refs/heads/main`,
  and GitHub-hosted runner policy. The clean detached production audit accepted
  **7**, rejected **0**, found a complete matrix with no findings, and measured
  **5 deferred / 2 promoted**. Exact-cosine p95 was **8.390958 ms**.
- negative controls: PASS. Run **30201489016** persisted signed artifacts after
  its planted core failure; the guard named the failed conclusion and missing
  core identity, then accepted **0** executions. Mixed-control run
  **30201602108** was canceled rather than conflated with the duplicate test.
  Isolated run **30201653302** passed all seven jobs and attestations but made
  both shell receipts claim `python=3.11`; the guard named the duplicate and
  missing `python=3.12` identity, then accepted **0** executions. The
  throwaway remote/local branch and worktree were deleted.
- durability acceptance: PASS. The seven receipts and seven bundles are
  committed under `evidence/ci-runs/30202019640-1/`. The release-grade report
  is committed at `evidence/v0.10.3/deferred-audit/report.json`, 33,754 bytes
  at SHA-256
  `272487af426675c3b5f3be25f5521f5a03bc5f148cd8d50c5651a692c5993c51`.
  Manifest schema 2 validation and protected-artifact verification passed all
  **39/39** file pins and both protected databases **2/2**.
- re-derivation acceptance: PASS. The network-enabled exact command passed
  with seven rows, five source dispositions, seven triggers, release evidence
  grade, attestations required, and view materialization false. A first
  restricted-sandbox invocation could not initialize a Sigstore verifier and
  rejected all seven rows; no assertion or evidence byte changed before the
  exact network-enabled rerun passed.
- Python acceptance: PASS. Both complete shell lanes passed **187/187** under
  Python 3.11.4 and 3.12.13, with the existing single Starlette deprecation
  warning.
- repository acceptance: PASS. `./run ci-local` passed **19/19**: 99 workspace
  tests, 20 net tests, warning-denied builds, clippy/fmt, locked Rust 1.78,
  lifecycle and evidence checks, persisted fingerprints, protected databases
  **2/2**, and all **39/39** pins.
- golden-E2E delta: none. The required final standalone `./run golden` passed
  **11/11** with every exact anchor unchanged.
- protected/tag delta: none. No product runtime, dependency, lockfile,
  architecture, protected byte, prior pinned evidence byte, provider
  configuration, or tag changed. `v0.10.1` remains published unchanged and
  `v0.10.2` remains local-only at its original annotated tag object.
