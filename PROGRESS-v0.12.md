# PROGRESS-v0.12.md — append-only execution record

This file records v0.12 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-27 · E0-GATE — dirty worktree preserved and v0.12 admitted

- owner: Codex
- commit: a81430ab8a50961d03eff019d3449405312d8280
- result: PASS for cycle activation only; E0 remains unchecked. The mandated
  opener found entering HEAD
  `916b20f8c3dabd743a0568cb14353a0c889e2ab1`, described as
  `v0.11.0-1-g916b20f-dirty`, with local `main` and `origin/main` aligned
  (zero ahead / zero behind). Annotated `v0.11.0` remained tag object
  `fcfa4825e6ffbc06c0ad73e18044965c10786aa8`, peeled to
  `6daeb7e9f2cc0022b5e1a1dcf2ce8702b5be0321`.
- dirty-state inventory: preserved without stashing, reverting, cleaning, or
  staging the operations work. Modified tracked files were `AGENTS.md`,
  `README.md`, `STATE.md`, and `run`; untracked files were this supplied
  runbook, `intel-platform-OPERATIONS.md`,
  `shell/tests/test_model_profiles.py`, and `tools/model_profiles.py`.
  The draft omitted `README.md` from its entering-state list; its diff is
  explained by the same model-profile work (command documentation,
  operations-manual link, and the nine-test count). The other tracked diffs
  contain the standing-authorization block, prior live-evidence record, and
  `./run models` dispatch; the three untracked operations files are their
  implementation, manual, and tests.
- correction: implementation commit
  `a81430ab8a50961d03eff019d3449405312d8280` committed only the supplied
  runbook, the `AGENTS.md` active-cycle header, and the empty append-only
  progress log. The pre-existing `AGENTS.md` operations hunk remained
  unstaged.
- lifecycle acceptance: PASS. `./run cycle-check` reports active v0.12 open
  with nine closed execution runbooks. `./run checklist-audit` resolves the
  entering **88/88** checked tasks with zero exemptions. `git diff --check`
  passed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the
  entering matrix and shell-count disambiguation.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file was
  touched.

### 2026-07-27 · E0 — entering state rebuilt and seven findings confirmed

- runbook: `TASKS-v0.12-EXECUTION.md`
- owner: Codex
- commit: 83e7bfab5388d851f05dc9e804ec91a3aebecf70
- result: PASS. The deliberately dirty operations worktree remained intact.
  The permitted entering matrix passed **19/19** with **119** workspace Rust
  tests, **21** net tests, **200/200** Python 3.11 shell tests, zero denied
  rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78 green, **2/2**
  protected databases, **54/54** pins, and **11/11** golden. The initial
  sandboxed matrix is recorded as an environment non-result because eight
  shell controls were denied loopback/process access.
- shell-count acceptance: PASS. Python 3.12 passed **200/200** and both
  interpreters verified **21/21** constrained packages. Moving only
  `shell/tests/test_model_profiles.py` out of collection, then restoring it
  immediately, passed **191/191** under Python 3.11; the exact delta is nine.
  Thus 191 is the released v0.11.0 suite and 200 is the dirty-worktree suite.
- C1 acceptance: PASS fail-before. A disposable real `cored` and scratch DB
  began with one finance document and generation 1. After a NULL persisted
  fingerprint forced rematerialization failure, non-paged `techwire` returned
  HTTP **500** but left **5** total documents / **4** `techwire` rows durable;
  generation remained 1.
- C2 acceptance: PASS. Recursive Rust grep found exactly one production call
  outside the store: `apps/cored/src/main.rs` passes literal `16`. The public
  store method accepts a caller-supplied threshold; all other nine calls are
  in its `#[cfg(test)]` module.
- C3/C6/C7 acceptance: PASS as confirmed findings. Checklist audit proves
  box/progress/commit provenance but does not evaluate criteria. The mutable
  model controller carries free-form remote transition strings without a
  structural allowlist. Its nine tests cover only `classify_profile` and
  `transition_script`; four named failure gates and all three augment
  dispositions remain for the operations tasks.
- C4 acceptance: PASS through the 200/191 control. C5 acceptance: PASS with a
  correction to the draft's example set—the tracked scan excluding
  `evidence/` found **11** paths. Ten predate the current correction runbook;
  historical committed occurrences already falsified v0.11's absence claim
  before the supplied operations body.
- finding disposition: C1-C7 all confirmed; none refuted.
- lifecycle acceptance: PASS. Standalone `golden`, `verify-artifacts`,
  `cycle-check`, `checklist-audit` (**88/88**, zero exemptions),
  `progress-check`, `version-check`, and manifest validation passed.
- golden-E2E delta: **0**; all **11/11** anchors remained byte-identical.
- protected artifact delta: **0**. Independent SHA-256 and byte-count witnesses
  matched `data/core.db` and `data/live-smoke.db`; annotated `v0.11.0` remained
  object `fcfa4825e6ffbc06c0ad73e18044965c10786aa8` peeled to unchanged release
  commit `6daeb7e9f2cc0022b5e1a1dcf2ce8702b5be0321`.

### 2026-07-27 · INGEST-ATOMIC — corpus append and identity share one commit

- runbook: `TASKS-v0.12-EXECUTION.md`
- owner: Codex
- commit: 904866e41a6848de9bde021e12e5c4d7b4fff774
- result: PASS. `append_new` now appends and globally rematerializes
  `canonical_id` inside one SQLite transaction. The non-paged handler only
  bumps view generation after that successful durability point; no fallible
  operation remains between them.
- non-paged failure acceptance: PASS fail-before/pass-after. Before the fix,
  the new regression returned HTTP 500 and preserved generation but found
  **5** committed rows instead of the required **1**. After the fix, the same
  injected missing-fingerprint failure returns HTTP 500, leaves count at 1,
  and leaves generation unmoved.
- paged boundary acceptance: PASS before and after. A successful first page
  leaves two documents durable with canonical ids, cursor token, and generation
  1; a later injected page failure adds zero rows, preserves that cursor and
  identity, and does not bump generation again.
- architecture/API acceptance: PASS. `ARCHITECTURE.md` §3 item 8 now names the
  same-transaction rule for every store write path that adds, changes, or
  removes rows. No schema or `/ingest` success-body change occurred. Source
  search finds `append_new` in the handler and no handler-level
  `assign_canonical_ids` call.
- executable-evidence correction: the first `ci-local` correctly refused a
  stale `audit_deferred.py` locator for the removed handler assignment. Its
  writer inventory now locates the actual atomic `append_new` path; no deferred
  trigger or disposition changed. The identical rerun passed **19/19**.
- matrix acceptance: PASS with **121** workspace Rust tests, **21** net tests,
  warning-denied offline/net builds, clippy, fmt, locked Rust 1.78 check/tests,
  **200/200** Python 3.11 shell tests, and protected evidence **2/2** with all
  **54/54** pins. Standalone relevant Rust/MSRV lanes also passed.
- golden-E2E delta: **0**; standalone and matrix golden runs both passed all
  **11/11** byte-identical anchors.
- protected artifact delta: **0**; no protected database or pinned evidence
  file changed.

### 2026-07-27 · THRESHOLD-ONE — production threshold seam closed

- runbook: `TASKS-v0.12-EXECUTION.md`
- owner: Codex
- commit: 086166a0618426e6ecde9da34aecca8d2cd8541a
- result: PASS with preferred disposition (b). No real out-of-crate caller
  existed, so production exposes no-argument
  `rematerialize_canonical_ids()` for maintenance/backfill while the
  caller-supplied threshold method is store-test-only.
- threshold acceptance: PASS. Recursive Rust grep finds the definition and
  nine calls only inside `crates/store/src/sqlite.rs` and its `#[cfg(test)]`
  module. `DEDUP_MAX_DISTANCE` remains private and every production path
  selects it inside the store.
- R1 failure control: PASS. A disposable detached worktree with an injected
  `store.assign_canonical_ids(16)` exited 1 with
  `invariant-scan: R1 FAIL: apps/cored/src/main.rs:1267: production
  assign_canonical_ids call outside the store`; the exact scratch worktree was
  removed afterward. The clean tree exits 0 with `R1 PASS`.
- R1 scope acceptance: PASS. Its module docstring explicitly excludes
  store-internal and test numeric thresholds while refusing all production
  calls outside the store.
- executable-evidence acceptance: PASS. The deferred writer inventory names
  the no-argument maintenance seam. A raw release-report re-derivation without
  its runner directory was an invocation non-result; the authoritative
  wrapper resolved the proper historical baseline and passed.
- matrix acceptance: PASS. `./run ci-local` passed **19/19** with **121**
  workspace Rust tests, **21** net tests, **200/200** shell tests,
  warning-denied builds, lint/format, and locked Rust 1.78 lanes.
- golden-E2E delta: **0**; standalone and matrix golden passed **11/11**.
- protected artifact delta: **0**; protected databases remained exact **2/2**
  and all **54/54** evidence pins matched.
