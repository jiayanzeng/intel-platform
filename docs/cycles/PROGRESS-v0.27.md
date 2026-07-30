# PROGRESS-v0.27.md — append-only execution record

This file records v0.27 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-30 · ACTIVATE — v0.27 admitted with its supplied scope table

- owner: Codex
- commit: e53cc729483b161ea59ffdd7d69726c2fb47e98d
- result: PASS. The supplied runbook's declared scope parsed in its original
  executable Markdown-table dialect after the activation anchor existed; no
  translation or scope correction was required.
- worktree acceptance: PASS. Before activation the only worktree item was the
  operator-supplied untracked
  `docs/cycles/TASKS-v0.27-EXECUTION.md`. Implementation commit
  `e53cc729483b161ea59ffdd7d69726c2fb47e98d` contains only that runbook, the
  `AGENTS.md` v0.27 declaration, and this progress-log skeleton. Its immediate
  parent remains the unamended v0.26 post-push audit
  `e0d43ff45243aa6dda627563838f33b3483b6774`.
- entering-ref acceptance: PASS with the runbook's branch-name hypothesis
  corrected. Before activation, HEAD was post-push audit
  `e0d43ff45243aa6dda627563838f33b3483b6774` on branch
  `codex/v0.23-action-migration`, not on local `main`; local `main` remained
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. Read-only remote inspection
  resolved `main` and the peeled v0.16.1 tag to closing commit
  `397d100ae425d5d059cef8a8ddb2ac13cfde52f5`, with annotated tag object
  `ae593e882898b9c49d5e91e2d50b6ca1f02ac49b`; historical
  `refs/heads/candidate/v0.16.0` remained
  `3481e4ba85d65c927b7d0fc3a430bc04fb094394`, and
  `refs/heads/codex/v0.26-evidence-1cd88ac` remained
  `1cd88acd99704cc76c866331e505db446936e469`. No ref changed, and
  `STATE.md`'s header was not given a mutable branch-hash assertion.
- lifecycle acceptance: PASS. `cycle-check` reports active v0.27 open with
  twenty-four closed execution runbooks and three historical runbooks.
  `checklist-audit` passes **208 checked / 3 retracted / 208 matched / 0
  exemptions**. `progress-check` correctly reported that the new skeleton had
  no dated entry before this audit record existed.
- scope acceptance: PASS. The activation commit is the scope anchor, so its
  `activation..HEAD` diff is empty. The static release-intent rule accepts the
  complete declared release-authority set.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and drafted-gate measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- publisher-request acceptance: PASS. Activation invoked repository and
  read-only Git remote ref commands only; it made no request to a publisher
  origin.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-30 · E0 — entering state rebuilt and G1–G7 settled

- owner: Codex
- commit: ddb7cb8eb54cca10437b73b15e54c61c2ae3d7f9
- result: PASS. All seven bounded questions carry executed or source-grounded
  measurements in the runbook; no decision reserved for a later operator gate
  was silently taken.
- entering-matrix acceptance: PASS. `./run ci-local` passed all **20** jobs:
  **139** workspace tests, **56** net tests, warning-denied current and locked
  Rust 1.78 lanes, clippy, fmt, ShellCheck, floor byte-compilation,
  invariant-scan **12 rules / 44 controls**, and embedded golden. Clean Python
  3.11.4 and 3.12.13 rebuilds each collected and passed **291**, failed zero,
  and skipped zero. `tools/test_population.py` derived
  `collected=291`, `equivalent=true`, and `equivalent_passed=291`.
- standalone-tool acceptance: PASS. Standalone golden passed **11/11**;
  evidence-report, cycle-check, checklist-audit, progress-check, version-check,
  invariant-scan, and root export-check passed. Export coverage was **99
  derived / 7 required / 179 exported**. Sandboxed loopback and package-registry
  failures were environment non-results and their actual entry points passed
  after the required permission reruns.
- G1 acceptance: PASS by reading and execution. RSS reads the complete current
  body and has no cursor/watermark/disappearance field, log, or continuity
  test. Fresh-archive `/ingest` returned **200 fetched / 200 new /
  `ok:true`**, then **200 fetched / 0 new / `ok:true`** for the identical
  window. A failure-capable database trigger proved canonical reassignment did
  not run on the second call. A completely advanced latest-200 window would
  report ordinary **200/200 success** and no lost filing.
- G2 acceptance: PASS. Direct parsing confirmed the drafted **200** items,
  `16:13:52`–`17:31:22 EDT` endpoints, **4,650-second / 77.5-minute** span,
  **11.0-second** median gap, **215.0-second** maximum gap, `{16:133,17:67}`
  hour counts, exact channel description, and unchanged
  `Wed, 29 Jul 2026 21:50:03 EDT` build/publication date at both byte-identical
  capture times.
- G3 acceptance: PASS. Committed evidence has no captured `ETag` or
  `Last-Modified`. The locked client sends its installed `User-Agent` and
  reqwest's `Accept: */*`, with no `If-None-Match` or `If-Modified-Since`.
  The observation gap was recorded without a request or implementation
  proposal.
- G4 acceptance: PASS. Every admission-describing sentence in `AGENTS.md` and
  `ARCHITECTURE.md` was enumerated and classified. The two true-of-neither
  readings are the unqualified opening claims at `ARCHITECTURE.md:67` and
  `AGENTS.md:417-421`, because only `artifacts[]` can carry the chain while
  `pinned_files[]` rejects `admission`.
- G5 acceptance: PASS. Temporary-config, production-config, dispatcher,
  new-subcommand, direct-observer, and deferral paths were priced with exact
  successful request counts and pin effects. The viable no-repository-change
  production-runtime construction costs four bounded publisher requests; no
  path was executed.
- G6 acceptance: PASS. The same 200-document body was ingested twice into one
  fresh archive with the measured responses and canonical-reassignment
  failure control stated above.
- G7 acceptance: PASS. Whether the core-internal named `/ingest` response is a
  §8 named surface is recorded as a reasoned question for R-CLOSE, not decided
  at E0.
- manifest/object acceptance: PASS. The manifest is **165,488 bytes**; two
  consecutive full verifications took **0.21 s / 0.23 s real**. Both protected
  databases and all **286** pins matched. Local and activation-time remote
  object inspection re-verified annotated v0.16.1 tag object
  `ae593e882898b9c49d5e91e2d50b6ca1f02ac49b`, closing commit
  `397d100ae425d5d059cef8a8ddb2ac13cfde52f5`, and release parent
  `b9af84b8785bcd52c16ab0225d66386ecd872c4d`.
- golden-E2E delta: **0**; standalone and embedded outcomes remain byte-identical
  at **11/11**.
- publisher-request acceptance: PASS. E0 issued **zero** publisher requests.
- protected/config/ref acceptance: PASS. `STATE.md`, `config/core.json`,
  `config/schedule.json`, `run`, the evidence validator, the manifest, and all
  protected/pinned bytes are unchanged. No working-repository ref was created,
  moved, or deleted.

### 2026-07-30 · WINDOW-MEASURE — latest-200 margin derived from pinned bytes

- owner: Codex
- commit: 5eee3f963b9e48a305eb426023bfa1b79df6525b
- result: PASS. A committed point-of-use test now derives the latest-window
  timing distribution from the pinned SEC response, and the observation record
  states both the measured margin and its limits.
- derivation acceptance: PASS. Focused replay passed **2/2**. The new test first
  enforces 892,641 bytes and SHA-256 `154556cd…`, then derives **200** items,
  oldest `16:13:52 EDT`, newest `17:31:22 EDT`, **4,650 seconds / 77.5
  minutes**, 199 gaps, **11 seconds median**, **215 seconds maximum**, and hour
  population `{16:133,17:67}`. It derives the complete gap histogram and
  confirms the channel build/publication date.
- criterion acceptance: PASS. For consecutive successful polls over a stable
  fixed latest-N identity set, coverage holds if and only if the poll interval
  is shorter than the time the window advances by N items. The named terms are
  the **600-second poll interval** and the **4,650-second observed latest-200
  span**, for a measured ratio of **7.75×**; the poll consumes **12.90%** of
  the observed span.
- evidence-limit acceptance: PASS. The record names one post-close
  77.5-minute window on one Wednesday and expressly does not establish
  peak-season density, deadline-day density, or density during hours neither
  live sample covered.
- idle-sample acceptance: PASS with a drafted value refuted. Both captures were
  outside filing hours with identical bytes, hash, and `lastBuildDate`.
  Executed timestamp subtraction measures **5h44m39.680936s**, not the
  runbook's **7h28m**. A dated amendment records the author error. The unchanged
  observable representation refutes the ten-minute statement as idle observable
  behavior and, separately, fails to test window velocity because no filings
  arrived.
- regression acceptance: PASS. Warning-denied workspace tests passed **140**;
  warning-denied net tests passed **31 ingest + 26 cored = 57**. Clippy and fmt
  passed. The SEC identity control remained **200 kept / 0 dropped**.
- golden-E2E delta: **0**; standalone golden remains byte-identical at
  **11/11**.
- boundary acceptance: PASS. `config/schedule.json` and production source are
  unchanged; no scheduler ran, no publisher request occurred, and no protected
  or pinned byte changed.

### 2026-07-30 · CADENCE-CRITERION — architectural reason corrected

- owner: Codex
- commit: f4f877164216e38b56dd31eb4242afd8a7014c12
- result: PASS. A new dated architecture row records latest-window advance
  time, rather than the ten-minute rebuild description, as the governing
  cadence quantity. The configured and recorded value remains 600 seconds.
- append-only correction acceptance: PASS. SHA-256 comparison proves the v0.26
  cadence row is byte-identical before and after this task. The new v0.27 row
  follows it and records **600 seconds against 4,650 seconds**, **7.75×**
  span/poll margin, **12.90%** span consumed per poll, and the peak-season,
  deadline-day, and uncovered-hour gaps.
- number-decision acceptance: PASS. This one sample's positive margin does not
  imply a value change, so no change is recommended or applied.
- executable-record acceptance: PASS. The new scheduler test parses the v0.27
  architecture row, resolves the committed SEC job through `load_schedule` and
  `build_jobs`, and compares both values. Its planted 601-second row raises
  `architecture SEC cadence 601 != scheduled 600`, proving the test is
  non-vacuous.
- shell acceptance: PASS. Focused scheduler tests passed **10/10** under both
  interpreters. Complete constrained Python 3.11.4 and 3.12.13 lanes each
  collected and passed **292**, failed zero, and skipped zero. The comparator
  derived `collected=292`, `equivalent=true`, and `equivalent_passed=292`.
- separation acceptance: PASS. SHA-256 comparison proves the v0.25 terms row is
  byte-unchanged. The new row expressly says the cadence correction satisfies
  neither the terms condition nor the coverage-detection objective.
- golden-E2E delta: **0**; standalone golden remains byte-identical at
  **11/11**.
- boundary acceptance: PASS. `config/schedule.json` and `config/core.json` are
  byte-unchanged; no production source changed, no scheduler ran, and no
  publisher request occurred.

### 2026-07-30 · ADMISSION-LANGUAGE — manifest containers named and executed

- owner: Codex
- commit: 405e68fa6d144e8bca245fe5d2852980a8db3958
- result: PASS. The two G4 statements that could be read as true of neither
  schema-v2 container now name the applicable container, and an executing
  fixture proves both documented valid shapes and both exact prohibited
  shapes.
- container-language acceptance: PASS. `AGENTS.md` and `ARCHITECTURE.md`
  jointly state the disjoint capabilities in one place: `artifacts[]` requires
  the SQLite `expected` shape and carries chained `admission`; `pinned_files[]`
  accepts graded immutable bytes under `evidence/` and `observations/`, plus
  exact registered authorization paths, and forbids `admission`.
- author-rule acceptance: PASS. The operating contract now requires each task
  demanding a pinned byte to name its target container. A requirement
  expressible by neither container is an author-side defect to record and
  correct, not a condition to work around. The fifth and sixth v0.26 instances
  remain closed historical dispositions and are cited only as motivating data.
- executable-contract acceptance: PASS. The new fixture validates one
  `artifacts[]` entry and three `pinned_files[]` entries covering evidence,
  observation, and authorization grades. Its mutations execute the exact
  rejections `pinned_files[0]: keys differ; missing=[],
  extra=['admission']` and `artifacts[0]: keys differ;
  missing=['expected'], extra=[]`. Focused execution passed **1/1** in both
  Python lanes.
- limitation acceptance: PASS. The contract states that the fixture proves
  documentation/validator agreement today but cannot prevent future drift;
  v0.27's prohibition on editing the validator controls that limitation here.
- shell acceptance: PASS. Complete constrained Python 3.11.4 and 3.12.13 lanes
  each collected and passed **293**, failed zero, and skipped zero. The
  comparator derived `collected=293`, `equivalent=true`, and
  `equivalent_passed=293`.
- invariant acceptance: PASS. `invariant-scan` remains **12 rules / 44
  controls**; `cycle-check`, `version-check`, and `git diff --check` passed.
- forbidden-file acceptance: PASS. `tools/evidence_artifacts.py` is unchanged at
  SHA-256
  `3e5e0c5ff6e12c25180833124faaaf91dc43b5171e893e83500e029d04e99af5`,
  and `config/protected-artifacts.json` is unchanged at SHA-256
  `8711aa1b95d6071c6492594aa20a3c4ab8a1756ffe4b5ed72b5208f39ed9a3da`.
- golden-E2E delta: **0**; standalone golden remains byte-identical at
  **11/11**.
- boundary acceptance: PASS. No production source changed, no prior record was
  reopened, and no publisher request occurred.

### 2026-07-30 · COVERAGE-DETECTION — id-only overlap made visible

- owner: Codex
- commit: 2c0c9d11cc67c93ccbd1751b7eaff84b84919148
- result: PASS. The operator authorized Option 1, and every successful
  non-paged source now carries a pre-insert id-overlap outcome in its `/ingest`
  result and a human-readable log without failing or discarding the poll.
- decision acceptance: PASS. The selected claim is dated and conditional on
  contiguous publication-order windows and ids stable across polls. The pinned
  body re-derives **200 items / zero ascending inversions**, **200 unique
  GUIDs / 200 distinct accession numbers**, the SEC host and accession-to-GUID
  correspondence, and source-id-plus-GUID parser identity. Accession
  immutability supports stability; future publisher re-issue behavior remains
  a stated dependency.
- siting acceptance: PASS. Cored calls the store's held-set assessment before
  every tail `append_new`, with `sel.source.id()` and that source's `docs`.
  The per-source outcome is computed before commit and carried into
  `IngestSourceResult`, not defaulted or back-filled. The result and log expose
  `first_window`, `empty_window`, `overlap`, `gap_detected`, raw publisher
  boundary strings for gaps, and explicit `not_applicable_paged` for OAI-PMH.
- failure-direction acceptance: PASS. A gap finding does not fail the poll; the
  incoming window is committed. Empty overlap is deliberately conservative:
  publisher re-issue or GUID-form changes can produce a visible false positive,
  and neither zero false positives nor a measured loss size is claimed.
- firing acceptance: PASS. A genuinely disjoint pinned-window sequence stored
  67 older items, omitted 66 intervening items, and ingested 67 newer items. It
  returned `gap_detected`, raw boundary pair
  `Wed, 29 Jul 2026 16:26:17 EDT` /
  `Wed, 29 Jul 2026 17:00:13 EDT`, and committed all 67 incoming rows.
  Re-assessment after insertion returned `overlap`, proving the response field
  came from the pre-insert check.
- non-misfiring acceptance: PASS. An empty per-source store ingesting the
  pinned 200-document window reported `first_window`; the identical second
  window reported `overlap` and **0 new**. A combined non-paged batch
  independently reported overlap for `techwire` and a gap for `osdaily`,
  proving per-source partitioning. The paged fixture reported
  `not_applicable_paged` and committed its cursor.
- invariant acceptance: PASS. R12 now has **18 controls** and the repository
  total is **12 rules / 46 controls**. The new insert-before-query and
  combined-batch mutations each produced the registered expected failure;
  `cycle-check`, `version-check`, fmt, and `git diff --check` also passed.
- regression acceptance: PASS. Full `ci-local` passed **20/20** jobs with
  warning-denied **145** workspace tests, **62** net tests (**32 ingest,
  including three replay tests, + 30 cored**), locked Rust 1.78, clippy, fmt,
  and ShellCheck. Complete constrained Python 3.11.4 and 3.12.13 lanes each
  collected and passed **293**, failed zero, and skipped zero. The first
  sandboxed Python 3.12 attempt lacked its required loopback/process
  permissions and was a non-result; its real entry point passed on rerun.
- identity acceptance: PASS. The 200-document SEC corpus remains **200 kept /
  0 dropped**; the same fixture run separately kept one filings-digest
  document. `crates/extract` and `crates/view` are byte-unchanged.
- golden-E2E delta: **0**; standalone golden remains byte-identical at
  **11/11** with its Hamming-12 collapse.
- boundary acceptance: PASS. `config/schedule.json`, `config/core.json`, and
  `config/protected-artifacts.json` are byte-unchanged. The allowed
  `crates/ingest/src/lib.rs` and `crates/ingest/src/rss.rs` production
  permissions were unused; no compliance, extract, view, or shell production
  source changed. No scheduler ran and no publisher request occurred.

### 2026-07-30 · MULTI-ORIGIN — mixed robots dispositions isolated live

- owner: Codex
- commit: 641b8021014e2599012a1befcf1d6f0961bce91c
- result: PASS with source-level limitations recorded. One authorized,
  bounded, plaintext-observable runtime exercised arXiv then SEC in the same
  process-scoped robots cache. arXiv's permissive missing-policy did not change
  SEC's independently evaluated restrictive-policy result. arXiv content timed
  out before a page committed; SEC returned and stored 200 documents.
- decision acceptance: PASS. The operator authorized Step 6 on 2026-07-30
  after correcting its rationale: unit tests already prove cache keying/reuse
  and per-host independence, so the first live measurement unique to this
  configuration is coexistence of opposing robots dispositions.
- paging-bound acceptance: PASS. Exact focused execution proved
  `max_pages: 1` permits at most one OAI-PMH content request and checkpoints a
  non-terminal token plus `pending_high_water` without advancing completed
  `high_water`; the cursor lifecycle test also passed. An initial incorrectly
  filtered zero-test invocation was classified as a vacuous non-result. The
  live timeout occurred before parsing, so no cursor or high-water state was
  written.
- protected-target acceptance: PASS. Manifest validation and
  `verify-artifacts` passed before and after with **286** pins and both
  protected databases exact. A deliberate `data/core.db` target exited **2**
  before network. The live archive
  `data/live-20260730T125247Z-99839.db` remained ignored and unadmitted; it
  measured **253,952 bytes**, integrity `ok`, **200** SEC documents, **200**
  distinct non-null canonical ids, zero cursor rows, and SHA-256
  `47f64b7ebe690b0987b17af404b384cad2abdea7eb0e4b83e9dc54534a8d422c`.
- observer acceptance: PASS. A disposable out-of-tree net wrapper, SHA-256
  `72783cb5e1b6848d1675bd3bcf608872676781bf39520b394f9af027d91baa33`,
  wrote plaintext and refused duplicate or fifth requests before `send`; its
  two-source config SHA-256 was
  `7646cff12d6c9df9e9727cdae94bb0957c3e168fcaa2ead1f7893b66138f26c0`.
  A planted pre-existing request marker produced an actual pre-network refusal
  with no response file, proving the quota control can fail.
- request-bound acceptance: PASS. Exactly **4** application-level request
  starts crossed `send`, **2 per origin**: one robots and one content attempt.
  There was no redirect, retry, second OAI-PMH page, fifth request, or
  scheduler. Three responses were plaintext-observed; publisher receipt is not
  claimed for the timed-out arXiv content attempt.
- disposition acceptance: PASS. Derived origin
  `https://oaipmh.arxiv.org` returned HTTP 404 / 11,083 bytes / SHA-256
  `fe5a8ce88b89f96db55e8d9a7eb3d978f3d364bf31d48c4880422511e9035ab2`
  and used `allow` as `RfcAllowAll`. Derived origin
  `https://www.sec.gov` returned HTTP 200 / 2,622 bytes / SHA-256
  `72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f`
  and independently produced `Body(allow)` under `deny` after arXiv occupied
  the cache. Both bodies were byte-identical to committed captures.
- interval acceptance: PASS. Request-start intervals measured **1.827372 s**
  within arXiv, **60.004385 s** from arXiv content to SEC robots,
  **1.313344 s** within SEC, and **61.831757 s** between robots requests.
  The sequential timeout prevented a sub-floor cross-origin sample; such a
  shorter interval would be expected and correct for independent host clocks.
  The three focused cache/limiter tests each passed **1/1**.
- response acceptance: PASS as an honest partial corroboration. `/ingest`
  returned **200 fetched / 200 new**. ArXiv reported `ok:false`, zero
  documents, `not_applicable_paged`, and the timeout; SEC reported `ok:true`,
  200 documents, and `first_window`. No successful live arXiv page/cursor or
  SEC `overlap` is claimed, and the authorization was not expanded.
- non-exercise acceptance: PASS. T7 did not fire and is not nearer its trigger
  because the sources were sequential, not concurrent harvesters. A successful
  live arXiv checkpoint, a sub-floor cross-origin interval, and the 600-second
  schedule remain unexercised.
- regression acceptance: PASS. Full `ci-local` passed **20/20** jobs with
  warning-denied **145** workspace and **62** net tests (**32 ingest + 30
  cored**), locked Rust 1.78, invariant-scan **12 rules / 46 controls**,
  clippy, fmt, and ShellCheck. Python 3.11.4 and 3.12.13 each collected and
  passed **293** with zero skips.
- golden-E2E delta: **0**; standalone golden remains byte-identical at
  **11/11**.
- boundary acceptance: PASS. `config/core.json`, `run`,
  `config/protected-artifacts.json`, both protected databases, and production
  compliance, ingest, extract, view, and shell source are byte-unchanged. The
  archive was not admitted to protected evidence or golden.

### 2026-07-30 · RE-MEASURE — neutral candidate authenticated on hosted CI

- owner: Codex
- commit: 5713e9c4c87c3af1327e038eff4c390e042a29a4
- result: PASS. Exact evidence candidate
  `f2b5f7a9ded1b21f3815752cc9e310bd29c1478e` was pushed only to neutral
  ref `refs/heads/codex/v0.27-evidence-f2b5f7a`; hosted run
  **30545771070**, attempt **1**, passed all seven executable jobs at that
  exact candidate and ref.
- neutral-ref acceptance: PASS. Remote `main`, the historical candidate refs,
  and annotated `v0.16.1` did not move. No tag was created. Workflow blob
  `48ea726b798f1049e0b29cce1f0c64588861c2dd` was the candidate CI
  configuration; the report-only dependency-drift job skipped as designed.
- population acceptance: PASS. Fresh local Python 3.11.4 and 3.12.13 lanes
  each collected and passed **293** with zero skips. For each hosted lane,
  `tools/test_population.py` derived
  `{"collected":293,"equivalent":true,"equivalent_passed":293,"hosted":{"on_site_skipped":1,"passed":292,"skipped":[{"node_id":"tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt","reason":"on-site production audit requires protected corpora and built cored"}]},"local":{"passed":293,"skipped":0},"schema_version":1}`.
  The single hosted skip was named, carried that declared reason, and was
  marked `on_site`.
- receipt acceptance: PASS. Seven receipts and seven paired Sigstore bundles
  were registered in `pinned_files[]` with `supporting` grade and no
  `admission` key. Each bundle verified the exact receipt bytes, repository,
  CI workflow identity, candidate digest, neutral source ref, and
  GitHub-hosted runner policy. The first batch-verification harness
  accidentally included its own temporary decoder file and was a harness
  non-result; the corrected exact fourteen-file entry point verified all
  seven pairs.
- release-report acceptance: PASS. The release-posture report is **34,995
  bytes**, SHA-256
  `67b0c7a5488293cba8bc38e410bd24c748af6f1598481a23a37eeb623ec8dc64`,
  grade `release`, with attestations required. It observed and accepted **7**
  identities, rejected **0**, found no matrix finding, and recorded **5
  deferred / 2 promoted / 0 implemented deferred subsystems**. A first clean
  detached re-derivation lacked ignored protected databases, and a second
  lacked the new logical receipt paths; both were construction non-results.
  After exact protected bytes and the already-authenticated receipts were
  mirrored into the detached candidate, re-derivation passed all seven rows.
- manifest acceptance: PASS. The fourteen hosted files plus the report moved
  the manifest from **286** to **301** pins. `python3
  tools/evidence_artifacts.py validate`, `./run verify-artifacts`, and
  `./run evidence-report` passed; both protected SQLite artifacts remained
  byte-identical. The validator was not changed.
- no-publisher acceptance: PASS. Candidate workflow inspection found no
  publisher URL or publisher-directed ingest command. Complete hosted-log
  search found exactly two `usgaap.rss` occurrences, both local `PIN MATCH`
  output for the committed SEC observation; broader `curl` search found only
  the rustup installer URL. No hosted publisher request occurred.
- scope acceptance: PASS. The dated amendment fixes the receipt placeholder
  to `evidence/ci-runs/30545771070-1/**` and corrects the activation table's
  contradiction by allowing `config/protected-artifacts.json` only for this
  required pin registration. The exact evidence directory, manifest change,
  and amendment landed together in the implementation commit.
- regression acceptance: PASS. Full `ci-local` passed **20/20** jobs with
  warning-denied **145** workspace tests, **62** net tests (**32 ingest + 30
  cored**), invariant-scan **12 rules / 46 controls**, locked Rust 1.78,
  clippy, fmt, ShellCheck, and shell **293/293**. The first sandboxed rerun
  could not bind the net test's loopback socket and was a non-result; the
  exact command passed with its required local permissions.
- golden-E2E delta: **0**; hosted, embedded, and required standalone golden
  remain byte-identical at **11/11**.
- boundary acceptance: PASS. No production source, protected database,
  publisher configuration, schedule, document identity, `config/core.json`,
  or publisher ref changed. Step 8 remains behind its separate operator
  publication decision.

### 2026-07-30 · R-CLOSE — v0.17.0 tagged close

- owner: Codex
- commit: d5969207835c9f27f461d292b169ccb8d6ae5a46
- result: PASS. Release implementation commit
  `d5969207835c9f27f461d292b169ccb8d6ae5a46` prepares v0.17.0 and is the
  untagged immediate parent of the closing tree. No corrective trigger was
  visible at entry; the publication trigger is the operator's explicit
  decision to ship the authenticated coverage detector, corrected cadence
  criterion, executable admission-language contract, and bounded
  mixed-disposition measurement.
- closing-evidence acceptance: PASS. Authenticated candidate
  `f2b5f7a9ded1b21f3815752cc9e310bd29c1478e` and run **30545771070**
  attempt **1** remain separate from the release parent. All seven executable
  hosted jobs passed. Release-grade verification required attestations,
  accepted **7 / rejected 0** identities, and confirmed the complete matrix.
- release-identity acceptance: PASS. G7 is now reusable: a named observable
  response shape remains versioned when its route is internal loopback; the
  access classification does not erase the contract. Adding coverage fields
  to `/ingest` therefore requires the minor **v0.17.0**. The public
  value-domain criterion does not fire because no serialized `/v1/*` field
  gains, loses, or redefines a value. The exact **38**
  `v0.16.1..d5969207835c9f27f461d292b169ccb8d6ae5a46` paths are
  classified once in eight disjoint groups in `STATE.md`.
- coverage acceptance: PASS. The selected overlap/id-only detector depends on
  contiguous publisher windows and stable ids. Pinned bytes derive 200 items
  with zero ascending inversions and 200 unique GUIDs carrying 200 distinct
  SEC accession numbers. First and identical windows respectively
  non-misfire as `first_window` and `overlap`; a 67-held / 66-omitted /
  67-incoming construction fires `gap_detected` with raw boundary strings
  `16:26:17 EDT` / `17:00:13 EDT` and still commits. Post-insert reassessment
  returns overlap, the combined batch remains partitioned by source, and
  OAI-PMH is `not_applicable_paged`. Publisher re-issue or GUID-form change
  can produce a visible false positive; zero false positives are not claimed.
- cadence acceptance: PASS. Window advance is the loss criterion. The pinned
  latest-200 sample spans **4,650 seconds / 77.5 minutes** against the
  unchanged 600-second interval: **7.75×** margin, or **12.90%** of the
  observed span consumed per poll. The v0.26 row is intact; the number did not
  change. Peak-season, deadline-day, and uncovered-hour density remain
  unmeasured. The 600-second schedule has never run and this publication does
  not authorize it.
- admission acceptance: PASS. The container-language fix addresses the
  generator of the fifth and sixth author-side unsatisfiable rules without
  reopening either record. SQLite `artifacts[]` carry corpus facts and chained
  admission; immutable `pinned_files[]` carry graded bytes and forbid
  admission. Executing fixtures accept both documented shapes and reject both
  prohibited cross-container shapes.
- source/scope acceptance: PASS. Exactly four application request starts in
  the authorized Step 6 runtime put arXiv `RfcAllowAll` and SEC
  `Body(allow)` in one process-scoped cache without policy bleed. arXiv timed
  out before a page committed; SEC stored 200 documents. The sources were
  sequential, not concurrent harvesters, so T7 did not fire and is not nearer
  its trigger. Three conditional production permissions were used:
  `crates/store/src/lib.rs`, `crates/store/src/sqlite.rs`, and
  `apps/cored/src/main.rs`; `crates/ingest/src/lib.rs` and
  `crates/ingest/src/rss.rs` were unused.
- non-exercise acceptance: PASS. No `edgar:*` mapping, conditional GET,
  `config/core.json` change, cadence change, dependency/schema change,
  protected-database change, scheduler run, or identity change occurred.
  `crates/extract` and `crates/view` are byte-unchanged; SEC remains **200
  kept / 0 dropped**.
- release-parent acceptance: PASS. At the exact committed parent,
  `./run ci-local` passed all **20** jobs: workspace **145**, net **62**
  (**32** ingest + **30** cored), warning-denied current and locked Rust 1.78
  builds, clean rustc/clippy/fmt/ShellCheck, `invariant-scan` **12/12 rules /
  46 controls**, and embedded golden **11/11**. Mandatory standalone golden
  passed **11/11**.
- population acceptance: PASS. Constrained Python **3.11.4** and **3.12.13**
  lanes each collected and passed **293** with zero skips. The authenticated
  candidate comparators separately derived equivalence from hosted 292 passes
  plus the one named, reasoned, `on_site` skip in both lanes.
- evidence acceptance: PASS. All **301** pins and both protected databases
  remained exact. Manifest size is **174,152 bytes**; consecutive complete
  verification runs were **0.16 s / 0.10 s real**. Project-root
  `export-check` passed **99** derived sources / **7** required / **180**
  exported.
- protocol acceptance: PASS. The closed record names release parent
  `d5969207835c9f27f461d292b169ccb8d6ae5a46` and evidence candidate
  `f2b5f7a9ded1b21f3815752cc9e310bd29c1478e` separately, omits the
  not-yet-knowable tag-object field, and requires the annotated v0.17.0 tag to
  target this immediate child and move atomically with `main`.
- residual acceptance: PASS. A4, editable L1, R3/R4, the measured-value
  heuristic, T7, NEGATIVE-CACHE Decision B, scheduled L2, FastAPI
  version-literal relocation, and terms-gate operator responsibility remain
  open or unchanged.
- publisher-request acceptance: PASS. R-CLOSE made no publisher request.
- golden-E2E delta: **0**.
