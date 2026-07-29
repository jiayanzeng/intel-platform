# PROGRESS-v0.19.md — append-only execution record

This file records v0.19 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-29 · ACTIVATE — v0.19 admitted

- owner: Codex
- commit: 3b5c37c
- result: PASS for cycle activation only; E0 remains unchecked. Before
  activation, local `main` and the measured `origin/main` tracking ref were
  aligned at `344124819cb3c554f851d0cac3f0f1ed08d1aa10`.
- worktree acceptance: PASS. The only pre-activation worktree item was the
  operator-supplied untracked `TASKS-v0.19-EXECUTION.md`; implementation commit
  `3b5c37c` contains only that runbook, the `AGENTS.md` v0.19 declaration, and
  this new append-only progress log.
- lifecycle acceptance: PASS. `./run cycle-check` reports active v0.19 open
  with sixteen closed execution runbooks. `./run checklist-audit` resolves the
  entering 151 checked tasks, reports the same three retractions, and finds zero
  exemptions. `git diff --check` passed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and G1–G6 measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-29 · E0 — entering state and drafted gates measured

- owner: Codex
- commit: e10b0c0
- result: PASS. The read-only Gate contains every acceptance surface; only the
  runbook status/checklist and this append-only record moved. `STATE.md`
  remained blob `f8f07f6…`, byte-identical to the entering commit.
- entering-matrix acceptance: PASS. The first sandboxed `./run ci-local` was a
  loopback-bind permission non-result; the identical permitted invocation
  passed **20/20** with **131** workspace tests, **55** net tests (**29 + 26**),
  shell **245/245** on Python 3.11.4, locked Rust 1.78, zero
  rustc/clippy/fmt/ShellCheck failures, `invariant-scan` **11/11 rules / 23
  controls**, all **161/161** pins, protected databases **2/2**, and golden
  **11/11**. A clean constrained Python 3.12.13 rebuild resolved **21/21**
  packages and passed shell **245/245**.
- refs/G2 acceptance: PASS. Local and remote main are `344124819c…`; annotated
  `v0.15.2` is locally and remotely object `22beef8e…`, peeled to reachable
  release commit `b3c4c4d3…`. These contradict `STATE.md`'s header assertion of
  `f13c6129…` and an absent remote tag, while cycle, checklist, progress, and
  version checks all passed over that false status.
- G1 acceptance: PASS and CONFIRMED. A temporary executing control measured a
  first unreachable result remaining cached at fetches/calls **1/1** and an
  expired allowing policy overwritten by unreachable and then remaining cached
  at **2/2**. The test was removed and the source blob restored exactly.
- G5 acceptance: PASS and CLOSED CLEAN. A temporary production-entry control
  rejected a relative URL before the gate with robots/page fetches **0/0**;
  initial and redirected network URLs pass through `reqwest::Url::parse/join`,
  so the helper sentinels cannot key a production request. The test was removed
  and the source blob restored exactly.
- G6 acceptance: PASS. Named acquisition tests prove the page and robots-policy
  limiters are consulted; the crawl-delay ratchet test measures a 10-second
  publisher delay, but no test measures the default 0.500-second harvest-page
  interval.
- G3 acceptance: PASS and CONFIRMED with corrected measured quantities.
  Root-run Repomix 1.17.0 wrote **4,887,220 bytes / 339 included files** after
  collecting 340 and security-excluding one Rust file. Evidence contributes
  **1,613,565 bytes / 178 files**, closed cycles through v0.11 contribute
  **657,725 bytes / 17 files**, and `STATE.md` is **534,657 bytes / 8,133
  lines**.
- object/pin acceptance: PASS. Remote objects were re-read after the controls;
  standalone `verify-artifacts` passed **161/161** pins and protected databases
  **2/2**. No protected file or published object changed.
- golden-E2E delta: **0**; mandatory standalone `./run golden` passed
  **11/11**.

### 2026-07-29 · STATUS-TRUE — publication status made executable

- owner: Codex
- commit: 9834a8e
- result: PASS. The reconciliation executes inside `cycle-check`; its Gate
  contains the checker, focused shell tests, forward `STATE.md` correction, and
  runbook/progress status only. No closed runbook or historical append moved.
- fail-before acceptance: PASS. With the checker present and the false header
  intact, `cycle-check` exited **1** with exactly two messages:
  `publication disposition agreement` for a reachable annotated release versus
  pending publication, and `publication assertion freshness` for asserted
  `origin/main` `f13c6129…` versus measured `344124819c…`.
- focused-test acceptance: PASS. `test_cycle_check.py` passed **20/20** on both
  Python 3.11.4 and Python 3.12.13. The new controls fail both rules and all
  three ref labels, accept a current header, and exclude the historical body.
- publication-audit acceptance: PASS. The forward header/audit records local
  and remote main `344124819c…`, annotated object `22beef8e…`, peeled target
  `b3c4c4d3…`, and publication CI run `30375179895`, attempt **1**, event
  `push`, exact head, completed status, and `success` conclusion. No run was
  dispatched.
- pass-after acceptance: PASS. Cycle, checklist, progress, and version tools
  plus the reconciliation are green; `invariant-scan` remains **11/11 rules /
  23 controls**.
- scope acceptance: PASS. The v0.18 closing record, `PROGRESS-v0.18.md`, every
  closed runbook, and every historical `STATE.md` append remain unchanged. No
  production Rust path, dependency, lockfile, schema, protected database, or
  public surface changed.
- golden-E2E delta: **0**; mandatory standalone execution passed **11/11**.

### 2026-07-29 · EXPORT-BUDGET — review corpus reduced losslessly

- owner: Codex
- commit: d33e092
- result: PASS. Root-run Repomix 1.17.0 moved from **4,887,220 bytes /
  339 included files** to a fixed-point **2,640,795 bytes / 146 files**.
- selection acceptance: PASS. The configured export excludes `evidence/**` and
  the exact `docs/cycles/{TASKS,PROGRESS}-v0.{8,9,10,11}*` pattern, retains
  `Cargo.lock`, `config/protected-artifacts.json`, `AGENTS.md`, and `run`, and
  contains all **89/89** tracked files under `crates/`, `apps/`, `tools/`, and
  `shell/`. The Repomix security scan is disabled so it cannot silently omit a
  source; registered self-testing invariant R4 remains the credential control.
- archival acceptance: PASS. The pre-split `STATE.md` was **535,858 bytes** at
  SHA-256
  `9553fb682d04e1b2a925e90bd11ab2ae867bd0e6025193abde9a643c9239f3b6`.
  The byte-identical archived block is **297,739 bytes** at SHA-256
  `3233af5b4c148f7a7f4700edba3238dc67245f28d83dc07cc53c26ebdca6a414`.
  Substituting it once for the retained pointer reconstructed the exact
  **535,858-byte** pre-split hash. No repository file was deleted.
- artifact acceptance: PASS. Manifest validation and `verify-artifacts` passed
  **161/161** pins and protected databases **2/2** after the split.
- status acceptance: PASS. `cycle-check`, `checklist-audit`,
  `progress-check`, `version-check`, and Step 2's publication reconciliation
  are all green after this append names the real implementation commit.
- scope acceptance: PASS. No production path, dependency, lockfile, schema,
  protected artifact, public surface, or historical closed-cycle record moved.
- golden-E2E delta: **0**; mandatory standalone `./run golden` passed
  **11/11**.

### 2026-07-29 · NEGATIVE-CACHE — transient failure gets a chosen policy

- owner: Codex
- commit: 499716d
- result: PASS. `Unreachable` remains fail-closed but is cached for a named
  **300-second** negative TTL instead of the ordinary **86,400-second** policy
  TTL.
- gate acceptance: PASS. The dated runbook amendment widened Step 4 only to the
  one production cache-construction call and required status records. No
  document-request control flow, connector behavior, `/v1/*` surface, schema,
  dependency, lockfile, protected artifact, limiter, crawl-delay ratchet, or
  single-flight behavior moved.
- fail-before acceptance: PASS. Both new controls exited **101** before the
  implementation: the standalone unreachable result and the good-policy
  overwrite result each remained cached past their expected negative boundary.
- Decision A acceptance: PASS. `ROBOTS_NEGATIVE_TTL` is named beside
  `ROBOTS_TTL` and passed into production. Executing controls prove
  `Unavailable` retains the ordinary TTL, repeated unreachable denial performs
  no fetch before 300 seconds, and the result is retried at expiry.
- Decision B acceptance: PASS and DEFERRED WITH TRIGGER. The operator selected
  no stale-policy fallback on 2026-07-29. `Unreachable` still overwrites an
  expired good policy and denies. Reconsideration requires a measured live
  transient robots outage for an admitted publisher while a usable
  last-known-good policy exists, followed by explicit operator authorization.
- fail-closed acceptance: PASS. Existing tests re-prove default 404 handling,
  explicit publisher `Disallow`, network-without-cache rejection before a
  request, and the subtractive operator deny-list. `apply_crawl_delay` remains
  byte-identical at slice SHA-256 `ea16d8cac28b094f23eba38c5656c800a79515c049b57f0a85f85abe6bd77327`;
  the limiter/`acquires` slice remains
  `4280d757274fd3ae739a2e600054b1fe517287cff64e56abea82176ea73c38ed`.
- matrix acceptance: PASS. `./run ci-local` passed **20/20** with **133**
  workspace tests, **55** net tests (**29 + 26**), locked warning-denied Rust
  1.78, Python 3.11 shell **248/248**, invariant **11/11 rules / 23 controls**,
  all **161/161** pins, protected databases **2/2**, and clean
  clippy/fmt/ShellCheck. Python 3.12.13 independently passed **248/248**.
- status acceptance: PASS. Cycle, checklist, progress, and version checks are
  green after this append names the real implementation commit.
- golden-E2E delta: **0**; standalone and full-matrix runs passed **11/11**.

### 2026-07-29 · PREVIEW-DISPOSITION — unsupported preview retired

- owner: Codex
- commit: 2cabfcc
- result: PASS. The operator selected exactly one disposition: **retire**.
  Implementation commit `2cabfcc` deletes the coupled `diagnostics` /
  `robots-preview` feature declarations, preview binary, robots-only
  fetch/helper and wire test, diagnostic API and its two tests, and
  diagnostics-only parser/matcher provenance bookkeeping.
- gate acceptance: PASS. Only the preview's own sources, manifests, feature
  declarations, tests, binary, `ARCHITECTURE.md`, and required status records
  moved. The public `/v1/*` surface, SQLite schema, dependency set,
  `Cargo.lock`, protected artifacts, and default robots-policy decisions are
  unchanged.
- disposition acceptance: PASS. Cargo metadata shows no feature or binary
  target for `intel-compliance`; `intel-ingest` exposes only `net` and its
  library target. `ARCHITECTURE.md` records retirement and preserves the
  published v0.15.2 tag plus v0.18 wire observations as historical evidence.
- supplemental-matrix acceptance: PASS. Before retirement, compliance
  `--features diagnostics` passed **42/42**, while ingest
  `--features robots-preview` passed **30/30** library plus **1/1** binary
  tests. After retirement both commands exit **101** with
  `does not contain this feature`; surviving all-features suites pass
  compliance **40/40** and ingest **29/29**, with no binary suite.
- default-build acceptance: PASS. `./run ci-local` passed **20/20** with
  **133** workspace tests, **55** net tests (**29 + 26**), warning-denied
  current and Rust 1.78 builds, Python 3.11 shell **248/248**, invariant
  **11/11 rules / 23 controls**, **161/161** pins, protected databases
  **2/2**, and clean clippy/fmt/ShellCheck. Python 3.12.13 independently
  passed **248/248**.
- status acceptance: PASS. Cycle, checklist, progress, and version checks are
  green after this append names the real implementation commit.
- golden-E2E delta: **0**; standalone and full-matrix runs passed **11/11**.

### 2026-07-29 · RE-MEASURE — v0.15.3 release evidence admitted

- owner: Codex
- commit: 907f661
- result: PASS. The authorized candidate is
  `197e93effe9a6abf9c59488a9849c6dcda47646c` on
  `candidate/v0.15.3`; hosted workflow-dispatch run `30414648482` attempt 1
  completed successfully at that exact SHA.
- gate acceptance: PASS. Remote mutation was limited to the candidate branch
  and authenticated dispatch. Admission commit `907f661` contains only seven
  signed receipt/bundle pairs, the release-grade deferred-audit report,
  `config/protected-artifacts.json`, and required status records. No tag,
  `main` advance, publication, product path, public surface, dependency,
  lockfile, schema, or protected database moved.
- workflow acceptance: PASS. The remote candidate workflow was read before
  dispatch and contained every expected core, lint, net, MSRV, two-shell,
  golden, signing, and upload invocation. Its blob
  `96e85af978981b7af9bdd8e9e11069f158f35e57` equals the local workflow blob.
- same-commit count acceptance: PASS. Local `./run ci-local` passed **20/20**
  with **133** workspace tests, **55** net tests (**29 + 26**), shell
  **248/248** on Python 3.11.4, Rust 1.78, invariant **11/11 rules / 23
  controls**, R10's **45** exemptions, and golden **11/11**; constrained
  Python 3.12.13 independently passed **248/248**. Hosted logs report the same
  **133**, **55**, **11/11 / 23**, **45**, and **11/11** counts. Each hosted
  shell collected **248** as **247 passed + 1 declared on-site-only
  protected-corpus skip**, exactly equal to local collection.
- authentication/re-derivation acceptance: PASS. All **7/7** derived
  identities across **6** blocking jobs have successful Linux receipts and
  verified Sigstore bundles; zero receipts were rejected. The clean detached
  report records **5 deferred / 2 promoted / 0** deferred subsystems
  implemented. Post-commit authenticated re-derivation passes **7** rows,
  **5** source dispositions, and **7** triggers with release grade and
  attestations required.
- artifact acceptance: PASS. Report
  `evidence/v0.15.3/deferred-audit/report.json` is **34,530** bytes at
  SHA-256
  `3006f9ed8641cbc6483a2a1608c65da52ff008e59837218997f207a7cf588b2e`.
  Post-commit `verify-artifacts` and `evidence-report` pass all **176/176**
  pins — **174/174** evidence plus **2/2** authorization surfaces — and both
  protected databases exact. Exact cosine at the largest **2,600-document**
  archive measured p95 **6.786459 ms**, below the **16.264 ms** A3 anchor.
- remote acceptance: PASS. Final read-only inspection found `origin/main`
  unchanged at `344124819cb3c554f851d0cac3f0f1ed08d1aa10`, candidate branch
  exact at the evidence SHA, and no `v0.15.3` tag.
- golden-E2E delta: **0**. The first post-admission sandboxed invocation was a
  loopback-bind permission non-result; the identical permitted invocation
  passed **11/11**.

### 2026-07-29 · R-CLOSE — v0.15.3 release measured and locally tagged

- owner: Codex
- commit: dbff27d
- result: PASS. Release disposition is **release (as of 2026-07-29)**. The
  operator authorized publication because Step 4 changes production behavior
  received by an artifact consumer: `cached()` selects TTL by exhaustive
  policy variant and `cored` wires a **300-second** negative TTL. The patch
  default classifies the compatible identity; it is not the trigger.
- gate acceptance: PASS. Steps 1–6 were complete and boxed, the worktree was
  clean, and the publication decision was explicit before release mutation.
  R-CLOSE changed only its declared release reconciliation surfaces; it did
  not alter `repomix.config.json` or repair the v0.20 export findings.
- severity/retry acceptance: PASS. The pre-fix result was fail-closed
  availability loss: it denied access and never allowed a publisher-refused
  request. The correction deliberately permits another `/robots.txt` attempt
  at most once per **300 seconds** instead of once per **24 hours**, bounded by
  ingest frequency and the shared limiter acquired by `policy_for`.
  `Unreachable` still denies while cached and overwrites expired good policy;
  Decision B remains deferred under its live-outage and authorization trigger.
- identity/removal acceptance: PASS. v0.15.3 is patch-compatible because no
  `/v1/*` name, response body, or schema changed. The unsupported
  `diagnostics` and `robots-preview` features and preview binary that shipped
  in v0.15.2 are explicitly recorded as removed. Evidence candidate
  `197e93effe9a6abf9c59488a9849c6dcda47646c` and exact release commit
  `dbff27d559193847dd2028c435c686ba656dac85` are separate subjects. Local
  annotated tag object `2039e01475b43285ecbbf2739f788b7f855a5603`
  peels exactly to the release commit.
- exact-release acceptance: PASS. Clean-tree `./run ci-local` passed
  **20/20** with **133** workspace tests, **55** net tests (**29 + 26**),
  locked Rust 1.78, zero rustc/clippy/fmt/ShellCheck failures, Python 3.11.4
  **248/248**, `invariant-scan` **11/11 rules / 23 controls**, **176/176**
  pins, protected databases **2/2**, and golden **11/11**. The first sandboxed
  invocation was a loopback-bind non-result; the identical permitted
  invocation passed. A clean constrained Python 3.12.13 rebuild resolved
  **21/21** packages and passed **248/248**.
- supplemental/evidence acceptance: PASS. All-features suites passed
  `intel-compliance` **40/40** and `intel-ingest` **29/29**; both retired
  feature commands exited **101** with Cargo's `does not contain this
  feature`. The documented release-posture re-derivation authenticated **7**
  rows, **5** source dispositions, and **7** triggers. One over-specified
  rederive invocation exited **2** because production-only flags are forbidden
  in rederive mode; it changed no file and the documented invocation passed.
- export acceptance: PASS with three named v0.20 omissions. Root-run Repomix
  1.17.0 reports **2,669,764 characters / 145 files** at the release commit;
  its serialized XML is **2,674,706 bytes**. All **88/88** paths derived from
  `git ls-files crates apps tools shell`, all four fixtures named by
  `config/core.json`, and every named release-critical file are present. The
  comparable E0 summary was **4,887,220 characters / 339 files**. The missed
  v0.6/v0.7 tasks, missing derived `export-check`, and missing AGENTS rules are
  carried to v0.20 without a config change here.
- epistemic/diff/architecture acceptance: PASS. The close records that a false
  publication status previously passed every project check. All **39** diff
  paths are classified once in `STATE.md`; `CHANGELOG.md` includes the retry
  trade and `Removed` heading. `ARCHITECTURE.md` keeps A4, editable L1,
  R3/R4, the measured-value heuristic, T7, Decision B, the export omissions,
  and scheduled L2 open.
- product/publication acceptance: PASS locally. `arxiv-cs` remains the sole
  real publisher and three sources remain fixture placeholders. Before local
  tagging, remote inspection found `origin/main`
  `344124819cb3c554f851d0cac3f0f1ed08d1aa10`, the candidate exact, and no
  remote `v0.15.3` tag. The closing audit commit and tag are authorized for one
  atomic push.
- golden-E2E delta: **0**. The mandatory standalone release invocation passed
  **11/11**.

### 2026-07-29 · POST-PUBLICATION — status self-reference gate tripped

- owner: Codex
- commit: 692069e
- result: BLOCKED for a green publication run; publication itself succeeded.
  The authorized atomic push advanced remote main exactly to closing audit
  `692069ead0b8823d6874d8f2fc0a593d9f26704f` and created annotated tag object
  `2039e01475b43285ecbbf2739f788b7f855a5603`, peeled to release commit
  `dbff27d559193847dd2028c435c686ba656dac85`.
- hosted acceptance: FAIL. Push run `30417274925` attempt **1**, exact head
  `692069e…`, completed with conclusion **failure**. Golden, clippy/fmt, core,
  Rust 1.78 MSRV, net, and Python 3.12 job instances succeeded. Python 3.11
  passed version consistency and then `cycle-check` exited **1** because
  `STATE.md` asserted pre-publication main `3441248…` while the hosted checkout
  correctly measured newly published main `692069e…`; every later Python 3.11
  step was skipped.
- gate disposition: STOP and record. The immutable closing commit can contain
  only the ref measured before its own atomic publication. Re-running it
  cannot change that value, while pushing a forward correction moves main
  again. The checker is not weakened and the failed run is not called a pass.
  v0.20 must add a failure-capable design that makes publication freshness
  satisfiable across both pre- and post-publication states.
- scope acceptance: PASS for evidence preservation. The release tag, release
  commit, protected artifacts, admitted evidence, and closing record remain
  unchanged. `STATE.md` receives a forward publication audit; no historical
  append is rewritten. The three export-control omissions remain open and the
  newly exposed status self-reference is a fourth v0.20 finding.
- golden-E2E delta: **0**. The publication run's golden job succeeded, and the
  exact release commit's mandatory standalone golden was already **11/11**.
