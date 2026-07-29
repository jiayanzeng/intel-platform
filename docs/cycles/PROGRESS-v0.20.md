# PROGRESS-v0.20.md — append-only execution record

This file records v0.20 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-29 · ACTIVATE — v0.20 admitted

- owner: Codex
- commit: 2a9e1c8
- result: PASS for cycle activation only; E0 remains unchecked. Before
  activation, local `main` was the intentionally unpushed forward publication
  audit `72b6f425114e06b1e148e0aa360e280a690e4f0c`, one commit ahead of
  measured `origin/main`
  `692069ead0b8823d6874d8f2fc0a593d9f26704f`.
- worktree acceptance: PASS. The only pre-activation worktree item was the
  operator-supplied untracked `TASKS-v0.20-EXECUTION.md`; implementation commit
  `2a9e1c8` contains only that runbook, the `AGENTS.md` v0.20 declaration, and
  this new append-only progress-log skeleton.
- lifecycle acceptance: PASS. After the implementation commit,
  `./run cycle-check` reports active v0.20 open with seventeen closed execution
  runbooks. `./run checklist-audit` resolves the entering **158/158** checked
  tasks, reports the same three retractions, and finds zero exemptions.
  `git diff --check` passed.
- G1 activation observation: `cycle-check` passes locally only because the
  measured `origin/main` has not moved from the literal value asserted in the
  current `STATE.md` header. This is evidence for E0's fixed-point gate, not
  evidence that the publication-freshness rule is satisfiable.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and G1–G5 measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-29 · E0 — entering state and drafted gates measured

- owner: Codex
- commit: 3794100
- result: PASS. The read-only Gate contains every acceptance surface; only the
  runbook status/checklist and this append-only record moved. `STATE.md`
  remained blob `fb996dc34c41b81da8418946896898c3125a3ad7`,
  byte-identical to the entering tree.
- entering-matrix acceptance: PASS. The first sandboxed `./run ci-local` was a
  loopback-bind permission non-result; the identical permitted invocation
  passed **20/20** with **133** workspace tests, **55** net tests (**29 + 26**),
  shell **248/248** on Python 3.11.4, locked Rust 1.78, zero
  rustc/clippy/fmt/ShellCheck failures, `invariant-scan` **11/11 rules / 23
  controls**, all **176/176** pins, protected databases **2/2**, and golden
  **11/11**. A clean constrained Python 3.12.13 rebuild resolved **21/21**
  packages and passed shell **248/248**. Standalone golden passed **11/11**.
- hosted-state acceptance: PASS as a recorded red result, not a green matrix.
  GitHub run `30417274925` remains failed at exact remote head `692069e…`.
  E0 found a later attempt **2** than the draft's attempt 1. Six blocking job
  instances succeeded; only `shell (Python 3.11)` failed, at
  `active cycle and amendment consistency`, because `cycle-check` reported
  asserted `origin/main` `344124819c…` versus measured `692069ead0…`, then
  exited 1.
- G1 acceptance: PASS and CONFIRMED. Exact commit `72b6f42…` passed while the
  simulated tracking ref equaled its header's `692069e…`, then the same
  immutable content failed after that ref moved to `72b6f42…`. A truth-table
  construction showed the pre-push literal passes only before, the post-push
  literal only after, and no third literal passes either; satisfiable was
  **false** because the two required values differ.
- G2 acceptance: PASS and CONFIRMED. A stale header produced one error with
  complete history. Removing its tag made `check_publication_status` return
  exit **0** with `errors=[]`. A depth-1 clone with the tag object/target but no
  connecting ancestry made `merge-base --is-ancestor` exit **1**, while the
  same check again returned zero errors over a stale header.
- G3 acceptance: PASS with corrected measurements. Root-run Repomix 1.17.0
  produced **2,713,184 characters / 147 files** and **2,718,308** serialized
  bytes. The pattern excludes **17 / 657,725 bytes** and retains **20 /
  633,876 bytes** under `docs/cycles/`; missed `TASKS-v0.6.md` and
  `TASKS-v0.7.md` total **31,147 bytes**, not the draft's 30,842.
- G4/source-drift acceptance: PASS. `run` has no export command and `AGENTS.md`
  has no Repomix/export-check rule. The current source set derived from
  `git ls-files` is **88**, all **88/88** present in the export. The recorded
  **89** at EXPORT-BUDGET differs by exactly the later-deleted
  `crates/ingest/src/bin/robots_preview.rs`; no discrepancy remains open.
- G5 acceptance: PASS and CONFIRMED. An unrelated nearby `outstanding` matched
  after `publication`. The bounded header-only false refusal is accepted for
  this four-change cycle; it cannot produce a false pass.
- object/pin acceptance: PASS. Remote main is `692069e…`; annotated
  `v0.15.3` is object `2039e014…`, peeled to `dbff27d559…`. Standalone
  `verify-artifacts` passed all **176/176** pins and protected databases
  **2/2**.
- status acceptance: PASS after the implementation commit exists.
  `cycle-check`, `progress-check`, `version-check`, and `invariant-scan` are
  green; the expected pre-audit `checklist-audit` refusal named only E0's
  missing progress entry and is rerun after this append.
- golden-E2E delta: **0**; mandatory standalone execution passed **11/11**.
