# PROGRESS-v0.17.md — append-only execution record

This file records v0.17 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-28 · ACTIVATE — v0.17 admitted

- owner: Codex
- commit: 9aa74c4
- result: PASS for cycle activation only; E0 remains unchecked. The session
  opener measured local `main` and `origin/main` aligned at
  `cdae3c922a2156701c0df0ceb4f45fc937fa7f20`.
- worktree acceptance: PASS. Before activation the only worktree change was the
  operator-supplied untracked `TASKS-v0.17-EXECUTION.md`; the activation commit
  contains only that runbook, the `AGENTS.md` v0.17 declaration, and this new
  append-only progress log.
- published-tag acceptance: PASS. Annotated `v0.15.0` remains tag object
  `b7ee3445728e1816e1622c9498ffc2f165ed5dd5`, dereferencing exactly to release
  commit `8f97205a3ed4fe82f6a5ede2febce7a5d82d9f81`.
- lifecycle acceptance: PASS. `./run cycle-check` reports active v0.17 open
  with fourteen closed execution runbooks. `./run checklist-audit` resolves the
  entering 137 checked tasks, reports the same three retractions, and finds zero
  exemptions. `git diff --check` passed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and F1–F5 measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-28 · E0 — entering state and F1–F5 measured

- owner: Codex
- commit: d8d1cd1
- result: PASS. The entering state was measured at activation-audit commit
  `79f5b6232959a13b9f4adb768c6c9f7a1bcfbcd9`; E0 makes no product change.
- entering-matrix acceptance: PASS with
  `CARGO_TARGET_DIR=/private/tmp/intel-v017-e0-ci-target`. Contrary to the
  asserted stop at job 11, the fresh-target `./run ci-local` passed **20/20**:
  **126** workspace tests, **49** net tests (**23** ingest + **26** cored),
  Python 3.11.4 shell **243/243**, warning-denied offline/net builds, clippy,
  fmt, ShellCheck, floor byte-compilation, locked Rust 1.78 check/test,
  `invariant-scan` **11/11 rules / 19 controls**, all **131/131** pins, both
  protected databases exact, and golden **11/11**. Standalone golden and every
  named lifecycle/artifact/invariant command also passed. Clean Python 3.12.13
  resolved **21/21** exact packages and passed **243/243**.
- F2 rate acceptance: PASS and classified. The exact User-Agent wire test
  failed **20/20** at HEAD and **10/10** at published release commit
  `8f97205a…`, even though the full suite passed it once. It is deterministic
  when isolated under the current platform proxy and can be masked by
  full-suite timing; the test source blob is identical at the evidence
  candidate, release commit, and HEAD, so this is not post-release source drift.
- hosted comparison: RECORDED. GitHub reports zero check runs for the exact
  release commit. The authenticated Linux net receipt is at the separate,
  byte-identical-test-source candidate `43706216…` and records success with
  **23** ingest tests. No exact-release hosted execution is invented.
- F2 mechanism acceptance: PASS. macOS routes `127.0.0.1` through configured
  proxy `127.0.0.1:1082` because only `localhost` is excepted. The failing
  client reports `hyper::Error(IncompleteMessage)`, a clean EOF/FIN rather than
  reset; the raw listener does not reach its request diagnostic. With
  `NO_PROXY=127.0.0.1,localhost`, both complete raw requests arrive, each has
  **0 queued request bytes** before server close while the peer is open, and
  the test passes. The unread-byte/RST hypothesis is refuted.
- F1 table acceptance: PASS. Eleven executing cases recorded the first-segment
  truncation, lost query on multi-segment paths, retained fragment on a
  one-segment path, correct empty/trailing-slash fallback, retained port,
  stripped userinfo, lost percent-encoded/doubled-slash tail, and the
  `host?query` F1d defect. `STATE.md` contains the complete table.
- F1a/F1c acceptance: PASS. `get_text_with` calls `gate()` before the first
  fetch and before every redirected fetch. All existing ingest test policies
  are empty, root, or single-segment; none can expose multi-segment derivation.
- published-record acceptance: PASS with the distinction named. Published
  “full gate” claims describe component composition/call order, and the old
  RFC-matching statement describes matching the supplied path; no immutable
  record claims complete URL-path enforcement. The false source comment is
  corrected forward, not retracted. Retractions remain **three**.
- F5 acceptance: PASS and dependency rejected. An isolated direct `url`
  dependency grew the normal ingest graph **16 → 44**, resolving `url 2.5.8`,
  `idna 1.1.0`, `idna_adapter 1.2.2`, and ICU 2.2.0. The adapter and seven ICU
  packages declare Rust **1.86**; Cargo 1.78 cannot parse the adapter's
  edition-2024 manifest. The real `Cargo.lock` remained untouched.
- release-identity acceptance: PASS. `origin/main` remained `cdae3c9…`;
  annotated tag object `b7ee3445…` still dereferences to `8f97205a…`; all
  **131/131** pins and both protected databases match.
- golden-E2E delta: **0**; the matrix and mandatory standalone invocation both
  remained **11/11**.

### 2026-07-28 · NET-DOUBLE — raw wire fixture bypasses operator proxies

- owner: Codex
- commit: dcf7eaa
- result: PASS. The Gate remained test-support-only:
  `crates/ingest/src/net.rs` production behavior is unchanged, and the raw
  listener/header capture remains the test subject.
- mechanism acceptance: PASS. The test scopes `NO_PROXY` to
  `127.0.0.1,localhost` before constructing both real reqwest clients and
  restores the prior value through a drop guard. The operator proxy can no
  longer intercept the IP-literal raw fixture.
- rate acceptance: PASS. The exact isolated sample changed from **0/20** in E0
  to **20/20** after the fix. The complete ingest net suite passes **24/24**.
- failure-capability acceptance: PASS. A dedicated expected-panic control feeds
  `intel-platform/deliberately-different` into the same shared wire assertion
  and observes `document client User-Agent bytes differ`; the equality guard
  can still fail.
- matrix acceptance: PASS. From
  `CARGO_TARGET_DIR=/private/tmp/intel-v017-e0-ci-target`, `./run ci-local`
  reaches job 20 and passes **20/20** with **126** workspace tests, **50** net
  tests (**24 + 26**), shell **243/243**, locked Rust 1.78, zero
  rustc/clippy/fmt/ShellCheck failures, `invariant-scan` **11/11 rules /
  19 controls**, all **131/131** pins, and golden **11/11**.
- portability acceptance: PASS with boundary stated. The fix applies to
  reqwest-visible operator/system proxies honoring `NO_PROXY`; it would need
  revisiting if reqwest stopped honoring that contract, a future test omitted
  the scoped guard, or traffic were rewritten below reqwest's proxy layer.
- golden-E2E delta: **0**; the full matrix and mandatory standalone invocation
  both remained **11/11**.

### 2026-07-28 · ROBOTS-PATH — complete URL target reaches both robots gates

- owner: Codex
- commit: 59cce12
- result: PASS. Before implementation, Step 3's Gate was widened by a dated
  amendment to include `crates/ingest/src/net.rs` test support required by the
  cross-origin redirect acceptance criterion. E0 rejected the `url` dependency,
  so the implementation adds no dependency and leaves both manifests and
  `Cargo.lock` unchanged.
- fail-before acceptance: PASS. With the new controls and old implementation,
  the case table returned `/private` for `/private/secret/file`, the
  multi-segment and query rules permitted their targets, a fragment changed the
  comparison target, and the cross-origin redirect fetched its disallowed
  second document. The sibling-path allow control remained green.
- derivation acceptance: PASS. All **11** E0 rows execute with stated outputs:
  full multi-segment paths, path plus query, fragment exclusion, empty path,
  trailing slash, explicit port, userinfo, percent encoding, doubled slash, and
  a query without a path. `host_of` now separates the authority before parsing
  the tail, strips userinfo, preserves an explicit port, and no longer absorbs a
  no-path query. The source comments state the measured behavior.
- robots-corpus acceptance: PASS. Publisher policies now test a blocked
  multi-segment descendant, an allowed sibling, a query-specific denial, and a
  fragment that is excluded from matching. The focused gate set passes
  **15/15**.
- redirect acceptance: PASS. The cross-origin control observes the first
  origin's policy before its document request, then observes the second
  origin's multi-segment denial and proves the redirected document is never
  requested.
- invariant disposition: PASS with no new rule. The behavior executes directly
  at the gate and redirect sites; a static rule restating it would not add
  coverage.
- MSRV and matrix acceptance: PASS. Warning-denied
  `cargo +1.78.0 check --workspace --locked --all-targets` passed; the complete
  ingest net suite passed **29/29**. `./run ci-local` passed **20/20** with
  **131** workspace tests, **55** net tests (**29 + 26**), shell **243/243**,
  locked Rust 1.78 check/test, zero rustc/clippy/fmt/ShellCheck failures,
  `invariant-scan` **11/11 rules / 19 controls**, all **131/131** pins, and
  both protected databases exact.
- scope acceptance: PASS. No live harvest ran. The temporary pre-correction
  harvest suspension is lifted by Step 3 acceptance; T7 robots single-flight
  remains deferred because concurrent cache misses are unchanged.
- golden-E2E delta: **0**; the full matrix and mandatory standalone invocation
  both remained **11/11**.

### 2026-07-28 · HARVEST-PREFLIGHT — artifact verification is an entry-point guard

- owner: Codex
- commit: 11814e9
- result: PASS. `cmd_harvest_arxiv` invokes `cmd_verify_artifacts` before
  cargo/environment setup, destination resolution/protection, reachability, or
  any harvest request. No live harvest ran.
- gate acceptance: PASS after a pre-commit amendment. Changing `run` exposed its
  whole-file authorization pin, so Step 4's Gate was widened only to that pin's
  hash/size/provenance. The exact runner diff is the two-line harvest preflight;
  the model-profile functions/dispatch, `tools/model_profiles.py`, and the
  authorization policy are unchanged.
- fail-before acceptance: PASS. The focused shell test initially failed with
  `cmd_harvest_arxiv must invoke its named artifact-integrity preflight`.
- ordering acceptance: PASS. The offline dynamic harness observes
  `artifact-verification → cargo-check → python-environment →
  destination-protection → reachability-probe → network-request`. A forced
  verification status **37** exits as **37** with only the first event recorded,
  before any possible outbound operation.
- removal-control acceptance: PASS. A reconstructed runner with the named
  two-line preflight removed reaches later controls, and the shared assertion
  fails with a message naming `cmd_harvest_arxiv`.
- distinct-control acceptance: PASS. Artifact-integrity verification and
  protected-destination refusal keep separate calls and separate identifying
  messages; one verifies existing protected bytes/corpus facts and the other
  refuses a protected output target.
- entry-point acceptance: PASS. Repository search found one governed live
  harvest entry point: `harvest-arxiv` dispatches to `cmd_harvest_arxiv`. No
  other runner command both creates a net-enabled harvester and requests
  publisher documents.
- pin acceptance: PASS. The forward `run` authorization pin is
  `7351f2ffb7eb6def34c99c812a61a10690b6f690e9e1e44cee88790ca6dcc455`
  at **41959** bytes. Manifest validation and `verify-artifacts` pass with
  **131/131** pins and both protected databases exact; protected corpus bytes
  did not change.
- matrix acceptance: PASS. The focused control passes **1/1** and
  `./run ci-local` passes all **20/20** jobs with **244/244** shell tests,
  **131** workspace tests, **55** net tests (**29 + 26**), locked Rust 1.78,
  zero rustc/clippy/fmt/ShellCheck failures, and `invariant-scan` **11/11 rules
  / 19 controls**.
- golden-E2E delta: **0**; the full matrix and mandatory standalone invocation
  both remained **11/11**.

### 2026-07-28 · R11-BREADTH — declared scope has exact-site failure controls

- owner: Codex
- commit: a63b46b
- result: PASS. R11 retains its declared four-spelling and derived-variable
  scope; every part now has an independently reconstructible failure control.
- gate acceptance: PASS after a pre-commit amendment added
  `ARCHITECTURE.md`, which the task's own reconciliation criterion requires.
  The existing AST detector and rule schema already supported the full scope,
  so `tools/invariant_scan.py` did not change.
- direct-spelling acceptance: PASS. Separate controls fail at
  `shell/intel_shell/pipeline.py:26` for `config/entities.json`,
  `config/core.json`, `CORE_CONFIG`, and `CORE_ENTITIES`, each with its exact
  expected spelling in the finding.
- derived-variable acceptance: PASS. A fifth control assigns a module-local
  variable from `os.environ["CORE_ENTITIES"]`, passes that variable to
  `open()`, and fails at `shell/intel_shell/pipeline.py:27` with the taint source
  named.
- self-test acceptance: PASS. Focused R11 self-test executes **5/5** controls.
  The complete invariant module passes **21/21** tests, and complete
  `invariant-scan --self-test` passes **11/11 rules / 23 controls**, up from
  **19** controls.
- architecture acceptance: PASS. `ARCHITECTURE.md` closes the v0.16
  control-breadth mismatch and preserves the bounded claim: unknown future
  configuration names remain outside the four-spelling rule.
- matrix acceptance: PASS. `./run ci-local` passes all **20/20** jobs with
  **244/244** shell tests, **131** workspace tests, **55** net tests
  (**29 + 26**), locked Rust 1.78, zero rustc/clippy/fmt/ShellCheck failures,
  all **131/131** pins, and both protected databases exact.
- golden-E2E delta: **0**; the full matrix and mandatory standalone invocation
  both remained **11/11**.

### 2026-07-28 · RE-MEASURE — authenticated release evidence admitted

- owner: Codex
- commit: 7a9aa36
- result: PASS. Under the operator's one narrow authorization, exact evidence
  candidate `3481e4ba85d65c927b7d0fc3a430bc04fb094394` was pushed only to
  `candidate/v0.16.0`. Final live inspection still reports `origin/main` at
  `cdae3c922a2156701c0df0ceb4f45fc937fa7f20`, the candidate at the exact
  authorized commit, and no `v0.16.0` tag.
- gate acceptance: PASS after the pre-commit Step 6 amendment made the Gate
  contain every evidence-admission surface required by its acceptance
  criteria. No closed runbook or prior progress entry changed; no tag,
  publication, or `main` advance occurred.
- remote-workflow acceptance: PASS. Before dispatch, the remote candidate's
  `.github/workflows/ci.yml` blob
  `96e85af978981b7af9bdd8e9e11069f158f35e57` was read and proved
  byte-identical to the local candidate.
- hosted-count acceptance: PASS from workflow-dispatch run `30357365420`,
  attempt 1. All **7/7** derived identities authenticated with zero rejected
  receipt across **6** blocking jobs: `core`, `golden`, `lint`, `msrv`, `net`,
  `shell/python=3.11`, and `shell/python=3.12`. Hosted logs measured **131**
  workspace tests, **55** net tests (**29** ingest + **26** cored),
  `invariant-scan` **11/11 rules / 23 controls**, and golden **11/11**.
- shell-equality acceptance: PASS. Each hosted interpreter collected **244**
  tests and reported **243 passed / 1 declared on-site-only skip / 1 warning**;
  the same candidate locally passed all **244/244** with the same warning.
  The candidate's ingest net leg is specifically **29/29** in both hosted and
  local execution. R10 measured local **20 jobs / 24 checks**, hosted **6
  blocking jobs / 23 checks**, and the same derived exemption count **45**.
- authenticated-audit acceptance: PASS. The release-posture audit required
  attestations, accepted all **7/7** identities with zero rejection, and
  recorded **5 deferred / 2 promoted** with exact cosine p95 **8.660458 ms**.
  `evidence/v0.16.0/deferred-audit/report.json` is SHA-256
  `34804a849db56bb05cc97d4f45541702832478768119c0251769a07dd76b1bcc`
  at **34468** bytes. Authenticated re-derivation passed with
  `evidence_grade=release`, attestations required, and seven rows/triggers.
- pin acceptance: PASS. Fourteen signed hosted files plus the release audit
  added fifteen pins. Manifest validation, `verify-artifacts`, and
  `evidence-report` pass with **146/146** total — **144/144** evidence plus
  **2/2** authorization surfaces — and both protected databases remain exact.
- local-matrix acceptance: PASS. A first sandboxed invocation was a non-result
  when the raw loopback fixture could not bind. The identical permitted
  `CARGO_TARGET_DIR=/private/tmp/intel-v017-step6-ci-target ./run ci-local`
  then passed all **20/20** jobs: **131** workspace tests, **55** net tests
  (**29 + 26**), shell **244/244**, locked Rust 1.78, zero
  rustc/clippy/fmt/ShellCheck failures, `invariant-scan` **11/11 rules / 23
  controls**, persisted fingerprints, and all protected evidence.
- scope acceptance: PASS. This task changes only authenticated hosted/audit
  evidence, its manifest admission, and active cycle/status records. It
  changes no product path, public response, schema, dependency, lockfile,
  protected corpus byte, published release, tag, or `main` ref.
- golden-E2E delta: **0**; the full matrix and mandatory standalone invocation
  both remained **11/11**.
