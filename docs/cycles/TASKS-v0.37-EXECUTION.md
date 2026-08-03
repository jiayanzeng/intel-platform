# TASKS-v0.37-EXECUTION.md — publish, then make it durable

## Runbook amendments

PUBLISH — the pre-activation post-push append was rejected because the
untracked v0.37 runbook was classified as an older open cycle; the declared
fallback therefore activates first and completes PUBLISH as the first active
step — 2026-08-03
ACTIVATE — supplied runbook corrected to carry the governed artifact
boundaries and every immediately prior trigger subject in the canonical
machine-readable deferred table; no trigger or boundary moved — 2026-08-03

**Cycle:** v0.37
**Entering release:** v0.17.3, closed locally at v0.36, unpublished; v0.17.2
likewise unpublished on the same lineage
**Entering ref (hypothesis):** audit child `e068cacc76685791c54ab47c84be6abbd592271d`
**Prior cycle:** v0.36 — closed, fully discharged, 10/10/10 under its own
box-coverage control
**Autonomy:** the standing `CYCLE_AUTONOMY_AUTHORITY` block governs. Every
decision in this cycle is taken in §2 or delegated in §4 with a decision rule.
The publication in Step P0 executes under the operator's delegated grant,
recorded exactly in DR7. No operator question is routed mid-cycle.

---

## 0. Why this cycle exists

v0.36 closed the empty-witness family. What remains is making the results
durable, in three senses:

1. **Published.** Two closes sit local and unpublished. The operator has
   delegated the release decision; DR7 records it exactly. Publication makes
   both closing records immutable, gives the audit chain its external anchor,
   and relieves C7's absence-observation predicate of weight it was recorded as
   barely able to carry. It also puts the Step 1A machinery through its
   published direction for the first time on real state.
2. **Reliable.** The one v0.37 finding from the v0.36 handoff — the
   PID-plus-clock temp-directory collision in `sec_identity_measure` — is a
   flaky gate, and a flaky gate erodes exactly the measurement authority this
   project runs on.
3. **Roomy and controlled.** The export sits at 96.7% of its ceiling, and G6's
   value-domain rule is still prose. Step 3 recovers headroom through the
   established archive mechanism; Step 4 builds the release-baselined
   response-domain manifest that C4 named as the thing that would change its
   determination — converting the last empty-witness family member from
   deferral to executed control.

SEC EDGAR is **not** in scope. Its determinations are closed and its trigger
row stands; admission requires wire evidence and operator approval under the
lifecycle policy, and this runbook does not request either. The handoff states
what a single combined grant would need to contain.

---

## 1. Findings carried in

| # | Priority | Finding | Measured basis |
|---|---|---|---|
| F1 | **P1** | Parallel `sec_identity_measure` tests can collide on their temporary directory | `DisposableDir::create` names the directory `intel-platform-sec-identity-{pid}-{nanos}`; two tests in one process within one clock tick collide, and `create_dir` panics on `AlreadyExists`. The v0.36 final gate hit it once. |
| F2 | **P1** | Export headroom is 0.80 cycles | Release-parent governed field 2,885,942; delivered export 2,901,790 / 154 files; ceiling 3,000,000. Retention advance recovers the v0.35 pair (~148,051 bytes → baseline ≈ 2,753,739), but v0.36 grew the governed field by 143,456 in one cycle, so one normal cycle re-approaches the ceiling. `STATE.md` alone is 342,163 bytes — 11.8% of the export — and the archive mechanism with its permanent-tail marker already exists. |
| F3 | **P2** | G6's value-domain rule remains prose | C4's own falsifier: "a complete release-baselined response/domain manifest would change that determination." All six `/v1/*` routes live in `shell/intel_shell/app.py` (`/v1/signals`, `/v1/search`, `/v1/brief`, `/v1/ask`, `/v1/billing/webhook`, `/v1/billing/stripe`) — a FastAPI surface whose native schema emission is the obvious derivation seam. |

---

## 2. Decisions taken — do not re-litigate

If a measurement refutes a stated basis, record the refutation, stop that step,
continue with the rest, and surface it at handoff.

### DR7 — Publication of v0.17.2 and v0.17.3: granted, exact

The operator delegated the release decision to the reviewer
("decide how to release based on best practices," 2026-08-03). The decision is
**publish both, now, before activation**, and this section is the exact
authorization instrument.

**Why both:** publishing makes both closing records immutable under the
retraction bar and anchors the hosted-run evidence externally. Leaving either
close unpublished extends the span where the only publication evidence is a
dated absence observation — the predicate C7 itself recorded as unable to
refresh offline. A partial publish (main + v0.17.3 only) would leave a
published lineage containing an unpublished tagged close inside it, a state
with no precedent here and no stated reason.

**The exact grant.** All identities verbatim; any mismatch is a stop:

- Remote: `origin`. Branch: `main`, currently `f02379f…`, advanced by
  **fast-forward only** to `e068cacc76685791c54ab47c84be6abbd592271d`.
- Annotated tags pushed after the branch: `v0.17.2` (object
  `16ee7bcb2214859156edbceeb5e314ac1a67f39b`, target
  `9996c6820d720160b64607575d0270d2e5393ef9`) and `v0.17.3` (object
  `0fe42d7a6a86e94bb95a93a86b7a4b09917b97f4`, target
  `a5afab9e6842a1b6c00a7d17fdeaa3e254edf80f`).
- Non-force. Nothing deleted. No other ref moves. This grant covers exactly
  these three refs at exactly these objects, once.

**Preconditions, each measured and recorded immediately before the push:**
`git ls-remote` shows `main` at `f02379f…` and both tags absent;
`git merge-base --is-ancestor f02379f… e068cacc…` succeeds; the local tag
objects match the identities above. Any precondition failing is a
stop-and-report — the remote moved or the lineage differs from what this grant
was issued against, and the grant does not transfer.

**Irreversibility is accepted and one-directional.** Once pushed, the records
are published: the retraction bar applies to them, and no failure afterward is
grounds to delete or force-move a ref. If the post-push hosted run fails, the
truthful state is "published, hosted verification failed," recorded as such
and stopped on — not unwound.

### DR8 — STATE.md archival: granted, bounded

Step 3 may create one new append-only archive file under `docs/state-archive/`
and pin it in `config/protected-artifacts.json` at grade `structural`,
following the `STATE-through-v0.28.md` precedent exactly. This is the one
structural-archive write the standing ask-first list reserves, granted here
with bounds: content moved out of `STATE.md` is byte-identical in the archive;
the move is subtractive from `STATE.md` and additive to the archive with
nothing altered in between; the permanent tail and its marker stay in
`STATE.md`; and the archive file, once pinned, is never edited. The boundary —
which history moves — is C10's.

### DR9 — Version disposition rule, carried forward

DR5's three clauses govern unchanged, in precedence order: minor for a new
route or observable named surface; minor for any addition, removal, or
redefinition of a value in the domain of a serialized `/v1/*` field
(adjudicated this cycle against the Step 4 manifest, not prose, if Step 4
lands); otherwise patch. Step 4's constraint is byte-identical `/v1/*`
payloads, so the expected disposition is **patch v0.17.4**; the reasoning is
recorded either way, and any Step 4 measurement showing payload movement is a
stop under §3.

### DR10 — The v0.37 close defaults to unpublished-local

R-CLOSE ends with the annotated tag local and a fresh dated absence
observation for the new release, exactly as v0.36 did — the lifecycle now
represents this truthfully and the publication question rides the handoff.
DR7 is a one-time grant for the two named releases and does not extend to
v0.17.4.

---

## 3. The retained gate and stop conditions

**Publishing anything beyond DR7's three named refs requires separate exact
operator authorization.** DR7 spends the operator's delegated grant precisely
once; it establishes no standing publication authority.

Stop-and-report conditions (halt the affected step, record the measurement,
continue unaffected work, surface at handoff):

1. A DR7 precondition fails, or the post-push hosted run fails.
2. A measurement indicates a **published** record contains a false claim —
   after Step P0 this includes every v0.35 and v0.36 record.
3. A change would move an entitlement or licensing outcome, a golden input, a
   protected database, an `observation`-grade byte, or a dependency
   resolution.
4. Any `/v1/*` payload byte moves under Step 4.
5. A change would move an accepted boundary or ceiling — including the
   3,000,000-byte export ceiling — rather than select inside it.

---

## 4. Codex-owned determinations

Measure, decide, record the reasoning and the falsifier. A recorded decision
with a stated falsifier is complete work.

### C8 — the manifest derivation seam

Step 4 needs a machine-readable statement of each serialized `/v1/*` field's
value domain, derived from the serialization types themselves — never a
hand-maintained parallel list. The routes are FastAPI; native schema emission
is the obvious seam, but measure first whether the routes serialize through
declared response models at all. If they serialize raw dicts, the models must
be introduced — under the hard constraint that every `/v1/*` payload stays
byte-identical, proven by the configured-subscription comparison machinery
Step 4 of v0.36 built plus golden zero-delta. If byte-identity cannot be
proven under model introduction, that finding outranks the manifest: record
it, defer G6 again with the sharpened trigger, and do not ship a
behavior-moving "refactor" to get a schema.

### C9 — the collision-proof directory mechanism

Collision-proof by construction, std-only preferred: a retry-on-`AlreadyExists`
loop with a varying component, or an atomic create pattern. The executable
witness is a unit test that pre-creates the candidate path and proves creation
still succeeds — a rerun-until-green criterion is not a control.

### C10 — the archive boundary

Derive the boundary from a stated principle rather than picking a line number:
keep in `STATE.md` the current publication epoch and one prior, archive
everything older, keep the permanent tail. Target: post-archival delivered
export ≤ 2,600,000 bytes (≥ 2.5 cycles of headroom at the measured v0.36
growth rate). If the derived boundary cannot reach the target, report the
exact shortfall and the ceiling question rides the handoff — the ceiling
itself is not moved (§3.5).

### C11 — anything E0 surfaces

Standing latitude to add rules; none to add acceptance criteria nothing
executes.

---

## 5. Dependency gates

- Step P0 precedes ACTIVATE. If `cycle-check` rejects the pre-activation
  post-push append (the v0.36 Step 0e precedent), activate first, run P0 as
  the first step, and record which ordering executed — the ordering is
  derived, not asserted.
- Steps 2–4 require **E0 complete**. Steps 2, 3, 4 are otherwise independent
  and may interleave.
- Step 5 runs only if Step 4 (or any step) moved production code, under the
  standing evidence-ref authority.
- Step 6 requires every prior step complete or explicitly deferred with a
  dated observation, and Step 3's re-measured governed rows.

---

## Declared scope

The standing always-allowed set remains `STATE.md`, this runbook, and
`docs/cycles/PROGRESS-v0.37.md`. The table is otherwise exact;
release-authority precedence applies only at R-CLOSE.

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `release` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
| `allow` | `docs/intel-platform-OPERATIONS.md` |
| `allow` | `docs/state-archive/**` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `tools/checklist_audit.py` |
| `allow` | `tools/progress_check.py` |
| `allow` | `tools/domain_manifest.py` |
| `allow` | `tools/audit_deferred.py` |
| `allow` | `tools/evidence_artifacts.py` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `config/checklist-exemptions.json` |
| `allow` | `config/protected-artifacts.json` |
| `allow` | `shell/intel_shell/**` |
| `allow` | `shell/tests/**` |
| `allow` | `crates/**/src/**` |
| `allow` | `crates/**/tests/**` |
| `allow` | `apps/**/src/**` |
| `allow` | `repomix.config.json` |
| `allow` | `run` |
| `forbid` | `tools/model_profiles.py` |
| `forbid` | `.github/workflows/**` |
| `forbid` | `config/core.json` |
| `forbid` | `config/schedule.json` |
| `forbid` | `config/entities.json` |
| `forbid` | `config/subscriptions*.json` |
| `forbid` | `observations/**` |
| `forbid` | `fixtures/**` |
| `forbid` | `docs/cycles/**` (except this runbook and `PROGRESS-v0.37.md`, by standing precedence) |
| `release_authority` | `Cargo.toml` |
| `release_authority` | `Cargo.lock` |
| `release_authority` | `crates/*/Cargo.toml` |
| `release_authority` | `apps/*/Cargo.toml` |
| `release_authority` | `shell/intel_shell/__init__.py` |
| `release_authority` | `shell/intel_shell/app.py` |
| `release_authority` | `CHANGELOG.md` |
| `release_authority` | `README.md` |

`docs/state-archive/**` moves from forbid to allow under DR8's bounds and only
for Step 3's one new file plus its pin. `shell/intel_shell/**` moves to allow
under C8's byte-identity constraint. Everything else matches the v0.36 table.

**Step 3 scope correction (2026-08-03).** The supplied table forbade
`tools/evidence_artifacts.py` even though DR8 requires a new exact structural
archive pin and that tool's `STRUCTURAL_ARCHIVE_PIN_PATHS` is the executable
admission registry. The pre-implementation validator inspection proved a new
path cannot pass the stated acceptance without changing that registry. Per the
operating contract's gate-versus-criteria rule, the gate is widened for the one
new exact archive path and its focused schema control; no general archive
prefix is admitted.

**Step 4 scope correction (2026-08-03).** C8's required response-model
decorators make the existing `/v1/ask` and billing decorators multi-line. The
source-deterministic deferred audit assumed their exact prior one-line syntax,
so the complete shell population failed before it could rederive the committed
receipt. The supplied table omitted `tools/audit_deferred.py`, making the
acceptance population and scope mutually unsatisfiable. The table now permits
only that bounded parser compatibility change: route boundaries are discovered
from actual Python AST decorators instead of textual one-line spellings. No
deferred disposition, receipt byte, or audit outcome changes.

The prior cycle's documents are protected by the `docs/cycles/**` forbid.

---

## Step P0 · PUBLISH — execute DR7

**Objective.** Publish `main`, `v0.17.2`, and `v0.17.3` exactly as granted,
then bring the lifecycle records to the published state truthfully.

Sequence:

1. Record every DR7 precondition measurement, dated.
2. Push `main` fast-forward to `e068cacc…`. Push both annotated tags.
3. Record the push-triggered hosted run on `main` at `e068cacc…`: run id,
   attempt, conclusion. It must pass all blocking identities.
4. Append to `STATE.md`, in the exact five-field form, one post-push record
   per release — this supersedes each absence observation without editing it:

   ```
   - **Post-push verification date:** 2026-08-0X
   - **Post-push release:** v0.17.2
   - **Post-push annotated tag object:** `16ee7bcb2214859156edbceeb5e314ac1a67f39b`
   - **Post-push closing commit:** `9996c6820d720160b64607575d0270d2e5393ef9`
   - **Post-push hosted run:** `<run id>`
   ```

   and likewise for `v0.17.3` with object `0fe42d7a…`, closing commit
   `a5afab9e…`, and the same run id. Both records land in `STATE.md` at column
   zero — the record regex is line-anchored, and an indented append matches
   nothing. Update the `STATE.md` status header to
   say published — the header is current status, not a dated measurement, and
   leaving "unpublished" in it after the push would be a false claim.
5. The dated absence observations remain in place untouched, as true
   historical measurements.

**Acceptance criteria.** `ls-remote` shows all three refs at the granted
objects; the hosted run passed and its id is recorded; `./run cycle-check`
passes on the **published** path for both releases — the required-and-fresh
post-push R12 control site now binding on real published state — and the
Step 1A planted controls pass unmodified; `progress-check` passes.

**Done when** the published state is the measured state and no record asserts
anything the remote does not show.

**Measured disposition — 2026-08-03.** The publication and both post-push
records completed exactly, but the acceptance assertion that `cycle-check`
binds both releases was refuted at the entry point: it selects only
`newest_closed_release`, reports v0.17.3, and never reads v0.17.2's older
record. Fresh `ls-remote` and local object inspection independently match all
v0.17.2 fields. The affected historical multi-release control claim is
explicitly deferred; no record is false, no ref is unwound, and unaffected
steps continue under §2.

---

## ACTIVATE

- Move the `AGENTS.md` active-cycle declaration to v0.37; create
  `docs/cycles/PROGRESS-v0.37.md`; commit this runbook.
- Advance retention to v0.36–v0.37 through the derived pattern; if the derived
  value and `repomix.config.json` disagree, the disagreement is the finding —
  record before changing either.

**Acceptance criteria.** `cycle-check` resolves v0.37 from the declaration
alone; retention derives to exactly v0.36–v0.37; the excluded boundary is
reported as a measurement.

---

## Step 1 · E0 — entering-state reconstruction

Every figure is a hypothesis from a source-export review; no repository
command produced any of them. Confirm or refute against real bytes. A refuted
hypothesis is a finding, not an error to route around.

| # | Hypothesis | How to settle |
|---|---|---|
| H1 | Object graph: release parent `9946ceda…`, closing `a5afab9e…` (immediate child), tag `0fe42d7a…` → `a5afab9e…`, audit child `e068cacc…` (immediate child of closing) | `git cat-file` / `rev-parse` the chain |
| H2 | `f02379f…` is an ancestor of `e068cacc…`; remote `main` sits there; both tags absent remotely | `merge-base --is-ancestor`; `ls-remote` — these are also DR7 preconditions and are recorded twice: here and immediately before the push |
| H3 | `DisposableDir::create` names `intel-platform-sec-identity-{pid}-{nanos}` and panics on `AlreadyExists`; pre-creating the path reproduces the v0.36 flake deterministically | read the code; write the forced-collision reproduction |
| H4 | Registry 14 rules / 81 controls; exemptions 9; retractions 3; checklist 287/3/278+9 | run the tools |
| H5 | Retention pattern excludes through v0.34; delivered export 2,901,790 / 154; the v0.35 pair is 148,051 bytes, so post-retention baseline ≈ 2,753,739 before v0.37 growth | measure the export at the activation tree |
| H6 | `STATE.md` is 342,163 bytes with exactly one permanent-tail marker and exactly two absence observations (v0.17.2, v0.17.3) | `wc -c`, grep counts |
| H7 | All six `/v1/*` routes live in `shell/intel_shell/app.py`; whether they serialize through declared response models is **unmeasured** and decides C8's path | enumerate decorators; read each handler's return path |
| H8 | Hosted CI triggers on `push: branches: [main]`, so the P0 run exists without workflow edits | read `ci.yml` (workflows are forbidden to edit; this only reads) |
| H9 | The v0.36 governed-field growth was +143,456 bytes; C10's ≤ 2,600,000 target therefore implies ≥ 2.5 cycles headroom | arithmetic against measured figures |

Plus the standing entering measurements: `git status --porcelain` (expected
untracked set: the three amendment inputs, exactly), full `./run ci-local`,
`invariant-scan --self-test`, shell tests, golden — counts, not adjectives.

**Acceptance criteria.** Every hypothesis carries a dated verdict: confirmed,
refuted, or unmeasurable-with-stated-reason.

**E0 verdicts (measured 2026-08-03).**

| # | Verdict | Measured result |
|---|---|---|
| H1 | **confirmed** | `9946ceda…` is the release parent and immediate parent of `a5afab9e…`; tag object `0fe42d7a…` peels to `a5afab9e…`; `e068cacc…` is its immediate audit child. |
| H2 | **confirmed for the entering DR7 measurement; superseded after publication** | Immediately before PUBLISH, `main=f02379f…`, both tags were absent, and the ancestor check passed. The fresh E0 remote measurement has `main=e068cacc…` and both exact tags present, as DR7 required. |
| H3 | **confirmed** | The entering PID-plus-nanoseconds constructor panics on `AlreadyExists`; a test-only nonce seam pre-created the exact path and reproduced the caught panic deterministically, **1/1**. |
| H4 | **refuted** | Registry **14/81**, exemptions **9**, and retractions **3** are correct; the pre-E0 checklist is **289 checked / 3 retracted / 280 matched / 280 resolved / 9 exemptions**, not 287/3/278+9. |
| H5 | **partly confirmed, otherwise refuted** | The v0.35 pair is exactly **148,051 bytes**. Commit-exact exports are **2,858,294 / 151 / 2** at `e068cacc…` and **2,746,484 / 151 / 2** at activation `5884ef77…`; 2,901,790/154 included three untracked inputs, and the 2,753,739 estimate is 7,255 bytes high. |
| H6 | **refuted** | Pre-record State is **345,139 bytes**, with one permanent-tail marker and two absence observations; PUBLISH has additionally added two exact post-push records. |
| H7 | **confirmed and C8 selected** | Exactly six `/v1/*` routes are in `app.py`; runtime introspection reports `response_model=None` for all six. Five return raw dictionaries and one returns `PlainTextResponse`, so C8 takes the response-model introduction path. |
| H8 | **confirmed** | `.github/workflows/ci.yml` lines 19–21 trigger on pushes to `main`; no workflow byte moved. |
| H9 | **confirmed** | At +143,456 bytes/cycle, a 2,600,000-byte export leaves 400,000 bytes = 2.79 cycles; the 2.5-cycle threshold permits at most 2,641,360 bytes. |

Standing measurements also passed: the entering status named exactly the three
untracked amendment inputs; `ci-local` passed **22/22**; the registered scan
passed **14/14 rules / 81 controls**; permission-complete Python 3.11 and 3.12
each passed **368/368** with identical populations; and golden passed
**11/11**. The test-only collision reproduction moved no production code. No
E0 stop condition fired.

**Done when** dependent steps start from measurements, not from this document.

---

## Step 2 · TEST-ISOLATION — remove the collision, prove it

Per C9. Replace the clock-and-PID name with a collision-proof construction.

**Acceptance criteria.** The forced-collision unit test (pre-created path)
passes; the full store test suite passes under default parallelism across a
stated repeated-run count with zero `AlreadyExists`; no production code moved
in this step, stated explicitly.

**Done when** the v0.36 flake's reproduction is impossible by construction,
not improbable by clock.

---

## Step 3 · STATE-ARCHIVE — recover headroom inside the mechanism

Per DR8 and C10.

**Acceptance criteria.** The archive file exists, is pinned `structural`, and
`verify-artifacts` matches it; moved content is byte-identical (prove by
hash-of-concatenation or equivalent, stated); `STATE.md` retains its permanent
tail, both post-push records, the current-epoch body, and every field the
`GOVERNED_ARTIFACT_ROW_SPECS` and publication checks parse; `cycle-check` and
`progress-check` pass; the delivered-export measurement is restated with the
new baseline against the C10 target, and the governed rows re-measured.

**Done when** headroom is restated in bytes, %, and cycles — and either meets
the target or carries the exact shortfall for the handoff.

---

## Step 4 · DOMAIN-MANIFEST — G6 gets an executed control

Per C8 and F3.

**4a — derive the manifest.** One release-baselined machine-readable statement
of every serialized `/v1/*` response field and its value domain, derived from
the serialization types, emitted by `tools/domain_manifest.py` (new), and
recorded as the v0.17.4 baseline.

**4b — register the rule.** A new invariant rule diffs the derived manifest
against the release-baselined one and fails on any added, removed, or
redefined field domain absent a minor disposition. Planted controls: mutants
that add an enum variant, remove a field, and change a field's type — each
fails before and passes after, control-site anchored.

**4c — byte-identity holds.** The complete configured-subscription `/v1/*`
comparison from v0.36 Step 4 reruns byte-identical, and golden is 11/11 zero
delta. Any movement is a §3.4 stop.

**Acceptance criteria.** Manifest derived not declared; rule registered with
executable `fail_before` mutants; `invariant-scan --self-test` totals stated;
byte-identity proven; DR9's clause 2 at close cites the manifest diff, not
prose. If C8 concluded the models cannot be introduced byte-identically, this
step records that finding, updates the G6 deferral trigger to name it, and
ships nothing.

**Done when** a value-domain change without a minor bump is a failing check,
or the precise obstacle is a recorded finding with a sharpened trigger.

---

## Step 5 · RE-MEASURE — hosted, conditional

Runs only if production code moved (C8's model introduction qualifies; Step 2
must not). Evidence ref per the standing authority: `codex/v0.37-evidence-…`,
`ls-remote` pre-check recorded, non-force, one ref, `main` and tags untouched.
Report run id, attempt, ref, identity count. If it does not run, record the
dated reason and which claims rest on local execution only.

**First candidate finding (2026-08-03).** Production shell moved, so exact
audited candidate `2e5921f0d0d3f4d64bde56b95325216d33caa59b` was pushed once
to fresh immutable ref `codex/v0.37-evidence-2e5921f` after an empty
`ls-remote` result. Run `30832624982`, attempt 1, passed **8/9** blocking
identities and failed only the Python 3.11 pre-install invariant step: R15
imported FastAPI/Pydantic before the workflow's existing install phase. This
is a topology defect, not a hosted transient, so the run was not retried and
the ref was not moved. R15 now dependency-freely derives the contract from the
actual route/type AST and the installed shell population separately proves
equivalence to runtime OpenAPI. Step 5 remains open; only a new exact candidate
on a fresh non-force evidence ref can satisfy it.

---

## Step 6 · R-CLOSE

Two-commit tagged close under the corrected ordering, stated here so it needs
no amendment: release parent → closing commit carrying the record with this
cycle's boxes checked → local annotated tag (v0.17.4 if DR9 yields a release)
→ **append-only audit child as the immediate next commit**, carrying
`- cycle-ending review-export audit: closing_tree=…; bytes=…; audit_delta=…`
measured against the closing tree it follows. The audit child is the final
commit of v0.37 and the next cycle's entering ref. Every other criterion is
evaluated at the assembled closing worktree; the audit-field criterion alone
at the audit child. Deferring the field past the cycle remains prohibited.

**Acceptance criteria.**
- Dated disposition per DR9, naming any behaviour movement rather than letting
  the version imply its absence; clause 2 adjudicated against the Step 4
  manifest if it landed.
- `version-check` passes, authorities and restatements counted.
- `checklist-audit` passes with all four figures stated and a non-zero v0.37
  line.
- Governed export row bound; audit child present in the stated order;
  `audit_delta` reconciled against the current governed baseline at the
  assembled closing worktree.
- Per DR10: fresh dated absence observation for the new release; post-close
  `cycle-check` passes truthfully on the mixed state — two published releases
  with post-push records, one unpublished local close with its observation —
  and the Step 1A planted controls pass unmodified.
- Every deferral row carries a dated v0.37 observation; triggers unchanged.
- `invariant-scan --self-test`, shell, golden: counts stated, zero hand-typed
  finding lines.
- No publication beyond DR7's three refs (§3).

**Done when** the cycle is closed, audited, truthfully represented, and the
handoff written.

---

## Governed artifact byte-boundary authority

- governed artifact byte boundary: path=`STATE.md`; bytes=`453741`
- governed artifact byte boundary: path=`config/protected-artifacts.json`; bytes=`1048576`

**Carried forward byte-identically.** A change to either figure is an
architectural change requiring its own justification and operator
authorization. The 3,000,000-byte review-export ceiling remains separately
governed.

---

## Deferred means deferred

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.37 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | v0.37 · 2026-08-03 — PUBLISH started no harvester and observed no second concurrent harvester; the trigger did not fire. | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.37 · 2026-08-03 — PUBLISH made no live publisher request, observed no transient robots outage, and received no Decision B authorization; the trigger did not fire. | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.37 · 2026-08-03 — No live publisher request or 304 observation occurred; the combined trigger did not fire. | none |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.37 · 2026-08-03 — Scope permits the ingest source path, but no connector review occurred and no mapping changed; the combined trigger did not fire. | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.37 · 2026-08-03 — PUBLISH ran no publisher runtime, added no origin, and observed no concurrency; the trigger did not fire. | none |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | v0.37 · 2026-08-03 — No bounded scheduled window was authorized or executed; the trigger did not fire. | none |
| Postgres / pgvector / multi-host seam | unchanged | v0.37 · 2026-08-03 — PUBLISH changed remote release refs and State only; no Postgres, pgvector, or multi-host seam appeared. | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.37 · 2026-08-03 — No third-party shell or replacement-shell HC1 claim appeared; the trigger did not fire. | none |
| L2 forced-command wrapper | an operator server session | v0.37 · 2026-08-03 — No operator server session occurred; the trigger did not fire. | none |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.37 · 2026-08-03 — DOMAIN-MANIFEST's complete registered scan passed **15/15 rules / 84 controls**; R3/R4 found no outside spelling. | none |
| `--features net` Rust 1.86 execution | a scoped cycle authorized to change evidence topology and an executable local or hosted lane that actually pins and runs the net path on Rust 1.86 | v0.37 · 2026-08-03 — Hosted PUBLISH run 30824053490 executed the pinned Rust 1.86 success lane, while workflow/evidence topology remains scope-forbidden; the combined trigger did not fire. | none |
| GitHub attestation verifier version admission | the installed or proposed `gh attestation verify` version differs from the exact repository pin, or its accepted bundle/workflow contract changes | v0.37 · 2026-08-03 — No verifier pin or accepted bundle/workflow contract changed; the trigger did not fire. | none |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.37 · 2026-08-03 — No third-publisher review or admission occurred; the trigger did not fire. | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.37 · 2026-08-03 — DR7 moved only main, v0.17.2, and v0.17.3; it did not authorize or move either historical tag. | none |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.37 · 2026-08-03 — PUBLISH did not move either historical tag or remove the hosted flag; the combined trigger did not fire. | none |
| Manifest retention/indexing | the manifest reaches its governed artifact byte boundary, or two consecutive clean `./run verify-artifacts` runs each take ≥1.00 s real | v0.37 · 2026-08-03 — STATE-ARCHIVE measured **193,830 / 1,048,576 bytes**, **333 pins**, and two complete checks at **0.09 s / 0.10 s real**. Neither trigger fired. | none |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.37 · 2026-08-03 — DOMAIN-MANIFEST moved non-version shell source, so the broad trigger fired. Step 4 rechecked the literal as one of `version-check`'s syntax-derived executable authorities and retained it package-owned; R-CLOSE will move its value with the other authorities. | **Step 4 completed 2026-08-03** |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.37 · 2026-08-03 — DOMAIN-MANIFEST completed the authorized G6 subcase: R15 now derives and diffs every declared `/v1/*` response domain. Other heterogeneous R-CLOSE criteria remain prose adjudications. | **Step 4 completed 2026-08-03** |
| Second `STATE.md` archival | the export ceiling trigger fires, or `STATE.md` reaches its governed artifact byte boundary | v0.37 · 2026-08-03 — DR8 authorized completion ahead of the unchanged trigger: the post-record live State is **94,681 / 453,741 bytes** and the structural archive is pinned at **258,658 bytes**. Neither boundary trigger had fired. | none |
| Retention derivation across a version-family boundary | an active cycle whose name is not of the form `v0.<n>` — raising at `v1.0`–`v1.2`, silently under-excluding from `v1.3` onward | v0.37 · 2026-08-03 — The active cycle is v0.37; the version-family trigger did not fire. | none |
| Published-release divergence | the unpublished distance contains a measured runtime behaviour difference persisting across three consecutive closed cycles within the current publication epoch, or acquires any public-surface change | v0.37 · 2026-08-03 — Exact publication of v0.17.3 resets the count to zero at its closing commit. DOMAIN-MANIFEST adds validation and native derivation for the already-serialized contract, while the complete ten-response witness remains exact at **6,869 bytes / SHA-256 `dfec8ff81d68526dd5468ce22660be9d7678c6a8fdd8e52d6ac921c83371cef3`**, the manifest diff is empty, and golden is **11/11**. No measured runtime or public `/v1/*` surface difference starts or fires the trigger. | none |
| MSRV current-restatement membership | a current restatement of either Rust floor lands outside the registry without failing a check | v0.37 · 2026-08-03 — PUBLISH changed no Rust-floor restatement or registry member, and the registered scan passed. | none |
| Retention arithmetic fallback | the retention formatter again permits an omitted retained set, or any live production or fixture caller supplies a set not derived by `expected_retained_cycle_paths` for that root | v0.37 · 2026-08-03 — ACTIVATE derives exactly the v0.36–v0.37 retained set and advances only the excluded boundary through v0.35. | none |
| Optional cycle-ending audit disclosure | a closed cycle whose delivered export differs from its governed figure and which records no cycle-ending audit field | v0.37 · 2026-08-03 — v0.36's immediate audit child already records its closing-tree difference; v0.37 remains open. | none |
| SEC EDGAR admission | the three v0.25 determinations closed | v0.37 · 2026-08-03 — The determinations remain closed; no admission or live wire request occurred, and admission still awaits the combined grant named in the handoff. | none |
| License enum semantics | a second publisher requires an inexpressible license value | v0.37 · 2026-08-03 — No second publisher or inexpressible license value appeared; the trigger did not fire. | none |
| Terms-level automated-access gate | a candidate's terms restrict beyond robots.txt | v0.37 · 2026-08-03 — No candidate terms review occurred; the trigger did not fire. | none |
| Feed shape observation | an uncovered publisher feed shape | v0.37 · 2026-08-03 — No publisher feed was fetched and no uncovered shape was observed; the trigger did not fire. | none |
| Threshold-authority limitation | a common dependency module or manifest edge appears between store and view | v0.37 · 2026-08-03 — v0.36 completed the shared `assign_dedup_identity` seam under R14; PUBLISH changed neither consumer nor manifest edge. | none |
| ARCHITECTURE.md §8 / AGENTS.md R-CLOSE tag-mechanics duplication | the restatements diverge | v0.37 · 2026-08-03 — PUBLISH left both restatements unchanged and the registered authority checks passed; no divergence was observed. | none |
| Review-export capacity | the export crosses the declared ceiling | v0.37 · 2026-08-03 — STATE-ARCHIVE's delivered worktree export is **2,558,258 bytes**, leaving **441,742 bytes / 14.72% / 3.08 cycles** at the measured +143,456-byte denominator. The trigger did not fire. | none |
| Public value-domain control (G6) | a `/v1/*` field's domain changes undetected | v0.37 · 2026-08-03 — DOMAIN-MANIFEST derives **6 routes / 31 status-media variants / 112 field occurrences** into the v0.17.4 baseline. R15's added-enum, removed-field, and changed-type mutations each fail at the serialization control site; the complete scan passes **15/15 rules / 84 controls**. | **Step 4 completed 2026-08-03** |

---

## Standing prohibitions

- No closed-cycle document, observation, or fixture edited; corrections are
  forward and dated. After P0 this carries the published-record weight.
- No push beyond DR7's three refs and the standing evidence-ref authority. No
  force-push, ref deletion, or tag movement anywhere, ever.
- No expectation, anchor, or figure copied from a checker's own output where
  the construction can produce it independently.
- No acceptance criterion discharged by inspection where a registered
  self-testing rule with an executable `fail_before` can exist.
- No hardcoded scope list where the scope can be derived.
- No acceptance discharged by an executable whose witness set is empty.
- No retraction added without quoting the bar and obtaining an operator
  decision.
- The ask-first list is not widened by convenience; DR7 and DR8 are spent
  grants, not precedents.
- The three untracked amendment inputs stay untouched.

---

## Cycle checklist

- [x] PUBLISH
- [x] ACTIVATE
- [x] E0
- [x] TEST-ISOLATION
- [x] STATE-ARCHIVE
- [x] DOMAIN-MANIFEST
- [ ] RE-MEASURE
- [ ] R-CLOSE

*Box ids match the `PROGRESS-v0.37.md` entry ids exactly; the box-coverage
rule audits this runbook like any other.*

---

## Handoff

One report: each DR executed and whether any measurement refuted its basis;
each C-determination with reasoning and falsifier; every stop condition
triggered or an explicit none; the post-archive headroom figures; and the
v0.38 findings list — findings, not proposed acceptance criteria; the criteria
come from review.

Then the two standing operator questions, stated once each: publication of
v0.17.4 (DR10 default leaves it local), and SEC EDGAR admission — which now
needs exactly one combined grant covering the live wire request and the
admission approval under the
`append_only_chained_records_with_wire_evidence_and_operator_approval`
lifecycle, the determinations having been closed since v0.25's observations
were pinned.

---

## Provenance

**What I measured, on the delivered post-v0.36 export (2,901,790 bytes / 154
files, byte-exact against the reported final figure):** the C7 predicate
implementation and both record regexes (`POST_PUSH_RECORD_RE` five fields;
`UNPUBLISHED_LOCAL_CLOSE_RE` five fields; the published path takes precedence
once a record exists, so absence observations are superseded by append, not
edit); the R12 control sites for required-and-fresh post-push and for
audit-child ordering; `ci.yml` triggering on `main` pushes; the
`DisposableDir` nonce construction; the retention pattern excluding through
v0.34; the v0.35 pair at 148,051 bytes; `STATE.md` at 342,163 bytes with one
permanent-tail marker and two absence observations; the six `/v1/*` routes in
`shell/intel_shell/app.py`; the registry at 14 rules / 81 controls; nine
exemptions; the v0.36 declared-scope table format this one mirrors; and the
deferred table recording the v0.25 determinations as closed with the
threshold-authority trigger discharged through shared `assign_dedup_identity`
under R14.

**What I could not measure and marked as hypotheses:** anything requiring
`.git` — ancestry of `f02379f…`, remote state, local tag object identity —
which is why H1/H2 exist and why DR7's preconditions are measured again at
push time. **What I did not do:** no repository command, no push, no test run;
every figure above is for E0 to confirm against real bytes.
