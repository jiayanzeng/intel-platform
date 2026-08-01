# TASKS-v0.33-EXECUTION.md (r2) — model the operation, not just the boundary

## Runbook amendments

*(Appended per step as each completes, in the v0.32 form: `Step N — <what was
implemented> — <date>`.)*

**r2 — 2026-08-01 — reviewer pre-flight before hand-off.** The three archival
cuts in Step 5 were executed against the delivered tree in throwaway clones and
checked with the real `tools/version_check.py`. Three things changed as a
result, all recorded below and in the provenance section: **Option A's cut point
was wrong and is corrected**; **`STATE.md`'s per-cycle block ordering is not
uniform**; and **one Step 4 acceptance criterion was redundant and one was
understated**. r1 is superseded. Nothing in r1 is edited in place — the
corrections are stated as corrections.

**r3 — 2026-08-01 — activation-contract correction.** Executing the real
`./run cycle-check` after staging the operator-supplied r2 file exposed four
author-side schema defects before activation: `conditional` was not a supported
declared-scope class; the deferred table omitted its executable measured-
observation column; the immediately prior `MSRV current-restatement membership`
subject was not carried forward; and two action cells used `Steps N–M`, which
does not satisfy the named `Step N` grammar. The permission is now an `allow`
whose conditional use remains prose-constrained to Step 5 Option B, the prior
measured observations are carried forward until E0 replaces them with v0.33
measurements, the missing subject is restored, and each discharging step is
named in the executable form. The checker was not weakened.

**r4 — 2026-08-01 — Fidelity B expressibility correction.** The operator
selected Cut B and Fidelity B. The required pre-manifest validators passed, but
a synthetic `pinned_files[]` entry for the mandated
`docs/state-archive/STATE-through-v0.28.md` path made the real manifest entry
point exit 2 because schema v2 admitted only evidence, observation, and exact
authorization paths. The runbook simultaneously forbade the only validator
that could register the archive, so its Option B acceptance criterion was
author-side unsatisfiable. In accordance with `AGENTS.md §7`, this amendment
records and corrects that defect: `tools/evidence_artifacts.py` is narrowly
allowed for an exact structural-archive registry and failure-capable tests;
prefix admission remains forbidden.

Step 1 — rebuilt the exact entering state and settled G1–G6 — 2026-08-01

The measured baseline corrected checklist 253 to 254, confirmed the delivered
audit-child export at 2,734,366 bytes, proved the publication family admits
missing and unmatched headers, classified the Architecture overstatement as a
reviewer error by measured authorship, replaced the mixed-kind margin forward,
enumerated the complete live permanent-tail bindings, established that archive
fidelity has no standing reader, and measured Option B returning 178,125 bytes
to both State and export boundaries. No archival cut was selected or performed.

Step 2 — publication-status admission and newest-release selection completed — 2026-08-01

Step 3 — governed export margin bound to a same-kind progress series — 2026-08-01

Step 4 — State archival-region and external-reference contract completed — 2026-08-01

Step 5 — operator-selected Cut B archived through v0.28 with a standing Fidelity B pin — 2026-08-01

---

**Three reviewer errors, all mine, recorded before anything else.**

1. **v0.32 G1 required each governed byte margin to be stated "in cycles under
   an explicitly named denominator." It never required the denominator to be
   the same kind of measurement as the numerator.** Codex complied exactly:
   the `ARCHITECTURE.md` review-export row states **51,989 bytes larger than
   v0.31's delivered export** and derives **5.65 cycles** of margin. That
   subtraction is a *candidate* export minus a *delivered* export. The
   like-for-like figures I measured are **+79,962 bytes/cycle** delivered→delivered
   and **+77,014** candidate→candidate, giving **3.32** and **3.81** cycles.
   **The recorded margin overstates the real one by roughly 70%, and it will do
   so again every cycle, in the same direction, because the CLOSE-POINT rule
   that correctly binds the governed *bytes* to the last field the closing tree
   can see also silently fixes the evaluation point of the *estimate* written
   beside them.** v0.31's named root cause was that a binding inside a
   multi-commit protocol is not specified until it names its evaluation point.
   I fixed that for the binding and reintroduced it one level down, in the
   derived estimate, in the cycle whose title was *measure the artifact, not the
   sentence about it*. The criterion was satisfiable and satisfied; **the
   criterion was wrong, and correcting it is G2's job and Step 3's.**

2. **r1 of this runbook picked the Option A cut point by pattern rather than by
   measurement, and asked Step 4 to protect something already protected.**
   Option A read "cut at v0.26 R-CLOSE, line 2924," on the assumption that a
   cycle's block begins at its R-CLOSE line. It does not always: the record
   immediately above 2924 is **v0.16.1 post-push verification at line 2881**,
   and **v0.26 is the cycle that published v0.16.1**. An archive labelled
   "through v0.26" cut at 2924 would have left one of v0.26's own records
   behind. The corrected boundary is **2881**; the byte figures move with it.
   Separately, r1 required Step 4 to enforce that the registered MSRV
   restatement stays in the non-movable region. **Executing the real
   `version-check` against a tree with that line removed shows v0.32 Step 4's
   zero-extraction rejection already catches it** — so that criterion asked for
   a duplicate control, which is this project's own prohibition. What r1
   understated is the gap that is real: **section anchors have no protection at
   all, and I measured an archival that removes five of them passing every
   check.** Both corrections are carried below.

3. **r2 offered Fidelity B as a manifest-only choice even though the manifest
   schema could not express the required archive path, then explicitly forbade
   changing that schema validator.** The real entry point rejected a synthetic
   Option B plant with `pinned_files[331].path: pinned files must live beneath
   evidence/, observations/, or be an exact registered authorization surface`.
   Neither the SQLite `artifacts[]` shape nor an evidence-path alias can
   honestly describe the selected archive. r4 therefore permits the narrow
   validator and test change needed to register this exact structural archive;
   no prefix, alias, or mislabelled authorization grade is introduced.

---

## The named root cause for this cycle

v0.32 made every governed boundary read the artifact. **Nothing reads the
operation that moves the boundary.**

| governed quantity | crossing detector | disposing operation | what models the operation |
|---|---|---|---|
| `STATE.md` archival boundary | **executable** — reads the file's bytes at a named tree | second archival to `docs/state-archive/**` | **nothing** — no eligible-region contract, no fidelity check, no consumer |
| protected-manifest byte bound | **executable** — reads the file's bytes | retention/indexing | nothing, and correctly deferred: 99.43 cycles away |
| review-export ceiling | **executable** — bound disclosed honestly | retention advance + archival exclusion | retention is executable; the archival half is not |
| publication-status reconciliation | R12 disables each rule *inside* the family | — | **the family's admission gate has no control at all** |

**The nearest governed trigger of all is disposed by a large mechanical rewrite
of `STATE.md`, and every precondition of that rewrite is currently a sentence.**
The eligible region is undefined. The byte-for-byte fidelity claim has no
reader. And the one lifecycle check most likely to be disturbed by rewriting
the top of `STATE.md` — publication-status reconciliation — **fails open when
its header is absent, renamed, or the file is missing**, which I measured by
executing the real function.

The objective of v0.33 is that **the operation which answers a trigger is as
executable as the trigger itself**, and then to perform it with roughly three
cycles of margin in hand rather than under boundary pressure.

---

## Declared scope

| Scope class | Path or value |
|---|---|
| `scope_version` | `1` |
| `disposition_intent` | `no-release` |
| `allow` | `tools/cycle_check.py` |
| `allow` | `tools/version_check.py` |
| `allow` | `tools/invariant_scan.py` |
| `allow` | `config/invariant-rules.json` |
| `allow` | `shell/tests/**` |
| `allow` | `docs/state-archive/**` |
| `allow` | `AGENTS.md` |
| `allow` | `ARCHITECTURE.md` |
| `allow` | `tools/export_check.py` |
| `allow` | `tools/evidence_artifacts.py` |
| `allow` | `repomix.config.json` |
| `allow` | `config/protected-artifacts.json` |
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
| `forbid` | `docs/cycles/**` (except this runbook and `PROGRESS-v0.33.md`, by standing precedence) |

The `config/protected-artifacts.json` allow is conditionally usable **only**
under Step 5 Option B after explicit operator selection. If Option A is
selected, this permission remains unused and must be reconciled that way at
close.

**`docs/state-archive/**` moves from `forbid` to `allow` this cycle, and that is
the single most consequential line in this table.** It has been `forbid` since
v0.30. Every step that writes under it is named below; a write under that prefix
from any unnamed step is a scope finding, not a convenience.

**`disposition_intent` is `no-release`, and the reason is structural.** Every
production source path, every workflow path, and every publisher/scheduler
configuration path is forbidden. No step is scheduled to change runtime
behaviour, any `/v1/*` route, response shape, or serialized value domain.
**That is a hypothesis Step 7 must verify against the measured diff, not an
assertion this table settles.** If any step measures a production behaviour
change, the scope gate was violated and that is the finding — reopen the
disposition before Step 6, not at Step 7. That is the v0.31 lesson and it holds.

---

## Entering state

**Every line in this section is a hypothesis. Report the measured value,
especially where it differs.** These are the reviewer's readings of the
delivered v0.32 export and are labelled by how they were obtained in the
provenance section at the end.

- v0.32 closed **2026-08-01** with `no-release`. Closing implementation commit
  `86b8db0b4026c23371317c7881dcc9497806c20b`; audit record
  `70b7f93c94c67e43f6f4a29ede5823081955f3fa`.
- Published **v0.17.1** remains current. Remote `main` and the peeled tag both
  resolve to closing commit `f02379f03ccdfd1b019413234f2ad014d169fb04`;
  annotated tag object `14912f134e45277e2b4fd10b7f5bf8b4900ca20d`; release
  commit `7a621e39a069a1ef26438e841e7bb1ca2f34165b`.
- Local `ci-local` **20/20**; Python 3.11.4 and 3.12.13 each **336/336**;
  golden **11/11**; `invariant-scan` **12 rules / 61 controls**; manifest
  **331 pins / 191,395 bytes**; retractions held at **3**.
- `STATE.md` is **352,895 bytes** against its **453,741-byte** governed
  boundary, leaving **100,846 bytes**.
- The delivered review export is **2,734,366 bytes / 153 files**. The recorded
  closing-tree figure is **2,729,387**; the delivered export is **4,979 bytes**
  larger, which is consistent with the audit child but **is not proven to be
  it**. E0 owns that confirmation.
- The v0.30 TASKS/PROGRESS pair totals **106,928 bytes** and leaves the export
  when retention advances at v0.33 activation.

---

## Gaps this cycle must settle

| Gate | Sources | What must be measured |
|---|---|---|
| **G1** [P1] | `tools/cycle_check.py:589–596`; `tools/invariant_scan.py` R12; `ARCHITECTURE.md` ¶ on publication reconciliation | **The publication-status family's admission gate fails open and `ARCHITECTURE.md` claims it does not.** Executing `check_publication_status` directly, I measured **0 errors** for an absent `**As of:**` header, **0** for a renamed header, and **0** for an absent `STATE.md`, against **1 error** for a valid header. `ARCHITECTURE.md` states that R12 "independently disables each current rule family, so a rule that examines nothing cannot report a clean result merely because its pattern found nothing." **Confirm or refute by execution at the real `./run cycle-check` entry point over the same three constructions.** `version_check.state_version()` raises on a missing header and may mask this at the composite lane — **measure whether it does, and say plainly whether the protection is `cycle-check`'s own or borrowed from another tool.** Then determine by measurement which cycle introduced the `ARCHITECTURE.md` sentence; **do not attribute it without measuring it.** |
| **G2** [P1] | `ARCHITECTURE.md` review-export row; `PROGRESS-v0.31.md:464`; the v0.32 closing and audit records | **The governed export margin estimate mixes measurement kinds.** Derive all three same-kind series — governed→governed (`2629379` → `2706393`), closing-tree→closing-tree (`2649103` → `2729387`), and delivered→delivered (`2654404` → the confirmed v0.32 delivered figure). State each denominator, each resulting margin in cycles, and **which of them the governed row can honestly carry given that the closing tree cannot see its own export.** Then state whether the recorded **5.65 cycles** is a measurement error, a criterion error, or both. |
| **G3** [P1] | `STATE.md`; `tools/export_check.py:43`; `tools/version_check.py:318`; `docs/state-archive/STATE-through-v0.21.md` | **`STATE.md` has two structurally different regions and no control distinguishes them.** Measure the header block, the dated-append region, and the permanent numbered tail (`## 1.`–`## 7.`) in bytes at the delivered tree. Enumerate **every** binding into the permanent tail: the registered `current correction: offline needs >= 1.78` restatement read by `OFFLINE_MSRV_RESTATEMENTS`, and every external `STATE §N` cross-reference, by file and line. **Say which region an archival may move and what makes that answer executable rather than asserted.** Note that the numbering has no `## 3.`; determine whether anything references it. **The reviewer pre-flight already measured four constructions at the real `version-check`: an over-cut into the permanent tail and a dropped restatement line are both REJECTED with `current run-reference correction yielded zero extracted current restatements`; a renamed `## 5.` heading and an archival removing §1, §2, §4, §5 and §6 while keeping §7 both PASS. Confirm those four at the complete `./run version-check` and `./run cycle-check` entry points, and report any difference as a finding.** |
| **G4** [P2] | `docs/state-archive/**`; `config/protected-artifacts.json`; `tools/*.py`; `run` | **The v0.21 archive claims byte-for-byte preservation and nothing reads it.** Confirm by exhaustive search that no tool, test, config, or manifest pin consumes `docs/state-archive/**`. Then state plainly what would detect a truncated, reordered, or corrupted archive, and what the answer implies for a second one. **If the answer is "nothing," say so; a recorded bound is acceptable, a claimed property with no reader is not.** |
| **G5** [P2] | `tools/checklist_audit.py:337–360`; `tools/cycle_check.py`; `tools/version_check.py`; `tools/invariant_scan.py` | **Enumerate every executable reader of `STATE.md` and state, per reader, what an archival would do to it.** My reading is that `checklist_audit` enumerates execution runbooks only and is therefore unaffected, so the audit total does not fall. **Confirm or refute by execution against a throwaway clone carrying the proposed cut**, and report the checklist figures before and after. |
| **G6** [P3] | `ARCHITECTURE.md` dispositions table; the v0.32 deferred table | **Both governed byte boundaries land in the same window and one operation disposes both.** Derive each margin in cycles under same-kind denominators, state the `STATE.md` row's first clause dependency on the export clause explicitly, and record how many bytes the proposed archival returns to **each** of the two boundaries. |

---

## Governed artifact byte-boundary authority

- governed artifact byte boundary: path=`STATE.md`; bytes=`453741`
- governed artifact byte boundary: path=`config/protected-artifacts.json`; bytes=`1048576`

**This authority is carried forward byte-identically from v0.32.** If a step
proposes changing either figure, that is an architectural change requiring its
own justification and operator authorization — not a consequence of archiving.

---

## Deferred means deferred

Every row carries its **unchanged** trigger. The observation column must be
rewritten with **v0.33** dated measurements; the trigger column must not be
edited to match what happened.

| Deferred item | Unchanged trigger | Measured observation (cycle-identified) | v0.33 action |
|---|---|---|---|
| T7 robots single-flight | a second concurrent harvester | v0.33 · 2026-08-01 — no harvester, `cored` process, or listener on 8788 was started and no publisher request ran; trigger did not fire | none |
| NEGATIVE-CACHE Decision B | a live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | v0.33 · 2026-08-01 — no publisher request, outage exercise, or operator authorization occurred; trigger did not fire | none |
| Conditional GET (`ETag` / `If-Modified-Since`) | an operator-authorized cycle whose scope permits the `net` request path plus a live 304 observation | v0.33 · 2026-08-01 — scope forbids the net request path and no live 304 was observed; trigger did not fire | none — the gap stays recorded |
| `edgar:*` extension field mapping | an operator-authorized cycle permitting `crates/ingest/src/**` for mapping, with a connector review | v0.33 · 2026-08-01 — production source remains forbidden and no connector review occurred; trigger did not fire | none |
| Live multi-publisher behaviour in one runtime | further origins beyond the two configured, or concurrency | v0.33 · 2026-08-01 — no runtime, third origin, or concurrency was exercised; trigger did not fire | none — complete, do not re-exercise |
| First recurring scheduled SEC run | explicit operator authorization of a bounded scheduled window, separate from any cycle scope | v0.33 · 2026-08-01 — no scheduler or service ran and no authorization was supplied; trigger did not fire | none — see the standing note below |
| Postgres / pgvector / multi-host seam | unchanged | v0.33 · 2026-08-01 — no topology, dependency, schema, or production-source path changed | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | v0.33 · 2026-08-01 — no third-party shell or replacement-invariance claim appeared; trigger did not fire | none |
| L2 forced-command wrapper | an operator server session | v0.33 · 2026-08-01 — no model-profile command or server session occurred; trigger did not fire | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | v0.33 · 2026-08-01 — registered 12-rule / 61-control vocabulary remained green and no new spelling appeared; trigger did not fire | none |
| `--features net` Rust 1.86 execution | a scoped cycle authorized to change evidence topology and an executable local or hosted lane that actually pins and runs the net path on Rust 1.86 | v0.33 · 2026-08-01 — no executable Rust-1.86 lane was added and workflow/run changes remain forbidden; trigger did not fire | none |
| Third configured publisher | a completed compliance review, then a separate admission decision | v0.33 · 2026-08-01 — no compliance review or admission decision occurred; trigger did not fire | none |
| `v0.8.0` / `v0.10.2` publication | operator-authorized push of both exact annotated objects | v0.33 · 2026-08-01 — neither historical tag was present remotely and no historical ref moved; trigger did not fire | none — no historical ref touched |
| `--skip-local-tag-verification` removal | both historical tags published plus a passing hosted full-history `cycle-check` without the flag | v0.33 · 2026-08-01 — both tags remained absent and no hosted verification changed the unchanged flag; trigger did not fire | none — the flag stays |
| Manifest retention/indexing | the manifest reaches its governed artifact byte boundary, or two consecutive clean `./run verify-artifacts` runs each take ≥1.00 s real | v0.33 · 2026-08-01 — operator-selected Fidelity B raised the manifest to 192,042 bytes / 332 pins; two complete runs matched every pin and both protected databases in 0.11 s and 0.10 s real, so neither trigger fired | Step 5 — completed with the exact through-v0.28 structural archive pin |
| Version literal in `app.py` | a cycle whose declared scope permits shell source changes | v0.33 · 2026-08-01 — release-authority precedence admits the unchanged version literal while no shell source or release value changed | none — `shell/intel_shell/**` is forbidden |
| Release-classification criteria with no executed control | an operator decision that prose adjudication is insufficient | v0.33 · 2026-08-01 — no such operator decision was supplied; trigger did not fire | none — recorded, not acted on |
| **Second `STATE.md` archival** | the export ceiling trigger fires, or `STATE.md` reaches its governed artifact byte boundary | v0.33 · 2026-08-01 — under explicit operator authorization, Step 5 performed Cut B ahead of the trigger: the 178,125-byte archive plus 194,542-byte pre-record live complement reconstructed the 372,667-byte pre-cut State exactly, and post-cut tree `91be7ac3b7c90f5407353136cde8e647f7af2f2f` exported 2,584,353 bytes; neither trigger clause had fired | **Step 4 and Step 5 — completed ahead of the trigger; the unchanged condition governs recurrence** |
| Planted-control line numbers re-derived by hand | a control-schema change, or a cycle in which the re-derived count exceeds the controls it protects | v0.33 · 2026-08-01 — Step 2's control-schema trigger fired and emitted mutation output re-derived 25 shifted existing values plus four new admission/selector values. Step 3's schema change then re-derived 29 shifted existing values plus one new same-kind-margin value at line 2401. Step 4's schema change re-derived 30 shifted existing values plus one new State-region value at line 2213. The latest shifted-existing count is fewer than the 67 registered controls protected | Step 2 and Step 3 and Step 4 — completed; count and re-derive from emitted output |
| Retention derivation across a version-family boundary | an active cycle whose name is not of the form `v0.<n>` — raising at `v1.0`–`v1.2`, silently under-excluding from `v1.3` onward | v0.33 · 2026-08-01 — v0.33 still matches `v0.<n>` and production uses the Git-derived tracked retained set; trigger did not fire | none — recorded, not acted on |
| Published-release divergence | the unpublished distance contains a measured runtime behaviour difference persisting across three consecutive closed cycles within the current publication epoch, or acquires any public-surface change | v0.33 · 2026-08-01 — v0.17.1 publication reset the count to zero, and the v0.33 activation/E0 distance carries no runtime or public-surface change; no fresh count started | Step 7 — restate the epoch count under the v0.32 reset rule |
| MSRV current-restatement membership | a current restatement of either Rust floor lands outside the registry without failing a check | v0.33 · 2026-08-01 — contextual floor predicates found no unregistered live current restatement; trigger did not fire | none — completed control remains active |
| Retention arithmetic fallback | the `retained_cycle_paths=None` branch produces an answer that differs from the tracked retained set in any construction a control or test relies on | v0.33 · 2026-08-01 — production supplied the Git-derived set while synthetic fallback divergence remained possible; trigger did not fire | none — recorded, not acted on |
| Optional cycle-ending audit disclosure | a closed cycle whose delivered export differs from its governed figure and which records no cycle-ending audit field | v0.33 · 2026-08-01 — optionality remains deliberate in the general checker and the open v0.33 runbook separately requires its own audit; no closed v0.33 construction exists yet | none — the v0.32 ruling stands; this runbook separately requires its own |

**Standing note on the SEC clock.** `config/core.json` names `sec-edgar-usgaap`
as a live source with no fixture and `robots_on_missing: deny`;
`config/schedule.json` gives it a 600-second interval. **That clock has never
issued a request.** It is a configured cadence nothing executes — rule zero
applied to operations rather than code. It is correctly deferred behind a
separate authorization and **this cycle does not authorize it**. It is recorded
here so that it is not mistaken for an executed property.

---

## Step 1 · E0 — Rebuild the entering state and settle G1–G6 🤖

**Objective.** Confirm `HEAD` is green and settle all six gates. **Every line
under `## Entering state` is a hypothesis.**

**Decision gate.** If the worktree is dirty apart from this untracked runbook, if
the v0.32 closing and audit commits are not where the entering state places
them, if published v0.17.1 identity has moved, or if any local gate fails at
entry — **record and stop.**

**Acceptance criteria.**

- All **20** `ci-local` jobs pass; `invariant-scan` passes its registered
  self-test with the rule and control totals stated; golden **11/11**; all pins
  verified twice with both real times recorded; both Python lanes reported as
  collected/passed/skipped **via `tools/test_population.py`**, never as a bare
  `N/N`.
- Published state confirmed **independently by direct remote inspection**, not
  from the closing record: remote `main` and the peeled `v0.17.1` tag both
  resolve to the closing commit, the annotated object has Git type `tag`, and
  the closing commit's immediate parent is the release commit.
- **The delivered-export identity is settled.** Measure `./run export-check`
  from the project root at the exact audit-child tree
  `70b7f93c94c67e43f6f4a29ede5823081955f3fa` and report the byte count. **The
  reviewer measured 2,734,366 bytes on the delivered export and inferred the
  audit child from a 4,979-byte difference; confirm or refute that inference by
  measurement and report the difference if any.**
- G1 settled **by execution at the real entry point**, with the emitted output
  of `./run cycle-check` recorded verbatim for each of the three constructions
  (absent header, renamed header, absent `STATE.md`) in a throwaway clone.
- G2 settled **by derivation**, with all three same-kind series computed and
  the honest-carrying-point named.
- G3 settled **by direct measurement and exhaustive search**, with every
  permanent-tail binding enumerated by file and line.
- G4 settled **by exhaustive search**, with the answer stated plainly even if
  the answer is "nothing."
- G5 settled **by execution against a throwaway clone**, with checklist figures
  before and after.
- G6 settled with both margins under same-kind denominators and the clause
  dependency stated.
- The deferred table's rows are rewritten with **v0.33** measured observations,
  and every trigger-bearing `ARCHITECTURE.md` row carries a v0.33 measurement.
- The governed-export exemption reported by the real entry point at activation
  is recorded **by name**.

**Done when** every gate carries a measured answer and the entering state is
either confirmed or corrected in `STATE.md`.

- [x] **E0**

---

## Step 2 · Close the publication-status admission gate 🤖

**Objective.** Make the publication-status family fail closed at its own
admission gate, and correct the `ARCHITECTURE.md` sentence that claims it
already does.

**Dependency gate.** Requires G1 settled. **If G1 refutes the fail-open finding
at the real entry point — that is, if `./run cycle-check` rejects all three
constructions — then this step's implementation is cancelled and the step
instead records the refutation and names which check supplied the floor.** A
reviewer finding that measurement contradicts is corrected, not defended.

**The shape.** Today `check_publication_status` returns silently when
`STATE.md` is absent and when `STATE_HEADER_RE` finds no match. Those returns
sit *above* every rule R12 exercises, so R12 can disable each rule inside the
family and still never observe the family being skipped entirely. **A gate that
admits a rule family to execution is itself a rule.**

**Acceptance criteria.**

- **The rejection precedes the acceptance.** Before the fix, record the real
  entry point's output for each of the three constructions. After the fix,
  record it again. Both are required; the second alone proves nothing.
- Absent `STATE.md`, absent `**As of:**` header, and a header present but
  unmatched by `STATE_HEADER_RE` each produce a **distinct, named defect** that
  fails the entry point. The three cases must be distinguishable in the emitted
  text; one generic message for three causes is not acceptable.
- **The relationship to `version_check.state_version()` is stated in the check's
  own emitted text or in a comment at the site.** Two tools parse the same
  header with two independently hand-written regexes for two different reasons.
  Whichever way the coupling is resolved, **it must be written down where the
  next reader will find it**, because a header edit satisfying one parse and
  not the other is possible in both directions.
- Registered R12 gains controls that plant **each** of the three admission-gate
  cases and observe the real entry point missing the plant when the branch is
  disabled. Every shifted `expected_line` value is **re-derived from real
  emitted self-test output**, never computed by hand, and the count of shifted
  values is recorded.
- `ARCHITECTURE.md`'s publication-reconciliation paragraph is corrected to state
  what R12 actually covers. **If G1 determined that the overstating sentence was
  introduced by a runbook this reviewer authored, it is recorded as a reviewer
  error in the closing record; if it was not, it is recorded as a finding. The
  classification follows the measurement.**
- Focused lifecycle tests pass with the count stated. Both Python lanes and the
  complete `ci-local` entry point pass **with the task box still open**, and the
  standalone post-task `./run golden` passes **11/11** with delta **0**.

**Done when** no construction of `STATE.md` causes the publication-status family
to report clean by examining nothing.

- [x] **ADMIT-GATE**

---

## Step 3 · Correct the export margin criterion 🤖

**Objective.** Make the governed export row's cycle-margin estimate use a
same-kind denominator, and state its evaluation point the way v0.31 taught us
to state the binding's.

**Dependency gate.** Requires G2 settled.

**The shape.** The governed *bytes* are correctly bound to the last field the
closing tree can already see — that rule is right and stays. **The margin
sentence beside them silently inherits that evaluation point while subtracting
a figure of a different kind.** The fix is not to move the governed binding. It
is to require the margin's two terms to come from the same series, and to name
which series.

**Acceptance criteria.**

- The corrected row states its denominator's **kind** as well as its value —
  governed→governed, closing→closing, or delivered→delivered — and the numerator
  comes from the same series.
- **The v0.32 figure is corrected forward, not rewritten.** The `5.65`
  measurement stays in its dated historical record as evidence of what was
  computed on 2026-08-01. The current row carries the corrected margin with a
  dated v0.33 observation. **A dated historical measurement is not edited to
  match a later understanding.**
- Whatever check reads the governed export field is extended so that a row whose
  margin terms come from different series is rejected, **or** the check's own
  emitted bound states explicitly that same-kind agreement is not executable
  and why. **One of these two, not neither.** If the bound is the answer, it
  must name the limit in the check's output, in the v0.32 Step 3 manner.
- If a control ships, R12 plants a mixed-kind row and observes the real entry
  point missing it when the branch is disabled; shifted `expected_line` values
  are re-derived from emitted output and counted.
- The complete entry point passes **20/20** with the task box open; golden
  **11/11**, delta **0**.

**Done when** the number that says how much room is left is computed from two
measurements of the same kind, or the check says out loud that it cannot check
that.

- [x] **MARGIN-KIND**

---

## Step 4 · Make the archival's eligible region executable 🤖

**Objective.** Before any byte moves, ship a check that knows which part of
`STATE.md` may be archived and what must never leave it.

**Dependency gate.** Requires G3 and G5 settled. **No byte may be written under
`docs/state-archive/**` in this step.** This step ships the contract; Step 5
performs the cut.

**The shape.** `STATE.md` is three regions, measured at the delivered tree:

| region | lines | bytes | archival eligibility |
|---|---|---|---|
| status header block | 1–4 | **2,405** | **never movable** — read by `cycle_check.STATE_HEADER_RE` and `version_check.state_version()` |
| dated cycle appends | 5–4,982 | **306,676** | **eligible**, oldest-first, cut only at a cycle-append boundary |
| permanent numbered tail `## 1.`–`## 7.` | 4,983–5,367 | **43,814** | **never movable** — carries the registered MSRV restatement and every external `STATE §N` anchor |

The permanent tail is load-bearing in ways the byte-count control cannot see:
`STATE.md:5320` carries `current correction: offline needs >= 1.78`, which
`version_check.OFFLINE_MSRV_RESTATEMENTS` reads as a **registered current
restatement**; and `§2`, `§5`, `§6`, and `§6b` are cited from
`crates/compliance/src/lib.rs`, `crates/ingest/src/arxiv_oai.rs`,
`rust-toolchain.toml`, `AGENTS.md`, `ARCHITECTURE.md`, `README.md`, and
`tools/version_check.py`. **All of those anchors resolve today. Nothing
executes any of them.**

**What is already protected, measured — do not rebuild it.** Executing the real
`tools/version_check.py` against throwaway trees:

| construction | real emitted result |
|---|---|
| over-cut carries the archive into the permanent tail | **REJECTED** — `STATE.md: current run-reference correction yielded zero extracted current restatements` |
| the registered restatement line alone is removed | **REJECTED** — same error |
| `## 5. Known limitations` renamed, everything else intact | **PASS (0.17.1)** |
| §1, §2, §4, §5 and §6 archived; §7 and the restatement kept | **PASS (0.17.1)** |

**The registered MSRV restatement already has a working reader — v0.32 Step 4's
zero-extraction rejection. Do not add a second one.** The last row is the gap
this step exists for: **an archival removing five sections, three of which are
cited from seven external files including two production Rust source comments
and `rust-toolchain.toml`, is silent.** Note also that the first row's rejection
is **incidental** — the over-cut is caught only because it happens to swallow
line 5320. An over-cut stopping one line short would pass.

**Acceptance criteria.**

- The check derives the three region boundaries from `STATE.md`'s own structure.
  **It does not carry a hardcoded line number, a hardcoded byte figure, or a
  hardcoded list of section numbers.** Hardcoded scope lists are this project's
  oldest named defect class and this step is the one most tempted by them.
- Every external `STATE §N` cross-reference is **derived** from the tracked file
  set and each is required to resolve to a heading that exists. A reference to a
  section that does not exist is a defect. **Report what the derivation finds,
  including whether `## 3.` is referenced by anything.**
- **The permanent tail's lower boundary is enforced in its own right, not via
  the restatement.** The measured incidental rejection above is not a floor: a
  cut that stops short of line 5320 must still fail.
- **The rejection precedes the acceptance.** Reproduce all four constructions in
  the table above at the complete entry point and record each emitted result
  verbatim, before and after the fix. The two that currently PASS must fail
  afterwards; **the two that already REJECT must still reject for the same
  stated reason and must not acquire a second, duplicate error.**
- R12 gains at least one control over the new rule family; shifted
  `expected_line` values are re-derived from emitted output and counted.
- `checklist-audit` does not fall. The complete entry point passes **20/20**
  with the task box open; golden **11/11**, delta **0**.

**Done when** a proposed cut that would break a binding fails a check instead of
being caught by a reviewer.

- [x] **REGION-CONTRACT**

---

## Step 5 · Perform the second `STATE.md` archival 🧑🤖

**Objective.** Execute the operation the nearest governed trigger exists to
force, ahead of the trigger, under explicit operator authorization.

**Dependency gate.** Requires Step 4 shipped and green. **If Step 4's contract
rejects the operator-selected cut, the cut changes — the contract does not.**

**🧑 Operator decision 1 — the cut point.** Measured options, all at the
delivered tree, with `STATE.md` currently at **352,895** bytes and its boundary
at **453,741**:

| option | archive through | cut line | archived bytes | live `STATE.md` after | margin after | cycles at +31,177 |
|---|---|---|---|---|---|---|
| **A — conservative** | v0.26 | **2,881** | 128,041 | 224,854 | 228,887 | **7.3** |
| **B — precedent-matching** | v0.28 | 2,095 | 178,125 | 174,770 | 278,971 | **8.9** |
| **C — retention-derived** | v0.30 | 1,052 | 243,098 | 109,797 | 343,944 | **11.0** |

**All three were executed in throwaway clones. Complement equality holds
exactly for each — archived plus live equals 352,895 bytes — and each post-cut
tree passes the real `version-check` at `0.17.1` with restatements steady at
22/1.78 and 3/0.17.1.** These are pre-flight measurements on a reviewer's
reconstruction, not on the repository; **E0 and this step re-measure them.**

**A's cut line is 2,881, not the v0.26 R-CLOSE line at 2,924.** The record
between them is v0.16.1's post-push verification, and v0.26 is the cycle that
published v0.16.1. **A cycle's records do not all sit below its R-CLOSE line.**
B and C are unaffected because v0.28, v0.29 and v0.30 all closed `no-release`
and produced no post-push record — which is luck, not structure.

**One structural caveat that bears on Option C specifically.** Option C's appeal
is that it is *derived* — it cuts at the export retention window's edge, so the
rule advances by itself. But `STATE.md`'s blocks are not uniformly ordered:
**every cycle from v0.22 through v0.31 writes its block newest-first, R-CLOSE at
the top and E0 at the bottom; v0.32 writes its block oldest-first, E0 at line 5
and R-CLOSE at 378.** A derived cut rule needs a reliable block-boundary
detector, and the file offers no per-cycle heading — only bold run-in
paragraphs whose ordering convention changed one cycle ago. **Step 4's contract
must handle both orderings, or Option C is not actually derivable and should be
selected on its byte reclaim alone.**

Option B most closely reproduces the v0.21 outcome, which archived **297,739**
bytes from a **453,741**-byte file and left roughly **156,000** live. **B is the
reviewer's recommendation** — it matches the precedent, buys nearly nine cycles,
and its cut point is clean by structure rather than by luck. The decision is
the operator's.

**🧑 Operator decision 2 — the fidelity claim.** G4 will report what detects a
corrupted archive. If the answer is "nothing," two options:

- **Option A — recorded bound.** Verify byte-for-byte at cut time, record the
  hash and the verification in the closing record, and state explicitly in
  `ARCHITECTURE.md` that this is a **one-time verification, not a standing
  control**. Cheap, honest, adds no manifest bytes.
- **Option B — manifest pin.** Register the archive in
  `config/protected-artifacts.json` so `./run verify-artifacts` checks it every
  run. Makes the claim executable. **Costs a governed-artifact edit and moves
  the manifest's byte figure**, which has its own dated trigger and its own
  99.43-cycle margin. Activates the conditionally usable manifest `allow` above.

**Neither is defaulted.** Option B is the stronger answer to rule zero; Option A
is the smaller blast radius. Both are defensible and the choice is the
operator's.

**Acceptance criteria.**

- The archive is written to `docs/state-archive/STATE-through-v0.<N>.md` where
  `<N>` is the selected cut, **byte-for-byte**, and the removal from live
  `STATE.md` is exactly the complement. **Prove it: the archived bytes plus the
  live remainder must equal the pre-cut file, and that equality is measured, not
  asserted.**
- Step 4's region contract passes on the post-cut tree. Every external
  `STATE §N` anchor still resolves. The registered MSRV restatement is still in
  the live file. The status header block is byte-unchanged.
- `./run version-check` passes at exact **0.17.1** with its restatement count
  stated. `./run cycle-check` passes with both artifact boundaries `bound`.
  **`checklist-audit` does not fall** — report the figures before and after.
- The post-cut `STATE.md` byte count and the post-cut project-root export are
  both measured and recorded **against the named trees they were measured on**.
- Both Python lanes and the complete `ci-local` entry point pass; golden
  **11/11**, delta **0**.
- The deferred `Second STATE.md archival` row records that the operation was
  performed **ahead of its trigger under operator authorization**. **The trigger
  text is not edited.** A row whose operation has been executed still states
  the unchanged condition under which it would recur.

**Done when** the archive exists, the live file is smaller by exactly the
archived amount, and every binding into `STATE.md` still resolves.

- [x] **ARCHIVE-CUT**

---

## Step 6 · RE-MEASURE — authenticate the exact candidate 🧑🤖

**Objective.** Put release-grade authenticated evidence on the exact candidate,
on a **fresh** ref that says what it is.

**Acceptance criteria.**

- The candidate is the exact clean tree. **The ref is fresh:**
  `codex/v0.33-evidence-<sha7>`, its prior non-existence confirmed by
  `git ls-remote` **before** any push, its post-push readback confirmed to
  resolve to the exact candidate, and both facts recorded. **A reused ref is a
  finding to record, not a detail to omit.**
- 🧑 The operator explicitly approves publishing the measured candidate to that
  new ref. This is the only remote mutation this step may perform.
- All seven executable hosted jobs pass. Every receipt, attestation, bundle, and
  persistence step passes. The repository verifier consumes the downloaded set,
  states accepted and rejected counts, and every accepted identity binds the
  exact candidate digest **and the fresh source ref**.
- Both shell lanes compared by `tools/test_population.py` with
  comparator-derived `collected`, `equivalent`, and `equivalent_passed`. **Every
  figure written is the comparator's output, never transcribed from a log.**
- All pins verified on the candidate; golden **11/11** locally and hosted.
- **No publisher request, no scheduler run, no model-profile command, no
  manifest registration** except under a selected Step 5 Option B, which is
  registered before this step, not during it.
- Remote `main`, the peeled `v0.17.1` tag, and its annotated tag object are
  re-measured after the run and confirmed unmoved.

**Done when** the candidate carries release-grade authenticated evidence on a
ref that says what it is.

- [ ] **RE-MEASURE**

---

## Step 7 · R-CLOSE — close v0.33 with a reasoned disposition 🧑🤖

**Objective.** Close v0.33 with an explicit, reasoned disposition.

**🧑 The operator's decision, and only the operator's.** Publication
authorization is a separate explicit act and is **not** implied by this runbook,
by green gates, or by hosted evidence. Two outcomes, neither defaulted:

- **`no-release`** — close on v0.33's own record and state **what the
  unpublished distance now contains**, measured against published v0.17.1. A
  distance of lifecycle controls, an archival, and cycle records is a reason;
  **"nothing shipped" is a weaker statement and must not be substituted for it.**
- **`release` at patch** — only if a step measured something belonging in users'
  hands. Under this cycle's declared scope such a measurement is itself a scope
  finding, and selecting this outcome means reopening the disposition **before**
  Step 6.

**Acceptance criteria.**

- The closing record names the closing date and the dated disposition, and —
  under `no-release` — enumerates the intentionally unreleased commits, with
  every version source and tag unchanged.
- **The governed export row in the closing tree equals the last governed field
  that tree can already see**, and the closing tree's own export goes only in
  the audit child's `cycle-ending review-export audit` field. **Its margin
  estimate uses Step 3's corrected same-kind rule.**
- Every declared permission is reconciled as used or unused, **by path**,
  including whether the conditionally usable manifest permission activated.
- The published-release divergence row restates the epoch count under v0.32's
  reset rule, with a dated v0.33 observation.
- Both governed byte boundaries are re-measured post-archival and each margin is
  restated in cycles under a **same-kind** denominator.
- Every reviewer error is recorded **in this file's header, not in the closing
  record**, because a provenance note is where a reader looks last and an error
  is what they should see first.
- The count of `expected_line` values shifted across the cycle is stated, and
  compared against the number of controls they protect.
- 🧑 The operator authorizes the disposition explicitly.

**Done when** v0.33 is closed on a record that says what it did and what it
deliberately did not.

- [ ] **R-CLOSE**

---

## Standing prohibitions

These hold for every step unless a step names its exception explicitly.

1. **No publisher request, harvest, scheduled process, service, or
   model-profile command.** The SEC 600-second clock is not authorized to issue
   traffic by this cycle or by anything in it.
2. **No production source, workflow, dependency, schema, or release-value
   change.** Every such path is `forbid`.
3. **No closed cycle document is moved, edited, or deleted.**
4. **No historical ref is created, moved, or deleted**, including `v0.8.0` and
   `v0.10.2`.
5. **No `expected_line` value is computed by hand.** Every one is re-derived
   from real emitted self-test output and the count is recorded.
6. **No figure is transcribed from a runner log** where a comparator exists.
7. **Every export figure names the tree it was measured on.**
8. **No dated historical measurement is edited to match a later understanding.**
   Corrections go forward.
9. **`checklist-audit` must not fall**, and the retraction count stays at
   **three** unless a twice-verified measured false claim in an immutable
   published record is produced.
10. **No write under `docs/state-archive/**` from any step other than Step 5.**

---

## Cycle checklist

- [x] Worktree clean at entry apart from this untracked runbook
- [x] `AGENTS.md` active-cycle declaration advanced to **v0.33**
- [x] `PROGRESS-v0.33.md` created and appended per step, after each
      implementation commit exists
- [x] Retention advanced; the activation rejection text recorded verbatim if the
      stale-glob construction is exercised
- [x] All six gates settled with measured answers
- [x] Deferred table rewritten with v0.33 observations, **triggers unchanged**
- [x] Every trigger-bearing `ARCHITECTURE.md` row carries a v0.33 measurement
- [x] Governed export row carries a same-kind margin
- [ ] Both governed byte boundaries re-measured post-archival
- [ ] Closing record + append-only audit child, per the tagged-close protocol
- [ ] Cycle-ending review-export audit field present in the audit child

---

## Provenance

**Measured by this reviewer, by executing real code.** The publication-status
fail-open: `tools/cycle_check.py`'s `check_publication_status` was loaded from
the delivered export and called directly against four constructions of
`STATE.md` with a valid closed-release runbook present. A valid `**As of:**`
header produced **1** error; an absent header, a renamed header, and an absent
`STATE.md` each produced **0**. `version_check.state_version()` was read and
raises on a missing header — **that is a read, not an execution**, and G1 owns
confirming it at the composite entry point.

**Measured by this reviewer, by executing real code against reconstructed
trees (the r2 pre-flight).** All three Step 5 cuts and four mis-cut
constructions were built in throwaway copies of the delivered export, each
initialized as a Git repository so tracked-file enumeration would run, and
`tools/version_check.py` was executed against each. Baseline: **PASS (0.17.1)**,
22 MSRV restatements, 3 release restatements, `tracked=156`. Cuts A, B and C:
**PASS (0.17.1)**, restatements unchanged, `tracked=157`. Over-cut and
restatement-removal: **rejected** with the zero-extraction error. Renamed `## 5.`
heading and five-section removal: **PASS**. Complement equality verified byte
-exact for all three cuts. **These trees are reconstructions from an XML export,
not clones of the repository, and `cycle-check`, `checklist-audit` and
`export-check` were not exercised because they depend on real commit history —
E0 owns all of it at the real entry points.**

**Measured by this reviewer, by direct file measurement of the delivered
export.** The export at **2,734,366 bytes / 153 files**; `STATE.md` at
**352,895 bytes**, decomposing exactly as **2,405 + 306,676 + 43,814**; every
figure in the Step 5 cut table; the v0.30 pair at **106,928 bytes**; the
`STATE §N` cross-reference inventory; the absence of a `## 3.` heading; that
`tools/checklist_audit.py` enumerates execution runbooks and does not read
`STATE.md`; that `tools/export_check.py:43` and `tools/version_check.py:318`
both exclude `docs/state-archive/`; the per-cycle block ordering — v0.22 through
v0.31 newest-first, v0.32 oldest-first — and the placement of v0.16.1's
post-push record at line 2881, above v0.26's R-CLOSE.

**Derived by arithmetic from recorded figures.** All three export series and
their margins; the `STATE.md` growth series **289,117 → 321,718 → 352,895**
(+32,601, +31,177 closing-to-closing) and **324,290 → 352,895** (+28,605
delivered-to-delivered); the 3.09–3.53 and 3.32–3.81 cycle margins.

**Inferred, not measured.** That the delivered export corresponds to audit child
`70b7f93c94c67e43f6f4a29ede5823081955f3fa`. The 4,979-byte difference from the
recorded closing-tree figure is consistent with it; **consistency is not
identity, and E0 owns the confirmation.**

**Asserted and not verified.** Every line under `## Entering state` not listed
above. All hosted run contents, ref topology, remote state, and every figure
Codex reported for trees this reviewer did not receive. Whether
`./run cycle-check` as a whole fails open on the three constructions — only the
single function was executed.

**Not verifiable by this reviewer at all.** That no historical cycle document
was moved, edited, or deleted: retention depth 3 exports only v0.30–v0.32, so
v0.1 through v0.29 are outside reach and that claim rests on `checklist-audit`
and on Codex's measurement. Also unverifiable here: the contents of
`docs/state-archive/STATE-through-v0.21.md`, which is export-excluded — **so
G4's fidelity question is one this reviewer raised without being able to check
the existing archive's own integrity, and that limitation is stated rather than
left implied.**

**Two reviewer errors are recorded in this file's header** rather than here. The
second was found by executing the runbook's own Step 5 before handing it over,
which is the only reason r1's wrong cut point did not reach implementation.
**A pre-flight is cheaper than a cycle.**

**One near-error, recorded because the discipline is cheap.** In drafting G3
this reviewer initially concluded that `README.md`'s citation of `STATE §6b`
was a broken cross-reference, on the strength of a faulty heading grep. `§6b`
exists at `STATE.md:5116`. The finding was corrected before it reached this
runbook; it is noted here because a finding caught by better measurement is the
same event as a finding caught too late, minus the cost.
