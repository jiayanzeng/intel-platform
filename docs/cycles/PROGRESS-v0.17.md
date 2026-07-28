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
