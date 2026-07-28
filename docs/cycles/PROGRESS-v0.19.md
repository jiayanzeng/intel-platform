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
