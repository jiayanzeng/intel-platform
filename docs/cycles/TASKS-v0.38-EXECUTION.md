# TASKS-v0.38-EXECUTION.md — the admission cycle

## Runbook amendments

Step 3 — exact hosted candidate, ref, signed-receipt, identity, population-equivalence, and remote readback result appended; acceptance meaning unchanged — 2026-08-04

Step 2A — Grant-B wire, DR12, fresh-archive, entitlement, and admission result appended; exact deferred-auditor and export-checker scopes added after their two-archive/one-RSS assumptions failed on the valid third admission and second RSS pin; acceptance meaning unchanged — 2026-08-04

Step 2 — derived rehearsal checklist and wire-residue record appended; acceptance meaning unchanged — 2026-08-04

Step 1 — dated E0 verdict table and discharged G6 completion appended; acceptance meaning unchanged — 2026-08-04

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
| `allow` | `tools/audit_deferred.py` |
| `allow` | `tools/export_check.py` |
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

**E0 verdicts (measured 2026-08-04).**

| # | Verdict | Measured result |
|---|---|---|
| H1 | **confirmed for the local graph; publication superseded the remote hypothesis** | Release parent `514bec6c…` has parent `11cad3c…`; closing `f4f2690a…` has immediate parent `514bec6c…`; audit child `a7d6c80e…` has immediate parent `f4f2690a…`; annotated object `902d30f0…` peels to `f4f2690a…`; and `e068cacc…` is an ancestor of the audit child. Immediately before P1, remote `main=e068cacc…` and v0.17.4 was absent. Fresh E0 readback after the authorized publication is `main=a7d6c80e…`, tag object `902d30f0…`, peeled target `f4f2690a…`. |
| H2 | **archive confirmed; live counts refuted after P1** | Before this E0 record, State is **110,556** bytes, not 107,454. `STATE-through-v0.35.md` is exact **258,658** bytes at SHA-256 `fb1114f6…` and matches its structural pin. There are **3** post-push records, not 2, plus the same **3** historical unpublished-local observations; v0.17.4's absence record is historical because the complete post-push record now takes precedence. The manifest is **193,830** bytes and complete verification matches **2 artifacts / 333 pins**. |
| H3 | **partly confirmed; unit corrected** | The registered suite is **15 rules / 84 planted controls**, checklist exemptions are **9**, retractions are **3**, and the pre-E0 checklist is **297 checked / 288 matched / 288 resolved / 9 exemptions**, not 295/286+9. The v0.17.4 manifest is exact **47,135** bytes over **6 routes / 31 status-media response variants / 112 recursive field occurrences**; `domain_manifest.py check` passes. |
| H4 | **confirmed** | `config/core.json` names exact source `sec-edgar-usgaap`, real RSS URL `https://www.sec.gov/Archives/edgar/usgaap.rss.xml`, `PublisherPermitted`, and `robots_on_missing=deny`. The four substantive v0.25 observation pins (plus their directory `.gitattributes`) match. Focused replay passes **3/3** and consumes the captured RSS through the shipped parser. |
| H5 | **confirmed as deliberately unmeasured** | E0 does not promote fixture evidence into wire evidence or predeclare the derived checklist. Step 2 remains the sole owner of the lifecycle-clause enumeration and its fixture/wire partition. |
| H6 | **refuted** | `config/schedule.json` already schedules both finance sources for `quant-desk`: `filings-digest=7200` and `sec-edgar-usgaap=600`. Step 2A therefore must not edit the schedule merely to "enable" SEC; its bounded action is the existing scheduled source through the normal fresh path plus the append-only admission record. |
| H7 | **refuted by the activation-tree measurement** | The exact activation commit exports at **2,596,652 bytes / 158 files / 2 retained cycles**, leaving **403,348 bytes / 13.44% / 2.81 cycles** at +143,456 bytes/cycle. Retention excludes through v0.36 and retains exactly v0.37–v0.38, not an excludes-through-v0.35 boundary. |

Standing reconstruction also passed: the entering porcelain named exactly the
three historical untracked amendment inputs; full permission-complete
`ci-local` passed **22/22** identities; its registered mutation scan passed
**15/15 rules / 84 controls**; Python 3.11 and 3.12 each passed the identical
**370/370** collected population with no skips; Rust 1.78 offline and Rust
1.86 net succeeded while Rust 1.85 refused the declared locked ICU floor;
focused SEC replay passed **3/3**; and golden passed **11/11**. No E0 stop
condition fired.

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

**REHEARSAL-COMPLETE result (measured 2026-08-04).** The checklist below is
derived from the protected-artifact lifecycle, the configured source and
schedule, HC1/HC2/HC8/HC13, and the robots/redirect/dedup invariants. It is not
an inference from a green replay alone. Every fixture-side clause now has an
executing witness; the two new semantic guards also carry mutations that make
the target construction fail.

| Derived lifecycle clause | Executing fixture witness | Residue reserved to W1 |
|---|---|---|
| Evidence lifecycle and fresh target | `test_cmd_harvest_sec_is_fresh_bounded_and_consumes_no_observation_file` proves artifact preflight precedes startup, the default path is fresh, protected targets are refused, only `finance/sec-edgar-usgaap` is posted, cleanup is deterministic, and no observation file can feed the harvest. Its planted missing-preflight and wrong-source mutations fail. | Execute that path against one newly named database and record its actual lifecycle and database facts. |
| Source, license, missing-policy, and cadence configuration | Config validation plus `test_admitted_sec_source_has_an_explicit_resolvable_cadence` and its architecture-mismatch test bind the real SEC RSS URL, `PublisherPermitted`, `robots_on_missing=deny`, and the existing 600-second schedule. | Report the source selected by the live request. No schedule edit or recurring scheduler run is authorized. |
| Declared identity and terms gate | Cored's contact-before-bind validation and both live clients' exact/mismatched User-Agent tests cover construction. The pinned terms determination is now exact-byte checked and semantically consumed; affirmative compatibility, all three reviewed SEC pages, monitored contact, and operator responsibility are required, and a planted `Undetermined` mutation fails. | Re-fetch the published access terms and use the actual monitored-contact identity on the outbound request; fixtures cannot prove either current page content or the wire-visible header. |
| Publisher robots plus operator deny-list | The pinned robots body is exact-byte replayed through production `RobotsGate`: the configured RSS path is allowed, `/Archives/bin` is denied, the operator gate composes, missing/typo policy denies, and a planted target-path `Disallow` mutation fails. The compliance suite exercises precedence, normalization, missing-policy, redirect re-gating, cache, and limiter controls. | Capture the current robots response and record the production live verdict and effective delay. |
| Redirect, query, and rate behavior | Net ingest tests exercise disabled automatic redirects, full re-gating, hop bounds, same-origin/allow-list handling, and limiter timing; cored tests bind the target request to the configured source. | Record actual status/`Location` behavior, request count, ordering, timing, and absence of retry/automatic redirect on this bounded run. |
| Feed shape and production parser | The 892,641-byte v0.25 RSS pin is exact; `sec_observation_replay` runs it through the shipped parser as 200 SEC documents with the configured source/license and measured content/timestamp premises. | Capture the current RSS response, compare its shape under DR12, and have the harvest consume that live response rather than any evidence file. |
| Non-paged latest-window coverage | Replay proves GUID uniqueness, ordering/timestamp ties, and overlap premises; cored harvest tests cover first-window, overlap, boundary, and gap outcomes. | Measure the current archive result as `first_window`; no repeated fetch or historical backfill is authorized. |
| Persistence, global-within-sector dedup, and retrieval license | `measures_shipped_identity_on_parser_produced_sec_documents` persists the parser-produced corpus, measures 201 input / 201 kept / 0 dropped, proves identity equivalence, and now retrieves the SEC hit in finance with `PublisherPermitted` and a snippet while a disjoint sector is empty. The license-compatibility negative test still maps unknown licenses to `IndexOnly`. | Measure the fresh database's document counts, integrity, null simhash/canonical counts, dedup outcome, and stored license. |
| Entitlement and core SQL isolation | Cored source/sector filters and shell subscription tests prove shell entitlement plus core SQL filtering; the bounded harness cannot post any non-SEC sector/source. | Re-measure every configured subscription and name only the intended finance additions, if any. |
| Observation pins and DR12 comparison | Artifact validation proves exact hashes/bytes, rejects one-byte changes, and keeps `pinned_files[]` disjoint from admission chains. | Pin each newly captured dated observation and record the per-artifact v0.25 comparison; material drift stops admission. |
| Append-only database admission | The artifact suite rejects changed hashes without a new admission, missing wire/approval fields, bad `prior_sha256`, incomplete chains, and `admission` under `pinned_files[]`; its complete chained fixture verifies. | If and only if DR12 passes, append the fresh database's exact hash/bytes/corpus facts with wire references and Grant B approval, then run both artifact entry points. |
| Recurrence and concurrency bounds | Scheduler fixtures prove the configured cadence, while the new harness is deliberately single-source and one-shot. | None: a recurring scheduled run, a second concurrent harvester, conditional GET/304, and repeated fetch behavior remain deferred and are not claims of W1. |

The irreducible wire residue is therefore exact and narrow: current SEC robots,
terms, and RSS bytes/status/shape; the real outbound declared identity; actual
request ordering, redirect behavior, counts, and rate timing; the production
parser consuming the live RSS response; the fresh database's harvest,
integrity, identity, license, and entitlement facts; and the append-only
admission record bound to those bytes and Grant B. A fixture cannot establish
any of those current external facts. Conversely, W1 is not evidence for a
recurring scheduler run, concurrency, a 304 path, historical backfill, or a
second fetch. No publisher request was made during this step. Fresh focused
measurements pass SEC replay **4/4**, SEC store identity **3/3**, compliance
**40/40**, shell harvest/config/scheduler **14/14**, artifact fixtures **21/21**,
and net ingest **29/29**; the registered invariant scan remains **15/15 rules /
84 controls**.

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

**WIRE-ADMISSION result (measured 2026-08-04).** Grant B's evidence capture
ran before the harvest and made one sequential, no-redirect, no-retry request
each for SEC robots, published access terms, and the configured US GAAP RSS
feed. All three returned HTTP 200. Fresh robots are byte-identical to v0.25;
the current terms preserve every material condition in the pinned affirmative
determination; and the changing current feed preserves the measured 200-item
parser-facing shape. The per-artifact comparison records DR12 **compatible**.

The separate production `./run harvest-sec` invocation consumed the live
configured URL through the normal net parser into fresh
`data/live-20260803T195324Z-37051.db`; no observation file was a harvest input.
It measured `first_window`, **200 fetched / 200 new / 200 stored**, live robots
`Body(allow)` for the exact RSS path, a **0.500-second** effective delay, and
clean shutdown. The **253,952-byte** archive at SHA-256
`fb1046b79e7501d51e2dde3fd89fb7dfe0094defa6205b12afb39a21dff06044`
passes integrity with **200** `finance/sec-edgar-usgaap/PublisherPermitted`
rows, zero null SimHashes or canonical ids, zero noncanonical rows, **200**
distinct canonical identities, and zero cursors.

The actual public shell/core boundary re-measured both configured
subscriptions. `acme-research` (`science,technology`) analyzed **0** documents;
`quant-desk` (`finance`) analyzed **200**, with zero near-duplicate collapses.
The only intended entitlement movement is therefore the named **200-document
finance addition for `quant-desk`**; no subscription configuration or public
response domain changed. The archive is admitted by a non-retroactive initial
`artifacts[]` record whose wire references and operator-approval citation bind
Grant B. The five capture files and the dated admission report are exact
`observation`-grade pins. Both artifact entry points accept **3 artifacts /
339 pinned files**; the manifest is **200,440 / 1,048,576 bytes**, and two
complete checks take **0.09 s / 0.09 s real**. A recurring scheduler run,
concurrency, conditional GET/304, repeated fetch, and backfill remain
unmeasured and unclaimed.

The first full-gate attempt exposed an author-side scope defect: the on-site
deferred auditor selected every `artifacts[]` record and asserted that the
manifest contained exactly the two historical cosine inputs, so the valid
third admission failed before either named input was measured. Step 2A's
simultaneous admission-and-clean-`ci-local` criterion necessarily contains the
exact `tools/audit_deferred.py` correction; the declared scope now says so
explicitly. The correction selects `data/core.db` and `data/live-smoke.db` by
their stable manifest paths and leaves additional admitted archives outside
that historical measurement. A regression test plants the SEC-shaped third
record and requires the same two-input selection. No evidence disposition,
committed receipt, protected byte, or acceptance meaning changes.

The first project-root export attempt then exposed the analogous one-capture
assumption in `tools/export_check.py`: it required exactly one SEC RSS body
beneath `observations/**`, so the required second pinned capture stopped
inspection before the export was measured. Step 2A's evidence-pin and bounded
review-export criteria necessarily contain this second author-contract
correction, and the exact declared scope now names the checker. The Repomix
registry names both historical paths explicitly; the checker derives those
exact configured paths, rejects a wildcard, missing byte, or non-observation
path, and requires every one to remain absent from the export. A regression
plants two exact captures and removes one to prove the guard can fail. The
permission-complete project-root entry point then passes at **2,766,436 bytes /
163 files / 2 retained cycles**, leaving **233,564 bytes / 7.79% / 1.63
cycles** at +143,456 bytes/cycle. No source, record, or comparison result is
excluded; only the two separately pinned raw RSS bodies stay outside the
bounded review artifact.

The permission-complete corrected full gate passes **22/22** identities,
including registered scan **15/15 rules / 84 controls**, Python 3.11
**373/373**, both Rust floors and warning gates, artifact verification, and
golden **11/11** with zero delta. The separate permission-complete Python 3.12
lane passes the identical **373/373** population with no skips. The first
370-pass/1-fail attempt is retained as the finding that caused the scoped
correction; it is not acceptance evidence.

---

## Step 3 · RE-MEASURE — hosted, conditional

If production code moved: evidence ref under the standing authority,
`ls-remote` pre-check recorded, run id / attempt / identities reported.
Otherwise the dated reason and the local-only claim list.

**RE-MEASURE result (measured 2026-08-04).** The operational `run` path and
executable controls moved, so hosted verification ran. Exact audited candidate
`816a0648c0dd9f4be1caad01ed3395997671cf25` first passed the complete
permission-capable local matrix at **22/22** jobs, including Python 3.11
**373/373**, registered scan **15/15 rules / 84 controls**, both Rust floors,
artifact verification, and golden **11/11**. The separate local Python 3.12
lane passed the identical **373/373** population.

Immediately before ref creation, `git ls-remote --exit-code` returned **2**
with no output for fresh
`refs/heads/codex/v0.38-evidence-816a064`. An initial push command supplied an
incorrect guessed full SHA behind that correct short id; local and remote
reported `bad object` / `remote unpack failed`, no ref was created, and a fresh
`ls-remote` again returned **2** with no output. After resolving the candidate
with `git rev-parse`, one non-force push created exactly the named ref at the
exact candidate. This rejected bad-object attempt is a remote non-result, not a
second ref creation or force/retry of an existing ref.

Workflow-dispatch run **30852480662**, attempt **1**, completed `success` on
that exact SHA/ref. All **9/9** blocking identities passed and persisted **9
receipts / 9 Sigstore bundles**; dependency drift was the sole report-only
skip. The run was dispatched once and not retried. Both hosted shell lanes
collected **373**, passed **372**, and skipped only named
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
with its `on_site` marker and declared protected-corpora/built-core reason.
Both direct `tools/test_population.py` comparisons derived
`equivalent=true`, `equivalent_passed=373`, and one allowed hosted skip. Hosted
golden passed **11/11**.

Final readback kept the evidence ref exact, remote `main` at `a7d6c80e…`, and
v0.17.2/v0.17.3/v0.17.4 annotated objects at their unchanged values. No tag,
publication ref, dependency, workflow byte, protected byte, publisher wire,
entitlement/license outcome, or public response domain moved.

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

**R-CLOSE result (measured 2026-08-04).** DR13 selects patch **v0.17.5**.
SEC admission enables bounded harvesting of an already-configured source and
adds the intended 200-document finance result for `quant-desk`; the exact
release-baselined source derivation and installed runtime comparison each pass
with **0 differences** across **6 routes / 31 status-media response variants /
112 recursive field occurrences**. No route, response field, field type,
serialized `/v1/*` field-domain value, subscription configuration, or license
enum moves, so the minor clause does not fire.

Untagged release parent `37f552c0c326098bdcf8f19de7eac19670d74680`
moves only the five executable 0.17.5 authorities, README's three current
restatements, cored's lockfile package value, and release-preparation records.
Its complete local gate passes **22/22** jobs: Python 3.11 and 3.12 each pass
**373/373**, registered scan passes **15/15 rules / 84 controls**, both Rust
floors and warning gates pass, all **3 artifacts / 339 pins** match, and golden
passes **11/11**. Exact hosted candidate
`816a0648c0dd9f4be1caad01ed3395997671cf25` and run **30852480662**,
attempt 1, already passed **9/9** blocking identities with **9 receipts / 9
Sigstore bundles**.

The exact release-parent export passes at **2,781,281 bytes / 163 files / 2
retained cycles**, retaining v0.37–v0.38 and excluding both protected raw RSS
bodies and all structural archives. It leaves **218,719 bytes / 7.29% / 2.04
cycles** at the latest positive +107,226-byte adjacent-cycle denominator. The
manifest remains **200,440 / 1,048,576 bytes**. DR14 remains local-only:
direct pre-close checks found no local or remote v0.17.5 tag, and remote `main`
remained exact published v0.17.4 audit child `a7d6c80e…`. No push or remote ref
movement beyond spent Grant A occurred.

The immediate child of that release parent carries this checked closing
record and becomes the target of a local annotated v0.17.5 tag only after it
exists. Its immediate audit child measures the closing-tree export, appends the
required non-governing audit field, re-runs the full local gate on the delivered
head, and is the final v0.38 commit.

---

## Cycle closing record

- **Cycle closed:** 2026-08-04
- **Release disposition:** release (as of 2026-08-04)
- **Release:** `v0.17.5`
- **Release commit:** `37f552c0c326098bdcf8f19de7eac19670d74680`
- **Evidence candidate:** `816a0648c0dd9f4be1caad01ed3395997671cf25`
- **Candidate hosted run:** `30852480662` attempt 1
- **Disposition reason:** SEC admission enables bounded harvesting of an
  already-configured source and adds the intended finance corpus. The public
  domain manifest reports **0 differences** across **6 routes / 31
  status-media variants / 112 field occurrences**. No route, response field,
  field type, or serialized `/v1/*` value-domain value moves, so DR13 selects
  patch **v0.17.5** while naming the operational behavior movement.
- **Release identity:** `version-check` derives 0.17.5 from all five executable
  authorities and reports **3** offline-MSRV pins, **22** current offline-MSRV
  restatements, and **3** current release restatements. The release parent is
  untagged and is this closing record's immediate parent. This tree contains no
  annotated-tag-object field; the local annotated tag targets this closing
  commit only after it exists.
- **Anchored evidence:** exact candidate `816a0648…` and run 30852480662
  passed **9/9** blocking identities and persisted **9 receipts / 9 Sigstore
  bundles**. Both local release-parent lanes pass **373/373**; both hosted
  populations derive equivalent **373**-test results with one named, reasoned,
  `on_site` skip; hosted and local golden pass **11/11**.
- **Governed export:** exact release parent
  `37f552c0c326098bdcf8f19de7eac19670d74680` produced **104 derived / 7
  required / 163 exported / 2,781,281 bytes / 2 retained cycles**, retaining
  v0.37–v0.38 and excluding both protected raw RSS bodies and all structural
  archives. At +107,226 bytes/cycle, **218,719 bytes / 7.29% / 2.04 cycles**
  remain below the fixed ceiling.
- **Artifact boundaries:** the assembled closing State is **129,970 / 453,741
  bytes**. The manifest is **200,440 / 1,048,576 bytes** and both complete
  verification runs remain below the 1.00-second trigger. Neither boundary
  trigger fires.
- **Deferral disposition:** every active row carries its latest dated v0.38
  observation. G6 and SEC admission are completed rather than deferred. The
  release-parent self-test passes **15/15 rules / 84 controls** with **0**
  hand-typed absolute finding-line fields.
- **Divergence disposition:** publication of v0.17.4 reset the epoch count to
  **0**. v0.38 is the first subsequent closed cycle with a measured runtime-
  behavior difference, so the consecutive count becomes **1**. No public-
  surface change occurs; neither the three-cycle nor immediate trigger fires.
  An unpublished local close does not reset the epoch.
- **Scope reconciliation:** release authority changed only `Cargo.lock`,
  `apps/cored/Cargo.toml`, both shell version literals, `CHANGELOG.md`,
  `README.md`, and the State version header. Active State/runbook/progress and
  Architecture records carry the close. No dependency graph, protected byte,
  fixture, observation, closed-cycle document, publisher request, workflow, or
  unauthorized remote ref moved during R-CLOSE.
- **Publication boundary:** direct pre-close readback found no local or remote
  `refs/tags/v0.17.5` entry, while remote `main` remained exact
  `a7d6c80e7e5ccd963e8ebb46ee054b30af88abb0`. No push, `main` movement, or
  tag publication is authorized or performed. The annotated tag is local-only;
  the immediate next commit records the measured closing-tree export.
- **Checklist reconciliation:** the assembled closing worktree passes at
  **302 checked / 3 retracted / 293 matched / 293 commits resolved / 9
  exemptions**, with v0.38 itself nonempty at **7 checked / 7 matched / 7
  resolved**.
- **Golden reconciliation:** the release-parent full gate and standalone run
  pass **11/11**, delta **0**. The assembled closing-worktree standalone run
  and final audit-child full gate re-execute the same anchor.

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
| T7 robots single-flight | a second concurrent harvester | v0.38 · 2026-08-04 — W1 ran exactly one bounded SEC harvester; R-CLOSE ran no harvester and observed no second concurrent process through cycle end, so the trigger did not fire. | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.38 · 2026-08-04 — Fresh SEC robots returned HTTP 200 and the live production cache reported `Body(allow)`; no transient outage or Decision B authorization occurred, so the combined trigger has not fired. | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.38 · 2026-08-04 — W1's fresh feed capture returned HTTP 200 and the production ingest reported `first_window`; no live 304 was observed, so the combined trigger has not fired. | none |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.38 · 2026-08-04 — The source path was in scope, but no connector mapping review or mapping change occurred through R-CLOSE; the combined trigger did not fire. | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.38 · 2026-08-04 — W1 ran only the already-configured SEC source in one process; no further origin or concurrent harvester appeared, so the trigger has not fired. | none |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | v0.38 · 2026-08-04 — Grant B discharged one manual admission harvest only. No bounded recurring-window authorization was issued and no scheduled run executed through R-CLOSE; the trigger remains deferred. | none |
| Postgres / pgvector / multi-host seam | unchanged | v0.38 · 2026-08-04 — The release-parent full gate and R-CLOSE introduced no Postgres, pgvector, or multi-host seam; the unchanged trigger did not fire. | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.38 · 2026-08-04 — No third-party shell or replacement-shell HC1 claim appeared through R-CLOSE; the trigger did not fire. | none |
| L2 forced-command wrapper | an operator server session | v0.38 · 2026-08-04 — No operator server session occurred through R-CLOSE; the trigger did not fire. | none |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.38 · 2026-08-04 — The release-parent registered scan and all planted mutations pass **15/15 rules / 84 controls**; no outside vocabulary spelling was found. | none |
| `--features net` Rust 1.86 execution | a scoped cycle authorized to change evidence topology and an executable local or hosted lane that actually pins and runs the net path on Rust 1.86 | v0.38 · 2026-08-04 — Hosted run 30852480662 and the release-parent full gate most recently passed the pinned Rust 1.86 lane; workflow/evidence topology remained scope-forbidden, so the combined trigger did not fire. | none |
| GitHub attestation verifier version admission | the installed or proposed `gh attestation verify` version differs from the exact repository pin, or its accepted bundle/workflow contract changes | v0.38 · 2026-08-04 — R-CLOSE changed no verifier pin or accepted bundle/workflow contract; the trigger did not fire. | none |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.38 · 2026-08-04 — W1 admitted only the already-configured second publisher; no third-publisher review or admission occurred through R-CLOSE. | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.38 · 2026-08-04 — Step 3's final remote readback and R-CLOSE show no historical-tag movement; both names remained outside Grant A and no authorization was issued. | none |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.38 · 2026-08-04 — Both historical tags remain unpublished and the hosted flag remains unchanged through R-CLOSE; the combined trigger did not fire. | none |
| Manifest retention/indexing | the manifest reaches its governed artifact byte boundary, or two consecutive clean `./run verify-artifacts` runs each take ≥1.00 s real | v0.38 · 2026-08-04 — R-CLOSE measures **200,440 / 1,048,576 bytes** after admission; the latest timed pair remains W1's two complete verifications of **3 artifacts / 339 pinned files** at **0.09 s / 0.09 s real**. The release-parent gate re-matched every byte, so neither trigger clause fires. | none |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.38 · 2026-08-04 — The broad trigger fired and Step 4 moved all five executable release authorities coherently to 0.17.5; `version-check` passes. | **Step 4 completed 2026-08-04** |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.38 · 2026-08-04 — R15 executably reports zero public-domain movement; R-CLOSE adjudicated the remaining heterogeneous criteria and selected patch v0.17.5 while naming the SEC harvest-enablement behavior movement. No broader operator decision displaced that boundary. | **Step 4 completed 2026-08-04** |
| Second `STATE.md` archival | the export ceiling trigger fires, or `STATE.md` reaches its governed artifact byte boundary | v0.38 · 2026-08-04 — R-CLOSE measures the assembled State at **129,970 / 453,741 bytes** and exact release-parent export at **2,781,281 / 3,000,000 bytes**; neither boundary trigger fired. | none |
| Retention derivation across a version-family boundary | an active cycle whose name is not of the form `v0.<n>` — raising at `v1.0`–`v1.2`, silently under-excluding from `v1.3` onward | v0.38 · 2026-08-04 — The closing active cycle remains in the `v0.<n>` family; the trigger did not fire. | none |
| Published-release divergence | the unpublished distance contains a measured runtime behaviour difference persisting across three consecutive closed cycles within the current publication epoch, or acquires any public-surface change | v0.38 · 2026-08-04 — Publication of v0.17.4 reset the count to **0**. v0.38 is the first subsequent closed cycle with a measured runtime-behavior difference, so the count becomes **1**; R15 reports zero public-domain differences, so neither the three-cycle nor public-surface trigger fires. | **Step 4 completed 2026-08-04** |
| MSRV current-restatement membership | a current restatement of either Rust floor lands outside the registry without failing a check | v0.38 · 2026-08-04 — R-CLOSE `version-check` derives **3** executable offline pins at 1.78, **22** offline-floor current restatements, and **3** release-version restatements at 0.17.5; all **585** tracked files remain classified. | none |
| Retention arithmetic fallback | the retention formatter again permits an omitted retained set, or any live production or fixture caller supplies a set not derived by `expected_retained_cycle_paths` for that root | v0.38 · 2026-08-04 — Exact release-parent `export-check` derived and retained only v0.37–v0.38; no omitted or non-derived retained set appeared. | none |
| Optional cycle-ending audit disclosure | a closed cycle whose delivered export differs from its governed figure and which records no cycle-ending audit field | v0.38 · 2026-08-04 — R-CLOSE binds the **2,781,281-byte** release-parent governed field and reserves the required immediate audit child. The closing-tree measurement and audit field are evaluated there, the first point at which the tagged closing tree exists; no post-handoff omission is permitted. | **Step 4 audit child** |
| License enum semantics | a second publisher requires an inexpressible license value | v0.38 · 2026-08-04 — The admitted live archive stores all **200/200** rows as existing `PublisherPermitted`; finance-only public-shell isolation is unchanged and no inexpressible value appeared, so the trigger has not fired. | none |
| Terms-level automated-access gate | a candidate's terms restrict beyond robots.txt | v0.38 · 2026-08-04 — The fresh terms page preserves the pinned determination's user-agent/contact, rate, responsibility, and public-information reuse conditions; DR12 passed without re-determination and no uncovered restriction appeared. | none |
| Feed shape observation | an uncovered publisher feed shape | v0.38 · 2026-08-04 — Fresh RSS differs in current filing contents but retains the covered 200-item field shape; production parsed and stored **200/200** rows, so no uncovered shape appeared. | none |
| Threshold-authority limitation | a common dependency module or manifest edge appears between store and view | v0.38 · 2026-08-04 — The shared `assign_dedup_identity` seam remains completed under R14; R-CLOSE added no dependency module or manifest edge. | none |
| ARCHITECTURE.md §8 / AGENTS.md R-CLOSE tag-mechanics duplication | the restatements diverge | v0.38 · 2026-08-04 — The release-parent full gate passes with both tag-mechanics restatements unchanged and no observed divergence. | none |
| Review-export capacity | the export crosses the declared ceiling | v0.38 · 2026-08-04 — Exact release parent `37f552c0c326098bdcf8f19de7eac19670d74680` exports at **2,781,281 bytes / 163 files / 2 retained cycles**, leaving **218,719 bytes / 7.29% / 2.04 cycles** at +107,226 bytes/cycle. Both exact pinned SEC RSS bodies and all structural archives remain excluded; the ceiling trigger did not fire. | none |

## Deferred completions

| Deferred item | Completion |
|---|---|
| **Public value-domain control (G6)** | 2026-08-04 — completed in v0.38 Step 1. R15 checks the exact v0.17.4 baseline at **6 routes / 31 status-media response variants / 112 recursive field occurrences**; its planted added-enum, removed-field, and changed-type mutations each fail at the executing serialization control, and the fresh full scan passes **15/15 rules / 84 controls**. |
| **SEC EDGAR admission** | 2026-08-04 — completed in v0.38 Step 2A under Grant B. Fresh robots/terms/feed evidence passed DR12, the production live path stored a coherent **200-document** first window in a fresh archive, public entitlement remained finance-only, and the non-retroactive admission chain plus **6** observation pins pass both artifact entry points. |

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
- [x] E0
- [x] REHEARSAL-COMPLETE
- [x] WIRE-ADMISSION
- [x] RE-MEASURE
- [x] R-CLOSE

*Box ids match the `PROGRESS-v0.38.md` entry ids exactly.*

---

## Handoff

**Decision report.** Grant A published exact v0.17.4 once, non-force, moving
only `main` to `a7d6c80e…` and creating its exact annotated tag; hosted run
30841505130 passed 9/9. Grant B captured exactly one robots, terms, and RSS
response, admitted the compatible evidence and fresh 200-document archive,
and ran one bounded manual SEC harvest. DR12 found no incompatible policy or
feed-shape drift. DR13 selected patch v0.17.5 because the admission adds the
named operational behavior and finance corpus without moving the 6/31/112
public response domain. DR14 kept v0.17.5 local and unpublished; no authority
from Grant A was reused.

**Codex-owned determinations.** C12 derived the complete admission checklist
from the lifecycle, compliance, and architectural authorities; fixtures closed
every state-machine clause and left only current wire/path facts. C13 recorded
fresh evidence in the v0.25-compatible dated form before the independent live
harvest consumed the configured URL. C14 corrected two author-side assumptions
exposed by the valid third artifact: the historical deferred audit now selects
its named inputs, and export inspection now derives every exact raw-RSS
exclusion from Repomix configuration.

**Stops and headroom.** No retained stop condition fired. One incorrect guessed
full SHA was rejected before creating any evidence ref; the subsequent fresh
absence check and correct non-force creation are recorded. The exact release
parent exports at **2,781,281 / 3,000,000 bytes**, leaving **218,719 bytes /
7.29% / 2.04 cycles** at +107,226 bytes/cycle. The manifest is **200,440 /
1,048,576 bytes**, leaving **848,136 bytes**. State remains below its
**129,970 / 453,741 bytes**. Golden remains byte-identical at **11/11**.

**v0.39 findings.** (1) Review-export headroom is now only 2.04 measured
cycles at the latest positive adjacent-cycle denominator; the fixed ceiling
has not fired. (2) The first evidence-ref push command used an incorrect
guessed full SHA and was correctly rejected without creating a ref; future
commands should resolve the full candidate before construction. Both
author-contract assumptions exposed by the third admission are fixed and
tested in v0.38, so they are evidence, not open findings.

**Standing operator question.** Whether to publish exact local v0.17.5 after
reviewing this close. SEC admission is complete; any recurring scheduled SEC
window still requires its separate explicit authorization.

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
