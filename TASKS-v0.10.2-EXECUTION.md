# TASKS-v0.10.2-EXECUTION.md — evidence-integrity and publication runbook for Codex

v0.10.2 is an **evidence-integrity-hardening and publication cycle**. v0.10.1
closed locally (annotated tag object `8ded63f79ed12b4180e8bcd0bcff4ef30a080a79`
dereferencing to release commit `e5af6bc5df8261cc004bd4d3247b70f8cbe930bb`) with
a green 19-job local matrix, a fresh conformant real-model battery, and a clean
re-measured deferred-audit receipt. The v0.10.1 self-audit — independently
re-verified against the shipped tree — is **accurate**: every reported finding
reproduces and every reported pass holds. This cycle acts on the four findings it
raised.

The four findings share **one root cause**, and this cycle is organized around
naming it: *the audit tooling trusts locally-supplied or locally-measured
evidence without binding it to an unforgeable producer or an enforced
precondition.* This is the project's own doctrine (`AGENTS.md §0` — a claimed
property that nothing executes is not a property) raised one level: **evidence
that no unforgeable producer stands behind, and that no gate refused to accept,
is not evidence.** A hand-authored receipt is accepted; a dirty/wrong-subject
production report is written; a contradictory resumed attempt is reused; and the
operating contract still points at a closed cycle's logs. Each is that same
failure.

This cycle does five things and deliberately no more:

1. **binds CI-runner receipts to their producer** — require the exact release
   commit, successful conclusions, the complete expected job matrix under one
   run id, and reject anything a runner did not emit (with an attestation tier
   completed at publication);
2. **enforces the production-audit subject** — no production measurement runs
   against a dirty worktree or an unexpected HEAD;
3. **hardens resume validation** — a reused attempt must be internally
   consistent (HTTP 200, conforming schema) and any resumed `LEAK` halts;
4. **makes the operating contract cycle-neutral** — `AGENTS.md` stops naming a
   specific cycle's runbook and log, and a check enforces that it stays neutral;
5. **publishes v0.10.1** under explicit operator authorization, and re-measures
   the receipt against authenticated hosted evidence.

It ships no new ingestion source, no subscriber-facing surface, no runtime or
public-API change, and no change to the golden regression. **Golden stays 11/11
byte-identical through every task in this file.** The default disposition at
R-CLOSE is a **patch release `v0.10.2`**.

---

## Entering state (asserted, not yet verified)

Taken from `STATE.md` (v0.10.1) and the v0.10.1 self-audit. **Every sentence here
is a hypothesis until Step 1 (E0) measures it.** Prior measurement is not
permission to skip the entering-state run — including when the prior measurement
is your own or your predecessor's.

- Worktree clean; `./run ci-local` **19/19**; `./run version-check` **PASS at
  0.10.1**; golden **11/11**; protected evidence **2/2 exact**; both v0.10.1 JSON
  reports **hash-pinned** and the deferred-evidence re-derivation blocking;
  `cycle-check` reports the v0.10.1 runbook **closed**; `checklist-audit` green.
- Rust **99 workspace / 20 net** tests, 0 rustc warnings. Python **3.11.4 and
  3.12.13: 138 shell tests each**; **21/21** exact packages both interpreters.
- Release commit `e5af6bc5df8261cc004bd4d3247b70f8cbe930bb`; annotated tag object
  `8ded63f79ed12b4180e8bcd0bcff4ef30a080a79` (`v0.10.1`), **local only**.
- `X-REGEN` recorded **45/45** valid real-model cells `NOT EXERCISED`, zero
  `LEAK`, real-path positive control `GUARD FIRED`. `RECEIPT` re-measured clean at
  the released commit: `{promoted:2, deferred:5}`, CI-runner `promote` under the
  restated trigger, seven accepted runner receipts.
- **v0.10.1 is unpublished.** Local `main` is 12 commits ahead of `origin/main`;
  remote `main` is at the approved G-RUN checkpoint `5bcabcb8…`; no remote
  v0.10.1 tag exists; no push is authorized.

### Defects this runbook is drafted against (verify, do not trust)

Each was read out of the shipped tree on 2026-07-26 by path and line and is a
hypothesis until E0 confirms or refutes it. F1–F4 correspond to the four v0.10.1
self-audit findings; the **[augment]** notes are where independent
re-verification adds to the finding and must be honored alongside it.

| # | Location | Claim to verify |
|---|---|---|
| F1 | `tools/audit_deferred.py:656-760` (`runner_receipt_measurement`) | Receipts are accepted after **only** field-format and Git-ancestry checks (`git merge-base --is-ancestor <sha> <audited_head>`). Nothing authenticates the GitHub run/artifact, and nothing requires `sha == the released commit`. A hand-authored JSON with any ancestor SHA and the seven required fields is accepted and counted. |
| F1 **[augment]** | same function, lines 701-706 and 744-749 | The `conclusion` field is required to be present and non-empty but its **value is never checked** — a receipt with `conclusion:"failure"` is still accepted and counted as an observed execution. There is also no requirement that the **complete expected job matrix** (core, golden, lint, msrv, net, shell×2) is present under **one** `run_id`; a single fabricated receipt promotes the row. The seven committed receipts happen to be `sha==release`, `conclusion==success`, one `run_id` — but nothing enforces any of it. |
| F2 | `tools/audit_deferred.py:1216-1262` (`run_production`) | The production path records `git_subject()` (which carries `worktree_dirty`) but **never rejects** a dirty worktree or an unexpected HEAD, and there is no `--expected-head` (grep: zero references). The D2 failure class — a receipt measured on a dirty worktree at the wrong commit — is structurally reproducible. The current committed receipt is clean at the release commit only because the operator followed the procedure this time. |
| F3 | `tools/verify_llm.py:346-387` (`_resume_valid_attempts`) | The resume predicate reuses an attempt when `target_in_context` and `model_completed` are truthy, **without** validating `http_status` or the full attempt schema. |
| F3 **[augment]** (severity) | `tools/verify_llm.py:579-604` | In the real path, `model_completed` is set `True` **only inside** the `http 200` branch, so the contradictory state `model_completed:true` + `http_status:502` is **not naturally producible** — it can exist only in a hand-edited or cross-contaminated resume source. F3 is therefore the same defect class as F1: trusting evidence-file contents no producer had to earn. Correctly **P2**; the fix is to require `http_status==200`, schema conformance, and an immediate halt on any resumed `LEAK`. |
| F4 | `AGENTS.md:13-17` vs `§5:214,226,230` | The header declares **v0.10.1** active and names `TASKS-v0.10.1-EXECUTION.md` / `PROGRESS-v0.10.1.md`, but the per-task workflow still directs agents to the **closed** `TASKS-v0.10-EXECUTION.md` and `PROGRESS-v0.10.md`. Literal execution edits historical records. |
| F4 **[augment]** (breadth) | `AGENTS.md:59` (§1) | The stale reference is broader than §5: `§1` line 59 also names `PROGRESS-v0.10.md`. Four hard-coded stale literals total (`PROGRESS-v0.10.md` ×3 at 59/230, `TASKS-v0.10-EXECUTION.md` ×2 at 214/226). This is a **recurring** defect — v0.10's runbook carried the identical class against v0.9 paths, and v0.10.1 fixed only the header, not the body. The permanent fix is cycle-neutral wording **plus** an executable guard so it cannot recur. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task: check the gate first, implement, run and capture every
acceptance criterion, run `./run golden`, update `STATE.md`, append
`PROGRESS-v0.10.2.md`, check the box here, and commit. Implementation commit and
audit-record commit stay separate. Do not batch status updates. *(Step 5 makes
§5's wording cycle-neutral; until it lands, read §5's "active cycle" as this
file and `PROGRESS-v0.10.2.md`.)*

- **🤖 = Codex executes and self-verifies end to end**, with no live model
  endpoint, no publication, and no push. These tasks' correctness is provable
  offline against synthetic evidence.
- **🧑 = exactly one named operator action or decision is required** (a clean
  worktree at the released commit, or explicit authorization to publish).

### Approved cycle-activation correction — 2026-07-26

The operator supplied this runbook as an untracked file, while `AGENTS.md`
correctly still declared the latest closed cycle, v0.10.1. E0's clean-tree gate
cannot run until that known input is admitted. Before E0, in a separate
preparatory implementation/audit pair: commit this reviewed runbook, declare
v0.10.2 active in the header of `AGENTS.md`, and create
`PROGRESS-v0.10.2.md`. Run `cycle-check` and `checklist-audit`; do not claim
E0's test, golden, or artifact acceptance from this preparatory correction.

The same review corrected a publication dependency below. The hardened
workflow added in RCPT-AUTH must be published before it can attest a checkout
of v0.10.1. PUBLISH therefore distinguishes the immutable v0.10.1 release tag
from the later reviewed v0.10.2 pre-release workflow commit on remote `main`.
It never moves or recreates `v0.10.1`.

### Session opener (run before reading further)

```bash
git status --porcelain=v1
git describe --tags --always --dirty
git rev-parse HEAD
git remote -v
git rev-list --left-right --count origin/main...HEAD
sed -n '1,20p' AGENTS.md
sed -n '1,6p' STATE.md
```

### Global definition of done

Protected hashes exact; both v0.10.1 evidence pins still match (`validate`
re-hashes them and runs on runners); golden **11/11 byte-identical**;
`./run version-check` green; zero rustc warnings on offline and net builds; all
Rust tests green; all shell tests green under Python 3.11 **and** 3.12; clippy,
fmt, ShellCheck, floor byte-compilation, and locked Rust 1.78 green. No mock,
fixture, double, health response, hand-authored receipt, or workflow
configuration is promoted to wire evidence.

**The `ci-local` job count enters and exits this cycle at 19.** No task adds a
job: F1/F3 add tests inside `shell pytest`, F2 changes how `audit-deferred` is
invoked (not a ci-local job), and F4 strengthens an assertion inside the existing
`active cycle consistency` job. Any task that nonetheless changes the count
records the new count in `STATE.md` and `PROGRESS-v0.10.2.md` in the same task.
**Every check this cycle adds must run on `ci.yml` runners too, so it may touch
only source, config, and git — never the built `cored` binary or the protected
DBs.**

---

## Deferred means deferred

None of the six standing deferral triggers fires in this cycle. The CI-runner
row's trigger — *a runner execution receipt exists for the released commit* — is
**tightened** in F1 (a receipt a runner actually produced, for the exact release
commit, with the full successful matrix), not implemented into a new subsystem.

| Deferred item | Unchanged trigger | v0.10.2 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none |
| Postgres | a second archive writer | none |
| pgvector | exact cosine stops fitting the measured request budget | none |
| Multi-host seam hardening | an actual core/shell host split | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none |
| CI-runner evidence | **tightened** → an *authenticated* runner receipt set for the released commit | strengthen the acceptance guard; do not fake a receipt |
| `/view` materialization | already fired in v0.10; promoted to a future implementation | none |

---

## Step 1 · E0 — Rebuild the entering state and re-confirm the four defects 🤖

**Objective.** Reproduce the v0.10.1 closed state from commands, and confirm or
refute each of F1–F4 by path and line before touching anything. A refuted or
already-fixed defect is struck from this cycle with a note.

**Gate.** If the worktree is not clean, or `git describe` is not
`v0.10.1[-N-g…]`, or `./run ci-local` is not 19/19, stop and record — do not
implement on an unknown baseline (`AGENTS.md §1`).

**Steps.**
1. Run the session opener. Confirm HEAD relative to `e5af6bc5…`, that annotated
   tag `v0.10.1` dereferences to it locally, that `origin/main` is at
   `5bcabcb8…`, and the ahead/behind count (expect local `main` 12 ahead).
2. Run `./run ci-local` (19/19), `./run golden` (11/11), `./run verify-artifacts`
   (2/2 exact **and** both pinned evidence files `PIN MATCH`),
   `./run version-check`, `./run cycle-check`, `./run checklist-audit`.
3. Re-verify each defect against HEAD:
   - **F1** — `sed -n '656,760p' tools/audit_deferred.py`; confirm acceptance is
     ancestry + field-format only, that `conclusion` value is unchecked, and that
     no `sha == release` or full-matrix/one-run_id requirement exists. Load
     `evidence/v0.10.1/deferred-audit/report.json` and print the accepted
     receipts' `sha`, `conclusion`, and `run_id` (expect all `45fa3d49…`,
     `success`, one `run_id`).
   - **F2** — `sed -n '1216,1262p' tools/audit_deferred.py`;
     `grep -rn 'expected_head\|expected-head' tools` (expect none); confirm no
     dirty/HEAD rejection.
   - **F3** — `sed -n '346,387p;579,604p' tools/verify_llm.py`; confirm the resume
     predicate omits `http_status`/schema checks and that `model_completed=True`
     is set only within the `http 200` branch.
   - **F4** — `grep -n 'TASKS-v0.10-EXECUTION\|PROGRESS-v0.10.md\|TASKS-v0.10.1-EXECUTION\|PROGRESS-v0.10.1.md' AGENTS.md`;
     confirm the four stale literals at lines 59/214/226/230.
4. Record the measured entering state in `STATE.md`.

**Failure-capable control.** E0 must be able to refute. If any of F1–F4 no longer
reproduces on HEAD, say so explicitly and strike that Step; do not perform a fix
whose precondition is gone.

**Acceptance criteria.** 19/19 · golden 11/11 · 2/2 exact + both pins `PIN
MATCH` · each defect confirmed or refuted by captured command output · `STATE.md`
re-stamped to the measured entering state.

**Done when** every downstream Step rests on a re-measured baseline, not on this
document's assertions.

---

## Step 2 · RCPT-AUTH (F1) — Bind CI-runner receipts to their producer 🤖

**Objective.** Make `runner_receipt_measurement` enforce the complete structural
contract for a released commit, then provide an authenticated mode that rejects
anything not backed by hosted provenance. Ancestry is necessary but far too
weak; raise the structural bar to the exact release commit, successful
conclusions, and the complete expected job matrix under one run id. The
cryptographic producer claim becomes executable only when PUBLISH supplies
hosted attestation bundles.

**Gate.** Corpus-free and offline-provable — this Step touches only
`tools/audit_deferred.py`, `ci.yml` receipt metadata, and synthetic-receipt
tests. Do not weaken the ancestry check; add to it. The cryptographic
**attestation tier** is completed at PUBLISH (Step 6) because attestations are
generated only by a hosted run on the published release; wire its verification
path here but do not require attestations to exist yet.

**Steps.**
1. Require the released commit. Add a required `released_commit` parameter to
   `runner_receipt_measurement` (threaded from an `--expected-head`/release
   argument, shared with Step 3). Reject any receipt whose `sha` is not exactly
   the released commit — ancestry alone no longer suffices.
2. Require success. Reject any receipt whose `conclusion` is not `success`
   (case-insensitive). Record rejected receipts with the reason, as today.
3. Require the complete matrix under one run. Declare the expected job set
   (`core`, `golden`, `lint`, `msrv`, `net`, `shell`) as data; require that the
   accepted receipts cover **every** expected job, all sharing a single
   `run_id`/`run_attempt`. A partial or multi-run set is a finding, not a pass.
   (The `shell` job appears once per Python-matrix leg; declare the expected
   count per job so both `shell` receipts are required, not deduplicated away.)
4. Enrich the emitted receipt so authentication is possible. In each `ci.yml`
   job's `emit CI-runner receipt` step, also record the workflow name,
   `github.repository`, the event/workflow SHA, and the independently resolved
   checkout SHA; keep the `upload-artifact` persistence. Add a required boolean
   `workflow_dispatch` input named `publish_evidence`, default `false`, and the
   narrowly required `id-token: write`, `attestations: write`, and
   `contents: read` permissions. When that input is true, run
   `actions/attest-build-provenance` over the job's receipt and persist the
   generated bundle beside the receipt artifact.
5. Wire the attestation-verification path (inert until Step 6). Add explicit
   bundle input plus `--require-attestations`. Structural-only mode remains
   corpus-free, offline, and token-free. Authenticated mode requires one valid
   bundle per accepted receipt and checks the subject SHA-256, repository,
   workflow signer identity, and released checkout commit; a missing or invalid
   bundle is a rejection. Step 6 must use authenticated mode.
6. Tests (synthetic, corpus-free, so they run on `ci.yml`): extend
   `shell/tests/test_deferred_audit.py` —
   - a **hand-authored receipt** for a valid ancestor that is **not** the release
     commit is **rejected** (this is the control the finding is about);
   - a receipt with `conclusion:"failure"` is rejected;
   - a receipt set missing one expected job, or spanning two `run_id`s, does
     **not** promote the CI-runner row;
   - the complete valid matrix for the release commit **does** promote it.

**Failure-capable control.** The hand-authored non-release receipt and the
`conclusion:"failure"` receipt must both be rejected, and an incomplete matrix
must fail to promote — each demonstrated in the test suite, fail-before/pass-after
against the current guard.

**Acceptance criteria.** Structural receipts require exact release commit,
`success`, and the complete single-run job matrix · non-release/failed/partial
receipts rejected in tests · authenticated verification path wired and
failure-capable but inert offline until PUBLISH · synthetic tests pass on 3.11
and 3.12 · golden 11/11 · protected 2/2 + pins match.

**Done when** the structural tier refuses the known malformed/fabricated cases
and the authenticated tier is wired to require hosted provenance. The claim
that the accepted set was actually runner-produced is deliberately deferred
until Step 6 executes that tier.

---

## Step 3 · SUBJ-ENFORCE (F2) — Enforce the production-audit subject 🤖

**Objective.** Make it impossible to write a production receipt against a dirty
worktree or the wrong HEAD. The D2 failure class must be structurally
unreachable, not merely avoided by procedure.

**Gate.** Git-only and offline-provable. Do not change the measurement content;
add a precondition that fails **before** any measurement runs.

**Steps.**
1. Add a required `--expected-head` argument to the production/`RECEIPT` path
   (`run_production` and its `run`/argparse wiring). Before measuring, resolve
   HEAD and fail with a clear error if it is not the expected commit.
2. Reject a dirty subject. Before measuring, run `git status --porcelain=v1`; if
   non-empty, fail and print the offending paths. `git_subject()` still records
   the (now necessarily clean) status for the receipt.
3. Wire `./run audit-deferred`/the `RECEIPT` subcommand to pass
   `--expected-head <released commit>` so the on-site path is guarded by default,
   and share the released-commit value with Step 2.
4. Controls: add tests (or a `--control` mode consistent with the existing
   control surface) proving both rejections — a dirty worktree fails before
   measurement, and a mismatched HEAD fails before measurement — and that a
   clean, matching subject proceeds.

**Failure-capable control.** A dirty worktree and a wrong HEAD must each abort
before any measurement is written; the clean/matching case must produce the
report. Demonstrated by the two controls, fail-before/pass-after.

**Acceptance criteria.** `--expected-head` required · dirty worktree and HEAD
mismatch abort before measurement · on-site invocation passes the released commit
by default · both controls demonstrated · shell tests green on 3.11 and 3.12 ·
golden 11/11 · protected 2/2 + pins match.

**Done when** a production receipt can only describe a clean worktree at the
intended commit.

---

## Step 4 · RESUME-STRICT (F3) — Validate resumed adversarial evidence for internal consistency 🤖

**Objective.** Stop resume from trusting a resumed attempt's completion metadata
without checking that it is internally consistent, and halt on any resumed
`LEAK`. This closes the same defect class as F1 at the adversarial-evidence layer.

**Gate.** Touches only `tools/verify_llm.py` and its tests — a harness, not the
`/v1/ask` path. Golden must stay byte-identical.

**Steps.**
1. Tighten the reuse predicate in `_resume_valid_attempts`
   (`tools/verify_llm.py:360-365`): reuse an attempt only when it is internally
   consistent — `target_in_context` **and** `model_completed` **and**
   `http_status == 200` **and** the attempt carries the full expected schema
   (the fields a fresh completed attempt records: `outcome`,
   `violation_doc_ids`, `context_doc_ids`, `raw_overlap`, `public_overlap`,
   telemetry). A stored attempt with `model_completed:true` **and**
   `http_status:502` — a state the real path cannot produce — is refused and
   retried.
2. Halt on resumed leak. If any resumed attempt carries `outcome == LEAK`, stop
   immediately, record it in `STATE.md`, and surface it — a leak in resumed
   evidence is an HC1 signal, not a reusable cell.
3. Tests: extend `shell/tests/test_verify_llm.py` —
   - a resumed attempt with `model_completed:true, http_status:502` is **not**
     reused (retried);
   - a resumed attempt missing required schema fields is **not** reused;
   - a resumed attempt with `outcome:LEAK` halts the resume with a recorded
     signal;
   - a fully-consistent completed attempt is reused, unchanged from today.
4. Re-run `./run golden`; confirm 11/11 byte-identical.

**Failure-capable control.** The contradictory-metadata attempt and the
schema-incomplete attempt must both be refused, and the resumed-leak case must
halt — each fail-before/pass-after against the current predicate.

**Acceptance criteria.** Reuse requires HTTP 200 + full schema conformance ·
resumed `LEAK` halts · all four tests fail-before/pass-after · shell tests green
on 3.11 and 3.12 · golden 11/11 · protected 2/2 + pins match.

**Done when** no resumed attempt whose metadata is internally inconsistent can be
counted, and a resumed leak cannot be silently reused.

---

## Step 5 · AGENTS-NEUTRAL (F4) — Make the operating contract cycle-neutral, and keep it that way 🤖

**Objective.** Stop `AGENTS.md` from naming any specific cycle's runbook and log
in its per-task workflow and decision-gate sections, and add an executable guard
so this defect class cannot recur.

**Gate.** Documentation plus one assertion. Do not change any invariant in
`AGENTS.md §0`–§4; change only the four stale cycle literals and add the guard.

**Steps.**
1. Replace the four hard-coded literals — `PROGRESS-v0.10.md` at §1:59 and §5:230,
   `TASKS-v0.10-EXECUTION.md` at §5:214 and 226 — with cycle-neutral wording that
   refers back to the single **Active cycle** declaration at the top (e.g. "the
   active cycle's `TASKS-vX.Y-EXECUTION.md` named above" and "the active
   `PROGRESS-vX.Y.md`"). The header declaration remains the one place a concrete
   cycle is named.
2. Add an executable guard inside the existing `active cycle consistency`
   (`cycle-check`) job: assert that outside the **Active cycle** declaration,
   `AGENTS.md` contains **no** `TASKS-v*-EXECUTION.md` or `PROGRESS-v*.md` literal
   other than the currently active pair. Fail if any stale cycle path appears.
3. Update `STATE.md` to record that the operating contract is now cycle-neutral
   and guarded.

**Failure-capable control.** Prove the guard bites: temporarily reintroduce a
stale `PROGRESS-v0.10.md` reference in a scratch copy and confirm `cycle-check`
fails; restore.

**Acceptance criteria.** No cycle-specific `TASKS`/`PROGRESS` literal in
`AGENTS.md` outside the active declaration · `cycle-check` fails on any stale path
· guard demonstrated fail-before/pass-after · `./run cycle-check` green on the
corrected file · golden 11/11 · protected 2/2 + pins match.

**Done when** following `AGENTS.md` literally can never again edit a closed
cycle's records, and a check enforces it.

---

## Step 6 · PUBLISH — Publish v0.10.1 and authenticate hosted evidence 🧑

**One operator decision: authorize publication of the immutable v0.10.1 tag
plus the reviewed v0.10.2 pre-release workflow commits needed to authenticate
it (including the temporary failure-control branch), or decline and record the
unpublished disposition.** Everything else is Codex's.

**Objective.** v0.10.1 is complete but unpublished. Publish it under explicit
authorization, run hosted CI on the published release so authenticated
(attested) receipts exist, and re-measure the receipt under the Step 2 guard.

**Gate.** Do not push anything the operator has not explicitly authorized. Publish
the exact reviewed commits and the existing annotated tag — do not re-tag or
rewrite history. If the operator declines, record the unpublished disposition and
its trigger (explicit publication authorization) and stop; the local release
record stays valid.

**Steps.**
1. If authorized: push the reviewed local `main` through the Step 5 audit
   record and push the existing annotated `v0.10.1` tag to `origin`. Confirm
   the remote tag object is unchanged and dereferences to `e5af6bc5…`; confirm
   that commit is an ancestor of remote `main`, whose head is the separately
   reviewed v0.10.2 pre-release workflow commit. Do not claim remote `main`
   itself is the v0.10.1 release commit.
2. From the published workflow definition on remote `main`, dispatch with
   `audit_sha=e5af6bc5…` and `publish_evidence=true`. Confirm every expected job
   passes, each checkout is exactly `e5af6bc5…`, each job emits one receipt and
   persisted provenance bundle, and capture the run id/attempt.
3. Re-measure the receipt against the authenticated hosted evidence, under the
   Step 2 guard and the Step 3 subject enforcement: on a clean worktree at
   `e5af6bc5…`, with `--expected-head e5af6bc5…` and
   `--require-attestations`, write a fresh
   `evidence/v0.10.2/deferred-audit/report.json` whose accepted receipts are the
   authenticated hosted set for the released commit. Hash-pin it (Step 2's
   attestation path now exercised).
4. If declined: record the decision, date, and trigger in `STATE.md`; leave the
   release unpublished and this Step's downstream re-measurement deferred.

**Failure-capable control.** If publishing, prove the runner can still fail: push
a throwaway branch with one planted version mismatch, confirm the `version-check`
job fails there and emits a `conclusion:"failure"` receipt that the Step 2 guard
**rejects**, delete the branch. Never on the release commit or the tag.

**Acceptance criteria.** Either remote `main` at the reviewed Step 5 audit
record with immutable tag `v0.10.1` still dereferencing to `e5af6bc5…`, hosted
CI green against that checkout, and attested receipts re-measured and pinned at
`evidence/v0.10.2/…`; or a dated decline with its trigger · exact reviewed
commits published · tag unmoved · golden 11/11 · protected 2/2 + pins match.

**Done when** v0.10.1's publication state is a recorded, authorized fact, and any
hosted receipt the audit accepts is one a runner provably produced.

---

## Step 7 · R-CLOSE — Close the cycle with one explicit release identity 🧑

**One operator decision: release `v0.10.2`, or record a no-release rationale.**

**Objective.** Record the cycle's disposition and, if releasing, tag exactly one
commit.

**Gate.** Release only if the full definition of done holds and no resumed or
fresh `LEAK` was recorded anywhere in the cycle.

**Steps.**
1. Confirm the closed-state definition of done: `./run ci-local` **19/19**,
   golden 11/11, version-check green, all Rust and shell tests green on both
   interpreters, protected 2/2, both v0.10.1 pins still `PIN MATCH`, plus any new
   `evidence/v0.10.2/…` pin from Step 6.
2. Record the release/no-release rationale, the classified diff path list, the
   agreeing version authorities, and the changelog entry. State the v0.10.1
   publication outcome from Step 6 explicitly.
3. If releasing: bump the five version authorities to `0.10.2`, update
   `CHANGELOG.md`, and place one annotated tag `v0.10.2` on the release commit.

**Acceptance criteria.** Release/no-release rationale recorded · every diff path
classified · version authorities agree at 0.10.2 (if releasing) · one annotated
tag on one commit · publication outcome recorded · golden 11/11 · protected 2/2 ·
`ci-local` 19/19.

**Done when** v0.10.2's disposition is a recorded, measured decision.

---

## Cycle checklist

- [x] **E0** — entering state re-measured at v0.10.1; F1–F4 confirmed or refuted
- [ ] **RCPT-AUTH** — receipts require exact release commit, `success`, and the complete single-run job matrix; hand-authored/failed/partial receipts rejected in tests; attestation path wired
- [ ] **SUBJ-ENFORCE** — `--expected-head` required; dirty worktree and HEAD mismatch abort before measurement; both controls demonstrated
- [ ] **RESUME-STRICT** — reuse requires HTTP 200 + full schema; resumed `LEAK` halts; four tests fail-before/pass-after
- [ ] **AGENTS-NEUTRAL** — `AGENTS.md` cycle-neutral; `cycle-check` fails on any stale cycle path
- [ ] **PUBLISH** — v0.10.1 published and hosted evidence authenticated/re-measured, or a dated decline
- [ ] **R-CLOSE** — release disposition recorded and, if applicable, `v0.10.2` tagged

---

## Standing prohibitions

- Do not mutate, delete, vacuum, or "refresh" `data/core.db` or
  `data/live-smoke.db`, and do not alter or re-pin the two v0.10.1 evidence JSONs;
  their hashes are frozen. New evidence in this cycle goes to fresh
  `evidence/v0.10.2/…` paths.
- Do not weaken the receipt ancestry check, the pin re-hash in `validate`, or the
  source-deterministic re-derivation; this cycle only strengthens the acceptance
  bar.
- Do not accept a receipt a runner did not emit, describe workflow configuration
  as an execution, or count a `conclusion:"failure"` or non-release-commit
  receipt (HC13).
- Do not reuse a resumed adversarial attempt whose completion metadata is
  internally inconsistent, and never silently reuse a resumed `LEAK`.
- Do not re-tag `v0.10.1`, rewrite published history, or push anything the
  operator has not explicitly authorized.
- Do not add a job or test that calls `production_measurements()`,
  `exact_cosine_measurement()`, `view_measurement()` benchmarks, or
  `verify-artifacts` unconditionally to `ci.yml` — runners have no built `cored`
  and no protected DBs. Guard corpus-dependent checks to skip on runnerless
  environments.
- Do not hand-edit `Cargo.lock` (HC12), raise the offline Rust 1.78 floor, lower
  the Python 3.11 floor, let core call an LLM (HC3), or change the `/v1/ask` or
  `/view` JSON bodies.
- Do not commit `.env`, provider keys, tunnel aliases, or raw secret-bearing
  responses.
- Do not batch `STATE.md` / `PROGRESS-v0.10.2.md` updates or combine two tasks in
  one commit.

## Provenance of this draft

Drafted on 2026-07-26 at declared local release `v0.10.1` — release commit
`e5af6bc5df8261cc004bd4d3247b70f8cbe930bb`, annotated tag object
`8ded63f79ed12b4180e8bcd0bcff4ef30a080a79` (local only) — against (a) an
independent static read of the shipped repository tree and (b) the v0.10.1 Codex
self-audit.

**The v0.10.2 tasks themselves have not been executed.** F1–F4 were read from the
shipped tree by path and line and are hypotheses until E0 confirms or refutes
each. Independent re-verification confirmed all four findings and every reported
pass of the v0.10.1 cycle: `ci-local` 19/19; Rust 99 / net 20; shell 138/138 on
3.11 and 3.12; `X-REGEN` a fresh no-resume 45/45 battery with the real-path
positive control `GUARD FIRED` and its aggregate gate enforced (an all-`NOT
EXERCISED` run without the control firing is `FAIL`); `RECEIPT` re-measured clean
at the released commit with `{promoted:2, deferred:5}` and the restated,
falsifiable CI-runner trigger; seven runner receipts all `sha==release`,
`conclusion==success`, one `run_id`; both evidence JSONs byte-pinned with the pin
re-hashed by `validate` on runners (the deferred-audit receipt verified here at
27,786 bytes / `00cf14ae…`, matching the manifest); and the source-deterministic
re-derivation corpus-free and blocking in both `ci-local` and `ci.yml`. The
v0.10.1 self-audit contained no self-contradiction and its finding-flags were
honest.

Re-verification added two items honored above: F1's guard also never checks
`conclusion == success` or the complete single-run job matrix (so a failed or
partial receipt would count), and F4's stale-path defect also affects `§1:59`,
making four stale literals rather than the §5 block alone. F3 was confirmed but
re-scoped by severity: the contradictory `model_completed:true`+`http_status:502`
state is not naturally producible (the real path sets `model_completed` only
inside the `http 200` branch), so it is a defense against hand-edited resume
evidence — the same defect class as F1 — and correctly P2. All four findings, and
this draft, rest on one root cause: **evidence no unforgeable producer stands
behind, and no gate refused to accept, is not evidence.**
