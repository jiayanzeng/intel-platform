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

### 2026-07-27 · INVARIANT-SCAN — absence claims become executable

- runbook: `TASKS-v0.12-EXECUTION.md`
- owner: Codex
- commit: 2a613edc977cd70c14f64dfc83229591500b32f7
- result: PASS. `./run invariant-scan` now loads the exact-schema registry in
  `config/invariant-rules.json`; every rule carries `id`, `claim`, `source`,
  `scope`, and a nonempty `fail_before`. It is local CI job 20 and runs in the
  existing Python 3.11 hosted shell identity, so the local count increased from
  19 to 20 without adding a hosted job identity.
- seeded-rule acceptance: PASS at **4/4**. R1 protects the Step 3 production
  call-site boundary; R2 enforces one production `TcpListener::bind` consuming
  the loopback-validated address list; R3 scans production Rust under
  `crates/` for recognized LLM imports, provider/base-URL constants, and
  provider calls; R5 permits exactly one private canonical-distance constant
  and no numeric production call argument. Each registry entry cites the prose
  sentence it executes. R4 remains intentionally deferred until Step 6 records
  the operator-selected credential policy text, as the runbook requires.
- failure-control acceptance: PASS. In a disposable worktree, an extra bind,
  an `async_openai::Client` import, and a second canonical-distance constant
  made R2, R3, and R5 each fail with path and line evidence; the worktree was
  removed. R1 retains Step 3's separate captured failure. A temporary registry
  whose first rule had an empty `fail_before` exited **2** with
  `rules[0].fail_before: must be a non-empty string`; the temporary file was
  removed.
- checklist acceptance: PASS. `checklist_audit.py` now loads the exact-schema
  retraction registry, rejects retraction/exemption overlap and retractions
  naming no resolved checked box, and reports checked and retracted counts
  separately. Before this task's implementation/progress pair it resolved
  **91 checked, 0 retracted**, all 91 entries and commits, and zero exemptions.
- operating-contract acceptance: PASS. `AGENTS.md` now requires every
  repo-wide absence criterion to have a registered scan and requires each
  task Gate to contain the scope of all its acceptance criteria.
- matrix acceptance: PASS. Final `./run ci-local` passed **20/20** with
  **121** workspace Rust tests, **21** net tests, **200/200** dirty-worktree
  shell tests, warning-denied offline/net builds, clippy, fmt, locked Rust
  1.78 lanes, protected artifacts **2/2**, and **54/54** evidence pins.
- golden-E2E delta: **0**; the matrix and final standalone golden runs passed
  every one of the **11/11** anchors.
- protected artifact delta: **0**; no protected database, pinned evidence,
  release tag, or remote ref changed.

### 2026-07-27 · RETRACT-0110 — v0.11 threshold claim corrected forward

- runbook: `TASKS-v0.12-EXECUTION.md`
- owner: Codex
- commit: a954e2ae4e107ce59a8dabd18bdff9d695ddbb7b
- result: PASS. The retraction registry now names v0.11 STORE-IDENTITY,
  quotes its false “one shared `max_distance` constant” criterion, states the
  released handler/store split, and names v0.12 INGEST-ATOMIC plus
  THRESHOLD-ONE as the correcting tasks.
- permanent-record acceptance: PASS. `PROGRESS-v0.11.md` gained one 21-line
  erratum after its closing record. `git diff --unified=0` showed only an
  addition beginning after original line 396; the original STORE-IDENTITY
  entry at lines 257–285 and every closed-runbook checkbox were not edited.
- checklist acceptance: PASS. Before this task's implementation/progress pair,
  `checklist-audit` reported **92 checked, 1 retracted**, all 92 entries and
  commits resolved, and zero exemptions. The retraction is distinct from an
  exemption and names a resolved checked box.
- state/release acceptance: PASS. The `STATE.md` header reports the released
  suite at **191/191** and separately records that the preserved untracked
  operations test file adds nine cases for **200/200** in the dirty worktree.
  It states explicitly that v0.11.0 remains published with the known,
  now-corrected threshold-source defect.
- immutable-release acceptance: PASS before and after. Annotated `v0.11.0`
  remained object `fcfa4825e6ffbc06c0ad73e18044965c10786aa8`, peeling exactly
  to release commit `6daeb7e9f2cc0022b5e1a1dcf2ce8702b5be0321`.
  Manifest validation matched **54/54** pins; `./run verify-artifacts` matched
  both protected databases **2/2**; `git diff --name-only` found no change
  under `config/protected-artifacts.json` or `evidence/`.
- matrix acceptance: PASS. `./run ci-local` passed **20/20** with **121**
  workspace Rust tests, **21** net tests, **200/200** current-worktree shell
  tests, warning-denied builds, clippy/fmt, locked Rust 1.78 lanes, the
  retraction-aware checklist, and all artifact checks.
- golden-E2E delta: **0**; the matrix and standalone runs each passed
  **11/11** exact anchors.
- protected artifact delta: **0**; the tag, release commit, 14 v0.11
  receipt/bundle files, all 54 manifest pins, and both protected databases are
  unchanged.

### 2026-07-27 · INFRA-POLICY — credential boundary replaces false host ban

- runbook: `TASKS-v0.12-EXECUTION.md`
- owner: Codex
- commit: 03abc066458c06249ef28fb0d3d02dacce89895c
- result: PASS with operator-selected **Option A**. RFC 1918 addresses and
  loopback-forward ports remain documentable because they grant no access
  without the operator's LAN or local route; no specific threat model was
  identified that makes them secret. The enforceable boundary is credential
  material.
- three-location acceptance: PASS. The active runbook's standing prohibition,
  `AGENTS.md`, and `STATE.md` decision-log §6g record the choice and reasoning.
  All three name the v0.11 host/port clause as false when written and lacking
  an executable guard for its entire lifetime.
- historical finding acceptance: PASS. The decision record cites E0's 11-path
  tracked scan, including `.env.example`, `README.md`, shell tests, and
  append-only history; ten paths predated the v0.12 runbook. Option B was
  rejected because no threat model justified it and historical records could
  never be cleaned completely.
- R4 acceptance: PASS. The registered rule scans every Git-tracked text file
  for tracked `.env` files, provider-key shapes, private-key headers, concrete
  long bearer values, non-placeholder secret assignments, and raw
  secret-bearing fields. Empty values, explicit placeholders, short demo
  fixtures, binary files, and non-secret network coordinates are scoped out in
  writing. The clean registry reports **5/5** passing rules.
- failure-control acceptance: PASS. A detached scratch worktree with a planted
  fake `sk-proj-…` key at `README.md:1` exited **1** with
  `invariant-scan: R4 FAIL: README.md:1: provider-key-shaped value`. The
  scratch worktree was removed and the clean pass repeated.
- matrix acceptance: PASS. `./run ci-local` passed **20/20** with **121**
  workspace Rust tests, **21** net tests, **200/200** dirty-worktree shell
  tests, warning-denied builds, clippy/fmt, locked Rust 1.78 lanes, protected
  artifacts **2/2**, and all **54/54** pins.
- golden-E2E delta: **0**; matrix and standalone golden each passed
  **11/11** exact anchors.
- protected artifact delta: **0**; no protected database, evidence pin, release
  tag, or remote ref changed.

### 2026-07-27 · OPS-AUTHORITY — remote authorization made executable

- runbook: `TASKS-v0.12-EXECUTION.md`
- owner: Codex
- commit: 0ef43a56aa4a7d813932fbf3607bf3ba68e420fa
- result: PASS with operator-selected **L1 now, L2 scheduled**. Under the
  operator-approved runbook amendment, this task shares one atomic
  implementation commit with OPS-ADMIT so the previously untracked controller
  is never committed without its construction guard and executable pins.
- L1 acceptance: PASS. `TRANSITIONS` is structured tuples, every remote payload
  passes `build_remote_command` before SSH, and the allowlist permits only
  lifecycle operations over the five named containers, bounded Docker
  inventory, loopback `/health` and `/v1/models` probes on 8080–8082, and the
  named exact read-only commands. Existing tests exercise every emitted
  transition and all allowed categories. Planted `docker rm`, `docker run`,
  `rm -rf`, and sixth-container commands each raise `ProfileError`.
- policy-copy acceptance: PASS. `AGENTS.md` and
  `intel-platform-OPERATIONS.md` carry byte-identical marker-delimited policy
  blocks. Registered R6 passes on the real tree. Changing one word in only the
  operations copy of a disposable Git-backed tree exited 1 with
  `model-profile authorization block differs from AGENTS.md`; the scratch tree
  was removed and the clean **6/6** registry pass repeated.
- pin acceptance: PASS. Manifest schema 2 retains all **54/54** evidence pins
  and adds two exact `authorization` pins. `run` is 40,980 bytes at
  `7afede56f13b5ee73d3f1dbe92910ce535908623676db21664409855c5ac006d`;
  `tools/model_profiles.py` is 21,394 bytes at
  `b7b84261a6bc45706f93f338682108a31c3b88ad00ad4c91061a90f77ed74292`.
  The validator's existing failure-capable test now proves a one-byte `run`
  mutation is refused.
- residual/schedule acceptance: PASS. Both mirrored copies state plainly that
  L1 cannot survive an agent editing the controller. L2 is scheduled for the
  next operator-authorized server-administration session and must be installed
  and refusal-tested before another model profile is admitted. No live server
  session occurred.
- matrix acceptance: PASS. The shared implementation passed `./run ci-local`
  **20/20**, **121** workspace Rust tests, **21** net tests, and warning-denied
  builds/lints; the operations file retained exactly nine tests.
- golden-E2E delta: **0**; matrix and mandatory standalone golden both passed
  all **11/11** exact anchors.
- protected artifact delta: database bytes remain exact **2/2** and all 54
  evidence pins remain exact; the only pin-set change is the two deliberate
  authorization-surface records.

### 2026-07-27 · OPS-ADMIT — model-profile operations enter HEAD

- runbook: `TASKS-v0.12-EXECUTION.md`
- owner: Codex
- commit: 0ef43a56aa4a7d813932fbf3607bf3ba68e420fa
- result: PASS. The operator-approved atomic implementation admitted
  `tools/model_profiles.py`, `shell/tests/test_model_profiles.py`,
  `intel-platform-OPERATIONS.md`, and the `run`/`AGENTS.md` operations changes
  in one commit, together with the selected L1 guard, pins, documentation,
  runbook amendment, and measured STATE record. OPS-AUTHORITY has its own
  preceding append-only audit commit; this is the separate OPS-ADMIT record.
- shell-count acceptance: PASS. Python 3.11.4 and 3.12.13 each passed exactly
  **200/200**, and both verified **21/21** constrained packages. The initial
  direct sandboxed invocation was an environment non-result with eight denied
  loopback/process-topology controls; identical permitted reruns passed. The
  former nine-test dirty delta is now part of HEAD, while released v0.11.0
  remains correctly recorded at 191/191.
- live-evidence acceptance: PASS as prior measured evidence only. The durable
  record names the operator-authorized 2026-07-27 Terminal.app/localhost:2222
  provenance, the exact two newly created container IDs, explicit 8080/8081
  HTTP health overriding `intel-embed`'s known wrong-port Docker label, the
  `osascript do shell script` route failure, and every measured profile/tunnel
  result. HC13 limits are explicit: one real-hardware run proves only that
  session, not later controller edits, another host, or changed server state.
  No server, Docker, SSH, or network session was run in v0.12.
- C7-augment acceptance: PASS. A malformed tabular inventory row now raises
  `ProfileError` and is tested. Requiring all five containers remains an
  intentional cross-project refusal because the shared controller must know
  every conflicting role exists before selecting either profile. `cmd_models`
  documents its deliberate stdlib-only bare-`python3` path so recovery works
  before a venv exists.
- ownership acceptance: PASS. The operations manual records
  `tools/model_profiles.py` in intel-platform as the single executable source
  of truth for both projects; Athenaeum delegates to it and must not keep a
  duplicate controller.
- gate remeasurement: PASS. Because the operations files changed from E0 for
  L1 and the required augments, the complete offline matrix was rerun before
  admission as required; the runbook independently prohibited a new live
  session.
- matrix acceptance: PASS. `./run ci-local` passed **20/20** with **121**
  workspace Rust tests, **21** net tests, warning-denied offline/net builds,
  clippy, fmt, ShellCheck, locked Rust 1.78 checks/tests, all shell tests, and
  artifact validation.
- golden-E2E delta: **0**; matrix and mandatory standalone golden both passed
  all **11/11** byte-identical anchors.
- protected artifact delta: protected databases remain exact **2/2** and all
  **54/54** evidence pins remain exact; both newly admitted authorization pins
  also match.
