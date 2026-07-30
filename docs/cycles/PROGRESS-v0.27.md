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
