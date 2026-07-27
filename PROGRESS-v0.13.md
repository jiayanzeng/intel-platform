# PROGRESS-v0.13.md — append-only execution record

This file records v0.13 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-27 · E0-GATE — clean worktree confirmed and v0.13 admitted

- owner: Codex
- commit: 5223d783b43c250102418163ef124f4e662b727b
- result: PASS for cycle activation only; E0 remains unchecked. The mandated
  opener found entering HEAD
  `466ebb3fc9736923110803e087acc798e417d084`, described as
  `v0.12.0-1-g466ebb3`, with local `main` and `origin/main` aligned (zero ahead
  / zero behind). The only worktree entry was the operator-supplied untracked
  `TASKS-v0.13-EXECUTION.md`. Annotated `v0.12.0` remained tag object
  `94d8215bc2151fecba1280dc793d3f5953cd8055`, peeled to
  `e5faf0c161a4256f33976664685653d8bd805d5d`.
- correction: implementation commit
  `5223d783b43c250102418163ef124f4e662b727b` committed only the supplied
  runbook, the `AGENTS.md` active-cycle header, and the empty append-only
  progress log.
- lifecycle acceptance: PASS. `./run cycle-check` reports active v0.13 open
  with ten closed execution runbooks. `./run checklist-audit` resolves the
  entering **99/99** checked tasks, reports the one existing v0.11 retraction
  separately, and finds zero exemptions. `git diff --check` passed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the
  entering matrix and C1–C5 reproduction.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file was
  touched.

### 2026-07-27 · E0 — entering state rebuilt and five findings confirmed

- runbook: `TASKS-v0.13-EXECUTION.md`
- owner: Codex
- commit: ed7249c1cf6429c6482592551a2a6e7dc996d9d3
- result: PASS. The permitted entering matrix passed **20/20** with **121**
  workspace Rust tests, **21** net tests, **205/205** Python 3.11 shell tests,
  zero rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green,
  protected databases **2/2**, all **71/71** pins, and golden **11/11**. The
  initial sandboxed matrix is an environment non-result because eight shell
  controls were denied loopback/process access after 197 tests passed.
  Python 3.12 passed **205/205**, with both interpreters verifying **21/21**
  exact packages. Standalone golden repeated **11/11**.
- C1 acceptance: PASS as a confirmed release-blocking finding. A real `cored`
  over exactly two scratch documents returned an empty `/retrieve` context for
  a finance scope querying science-only text; direct
  `documents_by_ids(["science-b"])` nevertheless returned the science body,
  proving upstream ranking rather than final hydration supplied containment.
  `/attest` has no sector field and returned HTTP 200 with a violation naming
  the out-of-sector `IndexOnly` document; a nonexistent id returned HTTP 400.
  The cross-sector existence/match oracle is live. No `/retrieve` body leak
  reproduced.
- C2 acceptance: PASS as a confirmed coverage defect. The renamed
  `INGEST_FUZZ_LIMIT=17` production mutation exited 0 with the exact line
  `invariant-scan: R5 PASS: Production Rust has one private
  canonical-distance constant and no numeric canonical-distance call
  argument.` The original named-constant and numeric-call controls separately
  exited 1 with `R5 FAIL` at `sqlite.rs:33` and `sqlite.rs:207`.
- C3 acceptance: PASS as a confirmed harness defect. Sixteen enumerated shell
  test files contain no invariant-scan test. Replacing R4's provider-key regex
  with the never-matching `(?!)` pattern still exited 0 and reported **6/6**
  rules passing, proving `fail_before` is not executed.
- C4/C5 acceptance: PASS as confirmed findings. The architecture's endpoint
  table and HC2 prose contradict the unscoped `/retrieve` and `/attest`
  hydration paths. The crawler already shares one UA constant across both
  clients and `RobotsCache`, but that constant has the stale `0.1` version and
  `you@example.com`; there is no contact override or startup refusal.
- published-baseline acceptance: PASS. Annotated `v0.12.0` remains object
  `94d8215bc2151fecba1280dc793d3f5953cd8055`, peeled to
  `e5faf0c161a4256f33976664685653d8bd805d5d`; all 71 pins and both protected
  databases re-verified byte-exact. No C1–C5 row refuted.
- golden-E2E delta: **0**; the mandatory post-task run remained **11/11**
  byte-identical.
- cleanup: both disposable worktrees, their temporary database/log, and the
  spawned core process were removed; the live tree returned clean before the
  task record.
