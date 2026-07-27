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
