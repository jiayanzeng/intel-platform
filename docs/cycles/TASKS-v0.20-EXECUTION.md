# TASKS-v0.20-EXECUTION.md — the controls that check the record

v0.19 made the publication status executable and immediately proved why that
mattered: the project's prior false remote-main/tag status had passed every
check it ran. The correction shipped, v0.15.3 published, and then the new
control failed on its own release.

**It failed because it is unsatisfiable by construction, not because the record
is false.** `check_publication_status`'s rule 2 requires the `STATE.md` header's
asserted `origin/main` to equal the measured ref. A closing audit commit can
only assert the pre-push value — the post-push value *is that commit's own
hash*, which does not exist while the commit is being written. Every successor
inherits the same fixed point: any commit `D` that records `origin/main = C`
becomes false the moment `D` is pushed and `origin/main = D`.

The other two labels in the same rule — annotated tag object and tag target —
have no such problem. They are immutable and knowable at write time. **The
defect is specific to the one ref whose value the act of recording changes.**

This cycle does four things and deliberately no more:

1. **corrects the self-reference defect structurally**, so the class is removed
   rather than tested for;
2. **makes the review export's completeness a derived, executing check** instead
   of a hand verification performed once;
3. **fixes the exclusion pattern that misses the two oldest cycles**;
4. **puts the export's two operating rules into `AGENTS.md`**, where they survive
   the next contributor.

**The public `/v1/*` JSON bodies, the SQLite schema, the robots matcher, the
politeness limiter, and the golden regression's 11 invariants are unchanged.
Golden stays 11/11 byte-identical through every task. No crate under `crates/`
or `apps/` is modified by any step in this file.**

**Version disposition.** Default is a patch release **`v0.15.4`**. No `/v1/*`
route or body moves and no crate changes; the diff is tooling, configuration,
and documentation. **`v0.16.0`** applies only if a `/v1/*` body or route moves.
**The publication decision has its own trigger and it is already visible:
published `main` is currently failing CI on a control this cycle corrects.**
Record the fired trigger at Step 7; do not inherit the default.

---

## Entering state (asserted, not yet verified)

**Every sentence here is a hypothesis until Step 1 (E0) measures it.**

- `v0.15.3` is published. Release commit
  `dbff27d559193847dd2028c435c686ba656dac85`, annotated tag object
  `2039e01475b43285ecbbf2739f788b7f855a5603`. v0.19 is closed 7/7. **None of
  this is reopened.** Every correction here is a forward append.
- Remote and local `origin/main` is closing audit commit
  `692069ead0b8823d6874d8f2fc0a593d9f26704f`.
- **Hosted CI at remote head is FAILING.** Run `30417274925` failed on
  `cycle-check`'s publication assertion freshness rule. Six other job instances
  succeeded; only one job runs `cycle-check`, because only one checkout declares
  `fetch-depth: 0`.
- Local `main` is one commit ahead at forward audit `72b6f42`, intentionally
  unpushed. **This is consistent with the project's push rhythm** — remote `main`
  advances only at publication, and publication-audit appends have always landed
  in the following cycle. It is not an anomaly to be resolved out of band.
- Protected pins are **176** — **174** evidence plus **2** authorization
  surfaces. Golden is **11/11**. Local CI is **20/20** with **133** workspace
  tests, **55** net tests (**29** `intel-ingest` + **26** `cored`), shell
  **248/248** on Python 3.11 and 3.12, `invariant-scan` **11/11 rules /
  23 controls**.
- The review export is **145 files**; **88** tracked files under `crates/`,
  `apps/`, `tools/`, `shell/`. v0.19's EXPORT-BUDGET recorded 89 — correct when
  measured, and reduced by one when PREVIEW-DISPOSITION later deleted the
  preview binary.
- A4, the editable-L1 controller residual, the R3/R4 open-bottom deny-lists, the
  active-runbook measured-value heuristic, T7 robots single-flight, and the
  deferred stale-policy fallback (NEGATIVE-CACHE Decision B) remain open. L2
  remains scheduled. **No step in this file closes or narrows any of them.**

---

## Drafted gates

| Gate | Where | Hypothesis |
|---|---|---|
| **G1** [P1] | `tools/cycle_check.py`, `check_publication_status` rule 2; `STATE_REF_ASSERTIONS` | **The freshness rule for `origin/main` has no satisfying assignment.** The header can only assert a pre-push value; the push makes the asserting commit itself the new value. Demonstrate the fixed point by construction: show that correcting the header to the current ref passes locally and would fail again on push. The tag-object and tag-target labels are unaffected and must stay. |
| **G2** [P1] | `tools/cycle_check.py:410–418`, `:445–448` | **The same check has two silent no-op paths.** If `merge-base --is-ancestor` cannot resolve — a shallow checkout, an unfetched tag — `reachable is None` and the function `return`s with no error. If a ref fails to resolve, `measured is None` and the label is `continue`d. **A control that silently does nothing when its inputs are missing is decorative**, and this one is protected today only by a single `fetch-depth: 0` in one job. |
| **G3** [P2] | `repomix.config.json` `customPatterns` | **The exclusion misses the two oldest cycles.** `docs/cycles/{TASKS,PROGRESS}-v0.{8,9,10,11}*` does not match `TASKS-v0.6.md` or `TASKS-v0.7.md` (**30,842 bytes**), which predate the enumerated floor and lack the `-EXECUTION` suffix. The implemented rule is "exclude v0.8 through v0.11"; the stated intent was "closed cycles through v0.11." |
| **G4** [P2] | `run`; `AGENTS.md` | **Nothing executes the export budget and nothing records its rules.** v0.19 Step 3's completeness criteria were verified once, by hand, at one commit. `run` has no export subcommand. `AGENTS.md` contains no reference to repomix, to root execution, or to why `enableSecurityCheck` must stay `false`. Two known silent-omission modes exist: a non-root invocation drops `Cargo.lock`, and the security scan dropped a Rust source (340 collected, 339 included) before it was disabled. |
| **G5** [P3] | `PENDING_PUBLICATION_RE` | **The pending-publication regex is proximity-based.** It matches `publication` followed within 240 characters by `pending` or `outstanding`. Confirm whether an unrelated nearby "outstanding" can false-fire, and either bound the pattern or record the looseness as accepted. **A refuted G5 is deleted, not worked around.** |

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate.

- **🤖 = Codex executes and self-verifies end to end** — no publication, no push.
- **🧑 = exactly one named operator action or decision.**

**Dependency gates.** **Step 2 blocks everything.** Until the self-reference
defect is corrected, every subsequent step's `cycle-check` acceptance is
measured against a control that cannot pass at a publication commit. Step 3
precedes Step 4, so the derived check has a corrected pattern to verify. Step 6
is blocked by every preceding implementation step; Step 7 by Step 6.

### Cycle activation (before E0)

In a separate preparatory implementation/audit pair: confirm the worktree is
clean, record the measured `origin/main`, and commit **only** this runbook at
`docs/cycles/TASKS-v0.20-EXECUTION.md`, the `AGENTS.md` header moving the active
declaration from v0.19 to v0.20, and a new `docs/cycles/PROGRESS-v0.20.md`.
**Local `main` already carries the unpushed forward audit `72b6f42`; activation
sits on top of it and does not amend, rebase, or squash it.** Run `cycle-check`
and `checklist-audit`, and **record that `cycle-check` passes locally only
because `origin/main` has not yet moved** — that passing result is evidence for
G1, not evidence the control is sound.

### Global definition of done

Protected hashes exact; all **176** pins match until Step 6 adds more; golden
**11/11 byte-identical**; `./run version-check` green; zero rustc warnings on
offline and net builds; all Rust tests green; all shell tests green under Python
3.11 **and** 3.12; clippy, fmt, ShellCheck, floor byte-compilation, and locked
Rust 1.78 green.

---

## Deferred means deferred

| Deferred item | Unchanged trigger | v0.20 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none |
| NEGATIVE-CACHE Decision B (stale-policy fallback) | a measured live transient robots outage for an admitted publisher while a usable last-known-good policy exists, plus operator authorization | none |
| Postgres / pgvector / multi-host seam | unchanged | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none |
| L2 forced-command wrapper | an operator server session | none — remains scheduled |
| R3/R4 open-bottom coverage | a spelling outside registered vocabulary | none |
| Second configured publisher | a separate compliance review per publisher | none — **do not add a source** |
| CI-runner evidence | an authenticated receipt set with identified matrix legs, durably committed | **re-measure at the new release commit — discharged by Step 6** |

---

## Step 1 · E0 — Rebuild the entering state, including the red one 🤖

**Objective.** Confirm the local matrix is green, confirm that the *hosted* state
is not, and settle G1–G5.

**Gate.** Read-only repository, object, and local execution measurements plus
`PROGRESS-v0.20.md` and this runbook's status records only. No production path,
tool, configuration, dependency, protected artifact, or public surface changes.

**Steps.**

1. Run the full entering matrix and standalone `./run golden`, plus
   `verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
   `version-check`, `invariant-scan`. **Record both Python lanes.**
2. **Record the entering hosted state as failing, with its run id, the failing
   job, and the exact error text.** Do not write "entering matrix green" on the
   strength of local runs while remote head is red. A local pass and a hosted
   failure at different commits are two facts, and both belong in the record.
3. **Confirm G1 as a fixed point, not just as a failure.** Show three
   measurements: (a) `cycle-check` passes at local `72b6f42` because
   `origin/main` still equals the value its header asserts; (b) the same content
   fails against a simulated post-push ref; (c) no header content exists that
   satisfies the rule both before and after its own push. **(c) is the finding**
   — a single failing run only shows the header was stale.
4. **Confirm G2 by construction.** In a disposable clone, shallow the checkout
   or remove the tag and show `check_publication_status` returning with **zero
   errors** over a header the full-history checkout rejects. Record the exit code
   and the empty error list.
5. **Confirm G3 by measurement.** List the files the current pattern excludes and
   the `docs/cycles/` files it retains, with byte totals.
6. **Confirm G4.** Show `run` has no export subcommand and `AGENTS.md` no
   repomix reference, and re-derive the expected source set from `git ls-files`
   for `crates/`, `apps/`, `tools/`, `shell/`. **Reconcile 88 against v0.19's
   recorded 89** and name the deleted preview binary as the difference, so the
   discrepancy is closed as drift-absorbed rather than left as an open question.
7. **Confirm or refute G5** with a constructed header string.
8. Re-verify the published `v0.15.3` objects and all **176** pins unchanged.

**Acceptance criteria.** Local matrix captured with both interpreters named ·
hosted failure recorded with run id, job, and error text · G1 demonstrated as a
fixed point with all three measurements · G2 reproduced with a zero-error silent
return · G3 and G4 measured · G5 confirmed or refuted · 88-versus-89 reconciled ·
published objects and 176 pins re-verified · golden 11/11.

**Done when** the entering state includes the part of it that is red.

---

## Step 2 · SELF-REF (G1, G2) — Remove the class, do not test for it 🤖

**Objective.** Make the publication reconciliation satisfiable at a publication
commit, and make its unavailable-input paths loud.

**Gate.** `tools/cycle_check.py`, its focused shell tests, `STATE.md`'s header,
and status records. **Blocked on E0 confirming G1 and G2.** No closed runbook,
historical append, dated closing record, crate, dependency, schema, protected
database, or public surface changes.

**Steps.**

1. **Remove `origin/main` from the freshness comparison and replace it with a
   structural prohibition:** the `STATE.md` header block must not assert a
   literal 40-hex `origin/main` value at all. Reasons to record in the code, not
   only here:
   - `origin/main` is the one ref whose value the act of recording changes. Tag
     object and tag target are immutable at write time and their freshness rules
     **stay exactly as they are**.
   - A mutable ref measurement belongs in the dated append-only body, which this
     check already excludes by design. Moving it there is not a loosening; it is
     putting a measurement where measurements go.
   - Inverting "must be current" into "must not be asserted" makes the defect
     impossible instead of detectable. **Coverage of the original v0.15.2 defect
     is preserved by rule 1**, which is the rule that actually caught it.
2. **Fail-before is the repository itself, again.** The header at `72b6f42`
   asserts a literal `origin/main` hash. Run the corrected check against it and
   capture the non-zero exit and its message verbatim.
3. **Make G2's silent paths loud.** An unresolvable tag, an unresolvable ref, or
   an ancestry query that cannot be answered must produce a named skip that the
   caller reports, or an error — never a bare `return` and never a `continue`
   that leaves the loop looking exercised. **Add a control that proves the
   check reports something when its inputs are absent.**
4. Add focused tests for: the prohibition firing; a header without a literal
   `origin/main` passing; the tag-object and tag-target freshness rules still
   firing on a wrong value; and each unavailable-input path reporting.
5. **Then** rewrite the `STATE.md` header to carry the disposition, the version,
   the annotated tag object, and the release commit — and **no `origin/main`
   hash**. Move the ref measurement into a dated body append.
6. Re-run every status tool and record them green.
7. **Do not weaken rule 1.** A reachable annotated release still cannot coexist
   with a header calling its publication pending.

**Acceptance criteria.** Corrected check fails at the entering content with its
message captured · focused tests cover the prohibition, a passing header, both
retained freshness labels, and every unavailable-input report · no bare `return`
or `continue` remains on an unresolvable input · rule 1 unchanged and re-proven ·
header carries no literal `origin/main` hash · the ref measurement appears in a
dated body append · all status tools green · `invariant-scan` unchanged or
increased · golden 11/11.

**Done when** a commit can record its own publication without lying and without
failing.

---

## Step 3 · EXPORT-PATTERN (G3) — The rule does what it says 🤖

**Objective.** Make the exclusion cover the cycles it claims to cover.

**Gate.** `repomix.config.json` and status records. **No repository file is
deleted.** No tool, crate, dependency, protected artifact, or public surface
changes.

**Steps.**

1. Replace the enumerated `v0.{8,9,10,11}` floor with a pattern that covers
   every closed cycle through v0.11 **including `TASKS-v0.6.md` and
   `TASKS-v0.7.md`**, which carry no `-EXECUTION` suffix.
2. **State the floor as a rule, not a list.** If the pattern language cannot
   express "through v0.11" without enumeration, say so and enumerate completely —
   an enumeration that is known-complete is honest; one that silently misses two
   files is not.
3. Re-run the export **from the project root** and record bytes and file count
   before and after.
4. Confirm nothing outside `docs/cycles/` changed inclusion.

**Acceptance criteria.** `TASKS-v0.6.md` and `TASKS-v0.7.md` excluded · every
`docs/cycles/` file from v0.12 onward retained · export bytes and file count
recorded before and after · no repository file deleted · no non-`docs/cycles/`
inclusion change · `verify-artifacts` **176/176** and protected databases
**2/2** after · golden 11/11.

---

## Step 4 · EXPORT-CHECK (G4) — Derive the expected set, do not pin it 🤖

**Objective.** Turn the export's completeness from a one-time hand verification
into an executing check.

**Gate.** `run`, a new export checker under `tools/`, its shell tests, `run`'s
authorization-pin record in `config/protected-artifacts.json`, and status
records. **Blocked on Step 3.** No crate, dependency, schema, protected
database, evidence artifact, or public surface changes.

**Steps.**

1. Add `./run export-check`. It **derives** the expected source set from
   `git ls-files` for `crates/`, `apps/`, `tools/`, `shell/` and compares it
   against the paths actually present in a freshly written export. **Do not pin a
   count.** The count legitimately drifts — it moved 89 → 88 when the preview
   binary was deleted — and a pinned number would have turned that correct change
   into a false failure.
2. Additionally require the presence of `Cargo.lock`,
   `config/protected-artifacts.json`, `AGENTS.md`, `run`, `Cargo.toml`,
   `rust-toolchain.toml`, and `.github/workflows/ci.yml`.
3. **Fail-before controls, both of the known silent-omission modes:** run the
   export from a subdirectory and prove the check reports the missing
   `Cargo.lock`; re-enable `enableSecurityCheck` in a disposable copy of the
   config and prove the check reports the omitted source. Capture both non-zero
   exits. **Restore the real configuration afterwards and show it restored by
   hash.**
4. **Do not add `export-check` to `ci-local` or `ci.yml` if it requires writing a
   multi-megabyte file or a network-fetched toolchain.** State plainly whether it
   is a hosted gate or an operator-local one; an operator-local check that says
   so is honest, and one silently assumed to run in CI is not.
5. Record the `run` authorization-pin movement with its before/after hashes and
   byte sizes, and confirm the model-profile functions, dispatch, and
   authorization policy are unchanged.

**Acceptance criteria.** Expected set derived from `git ls-files`, no pinned
count · both fail-before controls captured with non-zero exits · configuration
restored and hash-verified · hosted-versus-local status stated explicitly ·
`run` pin updated with before/after hashes · manifest validation and
`verify-artifacts` all pins exact · golden 11/11.

---

## Step 5 · EXPORT-CONTRACT (G4) — Two rules that outlive the person who learned them 🤖

**Objective.** Put the export's operating rules where the next contributor will
read them.

**Gate.** `AGENTS.md`, `ARCHITECTURE.md` if the invariant table is the right
home, and status records. No tool, crate, configuration, dependency, protected
artifact, or public surface changes.

**Steps.**

1. Record in `AGENTS.md`: **the export is written from the project root**, and
   the reason — a non-root invocation does not load `repomix.config.json` and
   silently drops `Cargo.lock`, which is the root cause of the lockfile drift
   this project already paid for once.
2. Record in `AGENTS.md`: **`enableSecurityCheck` stays `false`**, and the
   reason — it silently omitted a Rust source (340 collected, 339 included), and
   registered self-testing invariant R4 is the credential control. **Name the
   measurement**, so the rule cannot be re-litigated from intuition.
3. Point both rules at `./run export-check` as the thing that catches a
   violation, so the documentation and the executable agree.
4. **Do not turn either rule into a new hard constraint number** unless the
   existing HC series is genuinely the right home; an operating rule that reads
   as an invariant it is not is its own kind of false claim.

**Acceptance criteria.** Both rules recorded with their measured reasons · both
point at the executing check · no HC renumbering unless justified in the same
commit · `checklist-audit` and `cycle-check` green · golden 11/11.

---

## Step 6 · RE-MEASURE 🤖🧑

**Objective.** Produce release-grade hosted evidence for the v0.20 candidate.

**Gate.** 🧑 **One narrow authorization: a non-`main` branch push.** Remote
mutation is limited to the exact candidate branch and its authenticated hosted
evidence dispatch. Repository admission is limited to that run's signed
receipt/bundle pairs, the release-posture deferred-audit report,
`config/protected-artifacts.json`, and status records. No tag, `main` advance,
publication, product path, public surface, dependency, lockfile, schema, or
protected database changes.

**Steps.**

1. Push the candidate to `candidate/<version the trigger sets>`. **Name the
   branch after the decided version, not before the decision.**
2. **Read the remote branch's `ci.yml` and confirm it contains every invocation
   you expect before dispatching**, and that its blob equals the local one.
3. Dispatch with `publish_evidence: true` and `audit_sha` set to the candidate.
4. **Read every count out of the hosted log**, not from job status, and compare
   each against the local measurement **at the same commit**.
5. **Confirm the corrected `cycle-check` passes in the hosted job**, and record
   which job ran it and at what checkout depth. This is the one control this
   cycle exists to fix; a hosted green here is the acceptance, not the local run.
6. Commit the signed receipt/bundle set, re-run `./run verify-artifacts` and
   `./run evidence-report`, and record the new pin count in `STATE.md`,
   `PROGRESS-v0.20.md`, and the pending closing record.
7. Run `./run audit-deferred` in release posture with attestations required.

**Acceptance criteria.** Hosted run pinned to the candidate · every count read
from the log and equal to local at that commit · corrected `cycle-check`
green in the hosted job, with the job and depth named · identity set matches the
derived value · signed set committed and re-derived · new pin count in three
places · `origin/main` unchanged, no tag · golden 11/11.

---

## Step 7 · R-CLOSE 🧑🤖

**Objective.** Close the cycle with a measured record, and turn published `main`
green.

**Gate.** Steps 1–6 complete and boxed. Worktree clean. **🧑 One operator
decision: publication.**

**Steps.**

1. Re-run the complete definition of done at the release commit and capture it.
2. Record the version choice and the trigger that fired.
3. **State the publication trigger explicitly: published `main` was failing CI
   on a control this cycle corrects.** A tooling-only cycle would otherwise be a
   legitimate no-release, as v0.14 was; that is not this case, and the record
   must say why.
4. Record evidence candidate and release commit as **separate named fields**.
5. **State the release disposition as of a date**, in the form
   `cycle_check.py`'s validator reads.
6. **Record G1 honestly as a specification defect, not an implementation one.**
   The v0.19 runbook specified a freshness rule for a ref whose value the act of
   recording changes; `tools/cycle_check.py` implemented that specification
   faithfully. **Do not attribute it to the implementation, and do not describe
   the v0.19 control as having been wrong to add** — it caught a real false
   status before it caught itself. Retractions stay at three unless a measured
   false published claim says otherwise.
7. **Record `72b6f42` by name** as the forward audit that was held unpushed, and
   state that it landed in this cycle's push rather than out of band.
8. Confirm after the push that hosted CI at the new remote head is **green**, and
   record the run id. **This is the cycle's actual product.** If it is not green,
   that is the finding and the cycle does not close on a claim.
9. Classify every diff path exactly once in `STATE.md`; update `CHANGELOG.md`,
   `README.md`, and the release authorities.
10. Reconcile `ARCHITECTURE.md`. **A4, the L1 controller residual, the R3/R4
    open-bottom limitations, the measured-value heuristic, T7, and NEGATIVE-CACHE
    Decision B must all still read as open.**
11. Check R-CLOSE's box and replace the pending heading with the canonical
    `Cycle closed:` record **in one commit**.
12. **Carry the one-publisher fact forward unchanged.**

---

## Cycle checklist

- [x] **E0** — local matrix with both interpreters; hosted failure recorded with
  run id, job, and error text; G1 shown as a fixed point in three measurements;
  G2 reproduced as a zero-error silent return; G3/G4 measured; G5 confirmed or
  refuted; 88-versus-89 reconciled
- [x] **SELF-REF** — corrected check fails at the entering content; literal
  `origin/main` prohibited in the header; tag-object and tag-target freshness
  retained; every unavailable-input path reports; rule 1 unchanged and re-proven
- [ ] **EXPORT-PATTERN** — `TASKS-v0.6.md` and `TASKS-v0.7.md` excluded; v0.12+
  retained; before/after sizes recorded; no file deleted
- [ ] **EXPORT-CHECK** — expected set derived from `git ls-files`, no pinned
  count; both silent-omission fail-befores captured; configuration restored by
  hash; hosted-versus-local status stated; `run` pin updated
- [ ] **EXPORT-CONTRACT** — both rules in `AGENTS.md` with measured reasons and
  pointed at the executing check
- [ ] **RE-MEASURE** — hosted run pinned; counts equal local at the same commit;
  corrected `cycle-check` green in the hosted job with job and depth named
- [ ] **R-CLOSE** — version cites its trigger; publication trigger stated as the
  red published head; G1 recorded as a specification defect; post-push hosted CI
  confirmed green with its run id; all open items still open

---

## Execution records

### 2026-07-29 · E0

PASS. The read-only Gate contains every acceptance surface: only this status
record, the E0 checklist box, and the append-only v0.20 progress record move.
`STATE.md` remains blob
`fb996dc34c41b81da8418946896898c3125a3ad7`, byte-identical to the entering
tree.

- **Local matrix:** the first sandboxed `./run ci-local` was a permission
  non-result when its loopback wire fixture could not bind. The identical
  permitted command passed **20/20** with **133** workspace tests, **55** net
  tests (**29** `intel-ingest` + **26** `cored`), shell **248/248** on Python
  3.11.4, zero rustc/clippy/fmt/ShellCheck failures, locked Rust 1.78,
  `invariant-scan` **11/11 rules / 23 controls**, all **176/176** pins,
  protected databases **2/2**, and golden **11/11**. A clean constrained
  Python 3.12.13 rebuild resolved **21/21** packages and independently passed
  shell **248/248**. Its first restricted package-resolution attempt was a DNS
  permission non-result; the permitted retry resolved the exact constraints.
  Standalone `./run golden` passed **11/11**, delta **0**. Standalone
  `verify-artifacts`, `cycle-check`, `checklist-audit`, `progress-check`,
  `version-check`, and `invariant-scan` all passed.
- **Hosted red state:** GitHub run `30417274925` is still **failure** at exact
  remote head `692069ead0b8823d6874d8f2fc0a593d9f26704f`. The runbook draft
  recorded attempt 1; E0 found that the same run had since been rerun and
  measured attempt **2**. Six blocking job instances succeeded. The sole
  failure is job `shell (Python 3.11)`, step
  `active cycle and amendment consistency`, whose exact checker finding is:

  > `cycle-check: ERROR: STATE.md: publication assertion freshness: origin/main asserts 344124819cb3c554f851d0cac3f0f1ed08d1aa10, but the measured ref is 692069ead0b8823d6874d8f2fc0a593d9f26704f`

  The next line is `cycle-check: FAIL (1 defect(s))`; the process exited 1.
  This is a hosted failure, not part of a green entering matrix.
- **G1 — CONFIRMED as a fixed point.** In a disposable full-history clone,
  exact commit `72b6f425114e06b1e148e0aa360e280a690e4f0c` passed
  `cycle-check` while `origin/main` remained the header's asserted
  `692069ead0b8823d6874d8f2fc0a593d9f26704f`. Moving only the simulated
  post-push tracking ref to `72b6f42…` made the same immutable content fail,
  reporting asserted `692069e…` versus measured `72b6f42…`. The construction
  then evaluated the only two candidate ref literals plus a third value:
  the pre-push literal passes only before the push, the post-push literal
  passes only afterward, and neither state accepts a third value. Because the
  two refs differ, the reported satisfiable result is **false**. No literal
  header content can satisfy both states of its own push.
- **G2 — CONFIRMED in both silent paths.** Against the full-history clone and
  deliberately stale header, `check_publication_status` returned one error.
  Removing only the `v0.15.3` tag made the same function return exit **0** with
  `errors=[]`. A separate depth-1 clone fetched the tag object and target but
  not the connecting history; `git merge-base --is-ancestor` exited **1**,
  while `check_publication_status` again returned exit **0** with `errors=[]`
  despite the stale literal `origin/main`. Both unavailable-input paths can
  therefore make the control silently decorative.
- **G3 — CONFIRMED with corrected quantities.** Root-run Repomix 1.17.0
  produced **2,713,184 characters / 147 files** and a **2,718,308-byte** XML
  export. The current pattern excludes **17** cycle files totaling **657,725
  bytes** and retains **20** cycle files totaling **633,876 bytes**. The
  retained set includes `TASKS-v0.6.md` (**14,972 bytes**) and
  `TASKS-v0.7.md` (**16,175 bytes**), totaling **31,147 bytes** rather than the
  draft's **30,842**. Every v0.12+ cycle file is retained.
- **G4 — CONFIRMED and the source-count drift reconciled.** `./run help`
  contains no export command, and repository search finds no `repomix` or
  `export-check` reference in either `run` or `AGENTS.md`. The set derived from
  `git ls-files` under `crates/`, `apps/`, `tools/`, and `shell/` is **88**,
  and the export contains all **88/88**. The EXPORT-BUDGET audit commit had
  **89**; the sole tracked deletion from that set is
  `crates/ingest/src/bin/robots_preview.rs`, retired by
  PREVIEW-DISPOSITION. The difference is fully drift-absorbed.
- **G5 — CONFIRMED and accepted as bounded looseness.** The constructed header
  `publication is complete and exact. An unrelated export review has
  outstanding documentation` matched from `publication` through the unrelated
  `outstanding`. The false positive is accepted for this cycle because the
  expression is bounded to the live header paragraph and can only cause a loud
  conservative refusal, not a false pass; this cycle does not expand into a
  fifth tool change.
- **Final integrity:** remote inspection re-read `main` at
  `692069ead0b8823d6874d8f2fc0a593d9f26704f`, annotated `v0.15.3` at object
  `2039e01475b43285ecbbf2739f788b7f855a5603`, peeled to exact release commit
  `dbff27d559193847dd2028c435c686ba656dac85`. All **176/176** pins and both
  protected databases remain exact. No production path, tool, configuration,
  dependency, protected artifact, public surface, or `STATE.md` byte changed.

### 2026-07-29 · SELF-REF

PASS. E0 confirmed both blocking gates before implementation. The Gate contains
every changed path: `tools/cycle_check.py`, its focused test file, `STATE.md`'s
live header and dated status append, and this runbook's status/checklist record.
No closed runbook, historical append, crate, dependency, schema, protected
artifact, database, or public surface changed.

- **Structural correction and fail-before:** the freshness comparison no
  longer contains `origin/main`. The live `STATE.md` header instead rejects any
  literal 40-hex assertion for that mutable ref. The reason is recorded beside
  the implementation: publishing the asserting commit moves that same ref,
  while tag object and peeled tag target are immutable at write time. Before
  rewriting the header, the corrected entry point exited **1** with exactly:

  > `cycle-check: ERROR: STATE.md: publication status header must not assert a literal origin/main hash; publishing the asserting commit moves that ref, so record mutable-ref measurements in a dated body append`

  The next line was `cycle-check: FAIL (1 defect(s))`. After the header rewrite,
  `cycle-check` passes with the annotated release refs verified. The live header
  retains version, publication disposition, annotated tag object, and peeled
  release commit, with no `origin/main` hash. The E0 branch measurement now
  appears only in the dated 2026-07-29 body append.
- **Unavailable inputs are loud:** tag object resolution, peeled-target
  resolution, release-record agreement, and `merge-base --is-ancestor` are
  checked before the disposition/freshness rules. A missing tag ref reports
  `publication verification unavailable`; a missing peeled target reports its
  own named unavailable error; and an unanswerable ancestry query reports
  `publication ancestry verification unavailable` with the Git diagnostic or
  exit status. No unresolvable-input `return` or `continue` silently leaves the
  check looking exercised.
- **Focused controls:** `shell/tests/test_cycle_check.py` passes **24/24**. It
  proves the header prohibition fires, a header without the mutable literal
  passes, both retained immutable freshness labels fire on wrong values, and
  all three unavailable-input paths report. The original pending-publication
  test remains and passes, re-proving unchanged rule 1; a dated body containing
  a stale historical branch hash is deliberately ignored.
- **Full matrix and status:** the permitted `./run ci-local` passed **20/20**
  with **133** workspace tests, **55** net tests (**29 + 26**), shell
  **252/252** on Python 3.11.4, zero rustc/clippy/fmt/ShellCheck failures,
  locked Rust 1.78, `invariant-scan` unchanged at **11/11 rules / 23 controls**,
  all **176/176** pins, protected databases **2/2**, and golden **11/11**.
  Python 3.12.13 independently passed the **21-package** constraint check and
  shell **252/252**. `cycle-check`, `checklist-audit`, `progress-check`,
  `version-check`, `invariant-scan`, manifest validation, and
  `verify-artifacts` all passed.
- **Regression anchor:** the mandatory standalone `./run golden` passed
  **11/11**, delta **0**.

---

## Standing prohibitions

- **Do not amend, rebase, or squash `72b6f42`.** It is unpushed but it is the
  forward publication audit; correct forward on top of it.
- **Do not weaken rule 1** of the publication reconciliation while fixing rule 2.
  A reachable annotated release still cannot coexist with a header calling its
  publication pending.
- **Do not fix G1 by relaxing the comparison to ancestry.** `f13c6129…` was an
  ancestor of `344124819c…` and would have passed an ancestry rule, so ancestry
  would not have caught the defect the control was built for.
- **Do not fix G1 by exempting the closing commit.** An exemption keyed to the
  commit that most needs the check is how a control becomes decorative.
- **Do not pin a source-file count** in `export-check`. The count drifts
  correctly; derive it.
- **Do not re-enable `enableSecurityCheck`** outside a disposable copy, and
  restore the real configuration by hash afterwards.
- **Do not delete a repository file to shrink the export.** Exclusion is an
  export concern; `verify-artifacts` still hashes what is on disk.
- **Do not modify any crate under `crates/` or `apps/`.** This cycle is tooling,
  configuration, and documentation. A source change is a scope violation, not a
  convenience.
- **Do not touch the robots matcher, the negative TTL, the politeness limiter,
  or the crawl-delay ratchet.**
- **Do not claim any task closes or narrows A4**, the L1 residual, the R3/R4
  open-bottom limitations, T7, or NEGATIVE-CACHE Decision B.
- **Do not batch `STATE.md` / `PROGRESS-v0.20.md` updates or combine two tasks in
  one commit.**
- If any Step's Objective, Acceptance criteria, or "Done when" is amended after
  this file is first committed, name the amendment in a dated
  `## Runbook amendments` block in the same commit.

---

## Provenance of this draft

Every gate above was read out of the repomix export of the v0.15.3 tree on
2026-07-29 by path and line, and each is written as a hypothesis for E0 to
confirm or refute.

**The v0.15.3 release itself is clean and its notes are complete.** The
`RobotsCache` correction is built the right way: `RobotsCacheTtls` plus
`new_with_ttls`, with the legacy `new` delegating `RobotsCacheTtls::new(ttl,
ttl)` so no existing call site silently changes; `cached()` matches `Policy`
exhaustively with no wildcard arm, so a future variant is a compile error rather
than a silent inheritance of the wrong lifetime; fail-closed is preserved and
only the duration moved; and `store()` still overwriting is the correct
expression of Decision B being deferred. The retirement is complete at the
manifests — `intel-compliance` declares no `[features]`, `intel-ingest` declares
only `net`. The release notes state the increased retry frequency without
dressing the change as purely conservative, and the `Removed` section names both
retired features and the consumer impact.

**G1 originates in `TASKS-v0.19-EXECUTION.md` Step 2, not in
`tools/cycle_check.py`.** The runbook specified that any `origin/main` hash
asserted in the header must equal the measured ref. The implementation is
faithful to that specification. The specification was wrong, and Step 7 must
record it that way.
