# PROGRESS-v0.11.md — append-only execution record

This file records v0.11 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-27 · E0-GATE — supplied runbook admitted before baseline restart

- owner: Codex
- commit: 57e56b7268345ea17dda6641dd2682295b43ec55
- result: BLOCKED, then corrected without claiming E0 complete. The read-only
  opener found only the operator-supplied untracked
  `TASKS-v0.11-EXECUTION.md`; `AGENTS.md` still correctly declared the latest
  closed cycle, v0.10.3.
- identity evidence: entering HEAD was
  `d24f2b83c9657b1fa47d7f3315a4120181f2624e`
  (`v0.10.3-1-gd24f2b8`), and local `main` and `origin/main` were aligned at
  that commit with zero ahead / zero behind.
- correction: committed the reviewed runbook unchanged, declared v0.11
  active, and created this progress log.
- lifecycle acceptance: the pre-admission `./run cycle-check` correctly
  refused a runbook with no first committed version. After commit,
  `./run cycle-check` passed with active v0.11 and eight closed execution
  runbooks. `./run checklist-audit` resolved the entering 77/77 checked tasks
  with zero exemptions; `git diff --check` passed.
- test acceptance: NOT RUN at this gate checkpoint. E0 remains unchecked and
  restarts from the clean post-audit tree.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected file was touched.

### 2026-07-27 · E0 — entering state rebuilt and S1–S8 confirmed

- owner: Codex
- commit: 337e7c04b76ee8034b6cf2e75f5897869f538d6c
- result: PASS after the separately recorded activation pair. Clean HEAD
  `ac1b2ef9cc6b9913add42d22b2d4b23f10e2a29a` was
  `v0.10.3-3-gac1b2ef`; local `main` was two ahead / zero behind
  `origin/main` at `d24f2b83…`.
- baseline acceptance: PASS. The first sandboxed `./run ci-local` was an
  environment non-result: eight shell controls were denied `ps` or loopback
  binds after all earlier units passed. The permitted identical rerun passed
  **19/19** with 99 workspace tests, 20 net tests, warning-denied builds,
  clippy/fmt, locked Rust 1.78, 187/187 Python 3.11 shell tests, golden 11/11,
  protected artifacts 2/2, all 39 pins, fingerprints, and lifecycle auditors.
- Python acceptance: PASS. The independent Python 3.12.13 lane passed
  187/187, and both interpreters verified 21/21 constrained packages.
- artifact acceptance: PASS. Standalone protected verification matched 2/2;
  manifest validation and an independent `hashlib.sha256` witness each matched
  all **39/39** pins with zero mismatches.
- defect acceptance: PASS. Static source capture confirmed S1's unchecked bind
  and optional token; both S2 body endpoints' missing sector predicates; S3's
  single-group selection; S4's raw matching; S5's limiter replacement; S6's
  fail-open library seam and defect-encoding test; S7's event-by-event live
  mutation; and S8's maintenance writes without canonical rematerialization.
  Every augment row also reproduced.
- failure-capable controls: PASS. Three temporary compliance controls asserted
  and observed the ignored duplicate product-token group, the
  `/foo/bar/%62%61%7A` evasion, and the crawl-delay transition resetting the
  counter and allowing a zero-time first acquire. A temporary signed-webhook
  control observed HTTP 400 plus the first event's surviving live mutation.
  All scratch edits were removed before the E0 record.
- inherited-guard acceptance: PASS. The v0.10.3 report is release grade with
  attestations required, seven distinct expected/accepted identities, zero
  rejection, seven verified rows, and 14 tracked existing receipt/bundle
  paths. Fresh and resumed adversarial paths share one consistency checker.
- lifecycle acceptance: PASS. Standalone version, cycle, checklist, and
  progress checks passed; checklist entered at 77/77 historical tasks with
  zero exemptions.
- golden-E2E delta: none. Standalone `./run golden` passed **11/11** with every
  exact anchor unchanged.
- protected artifact delta: none. Both protected databases and all 39 existing
  pins remained byte-exact.

### 2026-07-27 · BIND-LOOPBACK — core bind invariant made structural

- owner: Codex
- commit: 022faf9579706f5aceb0b21662098d1f81824a05
- result: PASS. `CORE_BIND` is resolved with `ToSocketAddrs`; startup refuses
  an empty resolution or any non-loopback result before opening the listener,
  and the listener consumes the validated addresses without resolving twice.
- boundary acceptance: PASS. Unit controls reject IPv4/IPv6 unspecified
  addresses, a LAN literal, and a synthetic mixed loopback/non-loopback
  hostname result. IPv4 loopback, IPv6 loopback, and `localhost` pass. The
  refusal names the offending address and multi-host seam deferral.
- runtime acceptance: PASS after one explicitly recorded stale-binary
  non-result. A warning-denied rebuild followed by
  `CORE_BIND=0.0.0.0:8788 target/debug/cored` exited before binding and named
  `0.0.0.0:8788` plus the required design-task message.
- topology acceptance: PASS. No override flag exists. `STATE.md §6d` records
  both the rejected override alternative and the decision to retain
  `CORE_TOKEN` as optional defense-in-depth under an enforced loopback bind.
  The daemon contract and `ARCHITECTURE.md` name the executable enforcement.
- regression acceptance: PASS. `./run ci-local` passed **19/19** with
  **102** workspace tests, **20** net tests, zero warning/lint/format failures,
  locked Rust 1.78, and **187/187** Python 3.11 shell tests. `run`, `deploy/`,
  Cargo manifests, and `Cargo.lock` have no diff; no dependency was added.
- golden-E2E delta: none. The required standalone `./run golden` passed
  **11/11** with every exact anchor unchanged.
- protected artifact delta: none. Standalone `./run verify-artifacts` matched
  both protected databases **2/2** and all existing pins **39/39**.

### 2026-07-27 · SECTOR-BIND — document-body endpoints bound in core SQL

- owner: Codex
- commit: d85156fc8f86b8c6ed187d545b7f3e9ffa37148f
- result: PASS. `/docs` requires ids plus sectors and
  `/embeddings/missing` requires model plus sectors. Both store queries bind a
  `sector IN (…)` predicate in SQL and return empty for an empty sector set.
- decision acceptance: PASS. The preferred zero-exception outcome was selected
  for `/embeddings/missing` and recorded in `STATE.md §6e`. The embedding
  maintenance worker and verifier pass every configured core sector; `/docs`
  receives the current subscriber's entitled sectors. `ARCHITECTURE.md` now
  states that every body-returning endpoint is sector-bound in core SQL.
- failure-capable acceptance: PASS. Handler tests span technology and finance
  ids, prove cross-sector bodies do not return, and prove empty-sector
  `/docs` and `/embeddings/missing` queries return nothing. A store test
  exercises both predicates and bound values; a shell transport test captures
  the explicit query parameters. All Python call sites and doubles were
  updated.
- regression acceptance: PASS. `./run ci-local` passed **19/19** with
  **104** workspace tests, **20** net tests, warning-denied builds,
  clippy/fmt, locked Rust 1.78, and **188/188** Python 3.11 shell tests. The
  first sandboxed Python 3.12 run was an eight-denial environment non-result;
  the permitted identical rerun passed **188/188**, with **21/21** exact
  packages.
- golden-E2E delta: none. The required standalone `./run golden` passed
  **11/11** with every public body and corpus anchor unchanged.
- protected artifact delta: none. Standalone `./run verify-artifacts` matched
  both protected databases **2/2** and all existing pins **39/39**.

### 2026-07-27 · ROBOTS-MERGE — winning-specificity groups merged safely

- owner: Codex
- commit: dd8898528a7a96aa25079ccd87186cb85550c240
- result: PASS. The parser finds the longest matching non-`*` specificity,
  merges every group at that specificity in file order, falls back to merging
  every `*` group only when no specific token matches, and takes the maximum
  crawl delay across merged groups.
- failure-capable acceptance: PASS. Duplicate `intel-platform` groups enforce
  both disallows. The named generic-root regression proves `Disallow: /` from
  `*` does not override a specific allow-all; another specific/generic control
  proves unrelated `*` rules are absent. Two merged specific delays select
  seven seconds over two.
- contract acceptance: PASS. The parser doc-comment states both the
  same-specificity merge and the deliberate `*` exclusion, including why
  merging generic rules into a specific match would be incorrect.
- regression acceptance: PASS. `./run ci-local` passed **19/19** with
  **108** workspace tests, **20** net tests, warning-denied builds,
  clippy/fmt, locked Rust 1.78, **188/188** Python 3.11 shell tests,
  protected databases **2/2**, and evidence pins **39/39**.
- golden-E2E delta: none. The required standalone `./run golden` passed
  **11/11** with every exact anchor unchanged.
- protected artifact delta: none. No protected or pinned file changed.

### 2026-07-27 · ROBOTS-NORMALIZE — percent-equivalent paths matched safely

- owner: Codex
- commit: 3770f3f18deca223c8d198507d01dd85f286591b
- result: PASS. One zero-dependency normalizer is applied to both robots
  patterns and request paths. Unreserved percent triplets decode; every
  retained valid triplet uses uppercase hex.
- semantic acceptance: PASS. Reserved octets remain encoded, so `%2F` cannot
  re-segment the path and `%2A` cannot become a wildcard. Raw `*` and trailing
  `$` keep their parser semantics. Normalized specificity is used for
  longest-rule selection.
- failure-capable acceptance: PASS. The encoded `baz` audit case is blocked,
  reserved slash remains encoded, encoded star is literal, mixed-case hex
  converges, and normalization is idempotent. Existing wildcard and anchor
  controls remain green.
- dependency acceptance: PASS. No crate, manifest, or lockfile changed.
- regression acceptance: PASS. `./run ci-local` passed **19/19** with
  **113** workspace tests, **20** net tests, warning-denied builds,
  clippy/fmt, locked Rust 1.78, **188/188** Python 3.11 shell tests,
  protected databases **2/2**, and evidence pins **39/39**.
- golden-E2E delta: none. The required standalone `./run golden` passed
  **11/11** with every exact anchor unchanged.
- protected artifact delta: none. No protected or pinned file changed.

### 2026-07-27 · DELAY-CLOCK — crawl-delay transition preserves politeness state

- owner: Codex
- commit: c2fe99a3c16e067cdf0d91b79d0aaea34ad657f7
- result: PASS. A limiter's interval is atomic and mutates in place;
  `set_host_rate` remains synchronous, updates known hosts, and still creates
  a limiter for an unknown host. The async clock and acquisition counter stay
  on the same object.
- one-way acceptance: PASS. `apply_crawl_delay` still changes the rate only
  when publisher policy is slower than the configured floor, and `rate_for`
  reports the adopted rate.
- elapsed-behavior acceptance: PASS. A paused-clock test establishes the
  robots-fetch clock at counter one, adopts a ten-second delay, observes the
  second acquire pending through nine seconds, and observes release at exactly
  ten seconds with counter two. Existing per-host isolation remains green.
- regression acceptance: PASS. `./run ci-local` passed **19/19** with
  **114** workspace tests, **20** net tests, warning-denied builds,
  clippy/fmt, locked Rust 1.78, **188/188** Python 3.11 shell tests,
  protected databases **2/2**, and evidence pins **39/39**.
- golden-E2E delta: none. The required standalone `./run golden` passed
  **11/11** with every exact anchor unchanged.
- protected artifact delta: none. No protected or pinned file changed.

### 2026-07-27 · GATE-CLOSED — network reaches require publisher policy

- owner: Codex
- commit: 0257ea7a42c12328e1721c2d9fb280c6de097197
- result: PASS. The shared ingest gate returns the dedicated
  `NetworkWithoutRobotsCache` error for `Reach::Network` plus
  `robots_cache: None`, before the operator gate, limiter, or document fetch.
- failure-capable acceptance: PASS. The runbook-named defect test was inverted
  rather than removed and now requires the new error for a public network path.
  A sibling fixture-reach test preserves the prior no-cache behavior: the
  configured gate allows a public path and rejects a denied path.
- shipped-path acceptance: PASS. Existing network-plus-cache tests remain green
  for publisher allow/deny, operator composition, unreachable policy,
  per-source missing-policy handling, and redirect behavior.
- design acceptance: PASS. `STATE.md §6f` records and defers the type-level
  alternative because making the invalid pair unrepresentable would change the
  connector/context boundary and all builders and fixtures in this patch task.
- regression acceptance: PASS. `./run ci-local` passed **19/19** with
  **115** workspace tests, **21** net tests, warning-denied builds,
  clippy/fmt, locked Rust 1.78, **188/188** Python 3.11 shell tests,
  protected databases **2/2**, and evidence pins **39/39**.
- golden-E2E delta: none. The required standalone `./run golden` passed
  **11/11** with every exact anchor unchanged.
- protected artifact delta: none. No protected or pinned file changed.

### 2026-07-27 · BILLING-ATOMIC — rejected batches leave no entitlement mutation

- owner: Codex
- commit: d3a06a584133514fea3a2426fd5ead5eab3df2a0
- result: PASS. Authenticated neutral events are applied to a detached
  in-memory store and its frozen values are published to the live backend only
  after every event validates. Routes retain publish, save, result ordering.
- failure acceptance: PASS. A signed two-event batch with an invalid second
  event returns HTTP 400 and leaves `acme-research` unchanged in live state.
  The JSON-backed control observes the file unchanged as well.
- latent-save acceptance: PASS. After that rejection, an unrelated
  `quant-desk` mutation and save persists only the unrelated change; the
  rejected first acme mutation does not leak from memory onto disk.
- success acceptance: PASS. A fully valid delete/create batch publishes both
  events and records one save. An ignored event inside another valid batch
  retains its `ignored` result, its sibling update commits, and save is called
  once. Authentication, event types, and response shapes did not change.
- contract acceptance: PASS. `apply_event` remains a single-event in-memory
  mutator with caller-owned persistence, and its docstring now also requires
  detached staging for callers applying a batch.
- regression acceptance: PASS. `./run ci-local` passed **19/19** with
  **115** workspace tests, **21** net tests, warning-denied builds,
  clippy/fmt, locked Rust 1.78, and **191/191** Python 3.11 shell tests.
  The independent Python 3.12 lane also passed **191/191**.
- golden-E2E delta: none. The required standalone `./run golden` passed
  **11/11** with every exact anchor unchanged.
- protected artifact delta: none. CI matched protected databases **2/2** and
  existing pins **39/39**; no protected or pinned file changed.

### 2026-07-27 · STORE-IDENTITY — maintenance writes preserve corpus identity

- owner: Codex
- commit: 7ac5067b6989366f75f1b2e0e57c46f9684fcfca
- result: PASS. Successful document updates and deletes rematerialize global
  canonical ids inside the same transaction as the maintenance mutation.
  Missing-row operations remain clean `false` results.
- threshold acceptance: PASS. Harvest ingest, update, and delete all call
  `assign_canonical_ids_tx` with one store-local `DEDUP_MAX_DISTANCE = 16`
  constant; there is no second production threshold literal.
- failure-capable acceptance: PASS after one compile non-result. The first
  warning-denied run stopped because the new constant was test-only dead code.
  After routing the existing ingest call through it, the unfixed methods ran
  **18/21** green with three expected stale-identity failures: changed body,
  changed publication order, and deleted canonical. The no-op control passed.
- maintenance acceptance: PASS. After the repair, all **21/21** store tests
  passed. Content and publication-order changes select the new canonical,
  deleting the canonical leaves zero rows naming its id and promotes the
  survivor, and an identical update preserves exact canonical rows. The
  doc-comments name the corpus-wide maintenance cost and absence from the
  ingest hot path.
- regression acceptance: PASS. `./run ci-local` passed **19/19** with
  **119** workspace tests, **21** net tests, warning-denied builds,
  clippy/fmt, locked Rust 1.78, and **191/191** Python 3.11 shell tests.
- golden-E2E delta: none. The required standalone `./run golden` passed
  **11/11** with every exact anchor unchanged.
- protected artifact delta: none. Standalone `./run verify-artifacts` matched
  protected databases **2/2** and existing pins **39/39**; no schema,
  protected, or pinned file changed.

### 2026-07-27 · RE-MEASURE — authenticated v0.11 candidate evidence admitted

- owner: Codex
- commit: 3c6bb3002abc1477f923d3c825aee776eb126457
- gate acceptance: PASS. Remote `main` and the clean measurement subject were
  exact candidate `17221504d0c572e2b52f8509cb720d4a7c72f47d`; the production
  audit required the expected head, release grade, attestations, repository,
  workflow, source digest, and `refs/heads/main`.
- hosted acceptance: PASS. Operator-authorized run **30236305375**, attempt
  **1**, passed core, golden, lint, MSRV, net, shell `python=3.11`, and shell
  `python=3.12`. Seven receipt/bundle pairs persisted, every receipt named the
  candidate, and the audit accepted the exact seven distinct identities with
  **0 rejected** and **7 observed executions**.
- report acceptance: PASS after one pre-measurement missing-file non-result and
  one missing-directory copy non-result in the clean detached worktree. Exact
  ignored copies of both protected databases left `git status` clean. The final
  report is release-grade, requires attestations, is labeled `v0.11 RECEIPT`,
  records a clean subject, and measures **5 deferred / 2 promoted**. Exact
  cosine p95 was **15.033417 ms** at 2,600 documents against the **16.264 ms**
  anchor.
- durability acceptance: PASS. The **33,741-byte** report hashes to
  `2bfade7c8bf5d39323a91d0a599b4576bc83a9bdce1ef9c29cca7d7db82d3d71`.
  Its 14 receipt/bundle inputs and the report occupy fresh paths; manifest
  schema 2 validates all **54/54** pins. Fresh re-derivation passed with rows
  7, source dispositions 5, triggers 7, release grade, and attestations
  required.
- negative-control acceptance: PASS. Hosted run **30236791703** persisted all
  seven signed packages but planted a core failure; the audit rejected that
  receipt and accepted/observed **0** executions. Hosted run **30237021683**
  passed all jobs but signed two `shell/python=3.11` identities and no
  `shell/python=3.12`; the identity guard again accepted/observed **0**. One
  preceding HTTP 422 dispatch attempt created no run; its disposable YAML
  syntax was corrected and the source-shape lane repeated **36 passed / 1
  skipped** before dispatch. The remote and local throwaway branch and its
  worktree were deleted; no negative-control evidence was committed.
- regression acceptance: PASS. `./run ci-local` passed **19/19** with
  **119** workspace tests, **21** net tests, warning-denied builds,
  clippy/fmt, locked Rust 1.78, and **191/191** Python 3.11 shell tests. The
  independent Python 3.12 lane passed **191/191**; both interpreters verified
  **21/21** exact packages.
- golden-E2E delta: none. The mandatory standalone `./run golden` passed
  **11/11** with every corpus and public-response anchor unchanged.
- protected artifact delta: evidence-only. Both database artifacts remained
  exact **2/2**; 15 fresh immutable file pins were added, moving the manifest
  from **39/39** to **54/54** without altering any prior path or hash.
- tag acceptance: PASS. Remote enumeration returned the unchanged published
  annotated objects and peeled commits for v0.9.0, v0.10.0, v0.10.1, and
  v0.10.3. No tag was created, moved, or published.

### 2026-07-27 · R-CLOSE — v0.11.0 minor release published

- owner: Codex
- commit: 6daeb7e9f2cc0022b5e1a1dcf2ce8702b5be0321
- result: PASS. The operator explicitly selected and authorized release
  v0.11.0 after RE-MEASURE authenticated seven distinct successful identities
  with zero rejection and both real hosted negative controls accepted zero
  executions.
- release identity: PASS. `v0.11.0` is annotated tag object
  `fcfa4825e6ffbc06c0ad73e18044965c10786aa8`, which dereferences exactly to
  release commit `6daeb7e9f2cc0022b5e1a1dcf2ce8702b5be0321`. Its annotation is
  `intel-platform v0.11.0`; the separate closing audit does not move the tag.
- publication outcome: PASS. One atomic push advanced remote `main` to the
  release commit and created the v0.11.0 tag. Read-only remote verification
  returned main and the peeled tag at the release commit and the tag ref at
  the annotated object.
- version disposition: PASS. `/docs` and `/embeddings/missing` gain required
  internal sector parameters, while bind, robots, network-policy failure,
  billing rejection, and maintenance-write behavior change. Public `/v1/*`
  JSON bodies, the SQLite schema, cache representation, dependency resolution,
  and golden retrieval outputs are unchanged; a minor release accurately
  describes the internal-API and runtime delta.
- diff inventory: PASS. All **40** paths in `v0.10.3..v0.11.0` are classified
  exactly once in `STATE.md`: five release/public-documentation paths, one
  architecture path, four core runtime/store paths, four shell runtime paths,
  four executable verifier/test paths, one evidence-configuration path, 15
  durable-evidence paths, and six operating/state/task records.
- architecture reconciliation: PASS. `ARCHITECTURE.md §6` names `/docs` and
  `/embeddings/missing` in the core-SQL HC2 boundary and records their explicit
  sector-set, empty-fail-closed behavior. HC1 still says a rewritten shell can
  bypass or falsify the shipped `/attest` handoff, so A4 remains open.
- version authorities: PASS. Rust package, Python package, FastAPI literal,
  `STATE.md`, and newest changelog heading all read 0.11.0. Cargo mechanically
  changed only the local `cored` package version in `Cargo.lock`; no dependency
  resolution moved. `./run version-check` matched the exact annotated HEAD tag.
- candidate acceptance: PASS. Before the release commit, `./run ci-local`
  passed **19/19** with 119 workspace tests, 21 net tests, warning-denied
  builds, clippy/fmt, locked Rust 1.78, 191 Python 3.11 shell tests, golden
  **11/11**, protected databases **2/2**, all **54/54** pins, persisted
  fingerprints, and lifecycle auditors. The independent Python 3.12.13 lane
  passed **191/191**; both interpreters verified **21/21** exact packages.
- golden-E2E delta: none. The required standalone `./run golden` passed
  **11/11** with every exact anchor unchanged.
- protected artifact delta: none. All **54/54** file pins matched and both
  protected databases remained exact **2/2** with unchanged corpus facts.
- carried v0.10.2 disposition: PASS. Local annotated tag object
  `d821f8b2eb6f39fe4a7d06a88cd61de771c7b0ba` still dereferences to
  `7d127abac0b993c9e98294ee1c03ff01153de9d0`; v0.10.2 remains local,
  unpublished, and unmoved.
- final closure audit: PASS after one restricted-sandbox non-result. The first
  closed-state `./run ci-local` completed every non-shell lane but denied
  loopback socket creation and `ps` access to eight shell tests with
  `Operation not permitted`; those were environment refusals, not product
  assertion failures. The exact rerun with the required system access passed
  all **19/19** jobs. `cycle-check` reported v0.11 closed with nine closed
  execution runbooks; `checklist-audit` resolved **88/88** checked tasks with
  zero exemptions; `progress-check` resolved R-CLOSE to the release commit;
  `version-check` matched the exact HEAD tag; all **54/54** pins and protected
  databases **2/2** matched. The independent Python 3.12.13 lane passed
  **191/191** and **21/21** packages, and the final standalone golden remained
  **11/11**.
