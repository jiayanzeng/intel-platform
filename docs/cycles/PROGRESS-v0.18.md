# PROGRESS-v0.18.md — append-only execution record

This file records v0.18 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-28 · ACTIVATE — v0.18 admitted

- owner: Codex
- commit: 50ac8d0
- result: PASS for cycle activation only; E0 remains unchecked. Before
  activation, local `main` and the measured `origin/main` tracking ref were
  aligned at `f13c6129d608ab9259f421dce6ed419ce469c225`.
- worktree acceptance: PASS. The only pre-activation worktree item was the
  operator-supplied untracked `TASKS-v0.18-EXECUTION.md`; implementation commit
  `50ac8d0` contains only that runbook, the `AGENTS.md` v0.18 declaration, and
  this new append-only progress log.
- published-tag acceptance: PASS. Annotated `v0.15.1` remains tag object
  `d6a71c1a2afabd7ce7b335756b7ae66ff36cf1ba`, dereferencing exactly to release
  commit `a0ba69e0a3e8385287274bb404d5123f9a2b8ac7`.
- lifecycle acceptance: PASS. `./run cycle-check` reports active v0.18 open
  with fifteen closed execution runbooks. `./run checklist-audit` resolves the
  entering 144 checked tasks, reports the same three retractions, and finds zero
  exemptions. `git diff --check` passed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and G1–G6 measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-28 · E0 — entering state and incident boundary measured

- owner: Codex
- commit: 9222e18
- result: PASS. The read-only Gate was defined before the first E0 commit and
  contains the status/runbook acceptance surfaces; no product path, dependency,
  lockfile, protected artifact, or public surface changed.
- entering-matrix acceptance: PASS at activation-audit commit `af961f9` with
  `CARGO_TARGET_DIR=/private/tmp/intel-v018-e0-ci-target`. The first sandboxed
  attempt was a non-result because the net fixture could not bind loopback; the
  identical permitted invocation passed **20/20** jobs with **131** workspace
  tests, **55** net tests (**29** ingest plus **26** cored), Python 3.11.4 shell
  **244/244**, warning-denied offline/net builds, clippy, fmt, ShellCheck,
  locked Rust 1.78 check/test, `invariant-scan` **11/11 rules / 23 controls**,
  all **146/146** pins, both protected databases exact, and golden **11/11**.
- interpreter acceptance: PASS. Clean rebuilds resolved all **21/21** pinned
  packages and passed shell **244/244** under Python 3.11.4 and Python 3.12.13,
  with the same single third-party deprecation warning.
- G2 configured-URL acceptance: PASS. The live harness strips the fixture only
  from `arxiv-cs`; its configured `/oai?...` target is identical under old and
  corrected derivations. The three multi-segment `example.org` URLs differ but
  remain fixture-only and issue no publisher request.
- G2 redirect acceptance: PASS. The historically observed `/oai2?...` to
  `/oai?...` redirect is single-segment and identical under both derivations.
  The constructed multi-segment control `/oai/archive/page?cursor=abc`
  distinguishes old `/oai` from the corrected full target. No configured live
  URL or historically observed redirect was affected.
- G1 acceptance: PASS and closed clean. Direct helpers preserve scheme/host
  case, but production `get_text_with` parses the initial URL and joins every
  redirect through `reqwest::Url` before the sole production network call to
  `gate()`. A temporary executing mixed-case initial/redirect control passed
  **1/1** and observed only lowercase robots URLs, page URLs, and limiter keys;
  it was removed after measurement. ORIGIN-CASE must therefore skip.
- source-inventory acceptance: PASS. Configuration contains **4** sources:
  `arxiv-cs` is the sole real publisher; the other **3** are `example.org`
  placeholders.
- published-object/pin acceptance: PASS by live remote inspection. `main`
  remains `f13c6129…`; annotated `v0.15.1` remains tag object `d6a71c1…`
  peeled to release commit `a0ba69e0…`; manifest validation passes with
  **146/146** pins and both protected databases exact.
- golden-E2E delta: **0**; both the entering matrix and mandatory post-status
  standalone invocation passed **11/11**.
