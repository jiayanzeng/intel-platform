# PROGRESS-v0.26.md — append-only execution record

This file records v0.26 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-30 · ACTIVATE — v0.26 admitted with its supplied scope table

- owner: Codex
- commit: a90d080e1da18e8f16549b53c542b54259d74920
- result: PASS. The supplied runbook's declared scope parsed in its original
  executable Markdown-table dialect after the activation anchor existed; no
  translation or scope correction was required.
- worktree acceptance: PASS. Before activation the only worktree item was the
  operator-supplied untracked
  `docs/cycles/TASKS-v0.26-EXECUTION.md`. Implementation commit
  `a90d080e1da18e8f16549b53c542b54259d74920` contains only that runbook, the
  `AGENTS.md` v0.26 declaration, and this progress-log skeleton. Its immediate
  parent remains the unamended v0.25 post-push audit
  `12d0601e202efe36c6a36d42254bf39f3d12744d`.
- entering-ref acceptance: PASS with one entering-hypothesis correction.
  Before activation, HEAD was post-push audit
  `12d0601e202efe36c6a36d42254bf39f3d12744d` on branch
  `codex/v0.23-action-migration`, not on local `main`; local `main` remained
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. Read-only remote inspection
  resolved `main` and the peeled v0.16.0 tag to closing commit
  `c66c2b02191e3ca3126dddc3c004b175899b414e`, with annotated tag object
  `54f8cb2f89ed53d9e0b485f6cd46924a51e41813`; historical
  `refs/heads/candidate/v0.16.0` remained
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394`. No ref changed, and
  `STATE.md`'s header was not given a mutable branch-hash assertion.
- lifecycle acceptance: PASS. `cycle-check` reports active v0.26 open with
  twenty-three closed execution runbooks and three historical runbooks.
  `checklist-audit` passes **198 checked / 3 retracted / 198 matched / 0
  exemptions**. `progress-check` correctly reported that the new skeleton had
  no dated entry before this audit record existed.
- scope acceptance: PASS. The activation commit is the scope anchor, so its
  `activation..HEAD` diff is empty. The static release-intent rule accepts the
  complete declared release-authority set.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and drafted-gate measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- publisher-request acceptance: PASS. Activation invoked repository and GitHub
  ref/lifecycle commands only; it made no request to a publisher origin.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-30 · ACTIVATE-CORRECTION — trigger-table count made current

- owner: Codex
- commit: b6806e4b714a9eb0c42619834c4ac5f56985a9a8
- result: PASS. The first clean Python 3.11 E0 shell lane executed the live
  trigger-freshness control and found that v0.26 has **13** trigger-bearing
  rows while the exact current-table test still asserted **12**.
- fail-before acceptance: PASS. The clean constrained lane collected **284**,
  passed **283**, failed the exact
  `test_current_trigger_freshness_tables_are_complete` assertion, and skipped
  **0**. The observed count was `(2, 13)` against expected `(2, 12)`; this was
  a gate finding, not a passing shell measurement.
- gate-scope acceptance: PASS. The dated runbook amendment widens E0's gate
  only for `shell/tests/test_cycle_check.py`, which the full-matrix acceptance
  criterion already exercises and declared scope already permits. No objective,
  acceptance criterion, done condition, production permission, publisher
  permission, or trigger changed.
- focused acceptance: PASS. The unchanged failure-capable entry point now
  expects `(2, 13)` and passes **1/1**.
- lifecycle acceptance: PASS. `cycle-check` accepts the amended open v0.26
  runbook and its original activation anchor.
- scope acceptance: PASS. Only the active runbook and the exact shell
  lifecycle-count test changed. No production source, manifest, dependency,
  schema, protected artifact, public surface, configured source, or ref
  changed.
- complete-matrix acceptance: NOT YET CLAIMED. E0 restarts its clean Python
  lane after this correction and owns the complete entering result.
- golden-E2E delta: NOT MEASURED; no claim.
- publisher-request acceptance: PASS. The correction ran only a local focused
  lifecycle test and `cycle-check`; no publisher request occurred.

### 2026-07-30 · E0 — entering state rebuilt and seven gates settled

- owner: Codex
- commit: 4b9ed740953e7800480e59992c9364557c81a1d7
- result: PASS. Every drafted gate has an executed or enumerated measurement;
  G2 executed the shipped parser over the committed publisher-response bytes
  and accepted 200 documents.
- entering-matrix acceptance: PASS. `./run ci-local` passed all twenty stages:
  135 workspace Rust tests, 55 net-lane tests, current and Rust 1.78
  warning-denied builds, clippy, fmt, ShellCheck, floor byte-compilation,
  invariants 12/12 with 39 controls, and embedded golden 11/11.
- shell-population acceptance: PASS. Clean constrained Python 3.11.4 and
  3.12.13 lanes each collected 284, passed 284, and skipped 0. The comparator
  derived `collected=284`, `equivalent=true`, `equivalent_passed=284`, local
  `passed=284/skipped=0`, hosted `passed=284/on_site_skipped=0/skipped=[]`.
- standalone-controls acceptance: PASS. `golden` passed 11/11;
  `cycle-check`, `checklist-audit`, `progress-check`, `version-check`, and
  `invariant-scan` passed; root `export-check` passed 96 derived / 7 required /
  172 exported.
- G1 acceptance: PASS with finding. Store canonical assignment reads its
  private threshold at `crates/store/src/sqlite.rs:32`; view collapse reads an
  independent literal at `crates/view/src/lib.rs:44`. The execution record
  quotes R1 and R5's exact claims/scopes. R1 observes store caller topology and
  R5 observes the store constant bindings; neither compares the view value, so
  one declaration can move while the other remains 16 without either firing.
- G2 acceptance: PASS. A failure-capable disposable-clone integration probe
  executed shipped `RssSource` over the committed body and passed 1/1 with
  `parser-result=accepted documents=200`. Reqwest defaults a charset-less
  response to UTF-8 before roxmltree; this snapshot is lossless only because
  its bytes are pure ASCII. This is replay evidence, not fixture or live-wire
  evidence.
- G3 acceptance: PASS with finding. Schema-2 enumeration found 2 artifacts and
  266 pinned files, zero under `observations/`. The observation's prose hash is
  not executable; Step 2 must pin all five files before deriving its document
  measurements.
- G4 acceptance: PASS with finding. Offline finance ingest returned HTTP
  success with the fixture-backed source `ok:true` and fixtureless SEC
  `ok:false`, erroring that the binary lacks `net`. The shell pipeline printed
  the per-source error, continued, and exited 0. No existing test covers that
  exact fixtureless result or pipeline disposition.
- G5 acceptance: PASS. An external-effect capture double around the exact bare
  `harvest-arxiv` dispatcher recorded its generated config, three curl
  constructions, exact source-filtered ingest body, and zero SEC-origin
  requests. An isolated core confirmed that exact body selected only arXiv.
- G6 acceptance: PASS. Executing scheduler resolution produced the full
  quant-desk job at 7,200 seconds; no per-source cadence is needed, so SEC
  inherits the two-hour job interval.
- G7 acceptance: PASS. Generalizing `run` or adding a subcommand would require
  authorization and a replacement hash-chain admission. The viable no-pinned-
  byte path is a bounded operator sequence using a fresh archive, isolated
  loopback net core, exact SEC source selection, capture, and cleanup; a direct
  connector probe is not a harvest.
- artifact acceptance: PASS. Manifest validation reported 2 artifacts and 266
  pinned files; two `verify-artifacts` runs took 0.11 s / 0.09 s with all
  hashes exact; manifest size was 154,205 bytes.
- published-object acceptance: PASS. Read-only re-verification resolved remote
  main and peeled v0.16.0 to closing commit
  `c66c2b02191e3ca3126dddc3c004b175899b414e`, annotated tag object
  `54f8cb2f89ed53d9e0b485f6cd46924a51e41813`, and the historical candidate to
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394`; local object relations matched.
- scope acceptance: PASS. The implementation changed only the active runbook
  status/evidence. `STATE.md`, core and schedule config, production source,
  fixtures, corpus, golden input, protected bytes, and refs did not change.
- golden-E2E delta: **0**; standalone and matrix golden remained 11/11 with the
  hamming-12 true-positive collapse.
- publisher-request acceptance: PASS. E0 made no publisher request.

### 2026-07-30 · REPLAY-BLOCKED — schema cannot express the required pin

- owner: Codex
- commit: d5311a5f6c91db713597ce1a88b27e9ffcfe4212
- result: BLOCKED at the Step 2 decision gate before any document-set
  measurement. The runbook requires the five v0.25 observation files to remain
  at their original paths, become manifest-pinned, and carry a chained
  admission record. Executed schema 2 cannot represent that combination.
- pre-proposal acceptance: PASS. Before constructing a candidate,
  `evidence_artifacts.py validate` and `verify-artifacts` passed with 2
  artifacts, 266 pinned files, and both protected databases exact.
- byte-enumeration acceptance: PASS. All five source files were independently
  re-hashed at 903,679 bytes total. The active execution record lists each
  path, byte count, and SHA-256; the feed remains 892,641 bytes at
  `154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`.
- ordinary-pin fail-before acceptance: PASS. A disposable candidate adding an
  otherwise schema-shaped pinned-file object at the original observation path
  was examined by the real validator and failed because non-authorization pins
  must live beneath `evidence/`.
- chained-pin fail-before acceptance: PASS. A second disposable candidate
  included the required task/date/wire-reference/operator-approval/retroactive
  admission chain and was examined by the real validator; it failed the
  pinned-file exact-key check because `admission` is not allowed there.
- gate disposition: BLOCKED. Extending `tools/evidence_artifacts.py` and its
  schema is outside Step 2's Gate. Copying the bytes beneath `evidence/` would
  violate the runbook's explicit no-copy/original-path boundary. No workaround
  was implemented and no manifest proposal was made.
- replay acceptance: NOT MEASURED. Because pin-first is undischarged, no
  committed parser replay, field inventory, day-zone measurement, or extension
  enumeration was derived. The REPLAY checklist box remains unchecked.
- dependency disposition: IDENTITY-MEASURE and IDENTITY-DECISION remain blocked
  on Step 2. CADENCE remains independently eligible under the declared
  dependency graph.
- lifecycle acceptance: PASS. `cycle-check`, `progress-check`, and
  `checklist-audit` passed before this append, with the REPLAY box correctly
  unchecked.
- scope acceptance: PASS. The implementation commit changed only `STATE.md`
  and the active execution record. No schema, manifest, observation,
  production source, test, fixture, protected artifact, database, golden
  input, or ref changed.
- golden-E2E delta: **0**. The initial sandbox-only loopback bind refusal was a
  non-result; the identical permitted run passed 11/11.
- publisher-request acceptance: PASS. No publisher request was made.

### 2026-07-30 · CADENCE-BLOCKED — publisher-request gate violated

- owner: Codex
- commit: 6087c0fd6169882dad72f529738253cf54b5d097
- result: BLOCKED by an agent-side procedural violation at the Step 5 Gate.
  Codex directly opened the SEC Developer Resources URL even though the active
  runbook prohibits every publisher request before Step 6.
- request-boundary acceptance: FAIL. The web tool exposed one explicit
  retrieval of `https://www.sec.gov/about/developer-resources`; its underlying
  HTTP method, redirects, and request count are not observable, so the record
  conservatively says at least one publisher-origin request occurred. No
  robots URL, RSS URL, core, connector, or harvest command was invoked.
- guidance measurement: MEASURED BUT NOT ACCEPTED AS TASK COMPLETION. The
  official page returned “Developer Resources”, last reviewed or updated
  2025-03-10, and the current fair-access ceiling of no more than 10 requests
  per second total. The already committed v0.25 terms record had cited this URL
  on 2026-07-30, so the direct retrieval was unnecessary.
- stop acceptance: PASS. Work stopped immediately when the conflict was
  recognized. The weaker request-to-cite instruction was not used to silence
  the stronger no-request gate.
- cadence acceptance: NOT MEASURED. No cadence was chosen or explicitly kept;
  no resolvable-cadence test or vacuity disposition was produced. The CADENCE
  checklist box remains unchecked.
- architecture acceptance: NOT PERFORMED. `ARCHITECTURE.md` and its terms-gate
  row are byte-unchanged.
- scope acceptance: PASS after the stop. The implementation commit changed
  only `STATE.md` and the active execution record. `config/schedule.json`,
  shell tests/source, core config, production Rust, observations, manifest,
  protected artifacts, databases, and refs did not change.
- dependency disposition: Step 6 is ineligible both because CADENCE is not
  affirmative and because REPLAY remains blocked. Steps 7 and 8 remain blocked
  by their declared predecessors.
- golden-E2E delta: **0**; mandatory local golden passed 11/11 after the stop.
- classification: This is a cycle-execution failure by Codex, not an
  implementation defect and not live-harvest evidence.

### 2026-07-30 · AMENDMENT-01 — both blockers disposed; Step 2B authorized

- owner: Codex
- commit: b54cdbfcd727c7e327d100e4022f9d297c77ab81
- operator decision: AUTHORIZE Step 2B. The declared scope now conditionally
  permits `tools/evidence_artifacts.py`, the authorized deferral row discharges
  repository-wide observation coverage at Step 2B, and the new checklist row
  remains open until that task executes.
- supplied-amendment acceptance: PASS. All five dated operator-supplied entries
  were added under `Runbook amendments`; the Step 2, Step 2B, Step 4A, Step 4,
  Step 5, Step 6, Step 8, scope, deferral, checklist, and standing-prohibition
  replacements/additions are present. The quarantined retrieval remains
  uncited and the earlier `CADENCE-BLOCKED` progress entry is unchanged.
- REPLAY disposition: PASS. The unsatisfiable pin-first rule is classified as
  the fifth author-side rule with no satisfying assignment, not an
  implementation defect. Step 2 now requires a failure-demonstrated SHA-256
  and byte-length assertion at the point of use and forbids a manifest proposal.
- CADENCE disposition: PASS. The out-of-band retrieval remains a
  cycle-execution gate violation; its content is quarantined, the author-side
  ambiguity is recorded, and retractions remain three. Step 5 is eligible
  again only through its named committed observation paths.
- dependency acceptance: PASS. Step 2 blocks Step 3 and authorized Step 2B;
  Step 3 blocks Step 4A; Step 4A blocks Step 4; Step 6 requires affirmative
  Steps 2, 3, 4, 4A, and 5 plus a later explicit operator decision.
- lifecycle-control acceptance: PASS. `cycle-check` now recognizes one
  uppercase step suffix, so `Step 2B` and `Step 4A` retain distinct contract
  fields and deferred references. Two focused controls were added; the
  complete cycle-check test file passed 45/45 and the governed trigger
  population is now 2 architecture / 14 active-runbook rows.
- shell acceptance: PASS after discarding the sandbox-only failures that could
  not bind loopback or inspect processes. Permitted constrained Python 3.11.4
  and 3.12.13 runs each collected 286, passed 286, failed 0, and skipped 0,
  with the same accepted Starlette deprecation warning.
- invariant acceptance: PASS. `invariant-scan` passed 12/12 rules and all 39
  planted-failure controls. R12's two line-location pins were advanced with
  the checker edit; no claim, scope, rule, control construction, or count
  changed.
- lifecycle and version acceptance: PASS. `cycle-check`, `progress-check`,
  `checklist-audit` at 199 checked / 3 retracted / 199 matched / 0 exemptions,
  and `version-check` at 0.16.0 all passed.
- scope acceptance: PASS. The commit changed the active runbook, `STATE.md`,
  the exact lifecycle checker and tests needed for suffixed steps, and R12's
  shifted expected-line metadata. No production product source, publisher
  configuration, schedule, manifest, observation byte, protected artifact,
  database, public surface, dependency, or ref changed.
- golden-E2E delta: **0**; mandatory golden passed 11/11 with the hamming-12
  true-positive collapse intact.
- publisher-request acceptance: PASS. Amendment execution made no publisher
  request; the earlier quarantined retrieval remains recorded separately.

### 2026-07-30 · REPLAY — asserted real bytes through the shipped parser

- owner: Codex
- commit: 10071460c9a634279bf4b06b81675e0788b7d9e7
- result: PASS. The committed integration test executed shipped
  `RssSource::fetch` over the v0.25 SEC observation after verifying its bytes,
  and recorded the exact 200-document set without copying or mapping the
  observation.
- byte-assertion acceptance: PASS. Before parsing, the test asserted 892,641
  bytes and SHA-256
  `154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`,
  citing the committed v0.25 feed-shape record. The same assertion rejected a
  one-byte mutation at
  `feb138bb57e12466321c5db5a8f2a6ab1ea51ee59c9b94d355e7eaf65c9be748`;
  the disposable directory was removed.
- parser acceptance: PASS. The focused `-D warnings` test passed 1/1 and
  `RssSource::fetch` constructed 200 documents from 200 items. The test
  compared every `Document` field to the direct RSS children and configured
  provenance values.
- field-inventory acceptance: PASS. The execution record captures 200 distinct
  ids with maximum 114 bytes, titles of 30–80 characters, exact body-length
  distribution 3:108 / 4:64 / 5:5 / 6:4 / 7:19 and mean 3.810, one local day,
  all 200 raw dates retained with 191 distinct values, zero authors, 200
  distinct URLs, and `finance` / `PublisherPermitted` / `Rss` on every row.
- day-semantics acceptance: PASS. All raw zones were EDT and all constructed
  days were publisher-local `2026-07-29`. The executing test records that the
  parser ignores the clock and zone and independently found 0/200 UTC-day
  differences.
- extension acceptance: PASS. The committed v0.26 observation record lists 15
  `edgar:*` local names with both item populations and element totals,
  including 2,339 `xbrlFile` elements. None was mapped to `Document`.
- decoding acceptance: PASS with limitation. The body declares
  `windows-1252`; the shipped string path and roxmltree accepted it because
  the committed bytes are ASCII-only. This does not establish a general
  Windows-1252 decoder.
- establishment-boundary acceptance: PASS. Replay proves shipped parser
  behavior for this response only; paging, cursor durability, repeated
  fetches, on-wire politeness, redirects, conditional requests, and the next
  publisher response remain unmeasured.
- Rust acceptance: PASS. `RUSTFLAGS="-D warnings" cargo test --workspace
  --locked` passed 136 tests; clippy and fmt passed.
- lifecycle acceptance: PASS. `cycle-check` passed with REPLAY checked; the
  expected transitional checklist-audit failure before this append named only
  the absent REPLAY progress entry.
- scope acceptance: PASS. The implementation changed one integration test,
  one v0.26 observation record, `STATE.md`, and the active runbook. It changed
  no production source, dependency, fixture, protected artifact, manifest,
  golden input, core config, database, or ref.
- golden-E2E delta: **0**. The sandbox-only loopback bind refusal was a
  non-result; the permitted mandatory rerun passed 11/11.
- publisher-request acceptance: PASS. No publisher request was made.

### 2026-07-30 · OBSERVATION-PIN — observation bytes enter manifest coverage

- owner: Codex
- commit: 53ff369d17dcf9b62d1002ca9ad59686ce550f7d
- operator decision: AUTHORIZE, supplied 2026-07-30. The conditional
  `tools/evidence_artifacts.py` scope permission was used.
- result: PASS. `pinned_files` admits exactly one third prefix,
  `observations/`, and exactly one new grade, `observation`; five committed
  v0.25 observation files are now covered repository-wide.
- schema-shape acceptance: PASS. Observation pins carry only the existing six
  keys. No `admission` key was added, so a changed observation remains a defect
  rather than an artifact replaceable by an admission procedure.
- rejection-control acceptance: PASS. Four focused tests executed the real
  validator and passed 4/4. It rejected an observations path with
  `supporting`, rejected an `observation` grade under `evidence/`, and rejected
  an `observation` grade under an unregistered prefix. Each exact error was
  printed and captured.
- changed-byte acceptance: PASS. A disposable copy of the committed manifest
  and pins flipped one byte of the RSS body without changing its length.
  Validation reported its SHA mismatch: expected
  `154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`,
  actual
  `feb138bb57e12466321c5db5a8f2a6ab1ea51ee59c9b94d355e7eaf65c9be748`.
- pin-count acceptance: PASS. The manifest rose from 266 to **271** pins, five
  under `observations/`, all carrying only grade `observation`.
  `evidence_artifacts.py validate` passed schema 2 with 2 artifacts / 271 pins;
  `verify-artifacts` matched all 271 files and both protected databases.
- limitation acceptance: PASS. The runbook and `STATE.md` state that a pin
  detects changed repository bytes but does not prove those bytes are what the
  publisher served. Only the v0.25 wire record establishes that provenance.
- shell acceptance: PASS after discarding the sandbox-only lane whose eight
  failures could not bind loopback or inspect processes. Permitted constrained
  Python 3.11.4 and 3.12.13 each collected and passed **289**, failed 0, and
  skipped 0.
- invariant and lifecycle acceptance: PASS. `invariant-scan` remained 12/12
  rules / 39 controls; `cycle-check`, `progress-check`, and `version-check`
  passed before this append.
- scope acceptance: PASS. The implementation changed only the manifest
  validator, its shell tests, the manifest, `STATE.md`, and the active runbook.
  It changed no production product source, publisher config, observation byte,
  fixture, protected database, golden input, dependency, or ref.
- golden-E2E delta: **0**; mandatory golden passed 11/11 with the hamming-12
  true-positive collapse intact.
- publisher-request acceptance: PASS. No publisher request was made.

### 2026-07-30 · IDENTITY-MEASURE — 20 cross-issuer collapses measured

- owner: Codex
- commit: 4ec0082791eb169dea876f219a89b05d57578e90
- result: PASS with finding. At shipped radius 16, the 200 SEC documents
  produce 172 kept / 28 dropped; 8 drops share the kept document's issuer CIK
  and **20 cross issuer CIKs**. The existing finance fixture stays kept.
- shipped-rule acceptance: PASS. A committed test invoked the asserted-byte
  shipped RSS parser into a disposable binary interchange, sent the 201
  finance documents through `SqliteStore::append_new` and therefore private
  `assign_canonical_ids_tx`, then ran shipped `dedup_near` over the persisted
  fingerprints. The two shipped paths returned the same 28 drop pairs.
- per-drop acceptance: PASS. The committed observation record lists all 28
  dropped ids, kept ids, Hamming distances, issuer classes, and both CIKs.
- sweep acceptance: PASS as corpus measurement, not recommendation. Total
  kept / dropped / same / cross was 16: 173/28/8/20; 15: 187/14/6/8;
  14: 196/5/5/0; 13: 197/4/4/0; 12: 197/4/4/0; 10: 199/2/2/0; and
  8: 199/2/2/0. The fixture's minimum SEC distance was 23.
- mechanism acceptance: PASS. SEC three-token feature counts were
  `{4:40, 5:86, 6:48, 7:20, 8:5, 10:1}`, median 5; news counts were
  `{26:1, 28:1, 37:1, 40:2, 41:1, 42:1}`, median 40. SEC had 198 distinct
  fingerprints and 35/19,900 pairs inside radius 16; first-match identity
  yielded 28 drops. News had one of 21 pairs inside, the intended hamming-12
  golden pair. The full pair distributions are committed.
- same-day acceptance: PASS and not acted on. All 200 SEC inputs were on
  2026-07-29; 172 remained beside the 2026-07-03 fixture. The committed
  gazetteer resolved 0 mentions / 0 entities, so executed shipped analyze
  constructed no per-entity baseline, computed no z-score, and emitted zero
  signals and edges over its 26-day corpus window.
- prediction disposition: CONFIRMED except one author-side error. The draft's
  “28–36” news-feature comparison was wrong: execution measured range 26–42,
  median 40. This is not an implementation defect.
- Rust acceptance: PASS. The focused `-D warnings` measurement passed 1/1;
  full `-D warnings` workspace tests passed **137**; clippy and fmt passed.
- invariant and lifecycle acceptance: PASS. `invariant-scan` remained 12/12
  rules / 39 controls; `cycle-check`, `progress-check`, and `version-check`
  passed before this append.
- scope acceptance: PASS. Only two integration-test files, one v0.26
  observation, `STATE.md`, and the active runbook changed. Zero production
  source files, configs, fixtures, golden inputs, protected artifacts,
  databases, dependencies, or refs changed.
- golden-E2E delta: **0**; mandatory golden passed 11/11 and retained the
  hamming-12 true-positive drop.
- publisher-request acceptance: PASS. No publisher request was made.

### 2026-07-30 · THRESHOLD-AUTHORITY — boundary declarations synchronized

- owner: Codex
- commit: 0acbe17c63f3e56826242f7900aab3fdb693e8e4
- result: PASS. Store and view retain two deliberate boundary-local numeric
  declarations, and R5 now makes a unilateral change to either declaration
  fail.
- authority disposition: TWO WITH STATED LIMITATION. Neither production crate
  depends on the other, and Step 4A's allowed scope contains no common
  dependency module or manifest edge. The limitation is stated in
  `ARCHITECTURE.md`, R5's registered scope, and this progress record: R5
  provides static equality, not one shared compiled constant, and a coordinated
  edit to both values still needs separate behavioral evidence.
- claim/scope acceptance: PASS. R5 now checks every production store identity
  caller uses the private `DEDUP_MAX_DISTANCE`, exactly one store declaration
  and one `ViewParams` default exist, and their numeric values match. Its claim
  is no broader than those checks; test-only Rust remains excluded.
- planted-failure acceptance: PASS. The new registered control moved only the
  view default from 16 to 17 and left the store at 16. The real scanner rejected
  it at `crates/view/src/lib.rs:44` with the exact numeric mismatch.
- count acceptance: PASS. No rule was added: totals remain **12 rules** and
  rise from 39 to **40 controls**. The same counts appear in `STATE.md`, the
  active execution record, and this append.
- behavior acceptance: PASS. Both declarations remain 16 and neither
  production file changed. Golden remained byte-identical at 11/11, including
  the hamming-12 collapse.
- invariant-test acceptance: PASS. Python 3.11 and 3.12 focused invariant
  suites each passed 22/22. Full `invariant-scan` passed 12/12 rules and all
  40 controls.
- lifecycle acceptance: PASS. `cycle-check`, `progress-check`, and
  `version-check` passed before this append; fmt remained clean.
- scope acceptance: PASS. The implementation changed only
  `ARCHITECTURE.md`, the invariant registry and scanner, `STATE.md`, and the
  active runbook. Store/view production permissions were examined but unused;
  no test, config outside the registry, fixture, golden input, protected
  artifact, database, dependency, or ref changed.
- golden-E2E delta: **0**; mandatory golden passed 11/11 with byte-identical
  assertions.
- publisher-request acceptance: PASS. No publisher request was made.

### 2026-07-30 · IDENTITY-DECISION — radius guarded by measured feature floor

- owner: Codex
- commit: 1a48542c798d145ce9e02564aaa4e5c707e343f0
- result: PASS. The operator selected Option 1. Radius 16 is now eligible only
  when both documents have at least 26 three-token SimHash features.
- decision/claim acceptance: PASS. Twenty-six is the smallest feature count
  measured in the calibrated golden news corpus. The SEC maximum is 10, so
  11–25 remains deliberately ineligible rather than extrapolated. Sparse
  documents, including identical ones, remain distinct; that cost is stated in
  the runbook, `STATE.md`, and `ARCHITECTURE.md`.
- authority acceptance: PASS. Step 4A's two boundary-local radius declarations
  remain 16. `intel-extract` owns the one compiled `DEDUP_MIN_FEATURES` and
  shared two-sided guard; both store `assign_canonical_ids_tx` and view
  `dedup_near` invoke it. R1 remains unchanged because no identity caller was
  added.
- false-positive acceptance: PASS. The parser-produced 201-document finance
  test made both shipped paths keep 201 and drop 0. All 200 SEC documents
  remained distinct, eliminating all 20 previously measured cross-issuer
  collapses. Sparse-identical tests separately prove that distance zero is
  refused below the floor.
- true-positive acceptance: PASS. Golden remained byte-identical at 11/11 and
  still dropped `techwire::tw-004` for `osdaily::osd-004` at hamming 12.
- invariant acceptance: PASS. R5 now also observes the floor fixed at 26, both
  sides of the shared guard, and the store/view guard call sites. Four new
  planted mutations independently changed the floor, severed one guard side,
  removed the view call, and removed the store call; all four were detected.
  Counts remain **12 rules** and rise from 40 to **44 controls**, matching
  `STATE.md` and the active execution record.
- test acceptance: PASS. The `-D warnings` workspace passed **139** tests;
  both constrained Python lanes passed **289/289**; both focused invariant
  suites passed 22/22; full self-test passed 12/12 rules / 44 controls; clippy
  and fmt were clean. Initial sandboxed golden and shell runs could not bind
  loopback ports (and the shell audit could not inspect `ps`); their approved
  reruns executed those controls and passed.
- lifecycle acceptance: PASS. `cycle-check`, `progress-check`, and
  `version-check` passed before this append; `git diff --check` was clean.
- scope acceptance: PASS. The decision used the extract, store, and view
  permissions and their tests plus the declared invariant, architecture, and
  status paths. `config/core.json` and `config/schedule.json` were untouched.
  No ingest, compliance, shell source, dependency, protected database, fixture,
  golden input, or ref changed.
- golden-E2E delta: **0**; mandatory golden passed 11/11 with the hamming-12
  true-positive collapse intact.
- publisher-request acceptance: PASS. No publisher request was made.

### 2026-07-30 · CADENCE — explicit SEC source clock and G4 regression

- owner: Codex
- commit: bd546e1ae399ee1949524735dda45cdcfb7be5c2
- result: PASS. The inherited two-hour full-finance job was replaced with
  explicit source clocks: SEC every 600 seconds, `filings-digest` every 7,200
  seconds, and the finance refresh every 7,200 seconds.
- evidence acceptance: PASS. Every publisher fact came from a committed path.
  `observations/v0.25/terms-gate/sec-edgar-terms-determination.md` supplies the
  Developer Resources URL and 2026-07-30 read date;
  `observations/v0.24/publisher-review/sec-edgar-report.md` supplies the
  2-requests/second process floor, cited 10-requests/second publisher ceiling,
  and absence of publisher `Crawl-delay`; the `<description>` in
  `observations/v0.25/feed-shape/sec-edgar-usgaap.rss.xml` supplies the
  ten-minute feed-update interval.
- cadence acceptance: PASS. Six hundred seconds was chosen to match that
  committed update interval. Executed scheduler dry-run resolved
  `quant-desk:ingest-source:sec-edgar-usgaap` at 600 seconds,
  `quant-desk:ingest-source:filings-digest` at 7,200 seconds, and
  `quant-desk:refresh` at 7,200 seconds. The real-config regression executes
  the SEC job and fails if the source or cadence is absent.
- G4 acceptance: PASS. A failure-capable HTTP transport supplied the exact
  measured successful offline finance body: fixture-backed `filings-digest`
  `ok:true`, fixtureless SEC `ok:false`, and the absent-`net` error. The real
  shell pipeline printed the per-source error, continued through view and
  audit, wrote the brief, and returned 0.
- architecture acceptance: PASS. The dated cadence row is immediately after
  the existing SEC terms row. The terms row is byte-unchanged, and the new row
  explicitly says cadence does not satisfy terms.
- test acceptance: PASS. Focused cadence/G4 tests passed 10/10 in Python 3.11
  and 3.12. Both full constrained populations collected and passed **291** with
  zero skips. `invariant-scan` passed 12/12 rules / 44 controls; cargo fmt was
  clean.
- lifecycle acceptance: PASS. `cycle-check`, `progress-check`, and
  `version-check` passed before this append; `git diff --check` was clean.
- scope acceptance: PASS. Only the schedule, shell tests, architecture, and
  status records changed. Core config, production shell/core source,
  publisher bytes, fixtures, golden inputs, protected artifacts, databases,
  dependencies, and refs did not change.
- golden-E2E delta: **0**; mandatory golden passed 11/11, including the
  hamming-12 true-positive collapse.
- publisher-request acceptance: PASS. No publisher request or harvest
  occurred. Quarantined content was not cited.

### 2026-07-30 · HARVEST — wire crossed, plaintext evidence incomplete

- owner: Codex
- commit: 983fa9cf9d06403cac0c4f1b7df4c57812e15f02
- result: BLOCKED. The authorized isolated SEC ingest returned **200 fetched /
  200 new** and source `ok:true`, but the TLS-opaque observer did not measure
  all acceptance fields. HARVEST remains unchecked and Step 7 remains blocked.
- authorization acceptance: PARTIAL. The operator authorized one bounded
  harvest under seven conditions. No scheduler ran, no scheduled live run has
  occurred, and the 600-second cadence remains unexercised. No corrective
  publisher request is authorized.
- preflight acceptance: PASS. `verify-artifacts` matched all 271 pins and both
  protected databases. `data/core.db` was explicitly refused before
  reachability, and the harness-printed fresh absent target was
  `data/live-20260730T084234Z-16401.db`. Port 8788 was unused and the `-D
  warnings` net build passed.
- shipped-gate acceptance: PARTIAL. The live core logged `Body(allow)` for the
  SEC feed path with effective 0.500-second spacing. The observer recorded two
  SEC TLS connections at 08:47:16.394914Z and 08:47:17.646652Z, 1.251746
  seconds apart. Because TLS remained opaque, it did not capture the fresh
  robots body or establish its hash, exact status, redirect, or retry count.
- request-count acceptance: FAIL / NOT MEASURED. Two CONNECT records are not
  proof of the number of HTTP requests carried inside them. The record
  therefore does not claim exactly one feed request, exact publisher statuses,
  redirects, or retries even though the one core ingest completed.
- User-Agent acceptance: PARTIAL. The configured bytes were captured locally
  without printing the contact: 73 bytes, SHA-256
  `2fc0ac45a37a1c604d0f01d5039fffd0d734857b613de87cb6c848f29acec495`.
  The shipped two-client raw-wire test executed and passed, and the deliberate
  mismatch control fired. The publisher-received plaintext header was not
  observable through the relay, so byte-for-byte publisher receipt is not
  claimed.
- body-comparison acceptance: PARTIAL. The fresh archive contains 200 rows.
  All normalized ids, titles, descriptions, links, and raw publication dates
  equal the pinned observation; 200/200 descriptions equal pinned
  `edgar:formType`. The fresh XML declaration was not captured, so the pinned
  `windows-1252` declaration cannot be claimed for the fresh body.
- identity acceptance: PASS. The shipped guard kept **200 / dropped 0**. The
  fresh feature distribution is `{4:40, 5:86, 6:48, 7:20, 8:5, 10:1}`:
  200 below 11, zero in the 11–25 calibration gap, and zero eligible at floor
  26. Both distance-zero pairs, at 8/8 and 6/6 features, remain visible. This
  is the measured under-collapse cost in the safer failure direction.
- archive acceptance: PASS. The ignored, unadmitted 253,952-byte database has
  SHA-256
  `00b221483d58870f7841582f5afa9f0e3f6d19818e0c9cae1212d8bf6bfc8035`,
  passes integrity, and has 200 documents, 200 distinct canonical ids, zero
  canonical drops, and zero cursors. No protected byte changed.
- multi-origin acceptance: NOT EXERCISED. The selected runtime exercised SEC
  only; arXiv was not requested. Separate SEC cache/limiter use was observed,
  but two-origin runtime behavior remains unmeasured.
- lifecycle acceptance: PASS for the blocked record. `cycle-check`,
  `progress-check`, and `version-check` passed before the implementation
  commit; `git diff --check` was clean.
- golden-E2E delta: **0**. The initial sandboxed run could not bind loopback
  and was a non-result; the approved rerun executed all controls and passed
  11/11.
- disposition: this is an agent-side observation-design failure, not an
  implementation defect. No second robots or feed request was made. A
  corrective observable replay requires separate operator authorization.

### 2026-07-30 · HARVEST — corrective observation closes acceptance

- owner: Codex
- commit: bc23c4f6c49e76e99cd20426d4582f902a1ef394
- result: PASS. The operator separately authorized exactly one fresh robots
  request and one fresh feed request, with no scheduler and no archive
  mutation. The observable replay closed every plaintext field the first
  TLS-opaque attempt left unmeasured.
- observer acceptance: PASS. The disposable observer compiled offline against
  the repository's exact locked `reqwest 0.11.27`, `tokio 1.52.3`, and shipped
  ingest/compliance crates. Its pre-existing-output refusal executed first and
  failed before client construction. The observer source was SHA-256
  `e2396b69308f516bfe078eb0730c5b97e202bccd5c7b1e919433b1a6a0fc05c0`.
- preflight acceptance: PASS. All **271** pins and both protected databases
  matched immediately before and after the replay. No protected, production,
  configuration, fixture, golden, dependency, lockfile, or ref byte changed.
- robots acceptance: PASS. At **2026-07-30T09:18:38.296998Z**, the shipped
  `HttpRobotsFetcher` recording wrapper and `RobotsCache` each counted exactly
  **1** request. The cache returned `Body(allow)` for the feed path, the cored
  operator deny-list also allowed it, and the effective rate remained 2
  requests/second. The 2,622-byte body has SHA-256
  `72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`
  and is byte-identical to the v0.25 policy.
- feed-wire acceptance: PASS. At **2026-07-30T09:18:39.680936Z**, after both
  gates and the shared limiter, exactly one feed request began. The measured
  request-start interval was **1.383946 seconds**. Redirects and retries were
  disabled and counted zero. The response was HTTP **200**,
  `Content-Type: text/xml`, with no `Location` or `Retry-After` header. Its
  892,641-byte body has SHA-256
  `154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`
  and is byte-identical to v0.25.
- body-comparison acceptance: PASS. The fresh body still declares
  `windows-1252`, contains **200** items, and has description equal to
  `edgar:formType` in **200/200**. Byte identity makes the previously executed
  fresh-archive distribution authoritative here too:
  `{4:40, 5:86, 6:48, 7:20, 8:5, 10:1}`, with zero rows in 11–25.
- User-Agent acceptance: PASS. The exact installed value assigned to both
  clients was captured as **73 bytes**, SHA-256
  `2fc0ac45a37a1c604d0f01d5039fffd0d734857b613de87cb6c848f29acec495`,
  and compared byte-for-byte with the configured production construction
  without printing the contact. The raw contact-bearing temporary file was
  removed after verification.
- archive/identity acceptance: PASS from the original shipped-core phase. The
  unadmitted fresh archive remains 200 fetched / 200 new, 200 canonical / zero
  drops. The shipped guard kept 200 / dropped 0, and both distance-zero sparse
  pairs remain visible as the documented under-collapse cost.
- multi-origin acceptance: NOT EXERCISED and stated. The corrective phase made
  one robots plus one feed request to SEC and zero requests to any other
  origin. Both live phases exercised SEC only; arXiv cache/limiter behavior in
  the same production runtime remains unmeasured.
- schedule boundary: PASS. No scheduler ran, no scheduled live run has ever
  occurred, and the 600-second cadence remains unexercised. Neither bounded
  authorization grants that recurring traffic commitment.
- lifecycle acceptance: PASS. `cycle-check`, `progress-check`, and
  `version-check` passed before the implementation commit; `git diff --check`
  was clean.
- golden-E2E delta: **0**; mandatory golden passed **11/11**.

### 2026-07-30 · RE-MEASURE — hosted run green, admission clause unsatisfiable

- owner: Codex
- commit: c9721ab7969865ae35a9030d6da0cd8145a87c51
- result: BLOCKED. Hosted execution passed, but Step 7 step 3 requires a
  chained admission record for a receipt/bundle set and executed manifest
  schema 2 has no container that can express that combination. RE-MEASURE
  remains unchecked and R-CLOSE remains blocked.
- authorization acceptance: PASS. The operator authorized one exact
  neutral-branch push. Candidate
  `1cd88acd99704cc76c866331e505db446936e469` was pushed only to
  `refs/heads/codex/v0.26-evidence-1cd88ac`. Remote `main` remained
  `c66c2b02191e3ca3126dddc3c004b175899b414e`, historical
  `refs/heads/candidate/v0.16.0` remained
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394`, and no tag was created.
- hosted acceptance: PASS. Authenticated run **30531390933**, attempt **1**,
  passed all seven executable jobs at the exact candidate. Remote and local
  CI workflow blobs matched at
  `48ea726b798f1049e0b29cce1f0c64588861c2dd`; hosted golden passed 11/11
  and `invariant-scan` passed 12/12 rules / 44 controls.
- shell-comparator acceptance: PASS. For both Python 3.11 and 3.12,
  `tools/test_population.py` derived `collected=291`, `equivalent=true`, and
  `equivalent_passed=291`: local passed 291 / skipped 0; hosted passed 290
  plus one named `on_site` skip. The skipped node was
  `tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`;
  its declared reason was “on-site production audit requires protected
  corpora and built cored”.
- no-publisher-request acceptance: PASS. The workflow contains no harvest or
  ingest command. A case-insensitive complete-log search found no `sec.gov`,
  `harvest-arxiv`, `POST /ingest`, publisher URL, or publisher-directed HTTP
  command. Both `usgaap.rss` matches were `PIN MATCH` output for the committed
  observation path, not network commands.
- chained-admission acceptance: FAIL / NO SATISFYING ASSIGNMENT. The real
  validator rejected a receipt under `pinned_files` with
  `pinned_files[271]: keys differ; missing=[], extra=['admission']`. It
  rejected the same receipt under `artifacts` with
  `artifacts[2]: keys differ; missing=['expected'], extra=[]`; the required
  `expected` object is the SQLite document/integrity/fingerprint/canonical-id/
  cursor shape and cannot truthfully describe a JSON receipt. Under Amendment
  1's operator criterion, this is the sixth author-side rule with no
  satisfying assignment, not an implementation or hosted-CI defect.
- evidence acceptance: BLOCKED. The fourteen downloaded receipt/bundle files
  remain outside the repository. No evidence-directory scope amendment is
  claimed, no deferred-audit report was generated, and the manifest remains
  **271** pins with both protected databases exact.
- lifecycle acceptance: PASS for the blocked record. `cycle-check`,
  `version-check`, `progress-check`, manifest validation, `verify-artifacts`,
  and `git diff --check` passed before the implementation commit. The first
  sandboxed golden could not bind loopback and was a non-result; the approved
  rerun executed all controls and passed 11/11.
- golden-E2E delta: **0**; mandatory golden passed **11/11**.

### 2026-07-30 · RE-MEASURE — authenticated evidence admitted

- owner: Codex
- commit: be34f7610d61e8f57b6d1c68cde942d9bb240bb8
- result: PASS. The operator-approved amendment replaced the unsatisfiable
  chained-receipt clause with immutable pins plus paired Sigstore verification.
  The earlier blocked entry remains the accurate record of the original stop;
  this entry records the separately authorized completion.
- hosted acceptance: PASS. Run **30531390933**, attempt **1**, passed all seven
  executable jobs at exact candidate
  `1cd88acd99704cc76c866331e505db446936e469` on neutral ref
  `refs/heads/codex/v0.26-evidence-1cd88ac`. Remote `main` remained
  `c66c2b02191e3ca3126dddc3c004b175899b414e`, historical
  `refs/heads/candidate/v0.16.0` remained
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394`, and no tag was created.
- shell-comparator acceptance: PASS. For both Python 3.11 and 3.12,
  `tools/test_population.py` derived `collected=291`, `equivalent=true`, and
  `equivalent_passed=291`: local passed 291 / skipped 0; hosted passed 290
  plus the named `on_site` skip
  `tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`,
  whose declared reason is “on-site production audit requires protected
  corpora and built cored”.
- authenticated-evidence acceptance: PASS. The seven receipt JSON files and
  seven paired Sigstore bundles are registered as immutable `supporting`
  `pinned_files` beneath `evidence/ci-runs/30531390933-1/`. Every bundle
  verified the exact receipt bytes, repository `jiayanzeng/intel-platform`,
  workflow `jiayanzeng/intel-platform/.github/workflows/ci.yml`, candidate
  digest, neutral source ref, and GitHub-hosted runner policy. No `admission`
  key was added and no receipt entered the SQLite-only `artifacts` container.
- release-posture acceptance: PASS.
  `evidence/v0.26/deferred-audit/report.json` is **34,937 bytes**, SHA-256
  `267c23c676b0e227584d0eb9647d0ce8c4595804fb39e6ac5047691d066d0f25`,
  and grade `release`. It required attestations, accepted **7** distinct
  successful identities, rejected **0**, confirmed the single-run matrix
  complete, and recorded **5 deferred / 2 promoted / 0 implemented deferred
  subsystems**. Independent rederivation passed when supplied the pinned
  receipt directory.
- manifest acceptance: PASS. The fourteen hosted files and release-posture
  report raise the pin count from 271 to **286**. Manifest validation,
  `verify-artifacts`, and `evidence-report` passed with both protected
  databases exact. The exact evidence-directory scope row and dated amendment
  landed in the same implementation commit as the first admitted bytes.
- no-publisher-request acceptance: PASS. The hosted workflow has no harvest or
  ingest command, and complete-log inspection found no publisher URL or
  publisher-directed HTTP command. The two `usgaap.rss` strings were local
  `PIN MATCH` output. No additional publisher request was made while admitting
  or rederiving the evidence.
- lifecycle acceptance: PASS. `cycle-check`, `version-check`,
  `progress-check`, `invariant-scan` with self-test, `checklist-audit`,
  manifest validation, `verify-artifacts`, `evidence-report`, report
  rederivation, and `git diff --check` all passed. `invariant-scan` remains
  **12/12 rules / 44 controls**.
- golden-E2E delta: **0**; mandatory golden passed **11/11**.

### 2026-07-30 · R-CLOSE — v0.16.1 tagged close

- owner: Codex
- commit: b9af84b8785bcd52c16ab0225d66386ecd872c4d
- result: PASS. Release implementation commit
  `b9af84b8785bcd52c16ab0225d66386ecd872c4d` prepares v0.16.1 and is the
  untagged immediate parent of the closing tree. No corrective trigger was
  visible at entry; the publication trigger is the operator's explicit
  decision to ship the authenticated identity correction, explicit SEC
  cadence, and bounded first-contact validation.
- closing-evidence acceptance: PASS. Authenticated candidate
  `1cd88acd99704cc76c866331e505db446936e469` and run **30531390933**
  attempt **1** remain separate from the release parent. All seven executable
  hosted jobs passed. Release-grade verification required attestations,
  accepted **7 / rejected 0** identities, and confirmed the complete matrix.
- release-identity acceptance: PASS. v0.16.1 is patch because it corrects
  behavior within existing routes, fields, types, body shapes, and public
  value sets. The public value-domain criterion does not fire: no serialized
  `/v1/*` field gains, loses, or redefines a value. The exact **44**
  `v0.16.0..b9af84b8785bcd52c16ab0225d66386ecd872c4d` paths are classified
  once in eight disjoint groups in `STATE.md`.
- identity acceptance: PASS. At radius 16 the parser-produced SEC corpus
  measured 172 kept / 28 dropped, including 8 same-issuer and **20
  cross-issuer false collapses**. The selected two-sided 26-feature floor
  addresses the measured sparse-fingerprint mechanism: both shipped paths and
  the independent live sample keep **200 / drop 0**. Golden remains
  byte-identical and still drops `techwire::tw-004` for
  `osdaily::osd-004` at Hamming 12. Sparse identical documents remain visible
  as the explicit safer-direction under-collapse cost.
- parser/pin acceptance: PASS. Shipped `RssSource::fetch` constructed **200**
  documents from the asserted 892,641-byte observation. The body declares
  Windows-1252 but is ASCII-only; the existing UTF-8 string path accepted it
  losslessly, and no general non-UTF-8 decoder branch was established. No
  `edgar:*` field was mapped. G3 found the observation unpinned; authorized
  Step 2B added exactly the `observations/` prefix and `observation` grade and
  pinned all five v0.25 files without `admission`.
- scope/non-exercise acceptance: PASS. All three conditional Rust source
  permissions were used for the shared floor/guard and its store/view calls;
  the authorized conditional `tools/evidence_artifacts.py` permission was also
  used. No conditional source permission is unused. No ingest or compliance
  production source, `config/core.json`, dependency, schema, protected
  database, fixture, or golden input changed. A bounded SEC ingest did occur,
  but no scheduler or scheduled SEC run occurred and no production runtime
  exercised both origins together. Both configured real publisher sources
  have now been fetched.
- blocker acceptance: PASS. Step 2's original pin-first requirement remains
  the fifth author-side rule with no satisfying assignment: `artifacts[]`
  requires SQLite-only expected facts and the original `pinned_files[]`
  shape could neither admit the observation path nor carry `admission`.
  CADENCE's out-of-band retrieval remains a cycle-execution gate violation;
  its content is quarantined and uncited, its author-side ambiguity is
  recorded, and retractions remain **three**. Step 7's separately withdrawn
  chained-receipt clause remains the sixth unsatisfiable author-side rule.
- release-parent acceptance: PASS. `./run ci-local` passed all **20** jobs:
  workspace **139**, net **56** (**30** ingest including replay + **26**
  cored), warning-denied current and locked Rust 1.78 builds, clean
  rustc/clippy/fmt/ShellCheck, `invariant-scan` **12/12 rules / 44 controls**,
  and embedded golden **11/11**. Mandatory standalone golden passed **11/11**.
- population acceptance: PASS. Clean Python **3.11.4** and **3.12.13** lanes
  each collected **291**, passed **291**, failed 0, and skipped 0. The
  authenticated candidate comparators separately derived equivalence from
  hosted 290 passes plus the one named `on_site` skip in both lanes.
- evidence acceptance: PASS. All **286** pins and both protected databases
  remained exact. Manifest size is **165,488 bytes**; consecutive complete
  verification runs were **0.11 s / 0.10 s real**. Root `export-check` passed
  **99** derived sources / **7** required / **177** exported.
  Release-posture rederivation reproduced all 7 rows with attestations
  required.
- protocol acceptance: PASS. The closed record names release parent
  `b9af84b8785bcd52c16ab0225d66386ecd872c4d` and evidence candidate
  `1cd88acd99704cc76c866331e505db446936e469` separately, omits the
  not-yet-knowable tag-object field, and requires the annotated v0.16.1 tag to
  target this immediate child and move atomically with `main`.
- residual acceptance: PASS. A4, editable L1, R3/R4, the measured-value
  heuristic, T7, NEGATIVE-CACHE Decision B, scheduled L2, FastAPI
  version-literal relocation, terms-gate operator responsibility, and live
  multi-publisher behavior remain open or unchanged. One supported SEC
  harvest caller and zero schedulers do not move T7 nearer its trigger.
- historical-ref acceptance: PASS. Existing
  `refs/heads/candidate/v0.16.0` remains v0.15.1 evidence at
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394`; it predates and does not belong
  to this release and must not be renamed or deleted.
- publisher-request acceptance: PASS. R-CLOSE made no publisher request.
- golden-E2E delta: **0**.

### 2026-07-30 · POST-PUSH — v0.16.1 forward confirmation

- owner: Codex
- commit: 397d100ae425d5d059cef8a8ddb2ac13cfde52f5
- result: PASS. Atomic publication moved remote `main` and annotated tag
  `v0.16.1` together. Tag object
  `ae593e882898b9c49d5e91e2d50b6ca1f02ac49b` targets closing commit
  `397d100ae425d5d059cef8a8ddb2ac13cfde52f5`, whose immediate parent is
  release commit `b9af84b8785bcd52c16ab0225d66386ecd872c4d`.
- hosted-forward acceptance: PASS. Post-push run **30535121730**, attempt
  **1**, executed at the exact closing commit and passed all seven executable
  jobs: core, lint, golden, net, shell 3.11, shell 3.12, and MSRV. The
  report-only dependency-drift job was skipped as designed.
- population acceptance: PASS. Both machine-readable comparisons returned
  `collected=291`, `equivalent=true`, and `equivalent_passed=291`: local
  passed **291 / skipped 0**, while hosted passed **290** plus the one named,
  reasoned, `on_site` skip
  `tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`.
- hosted-count acceptance: PASS. Hosted execution reported **139** workspace
  tests; **56** net tests (**30** `intel-ingest`, including replay, plus
  **26** `cored`); checklist-audit **208 checked / 3 retracted / 208 matched /
  0 exemptions**; invariant-scan **12/12 rules / 44 controls**; **286** pins;
  and golden **11/11**.
- closure-semantics acceptance: PASS. Authenticated candidate run
  **30531390933**, attempt **1**, remains the signed closing evidence.
  Post-push run **30535121730** is forward confirmation of the published
  closing commit and does not replace those attestations.
- publisher-request acceptance: PASS. Complete hosted-log inspection found no
  publisher URL or publisher-directed request command. The only two
  `usgaap.rss` matches were local `PIN MATCH` output. Publication and
  verification made no publisher request.
- historical-ref acceptance: PASS. Existing
  `refs/heads/candidate/v0.16.0` remains v0.15.1 evidence at
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394`; it predates and does not belong
  to v0.16.1.
- audit-rhythm acceptance: PASS. This first descendant audit record is
  supported by its required local gates and intentionally remains
  hosted-unverified until the following publication.
- scope acceptance: PASS. This audit record changes only `STATE.md` and the
  active append-only progress log.
- golden-E2E delta: **0**; published-head hosted golden passed **11/11** and
  the mandatory local audit golden passed **11/11**.
