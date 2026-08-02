# TASKS-v0.35-EXECUTION.md — every number beside its own generator

## Runbook amendments

*(Appended per step as each completes, in the established form:
`Step N — <what was implemented> — <date>`.)*

**r1 — 2026-08-02 — activation-contract correction.** Executing the real
`cycle-check` against the staged operator-supplied runbook exposed one
author-side schema defect before its first commit: the runbook omitted the
machine-readable governed artifact byte-boundary authority carried by v0.34.
The unchanged `STATE.md` and `config/protected-artifacts.json` boundaries are
restored below. The checker, either boundary value, and every trigger remain
unchanged.

**Step 1 — entering state reconstructed; G1–G7 settled and all governed
observations refreshed — 2026-08-02.**

**Step 2 — all 68 planted-control locations derive from unique mutant anchors;
zero absolute line fields survive — 2026-08-02.**

**r2 — 2026-08-02 — Step 3 criterion-history clarification.** Step 1 required
every active observation placeholder naming v0.34 to be rewritten with a
measured v0.35 observation, so Step 3's instruction not to edit “the dated
v0.34 cell” cannot refer to a cell that still exists in this active runbook.
It is applied to the immutable v0.34 runbook and historical State record,
neither of which is edited. The active row receives the required forward
criterion and a new v0.35 measurement.

**Step 3 — arithmetic retention fallback deleted; every live caller and fixture
uses the Git-derived retained set — 2026-08-02.**

---

## Reviewer errors, mine, recorded before anything else

**1. I have read `AGENTS.md` §3 clause 1 in every cycle review since v0.23 and
never traced the edge it names.** The clause instructs an agent evaluating a new
crate to *"watch for the `icu_*` 2.2.0 chain via `idna` / `idna_adapter`, which
declares 1.86 and lives in the **offline** graph through `intel-compliance`."*
Measured against the committed tree, `crates/compliance/Cargo.toml` declares
exactly two dependencies — `async-trait` and `tokio` — and the lockfile's edges
put the chain under `net` only:

```
intel-ingest --(optional, feature "net")--> reqwest 0.11.27
             --> url 2.5.8 --> idna 1.1.0 --> idna_adapter 1.2.2 --> icu_* 2.2.0
```

The accurate statement is the one already sitting in
`crates/compliance/Cargo.toml`'s own comment: `texting_robots` **would have**
pulled that chain into the offline graph, which is why it was rejected. The
dependency gate states the counterfactual as the present fact, and it does so in
the one document that decides whether a crate may be admitted. An agent applying
clause 1 literally looks for the hazard in the wrong graph. **G7 owns this; Step
5 corrects it.** It is a reviewer miss of long standing, not an implementation
error.

**2. A method caveat that is not an error, recorded so the method is
auditable.** The Repomix export strips each file's trailing newline. My first
control-geometry pass reported R9/1's `find` text as occurring zero times in
`apps/cored/Cargo.toml`, which would have been a false finding about a broken
control. I re-read the raw bytes, found the text present, and re-appended the
newline before every subsequent measurement. Nothing was asserted from the
faulty pass. **E0 re-measures all control geometry against real repository bytes
regardless; my figures below are hypotheses, not results.**

---

## The named root cause for this cycle

v0.34's subject was *no control's admission may depend on the thing it
protects.* v0.35's is the next layer down.

**Every remaining hand-maintained number in the lifecycle machinery sits beside a
construction that could produce it — and where no such construction exists, the
assertion is standing in for one.**

Two shapes, and they are the same defect:

| shape | gap | what is asserted | what could produce it | cost of the assertion |
|---|---|---|---|---|
| **asserted where derivable** | G1 | 68 absolute `expected_line` integers | the constructed mutant tree | 36 → 12 → 25 → **27** hand re-derivations per cycle |
| | G2 | a retained-cycle boundary, computed twice | `git ls-files` | two answers that **measurably diverge** |
| | G3 | a growth denominator | a two-cycle-retention export pair | the margin the ceiling decision rests on |
| **asserted where nothing executes** | G4 | the `--features net` 1.86 floor | a 1.86-pass / 1.85-refute lane pair | rule zero, still open |
| | G5 | two deferral trigger states | an observation that is not the work itself | dated tautologies |

The asymmetry that makes G4 the cycle's centre of gravity: **the graph that
carries a 1.86-declaring crate is compiled only on 1.91; the graph that does not
carry one has a pinned, two-sided, executable floor lane.** The `msrv` job pins
1.78 and builds `--workspace` (offline, no `icu_*`). The `net` job pins 1.91 and
builds the only feature graph in which `icu_*` 2.2.0 is reachable. The floor
that has never been executed is the floor of the path this project's founding
scar is named after.

---

## Declared scope

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `no-release` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `tools/export_check.py` |
| `allow` | `shell/tests/**` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
| `allow` | `repomix.config.json` |
| `allow` | `run` |
| `allow` | `.github/workflows/ci.yml` |
| `allow` | `config/protected-artifacts.json` |
| `allow` | `tools/version_check.py` |
| `forbid` | `docs/state-archive/**` |
| `forbid` | `tools/model_profiles.py` |
| `forbid` | `tools/evidence_artifacts.py` |
| `forbid` | `apps/**/src/**` |
| `forbid` | `crates/**/src/**` |
| `forbid` | `crates/**/examples/**` |
| `forbid` | `crates/**/tests/**` |
| `forbid` | `shell/intel_shell/**` |
| `forbid` | `config/core.json` |
| `forbid` | `config/schedule.json` |
| `forbid` | `config/entities.json` |
| `forbid` | `config/subscriptions*.json` |
| `forbid` | `observations/**` |
| `forbid` | `fixtures/**` |
| `forbid` | `docs/cycles/**` (except this runbook and `PROGRESS-v0.35.md`, by standing precedence) |
| `release_authority` | `Cargo.toml`, `Cargo.lock`, `crates/*/Cargo.toml`, `apps/*/Cargo.toml`, `shell/intel_shell/__init__.py`, `shell/intel_shell/app.py`, `CHANGELOG.md`, `README.md` |

**Three scope moves relative to v0.34, each with its reason and its cost.**

- **`run` and `.github/workflows/ci.yml` move from `forbid` to `allow`.** Step 5
  cannot be hosted-only. R10's parity report emits
  `blocking hosted check ... has no local ci-local counterpart` as a **finding
  with no exemption path** — `RESIDUAL_LOCAL_CHECK_EXEMPTIONS` covers the
  opposite direction only. A hosted-only floor lane is therefore not expressible
  in the current control, and proposing one would be an author-side
  unsatisfiable requirement. Both sides move or neither does.
- **`config/protected-artifacts.json` moves from `forbid` to `allow`, for
  exactly one pin.** `run` is pinned at grade `authorization`
  (`sha256 44314ddf…`, 43,125 bytes) because `AGENTS.md` §8's L1 model-profile
  authorization rests on `run`'s bytes. Changing `run` obliges re-pinning it in
  the same cycle. **This is the cycle's largest deliberate loosening.** Step 5's
  acceptance criteria bound it: exactly one `pinned_files[]` entry may change,
  no `artifacts[]` entry and no `admission` record may be touched, the
  `tools/model_profiles.py` pin must be byte-identical at close, and the pin
  count must remain 332.
- **`tools/version_check.py` stays declared.** `OFFLINE_MSRV_AUTHORITIES` reads
  the `msrv:` job block and `run`'s `rustup run <ver> cargo … --workspace
  --locked` lines. Step 5 adds `rustup run` lines that are **not**
  `--workspace`, so the existing patterns should not match them. That is a
  hypothesis, not a fact — Step 5 must measure it, and if the new lines are
  captured as offline authorities the fix belongs to the pattern, not to the
  lane's spelling.

---

## Entering state

**Every line in this section is a hypothesis for E0 to confirm or refute.** It
is reconstructed from the delivered review export and the v0.34 progress log; I
did not run the repository.

| Claim | Value | How I obtained it |
|---|---|---|
| v0.34 closing implementation | `6a19d31dd00143fc85a5e6c157dceb90ce40e946` | read (progress log) |
| v0.34 audit child / delivered HEAD | `d8d20b81b9ea9027dada74ce047a7cd92815e9f3` | read, then **corroborated by measurement** (below) |
| Published `main` / peeled `v0.17.1` | `f02379f03ccdfd1b019413234f2ad014d169fb04` | read |
| Annotated tag object | `14912f134e45277e2b4fd10b7f5bf8b4900ca20d`, Git type `tag` | read |
| Release commit `R` | `7a621e39a069a1ef26438e841e7bb1ca2f34165b` | read |
| Evidence ref | `codex/v0.34-evidence-1117dc6` at `1117dc6db6ec0e55e8c8f078ca8059628f9f8262` | read |
| Governed export (closing-visible) | 2,527,180 bytes / 151 files / 2 retained cycles | read |
| Closing-tree export | 2,552,372 bytes; audit delta **+25,192** | read; arithmetic **confirmed**: 2,552,372 − 2,527,180 = 25,192 |
| **Delivered audit-child export** | **2,559,695 bytes / 151 files** | **measured** on the delivered export |
| Registered invariants | 12 rules / 68 controls | **measured**: R1:1 R2:1 R3:1 R4:1 R5:8 R6:1 R7:3 R8:3 R9:1 R10:3 R11:5 R12:40 = 68 |
| Checklist at close | 268 / 3 / 268 / 268 | read |
| Shell population | 352 collected / 352 passed on 3.11.4 and 3.12.13 | read |
| Golden | 11/11, delta 0 | read |

**The delivered-tree identity is corroborated, not assumed.** The delivered
export exceeds the reported closing-tree export by **7,323 bytes**; the R-CLOSE
entry appended to `PROGRESS-v0.34.md` measures **7,321 bytes**. One append beyond
the closing tree is the audit child. E0 confirms or refutes by running
`./run export-check` at exact `d8d20b81b9ea9027dada74ce047a7cd92815e9f3`.

**Expected activation state, predicted rather than discovered.** The committed
activation `cycle-check` will reject every trigger-bearing observation cell that
still names **v0.34**: four `ARCHITECTURE.md` rows and the 24 rows below. That
is the v0.28-forward cycle-identity rule behaving correctly, exactly as it did at
v0.34 activation. **It is not a defect and not a checker weakness.** E0 owns the
measured v0.35 rewrite. Any *other* activation defect — a missing column, a
dropped carried subject, an action with no literal discharging `Step N` — is an
author-side runbook defect, and is recorded as a numbered amendment before the
first commit rather than worked around.

**The retention pattern this activation must carry**, derived by executing
`expected_review_export_retention_pattern` standalone at v0.35 with tracked
runbooks v0.34 and v0.35:

```
docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-3]}{.md,.*.md,-*.md}
```

---

## Gaps

| Gap | Subject | Priority | Step |
|---|---|---|---|
| **G1** | 68 planted controls assert an absolute line number the mutant already determines | **P0** | 2 |
| **G2** | the retained-cycle boundary has two sources of truth that measurably diverge | **P1** | 3 |
| **G3** | every published growth denominator predates the retention change just made | **P1** | 4 |
| **G4** | the `--features net` 1.86 floor is a claim nothing executes | **P1** | 5 |
| **G5** | two deferral triggers are their own discharge condition | **P2** | 1 |
| **G6** | `test_r10_derives_every_exemption_without_pinning_its_count` pins four counts | **P3** | 5 |
| **G7** | `AGENTS.md` §3 clause 1 places the `icu_*` chain in the wrong graph | **P2** | 5 |

### G1 — the line-number coupling, and how far it is removable

For each of the 68 controls I built the mutant (`find` → `replace_with`,
exactly once) and asked whether the line at `expected_line` has text that is
unique **within that mutant**:

- **67 / 68 are unique as a single line.**
- **40 of those 67 already point at a named `# Invariant R12 control site:
  <subject>` marker.** The anchor vocabulary exists and is authored.
- **One exception: R1/1** (`crates/store/src/sqlite.rs`). Under mutation, line
  793 is `let changed = assign_canonical_ids_tx(&tx, max_distance)?;`, which
  also occurs at 816. Widening: 2-line window → 2 occurrences; 3-line → 2;
  **4-line window beginning at the planted `fn rebuild_identity_with_limit`
  signature → 1 occurrence.**

The re-derivation series is **36 → 12 → 25 → 27** shifted existing values, over a
control population of **58 → 61 → 68**. It is non-monotonic and supports no
linear approach rate — G5 of v0.34 settled that, and this gap does not reopen
it. The argument for acting is not that the count is rising; it is that the
count is **avoidable**, and that every hand-typed value is a place where a
figure can be copied from the wrong output.

**The constraint that must not be adopted:** requiring the anchor to lie inside
`replace_with`. Forty anchors are pre-existing marker comments sitting *above*
the mutation. That constraint would break them and would be an author-side
unsatisfiable rule of exactly the kind this project has recorded six times.

### G2 — measured divergence, and a trigger already satisfied

`expected_review_export_retention_pattern` computes the retained-cycle boundary
two ways. Executed standalone:

| construction | derived branch (Git-tracked set) | fallback branch (`retained_cycle_paths=None`) |
|---|---|---|
| active v0.35, tracked v0.34 + v0.35 | `…3[0-3]…` | `…3[0-3]…` — **agree** |
| active v0.36, tracked v0.34 + v0.36 | `…3[0-3]…` | `…3[0-4]…` — **differ** |

`tools/invariant_scan.py`'s `retention-skipped` control constructs the second
shape and builds its expected pattern from the **fallback**. So the v0.34
deferral row's trigger — *"the `retained_cycle_paths=None` branch produces an
answer that differs from the tracked retained set in any construction a control
or test relies on"* — **is satisfied today by an existing control**, while the
dated cell records that it did not fire.

The intent is plainly *"differs in a construction that relies on the two
agreeing."* Per this project's standing principle, a disagreement between a
measurement and a criterion is corrected in the **criterion**. The dated v0.34
observation is not retroactively edited; the row is forward-corrected.

**No operational hazard for v0.35:** both branches agree at v0.35.

### G3 — the denominators are epoch-stale

All four published rates — **77,014** (governed v0.31→v0.32), **77,862**
(post-retention steady), **86,946** (persistent components), **79,962**
(positive delivered) — were measured under **three-cycle** retention, which
carried a recurring −9,084 bytes/cycle turnover term. v0.34 moved retention to
**two cycles**. Step 3 of v0.34 made the entry point emit that it *"cannot detect
a basis predating a structural change."* One has since occurred.

Nothing here is dishonest: the bound is emitted, and the row is bound to the
last governed field it can see. But **the 6.14-cycle figure is not decision-grade
for choosing the next lever**, and the export is the nearest governed boundary.

The mechanical arithmetic v0.35 inherits, measured on the delivered export:

| item | bytes | share |
|---|---|---|
| v0.33 pair, which leaves the export at activation | **−97,951** | — |
| v0.34 pair, as the new prior | 85,337 | 3.34% |
| `STATE.md` | 243,431 | 9.53% |
| `config/protected-artifacts.json` | 192,094 | 7.52% |
| `tools/invariant_scan.py` | 129,033 | 5.05% |
| `tools/cycle_check.py` | 116,677 | 4.57% |
| **`tools/` group** | **605,291** | **23.71%** |

At two-cycle steady state the retention mechanism recycles approximately one
full runbook pair per cycle against roughly 78,000 bytes/cycle of growth
elsewhere. **That may materially change the projection in either direction**,
which is precisely why Step 4 measures it rather than asserting it. `tools/`
grew only ~3,000 bytes across v0.34 — a single cycle is not a trend, and Step 4
must say so.

### G4 — the oldest unexecuted claim in the repository

`.github/workflows/ci.yml`'s `net` job pins toolchain **1.91**. The `msrv` job
pins **1.78** and builds `--workspace` only. The `drift` job does compute
declared MSRVs of the resolved graph — but it is `if: github.event_name ==
'schedule'`, `continue-on-error: true`, and writes to `$GITHUB_STEP_SUMMARY`.
**It cannot fail, and nothing consumes its output.** So "the net path's floor is
1.86" is asserted in `AGENTS.md` §4, in `ci.yml`'s own comment block, and in
`ARCHITECTURE.md` and `STATE.md`, and is observed by zero executable assertions.
`STATE.md` §5 already says this plainly; it has said so for many cycles.

The honest control is two-sided, exactly like the 1.78/1.75 pair that settled the
offline floor: **1.86 expected to succeed, 1.85 expected to fail.** A lane that
can only pass proves nothing.

### G5 — triggers that are their own discharge

Two rows carry conditions that cannot be observed, only performed:

- `--features net` Rust 1.86 execution — *"…and an executable local or hosted
  lane that actually pins and runs the net path on Rust 1.86."*
- `v0.8.0` / `v0.10.2` publication — *"operator-authorized push of both exact
  annotated objects."*

Compare the event-shaped rows: *a second concurrent harvester*, *a live
transient robots outage*, *an operator server session*, *a spelling outside
registered vocabulary*. Those can be observed not to have happened. A
self-discharging condition yields a dated cell that is true forever and carries
no information, which is the freshness machinery doing work it cannot do.

**This is a taxonomy correction, not a demand to do the work.** Step 1 classifies
every governed row as *event-shaped*, *authorization-shaped*, or
*self-discharging*, and records the count. It changes no trigger text this
cycle. If `no-release`-shaped work items belong outside the freshness tables
entirely, that is an operator decision recorded at Step 7, not a Step 1 edit.

### G6 — a test whose name and body disagree

`shell/tests/test_invariant_scan.py::test_r10_derives_every_exemption_without_pinning_its_count`
asserts `local_jobs == 20`, `local_checks == 24`, `blocking_jobs == 6`, and
`hosted_checks == 23`. The derivation property the name claims is carried by the
two assertions that follow. The four integers are a separate, unnamed pin on the
current CI topology.

I do **not** assert this is a defect. A pinned count that must be consciously
updated is a legitimate control, of the same kind as the golden's
`documents_analyzed == 12`. But it is unnamed and it sits inside a test that
says it does the opposite, and **Step 5 moves at least two of the four values.**
Step 5 classifies it and either renames the test or splits the pins into a named
topology test with a stated reason.

### G7 — the dependency gate names the wrong graph

Recorded under *Reviewer errors* above. Step 5 corrects `AGENTS.md` §3 clause 1
so the hazard is placed where the measured edges put it, and so the executable
lane added by that step is the thing the clause points at.

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

Every trigger is carried **unchanged**. At activation the observation column
still named **v0.34**, as expected above. **E0 has now rewritten every cell with
a measured v0.35 observation and the literal active cycle name. No trigger
column was edited to match what happened.**

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.35 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | v0.35 · 2026-08-02 — Step 1 started no harvester and made no publisher request; trigger did not fire | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.35 · 2026-08-02 — Step 1 made no publisher request, observed no outage, and received no authorization; trigger did not fire | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.35 · 2026-08-02 — production net request source remains forbidden and no live 304 was observed; trigger did not fire | none — the gap stays recorded |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.35 · 2026-08-02 — production ingest source remains forbidden and no connector review occurred; trigger did not fire | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.35 · 2026-08-02 — Step 1 used repository checks and fixture/test runtimes only; no further origin or concurrency appeared | none — complete, do not re-exercise |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | v0.35 · 2026-08-02 — no scheduler or service ran and no bounded-window authorization was supplied; trigger did not fire | none — the 600-second clock still has never issued a request |
| Postgres / pgvector / multi-host seam | unchanged | v0.35 · 2026-08-02 — no topology, dependency, schema, or production-source path changed | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.35 · 2026-08-02 — no third-party shell or replacement-invariance claim appeared; trigger did not fire | none |
| L2 forced-command wrapper | an operator server session | v0.35 · 2026-08-02 — no model-profile command or server session occurred; trigger did not fire | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.35 · 2026-08-02 — the real self-test passed 12 rules / 68 controls and no new spelling appeared; trigger did not fire | none |
| **`--features net` Rust 1.86 execution** | a scoped cycle authorized to change evidence topology and an executable local or hosted lane that actually pins and runs the net path on Rust 1.86 | v0.35 · 2026-08-02 — Step 1 confirmed the lane is not present yet; this self-discharging trigger remains assigned to Step 5 | **Step 5 — this cycle is that scoped cycle; the trigger is self-discharging and G5 records that separately** |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.35 · 2026-08-02 — neither a third-publisher review nor admission decision occurred; trigger did not fire | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.35 · 2026-08-02 — direct remote inspection found neither historical tag and no historical ref moved; the self-discharging trigger did not fire | none — no historical ref touched; G5 classifies it |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.35 · 2026-08-02 — both tags remain absent and the flag remains unchanged; trigger did not fire | none — the flag stays |
| Manifest retention/indexing | the manifest reaches its governed artifact byte boundary, or two consecutive clean `./run verify-artifacts` runs each take ≥1.00 s real | v0.35 · 2026-08-02 — unchanged 192,042-byte / 332-pin manifest; Step 1's complete timed pair was 0.11 s / 0.10 s real; neither trigger fired | **Step 5 — the `run` pin changes; the manifest is `allow` for exactly one `pinned_files[]` entry** |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.35 · 2026-08-02 — shell source remains forbidden and no release value changed; trigger did not fire | none — `shell/intel_shell/**` remains forbidden |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.35 · 2026-08-02 — no such operator decision was supplied; trigger did not fire | none — recorded, not acted on |
| Second `STATE.md` archival | the export ceiling trigger fires, or `STATE.md` reaches its governed artifact byte boundary | v0.35 · 2026-08-02 — Step 1 measured State at 243,402 / 453,741 bytes and exact delivered v0.34 at 2,559,695 / 3,000,000 export bytes; neither trigger fired and Step 4 owns the post-retention projection | **Step 4 — re-place the availability in cycles on a post-retention basis** |
| **Planted-control line numbers re-derived by hand** | a control-schema change, or a cycle in which the re-derived count exceeds the controls it protects | v0.35 · 2026-08-02 — Step 2's schema change fired the first clause and completed the assigned work. All 68 controls now derive their finding line from an authored anchor resolved exactly once against the constructed mutant; 40 retain the pre-existing named R12 control-site marker, registered anchors are never wholly supplied by `replace_with`, and zero `expected_line` or other absolute-line fields survive | **Step 2 — completed; Step 7 moves this subject to Deferred completions** |
| Retention derivation across a version-family boundary | an active cycle whose name is not of the form `v0.<n>` — raising at `v1.0`–`v1.2`, silently under-excluding from `v1.3` onward | v0.35 · 2026-08-02 — v0.35 still matches `v0.<n>`; trigger did not fire | none — recorded, not acted on |
| Published-release divergence | the unpublished distance contains a measured runtime behaviour difference persisting across three consecutive closed cycles within the current publication epoch, or acquires any public-surface change | v0.35 · 2026-08-02 — the activation distance is lifecycle configuration and records only, with no runtime-behaviour or public-surface change; v0.17.1's reset leaves the epoch count at zero | **Step 7 — restate the epoch count under the v0.32 reset rule** |
| MSRV current-restatement membership | a current restatement of either Rust floor lands outside the registry without failing a check | v0.35 · 2026-08-02 — `version-check` reported 22 offline-MSRV and 3 release-version current restatements with no unregistered current floor statement; trigger did not fire | **Step 5 — the new lanes add Rust-floor literals; measure membership before and after** |
| **Retention arithmetic fallback** | the retention formatter again permits an omitted retained set, or any live production or fixture caller supplies a set not derived by `expected_retained_cycle_paths` for that root | v0.35 · 2026-08-02 — Step 3 deleted the optional branch, made the retained set mandatory, committed fixture cycle documents before derivation, and passed the real checker at the exact activation pattern. R12's new 69th control makes an optional parameter fail. The prior criterion was truthfully satisfied in Step 1; under this forward criterion the trigger did not fire | **Step 3 — completed; the corrected regression criterion remains governed** |
| Optional cycle-ending audit disclosure | a closed cycle whose delivered export differs from its governed figure and which records no cycle-ending audit field | v0.35 · 2026-08-02 — v0.34 carries its required audit field and v0.35 remains open; the general optionality ruling is unchanged | none — the v0.32 ruling stands; **this runbook separately requires its own at Step 7** |

---

## Step 1 · E0 — Rebuild the entering state and settle G1–G7 🤖

**Objective.** Confirm `HEAD` is green, re-measure every hypothesis in
*Entering state*, and settle all seven gaps. **Every line under `## Entering
state` is a hypothesis.**

**Decision gate.** If the worktree is dirty apart from this untracked runbook,
if `6a19d31d…` is not the immediate parent of `d8d20b81…`, if published v0.17.1
identity has moved, or if any local gate fails at entry — **record and stop.**

**Acceptance criteria.**

- All **20** `ci-local` jobs pass; `invariant-scan` passes its registered
  self-test with rule and control totals stated; golden **11/11**; all pins
  verified twice with both real times recorded; both Python lanes reported
  through `tools/test_population.py`, never as a bare `N/N`.
- Published state confirmed **by direct remote inspection**, not from the
  closing record: `main`, peeled `v0.17.1`, the annotated tag object and its Git
  type, the release parent, and the v0.34 evidence ref.
- **The delivered-export identity is settled by measurement.** Run `./run
  export-check` from the project root at exact `d8d20b81b9ea9027dada74ce047a7cd92815e9f3`.
  I measured **2,559,695 bytes / 151 files** and inferred the audit child from a
  7,323-byte difference against the reported closing tree, with the R-CLOSE
  progress append measuring 7,321 bytes. **Confirm or refute.**
- **G1 settled by construction over the real registry.** For each of the 68
  controls, build the mutant and record (a) whether the line at `expected_line`
  is unique in that mutant, (b) whether it is a named control-site marker, (c)
  for any non-unique case, the minimum anchor width that becomes unique. My
  figures — 67/68 unique, 40 marker-anchored, R1/1 requiring a 4-line window —
  are hypotheses. Report the measured table.
- **G2 settled by execution of both branches** on at least the v0.35 and
  skipped-cycle constructions, and by enumerating every call site that reaches
  the fallback. Name whether the `retention-skipped` control relies on the
  divergence.
- **G3 settled by derivation.** State explicitly which published denominators
  were measured under three-cycle retention and are therefore epoch-stale, and
  which post-retention adjacent pairs exist yet. If none exists, say so — do not
  synthesize one.
- **G4 settled by reading the real workflow and `run`.** Confirm the `net` job's
  pinned toolchain, the `msrv` job's scope, and that the `drift` job's MSRV
  output is consumed by nothing. Then measure the actual declared `rust-version`
  of the `icu_*` chain rather than repeating 1.86 from prose.
- **G5 settled by classification.** Classify all governed rows in both tables as
  event-shaped, authorization-shaped, or self-discharging, with counts. **Change
  no trigger text.**
- **G6 settled by reading the test and `r10_report`.** State which of the four
  pinned integers Step 5 will move.
- **G7 settled by tracing the real dependency edges** from `Cargo.lock` and the
  crate manifests, not from `AGENTS.md`.
- **Trigger acceptance.** All four `ARCHITECTURE.md` trigger-bearing rows and all
  24 rows above carry a measured v0.35 observation with a valid ISO date and the
  literal active cycle name. **No trigger text changes.**
- Golden **11/11**, delta **0**, on a standalone post-task run.

---

## Step 2 · ANCHOR — Derive every planted-control location 🤖

**Depends on:** Step 1's G1 table.

**Objective.** Replace the 68 absolute `expected_line` integers with an
expectation the constructed mutant determines.

**Decision gate.** If any control cannot be given an anchor that occurs
**exactly once in its mutant**, stop and record it as an author-side
unsatisfiable requirement — **do not** compute that control's anchor from the
emitted finding, and do not fall back to a line number for a subset without
recording the split and its reason.

**Design.** Schema field `expected_anchor`: a literal that must occur exactly
once in the mutated file. The harness derives the expected line from the
mutant and builds the expected finding as today. A companion
`expected_anchor_line_offset` (default `0`) names which line **within** a
multi-line anchor carries the finding; R1/1 is expected to need offset `3`.

**Why this does not weaken the control.** The anchor is authored, and it is
resolved against the **constructed mutant tree** — never against the rule's
output. The self-test still compares an independently-constructed expected
string to what the rule emitted. The only coupling removed is to file-global
line geometry.

**Acceptance criteria.**

- Config validation **rejects** an anchor occurring 0 times and an anchor
  occurring ≥2 times, each proved by a construction that runs the real
  `invariant_scan` entry point, with the emitted rejection text recorded
  verbatim.
- A planted mutation that makes a rule report **line + 1** is **caught** by the
  self-test. A control that cannot fail is not a control; demonstrate the
  failure before trusting the pass.
- Demonstrate that the anchor resolution reads the **mutant**, not the
  unmutated tree: a control whose anchor exists only in `replace_with` must
  resolve, and one whose anchor exists only in the original must be rejected.
- **No anchor may be a substring only of `replace_with` by requirement.** Forty
  anchors are pre-existing marker comments above the mutation; a rule demanding
  otherwise is unsatisfiable and must not be written.
- Registered suite passes **12/12 rules / N controls** with N stated and
  unchanged from 68 unless a control is added or removed with a reason.
- `shell/tests/test_invariant_scan.py` passes with the new schema cases;
  the focused count is stated.
- Full `./run ci-local` passes 20/20 with this task's box still open; golden
  **11/11**, delta **0**.
- **Report the count of remaining hand-typed absolute line numbers in
  `config/invariant-rules.json`.** If it is not zero, name each survivor and why.

---

## Step 3 · ONE-RETENTION — A single retained-cycle authority 🤖

**Depends on:** Step 1's G2 result.

**Objective.** Remove the second source of truth for the retained-cycle
boundary, or bound it with an executed comparison.

**Decision gate.** If deleting the fallback breaks fixture bootstrap in a way
that cannot be resolved by building the tracked set after commit, take the
narrow-the-criterion option **and say so explicitly** — do not leave both
branches live with an unexecuted claim that they agree.

**Acceptance criteria.**

- **Option A (preferred): delete the fallback.** Every call site supplies the
  Git-derived set. Fixtures commit their cycle documents before deriving the
  pattern. Prove by construction that no call path reaches an arithmetic
  boundary.
- **Option B: keep the fallback, add a differential control.** For every
  construction a test or control relies on, both branches are computed and
  compared, and a planted divergence in a construction that relies on agreement
  **fails**. The `retention-skipped` control's deliberate divergence must be
  named as an exception in the control itself, not in prose.
- Either way, **forward-correct the deferral row's criterion.** The trigger as
  written is already satisfied by an existing control. Correct the criterion;
  **do not edit the dated v0.34 cell** and do not claim the observation was
  wrong when the wording was.
- The v0.35 activation pattern is confirmed as
  `docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9],3[0-3]}{.md,.*.md,-*.md}`
  by the real `cycle-check` entry point, with the rejection text for a stale
  pattern captured verbatim.
- Focused `shell/tests/test_cycle_check.py` count stated; full gate 20/20;
  golden **11/11**, delta **0**.

---

## Step 4 · POST-LEVER BASIS — Measure the two-cycle epoch 🤖

**Depends on:** Step 1's G3 derivation.

**Objective.** Give the export margin a denominator measured under the
structure that now exists.

**Decision gate.** If no post-retention adjacent same-kind pair exists yet, say
so and **do not synthesize one**. A projection on a basis the checker says it
cannot validate is reported with that bound attached, not upgraded by wishing.

**Acceptance criteria.**

- The full governed series is restated, and **each transition is labelled with
  the retention depth in force when it was measured**. The four published
  denominators are explicitly marked epoch-stale with respect to the v0.34
  lever.
- The v0.33-pair reclaim that occurs mechanically at this activation is measured
  on the real export, not estimated. My figure is **97,951 bytes**; confirm or
  refute.
- The next `STATE.md` archival availability and the export-ceiling availability
  are both re-placed in cycles on post-retention denominators where one exists,
  and on named stale denominators with the bound stated where one does not.
  **State which boundary is nearest and by how much.**
- **No lever is selected in this step.** If the measured basis indicates one is
  needed, present the options with exact measured reclaims and stop for the
  operator. Present at minimum: a third `STATE.md` archival; excluding
  `config/protected-artifacts.json` (192,094 bytes / 7.52%) from the review
  export, with the cost that `export-check` currently *requires* that path and
  the change would move `REQUIRED_PATHS`; and retention depth 1, with the cost
  that the reviewer loses the prior cycle entirely.
- No dated historical figure is edited. Corrections are forward.
- Golden **11/11**, delta **0**.

---

## Step 5 · NET-FLOOR — Make the 1.86 claim executable 🤖

**Depends on:** Steps 1 (G4, G6, G7) and 2. **This is the cycle's largest
scope loosening; read the Declared scope notes before starting.**

**Objective.** Give the `--features net` MSRV floor a two-sided executable lane,
correct the dependency gate that misplaces its cause, and re-pin `run`.

**Decision gate — three clauses, any one stops the step.**

1. **If the 1.85 lane passes, the 1.86 claim is false.** The finding is the
   claim, not the lane. Record the measured floor and stop; do not adjust the
   lane until the operator has ruled on the corrected floor.
2. **If the 1.85 lane fails for a reason other than a declared
   `rust-version`** — a lockfile-format rejection, a registry or network error,
   an unrelated compile error — **it is a non-result, not a refutation.** This is
   HC12's exact lesson: the 1.75 failure surfaced as
   `failed to download replaced source registry 'crates-io'` and sent the
   investigation to the wrong place. The captured stderr must name the crate and
   its declared floor.
3. **If R10 parity cannot classify both sides**, stop and record the
   classification gap. A hosted lane with no local counterpart is not
   expressible: `RESIDUAL_LOCAL_CHECK_EXEMPTIONS` covers local-without-hosted
   only, and the reverse emits an unexemptable finding.

**Acceptance criteria.**

- A local lane pair in `run`'s `ci_local_jobs` table following the existing
  `rustup run <version>` pattern, and hosted counterparts in `ci.yml`, such that
  R10 parity passes **without adding a residual exemption**.
- The **1.86 lane passes** and the **1.85 lane refutes**, each with captured
  command text and output. The refutation output names the declaring crate and
  version. State whether the floor is genuinely 1.86 or something else.
- **Exactly one `pinned_files[]` entry changes** — `run`. `tools/model_profiles.py`
  is byte-identical at close, no `artifacts[]` entry moves, no `admission`
  record is created or edited, and the pin count remains **332**. Run both
  `python3 tools/evidence_artifacts.py validate` and `./run verify-artifacts`
  before proposing the manifest change, per `AGENTS.md` §7.
- **`version-check` is measured before and after.** Report offline-MSRV and
  release-version current-restatement counts (v0.34 closed at **22** and **3**)
  and confirm the new `rustup run` lines are not captured as offline
  authorities. If they are, the fix belongs to the pattern.
- **G7:** `AGENTS.md` §3 clause 1 is corrected to place the `icu_*` chain in the
  `net` graph via `intel-ingest` → `reqwest` → `url` → `idna` → `idna_adapter`,
  with the measured edges cited. The `intel-compliance` counterfactual is kept
  as the reason `texting_robots` was rejected, marked as a counterfactual.
- **G6:** `test_r10_derives_every_exemption_without_pinning_its_count` is either
  renamed or split so that a test claiming a derivation property does not
  silently pin four topology integers. State each new value and why it moved.
- **Evidence topology delta is stated explicitly** before Step 6: the expected
  receipt and Sigstore-bundle count, up from **7 / 7**, and every place that
  count is asserted.
- Full gate 20/20 with this task's box still open — note the local job total
  moves from 20; report the new total from `ci_local_job_count`, derived, not
  typed. Golden **11/11**, delta **0**.
- `AGENTS.md` §4's command block is updated to include the new lanes, so the
  document and the executable table agree.

---

## Step 6 · RE-MEASURE — Authenticate the exact candidate 🤖

**Depends on:** Steps 1–5 complete and boxed.

**Objective.** Produce release-grade hosted evidence for the exact candidate on
a fresh operator-authorized evidence ref.

**Decision gate.** Any reuse, force, move, or repurposing of an existing ref —
**stop**. Before any push, `git ls-remote` must exit zero with **no entry** for
the fresh ref, and the operator must explicitly authorize that exact candidate
to that one ref.

**Acceptance criteria.**

- Candidate HEAD clean; tree hash recorded; pre-push `ls-remote` absence
  recorded; the single push creates the ref; immediate and final readback each
  resolve it to the exact candidate.
- Hosted run recorded by id and attempt. **All executable jobs pass, including
  both new floor lanes.** The workflow's own SHA-256 is recorded — it changed
  this cycle, so state the new value and that it is intended.
- The repository release-grade verifier consumes the downloaded ephemeral
  receipts and bundles, accepts all, rejects none, and finds the complete runner
  matrix. **The expected count is Step 5's stated figure, not 7.** Every accepted
  identity binds repository, workflow, source digest, and source ref.
- Local and hosted shell populations compared through `tools/test_population.py`
  only. Every skip named with node id, declared reason, and `on_site` marker.
  Every written figure is comparator output.
- Project-root export at the exact candidate: bytes, files, retained set
  (v0.34–v0.35), both protected byte classes excluded, derived/required counts.
  Append the governed field in the exact form
  `- governed review-export measurement: tree=…; bytes=…`.
- All **332** pins and both protected databases match, with both real times
  recorded. Manifest bytes stated — this cycle they change; state the delta and
  that it is the single `run` pin.
- Published `main`, peeled `v0.17.1`, and the annotated tag object confirmed
  unchanged by direct remote readback.
- Golden **11/11**, delta **0**, locally on the exact candidate, hosted, and at
  the mandatory standalone post-record run.

---

## Step 7 · R-CLOSE — Close v0.35 on the operator's disposition 🤖

**Depends on:** Step 6.

**Objective.** Close the cycle on a dated, reasoned record.

**Decision gate.** **Publication authorization is not granted by this runbook.**
Present the measured diff classification and stop for the operator's explicit
selection. Do not push a tag or move `main` without it.

**The classification this step must present, not assume.** The declared
`disposition_intent` is `no-release`. Step 5 adds executable CI lanes and changes
one protected pin; under `ARCHITECTURE.md` §8 that is operations-and-evidence,
for which a patch release is *available* but not required, and there is no route,
response-body, schema, or `/v1/*` value-domain movement anywhere in this cycle.
**Present both readings with the measured path set and let the operator choose.**
If the operator selects a release, the declared release-authority patterns are
already in scope and the intent field is amended as a numbered runbook
amendment, recorded rather than quietly reinterpreted.

**Acceptance criteria.**

- The disposition is recorded in the dated form
  `Release disposition: release|no-release (as of YYYY-MM-DD)`, with the
  **structural reason** — the measured content of the unpublished distance. If
  `no-release`, "nothing shipped" is not substituted for that reason; this cycle
  did ship an executable control, and the record says what it is.
- `version-check` passes with every authority and current-restatement count
  stated.
- The governed export row is bound to the **last governed field visible in the
  closing tree**, and the separate append-only audit child records the
  closing-tree measurement in the exact non-governing form
  `- cycle-ending review-export audit: closing_tree=…; bytes=…; audit_delta=…`.
  **This runbook requires that audit field**; its general optionality is
  unchanged.
- Both artifact boundaries measured and stated with remaining cycles; the
  nearest governed boundary named.
- `checklist-audit` passes with all four figures stated once the real closing
  entry exists.
- The published-release divergence row is restated under the v0.32 epoch-reset
  rule.
- The complete entry point passes on the audit child; golden **11/11**.
- **Reviewer/control acceptance:** report the count of `expected_anchor` values
  that changed relative to activation and the count of surviving hand-typed line
  numbers. If Step 2 succeeded, the second number is zero and the
  planted-control deferral row closes into a **Deferred completions** table with
  a valid ISO-dated completion.

---

## Dependency gates

No new crate is admitted this cycle. If Step 5's measurement changes the
understood floor of the `net` graph, the three-clause gate in `AGENTS.md` §3 is
**re-read against the corrected clause 1**, and the corrected text is what
governs any future admission.

## Standing prohibitions

- No protected byte written except the single `run` pin at Step 5.
- No publisher request, scheduler run, service start, or model-profile command.
- No historical ref created, moved, or deleted; the sole remote mutation is
  Step 6's authorized evidence ref.
- No governed byte boundary or ceiling moved without an explicit operator
  selection recorded at Step 4.
- No closed-cycle document, observation, or fixture edited.
- No dated historical measurement edited; corrections are forward and dated.
- No expectation, anchor, or figure copied from a checker's own output where the
  construction can produce it independently.
- No acceptance criterion phrased as a repo-wide absence is discharged by
  inspection; it needs a registered, self-testing `invariant-scan` rule with an
  executable `fail_before`.

## Cycle checklist

- [x] ACTIVATE — runbook committed, declaration moved to v0.35, progress
      skeleton created, retention pattern advanced to `3[0-3]`
- [x] Step 1 · E0
- [x] Step 2 · ANCHOR
- [x] Step 3 · ONE-RETENTION
- [ ] Step 4 · POST-LEVER BASIS
- [ ] Step 5 · NET-FLOOR
- [ ] Step 6 · RE-MEASURE
- [ ] Step 7 · R-CLOSE

---

## Provenance

**What I read.** `STATE.md`, `ARCHITECTURE.md`, `AGENTS.md`, `CHANGELOG.md`,
`docs/cycles/TASKS-v0.34-EXECUTION.md`, `docs/cycles/PROGRESS-v0.34.md`,
`.github/workflows/ci.yml`, `run`, `tools/export_check.py`,
`tools/invariant_scan.py` (R10 and self-test paths),
`tools/cycle_check.py` (retention-pattern paths), `tools/version_check.py`
(authority declarations), `repomix.config.json`, the crate manifests, and
`Cargo.lock`.

**What I measured, on the delivered review export.**

1. Export size **2,559,695 bytes / 151 files**; retained set exactly the v0.33
   and v0.34 pairs; `Cargo.lock` present; no `docs/state-archive/**`; no
   `sec-edgar-usgaap.rss.xml`.
2. Delivered-tree identity corroborated: export exceeds the reported closing
   tree by **7,323 bytes**; the R-CLOSE progress append measures **7,321
   bytes**. Codex's audit arithmetic confirmed: 2,552,372 − 2,527,180 = 25,192.
3. Registry population **12 rules / 68 controls**, by rule.
4. Control geometry across all 68 mutants: **67 unique single-line anchors**,
   **40 already named control-site markers**, R1/1 unique only at a **4-line**
   window.
5. Retention-branch divergence by standalone execution of the real function:
   agree at v0.35, **differ** at a skipped cycle (`3[0-3]` vs `3[0-4]`).
6. Export composition by file and group, including the **97,951-byte** v0.33
   pair that leaves at activation and the **23.71%** `tools/` group.
7. Dependency edges placing `icu_* 2.2.0` under `net` only.
8. `run` pinned at grade `authorization`, sha256 `44314ddf…`, 43,125 bytes.

**What I did not do.** I did not run the repository, its test suite, its
checkers, or any Git command against it. Every figure above is a hypothesis for
E0 to confirm or refute against real repository bytes. Where my method could
have produced a false finding — the stripped-trailing-newline artifact — I have
said so above rather than letting the figure stand unqualified.
