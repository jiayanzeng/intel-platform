# PROGRESS-v0.25.md — append-only execution record

This file records v0.25 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-30 · ACTIVATE — v0.25 admitted with a valid live contract

- owner: Codex
- commit: 822aa54
- result: PASS. Before the activation commit, the supplied runbook's declared
  scope was translated from its non-executable YAML draft into the required
  Markdown table, and the manifest-retention remeasurement was assigned to
  Step 1. No task objective, gate, acceptance criterion, or permission changed.
- worktree acceptance: PASS. Before activation the only worktree item was the
  operator-supplied untracked
  `docs/cycles/TASKS-v0.25-EXECUTION.md`. Implementation commit `822aa54`
  contains only that runbook, the `AGENTS.md` v0.25 declaration, and this
  progress-log skeleton.
- entering-ref acceptance: PASS with one entering-hypothesis correction.
  Before activation, HEAD was post-push audit
  `947822c8ff85d256f20a38f1f91f5eb85326af7c` on branch
  `codex/v0.23-action-migration`, not on local `main`; local `main` remained
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. Read-only remote inspection
  resolved `main` and peeled `v0.15.8` to closing commit
  `64002678672a601804e5f67886c73fffb4d212c8`, with annotated tag object
  `dc5abe0690e77cef671896102382427721d97321`. No ref changed.
- lifecycle acceptance: PASS. `cycle-check` reports active v0.25 open with
  twenty-two closed execution runbooks and three historical runbooks.
  `checklist-audit` passes **191 checked / 3 retracted / 191 matched / 0
  exemptions**. `progress-check` correctly reported that the new skeleton had
  no dated entry before this audit record existed.
- scope acceptance: PASS. The activation commit is the scope anchor, so its
  `activation..HEAD` diff is empty. The static release-intent rule accepts the
  complete declared release-authority set.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and drafted-gate measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-30 · ACTIVATE-CORRECTION — crate-source scope made explicit

- owner: Codex
- commit: e1512ca
- result: PASS. The first clean Python 3.11 E0 shell lane executed the active
  scope control and found three release-authority/forbid overlaps rather than
  the one documented overlap. The two crate-wide forbids now name only
  `crates/ingest/src/**` and `crates/compliance/src/**`; the effective
  release-authority permission is unchanged.
- fail-before acceptance: PASS. The clean lane resolved all **21** constrained
  packages, collected **283**, passed **282**, failed the exact active-scope
  control, and skipped **0**. The failing assertion reported
  `crates/compliance/Cargo.toml`, `crates/ingest/Cargo.toml`, and
  `shell/intel_shell/app.py` instead of the required sole `app.py` overlap.
  This was a gate finding, not a passing shell measurement.
- focused acceptance: PASS. The unchanged failure-capable
  `test_current_scope_has_exactly_one_release_forbid_overlap` passes **1/1**
  after the runbook correction.
- lifecycle acceptance: PASS. `cycle-check` accepts the corrected active scope
  and its dated amendment.
- scope acceptance: PASS. Only the active runbook changed. No crate source,
  manifest, workflow, dependency, schema, protected artifact, public surface,
  configured publisher, or ref changed.
- golden-E2E delta: NOT MEASURED; no claim.

### 2026-07-30 · E0 — entering state rebuilt and six gates settled

- owner: Codex
- commit: cf092ad0209a952f55aaeb8221f82c578dbe1cfc
- result: PASS. The complete entering matrix, both clean shell lanes, every
  standalone control, G1–G6, artifact scale, published objects, and all pins
  were re-measured. The active runbook contains the command-backed record.
- entering-matrix acceptance: PASS. `./run ci-local` passed all **20** jobs:
  workspace **133**, net **55** (**29** ingest + **26** cored), warning-denied
  current and locked Rust 1.78 builds, clean clippy/fmt/ShellCheck, shell
  **283 / 283 / 0 skipped**, protected databases **2/2**, and embedded golden
  **11/11**. Standalone golden passed **11/11**. Standalone `cycle-check`,
  `checklist-audit` (**191 checked / 3 retracted / 191 matched / 0
  exemptions**), `progress-check`, `version-check`, `invariant-scan` (**12/12
  rules / 39 controls**), manifest validation, and root `export-check` (**94**
  derived / **7** required / **163** exported) passed.
- population acceptance: PASS. Clean Python **3.11.4** and **3.12.13** each
  collected **283**, passed **283**, failed **0**, and skipped **0**. The
  machine-readable comparator derived `equivalent=true` and
  `equivalent_passed=283`; its second input was the local 3.12 lane, not a
  hosted run.
- G1 acceptance: PASS. `PublicDomain` would make the unsupported
  government-work/public-domain claim, `CcBy` would invent a CC licence,
  `ClientOwned` would falsely assert subscriber ownership, and `IndexOnly`
  would be safe only by forfeiting the publisher's express reuse permission.
  No existing variant expresses publisher-granted reuse under the publisher's
  own terms.
- G2 acceptance: PASS. The executable model was enumerated as publisher
  `robots.txt` plus the operator deny-list, with no terms component. The SEC
  privacy, webmaster FAQ, and developer-resource texts were recorded by URL and
  2026-07-30 read date: the publisher disallows “unclassified” automation and
  operationally directs programmatic downloaders to declare an
  organization-and-contact User-Agent. No broader definition was inferred.
- G3 acceptance: PASS. The parser requires well-formed XML but treats every
  per-item field—`title`, `guid`, `pubDate`, `link`, `description`, and
  `author`—as optional; zero `item` elements succeeds with an empty result. No
  feed request was made.
- G4 acceptance: PASS. Public licence carriers were enumerated for
  `/v1/signals`, `/v1/search`, `/v1/ask`, and the conditional plaintext branch
  of `/v1/brief`. The standing rule does not explicitly classify a compatible
  expansion of a string enum's value domain.
- G5 acceptance: PASS after a dated runbook correction. Golden does read
  `config/core.json`, but explicitly selects only `science` and `technology`;
  the proposed source is confined to `finance`. Its measured expected outcome
  therefore remains **11/11**.
- G6 acceptance: PASS. The crawler identity derives its version from
  `CARGO_PKG_VERSION`; every net startup structurally requires a non-empty,
  non-placeholder contact before bind. Whether the contact is monitored remains
  an operator fact.
- evidence acceptance: PASS. The protected manifest remains **145,541 bytes**.
  Two consecutive `verify-artifacts` entry-point runs passed in **0.09 s** each,
  all **251** pins and both protected databases matched, and the v0.15.8
  annotated object, peeled closing commit, release parent, and live remote refs
  were re-verified.
- boundary acceptance: PASS. E0 made no publisher-origin request, no feed
  request, no working-repository ref mutation, and no change to `STATE.md`,
  `config/core.json`, production source, protected corpus, schema, or public
  surface.
- golden-E2E delta: **0**.

### 2026-07-30 · LICENSE-SEMANTICS — PublisherPermitted selects v0.16.0

- owner: Codex
- commit: ad029da80f9e5c0a463b9f0aa38eff95eb151ef2
- result: PASS. The operator selected `extend/minor`.
  `PublisherPermitted` records that a publisher expressly permits reuse under
  its own stated terms while making no claim about underlying copyright.
  `PublicDomain` remains excluded because the measured SEC evidence does not
  establish that issuer-authored filings are government works. `CcBy`,
  `ClientOwned`, and `IndexOnly` would each make a different false or
  unnecessarily restrictive claim.
- gate acceptance: PASS after a pre-implementation scope correction. The task's
  acceptance criteria required an `AGENTS.md` edit while its gate omitted that
  path; the dated amendment added the path already permitted by declared scope
  without changing the objective, implementation, or done condition. E0 had
  confirmed G1. No ingest, compliance, shell source, configured source,
  schema-breaking, or protected-database change occurred.
- version acceptance: PASS. The operator's exact symmetric public-value-domain
  criterion is now in `AGENTS.md` and reconciled in `ARCHITECTURE.md §8`.
  Adding, removing, or redefining a value of a field already serialized in a
  `/v1/*` response takes a minor release because exhaustive value handling is
  part of the consumer contract. The selected identity is **v0.16.0**
  independently of later source-admission gates.
- mapping acceptance: PASS. `PublisherPermitted`, `as_str()`, and `parse()` use
  exactly the same spelling. `redistributable()` is an exhaustive match and
  returns true for the new value. The focused core test enumerated all five
  licences and proved the existing spellings, parse outcomes, redistribution
  outcomes, and `/attest` behavior unchanged: only `IndexOnly` is
  non-redistributable and refused.
- persistence acceptance: PASS. The new store integration test round-tripped
  `PublisherPermitted`, observed the exact SQLite text, and returned a
  redistributable search snippet. SQLite's existing `license TEXT NOT NULL`
  column has no `CHECK`; writes already use `as_str()` and reads already route
  through `License::parse`. `crates/store/src/sqlite.rs` therefore required no
  edit, and that half of the conditional scope permission was unused.
- unknown-value acceptance: PASS in both directions. The actual offline `cored`
  entry point started from a temporary config containing
  `PublisherPermitted`; a temporary `FutureLicense` value exited **101** with a
  hard Serde error. A planted SQLite `FutureLicense` row silently fell back to
  `IndexOnly` and suppressed its snippet. Both directions fail safely, while
  the archive path means an older binary can silently reclassify a newer
  value.
- invariant acceptance: PASS. Step 2 produced no new invariant rule because a
  release-classification judgment is not observable by a registered source
  scan. `invariant-scan` remains exactly **12 rules / 39 controls**, recorded
  here, in `STATE.md`, and in the active runbook; no R12 mutation was added.
- complete-matrix acceptance: PASS. `./run ci-local` passed all **20** jobs:
  workspace **135**, net **55** (**29** ingest + **26** cored),
  warning-denied current and locked Rust 1.78 lanes, clean
  clippy/fmt/ShellCheck, Python 3.11 **283 collected / 283 passed / 0 skipped**,
  protected databases **2/2**, all **251** pins, and embedded golden **11/11**.
  Independent Python 3.12 passed **283 collected / 283 passed / 0 skipped**.
  `cycle-check`, formatting, and diff hygiene passed.
- release-boundary acceptance: PASS. `config/core.json` is unchanged, so zero
  configured sources produce the value and no `/v1/*` response can yet carry
  it. `README.md`'s now-stale four-value enumeration is explicitly assigned to
  Step 7, whose gate contains that release authority. Live remote inspection
  found no v0.16.0 tag and left the pre-existing
  `candidate/v0.16.0` branch at the v0.15.1 evidence commit
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394`; its seven immutable receipt
  provenance entries plus pinned report remain disambiguated as eight
  historical evidence subjects. No publisher/feed request or ref mutation
  occurred.
- runbook-correction acceptance: PASS. The false author-side G5 implication was
  recorded as a runbook error: golden uses only `science` and `technology`, so
  a future `finance` source does not enter it.
- golden-E2E delta: **0**; mandatory standalone `./run golden` passed
  **11/11**.

### 2026-07-30 · TERMS-GATE — SEC identity affirmative, terms operator-owned

- owner: Codex
- commit: a6f6d17bade91a9da194b132d98defc4a4134d14
- result: PASS. The operator accepted the recommended affirmative
  determination and confirmed its premise that the configured crawler contact
  is monitored. The identity satisfies the SEC's published
  organization-and-contact direction for the reviewed path.
- gate acceptance: PASS. Every criterion fit the existing gate:
  `observations/v0.25/**`, `ARCHITECTURE.md`, and status records. No code,
  config, schema, protected-artifact, or public-surface edit was required. E0
  had confirmed G2, so the dependency gate was open.
- publisher-text acceptance: PASS. The committed robots evidence records an
  **allow** verdict for `/Archives/edgar/usgaap.rss.xml`. The SEC Privacy
  Information page and Webmaster FAQ are cited by URL with their 2026-07-30
  read date. The former refuses “unclassified” automated tools; the latter
  directs programmatic downloaders to declare a User-Agent and supplies an
  organization-and-administrative-contact example. The publisher provides no
  separate glossary or registration transaction, so no broader definition was
  inferred.
- identity-property acceptance: PASS. The condition is now
  version-independent: **a monitored contact is present in the crawler
  identity**. E0 proved that net startup structurally requires a trimmed,
  non-empty, non-placeholder contact before bind and derives the version from
  package authority. Monitoring is an operator fact, and the operator confirmed
  it. No structural contact defect exists to fix or assign forward.
- architecture acceptance: PASS. The dated operational disposition records
  publisher terms as a publisher-specific operator responsibility outside the
  executable model. The SEC requirement is natural-language policy with no
  stable machine-readable classification or registration state; a third
  runtime boolean would assert an automation the system cannot perform.
  Publisher `robots.txt` plus the operator deny-list remain the two executable
  gates.
- limits acceptance: PASS. The determination binds only the SEC, the reviewed
  path, the cited texts, and 2026-07-30. It is not a general finding about
  government or regulatory publishers and establishes nothing about feed
  shape. Step 4 remains separately gated on authorization for one live feed
  GET.
- request and diff boundary: PASS. Step 3 made **zero publisher requests**.
  Final diff inspection found only `ARCHITECTURE.md`, `STATE.md`, the active
  runbook, and the new dated observation; all code and config paths were
  byte-unchanged.
- lifecycle acceptance: PASS. `cycle-check` validates the dated architecture
  row and unchanged task contracts. During drafting it rejected result text
  placed inside Step 2 and then Step 3 acceptance sections as undisclosed
  amendments; moving the unchanged record into the dedicated execution-record
  section produced the final pass. `invariant-scan` remains **12/12 rules / 39
  controls**.
- golden-E2E delta: **0**. The first restricted invocation exited before
  startup because the sandbox denied the loopback bind with `Operation not
  permitted`; the authorized rerun of the identical `./run golden` entry point
  passed **11/11**.

### 2026-07-30 · FEED-SHAPE — one SEC feed response observed

- owner: Codex
- commit: 6c16767a8a1cf98647a67b44813933f8f9914582
- result: PASS. The one authorized SEC US GAAP RSS request returned 200 items.
  E0's mandatory-field list is empty, so the shape condition is affirmative;
  repository-parser success remains deliberately unmeasured.
- gate acceptance: PASS. E0 confirmed G3, TERMS-GATE was affirmative, and the
  operator authorized one live feed GET. Every criterion fit
  `observations/v0.25/**` and status records. No code, config, schema,
  protected-database, or public-surface path was needed.
- preflight acceptance: PASS. `python3 tools/evidence_artifacts.py validate`
  and `./run verify-artifacts` passed with all **251** pins and both protected
  databases exact; port 8788 was free, the worktree was clean, and neither
  observation output existed. The disposable observer compiled offline and
  refused pre-existing outputs, policy drift, or a robots denial before a feed
  request.
- robots acceptance: PASS. At **2026-07-30T03:33:58Z**, the shipped
  `HttpRobotsFetcher`, `RobotsCache`, and `RobotsGate` made exactly one
  `GET https://www.sec.gov/robots.txt`; both cache and wrapper counted **1**.
  The **2,622-byte** body has SHA-256
  `72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`,
  byte-identical to v0.24. Publisher and operator gates both allowed the
  intended path, with redirects disabled and a **0.500-second** effective
  interval.
- feed-wire acceptance: PASS. Only after those checks, at
  **2026-07-30T03:34:00Z**, the monitored-contact
  `intel-platform/0.15.8` identity made exactly one redirect-disabled,
  no-retry GET of
  `https://www.sec.gov/Archives/edgar/usgaap.rss.xml`. The response was HTTP
  **200**, `Content-Type: text/xml`, no `Location` header, and **892,641
  bytes** with SHA-256
  `154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`.
  No additional publisher request occurred.
- shape acceptance: PASS. Independent offline XPath counting found **200**
  `<item>` elements. Optional `title`, `guid`, `pubDate`, `link`, and
  `description` are present and non-empty in **200/200**; optional `author` is
  present in **0/200**. The mandatory list is empty and therefore satisfied.
- parser-boundary acceptance: PASS. The repository parser was not run against
  the body. Its documented outcome is conditional and derived only from E0's
  source enumeration: if it accepts the XML, it sees 200 candidate items, uses
  the five present-value branches, conditionally converts each retained raw
  `pubDate`, and emits empty author vectors. Independent counting is not
  reported as parser success.
- storage acceptance: PASS. Raw policy, raw feed body, and report live only
  under `observations/v0.25/feed-shape/`; no fixture, protected corpus,
  configured source, or golden input changed. An observation-local
  `.gitattributes` marks the feed as binary so Git preserves the exact
  publisher bytes, including their measured trailing whitespace, without text
  normalization; the SHA-256 remained exact after staging.
- non-establishment acceptance: PASS. One response establishes nothing about
  paging, resumption-token equivalents, cursor durability, near-duplicate
  behavior, repeated-fetch politeness, conditional requests, or a live ingest.
  Step 5 is eligible but remains behind its separate operator admission
  decision.
- lifecycle acceptance: PASS. `cycle-check` passed. The staged observation,
  including the raw body, passed `invariant-scan` at **12/12 rules / 39
  controls** and R4 found no credential-bearing content. With the raw artifact
  correctly classified as binary, staged diff hygiene passed.
- golden-E2E delta: **0**. Mandatory standalone `./run golden` passed
  **11/11**.

### 2026-07-30 · ADMIT — SEC EDGAR RSS configured without harvest

- owner: Codex
- commit: 088712197c3e86e93f36a6094552dd40181e5d2c
- result: PASS. The operator admitted `sec-edgar-usgaap` under `finance` at
  `https://www.sec.gov/Archives/edgar/usgaap.rss.xml`, classified
  `PublisherPermitted`. The source is bound to the reviewed path, the
  monitored-contact identity, fresh publisher-robots plus operator deny-list
  enforcement, and total automated traffic at or below the SEC's then-current
  published ceiling.
- gate acceptance: PASS after one measured correction. The Step 5-required
  live-RSS deferral row increased the governed trigger-row population from 11
  to 12, exposing that the gate omitted its executable count control,
  `shell/tests/test_cycle_check.py`. The dated amendment added that exact path,
  which declared scope already permitted; no production, objective,
  acceptance, or done-condition permission changed.
- configuration acceptance: PASS. `config/core.json` contains the exact
  finance RSS source, `PublisherPermitted`, and explicit
  `robots_on_missing: "deny"`. SEC serves a policy today, so absence is not
  the reviewed condition and fails closed instead of copying arXiv's
  publisher-specific 404 exception.
- config-control acceptance: PASS. The focused test pins the sector, global id
  uniqueness, id, type, URL, licence, and conservative missing-policy value.
  Its fail-before run found no source and failed; the implemented control
  passed.
- no-harvest acceptance: PASS. Step 5 made no publisher request and ran no live
  harvest. Two publisher origins are configured, but only `arxiv-cs` has ever
  been harvested. The production origin-keyed robots cache and per-host limiter
  have never handled both origins in one runtime; live RSS fetching, repository
  parsing of the observed body, paging, repeated-fetch behavior, near-duplicate
  behavior, and cursor durability remain unmeasured.
- deferral acceptance: PASS. The second-publisher row closed on 2026-07-30.
  The first-live-RSS-harvest row is deferred to an operator-authorized v0.26
  runbook with declared live-RSS scope and fresh publisher gates.
- shell acceptance: PASS. The first complete rebuilt lanes each collected 284,
  passed 283, and failed the same stale trigger-row expectation; after the gate
  correction, focused controls passed 2/2 and clean Python 3.11 and 3.12 lanes
  each passed **284 collected / 284 passed / 0 skipped** with the same accepted
  third-party warning. `python3 tools/test_population.py
  /private/tmp/intel-v025-admit-py311.log
  /private/tmp/intel-v025-admit-py312.log` derived `collected=284`,
  `equivalent=true`, and `equivalent_passed=284`, with local passed 284/skipped
  0 and comparison passed 284/`on_site` skipped 0. The second input was local
  Python 3.12, not hosted evidence. The draft's nonexistent `compare`
  subcommand failed argument parsing; the cited command is the successful
  actual entry point.
- complete-matrix acceptance: PASS. `./run ci-local` passed all **20** jobs at
  the admitted configuration: workspace **135**, net **55** (**29** ingest +
  **26** cored), warning-denied current and locked Rust 1.78 lanes, clean
  clippy/fmt/ShellCheck, Python 3.11 **284/284**, embedded golden **11/11**,
  all **251** pins, and protected databases **2/2**. Independent Python 3.12
  passed **284/284**. `version-check`, `cycle-check`, JSON validation, and diff
  hygiene passed.
- invariant and evidence acceptance: PASS. `invariant-scan` remains **12/12
  rules / 39 controls**. Manifest schema 2 validated; all **251** protected
  pins and both protected databases remained exact. No protected corpus, pin,
  database, schema, dependency, lockfile, ingest source, compliance source,
  shell production source, public response, tag, or branch moved.
- golden-E2E delta: **0**. Mandatory standalone `./run golden` passed
  **11/11**, matching E0's finance-sector exclusion finding.

### 2026-07-30 · RE-MEASURE — authenticated v0.25 candidate evidence

- owner: Codex
- commit: 31449d57a744571941658f34bf4c39e512506a2f
- result: PASS. Authenticated hosted run **30513561141**, attempt **1**,
  passed all seven executable jobs at exact evidence candidate
  `779fbe55ba33dd5d196df391cc9a9eeb3ce0bbb3`.
- gate acceptance: PASS. The only remote mutation was the exact candidate push
  to neutral ref `refs/heads/codex/v0.25-evidence-779fbe5` and its
  authenticated evidence dispatch. Repository admission contains only that
  run's seven receipt/bundle pairs, the release-posture deferred report, the
  protected manifest, active runbook, and state record. No tag, `main`
  advance, publication, source, public surface, dependency, lockfile, schema,
  or protected database changed. The declared-scope diff sub-rule first fired
  after the changed evidence commit and found the table omitted the exact
  evidence and manifest paths that this gate already requires. Its dated
  correction adds only run `30513561141`'s directory, the exact v0.25 report,
  and the protected manifest; corrected `cycle-check` passed without
  broadening task authority.
- workflow-identity acceptance: PASS. Before dispatch, the remote branch's
  `.github/workflows/ci.yml` blob
  `48ea726b798f1049e0b29cce1f0c64588861c2dd` matched the local candidate
  blob exactly.
- hosted-count acceptance: PASS. Hosted counts were workspace **135**, net
  **55** (**29** `intel-ingest` + **26** `cored`), locked Rust 1.78, clean
  rustc/clippy/fmt/ShellCheck, lifecycle **196 checked / 3 retracted / 196
  matched / 0 exemptions**, and golden **11/11**.
- shell-comparator acceptance: PASS. For both Python 3.11 and 3.12,
  `tools/test_population.py` derived `collected=284`, `equivalent=true`, and
  `equivalent_passed=284`: local passed **284 / skipped 0**, while hosted
  passed **283** plus one named `on_site` skip. The skip node was
  `tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`;
  its declared reason was “on-site production audit requires protected
  corpora and built cored”.
- no-publisher-request acceptance: PASS. The hosted workflow contained no
  harvest command. A case-insensitive search of the complete run log for
  `sec.gov`, `usgaap.rss`, `harvest-arxiv`, `POST /ingest`, or an HTTP GET
  returned no matches. No hosted job made a publisher request.
- invariant acceptance: PASS. The hosted run and the post-admission local
  rerun both reported `invariant-scan` **12/12 rules / 39 controls**; hosted
  R10 reported **45** exemptions.
- signed-evidence acceptance: PASS. The seven receipt JSON files and seven
  Sigstore bundles under `evidence/ci-runs/30513561141-1/` bind the exact run,
  attempt, candidate digest, neutral source ref, repository, workflow signer,
  and GitHub-hosted runner identity.
- deferred-audit acceptance: PASS. Release-posture `./run audit-deferred`
  required attestations, accepted **7 / rejected 0** identities, confirmed the
  single-run matrix complete, and recorded **5 deferred / 2 promoted / 0
  implemented deferred subsystems**. At the largest evidenced archive of
  **2,600 documents**, exact-cosine p95 was **8.640 ms**, below the
  **16.264 ms** A3 request anchor. The **34,881-byte** report has SHA-256
  `9d7c367060d2c9f28aaf17586f7e54ab782f6f8113b64326d730cccb05cfb342`;
  `./run audit-deferred --rederive` reproduced it with attestations required.
- protected-evidence acceptance: PASS. Fourteen signed hosted files plus the
  report added fifteen schema-v2 manifest records, increasing the protected
  count from **251** to **266** pins. `python3
  tools/evidence_artifacts.py validate`, `./run verify-artifacts`, and
  `./run evidence-report` passed; both protected databases remained exact.
- remote-disposition acceptance: PASS. Read-only post-dispatch resolution
  found remote `main` unchanged at
  `64002678672a601804e5f67886c73fffb4d212c8`, historical
  `refs/heads/candidate/v0.16.0` unchanged at
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394`, and the neutral evidence ref at
  the exact v0.25 candidate. No `v0.16.0` tag exists.
- golden-E2E delta: **0**. Hosted and mandatory standalone golden each passed
  **11/11**.
