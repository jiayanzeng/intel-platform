# TASKS-v0.32-EXECUTION.md — measure the artifact, not the sentence about it

**Three reviewer errors, all mine, recorded before anything else.**

1. **v0.31 Step 4 asked for a partition over "every tracked file containing a
   Rust floor literal" and never asked what could count as one.** The shipped
   detector derives its literal set from the *currently correct* values — 1.78
   and 1.86 — so it can only see files that already agree. A tracked file
   asserting `offline needs >= 1.75`, which is the exact live defect the whole
   MSRV thread began with in v0.30, produces zero matches and is never
   classified. **The partition proves that every file stating the right floor
   belongs to a declared class; it cannot see a file stating a wrong one.**
   Specifying a partition without specifying its detector's domain is my error.
   G2 settles it; Step 3 owns it.
2. **v0.31 Step 6 enumerated the version authorities by hand, and the list is
   short by one.** I wrote "the Rust package, Python package, public FastAPI
   literal, `STATE.md` header, and newest `CHANGELOG.md` release" — five names
   copied from `ARCHITECTURE.md` §8. `README.md` is a declared
   `release_authority` in a scope table I also wrote, it was edited during this
   release, and its first line states `v0.17.1`. Nothing checks it. **I wrote a
   hardcoded scope list into the acceptance criteria of a project whose oldest
   named defect class is hardcoded scope lists.** G3 settles it; Step 4 owns it.
3. **v0.31 Step 7 dropped the evidence-ref requirement that v0.29 and v0.30 both
   carried.** Those runbooks named the ref shape — a fresh
   `codex/v0.<N>-evidence-<sha7>` per candidate. Restructuring Step 7 for the
   release shape, I wrote only "the candidate **is** the release commit" and said
   nothing about where it is pushed. The published v0.17.1 candidate was
   authenticated on the reused branch `refs/heads/codex/v0.23-action-migration`,
   so **every signed receipt for this release binds a source-ref identity naming
   a cycle from eight cycles ago.** The attestations are sound — they bind the
   exact candidate digest — but the ref is mutable, reusable, and now
   self-describing of the wrong thing. G4 settles it; Step 6 owns the convention.

---

**The named root cause for this cycle.** v0.31 built four real bindings, and
where a governed fact was directly available in the repository they still read
what the repository *says* rather than what it *is*.

| governed quantity | how it is available | what v0.31 does | consequence |
|---|---|---|---|
| `STATE.md` archival boundary | **the file's own byte count** | a hand-written figure in a prose cell | the nearest trigger of all is measured by nobody |
| protected-manifest 1 MiB bound | **the file's own byte count** | a hand-written figure in a prose cell | same shape, more headroom |
| review-export ceiling | not in-repo; the export is generated | written figure bound to the ceiling, **bound disclosed** | correct — this one is honest |
| Rust floor across tracked files | the tracked files themselves | read through a window cut to the shape of the right answer | a wrong floor is invisible |
| release version restatements | the tracked files themselves | five names written by hand | a sixth restatement drifts silently |

**Two of these quantities are plain byte counts of tracked files, and the
project writes them down instead of reading them.** The export ceiling is the
one case where a written figure is the only option, and v0.31 correctly says so
in the check's own text. That correctness makes the other two harder to defend,
not easier. The objective of v0.32 is that **where the artifact is present, the
artifact is what gets measured.**

---

## Declared scope

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `no-release` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `tools/export_check.py` |
| `allow` | `tools/version_check.py` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `shell/tests/**` |
| `allow` | `repomix.config.json` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
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
| `forbid` | `apps/**/src/**` |
| `forbid` | `crates/**/src/**` |
| `forbid` | `crates/**/examples/**` |
| `forbid` | `crates/**/tests/**` |
| `forbid` | `shell/intel_shell/**` |
| `forbid` | `config/core.json` |
| `forbid` | `config/schedule.json` |
| `forbid` | `config/entities.json` |
| `forbid` | `config/subscriptions*.json` |
| `forbid` | `config/protected-artifacts.json` |
| `forbid` | `observations/**` |
| `forbid` | `docs/state-archive/**` |
| `forbid` | `fixtures/**` |
| `forbid` | `docs/cycles/**` |

**`disposition_intent` is `no-release`, and this time that is not a
foreclosure.** v0.31's third reviewer error was that ordering made `release`
unavailable while presenting it as a choice. Here `release` is unavailable
because **every production source path is forbidden and no step is scheduled to
change behaviour** — the scope table says so and the diff gate executes it. That
is a declared constraint, not an accident of step order. **If any step measures
a production behaviour change, that measurement is the finding: record it, stop,
and the disposition decision reopens before Step 6 rather than at Step 7.**

**Release authorities are declared even under `no-release` intent.** Step 4 may
find a version restatement that disagrees, and `README.md` and `CHANGELOG.md`
must be reachable to correct one. Release-authority precedence over `forbid` is
the documented behaviour that makes the two shell version files reachable while
`shell/intel_shell/**` otherwise stays shut; v0.31 exercised exactly that path
and reconciled it explicitly.

**`config/protected-artifacts.json` is forbidden and is also Step 2's
measurement subject.** Reading its byte count is required; editing it is
prohibited. This cycle declares no manifest change and expects none.

**`run` and `.github/workflows/**` remain forbidden**, so no new lane job can
ship. Every check built this cycle must live inside `./run version-check` or
`./run cycle-check`, the only two lifecycle entry points present in both the
local matrix and the hosted `shell` job.

---

## Entering state (asserted, not yet verified)

**Every line here is a hypothesis for E0. Byte figures marked *export-derived*
were computed from the delivered Repomix export with the measured
one-byte-per-file correction applied; the export file's own size is exact. Where
E0 disagrees, E0 is right.**

- v0.31 closed `release v0.17.1` on 2026-08-01. Release commit
  `7a621e39a069a1ef26438e841e7bb1ca2f34165b`; closing commit on `main`
  `f02379f03ccdfd1b019413234f2ad014d169fb04`; annotated tag object
  `14912f134e45277e2b4fd10b7f5bf8b4900ca20d`; post-push audit
  `9625fb1f7a7af2e85bad8418480b5b89093b707b`. Candidate hosted run
  **30685356489**; post-push hosted run **30686179773**.
- Worktree clean; `ci-local` **20/20**; golden **11/11**; `invariant-scan`
  **12 rules / 58 controls** with R12 at **30**; `checklist-audit` **247 checked
  / 3 retracted / 247 matched / 247 commits resolved**; Rust **146** workspace
  and **62** net (**32 ingest + 30 cored**); shell **325** collected / **325**
  passed / **0** skipped on both constrained lanes.
- Manifest unchanged: **331** pins, **191,395** bytes *(export-derived)*, **2**
  artifacts, schema 2, **857,181** bytes to 1 MiB.
- **The delivered review export is 2,654,404 bytes across 153 files** — exact,
  because it is the export file's own size. That is **88.48%** of the
  3,000,000-byte ceiling and **345,596** bytes of headroom.
- The recorded cycle-ending audit names closing tree
  `f02379f0…` at **2,649,103** bytes. The delivered export exceeds it by
  **5,301**, which reconciles to the byte against the post-push append: the
  POST-PUSH progress entry measures **2,727** export bytes and the `STATE.md`
  post-push block **2,572**, summing to **5,299** plus the two stripped
  trailing newlines. **That post-push delta is a second post-closing movement
  and no field names it.** G5 owns what that means.
- `STATE.md` is **324,290** bytes *(export-derived)* against the recorded
  **453,741**-byte archival boundary, leaving **129,451**. Cycle growth was
  289,117 → 324,290 = **+35,173**, so the boundary is **3.68 cycles** away at
  that denominator — **nearer than it was last cycle, and the estimate got
  worse, not better.**
- Delivered-export series: v0.28 **2,530,129**, v0.29 **2,521,787** (−8,342),
  v0.30 **2,583,624** (+61,837), v0.31 **2,654,404** (+70,780). **Four points,
  three observations, two consecutive positive and increasing.** At +70,780 the
  ceiling is **4.88 cycles** away.
- Retention will drop the v0.29 pair at activation: **95,797** export bytes
  *(export-derived, 95,799 as repository bytes)*.
- Governed rows: `ARCHITECTURE.md` **13** data rows of which **4** are
  trigger-bearing, all four carrying v0.31 close-time values; the v0.31
  deferred table **22** rows.
- Retention glob is `2[0-8]`, correct for v0.31 and **wrong for v0.32**. The
  derivation now consumes the Git-tracked retained set, whose earliest member at
  v0.32 is v0.30, so the expected pattern is
  `docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9]}{.md,.*.md,-*.md}`.
  **This is the first activation at which the range closes a full decade.**
- `tools/version_check.py` checks **five** version authorities:
  `apps/cored/Cargo.toml`, `shell/intel_shell/__init__.py`,
  `shell/intel_shell/app.py`, `STATE.md`, `CHANGELOG.md`. **`README.md:1`
  states `v0.17.1` and is checked by none of them.**
- `rust_floor_partition_report` derives **559** tracked paths from
  `git ls-files` and matched **75** literal-bearing files with **0**
  unclassified and **6** multiply classified. Its literal alternatives are built
  from `{msrv.derived} ∪ {net source}` = `{1.78, 1.86}` plus their `.0` forms.
  **A tracked file containing only `1.75` or `1.80` yields zero occurrences and
  is skipped before any classification is demanded.**
- The check emits one bound — *file-level only; within-file current restatements
  cannot be separated from dated historical quotations by identical literal
  text*. **It does not name the value-closure bound above.**
- `expected_review_export_retention_pattern` retains a
  `retained_cycle_paths=None` default that falls back to the old arithmetic.
  Production always passes the Git-derived set; the fallback is reached only
  from `shell/tests/test_cycle_check.py` and from the two `invariant_scan`
  plants. **It is a second live declaration of the retention semantics inside
  the production module.**
- `check_governed_export_margin` permits **zero or one** cycle-ending audit
  field. **Zero is a silent pass**, so the disclosure the contract promises is
  optional.
- `MAX_EXPORT_BYTES` is imported by `tools/cycle_check.py` and constrains the
  *written* governed figure, correctly disclosed in the emitted error.
  `export-check` remains absent from all **20** `ci_local_jobs` and from the
  workflow, so real export bytes are still measured only operator-locally.
- **58** planted controls: **24** into `tools/cycle_check.py`, **6** into
  `crates/store/src/sqlite.rs`, **3** into `tools/version_check.py`, and the
  remainder elsewhere.
- Rough activation projection: dropping the v0.29 pair removes **95,799** bytes
  *(export-derived)* and this runbook plus a progress skeleton adds roughly
  57,000. **Arithmetic on a pre-change tree is not a measurement** and is
  labelled the same way it was the last four times.

---

## Drafted gates

| Gate | Where | Hypothesis |
|---|---|---|
| **G1** [P1] | `STATE.md`; `config/protected-artifacts.json`; `ARCHITECTURE.md` dispositions table; the v0.31 deferred table | **Two governed byte boundaries are plain file sizes and nothing reads either file.** Confirm by exhaustive search that no checker measures `STATE.md`'s or the manifest's byte count against its declared boundary. Then measure both against the delivered tree and state each remaining margin in bytes and in cycles under an explicitly named denominator. **Say plainly which of the three governed byte quantities is nearest, and whether the estimate for it improved or worsened this cycle.** |
| **G2** [P1] | `tools/version_check.py:424-505` | **The Rust-floor detector's domain is derived from the values it is meant to police.** Confirm by execution that a tracked file containing only a wrong floor literal produces zero occurrences and is skipped before classification. Then rule on whether a detector that can see a wrong floor is achievable without either enumerating wrong values by hand or matching every `N.M` numeral in the repository — and if the honest answer is a broadened pattern plus an explicit accept-list, **say so and name what that list costs.** Also state whether the current emitted bound is complete. |
| **G3** [P1] | `tools/version_check.py:612-625`; `ARCHITECTURE.md` §8; `README.md:1` | **The release-version authority set is written by hand and is incomplete.** Enumerate by derivation, not by reading §8, every tracked file that states the current release version in a present-tense form. Classify each as checked authority, unchecked restatement, or dated historical record. **Confirm by execution that `README.md`'s literal can disagree with the five checked authorities without any lane failing**, and rule on whether the same file-level partition shape Step 3 works on transfers to release versions or whether the two problems are different. |
| **G4** [P2] | `refs/heads/codex/*`; the v0.31 receipts; `AGENTS.md` R-CLOSE | **The published release's signed evidence binds a ref name from a different cycle.** Enumerate every `codex/*` ref in the working repository and record which candidate each currently points at. State what the receipts bind, and whether ref identity is load-bearing for verification or only for reading. Then rule on whether a per-candidate ref convention can be *executed* by anything, or whether it can only be a runbook criterion — **and if it can only be a criterion, say so rather than proposing a check that would not run.** |
| **G5** [P2] | `docs/cycles/PROGRESS-v0.31.md`; `tools/cycle_check.py:1940-1975`; `AGENTS.md` §5 | **A release cycle has two post-closing appends and the contract names one.** Confirm the reconciliation above by measurement. Then settle two things: whether the optional cycle-ending audit field should be required at close for a cycle that has one, and whether the post-push append needs its own named field or is correctly left unmeasured. **A record cannot measure its own tree, so at least one delta is always undisclosed; name which one and stop there rather than adding a field that recreates the fixed point.** |
| **G6** [P2] | `ARCHITECTURE.md` divergence row; `AGENTS.md` §5 | **A trigger fired, and nothing in the checker noticed or would ever notice.** The divergence row's disposition cell still reads *Accepted under the operator-selected bound*; only its observation cell records the firing. Confirm by exhaustive search that no control distinguishes a fired trigger from an unfired one. Then settle the reset: the condition counts "three consecutive closed cycles" and **the publication that disposed it defines no restart point.** State what v0.32's observation must say and whether any part of firing or resetting is executable, or whether it is irreducibly an operator adjudication. |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate.

- **🤖 = Codex executes and self-verifies end to end** — no publication, no push
  to `main`, no ref creation or deletion **in the working repository**.
- **🧑 = exactly one named operator action or decision.**

**Interpretive rules, binding throughout.** An exit code of 0 from a
construction the checker never examined is **not measured**. A measurement that
disagrees with an acceptance criterion is **reported as measured**; the criterion
is what gets corrected. **Where the artifact is present in the repository, the
artifact is what gets measured; a written figure is acceptable only where the
artifact cannot exist in the tree, and that must be stated in the check's own
text.** A detector whose domain is derived from the values it polices can only
confirm agreement. A rule that cannot fail has not passed: every step here
demonstrates its rejection path against real output before its acceptance path.

**The no-release closing shape, stated in advance so Step 7 is not surprised.**
Under `no-release`, the closing implementation commit is already closed when
`cycle-check` runs, and the R-CLOSE progress entry lands in the *audit child*.
The governed row in the closing tree must therefore equal **the last governed
field the closing tree can already see** — a mid-cycle measurement, not the
closing tree's own export. Writing the closing tree's figure into that row is
the v0.30 defect and `cycle-check` now rejects it. The closing tree's export
belongs only in the audit child's `cycle-ending review-export audit` field.

**The planted-control line-number hazard.** `invariant_scan.self_test` compares
the emitted finding against `expected_file:expected_line:` exactly. Twenty-four
controls point into `tools/cycle_check.py` and three into
`tools/version_check.py`. **Any insertion shifts every control site below it.**
Re-derive the affected values from real self-test output after each edit and
**record how many were re-derived** — that figure is this cycle's evidence for
the deferred row that names the hazard. Do not change the control schema.

**Dependency gates.** Step 1 blocks everything. Steps 2, 3, 4, and 5 are
independent of one another, but **Steps 2 and 5 both edit
`tools/cycle_check.py`** and **Steps 3 and 4 both edit
`tools/version_check.py`**, so within each pair whichever runs second re-derives
the control line numbers the first shifted. Step 5 **may be skipped entirely
under its own decision gate.** Step 6 is blocked by every preceding
implementation step; Step 7 by Step 6.

**No amendment obligation is known in advance.** This cycle declares no evidence
directory that cannot exist yet and no manifest change. If an amendment becomes
necessary it takes the established form: a dated `## Runbook amendments` entry
in the same commit that first needs it. **This is notice of the mechanism, not
permission for a scope change.**

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean and record the measured refs **without asserting a literal `origin/main`
hash in `STATE.md`'s header**. Commit **only** this runbook at
`docs/cycles/TASKS-v0.32-EXECUTION.md` — including its `## Declared scope` table
— the `AGENTS.md` header moving the active declaration from v0.31 to v0.32, a
new `docs/cycles/PROGRESS-v0.32.md`, and the `repomix.config.json` retention
edit.

**This file deliberately contains no reserved cycle-closing heading and no blank
closing template.** The closing record is appended when the cycle closes.

**The retention glob must move from `2[0-8]` to `2[0-9]`, and this is the first
activation whose range closes a full decade. Record the exact rejection text
before making the edit**; the predicted line is:

```text
cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.32 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-9]}{.md,.*.md,-*.md}' to agree with the tracked retained-cycle set; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-8]}{.md,.*.md,-*.md}']
```

**A difference between that prediction and the emitted line is itself a
finding**, and this activation is also the first exercise of v0.31's
retained-set derivation on a cycle it did not author.

**Every governed row below already carries `v0.32` and a date**, so activation is
green under the identity rule. **Those dates are carried-forward hypotheses and
E0 rewrites every one of them with v0.32 measurements.** The four
trigger-bearing `ARCHITECTURE.md` rows still name v0.31 and **must be remeasured
at activation or the identity gate rejects them.** The governed export row is one
of those four; at activation the progress record is empty, so **record the
exemption name the real entry point reports rather than assuming which one
applies.**

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

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.32 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none — the gap stays recorded |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none — complete, do not re-exercise |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none — design complete, execution separately gated |
| Postgres / pgvector / multi-host seam | unchanged | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none |
| L2 forced-command wrapper | an operator server session | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none |
| `--features net` Rust 1.86 execution | a scoped cycle authorized to change evidence topology and an executable local or hosted lane that actually pins and runs the net path on Rust 1.86 | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none — deferred under the v0.30 operator outcome |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none — no historical ref touched |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none — the flag stays |
| Manifest retention/indexing | 1 MiB manifest, or two consecutive `verify-artifacts` runs ≥1.00 s | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | Step 2 — measured directly rather than restated; no registration |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none — recorded, not acted on |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | none — recorded, not acted on |
| Second `STATE.md` archival | the export ceiling trigger fires, or `STATE.md` reaches 453,741 bytes | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute; **this is the nearest governed boundary and E0 must state its margin in bytes and cycles** | Step 2 — measured directly; boundary made executable; no archive |
| Planted-control line numbers re-derived by hand | a control-schema change, or a cycle in which the re-derived count exceeds the controls it protects | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | Step 2, Step 3, Step 4, and Step 5 — shifted values re-derived and counted |
| Retention derivation across a version-family boundary | an active cycle whose name is not of the form `v0.<n>` — raising at `v1.0`–`v1.2`, silently under-excluding from `v1.3` onward | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute; **the trigger text is preserved verbatim, but v0.31's tracked retained-set binding may have superseded its second clause, and E0 must say which clauses still hold rather than editing the trigger** | none — recorded, not acted on |
| Published-release divergence | the unpublished distance contains a measured runtime behaviour difference persisting across three consecutive closed cycles, or acquires any public-surface change | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute; **the trigger fired at v0.31 and was disposed by publication, and its restart point is undefined** | Step 5 — reset semantics settled or recorded as unsettleable |
| MSRV current-restatement membership | a current restatement of either Rust floor lands outside the registry without failing a check | v0.32 · 2026-08-01 — carried-forward hypothesis for E0 to confirm or refute | Step 3 — detector domain widened or its closure bound named |
| Retention arithmetic fallback | the `retained_cycle_paths=None` branch produces an answer that differs from the tracked retained set in any construction a control or test relies on | v0.32 · 2026-08-01 — new row; E0 records the entering readers of that branch | none — recorded, not acted on |
| Optional cycle-ending audit disclosure | a closed cycle whose delivered export differs from its governed figure and which records no cycle-ending audit field | v0.32 · 2026-08-01 — new row; E0 records that zero audit fields is a silent pass today | Step 5 — settled under its own decision gate |

---

## Step 1 · E0 — Rebuild the entering state and settle six gates 🤖

**Objective.** Confirm HEAD is green and settle G1–G6. **Every assertion in
`## Entering state` is a hypothesis.** Report the measured value, especially
where it differs.

**Decision gate.** If the worktree is dirty, if v0.31's release, closing,
tag, and post-push commits are not where the entering state places them, or if
any local gate fails at entry, **record and stop.**

**Acceptance criteria.**

- All 20 `ci-local` jobs pass; `invariant-scan` passes its registered self-test;
  golden **11/11**; all pins verified twice with both real times recorded; both
  Python lanes reported as collected/passed/skipped via
  `tools/test_population.py`.
- The published state is confirmed independently: remote `main` and the peeled
  `v0.17.1` tag both resolve to the closing commit, the annotated tag object has
  Git type `tag`, and the closing commit's immediate parent is the release
  commit. **Report what was measured, not what the closing record asserts.**
- G1 settled **by exhaustive search and direct measurement**, with all three
  governed byte quantities stated in bytes and in cycles under named
  denominators, and the nearest one identified.
- G2 settled **by execution**, with the wrong-floor construction run against the
  real function and its zero-occurrence outcome recorded verbatim.
- G3 settled **by derivation and execution**, with the tracked
  version-restatement set enumerated and the `README.md` disagreement
  demonstrated passing every lane.
- G4 settled with every `codex/*` ref enumerated and its current target recorded,
  and with an explicit ruling on whether any check can execute a ref convention.
- G5 settled with the post-push reconciliation measured and a ruling on which
  delta must remain undisclosed.
- G6 settled **by exhaustive search**, with an explicit statement of what v0.32's
  divergence observation must say now that the trigger has fired and been
  disposed.
- The activation rejection text produced by the stale retention glob is recorded
  verbatim, and any difference from the predicted text is reported as a finding.
- The deferred table's rows are rewritten with **v0.32** measured observations,
  and the four trigger-bearing `ARCHITECTURE.md` rows carry v0.32
  close-adjacent measurements.
- **The governed-export exemption reported by the real entry point at activation
  is recorded by name.**

**Done when** every gate carries a measured answer and the entering state is
either confirmed or corrected in `STATE.md`.

- [ ] **E0**

---

## Step 2 · BOUNDARY-MEASURE — Read the file, not the sentence 🧑🤖

**Objective.** Make the two in-repo governed byte boundaries measured facts
rather than transcribed figures, and decide what happens when one is crossed.

**Decision gate.** `config/protected-artifacts.json` is **forbidden**; it is
read for its byte count and never written. `docs/state-archive/**` is
forbidden; this step measures a boundary and archives nothing. **If any part of
this step would require an archive, a manifest edit, or a new lane job, stop and
record it.**

**Why this is not tidying.** `STATE.md` is **129,451** bytes from its archival
boundary and moved **+35,173** this cycle — under four cycles of headroom, and
the estimate worsened. That quantity is the byte count of a tracked file sitting
in the same tree as the checker. The project currently learns it by an author
typing it into a prose cell and a freshness rule confirming the cell carries a
date. **That is the exact shape of every finding this project has spent six
cycles removing, applied to its own nearest deadline.**

**🧑 The operator's decision, and only the operator's.** Making a boundary
executable means deciding what a crossing does. Two outcomes, neither defaulted:

- **Crossing is an error.** `cycle-check` fails once the measured size reaches
  the boundary, and the lane stays red until an archive lands. This is what a
  trigger is for, and it means **the lifecycle blocks itself at 453,741 bytes
  with no archive step currently scheduled.** Choose this only having accepted
  that consequence.
- **Crossing is a named reported state requiring a dated disposition.** The
  check measures and reports; below the boundary it reports a bound state, at or
  above it requires the governed row to carry an explicit dated
  trigger-fired disposition and fails only if that is absent. **This keeps the
  lane green while the operator decides, and it makes firing visible rather than
  optional.**

The second outcome is the one that composes with Step 5; the first is the one
that cannot be ignored. **Neither is recommended here** — the reason to choose
is a judgement about how this project should behave when it runs out of a
budget, and that is not a reviewer's call.

**Acceptance criteria.**

- `STATE.md`'s and `config/protected-artifacts.json`'s byte counts are **read
  from the files** at the checked tree and compared against their boundaries.
  **No figure transcribed from a prose cell participates in the comparison.**
- Each boundary is stated **once**, in one authority, and consumed from there.
  **Two declarations of one boundary is the defect being removed**, so if a
  boundary already exists as a literal anywhere, that occurrence becomes the
  authority or is derived from it.
- The chosen crossing behaviour from the operator decision is implemented, and
  **the check's own emitted text states what it measured and at which tree.**
- **The below-boundary and at-or-above-boundary paths are both demonstrated by
  execution** against constructed trees. A check that has only ever been seen
  passing has not been seen.
- The manifest's timing trigger is explicitly **out of scope and said to be**:
  wall-clock verification time is not a byte fact and cannot be measured by a
  lifecycle checker. **A rule that silently covers half its subject is worse
  than one that says what it covers.**
- A registered `R12` control proves a crossed boundary is caught.
  **Demonstrate the rejection before the acceptance.**
- Every `expected_line` shifted by this edit is re-derived from real self-test
  output and the count is recorded.

**Done when** neither boundary can be misstated in a governed row without a
lane noticing, demonstrated by execution rather than by argument.

- [ ] **BOUNDARY-MEASURE**

---

## Step 3 · FLOOR-DOMAIN — A detector that can only see agreement 🤖

**Objective.** Either widen the Rust-floor detector so a wrong floor is visible,
or name its value-closure bound in the check's own text.

**Decision gate.** `run` and `.github/workflows/**` are **forbidden.** The
offline pins are read, never written. **If any part of this step would add a
hosted job, change a toolchain pin, or alter the evidence topology, stop and
record it.**

**The bound, stated so the criteria are satisfiable.** A detector that matches
only `1.78` and `1.86` answers "does every file stating the current floor belong
to a declared class?" — a real question with a real answer. It does not answer
"does any file state a floor that is not the current one?", and **that second
question is the one v0.30 FLOOR-BIND existed to answer.** Widening the pattern
to every `N.M` numeral would match version numbers, byte counts, dates, and
timing figures across the whole repository, which is not a viable detector. A
middle shape exists — match a floor *in a floor-shaped context* rather than a
bare numeral — and it is the shape worth measuring. **Both outcomes are
acceptable; a widened detector that produces false positives nobody can triage
is not, and neither is leaving the closure bound unstated.**

**Acceptance criteria.**

- **Either** the detector recognizes a floor-shaped statement whose value is not
  the derived one, demonstrated against a planted tracked file carrying a
  refuted figure, **or** the check's emitted bound names the value closure
  explicitly alongside the existing within-file bound.
- If the detector is widened, its context predicate is **derived or registered,
  never a list of wrong values** — enumerating the wrong answers is the same
  hardcoded-membership defect one level down.
- **False-positive cost is measured, not asserted.** Run the widened detector
  over the real tracked set and report how many files it newly matches and how
  many require a classification decision. **If that number is not triageable,
  say so and take the bound-naming outcome instead** — reporting the measurement
  and correcting the criterion is the required behaviour, not a fallback.
- Dated historical records that quote the refuted figure **must keep quoting it
  and must not be rewritten.**
- The existing zero-extraction, pin-disagreement, and unclassified-file
  rejections continue to fire, confirmed by test.
- The binding lives in an entry point that already runs in both lanes.
- A registered `R12` control proves whichever property ships is exercised.
  **Demonstrate the rejection before the acceptance.**
- Every `expected_line` shifted by this edit is re-derived and the count
  recorded.

**Done when** a tracked file asserting a wrong Rust floor either fails
automatically or is explicitly named as outside the check's stated domain.

- [ ] **FLOOR-DOMAIN**

---

## Step 4 · VERSION-COMPLETE — Derive the authority set 🤖

**Objective.** Stop enumerating the release-version authorities by hand, and
bind every tracked present-tense restatement of the release version to the
checked value.

**Decision gate.** `shell/intel_shell/**` is forbidden except through declared
release-authority precedence, and this step does not change a version value.
**If correcting a restatement would require moving a version, stop and record
it** — that is a release action and this cycle declares `no-release`.

**Why this is the same problem as Step 3 and not the same solution.** Both are
"which files state this fact?" But the Rust floor has two values and a stable
phrasing, while the release version appears as `0.17.1` in code and `v0.17.1` in
prose, in a heading, a link path, a tag name, and a changelog entry, and it
changes every release. **The partition shape may or may not transfer, and G3
rules on that before this step commits to one.** If it does not transfer, the
honest outcome is a registered restatement list with a named maintenance
obligation — the same shape `OFFLINE_MSRV_RESTATEMENTS` has, **and this time
with a reader from the start.**

**Acceptance criteria.**

- `README.md`'s release-version statement is bound to the same value the five
  existing authorities agree on, **demonstrated by planting a disagreement and
  showing a lane fail.**
- The authority-or-restatement membership is **derived where G3 showed
  derivation is achievable, and registered with a named reader where it is
  not.** An unread registry does not discharge this criterion; that is v0.30's
  error and it does not get made twice.
- `ARCHITECTURE.md` §8's sentence naming the version sources is corrected to
  match what executes, or **§8 delegates to the check and stops restating the
  list.** Two declarations of the authority set is the defect being removed.
- Dated historical records naming an older release **must keep naming it.** Only
  present-tense statements of the current release are bound.
- A registered `R12` control proves a disagreeing restatement is rejected.
  **Demonstrate the rejection before the acceptance.**
- Every `expected_line` shifted by this edit is re-derived and the count
  recorded.

**Done when** a release-version restatement that disagrees with the checked
authorities fails automatically, in whichever of the two shapes G3 showed is
honest.

- [ ] **VERSION-COMPLETE**

---

## Step 5 · TRIGGER-STATE — What a fired trigger does 🤖

**Objective.** Give trigger firing a defined consequence and the divergence
count a defined reset, or record why neither is executable.

**Decision gate.** Blocked by nothing and **skippable in full.** If G6
concluded that firing is irreducibly an operator adjudication and that any
implementable check would be a self-report — a row asserting its own state with
nothing to contradict it — **record that and stop.** A self-report dressed as a
control is worse than an honest prose rule, and this project has the vocabulary
to say so. **Step 2's outcome may already supply the executable half for the two
measurable boundaries; if so, this step's remaining subject is the reset
semantics only, and shrinking to that is a legitimate result.**

**The specific defect, stated so the criteria are satisfiable.** The divergence
row's condition counts three consecutive closed cycles. v0.31 fired it and
disposed it by publishing. **Nothing states what resets the count.** A reader at
v0.32 cannot determine from the contract whether the count is now zero, whether
publication is the reset, or whether a later unpublished behaviour difference
starts a fresh count from its own cycle. The observation cell will be written by
whoever closes v0.32, and today they may write any of the three.

**Acceptance criteria.**

- The reset point is stated in the contract in the same symmetric form the
  latest-at-close rule uses, **so a later cycle cannot select a favourable
  reading.** Both directions are covered: what restarts the count, and what does
  not.
- **If any executable part exists, it ships with a demonstrated failing case.**
  If the only implementable form is a self-report, that ruling is recorded and
  nothing is built.
- The optional cycle-ending audit disclosure from G5 is settled in the same
  pass: either a closed cycle whose delivered export differs from its governed
  figure must carry the audit field, or the optionality is deliberate and said
  to be.
- If a control ships, a registered `R12` control proves it.
  **Demonstrate the rejection before the acceptance.**
- Every `expected_line` shifted by this edit is re-derived and the count
  recorded.

**Done when** a reader at the next cycle can determine the divergence count's
state from the contract alone, or the reason that cannot be made executable is
written down.

- [ ] **TRIGGER-STATE**

---

## Step 6 · RE-MEASURE — Hosted verification on a named neutral ref 🤖

**Objective.** Produce authenticated hosted evidence at an exact candidate on a
ref whose name describes what it holds.

**Decision gate.** Blocked by Steps 2–5. **The workflow is forbidden**, so the
job matrix, the receipt population, and the signed identity count must be
identical to the prior cycle's; **if any of them moves, that is a finding and
not a result.** The candidate is a no-release tree and goes to a neutral ref
only.

**The ref convention, restored.** The candidate is pushed to a **fresh ref of
the form `refs/heads/codex/v0.32-evidence-<sha7>`**, created for this candidate
and never previously used. **No existing branch is reused, force-moved, or
repurposed.** This is a criterion, not a check — G4 rules on whether anything can
execute it, and if the answer is no, then a criterion honestly labelled as a
criterion is what this gets.

**Acceptance criteria.**

- All seven executable hosted jobs pass at the exact candidate; the
  dependency-drift job skips under its declared report-only condition.
- Attestations required; every signed identity accepted, zero rejected; the
  complete runner matrix found.
- **The ref the candidate was pushed to is named in the record**, together with
  confirmation that it did not previously exist. **A reused ref is a finding to
  record, not a detail to omit** — v0.31's release evidence is on a branch named
  for v0.23 precisely because no record demanded the name.
- Both shell lanes compared by `tools/test_population.py` with
  comparator-derived `collected`, `equivalent`, and `equivalent_passed`. **Every
  figure written is the comparator's output, never transcribed from a log.**
- All pins verified on the candidate, unchanged; golden **11/11**.
- **No manifest registration occurs.** This cycle declares none and expects none.
- Remote `main`, the peeled `v0.17.1` tag, and its annotated tag object are
  re-measured after the run and confirmed unmoved.

**Done when** the candidate carries release-grade authenticated evidence on a
ref that says what it is.

- [ ] **RE-MEASURE**

---

## Step 7 · R-CLOSE 🧑🤖

**Objective.** Close v0.32 with an explicit, reasoned disposition.

**The drafted intent is `no-release` and the reason is structural, not
habitual.** Every production source path is forbidden this cycle, so the
unpublished distance from v0.17.1 should contain no behaviour change at all.
**That is a hypothesis this step must verify rather than assert**: if the
measured cycle diff contains a production behaviour change, the scope gate was
violated somewhere and that is the finding.

**🧑 The operator's decision, and only the operator's.** Publication
authorization is a separate explicit act and is **not** implied by this runbook,
by green gates, or by hosted evidence. Two outcomes, neither defaulted:

- **`no-release`** — close v0.32 on its own record and state what the
  unpublished distance now contains, measured against the published v0.17.1
  tree. **A distance of documentation and lifecycle checks only is a reason;
  "nothing shipped" is not the same statement and should not be substituted for
  it.**
- **`release` at patch** — only if a step measured something that belongs in
  users' hands. **This requires a measurement, and under this cycle's declared
  scope such a measurement would itself be a scope finding.** Selecting it means
  reopening the disposition before Step 6 rather than at this step; that is the
  v0.31 lesson and it holds.

**Acceptance criteria.**

- The closing record names the closing date and the dated release disposition,
  and — under `no-release` — the intentionally unreleased commits, with every
  version source and tag unchanged.
- **The governed export row in the closing tree equals the last governed field
  that tree can already see**, and the closing tree's own export goes only in the
  audit child's `cycle-ending review-export audit` field.
- Every declared permission is reconciled as used or unused, by path. **The
  release-authority set is reconciled explicitly**, because declaring those paths
  under `no-release` intent and then using or not using them is a fact the record
  owes a reader.
- Every gate G1–G6 has a recorded measured answer, including Step 2's operator
  outcome and Step 5's skip-or-implement ruling.
- **The three reviewer errors in this file's header are preserved in the cycle
  record as reviewer errors**, not restated as findings and not quietly dropped.
- The total of `expected_line` values re-derived across the cycle is recorded.
- The divergence trigger carries a dated observation consistent with whatever
  reset Step 5 settled, and **says which reading it is using.**
- `STATE.md` records the final export figure against the ceiling **naming its
  tree**, its own measured size against the archival boundary, the
  `checklist-audit` control, and the derived growth observations with their count
  stated.

**Done when** the disposition is authorized, recorded, and measured.

- [ ] **R-CLOSE**

---

## Cycle checklist

- [ ] Worktree clean at entry; v0.31 release, closing, tag, and post-push commits where E0 measures them
- [ ] Published `v0.17.1` identity re-measured independently, not inherited from the closing record
- [ ] Stale retention glob rejection recorded verbatim before the activation edit
- [ ] Every entering-state hypothesis measured and confirmed or corrected
- [ ] G1–G6 each carry a measured answer; G1, G2, and G3 answered **by execution**
- [ ] Every governed quantity present in the tree is measured from the tree
- [ ] Every detector's domain stated in its own emitted text
- [ ] Every new binding demonstrated **rejecting** before demonstrated passing
- [ ] No declared membership left in code without a reader
- [ ] No binding implemented as a self-consistency assertion
- [ ] No binding whose membership is written by hand rather than derived, or else the registry has a named reader
- [ ] No expected value hardcoded in any test added or edited this cycle
- [ ] Re-derived planted-control line numbers counted and recorded at every step
- [ ] Evidence candidate pushed to a fresh, self-describing ref; the ref named in the record
- [ ] No closed cycle document edited, moved, or deleted
- [ ] Workflow file byte-identical across the complete cycle diff
- [ ] Manifest byte-identical across the complete cycle diff
- [ ] `checklist-audit` total does not fall; every figure recorded
- [ ] Export under 3,000,000 bytes at every measured point, each naming its tree
- [ ] Golden **11/11** byte-identical at every step
- [ ] SEC identity population unchanged
- [ ] Both Python lanes reported as collected/passed/skipped, comparator-derived
- [ ] Deferred table rows all carry v0.32-identified observations
- [ ] No publisher request, no scheduler run, no cadence change
- [ ] Three reviewer errors preserved as such in the cycle record

---

## Standing prohibitions

- **No publisher request and no scheduler run.** The bounded window design
  exists and its execution authorization is again withheld from this cycle.
- **No edit to `.github/workflows/**` or `run`** — the workflow is read as the
  hosted MSRV authority and `run` is an `authorization` pin read as the local
  one. Neither is written.
- **No edit to `tools/model_profiles.py`** — also an `authorization` pin.
- **No manifest edit.** `config/protected-artifacts.json` is read for its byte
  count in Step 2 and written by nothing.
- **No `STATE.md` archival.** The boundary is made measurable; **measuring is not
  archiving**, and an archive is a separate authorized action.
- **No production source edit.** Every `crates/**/src/**`, `apps/**/src/**`, and
  `shell/intel_shell/**` path is forbidden; the two shell version files are
  reachable only as release authorities and this cycle moves no version.
- **No closed cycle document is edited, moved, renamed, or deleted.**
- **No push to `main`, no tag, no ref creation or deletion** other than the one
  fresh evidence ref Step 6 requires.
- **No reuse of an existing branch as an evidence candidate ref.**
- **No hardcoded expected value** in any test written or edited this cycle, and
  **no hand-written membership list without a named reader** in any binding built
  this cycle.
- **No binding that a single implementation can satisfy by construction**, and
  **no self-report presented as a control.**
- **No rule ships without a demonstrated failing case, and no detector ships
  without its domain stated in its own text.**
- **No rewriting of a dated historical record that quotes a refuted figure or an
  older release version.**
- **No retraction is proposed** without a twice-verified measured false claim in
  an immutable published record. **The count stands at three.** None of this
  cycle's findings concerns a false claim in an immutable published record —
  they concern live checkers, a live contract, and a live README — and **this
  reviewer is not proposing one.**

---

## Provenance of this draft

**Read, not measured:** the Codex v0.31 report; `TASKS-v0.31-EXECUTION.md` in
full including its eight amendments and closing record; `PROGRESS-v0.31.md` in
full; `AGENTS.md` §§0 and 5 including the R-CLOSE protocol section;
`ARCHITECTURE.md` §6's dispositions table and §8; `STATE.md` header and the
v0.31 sections.

**Measured against the 2026-08-01 delivered export, by path and line:** export
size **2,654,404** bytes and **153** files, exact; `STATE.md` at **324,289**
export bytes and `config/protected-artifacts.json` at **191,394**, each one
below its repository value under the one-byte-per-file rule, giving **324,290**
against the 453,741 boundary and **191,395** against 1 MiB;
`docs/cycles/PROGRESS-v0.31.md` at **35,292** export bytes with its POST-PUSH
entry at **2,727** and the `STATE.md` post-push block at **2,572**, whose sum of
**5,299** plus two stripped newlines reconciles the delivered export against the
recorded **2,649,103**-byte closing-tree audit exactly;
`config/invariant-rules.json` at **12** rules and **58** `fail_before` controls
with R12 at **30**, distributed **24** into `tools/cycle_check.py`, **6** into
`crates/store/src/sqlite.rs`, and **3** into `tools/version_check.py`; **every
one of the 58 `expected_line` values checked in range, and each of the 33
pointing into those three files verified to land exactly on its control
marker** — including the new ceiling control at `cycle_check.py:1920`, the
cycle-ending audit ordering at `:1949`, latest-at-tree at `:1964`, the joint
retention control at `:1151`, and the new partition control at
`version_check.py:484`; `check_governed_export_margin` in full, confirming that
zero cycle-ending audit fields is a silent pass;
`expected_review_export_retention_pattern`'s `retained_cycle_paths=None`
fallback and its three readers in `test_cycle_check.py` and `invariant_scan.py`;
`export_check.expected_retained_cycle_paths` deriving from tracked paths;
`version_check.main`'s **five** version authorities with `README.md` absent from
them; `README.md:1` stating `v0.17.1`; `run`'s **20** `ci_local_jobs` with
`export-check` absent; `checklist-audit` reconciled as v0.30's **239** plus
v0.31's **8** bolded tasks = **247**, against **23** bolded boxes across the
three retained runbooks; `config/checklist-retractions.json` at **3**;
`repomix.config.json` retention glob at `2[0-8]`; all five version authorities
reading **0.17.1**; the manifest at **331** pins / **2** artifacts / schema 2
with `run` and `tools/model_profiles.py` carrying the two `authorization`
grades.

**Measured by executing the real code paths in isolation:** the v0.32 expected
retention pattern, produced by running the committed `numeric_glob_range` at
`last_excluded=29` and formatting the result — this is the real function, not a
reimplementation, and reviewer error 2 of the v0.31 cycle is why that
distinction is stated; and the Rust-floor literal detector, reconstructed from
`_rust_floor_literal_pattern`'s committed body and run against floor-shaped
strings, which matched `1.78` and `1.86` and did **not** match `1.75`, `1.80`,
or `1.90`. **The second of those is the evidence for reviewer error 1 and for
G2**, and it is a reconstruction of one function rather than an execution of
`version-check`, so **G2 must confirm it against the real entry point with a
real tracked file before it is treated as settled.**

**Asserted and not verified:** every line under `## Entering state`; that
`README.md` can disagree with the five checked authorities without a lane
failing, which follows from reading `version_check.main` and is **G3's to
demonstrate**; that no control distinguishes a fired trigger from an unfired
one, which follows from reading the freshness and identity checks and is
**G6's to confirm exhaustively**; the enumeration of `codex/*` refs, which this
reviewer cannot see at all.

**Not verifiable by this reviewer at all:** that no historical cycle document was
moved, edited, or deleted — retention depth 3 exports only v0.29–v0.31, so v0.1
through v0.28 are outside reach and that claim rests on `checklist-audit` and on
Codex's measurement. Also unverifiable here: every figure Codex reported for the
release commit and the closing tree, since only the post-push child was
delivered; the hosted run contents; the ref topology; and whether the receipts
bind the ref name in the form the v0.31 record describes. **Said plainly rather
than left implied.**

**Three reviewer errors are recorded in this file's header** rather than here,
because a provenance note is where a reader looks last and an error is what they
should see first.
