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
