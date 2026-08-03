# TASKS-v0.38-EXECUTION.md — the admission cycle

## Runbook amendments

**Cycle:** v0.38
**Entering release:** v0.17.4, closed locally at v0.37, unpublished; v0.17.2
and v0.17.3 published with post-push records
**Entering ref (hypothesis):** audit child `a7d6c80e7e5ccd963e8ebb46ee054b30af88abb0`
**Prior cycle:** v0.37 — closed, fully discharged; both operator questions
carried forward intact
**Autonomy:** the standing `CYCLE_AUTONOMY_AUTHORITY` block governs. This
cycle contains two milestone steps that are **dormant by construction**: each
executes only under an operator grant whose exact required content is stated
in §2, and each records a dated not-granted observation otherwise. Everything
else is decided here or delegated with a rule.

**Do not start this cycle with neither grant issued.** Without at least one,
the autonomous remainder is observation upkeep and one rehearsal-coverage
step — not worth a cycle's overhead. The operator issues Grant A, Grant B,
both, or defers the cycle.

---

## 0. Why this cycle exists

v0.37 left the project at a clean pause: the empty-witness program is closed,
the lifecycle is truthful in both publication directions, headroom is 2.27
cycles, and the two remaining milestones are operator-gated by design —
publishing v0.17.4, and admitting SEC EDGAR as the second publisher.

The admission is closer than the deferral table's age suggests. Measured on
the current export: `sec-edgar-usgaap` is already a configured finance source
(`PublisherPermitted`, real SEC URL); the v0.25 observation set is pinned
(feed shape, robots.txt, terms determination, and an 892,641-byte captured
feed); and `sec_observation_replay.rs` already replays that captured feed
through the real ingest path, with the store and cored test suites consuming
the same fixture. The state machine is proven on fixtures. What remains is
exactly what HC13 says fixtures cannot prove — the wire — and that is what
Grant B authorizes.

---

## 1. Findings carried in

| # | Priority | Finding | Measured basis |
|---|---|---|---|
| F1 | **P3** | C10's headroom target was missed by 74,055 bytes and recorded honestly | Target ≤ 2,600,000; release parent measured 2,674,055 → 325,945 bytes / 2.27 cycles at +143,456/cycle. Below target, above trigger. No action this cycle; the deferral row continues to monitor. |
| F2 | **P2** | The rehearsal's fixture coverage has not been enumerated against the admission checklist | The replay test exists, but whether it exercises the license gate on `PublisherPermitted`, the robots-compliance path against the pinned `sec-edgar-robots.txt`, and dedup identity over the captured corpus is unmeasured. Step 2 measures and closes the gaps fixture-side, so the wire step proves only what only the wire can prove. |

---

## 2. Grants — exact required content, dormant until issued

Neither grant is assumed, implied, or partially in force. A grant is in force
only when the operator has issued it with at least the content below; Codex
records the grant text verbatim in the progress log before the gated step
runs.

### Grant A — publish v0.17.4

> Authorize publishing, once, non-force: `origin` `main` fast-forward to
> `a7d6c80e7e5ccd963e8ebb46ee054b30af88abb0`, then annotated tag `v0.17.4`
> (object `902d30f046c7e9f493fe3a18eefd5275ca5c5afe`, target
> `f4f2690a442d7a77f1dabb53fb3a120a2c987e97`). No other ref moves.

Reviewer recommendation, for the operator's consideration: **issue it.** The
published-release divergence count is 0, the hosted candidate passed 9/9, and
the same best-practice reasoning that published v0.17.2/v0.17.3 applies — an
unpublished close is carried by an absence observation the lifecycle itself
records as unable to refresh.

### Grant B — SEC EDGAR wire and admission

> Authorize, for the admission of `sec-edgar-usgaap` as the second publisher
> under the `append_only_chained_records_with_wire_evidence_and_operator_approval`
> lifecycle: (1) live wire requests to SEC EDGAR, limited to robots.txt, the
> published access-terms page, and the configured usgaap RSS feed, honoring
> the recorded compliance conditions (declared user agent, rate limits, and
> the terms determination pinned at
> `observations/v0.25/terms-gate/sec-edgar-terms-determination.md`); (2)
> writing and pinning the resulting fresh wire evidence as new dated
> `observation`-grade bytes; and (3) the admission itself, conditional on the
> fresh evidence being compatible with the pinned v0.25 observations —
> incompatibility is a stop-and-report, not a re-determination.

This grant covers the two ask-first items the admission requires (live wire;
observation-grade writes) plus the lifecycle's operator-approval clause, in
one instrument. It does not cover publication of any ref.

---

## 3. Decisions taken

### DR11 — rehearsal before wire, and the wire proves only the wire

Step 2A does not run until Step 2 has enumerated fixture coverage and closed
any fixture-closable gap. The wire evidence then exists to prove exactly the
residue: live reachability, current robots and terms bytes, current feed
bytes, and the fresh-path harvest behavior (`live_harvest: fresh_path_only`).
Every wire claim beyond that residue must instead cite its fixture proof.

### DR12 — drift between fresh and pinned observations is a finding, never a patch

If the fresh robots, terms, or feed shape differs materially from the pinned
v0.25 observations, W1 stops at the comparison: the fresh evidence is still
recorded and pinned (it is a true dated measurement), the admission does not
proceed, and the handoff carries the drift with the re-determination question.
Grant B's clause (3) makes this the operator's stated condition, not
reviewer caution.

### DR13 — disposition, carried

DR9's three clauses govern. Admission enables harvesting an
already-configured source; it adds no route and no serialized field, and the
R15 manifest diff adjudicates clause 2 executably. Expected: **patch
v0.17.5** if any release ships; the reasoning is recorded either way. A
manifest diff showing domain movement is a stop under §4.

### DR14 — the v0.38 close defaults to unpublished-local

As DR10 did: local tag, fresh dated absence observation, publication rides
the handoff. Grant A, if issued, covers v0.17.4 only.

---

## 4. Retained gate and stop conditions

Publishing anything beyond Grant A's refs, and any wire or observation write
beyond Grant B's scope, requires separate exact authorization. Stops:
a grant precondition fails; a published record is measured false; DR12 drift;
any `/v1/*` payload byte or manifest domain moves outside a declared
disposition; an entitlement/licensing outcome, golden input, protected
database, or dependency resolution moves; a boundary or ceiling would move
rather than be selected within.

---

## 5. Codex-owned determinations

### C12 — fixture-coverage enumeration method

Derive the admission checklist from the lifecycle policy's own clauses and
the pinned observation set, then measure which clauses have an executing
fixture witness. Rule: derived, not declared; each gap either gets a fixture
test this cycle or a written entry stating why only the wire can witness it.

### C13 — wire-evidence capture form

Follow the v0.25 observation format exactly (dated, per-artifact files,
pinned `observation`-grade) so compatibility comparison is file-to-file.
Rule: capture is read-only with respect to the pipeline — evidence first,
harvest second; the harvest consumes the live feed through the normal fresh
path, never the evidence files.

### C14 — anything E0 surfaces

Standing latitude for rules; none for unexecuted criteria.

---

## 6. Dependency gates

- Steps P1 and W1 execute only under their grants; otherwise each records a
  dated not-granted observation and the checklist box is checked over that
  observation — a recorded non-execution is the step's truthful completion.
- Step 2 requires E0. Step 2A requires Step 2 and Grant B. Step P1 requires
  only Grant A and may run first if granted.
- R-CLOSE requires all boxes checked (executed or truthfully not-granted) and
  the deferral rows dated.

---

## Declared scope

The standing always-allowed set remains `STATE.md`, this runbook, and
`docs/cycles/PROGRESS-v0.38.md`.

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `release` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
| `allow` | `docs/intel-platform-OPERATIONS.md` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `tools/checklist_audit.py` |
| `allow` | `tools/progress_check.py` |
| `allow` | `tools/domain_manifest.py` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `config/checklist-exemptions.json` |
| `allow` | `config/protected-artifacts.json` |
| `allow` | `config/schedule.json` |
| `allow` | `observations/**` |
| `allow` | `shell/intel_shell/**` |
| `allow` | `shell/tests/**` |
| `allow` | `crates/**/src/**` |
| `allow` | `crates/**/tests/**` |
| `allow` | `apps/**/src/**` |
| `allow` | `repomix.config.json` |
| `allow` | `run` |
| `forbid` | `docs/state-archive/**` |
| `forbid` | `tools/model_profiles.py` |
| `forbid` | `tools/evidence_artifacts.py` |
| `forbid` | `.github/workflows/**` |
| `forbid` | `config/core.json` |
| `forbid` | `config/entities.json` |
| `forbid` | `config/subscriptions*.json` |
| `forbid` | `fixtures/**` |
| `forbid` | `docs/cycles/**` (except this runbook and `PROGRESS-v0.38.md`, by standing precedence) |
| `release_authority` | `Cargo.toml` |
| `release_authority` | `Cargo.lock` |
| `release_authority` | `crates/*/Cargo.toml` |
| `release_authority` | `apps/*/Cargo.toml` |
| `release_authority` | `shell/intel_shell/__init__.py` |
| `release_authority` | `shell/intel_shell/app.py` |
| `release_authority` | `CHANGELOG.md` |
| `release_authority` | `README.md` |

`observations/**` and `config/schedule.json` are allowed **exclusively** for
Step 2A under Grant B — W1 not granted, any diff there is a violation to
report. `config/core.json` stays forbidden: the source is already configured,
and admission must not require editing it; if a measurement says otherwise,
that is a stop-and-report, not a scope widening. `docs/state-archive/**`
returns to forbid — DR8 was a spent grant.

---

## Step P1 · PUBLISH-v0.17.4 — dormant, Grant A

**Objective.** Execute Grant A exactly; bring the records to the published
state truthfully.

If granted: record the grant text; measure preconditions immediately before
the push (`ls-remote` shows `main` at `e068cacc…` and no `v0.17.4`; ancestry
`e068cacc… → a7d6c80e…` proven; local tag object matches); push; record the
push-triggered hosted run; append the five-field post-push record at column
zero; update the status header. Irreversibility per the DR7 precedent: a
failed post-push run is recorded and stopped on, never unwound.

If not granted: one dated not-granted observation; the absence observation
continues to carry the state.

**Acceptance criteria.** Either the published path passes `cycle-check` with
the fresh record and unmodified Step 1A controls, or the not-granted
observation is recorded. **Done when** the records match the remote exactly.

---

## ACTIVATE

Declaration to v0.38; progress skeleton; commit this runbook; retention
advances to v0.37–v0.38 through the derived pattern, disagreement recorded
before either side changes.

**Acceptance criteria.** `cycle-check` resolves v0.38 from the declaration;
retention derives exactly; the boundary is a measurement.

---

## Step 1 · E0 — entering-state reconstruction

Hypotheses from the export review; confirm or refute against real bytes.

| # | Hypothesis | How to settle |
|---|---|---|
| H1 | Object graph: `514bec6c…` → `f4f2690a…` (immediate child) ← tag `902d30f0…`; audit child `a7d6c80e…` immediate child of closing; remote `main` at `e068cacc…`, an ancestor; no remote `v0.17.4` | rev-parse, cat-file, ls-remote, is-ancestor |
| H2 | `STATE.md` 107,454 bytes; archive `STATE-through-v0.35.md` pinned structural 258,658 and byte-matching; two post-push records; three absence observations of which v0.17.4's is current | wc, verify-artifacts, grep counts |
| H3 | Registry 15 rules / 84 controls; exemptions 9; retractions 3; checklist 295/3/286+9; manifest baseline 47,135 bytes / 6 routes / 31 fields at v0.17.4 | run the tools |
| H4 | `sec-edgar-usgaap` configured with `PublisherPermitted` at the real SEC URL; the four v0.25 observation pins verify; `sec_observation_replay.rs` consumes the captured feed through ingest | read config; verify pins; run the test |
| H5 | Which lifecycle-derived admission clauses lack a fixture witness is **unmeasured** — the C12 enumeration is the deliverable, not this row | Step 2 |
| H6 | Whether `config/schedule.json` currently schedules any finance source is unmeasured and decides what W1's harvest enablement touches | read it; record it |
| H7 | Release-parent export 2,674,055; headroom 325,945 / 2.27 cycles; retention now excludes through v0.35 | measure at the activation tree |

Plus standing entering measurements: porcelain (three untracked amendment
inputs exactly), `ci-local`, `invariant-scan --self-test`, both Python
populations, golden — counts.

**Acceptance criteria.** Dated verdicts on every row. **Done when** dependent
steps start from measurements.

---

## Step 2 · REHEARSAL-COMPLETE — fixtures prove everything fixtures can

Per C12 and DR11. Enumerate the derived admission checklist; measure each
clause's executing witness; close every fixture-closable gap (license gate on
`PublisherPermitted`, robots-compliance path against the pinned robots bytes,
dedup identity and license gating over the captured corpus, terms-gate
consumption of the pinned determination — as the derivation, not this list,
dictates); write the wire-residue statement: the clauses only W1 can witness,
each named.

**Acceptance criteria.** The checklist is derived and every clause carries
either a passing fixture witness or a wire-residue entry; new tests follow
the planted-control discipline where a rule is registered;
`invariant-scan --self-test` totals stated; no wire touched.

**Done when** W1's job is exactly the residue and nothing else.

---

## Step 2A · WIRE-ADMISSION — dormant, Grant B

**Objective.** Capture fresh wire evidence, compare against the pinned
observations, and admit `sec-edgar-usgaap` under the lifecycle — or stop at
drift.

If granted, after Step 2: record the grant text; capture robots, terms, and
feed per C13 with the declared user agent and rate discipline; pin the
evidence; compare file-to-file against v0.25 (DR12 governs drift); on
compatibility, enable the scheduled harvest through the fresh path, run the
first live harvest, and append the chained admission record with the wire
evidence and the operator-approval citation (Grant B verbatim); re-run the
full local gate.

If not granted: one dated not-granted observation; the deferral row's trigger
stands unchanged.

**Acceptance criteria.** Either — evidence pinned and verified; comparison
recorded per artifact; admission record chained and append-only; harvest
consumed the live feed, not the evidence files; entitlement and licensing
outcomes measured unchanged for every configured subscription except the
intended finance additions, which are named; manifest diff clean or
disposition-declared; `ci-local` clean — or the not-granted observation.
**Done when** the second publisher is admitted on evidence, or the cycle
truthfully records that it awaits the grant.

---

## Step 3 · RE-MEASURE — hosted, conditional

If production code moved: evidence ref under the standing authority,
`ls-remote` pre-check recorded, run id / attempt / identities reported.
Otherwise the dated reason and the local-only claim list.

---

## Step 4 · R-CLOSE

The established two-commit tagged close, audit child immediate and final,
audit-field criterion evaluated at the audit child, all else at the assembled
closing worktree. Disposition per DR13; if W1 admitted the publisher, the
disposition reason names the harvest enablement as the behavior movement.
Per DR14 the close is unpublished-local with a fresh absence observation, and
post-close `cycle-check` passes on the mixed state with Step 1A controls
unmodified. All standing criteria: version-check counts, non-zero v0.38
checklist line, governed export row, dated deferral rows, self-test totals,
golden, zero hand-typed finding lines, no publication beyond Grant A.

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

The supplied short table omitted trigger-bearing subjects from the immediately
prior runbook, lacked the governed byte authorities, and did not assign actions
to named steps. ACTIVATE restores the derived carry-forward population before
any semantic result is claimed; later steps replace these activation-time
observations with the latest measurements available at close.

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.38 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | v0.38 · 2026-08-04 — ACTIVATE observed no second concurrent harvester; Step 2A remains a single bounded SEC harvest and the trigger has not fired. | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.38 · 2026-08-04 — Before W1, no v0.38 publisher request or transient robots outage has occurred and no Decision B authorization was issued; the trigger has not fired. | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.38 · 2026-08-04 — Grant B and scope permit only W1's bounded path, but no v0.38 live 304 has been observed; the combined trigger has not fired. | none |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.38 · 2026-08-04 — The source path is in scope, but ACTIVATE performed no connector mapping review or mapping change; the combined trigger has not fired. | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.38 · 2026-08-04 — ACTIVATE added no origin and observed no concurrency; W1 is bounded to SEC only, so the trigger has not fired. | none |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | v0.38 · 2026-08-04 — Grant B authorizes W1's bounded admission harvest but no recurring scheduled window has executed yet. | **Step 2A** |
| Postgres / pgvector / multi-host seam | unchanged | v0.38 · 2026-08-04 — ACTIVATE introduced no Postgres, pgvector, or multi-host seam; the unchanged trigger has not fired. | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.38 · 2026-08-04 — ACTIVATE observed no third-party shell or replacement-shell HC1 claim; the trigger has not fired. | none |
| L2 forced-command wrapper | an operator server session | v0.38 · 2026-08-04 — No operator server session occurred during ACTIVATE; the trigger has not fired. | none |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.38 · 2026-08-04 — ACTIVATE added no production vocabulary spelling; E0 owns the fresh registered scan. | none |
| `--features net` Rust 1.86 execution | a scoped cycle authorized to change evidence topology and an executable local or hosted lane that actually pins and runs the net path on Rust 1.86 | v0.38 · 2026-08-04 — P1 hosted run 30841505130 passed the existing Rust 1.86 lane; workflow/evidence topology remains scope-forbidden, so the combined trigger has not fired. | none |
| GitHub attestation verifier version admission | the installed or proposed `gh attestation verify` version differs from the exact repository pin, or its accepted bundle/workflow contract changes | v0.38 · 2026-08-04 — ACTIVATE changed no verifier pin or accepted bundle/workflow contract; the trigger has not fired. | none |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.38 · 2026-08-04 — W1 concerns the already-configured second publisher; no third-publisher review or admission occurred. | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.38 · 2026-08-04 — Grant A moved only `main` and v0.17.4; no historical tag was authorized or moved. | none |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.38 · 2026-08-04 — Both historical tags remain outside Grant A and the hosted flag is unchanged; the combined trigger has not fired. | none |
| Manifest retention/indexing | the manifest reaches its governed artifact byte boundary, or two consecutive clean `./run verify-artifacts` runs each take ≥1.00 s real | v0.38 · 2026-08-04 — ACTIVATE leaves the manifest at the entering 193,830 / 1,048,576-byte measurement; W1 owns fresh pin and timing measurements. | none |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.38 · 2026-08-04 — The broad trigger fires because shell source is in declared scope; any release-authority movement is confined to R-CLOSE. | **Step 4** |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.38 · 2026-08-04 — R15 remains the executable public-domain subcase; R-CLOSE owns the remaining heterogeneous classification adjudication. | **Step 4** |
| Second `STATE.md` archival | the export ceiling trigger fires, or `STATE.md` reaches its governed artifact byte boundary | v0.38 · 2026-08-04 — Entering State is 107,454 / 453,741 bytes and the entering governed export is 2,674,055 / 3,000,000 bytes; neither boundary trigger fired. | none |
| Retention derivation across a version-family boundary | an active cycle whose name is not of the form `v0.<n>` — raising at `v1.0`–`v1.2`, silently under-excluding from `v1.3` onward | v0.38 · 2026-08-04 — The active cycle remains in the `v0.<n>` family; the trigger has not fired. | none |
| Published-release divergence | the unpublished distance contains a measured runtime behaviour difference persisting across three consecutive closed cycles within the current publication epoch, or acquires any public-surface change | v0.38 · 2026-08-04 — Grant A published exact v0.17.4 closing commit `f4f2690a442d7a77f1dabb53fb3a120a2c987e97`, resetting the new publication epoch count to 0 there. W1 and R-CLOSE own the later runtime/public-surface classification. | **Step 4** |
| MSRV current-restatement membership | a current restatement of either Rust floor lands outside the registry without failing a check | v0.38 · 2026-08-04 — ACTIVATE changed no Rust-floor restatement; E0 owns the fresh `version-check` result. | none |
| Retention arithmetic fallback | the retention formatter again permits an omitted retained set, or any live production or fixture caller supplies a set not derived by `expected_retained_cycle_paths` for that root | v0.38 · 2026-08-04 — ACTIVATE derives exactly the v0.37–v0.38 retained set and supplies it explicitly; no omitted or non-derived set appeared. | none |
| Optional cycle-ending audit disclosure | a closed cycle whose delivered export differs from its governed figure and which records no cycle-ending audit field | v0.38 · 2026-08-04 — The cycle remains open; R-CLOSE reserves its immediate audit child as the first point where the tagged closing tree can be measured. | **Step 4 audit child** |
| SEC EDGAR admission | the three v0.25 determinations closed | v0.38 · 2026-08-04 — The trigger is satisfied and Grant B is issued; admission remains conditional on W1's fresh compatible wire evidence. | **Step 2A** |
| License enum semantics | a second publisher requires an inexpressible license value | v0.38 · 2026-08-04 — `PublisherPermitted` already expresses SEC's configured case; W1 re-measures the actual admitted outcome. | **Step 2A** |
| Terms-level automated-access gate | a candidate's terms restrict beyond robots.txt | v0.38 · 2026-08-04 — Grant B requires a fresh terms capture and compatibility comparison before admission; no v0.38 terms byte has yet been fetched. | **Step 2A** |
| Feed shape observation | an uncovered publisher feed shape | v0.38 · 2026-08-04 — Grant B requires a fresh feed capture and comparison before admission; no v0.38 feed byte has yet been fetched. | **Step 2A** |
| Threshold-authority limitation | a common dependency module or manifest edge appears between store and view | v0.38 · 2026-08-04 — The shared `assign_dedup_identity` seam remains completed under R14; ACTIVATE added no dependency module or manifest edge. | none |
| ARCHITECTURE.md §8 / AGENTS.md R-CLOSE tag-mechanics duplication | the restatements diverge | v0.38 · 2026-08-04 — ACTIVATE leaves both tag-mechanics restatements unchanged; no divergence is observed. | none |
| Review-export capacity | the export crosses the declared ceiling | v0.38 · 2026-08-04 — The entering governed release-parent figure is 2,674,055 bytes, leaving 325,945 bytes / 10.86% / 2.27 cycles at +143,456 bytes/cycle; ACTIVATE owns the fresh export measurement. | none |
| Public value-domain control (G6) | a `/v1/*` field's domain changes undetected | v0.38 · 2026-08-04 — R15 remains registered; Step 1 must execute its planted added-enum, removed-field, and changed-type controls once more before this row retires. | **Step 1** |

---

## Standing prohibitions

The full v0.37 set carries forward unchanged, plus: no wire request of any
kind outside W1-under-Grant-B; no observation write outside C13's capture;
Grants A and B are spent on execution and are not precedents; a not-granted
milestone is completed by its observation, never by a workaround.

---

## Cycle checklist

- [x] PUBLISH-V17-4
- [x] ACTIVATE
- [ ] E0
- [ ] REHEARSAL-COMPLETE
- [ ] WIRE-ADMISSION
- [ ] RE-MEASURE
- [ ] R-CLOSE

*Box ids match the `PROGRESS-v0.38.md` entry ids exactly.*

---

## Handoff

Each DR and grant outcome (executed, or not-granted with its observation);
the C12 checklist with its wire-residue statement; the DR12 comparison per
artifact if W1 ran; every stop or an explicit none; headroom; the v0.39
findings list — findings, not criteria. Then whichever operator questions
remain open: v0.17.4 or v0.17.5 publication, and the admission grant if it
was not issued this cycle.

---

## Provenance

**Measured on the delivered post-v0.37 export (2,690,027 bytes / 158
files):** the STATE.md header and figures (two post-push records, three
absence observations, 107,454 bytes); both archive pins including
`STATE-through-v0.35.md` at 258,658 structural; 15 rules / 84 controls with
R15 present; nine exemptions; `domain_manifest.py` and the 47,135-byte
v0.17.4 baseline recorded in STATE.md; the `AlreadyExists` retry in
`sec_identity_measure.rs`; retention excluding through v0.35; the deferred
table's headroom row (2,674,055 / 325,945 / 2.27 cycles); the finance source
configuration (`sec-edgar-usgaap`, `PublisherPermitted`, `sec.gov` URL); the
four pinned v0.25 SEC observations; and `sec_observation_replay.rs`
consuming the captured feed. **Not measurable from the export:** everything
requiring `.git` or the network — hence H1, and the grant preconditions
re-measured at execution time. **Not done:** no repository command, no wire
request, no push.
