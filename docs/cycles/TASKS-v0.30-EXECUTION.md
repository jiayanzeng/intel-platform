# TASKS-v0.30-EXECUTION.md — bind the population, not the instance

v0.29 closed `no-release` on 2026-07-31 and **every substantive claim in the Codex
report was independently re-derived and held.** Several matched to the byte.
`invariant-scan` moved **12 rules / 49 controls → 12 / 51** with R12 at **23**,
and the three v0.29 bindings are real: the retention pattern is derived from the
active cycle and the one `CYCLE_RETENTION_DEPTH` authority with no expected
string stored anywhere; the boundary populations are initialized before either
gate and an explicit relationship check replaces the traceback; the SQL/Rust
ordering test compares each production boundary against **the other**
implementation's derived result, which is why Codex's production-side mutation
made it fail. The manifest went from **316 → 331** pins through the sanctioned
path — explicit operator authorization, dated amendment, scope narrowed to two
exact evidence paths plus the manifest, one implementation commit — and the
fifteen registered records are **exactly** seven receipts, seven paired Sigstore
bundles, and one report, with no drift. `checklist-audit` **232** reconciles
exactly: 29 cycles × 8 bolded tasks, 231 before the closing box was checked.

**The newline artifact is now measured rather than assumed.** v0.29's reviewer
error 4 recorded that every byte figure derived from a Repomix export is a lower
bound. It is a lower bound by **exactly one byte per file**, and this review
proved it three independent times: `STATE.md` exports at 257,421 against the
recorded 257,422; the manifest at 191,394 against 191,395; and the R-CLOSE audit
entry at 4,964 against a 4,965-byte export delta. **Per-file repository size is
export size plus one. The export file's own byte count is exact.** That upgrade
is used throughout this file, and every figure below says which kind it is.

---

**Four reviewer errors, all mine, recorded before anything else.**

1. **The supplied review stated "nine declarations" of the MSRV floor without
   having enumerated nine.** The enumerated list is in G2 below and the count
   depends on whether job labels count as declarations. **Stating a count before
   holding the list is the error**, and it is the same error class this cycle
   exists to remove.
2. **The v1.0 retention divergence was demonstrated by reconstruction, not by
   the real checker.** The derivation was re-implemented in a standalone script
   and evaluated across future cycle names; `cycle_check` itself was never run
   against a `v1.0` tree. This is exactly how v0.29's `UnboundLocalError`
   demonstration was labelled, and **G3 owns settling it by execution.**
3. **The claim that the latest-at-close rule has no executed control rests on
   reading two assertions, not on an exhaustive search.** `check_trigger_table`
   validates a dated token and the active cycle literal and nothing else — but no
   exhaustive search of every checker was performed. **G4 settles it.**
4. **The pre-activation claim that this draft was "run through the real
   checker" stated more than its construction supported.** The full checker
   cannot execute against the delivered export: the evidence exclusion breaks
   cycle-identity resolution at import, and the export tree carries no git
   history, so the diff gate, commit resolution, and tag verification never ran.
   Every sub-check that **can** run against that construction was run, and every
   one passed — but by this file's own interpretive rule, an exit code from a
   construction the checker never fully examined is not the measurement the
   sentence implied. The construction is now disclosed in the provenance
   section, and **E0's full run against the real tree is the evidence of
   record.**

---

**The named root cause for this cycle.** v0.29 was a good cycle that built three
real bindings. **Every one of them binds a hand-picked membership, and nothing
checks that the membership is complete.**

| binding | what it binds | what selects the members | consequence |
|---|---|---|---|
| `check_trigger_boundary_relationship` | floor ≥ freshness | **a hand-written pair** | a fifth boundary constant is unbound by construction |
| `expected_review_export_retention_pattern` | glob ↔ active cycle + depth | **a same-prefix arithmetic assumption** | disagrees with `export_check` across a version family boundary |
| the latest-at-close rule in `AGENTS.md §5` | governed row ↔ latest measurement | **prose** | nothing executes it |

**A binding that names its members by hand is a hardcoded scope list.** That is
this project's oldest named defect class, and v0.29 reintroduced it one level up
— not in the values, but in the *membership of the bindings themselves*. The
objective of v0.30 is that **adding a new member without a binding fails
automatically.**

**The same shape exists outside `cycle_check`, and it is worse there.** The
offline Rust floor is **1.78**, pinned executably in two places
(`run:452` and `run:456` as `1.78.0`, `.github/workflows/ci.yml:305` as `1.78`),
and restated in prose in roughly a dozen more. **One of those restatements is
false.** `STATE.md:3763`, inside the live `## 7. Run reference` block, reads
`offline needs >= 1.75` — the exact claim `rust-toolchain.toml` was written to
refute, attributed to the exact version whose claim was measured false. The
toolchain file says the corrected floor "is restated in README and STATE.md §5";
**§7 was overlooked, so `STATE.md` contradicts itself in the live status
document.** And the second declared floor is worse still: **`--features net`
needs 1.86 is asserted in at least six places and executed in none.** The hosted
`net` job pins 1.91, the local net lanes use the ambient 1.91, and the `msrv` job
pins 1.78 without `--features net`. **Nothing anywhere builds on 1.86.**

**One instance of the root cause is deliberately left alone, and this file says
why.** Twenty of the fifty-one planted controls carry an `expected_line` pointing
into `tools/cycle_check.py`, and `invariant_scan.self_test` requires the emitted
finding string to match `file:line:` exactly. **Two steps below edit that file,
so roughly twenty stored line numbers must be re-derived by hand inside this
cycle.** The `find` strings and the `# Invariant R12 control site:` marker
comments already locate every site, so `expected_line` is a stored value that
could be derived — but changing the control schema touches all fifty-one
controls and rebuilds the project's core safety net. **That is its own cycle
with its own gates, not a side effect of this one.** It is recorded below with a
trigger and it is not acted on.

---

## Declared scope

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `no-release` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `tools/version_check.py` |
| `allow` | `tools/export_check.py` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `crates/store/src/sqlite.rs` |
| `allow` | `crates/**/tests/**` |
| `allow` | `shell/tests/**` |
| `allow` | `repomix.config.json` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
| `allow` | `rust-toolchain.toml` |
| `release_authority` | `Cargo.toml` |
| `release_authority` | `Cargo.lock` |
| `release_authority` | `crates/*/Cargo.toml` |
| `release_authority` | `apps/*/Cargo.toml` |
| `release_authority` | `shell/intel_shell/__init__.py` |
| `release_authority` | `shell/intel_shell/app.py` |
| `release_authority` | `CHANGELOG.md` |
| `release_authority` | `README.md` |
| `forbid` | `run` |
| `forbid` | `.github/workflows/**` |
| `forbid` | `tools/model_profiles.py` |
| `forbid` | `tools/evidence_artifacts.py` |
| `forbid` | `apps/cored/src/main.rs` |
| `forbid` | `crates/ingest/src/**` |
| `forbid` | `crates/compliance/src/**` |
| `forbid` | `crates/extract/src/**` |
| `forbid` | `crates/view/src/**` |
| `forbid` | `shell/intel_shell/**` |
| `forbid` | `config/core.json` |
| `forbid` | `config/schedule.json` |
| `forbid` | `config/subscriptions*.json` |
| `forbid` | `config/protected-artifacts.json` |
| `forbid` | `observations/**` |
| `forbid` | `docs/state-archive/**` |
| `forbid` | `fixtures/**` |
| `forbid` | `docs/cycles/**` |

**`.github/workflows/**` is forbidden, and that is new and deliberate.** The
1.86 finding has an obvious-looking fix — add a hosted job pinned to 1.86 — and
that fix changes the job matrix, the receipt and bundle population, the signed
identity count, and the deferred-audit report's expectations. **A recommended CI
job that would move the evidence topology is a scoped redesign, not an
addition.** Making the workflow forbidden converts that prohibition from prose
into something the diff gate executes.

**`docs/cycles/**` is forbidden wholesale, replacing two hand-written decade
globs.** The prior draft forbade `docs/cycles/TASKS-v0.2[0-9]-EXECUTION.md` and
`docs/cycles/PROGRESS-v0.2[0-9].md` — a hand-picked membership that left every
v0.1x closed document outside the executable gate and would have silently
stopped protecting v0.30's own pair the moment v0.31 activated, unless that
cycle's author remembered to extend the decade. That is this cycle's named root
cause sitting inside its own scope table. The scope gate's measured precedence
is **standing > release-authority > forbid > allow**, and the active runbook,
the active progress record, and `STATE.md` are standing — so the wholesale
forbid protects **every** closed cycle document while the active pair stays
editable, with no membership to maintain. The standing prohibition on editing
closed cycle documents is now **executed by the diff gate** rather than
restated beside it.

**`run` is forbidden and is also this cycle's MSRV authority.** It is an
`authorization` pin: it cannot change without breaking the manifest. **Reading it
is required; editing it is prohibited**, and its immutability is precisely what
makes it a good authority. It also means **no new lane job can be added**, so any
check built this cycle must live inside an entry point that already runs.
`./run version-check` and `./run cycle-check` both run in the local lane and in
the hosted `shell` job; nothing else is available.

**`config/protected-artifacts.json` is forbidden, with no notice of a mechanism
this time.** v0.29 registered fifteen evidence records under an explicit
authorization. **This cycle declares no manifest change and expects none.** If a
step believes it needs one, that belief is the finding: record it and stop.

**Release authorities are declared even though the intent is `no-release`.**
`README.md` and `CHANGELOG.md` are among them because the MSRV work may find a
false restatement there, and release-authority precedence is the documented
behaviour that makes them reachable while `shell/intel_shell/**` stays shut. The
two shell version files are release authorities matched by the broad shell forbid;
**that overlap is intentional and the v0.29 fixture derives it independently.**

---

## Entering state (asserted, not yet verified)

**Every line here is a hypothesis for E0. Byte figures marked *export-derived*
were computed from the delivered Repomix export with the measured
one-byte-per-file correction applied; where E0 disagrees, E0 is right.**

- v0.29 closed `no-release` at closure commit `20ddf90b…` with separate audit
  commit `d824be06…`; no version authority, tag, remote `main`, or release ref
  moved; **v0.17.0 remains published** at closing commit `4af28418…` with
  annotated tag object `df4fc3b0…`.
- Worktree clean; `ci-local` **20/20**; golden **11/11**; `invariant-scan`
  **12 rules / 51 controls**; `checklist-audit` **232/232**; Rust **146**
  workspace and **62** net (**32 ingest + 30 cored**); shell **306** collected /
  **306** passed / **0** skipped on both constrained lanes.
- Manifest: **331** pins, **191,395** bytes *(export-derived)*, **857,181** bytes
  to the 1 MiB bound; two verifications at **0.10 s / 0.10 s**.
- **The delivered review export is 2,521,787 bytes across 152 files** — this
  figure is exact, not a lower bound, because it is the export file's own size.
  That is **84.06%** of the 3,000,000-byte ceiling and **478,213** bytes of
  headroom.
- **The governed export row records 2,516,822 and the delivered export is 4,965
  bytes larger. That difference is exactly the R-CLOSE audit entry in
  `PROGRESS-v0.29.md`**, which is 4,964 bytes in the export. G4 owns what this
  means for the latest-at-close rule.
- `STATE.md` **257,422** bytes *(export-derived)*; the recorded next-archival
  boundary is **453,741**, leaving **196,319** bytes, or **≈8.71 cycles** at the
  derived 22,525 bytes/cycle rate.
- Delivered-export change across one cycle: **2,530,129 → 2,521,787 = −8,342
  bytes.** **This is one observation, not a rate**, and it disagrees in sign with
  the narrow 31,147 bytes/cycle planning denominator. E0 owns reconciling them.
- Governed rows: `ARCHITECTURE.md` **12** data rows of which **3** are
  trigger-bearing, all three carrying v0.29-identified close-time values; the
  v0.29 deferred table **17**.
- Retention glob is `2[0-6]`, correct for v0.29 and **wrong for v0.30** — and
  unlike last cycle, **`cycle-check` now rejects it automatically in both lanes**.
- The retention derivation, executed with the real function against the
  disclosed reviewer harness, **raises at `v1.0`–`v1.2` and from `v1.3`
  produces a family-scoped pattern that excludes no `v0.*` document**; the only
  check that catches the silent under-exclusion — `export_check`'s
  outside-retention-depth error — **runs in no automated lane** (operator-local
  `./run export-check` only). G3 owns confirming both behaviours with the real
  checker.
- `tools/cycle_check.py` declares **four** forward boundaries:
  `SCOPE_FORWARD_BOUNDARY` (0,23) at line 794,
  `TRIGGER_FRESHNESS_FORWARD_BOUNDARY` (0,23) and
  `TRIGGER_IDENTITY_FORWARD_BOUNDARY` (0,28) and
  `TRIGGER_FLOOR_FORWARD_BOUNDARY` (0,28) at lines 1458–1460. **One relationship
  is asserted.** `TRIGGER_IDENTITY_FORWARD_BOUNDARY` is read only at line 1600,
  inside a function reachable only above the freshness boundary.
- MSRV: offline floor **1.78** pinned at `run:452`, `run:456`, and
  `.github/workflows/ci.yml:305`; net floor **1.86** pinned nowhere.
  **`STATE.md:3763` states the offline floor as `>= 1.75`.**
- `STATE.md:3778` states `# 49 Rust + 69 shell` in the same live reference block;
  the measured populations are **146** and **306**.
- `Cargo.lock` contains **7** `icu*` entries and **no** `rust-version` metadata,
  so the 1.86 basis cannot be re-derived from the lockfile alone.
- **20** of the 51 planted controls carry an `expected_line` into
  `tools/cycle_check.py`; **6** into `crates/store/src/sqlite.rs`.
- `crates/store/src/sqlite.rs` states the archive ordering clause twice: at
  production line 301 and again in the test helper at line 1486.
- Rough activation projection: dropping the v0.27 pair removes **116,525** bytes
  *(export-derived)* and this runbook plus a progress skeleton adds roughly
  60,000. **Arithmetic on a pre-change tree is not a measurement** — the v0.28
  projection missed by 154,482 bytes and this one is labelled the same way.

---

## Drafted gates

| Gate | Where | Hypothesis |
|---|---|---|
| **G1** [P1] | `tools/cycle_check.py:794,1458-1472,1600,1980-2003` | **The boundary relationship covers two of four constants and nothing notices the other two.** Enumerate every `*_FORWARD_BOUNDARY` and state, for each pair, whether an ordering relation is load-bearing and why. Then **demonstrate by execution** what the real checker does today when the identity boundary is moved below the freshness boundary in a throwaway copy. **Record whether the identity gate becomes unreachable, silently always-on, or something else** — if that constant can declare a boundary no input can observe, the finding is a rule that cannot fire, not a traceback. |
| **G2** [P1] | `run`; `.github/workflows/ci.yml`; `rust-toolchain.toml`; `README.md`; `STATE.md` | **Two declared Rust floors: one enforced and misstated, one stated and unenforced.** Enumerate every site stating either floor and classify each as executable pin, current restatement, or dated historical record. **Confirm by execution that `STATE.md:3763` is a live restatement and is false**, and **confirm by search that no lane builds `--features net` on 1.86.** Then state plainly whether a general scan can separate current restatements from historical ones **without a hand-maintained exemption list**, and if it cannot, say so. |
| **G3** [P2] | `tools/cycle_check.py:1037-1074`; `tools/export_check.py:87-126` | **Two retention derivations agree only inside one version family, and they disagree in both directions across its boundary.** `export_check` sorts every runbook by version tuple and keeps the last three; `cycle_check` performs same-prefix arithmetic on the final component. Executed with the real functions against the disclosed reviewer harness: **`v1.0`–`v1.2` raise and block activation loudly — the good failure — while `v1.3` succeeds with a family-scoped pattern that excludes no `v0.*` document**, a silent under-exclusion that would re-admit roughly twenty-seven closed cycle documents to the export at once, and the only check that catches it runs in no automated lane. **Settle by execution against throwaway trees carrying `v1.0` and `v1.3` active declarations** — run the real `cycle-check` and the real `export-check` in each tree and record what each does, and which lane, if any, would have caught each behaviour. The reviewer's executions used the harness and **are not evidence.** |
| **G4** [P2] | `AGENTS.md §5`; `tools/cycle_check.py:1544-1586`; `ARCHITECTURE.md` export row | **A governance rule shipped with nothing executing it, and it may not be satisfiable as written.** Settle **by exhaustive search** whether any checker validates a governed row's measured *content* rather than its date and cycle literal. Then settle the fixed point: the export row is written in the closing commit, the audit entry is appended after it, and the delivered export exceeds the row by exactly the size of that entry. **Determine whether "latest available at close" can be bound to the cycle's own progress record, and state the residual as a named bounded quantity rather than leaving it undisclosed.** |
| **G5** [P2] | v0.28 and v0.29 closing records; `tools/export_check.py` | **The recorded headroom estimate and the observed export dynamics have opposite signs.** One derived denominator says 31,147 bytes/cycle of growth; the delivered-to-delivered observation says −8,342. **Derive the third data point at this cycle's activation and state plainly how many observations exist and what they do and do not support.** Then record which of the two archival triggers — the export ceiling or the 453,741-byte State boundary — is nearer, in cycles. |
| **G6** [P3] | `crates/store/src/sqlite.rs:296-312,1479-1494` | **The ordering is declared three times: production SQL, the test helper's copy, and the Rust comparator.** Confirm the two SQL clauses are byte-identical today. Then determine whether a single compile-time declaration is achievable **without runtime formatting and without allocation**, and if it is not, say so and leave the duplication in place with the reason recorded. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate.

- **🤖 = Codex executes and self-verifies end to end** — no publication, no push
  to `main`, no ref creation or deletion **in the working repository**.
- **🧑 = exactly one named operator action or decision.**

**Interpretive rules, binding throughout.** An exit code of 0 from a construction
the checker never examined is **not measured**. A measurement that disagrees with
an acceptance criterion is **reported as measured**; the criterion is what gets
corrected. **Two declarations of one fact are a defect until something binds
them, and a binding whose membership is written by hand is itself a declaration
that needs binding.** A rule that cannot fail has not passed: every step here
demonstrates its rejection path against real output before its acceptance path.

**The planted-control line-number hazard, stated in advance so no step is
surprised by it.** `invariant_scan.self_test` compares the emitted finding
against `expected_file:expected_line:` exactly. Twenty controls point into
`tools/cycle_check.py` and six into `crates/store/src/sqlite.rs`. **Any insertion
shifts every control site below it.** Re-derive the affected `expected_line`
values from the real self-test output after each edit, and **record how many were
re-derived** — that number is this cycle's evidence for the deferred row that
records the hazard. Do not fix the schema; that is out of scope.

**Dependency gates.** Step 1 blocks everything. Steps 2, 3, and 4 are independent
of each other, but **Steps 2 and 4 both edit `tools/cycle_check.py`**, so
whichever runs second re-derives the control line numbers the first shifted.
Step 5 is independent and **may be skipped entirely under its own decision
gate.** Step 6 is blocked by every preceding implementation step; Step 7 by
Step 6.

**No amendment obligation is known in advance.** Unlike v0.29, this cycle
declares no evidence directory that cannot exist yet and no manifest change. If
an amendment becomes necessary, it takes the established form: a dated
`## Runbook amendments` entry in the same commit that first needs it. **This is
notice of the mechanism, not permission for a scope change.**

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and record the measured refs **without asserting a literal `origin/main`
hash in `STATE.md`'s header**. Commit **only** this runbook at
`docs/cycles/TASKS-v0.30-EXECUTION.md` — including its `## Declared scope` table
— the `AGENTS.md` header moving the active declaration from v0.29 to v0.30, a new
`docs/cycles/PROGRESS-v0.30.md`, and the `repomix.config.json` retention edit.

**This file deliberately contains no reserved cycle-closing heading and no blank
closing template.** v0.28 and v0.29 both failed activation on exactly that, twice,
and both failures were this reviewer's. The closing record is appended when the
cycle closes.

**The retention glob must move from `2[0-6]` to `2[0-7]`, and this time the
checker will tell you.** v0.29's binding derives the expected pattern from the
active declaration and `CYCLE_RETENTION_DEPTH` and runs in both lanes. **Record
the exact rejection text before making the edit** — that is the first measured
proof that v0.29's Step 2 works on a cycle it did not author, and it is worth
more than the edit itself.

**Every governed row below already carries `v0.30` and a date**, so activation is
green under the identity rule. **Those dates are carried-forward hypotheses and
E0 rewrites every one of them with v0.30 measurements.** The three
trigger-bearing rows in `ARCHITECTURE.md` still name v0.29 and **must be
remeasured at activation or the identity gate rejects them** — that is v0.29's
reviewer error 6, and it is named here so it is not repeated a third time.

### Global definition of done

Protected hashes exact; all **331** pins match; **golden 11/11 byte-identical**;
`./run version-check` green; zero rustc warnings on offline and net builds; all
Rust tests green; all shell tests green under Python 3.11 **and** 3.12; shell
results recorded as collected / passed / skipped with every skip named and
compared by `tools/test_population.py`, never as a bare `N/N`; clippy, fmt,
ShellCheck, floor byte-compilation, and locked Rust 1.78 green.

**`checklist-audit` and the export ceiling are this cycle's two controls.** The
audit total must not fall. The export must stay under 3,000,000 bytes at every
measured point, and **every export figure recorded must name the tree it was
measured on.**

---

## Deferred means deferred

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.30 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | v0.30 · 2026-07-31 — hypothesis carried forward; no publisher request or concurrent harvester is expected in a cycle whose scope forbids the ingest and scheduler paths | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.30 · 2026-07-31 — hypothesis carried forward; no live outage, publisher request, or newly usable last-known-good policy is expected | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.30 · 2026-07-31 — hypothesis carried forward; `crates/ingest/src/**` is forbidden and no live request is authorized | none — the gap stays recorded |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.30 · 2026-07-31 — hypothesis carried forward; the mapping path is forbidden and no connector review is scheduled | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.30 · 2026-07-31 — hypothesis carried forward; the v0.27 sequential two-origin result remains the latest live execution | none — complete, do not re-exercise |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | v0.30 · 2026-07-31 — hypothesis carried forward; the bounded design exists and execution authorization was explicitly withheld from this cycle | none — design complete, execution separately gated |
| Postgres / pgvector / multi-host seam | unchanged | v0.30 · 2026-07-31 — hypothesis carried forward; single-writer SQLite and single-host topology are unchanged | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.30 · 2026-07-31 — hypothesis carried forward; only the first-party shell path is exercised and no shell-replacement invariance is claimed | none |
| L2 forced-command wrapper | an operator server session | v0.30 · 2026-07-31 — hypothesis carried forward; no operator server-administration session is scheduled | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.30 · 2026-07-31 — hypothesis carried forward; the closing invariant self-test is expected to expose no spelling outside registered vocabulary | none |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.30 · 2026-07-31 — hypothesis carried forward; no compliance review is in progress and no admission decision is pending | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.30 · 2026-07-31 — hypothesis carried forward; no publication authorization exists and no historical ref is touched | none — **no historical ref touched** |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.30 · 2026-07-31 — hypothesis carried forward; both historical tags remain unpublished so the trigger is absent | none — **the flag stays** |
| Manifest retention/indexing | 1 MiB manifest, or two consecutive `verify-artifacts` runs ≥1.00 s | v0.30 · 2026-07-31 — hypothesis carried forward; the manifest is unchanged at 331 pins and this cycle declares no registration | **Step 1 and Step 6 — re-measured only** |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.30 · 2026-07-31 — hypothesis carried forward; `shell/intel_shell/**` is forbidden except for release-authority precedence on the two version files | none — recorded, not acted on |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.30 · 2026-07-31 — hypothesis carried forward; the standing prose criteria are applied and no decision declares them insufficient | none — recorded, not acted on |
| Second `STATE.md` archival | the export ceiling trigger fires, or `STATE.md` reaches 453,741 bytes | v0.30 · 2026-07-31 — hypothesis carried forward; State is expected near 257,422 bytes leaving roughly 196,319, and the export is expected well beneath its ceiling | **Step 1 — boundary re-derived; no archive** |
| Planted-control line numbers re-derived by hand | a control-schema change, or a cycle in which the re-derived count exceeds the controls it protects | v0.30 · 2026-07-31 — hypothesis carried forward; 20 controls point into `tools/cycle_check.py` and 6 into `crates/store/src/sqlite.rs`, and two steps edit the former | none — recorded, not acted on |
| Retention derivation across a version-family boundary | an active cycle whose name is not of the form `v0.<n>` — raising at `v1.0`–`v1.2`, silently under-excluding from `v1.3` onward | v0.30 · 2026-07-31 — hypothesis carried forward; every cycle to date is `v0.<n>` so neither behaviour is reachable; reviewer-side execution of the real derivation exhibited both, and the only check catching the silent case runs in no automated lane | **Step 1 — settled by execution in both trees; recorded, not fixed** |
| Published-release divergence with no governed trigger | an operator decision that the distance between published v0.17.0 and the working head warrants a governed row | v0.30 · 2026-07-31 — hypothesis carried forward; the export ceiling and the manifest are governed by triggers and release staleness is not | none — recorded for **Step 7** |

---

## Step 1 · E0 — Rebuild the entering state and settle six gates 🤖

**Objective.** Confirm HEAD is green and settle G1–G6. **Every assertion in
`## Entering state` is a hypothesis.** Report the measured value, especially where
it differs. The one-byte-per-file export correction has been applied to the
figures above, so they should now be exact rather than low — **if they are still
low, that correction is wrong and saying so is the finding.**

**Decision gate.** If the worktree is dirty, if v0.29's closure and audit commits
are not where the entering state places them, or if any local gate fails at
entry, **record and stop.**

**Acceptance criteria.**

- All 20 `ci-local` jobs pass; invariant **12/51**; golden **11/11**; **331** pins
  verified twice with both real times recorded; both Python lanes reported as
  collected/passed/skipped via `tools/test_population.py`.
- G1 settled **by execution**, with the exact behaviour of a lowered identity
  boundary recorded verbatim.
- G2 settled **by execution and exhaustive search**, with every floor-stating
  site enumerated and classified, and with an explicit ruling on whether a
  general scan is achievable without a hand-maintained list.
- G3 settled **by execution** against throwaway `v1.0` **and `v1.3`** trees,
  confirming or refuting the reviewer's harness executions in **both** the
  raising and the silently under-excluding case, and recording which lane, if
  any, would have caught each.
- G4 settled **by exhaustive search**, with the fixed-point residual stated as an
  exact byte quantity against a named tree.
- G5 settled with the activation export derived and the number of available
  observations stated plainly.
- G6 settled with a stated ruling on whether one compile-time declaration is
  achievable without allocation.
- The activation rejection text produced by the stale retention glob is recorded
  verbatim, as the first independent proof that the prior cycle's binding works.
- The deferred table's 20 rows are rewritten with **v0.30** measured
  observations, and the three trigger-bearing `ARCHITECTURE.md` rows carry
  v0.30 close-adjacent measurements.

**Done when** every gate carries a measured answer and the entering state is
either confirmed or corrected in `STATE.md`.

- [ ] **E0**

---

## Step 2 · BOUNDARY-COVER — Bind the family, not the pair 🤖

**Objective.** Make it impossible to add a forward-boundary constant without
declaring its relationship, and assert the identity relationship that is
load-bearing today and unasserted.

**Decision gate.** If G1 showed that a lowered identity boundary produces a
reachable defect rather than an unobservable declaration, **that is a live defect
and not a latent one** — record the reclassification and treat it at P1.

**Acceptance criteria.**

- Every module constant whose name ends in `_FORWARD_BOUNDARY` is **enumerated by
  derivation**, never listed by hand. A constant added without a declared
  relationship must fail automatically, and that is the property being built.
- **The derivation's namespace is stated as a recorded bound.** Either the
  enumeration scans every module under `tools/`, or it is module-scoped and says
  so explicitly in the check's own text — **a bounded derivation that does not
  name its bound is the finding, not a detail.** A `*_FORWARD_BOUNDARY` constant
  landing outside the derived namespace must be either impossible under the
  chosen derivation or named as outside the binding with the residual recorded.
- The required relations are **declared, because semantics cannot be derived** —
  but the declaration is a registry the completeness check reads, not a chain of
  hand-written comparisons. Constants with no required relation are registered as
  independent **with a stated reason**, and an unregistered constant is an error.
- The identity boundary's required relation to the freshness boundary is
  asserted. A constant that can declare a boundary no input can observe is a rule
  that cannot fire, which is the outcome being designed out.
- Two registered `R12` controls, each demonstrated **rejecting before
  accepting**: the existing reversed-pair control continues to fire, and a new
  control injects an unregistered boundary constant and confirms the completeness
  check names it.
- The exhaustive-pair collapse and the initialized populations shipped by the
  prior cycle are unchanged, confirmed by test.
- Every `expected_line` shifted by this edit is re-derived from real self-test
  output and the count is recorded.

**Done when** adding an unregistered boundary constant fails automatically,
demonstrated by execution rather than by argument.

- [ ] **BOUNDARY-COVER**

---

## Step 3 · FLOOR-BIND — One false floor, one unexecuted floor 🧑🤖

**Objective.** Correct the false offline-floor claim, bind the restatements to the
executable pins, and put the unexecuted 1.86 claim in front of the operator
rather than quietly fixing or quietly keeping it.

**Decision gate.** `run` and `.github/workflows/**` are **forbidden.** The
offline pins are read, never written. **If any part of this step would add a
hosted job, change a toolchain pin, or alter the evidence topology, stop and
record it.**

**Why this is not documentation hygiene.** The false line is not a typo. It is
the exact claim `rust-toolchain.toml` exists to refute, in the live status
document, attributed to the release whose claim was measured false — and the
toolchain file states that the correction was applied to two files while a third
was missed. **This is the project's own flagship failure, still resident, three
years of cycles later.**

**🧑 The operator's decision, and only the operator's.** The `--features net`
floor of 1.86 is asserted in at least six places and executed in none. Three
outcomes, none defaulted:

- **Bind what is bindable and record 1.86 as an unexecuted claim** — correct the
  false offline restatement, bind every offline restatement to the executable
  pins, and add the net floor to the deferred table with a trigger. The cheapest
  honest outcome.
- **Restate 1.86 as derived rather than guaranteed** — rewrite every net-floor
  claim to say it follows from a dependency's declared metadata rather than from
  anything this project builds, and record why the lockfile alone cannot
  re-derive it.
- **Authorize a scoped later cycle to make 1.86 executable** — a design decision
  about the evidence topology, delivered later, not here.

**Acceptance criteria.**

- The offline floor is **derived from the executable pins**, which are read and
  compared to each other after normalization; the two pins are written in
  different string forms today and a check that tolerates that silently is not a
  binding.
- **An authority file yielding zero extracted pins is an error, not an empty
  set.** The offline pins are extracted from a bash script and a workflow file
  by pattern, and `version_check.py`'s AST-and-tomllib precedent does not
  transfer to either; format drift that empties the extraction must fail
  loudly, **demonstrated by a planted control**, or the binding passes
  vacuously — the silent no-op family this project has caught four times.
- Every current restatement of the offline floor states the derived value.
  **`STATE.md:3763` is corrected in the house forward-correction form**, not
  deleted — the false claim's history is the most valuable thing about it.
- Dated historical records that quote the refuted 1.75 figure **must keep quoting
  it and must not be rewritten.** If the scan cannot distinguish them without a
  hand-maintained exemption list, **say so plainly and record the list as a
  named permanent obligation** rather than presenting it as derived.
- The binding lives in an entry point that already runs in both lanes. **A check
  that requires a new lane job cannot ship**, because the lane definition is an
  authorization pin.
- A registered `R12` control proves a stale restatement is rejected.
  **Demonstrate the rejection before the acceptance.**
- `STATE.md:3778`'s stale `49 Rust + 69 shell` figures are corrected in the same
  pass, or the reason for leaving them is recorded.
- The operator's decision on the net floor is recorded with its date and reason.

**Done when** a restatement that disagrees with the executable pins fails
automatically, and the false line is corrected rather than removed.

- [ ] **FLOOR-BIND**

---

## Step 4 · MARGIN-BIND — Make the latest-at-close rule executable and honest 🤖

**Objective.** Give the governed-row measurement rule a control, and disclose the
fixed point it cannot escape.

**Decision gate.** `docs/state-archive/**` and `config/protected-artifacts.json`
are **forbidden.** This step binds how a row is written; it archives nothing and
registers nothing.

**The fixed point, stated so the acceptance criteria are satisfiable.** A
governed export row is written in the closing commit. The audit entry is appended
after it. **No record inside the repository can carry a measurement of a tree
that contains that record.** The rule as written therefore cannot be satisfied in
the strict sense, and the delivered export exceeds the recorded value by exactly
the size of the appended entry, every cycle, by construction. **A criterion that
disagrees with a measurement is the criterion that gets corrected.**

**Acceptance criteria.**

- The governed export figure is bound to the cycle's own progress record: the
  live row's value must equal the last export figure that record contains.
  **A second, independent derivation the first cannot satisfy by construction** —
  a row asserting itself is not a binding.
- **The empty-record state is named and demonstrated.** At activation, and
  mid-cycle before any export figure lands in the named progress record, the
  binding has no referent. The rule states which path that state takes — an
  error, or a named exemption with a stated reason — and the chosen path is
  **demonstrated by execution** against a record containing no export figure.
  **A vacuous pass on an empty record is the defect being removed.**
- The rule in the contract is amended to state the fixed point explicitly: the
  measurement is taken on the last tree measurable when the row is written, the
  appended audit entry is a known bounded delta, and **that delta is named and
  recorded rather than left as an undisclosed gap.** State it symmetrically so a
  later cycle cannot argue either direction opportunistically.
- A registered `R12` control proves a governed row carrying a superseded figure
  is rejected. **Demonstrate the rejection before the acceptance.**
- Governed rows whose subject is not an export figure are **explicitly out of
  scope or explicitly in it** — an ambiguous rule is the defect being removed,
  and a rule that silently applies to rows it cannot check is worse than one that
  says what it covers.
- Every `expected_line` shifted by this edit is re-derived from real self-test
  output and the count is recorded.

**Done when** a governed row that lags its own cycle's records fails
automatically, and the residual the rule cannot close is written down.

- [ ] **MARGIN-BIND**

---

## Step 5 · ORDER-CONST — One declaration of one ordering 🤖

**Objective.** Reduce the archive ordering from three declarations to two, so the
cross-implementation binding compares SQL against Rust rather than against a
copy of itself.

**Decision gate.** Blocked by nothing and **skippable in full.** If G6 concluded
that a single compile-time declaration requires runtime formatting or
allocation, **record that and stop** — the existing binding already catches
production-side divergence, which the prior cycle demonstrated, and a worse
implementation bought for tidiness is not an improvement. `apps/cored/src/main.rs`
and `crates/ingest/src/**` are forbidden: this step reaches the store and its
tests only.

**The blast radius is bounded and every record must say so.** The field is
observational, detection never fails the poll, and a divergence produces a
**wrong raw boundary string in one internal diagnostic** — not a dropped filing,
not data loss. **Do not inflate this.**

**Acceptance criteria.**

- The ordering clause is stated once and expanded at compile time. **No runtime
  formatting, no allocation, no behavioural change to any query.**
- The cross-ordering test still compares each production boundary against the
  other implementation's derived result, and still fails when the production SQL
  is mutated alone. **Demonstrate that rejection again after the change** — a
  refactor that quietly weakens a binding is the failure mode here.
- The existing misordered-window test is unchanged and still passes.
- Golden stays **11/11 byte-identical** and SEC identity stays **200 kept / 0
  dropped**. **If either moves, stop.**
- The `/ingest` response shape and every `/v1/*` value domain are unchanged, and
  both are recorded explicitly for the closing decision.
- Every `expected_line` shifted by this edit is re-derived and the count recorded.

**Done when** one declaration produces both call sites, or the reason it cannot
is recorded and nothing changed.

- [ ] **ORDER-CONST**

---

## Step 6 · RE-MEASURE — Hosted verification on a neutral branch 🤖

**Objective.** Produce authenticated hosted evidence at an exact candidate on a
neutral ref, without publishing.

**Decision gate.** Blocked by Steps 2–5. No push to `main`, no tag. **The
workflow is forbidden**, so the job matrix, the receipt population, and the
signed identity count must be identical to the prior cycle's; **if any of them
moves, that is a finding and not a result.**

**Acceptance criteria.**

- All seven executable hosted jobs pass at the exact candidate; the
  dependency-drift job skips under its declared report-only condition.
- Attestations required; every signed identity accepted, zero rejected; the
  complete runner matrix found.
- Both shell lanes compared by `tools/test_population.py` with comparator-derived
  `collected`, `equivalent`, and `equivalent_passed`. **Every number written is
  the comparator's output, never transcribed from a log.**
- **331** pins verified on the candidate, unchanged; golden **11/11**.
- **No manifest registration occurs.** This cycle declares none and expects none.

**Done when** the candidate carries release-grade authenticated evidence.

- [ ] **RE-MEASURE**

---

## Step 7 · R-CLOSE 🧑🤖

**Objective.** Close v0.30 with an explicit, reasoned disposition.

**The drafted intent is `no-release`, and the reason to look harder is
accumulating.** Published v0.17.0 still derives the incoming coverage boundary
positionally; the correction and two cycles of bindings now ride unpublished
behind it. **Nothing in this project governs that distance.** The export ceiling
has a trigger, the manifest has a trigger, the shell warning has a trigger, and
the gap between the published artifact and the working head has none — which
means it can grow indefinitely without any record ever being obliged to notice.
**That is the same shape as every finding in this cycle: a quantity nothing
watches.**

**🧑 The operator's decision, and only the operator's.** Publication
authorization is a separate explicit act and is **not** implied by this runbook,
by green gates, or by hosted evidence. Three options, stated so none is a
default:

- **`no-release`** — close v0.30 on its own record, and **record the reason the
  distance is still acceptable** rather than inheriting it from last cycle.
- **`release` at patch** — ship the order-independent boundary derivation and
  this cycle's corrections. No route, response shape, `/v1/*` value domain,
  dependency, or schema moves, so the named-surface rule and the public
  value-domain criterion both stay unfired. **This requires a stated reason of
  its own** and may not be inherited from "the gates are green."
- **Add a governed trigger for release divergence and close `no-release`** — put
  the distance under the same discipline as every other governed quantity, with a
  stated trigger and a dated observation that it has not fired, and let a later
  cycle act on it. **Recording is not doing, and a trigger is not an obligation
  to publish.**

**Acceptance criteria.**

- The closing record names `Cycle closed`, the dated `Release disposition`, and —
  if `release` — `Release` and `Release commit:` under the two-commit tagged
  closing protocol.
- Every declared permission is reconciled as used or unused, by path. **The newly
  forbidden workflow path and the wholesale `docs/cycles/**` forbid are
  reconciled explicitly**, because a prohibition nobody checks is the thing this
  cycle is about.
- Every gate G1–G6 has a recorded measured answer, including G2's operator
  outcome and G6's skip-or-implement ruling.
- **The four reviewer errors in this file's header are preserved in the cycle
  record as reviewer errors**, not restated as findings and not quietly dropped.
- The total number of `expected_line` values re-derived across the cycle is
  recorded, as evidence for the deferred row that names the hazard.
- `STATE.md` records the final export figure against the ceiling **naming its
  tree**, the `checklist-audit` control, and the derived growth observations with
  their count stated.

**Done when** the disposition is authorized, recorded, and measured.

- [ ] **R-CLOSE**

---

## Cycle checklist

- [ ] Worktree clean at entry; v0.29 closure and audit commits where E0 measures them
- [ ] Stale retention glob rejection recorded verbatim before the activation edit
- [ ] Every entering-state hypothesis measured and confirmed or corrected
- [ ] G1–G6 each carry a measured answer; G1, G2, and G3 answered **by execution**
- [ ] Every new binding demonstrated **rejecting** before demonstrated passing
- [ ] No binding implemented as a self-consistency assertion
- [ ] No binding whose membership is written by hand rather than derived
- [ ] No expected value hardcoded in any test added or edited this cycle
- [ ] Re-derived planted-control line numbers counted and recorded at every step
- [ ] No closed cycle document edited, moved, or deleted
- [ ] Workflow file byte-identical across the complete cycle diff
- [ ] Manifest byte-identical across the complete cycle diff
- [ ] `checklist-audit` total does not fall; every figure recorded
- [ ] Export under 3,000,000 bytes at every measured point, each naming its tree
- [ ] Golden **11/11** byte-identical at every step
- [ ] SEC identity **200 kept / 0 dropped** unchanged
- [ ] Both Python lanes reported as collected/passed/skipped, comparator-derived
- [ ] Deferred table rows all carry v0.30-identified observations
- [ ] No publisher request, no scheduler run, no cadence change
- [ ] Four reviewer errors preserved as such in the cycle record

---

## Standing prohibitions

- **No publisher request and no scheduler run.** The bounded window design exists
  and its execution authorization was explicitly withheld from this cycle.
- **No edit to `.github/workflows/**`.** The 1.86 finding has an obvious-looking
  fix that would move the evidence topology; that is a scoped redesign for a
  later cycle and an operator decision, not a step's initiative.
- **No edit to `run` or `tools/model_profiles.py`** — both are `authorization`
  pins. `run` is read as the MSRV authority and never written.
- **No manifest edit.** This cycle declares none.
- **No closed cycle document is edited, moved, renamed, or deleted** — a
  prohibition now **executed by the wholesale `docs/cycles/**` forbid** through
  the diff gate, with the active pair reachable only through standing
  precedence, rather than restated beside the gate it depends on.
- **No second `STATE.md` archival.** The boundary is re-derived; recording is not
  doing.
- **No push to `main`, no tag, no ref creation or deletion** before the
  authorized closing action.
- **No hardcoded expected value** in any test written or edited this cycle, and
  **no hand-written membership list** in any binding built this cycle.
- **No binding that a single implementation can satisfy by construction.**
- **No rule ships without a demonstrated failing case.**
- **No rewriting of a dated historical record that quotes a refuted figure.** The
  refuted 1.75 claim must survive in every dated context that quotes it; only
  live restatements are corrected.
- **No retraction is proposed** without a twice-verified measured false claim in
  an immutable published record. **The count stands at three.** The false
  `STATE.md:3763` line is a live-document correction, not a retraction candidate,
  and **this reviewer is not proposing one** — a false retraction proposal is
  already on this project's record as a reviewer error.

---

## Provenance of this draft

**Read, not measured:** the Codex v0.29 report; `TASKS-v0.29-EXECUTION.md` in
full including its ten amendments and closing record; `PROGRESS-v0.29.md` in
full; `AGENTS.md` §§0 and 5; `ARCHITECTURE.md` §6's dispositions table and §7;
`STATE.md` header and §7.

**Measured against the 2026-07-31 delivered export, by path and line:** export
size **2,521,787** bytes and **152** files, exact; the R-CLOSE audit entry at
**4,964** export bytes against a **4,965**-byte export delta, which is how the
one-byte-per-file correction was proven; `STATE.md` at 257,421 export bytes and
`config/protected-artifacts.json` at 191,394, each one byte below its recorded
value, which is how it was proven twice more; **12** rules and **51**
`fail_before` controls with R12 at **23**; **331** `pinned_files[]` of which
exactly **15** carry the v0.29 evidence paths, in a **2**-artifact schema-2
manifest; `run` `ci_local_jobs` at **20** with no export-check; `ci.yml` with
seven jobs, `./run version-check` at line 380 and `./run cycle-check` at line
387, and zero `export` occurrences; `cycle_check.py:1037-1074` the retention
derivation, `:1458-1472` the boundary constants and relationship check, `:1600`
the identity gate, `:1959-2020` the initialized populations and both forward
gates; `export_check.py:87-126` the version-sorted retention set;
`sqlite.rs:34-39` the comparator, `:296-312` the production derivation,
`:1470-1550` the cross-ordering test and its duplicated clause;
`repomix.config.json` retention glob at `2[0-6]`; `Cargo.lock` with 7 `icu*`
entries and no `rust-version` key; the MSRV sites enumerated in G2; the
per-control `expected_line` distribution at **20** into `cycle_check.py` and
**6** into `sqlite.rs`; `checklist-audit` reconciled as 29 × 8 = **232** through
`CHECKED_RE` applied to the three retained runbooks.

**Measured by execution against the disclosed reviewer harness (second review,
2026-07-31).** The harness is an export-derived tree: the 152 files extracted
from the delivered export, **three stubbed evidence artifacts** created solely
to satisfy cycle-identity resolution at import, and **no git history** — so the
diff gate, commit resolution, tag verification, and every git-dependent
`checklist-audit` sub-check **never executed**, and no result below claims they
did. What did execute, with the real functions imported from the real files:
the declared-scope parse of this draft (one line-anchored heading, zero errors,
all seventeen derived release authorities covered); the trigger
freshness/identity checks (**20** deferral rows green; the three
`ARCHITECTURE.md` rows rejecting with their v0.29 observations, exactly as the
activation section predicts); deferral step assignments and cross-step
value-criteria checks, zero errors; carry-forward, **0 dropped**; the boundary
relationship check; the stale-glob rejection at an activated v0.30, recorded
verbatim; and the retention derivation across `v0.29`–`v0.43`, `v1.0`–`v1.3`,
which raised below `v1.3` and silently under-excluded from it. **These
executions confirm the draft's construction; they are not the cycle's
evidence.** E0's full run against the real tree is the evidence of record.
Whether the harness should become a sanctioned, recorded construction — or
cycle-identity resolution should defer evidence reads past import so no
scaffold is needed — **remains an open operator decision outside this cycle's
scope**, deliberately not added to the deferred table without authorization.

**Measured by reconstruction, not against the repository:** the activation
export projection, which is arithmetic on a pre-change tree and missed by
154,482 bytes the last time it was attempted. The retention pattern's
behaviour across future cycles was **initially** produced by re-implementing
the derivation in a standalone script — reviewer error 2 — and has since been
re-executed with the real function under the disclosed harness above; **it
remains not evidence until G3 runs the real checker against throwaway trees.**

**Asserted and not verified:** every line under `## Entering state`; the claim
that no lane builds `--features net` on 1.86, which follows from reading three
toolchain pins and is **G2's to confirm by search**; the claim that no checker
validates a governed row's measured content, which follows from reading two
assertions and is **G4's to confirm exhaustively**.

**Not verifiable by this reviewer at all:** that no historical cycle document was
moved, edited, or deleted. Retention depth 3 exports only v0.27–v0.29, so v0.1
through v0.26 are outside this reviewer's reach and that claim rests on
`checklist-audit` and on Codex's measurement. **Said plainly rather than left
implied**, as it was last cycle.

**This revision folds in six operator-approved findings from the second
review of 2026-07-31:** the two-tree G3 execution matrix and sharpened
retention trigger; the MARGIN-BIND empty-record criterion; the FLOOR-BIND
zero-extraction criterion; the Step 2 derivation-namespace bound; the wholesale
derived `docs/cycles/**` forbid replacing two decade globs; and this provenance
disclosure with reviewer error 4.

**Four reviewer errors are recorded in this file's header** rather than here,
because a provenance note is where a reader looks last and an error is what they
should see first.
