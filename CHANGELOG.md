# Changelog

All notable changes to intel-platform releases are recorded here.

## Unreleased

## v0.15.6 — 2026-07-29

### Fixed

- Release closing now uses the executable two-commit protocol selected in
  v0.22. Release commit `R` carries release edits, immediate child `C` carries
  the complete closed-cycle record naming `R`, and the annotated release tag
  targets `C`. The record no longer predicts its own commit or later tag-object
  hash.
- `cycle-check` verifies the annotated tag type, `R` as `C`'s immediate parent,
  and the closed runbook in the tagged tree. Descendants require one dated
  forward record pinning the tag object, closing commit, and hosted run.
- R12 now has thirteen reconstructible fail-before mutations within the
  repository's **12 rules / 36 controls**. They cover the tagged-close shape,
  tag type, parent and tree agreement, live-header release assertion, and
  complete fresh post-push record in addition to the legacy publication rules.

### Documentation and controls

- v0.22 records the fourth member of one publication-control failure family:
  v0.19's unsatisfiable rule, v0.20's two silent unavailable-input paths,
  v0.21's vacuous pattern, and v0.22's self-referential closing fields. E0's
  field enumeration corrects the v0.21 record's narrower diagnosis as a step
  ordering problem.
- Local annotated `v0.8.0` and `v0.10.2` tags and their commit targets are
  valid; complete remote enumeration lacks both. The historical records remain
  correct, retractions remain three, and hosted local-tag verification stays
  skipped until both exact objects are published and a full hosted check passes
  or contrary evidence drives a forward correction.
- Manifest growth remains accepted with bounds: v0.22 adds the expected
  fifteen authenticated evidence pins, bringing the manifest to **221** total
  (**219** evidence plus **2** authorization), still far below its 1 MiB
  retention trigger.
- The hosted Node-runtime disposition is forward-corrected. GitHub's
  2025-09-19 announcement had already named 2026-06-16 before the disposition
  was written, so its supposed pending trigger was already satisfied. The
  migration is scheduled for v0.23 rather than changing the measured v0.22
  candidate; all seven current jobs are green while the runner forces Node 24.
- The same v0.23 workflow-maintenance pass must replace the fully floating
  `dtolnay/rust-toolchain@master` ref and add an operating-contract rule that a
  recorded trigger includes the measurement showing it has not already fired.

### Evidence and disposition

- Authenticated candidate run `30443692105` attempt 1 passed all seven
  executable jobs at exact candidate
  `10c78119cd10eeb17a01152de6b6f0c322b2b91e`: workspace **133**, net **55**
  (**29** `intel-ingest` + **26** `cored`), invariant-scan **12/12 rules / 36
  controls**, R10 **45** exemptions, and golden **11/11**. Each hosted shell
  lane collected **266** as **265 passed / 1** declared on-site-only skip,
  matching the local 266-test inventory.
- The release-grade deferred audit accepted seven authenticated receipts with
  zero rejected, and measured **5 deferred / 2 promoted / 0** implemented
  deferred subsystems. Its 34,816-byte report is pinned at SHA-256
  `7fc1b09004d1cb8e835cf90bd3d11bf68e856c4d56bb2c9564a7fdbf77abced0`.
- Publication was explicitly selected as **release as of 2026-07-29**. The
  trigger is Option C itself: planted failures prove the checker rejects
  violations, but only a real two-commit close, annotated tag over `C`, atomic
  publication, and dated forward append prove the protocol composes. Without
  publication, the claimed protocol and G3 correction would remain
  unexecuted.
- No `/v1/*` route or response body, schema, dependency, runtime behavior,
  robots policy, configured source, or protected database changed, so v0.15.6
  is patch-compatible.
- A4, editable L1, the R3/R4 open-bottom limits, active-runbook measured-value
  heuristic, T7, negative-cache Decision B, and L2 remain open. `arxiv-cs`
  remains the sole real publisher; the other three configured sources remain
  fixtures.

## v0.15.5 — 2026-07-29

### Fixed

- Publication reconciliation can no longer pass by examining no immutable-tag
  assertion. The live status header must contain both the annotated tag object
  and peeled release commit in the required narrow grammar; zero matches are a
  named error, and every found value must equal the measured ref.
- The fix deliberately preserves the ``[^`\n]`` capture boundary. Allowing
  intervening backticks would let an unrelated hash satisfy the assertion and
  recreate the same silent class after another rephrasing.
- Registered invariant R12 invokes the real `check_publication_status` entry
  point over nine planted cases. Seven independently reconstructible
  `fail_before` mutations disable the mutable-ref prohibition, both
  required/fresh immutable-ref families, pending-publication refusal, missing
  tag ref, missing peeled target, and unavailable ancestry; all seven must be
  detected.
- Release-object mismatch continues to mask later derived publication findings
  intentionally. Until the measured object and target agree with the closed
  record, pending and freshness conclusions depend on an untrusted identity.
  A focused combined case proves exactly one root-cause error.

### Documentation and controls

- This is the third member of one failure family: v0.19 specified an
  unsatisfiable publication rule, v0.20 left two unavailable-input paths as
  silent no-ops, and v0.21 found a live pattern that matched nothing. The
  common cause was that the checker rules were not themselves subject to the
  planted-failure discipline used elsewhere in the repository. R12 closes that
  class for every current publication-status rule.
- G6 remains an accepted bounded conservative refusal, not a reopened design
  question. The 240-character live-header proximity expression may false-fire
  loudly but cannot create a false pass.
- The published-tree audit found that v0.20's closing record was absent from
  its own release commit. Publishing v0.15.5 carries that forward correction,
  but the same ordering reproduces the v0.21 instance: the post-push hosted run
  cannot be recorded until after the release commit is published. The v0.22
  subject is a two-phase close based first on already-existing candidate hosted
  evidence, followed by a dated post-push confirmation.
- The ordering defect originates in the v0.20 runbook's R-CLOSE sequence,
  which required post-push hosted confirmation before checking the box and
  writing the closing record. It is a runbook fixed point, not an
  implementation defect in `cycle_check.py`.
- Missing remote historical tags are a separate v0.22 release-identity item.
  The v0.8, v0.8.1, and v0.10.2 records name annotated `v0.8.0` and `v0.10.2`
  tags that remote inspection did not find. Before changing records or remote
  refs, v0.22 must establish whether those tags exist locally, were deleted,
  or were never created. Hosted CI cannot settle this because its lifecycle
  check deliberately skips local tag verification.

### Evidence and disposition

- Authenticated run `30432249637` attempt 1 against evidence candidate
  `3f61aed183e195ccaf952cbc7f4528712bab028d` passed all seven derived
  identities with zero rejected receipts: workspace **133**, net **55**
  (**29** `intel-ingest` + **26** `cored`), invariant-scan **12/12 rules /
  30 controls**, R10 **45** exemptions, and golden **11/11**. Both hosted shell
  lanes collected **258** as **257 passed / 1 declared on-site-only skip**,
  matching the local **258-test** inventory at the same commit.
- The authenticated release-posture audit measured **5 deferred / 2 promoted /
  0 deferred subsystems implemented**. Its report is SHA-256
  `5e39cb000b08c6191d19f3ea91a90c6c89dc0680f0e76aed1e14523b2c06562a`
  at **34,714** bytes. All **206** pins are exact: **204** evidence plus **2**
  authorization surfaces.
- Publication was explicitly selected as **release as of 2026-07-29**. No
  publication trigger was visible at entry because published v0.15.4 was
  green. The measured trigger emerged at E0: replacing the asserted tag object
  with forty zeroes in the published header's own live phrasing still returned
  `errors=[]`. The published artifact therefore claimed a passing control that
  examined nothing; without this release, published `main` would continue to
  ship that false capability and could not carry G3's forward correction.
- No `/v1/*` route or body, schema, dependency, crate source, runtime behavior,
  robots policy, configured source, or protected database changed, so v0.15.5
  is patch-compatible.
- Retractions remain three. A4, the editable-L1 controller residual, the R3/R4
  bounded open-bottom scanners, the active-runbook measured-value heuristic,
  T7 robots single-flight, and the last-known-good fallback remain open; L2
  remains scheduled.
- This platform still aggregates one publisher: `arxiv-cs` is real and three
  of four configured sources are `example.org` fixture placeholders. Adding a
  second publisher remains a separate product and compliance decision.

## v0.15.4 — 2026-07-29

### Fixed

- Publication status no longer requires a commit to predict the mutable
  `origin/main` value that publishing that same commit creates. The live
  status header carries only immutable annotated-tag object and peeled-target
  facts; dated body records retain exact mutable-ref measurements.
- The correction fails closed when its inputs are unavailable. Missing tag
  refs, missing peeled targets, and unavailable ancestry each produce a named
  `cycle-check` defect. The existing rule that rejects a reachable release
  while the live header calls publication pending is unchanged.
- This was a specification defect in the v0.19 runbook, not an implementation
  defect in `tools/cycle_check.py`: the tool faithfully implemented the
  requested self-referential rule. Adding the v0.19 control was still correct;
  it first caught the repository's real false publication status before its
  own fixed point appeared.

### Documentation and controls

- The closed-cycle Repomix exclusion now covers v0.6 through v0.11. The
  measured inclusion diff removed only `TASKS-v0.6.md` and
  `TASKS-v0.7.md`; no repository source file was deleted.
- `./run export-check` generates from the project root, derives the tracked
  source set from `git ls-files`, and requires the release-control roots
  without pinning a count. Failure-capable controls prove that a non-root run
  loses `Cargo.lock` and that enabling Repomix's security pass silently omits
  `crates/ingest/src/lib.rs`.
- `AGENTS.md` now preserves both measured operating rules: review exports run
  from the project root and `enableSecurityCheck` remains `false`. Registered,
  self-testing invariant R4 remains the credential control.
- Forward publication audit `72b6f42` was intentionally held after v0.15.3
  and is included in this cycle's publication history rather than pushed out
  of band.

### Evidence and disposition

- Authenticated run 30423736121 attempt 1 against evidence candidate
  `8230d4f24f565afcde92931c987adff4339036af` passed all seven derived
  identities with zero rejected receipts: workspace **133**, net **55**
  (**29** `intel-ingest` + **26** `cored`), invariant-scan **11/11 rules /
  23 controls**, R10 **45** exemptions, and golden **11/11**. Both hosted
  shell lanes collected **255** as **254 passed / 1 declared on-site-only
  skip**, matching the local **255-test** inventory at the same commit.
- The authenticated release-posture audit measured **5 deferred / 2 promoted /
  0 deferred subsystems implemented**. Its report is SHA-256
  `b90b2f00d8129f17c09e48e2bdefb2d48d97f5d502e2723b8a5e2d0a5d25d00e`
  at **34,608** bytes. All **191** pins remain exact: **189** evidence plus
  **2** authorization surfaces.
- Publication was explicitly selected as **release as of 2026-07-29** because
  published `main` was failing CI on the status control this release corrects.
  A tooling-only cycle would otherwise have been eligible for no release; the
  red published head is the release trigger. No `/v1/*` route or body, schema,
  dependency, crate source, or runtime behavior changed, so v0.15.4 is
  patch-compatible.
- Retractions remain three. A4, the editable-L1 controller residual, the R3/R4
  bounded open-bottom scanners, the active-runbook measured-value heuristic,
  T7 robots single-flight, and the last-known-good fallback remain open; L2
  remains scheduled.
- This platform still aggregates one publisher: `arxiv-cs` is real and three
  of four configured sources are `example.org` fixture placeholders. Adding a
  second publisher remains a separate product and compliance decision.

## v0.15.3 — 2026-07-29

### Fixed

- `RobotsCache` now selects cache lifetime by exhaustive `Policy` variant:
  successful `Gate(_)` and definitive `Unavailable` results retain the
  24-hour policy TTL, while transient `Unreachable` results use the production
  five-minute negative TTL wired by `cored`.
- The gate remains fail-closed while an unreachable result is cached. This
  correction deliberately makes a failing origin eligible for another
  `/robots.txt` request at most once per 300 seconds instead of once per 24
  hours, bounded by ingest frequency and by the shared politeness limiter that
  `policy_for` acquires. A day-long denial caused by one dropped packet was
  arbitrary rather than conservative.
- An unreachable refresh still overwrites an expired last-known-good policy.
  Reusing stale policy remains deferred until a measured live transient outage
  affects an admitted publisher while a usable last-known-good policy exists,
  followed by explicit operator authorization.

### Removed

- The unsupported `diagnostics` and `robots-preview` Cargo features and the
  robots-only preview binary have been retired. They shipped inside v0.15.2,
  so consumers that selected either feature must remove it; the public
  `/v1/*` API is unchanged, and the behavior correction remains patch-scoped.

### Documentation and controls

- Publication status is now reconciled by `cycle-check`; its executing
  fail-before proved that the project's prior false remote-main/tag status had
  passed every existing check.
- The review export excludes evidence bodies and the selected closed-cycle
  records, archives old `STATE.md` history losslessly, and disables Repomix's
  security scan because it silently omitted a Rust source. Registered,
  self-testing invariant R4 remains the credential control.
- Three export-control omissions remain explicit v0.20 work: the exclusion
  pattern misses `TASKS-v0.6.md` and `TASKS-v0.7.md`; no derived
  `export-check` executes the expected `git ls-files` source set; and
  `AGENTS.md` does not yet require root execution or preserve the reason
  `enableSecurityCheck` must remain off.

### Evidence and disposition

- Authenticated run 30414648482 attempt 1 against evidence candidate
  `197e93effe9a6abf9c59488a9849c6dcda47646c` passed all seven derived
  identities with zero rejected receipts: workspace **133**, net **55**
  (**29** `intel-ingest` + **26** `cored`), invariant-scan **11/11 rules /
  23 controls**, and golden **11/11**. Both hosted shell lanes collected
  **248** as **247 passed / 1 declared on-site-only skip**, matching local
  **248/248** at the same commit.
- The authenticated release-posture audit measured **5 deferred / 2 promoted /
  0 deferred subsystems implemented**. Its report is SHA-256
  `3006f9ed8641cbc6483a2a1608c65da52ff008e59837218997f207a7cf588b2e`
  at **34,530** bytes. All **176** pins remain exact: **174** evidence plus
  **2** authorization surfaces.
- Publication was explicitly selected as **release as of 2026-07-29** because
  the negative-cache correctness defect changes production behavior received
  by a consumer of the artifact. The defect was bounded fail-closed
  availability loss, not a publisher-policy violation and not cosmetic;
  retractions remain three.
- This platform still aggregates one publisher: `arxiv-cs` is real and three
  of four configured sources are `example.org` fixture placeholders. Adding a
  second publisher remains a separate product and compliance decision.
- A4, the editable-L1 controller residual, the R3/R4 bounded open-bottom
  scanners, the measured-value heuristic, T7 robots single-flight, and the
  last-known-good fallback remain open; L2 remains scheduled.

## v0.15.2 — 2026-07-28

### Fixed

- `harvest-arxiv` no longer claims that its managed `cored` process remains
  available after the command returns. It reports the durable observation
  database and runtime log, then calls `cmd_down`; an executing fail-before
  control proves removal of that shutdown is detected.
- Publication is triggered by that false claim in the published v0.15.1 tree,
  not merely by the runbook's mechanical patch default. The tagged `run` is
  **41,959** bytes at SHA-256
  `7351f2ffb7eb6def34c99c812a61a10690b6f690e9e1e44cee88790ca6dcc455`
  and contains the false “cored still running … for inspection” line.

### Diagnostic and default-build scope

- No default-build compliance behavior changed. ORIGIN-CASE correctly shipped
  nothing after E0 proved `reqwest::Url` normalizes authority bytes before the
  gate; the matcher diagnostics and robots-only preview are excluded unless
  the `diagnostics` / `robots-preview` features are selected. The only
  default production behavior change is the `run` lifecycle correction above.
- The feature-gated preview ships inert and unsupported. It becomes a supported
  product or operator surface only after an operator names an owner and
  explicitly promotes the feature pair; neither condition is met in this
  release.

### Wire verification

- The first real publisher-policy preview requested only arXiv
  `/robots.txt`. It received the recorded **11,083-byte** HTTP 404 response,
  SHA-256
  `fe5a8ce88b89f96db55e8d9a7eb3d978f3d364bf31d48c4880422511e9035ab2`;
  the source's absence-only opt-in allowed the configured OAI-PMH target.
- The first harvest run under a gate that enforces the policy it claims
  ingested **2,692** real arXiv documents across three pages into a fresh,
  ignored observation database. It followed two `resumptionToken`s, persisted
  a final null cursor with high-water date 2026-07-28, and changed no protected
  or golden corpus byte.
- All wire facts were observed under crawler identity
  `intel-platform/0.15.1`. The v0.15.2 release head emits
  `intel-platform/0.15.2`, so a re-run cannot reproduce that versioned
  User-Agent line. The stable `intel-platform` product token is unchanged, and
  arXiv served no policy group whose selection could differ.

### Evidence and disposition

- Authenticated run 30369139464 attempt 1 against evidence candidate
  `2ce912dca181e5e7b949a4b2e6fd8487412388f9` passed all seven derived
  identities with zero rejected receipts: workspace **131**, net **55**
  (**29** `intel-ingest` + **26** `cored`), invariant-scan **11/11 rules /
  23 controls**, and golden **11/11**. Both hosted shell lanes collected
  **245** as **244 passed / 1 declared on-site-only skip**, matching local
  **245/245** at the same commit.
- The authenticated release-posture audit measured **5 deferred / 2 promoted /
  0 deferred subsystems implemented**. Its report is SHA-256
  `78901f2d181672f2a0ec073c18ec5bb02c68762de0fc7362b49f903ed6509448`
  at **34,520** bytes. All **161** pins remain exact: **159** evidence plus
  **2** authorization surfaces.
- Publication was explicitly selected as **release as of 2026-07-28** because
  F1 is a verified false claim in v0.15.1 and its zero-risk forward correction
  has an executing regression. The bounded v0.15.1 robots incident affected no
  configured live URL or historically observed redirect; retractions remain
  three.
- This platform currently aggregates one publisher: `arxiv-cs` is real and
  three of four configured sources are `example.org` fixture placeholders.
  Adding a second publisher is an open product question for a later cycle and
  remains a separate compliance decision.
- A4, the editable-L1 controller residual, the R3/R4 bounded open-bottom
  scanners, the measured-value heuristic, and T7 robots single-flight remain
  open; L2 remains scheduled.

## v0.15.1 — 2026-07-28

### Fixed

- Publisher robots policy now evaluates the complete request path plus query,
  excludes the client-only fragment, and re-runs that derivation before the
  first document request and every redirect. From v0.8.0 through v0.15.0 the
  gate could supply only the first path segment, so multi-segment or
  query-specific publisher rules could be weakened; single-segment rules
  remained enforced.
- The failure-capable raw-wire net fixture bypasses ambient loopback proxies,
  making its byte-identical request assertion deterministic without weakening
  the double.
- `harvest-arxiv` verifies protected artifacts before environment setup,
  reachability probing, or any publisher request.

### Verification

- R11's declared four-spelling scope is exercised by five reconstructible
  controls: both direct config paths, both environment names, and an
  environment-derived module-local variable. The v0.16 control-breadth
  limitation is closed without claiming unknown future spellings.
- Authenticated run 30357365420 attempt 1 against evidence candidate
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394` passed all seven derived
  identities with zero rejected receipts: workspace **131**, net **55**
  (**29** `intel-ingest` + **26** `cored`), invariant-scan **11/11 rules /
  23 controls**, and golden **11/11**. Both hosted shell lanes collected
  **244** as **243 passed / 1 declared on-site-only skip**, matching local
  **244/244** at the same commit; the ingest net leg was **29/29** both hosted
  and local.

### Evidence and disposition

- The patch trigger fired because no observable route, response body, or
  schema moved; this release corrects behavior within the existing surface.
  The signed receipts retain their provisional `candidate/v0.16.0` source ref
  and pin the candidate commit, not the branch's proposed version.
- The version-corrected offline release-posture audit accepted **7/7**
  attestations with zero rejection and measured **5 deferred / 2 promoted**.
  Its report is SHA-256
  `d73b198e4bb04c96273ae53ecef5e81e162a645ee6c0827450fd737fc7c8dbb9`
  at **34469** bytes. All **146** pins remain exact: **144** evidence plus
  **2** authorization surfaces.
- Publication was explicitly selected as **release as of 2026-07-28**. The E0
  audit found no immutable false completeness claim, so the correction is
  forward-only and retractions remain three. The Step 3 acceptance lifts the
  temporary live-harvest suspension.
- A4, the editable-L1 controller residual, the R3/R4 bounded open-bottom
  scanners, the measured-value heuristic, and T7 robots single-flight remain
  open; L2 remains scheduled.

## v0.15.0 — 2026-07-28

### Added

- Authenticated internal `POST /entities/unknown` moves gazetteer comparison
  behind the core-owned configuration seam. The shell still extracts model
  candidates, while core compares them against the gazetteer it actually
  loaded and returns only the unknown subset.
- R11 rejects production shell reads of core-owned configuration spellings.
  Its current single reconstructed failure proves the rule can fire; its
  broader declared spelling coverage remains an explicit open limitation and
  is the first task for v0.17.

### Changed

- All execution runbooks and progress logs now live under `docs/cycles/`,
  resolved through one shared cycle-identity implementation. Historical file
  bytes remain unchanged.
- R10's 45 exemptions are parser output rather than a name-pinned input:
  18 runner setup actions + 24 terminal receipt/attestation actions + 1
  constrained Python installation + 1 report-only job + 1 named
  operator-local protected-database residual.
- Rust test fixtures resolve from the runtime checkout. A relocated checkout
  reused a shared, uncleared Cargo target without recompilation and passed all
  126 workspace tests.

### Fixed

- `ci-local` now runs every one of its 20 derived jobs in a separate
  `bash -euo pipefail` process, so a failed command cannot be converted into a
  PASS by the wrapper call site.
- Fingerprint verification preserves the first validation failure while still
  cleaning up, and reports cleanup failure only when no earlier failure
  occurred.

### Evidence and disposition

- The new authenticated internal `/entities/unknown` route fired the minor
  release trigger. The selected release identity is `v0.15.0`.
- Authenticated run 30347262430 attempt 1 against evidence candidate
  `43706216c06608039d9c3e7ef2b86024b22d4a79` passed all seven derived
  identities across six blocking jobs with zero rejected receipts: workspace
  **126**, net **49** (**23** `intel-ingest` + **26** `cored`),
  invariant-scan **11/11 rules / 19 controls**, and golden **11/11**. Each
  hosted shell lane collected **243** tests as **242 passed / 1 intended
  on-site-only skip**, matching the local candidate's **243 passed**.
- The release-grade audit measured **5 deferred / 2 promoted**. The protected
  manifest contains **131 exact pins**: **129 evidence** plus **2
  authorization surfaces**.
- Publication was explicitly selected as **release as of 2026-07-28**. The
  hosted workflow never enters `ci_local_job`, so the pre-v0.15 local harness
  defect makes no published count false and no retraction is owed. Retractions
  remain three.
- A4, the editable-L1 controller residual, the R3/R4 open-bottom limitations,
  the active-runbook measured-value heuristic, and R11's control-breadth gap
  remain open.

## v0.14.1 — 2026-07-28

### Added

- R10 derives normalized verification scope from the local `ci-local` entry
  points and the blocking hosted workflow, then checks parity in both
  directions with three site-specific reconstructed failures.
- The deferred auditor derives its seven blocking receipt identities from
  `.github/workflows/ci.yml`; report-only status is determined by job-level
  `continue-on-error: true`, and narrowing below protected historical evidence
  is rejected.
- A cross-language source test derives every Rust `diagnostic_delay("…")`
  stage and requires it to appear in the Python benchmark header map.

### Changed

- Hosted Python 3.11 now executes `checklist-audit` and `progress-check`,
  matching their local entry points without changing the six-job blocking
  topology.
- Active-runbook criteria that explicitly cite another step's stored
  measurement are rejected by a documented vocabulary heuristic; same-commit
  invariant relations remain valid.
- Closing dispositions are dated, and the operating contract requires command
  behavior claims to be checked at the command's actual entry point.

### Evidence and disposition

- Step 4 retained all four observable diagnostic stage names. The
  `x-intel-view-stage-*` header set and stage strings remain identical to
  v0.14.0, firing the patch-release identity `v0.14.1`.
- Authenticated run 30333331839 attempt 1 against evidence candidate
  `6d197e562315b4fc6feb20c35b5fadc75b6b44a4` passed all seven derived
  identities: workspace **125**, net **48** (**23** `intel-ingest` + **25**
  `cored`), invariant scan **10/10 rules / 18 controls**, and golden
  **11/11**. Each hosted shell lane collected **237** tests as **236 passed /
  1 intended on-site-only skip**, matching the local candidate's **237
  passed**.
- The release-grade audit accepted seven authenticated receipts with zero
  rejection and measured **5 deferred / 2 promoted**. The protected manifest
  contains **116 exact pins**: **114 evidence** plus **2 authorization
  surfaces**.
- Publication was explicitly selected as **release as of 2026-07-28**. Public
  `/v1/*` bodies, the SQLite schema, diagnostic stage names, and golden
  behavior are unchanged. A4, the editable-L1 controller residual, the R3/R4
  open-bottom limitations, and the active-runbook heuristic limitation remain
  open.

## v0.14.0 — 2026-07-28

### Added

- R8 proves that production crawler-identity construction precedes the sole
  listener bind, with three site-specific reconstructed failures.
- R9 proves that the `test-support` fault-injection feature is reachable only
  through a dev-dependency edge, with a reconstructed production-edge failure.
- Active runbooks must assign every non-`none` deferred action to an existing
  step and must include RE-MEASURE when the release commit changes.

### Changed

- Every invariant control now asserts the file and line of its planted
  failure. R1 is an allow-list over the five production canonical-identity
  callers; R3 and R4 remain explicitly bounded open-bottom deny-lists rather
  than claiming universal absence.
- The focused invariant pytest parameterization derives its rule ids from the
  registry and rejects incomplete rule coverage, so registering a later rule
  cannot silently leave its controls unexecuted.
- The existing `/view` diagnostic delay remains bounded to 10,000 ms, is
  documented as benchmark-only, and now emits a startup warning naming both
  raw settings and the effective delay whenever either setting is present.

### Fixed

- Site-ambiguous invariant controls can no longer pass after firing at the
  wrong source location.
- The runbook template no longer permits an active deferred action with no
  named step responsible for discharging it.
- The v0.14 review claim that no hosted job emitted invariant self-test output
  was disproved: no-argument execution enters self-test, and retained v0.13
  hosted output ends
  `invariant-scan: SELF-TEST PASS (7/7 rules, 11 controls)`. No fourth
  retraction exists; the valid retraction count remains three.

### Evidence and disposition

- DIAGNOSTIC-KNOB option (b) added a startup warning and code change, firing
  the `v0.14.0` trigger; this choice is not an R-CLOSE default.
- Authenticated run 30324186389 against evidence candidate
  `ee9ee0f9ed96cb2cb7759c3c3e59fbf8f325ae1a` passed all seven identities:
  workspace **125**, net **48** (**23** `intel-ingest` + **25** `cored`),
  invariant scan **9/9 rules / 15 controls**, and golden **11/11**. Each hosted
  shell leg reported **224 passed / 1 skipped** because the on-site production
  measurement test intentionally skips without protected corpora and a built
  `cored`; local lanes passed **225/225**.
- The release-grade audit accepted seven authenticated receipts with zero
  rejection and measured **5 deferred / 2 promoted**. The protected manifest
  contains **101 exact pins**: **99 evidence** plus **2 authorization
  surfaces**.
- Publication is not authorized. The named publication trigger is a separate
  operator authorization to advance `origin/main` and create the annotated
  `v0.14.0` tag; it has not fired.
- Public `/v1/*` bodies, the SQLite schema, and golden behavior are unchanged.
  A4 and the editable-L1 controller residual remain open; L2 remains scheduled.

## v0.13.0 — 2026-07-27

### Added

- Every registered invariant rule now carries an executable fail-before
  mutation. Local CI reconstructs each mutation in a disposable source tree,
  requires exit 1, and verifies the rule-specific failure text. Hosted run
  30277584129 reconstructed all 11 controls and passed 7/7 registered rules.
- R7 enumerates every production caller of document-by-id body hydration,
  permits only the sector-scoped method, and refuses any renewed public
  unscoped store seam.
- The existing net CI job invokes all 24 `cored --features net` tests in
  addition to 23 `intel-ingest` net tests, without adding a local or hosted job
  identity. Hosted run 30277584129 read both invocations from the log and
  passed **24/24** cored plus **23/23** ingest tests.

### Changed

- Net-enabled `cored` startup requires a non-placeholder
  `INTEL_CRAWLER_CONTACT`. The structural `intel-platform` robots token remains
  fixed, its advertised version is derived from the crate version, and the
  byte-identical identity is used by both HTTP clients and `RobotsCache`.
- Production canonical-id rematerialization no longer accepts a distance
  parameter. R5 is now an allow-list over production call sites requiring the
  private `DEDUP_MAX_DISTANCE` source directly.
- Crawler identity installation now uses one atomic process-global
  initialization and compares the installed bytes with the request. Identity
  and robots-cache construction occur in `main()` startup, so unrelated
  `AppState` tests do not install crawler configuration.

### Fixed

- Published `v0.12.0` returned attestation violations naming documents outside
  the caller's sector set: a finance-scoped request named `science::b`. The
  exposure was a cross-sector existence-and-16-token-match oracle, not a
  document-body leak. `v0.13.0` closes it by binding `/attest` hydration to the
  caller's sector set in core SQL.
- Final `/retrieve` hydration and `/attest` now bind the shell-decided sector
  set in core SQL. The internal `/attest` endpoint intentionally returns the
  same `400 unknown context document id` response for an out-of-sector id and a
  nonexistent id, removing the former cross-sector existence/match oracle.
- The v0.12 R5 correction could be bypassed by renaming an alternate
  non-numeric threshold. The public maintenance seam was removed and the
  executable invariant now binds every production call to the one private
  threshold.
- The crawler User-Agent installer no longer has a check-then-set race whose
  losing thread could emit `could not install crawler User-Agent`. Concurrent
  identical installers now converge on one identity; different bytes retain
  the established deterministic refusal.

### Retractions and publication disposition

- The v0.12.0 R-CLOSE HC2 claim is retracted as **falsified by measurement**,
  not merely contradicted by source reading: the entering-state finance-scoped
  `/attest` probe returned a violation naming the out-of-sector
  `science::b`. BODY-BOUNDARY and R7-BODY-SECTOR correct the claim forward.
- The operator authorized `v0.13.0` because the UA-CONTACT trigger landed;
  the correction-only `v0.12.1` alternative therefore does not apply.
- **Publication trigger:** the operator separately authorized publication of
  `v0.13.0` on 2026-07-27 after accepting IDENTITY-INSTALL and RE-MEASURE.
  Evidence candidate `7faaa4e1271616ff9390111c863d12fbcfa4d2fd`
  remains distinct from the later release commit. Hosted run 30277584129
  passed all seven identities; its release-grade audit accepted all seven
  signed receipts with zero rejection. The release contains **86 exact pins**:
  **84 evidence files** plus **2 authorization surfaces**.
- A4 remains open because a rewritten shell can bypass or falsify the trusted
  `/attest` handoff. L1 remains client-side defense; an edited controller can
  rewrite it, and the server-enforced L2 forced-command wrapper remains open
  and scheduled.

## v0.12.0 — 2026-07-27

### Added

- A registered invariant scanner with executable R1–R6 rules, captured planted
  failures, local CI job 20, and hosted execution inside the Python 3.11 shell
  leg. The rules cover the production canonical-threshold seam, core bind path,
  core LLM-client absence, tracked credential boundary, single private distance
  constant, and mirrored model-profile authorization text.
- A guarded `./run models status|intel|athenaeum|athenaeum-bulk|stop` operator
  surface. Its L1 controller builds commands from a structured allowlist for
  exactly five named containers and the documented read-only probes.
- Pure, failure-capable model-profile guards for incomplete container
  inventories, foreign listeners, non-ready health results, and managed,
  absent, stale, or unreadable control sockets.
- Retraction-aware checklist auditing and a permanent forward correction for
  the false v0.11.0 canonical-threshold criterion.

### Changed

- Non-paged document append and corpus-wide canonical rematerialization now
  share one SQLite transaction, so a rematerialization failure returns HTTP 500
  without leaving appended rows or advancing view generation.
- Production canonical rematerialization selects its threshold only inside the
  store; the caller-supplied threshold seam remains test-only.
- Tracked infrastructure policy now treats credentials—not documented private
  LAN coordinates—as the enforceable disclosure boundary.
- Authorization-surface hashes join evidence-file hashes in protected-artifact
  manifest schema 2.

### Fixed

- v0.11.0 shipped a threshold-source defect: STORE-IDENTITY claimed one shared
  `max_distance` constant while the production ingest handler separately passed
  literal `16`. v0.12 INGEST-ATOMIC and THRESHOLD-ONE correct that claim
  forward; the published v0.11.0 tag and its evidence remain unchanged.
- A failed non-paged canonical rematerialization can no longer durably append
  documents while leaving the prior view generation in place.
- Model-profile parsing and transition decisions now fail with structured
  refusals instead of exposing bare parsing errors or silently routing around
  unsafe observed state.

### Publication and carried dispositions

- The operator selected and authorized v0.12.0 rather than a correction-only
  v0.11.1. The correction half alone could have been a patch, but the same
  release adds the `./run models` operator surface and changes `/ingest` failure
  semantics; one minor release accurately names the combined shipped change.
- Hosted run 30253646597, attempt 1, passed all seven expected jobs at exact
  evidence candidate `d664a7d3c524a3dfab932e158d9545953844b8dd`.
  The release audit accepted seven distinct authenticated receipts with zero
  rejection, measured five deferred / two promoted rows, and recorded
  exact-cosine p95 at 10.324209 ms for 2,600 documents.
- Real hosted controls rejected a persisted failed-core receipt and a duplicate
  `python=3.11`/missing-`python=3.12` shell matrix, accepting zero executions in
  each case. The admitted report, receipts, and Sigstore bundles bring immutable
  evidence to 69/69 pins; both authorization-surface pins also match.
- v0.11.0 remains published with the known threshold-source defect named above;
  its tag, release commit, receipts, report, and 54 pins are unchanged.
- A4 remains open because a rewritten shell can bypass or falsify the trusted
  `/attest` handoff. Model-profile authorization is L1 client-side defense only:
  an edited controller can rewrite it, and the L2 server forced-command wrapper
  remains scheduled for the next authorized server session.

## v0.11.0 — 2026-07-27

### Added

- Structural loopback-only startup validation for every resolved `CORE_BIND`
  address, with refusal before configuration, archive setup, or listener bind.
- Explicit sector sets on `/docs` and `/embeddings/missing`, enforced by bound
  predicates in core SQL and empty-set fail-closed behavior.
- Failure-capable coverage for duplicate robots groups, percent-equivalent
  paths, crawl-delay timing, missing publisher policy, billing rollback, and
  canonical identity after edits and takedowns.

### Changed

- Same-specificity robots groups now merge in file order while a specific
  product match remains isolated from generic `*` rules; multiple applicable
  crawl delays use the conservative maximum.
- Robots patterns and request paths normalize unreserved percent triplets
  without decoding reserved delimiters or turning encoded literals into
  wildcards.
- Crawl-delay changes update the existing per-host limiter in place, preserving
  its clock and acquisition counter; network ingestion without a publisher
  policy cache now fails closed.
- Billing batches validate against detached state before publishing once, and
  successful document maintenance rematerializes corpus-wide canonical identity
  in the same SQLite transaction.

### Fixed

- Non-loopback or mixed-resolution core binds can no longer expose unauthenticated
  internal endpoints.
- Internal document enumeration can no longer escape the core's sector boundary.
- A later invalid billing event can no longer leave an earlier entitlement
  mutation live in memory or persist it through an unrelated save.
- Document edits, publication-order changes, and canonical-row deletion can no
  longer leave stale or dangling `canonical_id` values.

### Publication and carried dispositions

- The operator selected a minor release because `/docs` and
  `/embeddings/missing` gain required internal query parameters and bind,
  robots, billing-failure, and maintenance-write behavior changes. Public
  `/v1/*` JSON bodies, the SQLite schema, cache representation, dependency
  resolution, and golden retrieval outputs are unchanged.
- Hosted run 30236305375 passed all seven expected jobs at exact candidate
  `17221504d0c572e2b52f8509cb720d4a7c72f47d`. The release audit authenticated
  all seven distinct receipts with zero rejection, measured five deferred /
  two promoted rows, and recorded exact-cosine p95 at 15.033417 ms for 2,600
  documents.
- Real hosted controls rejected a persisted failed-core receipt and a duplicated
  `python=3.11` matrix, accepting zero executions in each case. The admitted
  report, receipts, and Sigstore bundles bring immutable evidence to 54/54 pins.
- T7 single-flight, Postgres, pgvector, multi-host seam hardening, and the A4
  untrusted-shell boundary remain deferred. `/view` materialization remains a
  promoted future implementation; this release does not claim to close A4.
- v0.10.2 remains local and unpublished at its original annotated tag object;
  this release does not move or publish it.

## v0.10.3 — 2026-07-26

### Added

- Exact `(job, matrix)` identities for the seven-job hosted evidence set,
  including failure-capable duplicate-leg and failed-job controls.
- Run-scoped durable storage and SHA-256 pins for every accepted receipt and
  Sigstore bundle, plus a release-grade v0.10.3 production audit.
- A semantic historical-evidence registry and one active-cycle identity source
  for lifecycle, report-label, and benchmark tooling.

### Changed

- Release evidence now requires authenticated grade, a pinned workflow
  revision, exact successful single-run matrix coverage, and persisted posture
  that participates in re-derivation.
- Resumed adversarial attempts are revalidated against five one-way classifier
  invariants, their declared target/shape/model, and recorded overlap telemetry.
- Lifecycle checks distinguish strict local annotated-tag verification from
  hosted clones while retaining release-commit, contract-amendment, and stale
  source-literal enforcement.

### Fixed

- Duplicate receipt subjects or digests can no longer satisfy two matrix legs,
  and release-grade evidence cannot be produced in structural-only mode.
- A recorded receipt or bundle path must resolve to indexed, unchanged bytes
  in the named evidence worktree; lossy or fictional durable paths are refused.
- New audit labels no longer embed a stale prior cycle, and the immutable
  v0.10.2 mislabeled report is corrected by annotation without changing bytes.

### Publication and carried dispositions

- Hosted run 30202019640 passed all seven expected jobs at exact candidate
  `a1d8c958b4eaf4fe4add75cc49a7fec341c8f8a5`. The release audit authenticated
  all seven distinct receipts with zero rejection and measured two promoted /
  five deferred rows; exact-cosine p95 was 8.390958 ms.
- Real negative controls rejected the persisted failed-core run and a
  duplicated `python=3.11` shell matrix, accepting zero executions in each
  case.
- v0.10.2 remains local and unpublished at its original annotated tag object;
  this release does not move or publish it.
- This patch release changes release metadata, workflow/evidence integrity,
  lifecycle controls, tests, tools, and durable evidence only. Public and
  internal API behavior, runtime behavior, storage paths, database schema,
  cache representation, licensing outcomes, dependency resolution, and golden
  retrieval outputs are unchanged.

## v0.10.2 — 2026-07-26

### Added

- Authenticated GitHub build-provenance bundles for the complete seven-job
  released-commit matrix, plus a pinned production audit that accepts only
  exact, successful, single-run receipts.
- Cycle-contract regression coverage that rejects stale concrete task or
  progress paths in `AGENTS.md`.

### Changed

- Production deferred audits require an explicit expected HEAD, a clean
  worktree, exact receipt subjects, and the complete hosted job matrix before
  runner execution can be promoted.
- Adversarial-report resume accepts only internally consistent HTTP 200
  completions with the full current schema and stops immediately on any reused
  `LEAK`.
- The operating contract now derives active task and progress paths from its
  declared cycle instead of embedding stale cycle literals in the workflow.

### Fixed

- Receipt ancestry can no longer substitute for exact released-commit
  identity, and failed, partial, hand-authored, or unauthenticated receipt sets
  cannot promote execution evidence.
- Dirty or wrong-subject production measurements now abort before corpus work,
  and malformed or leaking resumed attempts cannot be silently trusted.
- Sigstore bundles persisted with a neutral extension are presented to the
  GitHub verifier through an ephemeral compatible filename without changing
  their authenticated bytes.

### Publication and carried dispositions

- v0.10.1 was published unchanged: remote `main` reached the reviewed Step 5
  audit record, the immutable v0.10.1 tag stayed on its release commit, and
  hosted CI produced seven authenticated successful receipts.
- The fresh v0.10.2 deferred audit records two promoted and five deferred rows,
  accepts all seven authenticated receipts with zero rejection, and measures
  exact-cosine p95 at 8.962542 ms for 2,600 documents.
- The fresh real-model matrix remains 45/45 valid cells as `NOT EXERCISED`,
  with zero `LEAK` and an independent `GUARD FIRED` positive control. T7
  single-flight, Postgres, pgvector, multi-host seam hardening, and the A4
  untrusted-shell boundary remain deferred.
- This patch release changes workflow, evidence integrity, lifecycle controls,
  tests, and release metadata only. Public and internal API behavior, runtime
  behavior, storage paths, database schema, cache representation, licensing
  outcomes, dependencies, and retrieval outputs are unchanged.

## v0.10.1 — 2026-07-26

### Added

- Runner-produced, persisted CI receipts whose commit ancestry is checked
  before they can promote the released-commit execution trigger.
- Corpus-free SHA-256 pins for the corrected deferred-audit receipt and fresh
  real-model adversarial report, plus a blocking source/config/Git
  re-derivation job.
- A guarded on-site test that executes the complete deferred-design production
  audit without requiring protected corpora on hosted runners.

### Changed

- Adversarial evidence counts only target-valid, model-completed attempts,
  retries transport failures without counting them, records graduated
  `n=8/12/16` telemetry, and requires a real-handler positive control.
- The local CI matrix has 19 tracked jobs; the workflow mirrors its new
  evidence re-derivation gate.
- Python constraint drift tests use an explicit synthetic distribution
  inventory while the product verifier continues to inspect the real
  interpreter and reject duplicates.

### Fixed

- The v0.10.1 deferred receipt now measures a clean detached v0.10.0 release
  tree and accepts seven real runner receipts instead of inferring execution
  from Git-remote presence.
- Finder `.DS_Store` files are ignored and the previously tracked copies were
  removed from version control.
- The real-model battery can no longer call a timeout a completed adversarial
  attempt, and the FastAPI pin-drift test cannot be masked by an unrelated
  ambient duplicate distribution.

### Carried dispositions

- The fresh real-model matrix completed 45/45 valid cells as
  `NOT EXERCISED`, with zero `LEAK`; the deployed-path positive control fired
  `GUARD FIRED`. This is an observed resistance result, not a proof that no
  model can reproduce gated text.
- T7 single-flight, Postgres, pgvector, multi-host seam hardening, and the A4
  untrusted-shell boundary remain deferred. CI-runner evidence and future
  `/view` materialization remain the two promoted deferred-audit rows.
- This patch release changes operations, evidence, and tests only. The public
  API, runtime behavior, database schema, cache representation, licensing
  boundary, and retrieval outputs are unchanged.

## v0.10.0 — 2026-07-25

### Added

- Executable active-cycle and checked-task auditors, plus failure-capable
  protected-artifact admission that rejects both byte drift and logical
  provenance drift.
- Reproducible Python 3.11/3.12 constraints, verified locally and on the first
  observed GitHub Actions executions.
- A decomposed `/view` cold-path benchmark and restart-invalidation verifier
  covering every mutation class without adding materialized storage.
- A resumable 45-cell real-model adversarial battery with separate
  failure-capable guard and leak controls.

### Changed

- The internal loopback `/view` response now exposes startup, SQLite-open,
  analysis, response-build, and serialization timing headers. Its JSON body,
  cache representation, public API, and database schema are unchanged.
- Deferred-design auditing now derives every progress input, measures seven
  triggers, and records CI-runner and `/view` promotions without implementing
  the five still-deferred subsystems.
- CI installs from the reproduced Python constraints and verifies that the
  resolved environment matches them before testing.

### Fixed

- The run harness is compatible with both local ShellCheck 0.11.0 and the
  runner's ShellCheck 0.9.0 diagnostics.
- The declared cycle checker accepts the current runbook's explicit closed
  state after release while continuing to reject a zero-unchecked runbook that
  has no valid closing record.

### Carried dispositions

- X1's real-model aggregate remains `NOT EXERCISED`, not a no-leak claim;
  failure-capable controls independently observed both `GUARD FIRED` and
  deliberate raw overlap without public overlap.
- T7 single-flight, Postgres, pgvector, multi-host seam hardening, and the A4
  untrusted-shell boundary remain deferred under their measured triggers.
- `/view` materialization remains a future implementation task; v0.10.0 ships
  only its measured design and internal diagnostic seam.

## v0.9.0 — 2026-07-25

### Added

- One executable JSON authority for protected-artifact hashes and logical
  provenance, with deterministic evidence reports and failure-capable controls.
- Bounded, secret-redacted provider capability probing that distinguishes
  transport blocks, identity drift, and capability failures before a full live
  verifier run.
- Reproducible `/view` and exact-cosine benchmarks plus an executable audit of
  every deferred scale and deployment trigger.
- A local 16-job release matrix, Python 3.11/3.12 lanes, and append-only
  progress-record validation.

### Changed

- Missing persisted fingerprints now fail closed at `/view`, `/retrieve`, and
  canonical-id materialization instead of being recomputed or skipped.
- Core document reads are sector- and id-scoped in SQL, and the process-scoped
  `/view` cache is bounded, validates configured sectors, and exposes internal
  hit/generation diagnostics without changing its JSON response.
- Provider identity is independent from a per-command transport route, allowing
  the same configured LAN models to be probed through operator-owned forwards.
- Execution-cycle names and artifact-release identities are now explicitly
  separate; the annotated tag and agreeing version sources define a release.

### Deferred

- `/view` restart materialization is promoted to future design task V2 after
  both protected archive sizes missed the predeclared cold p95 SLO twice; every
  warm distribution passed.
- T7 single-flight, Postgres, pgvector, and multi-host hardening remain deferred
  by measured triggers. Manifest-admission enforcement, dependency constraints,
  and a real-model `GUARD FIRED` observation remain named future work.

## v0.8.0 — 2026-07-24

### Added

- Core `/attest` enforcement for every public `/v1/ask` answer, with
  failure-capable controls for blocked and deliberately leaking model output.
- A protected-artifact manifest, disposable eleven-assertion golden E2E, and
  blocking CI coverage for lint, the net feature, MSRV 1.78, and release-version
  consistency.
- Strict per-model embedding dimensions, retrieval diagnostics for mismatched
  legacy vectors, and real-model verification against separately hosted Gemma
  chat and EmbeddingGemma embedding services.

### Changed

- Harvest pages now commit documents and continuation state atomically, and two
  live arXiv runs proved interruption-resume on the wire.
- Cross-origin redirects are followed manually only after the destination
  origin passes the full robots gate.
- SimHash fingerprints and corpus-global canonical identities are persisted and
  re-materialized deterministically rather than derived from arrival order.
- Bare live harvests use fresh databases and refuse the two protected evidence
  databases as targets.

### Deferred

- T7 scheduler single-flight remains deferred: the shipped scheduler is one
  synchronous writer, so no concurrent trigger exists to guard. The gate must
  be revisited if a concurrent scheduler is introduced.
