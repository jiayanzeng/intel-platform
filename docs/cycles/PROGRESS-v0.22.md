# PROGRESS-v0.22.md — append-only execution record

This file records v0.22 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-29 · ACTIVATE — v0.22 admitted

- owner: Codex
- commit: aa7fee3
- result: PASS for cycle activation only; E0 remains unchecked. Before
  activation, local `main` was the intentionally unpushed v0.21 closing audit
  `188055a21fd6cabf2025bb7ce609c18bf47c4519`, one commit ahead of measured
  remote `main` `b7c4b10eb506923e3ea854a32d1dc3f4c83b0eaa`.
- worktree acceptance: PASS. The only pre-activation worktree item was the
  operator-supplied untracked `docs/cycles/TASKS-v0.22-EXECUTION.md`;
  implementation commit `aa7fee3` contains only that runbook, the `AGENTS.md`
  v0.22 declaration, and this append-only progress-log skeleton.
- runbook-validity acceptance: PASS. Before the runbook's first commit, one
  provenance sentence reproduced the checker's exact cycle-closing heading
  and was rephrased without changing an objective, gate, acceptance criterion,
  or done condition. After the implementation commit, `./run cycle-check`
  reports active v0.22 open with nineteen closed execution runbooks.
- lifecycle acceptance: PASS. `./run checklist-audit` resolves the entering
  **171/171** checked tasks, reports the same three retractions, and finds zero
  exemptions. `git diff --check` passed, and the post-implementation worktree
  was clean.
- release-ref acceptance: PASS. Read-only local and remote measurements agree:
  annotated tag object `f2bfeacc1dc8207841430e3827e7babed5605b47` peels to
  release commit `b7c4b10eb506923e3ea854a32d1dc3f4c83b0eaa`; the activation
  record adds no literal `origin/main` assertion to `STATE.md`'s header.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and G1–G5 measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-29 · E0 — entering state and drafted gates settled

- owner: Codex
- commit: ee1f4e0
- result: PASS. The complete measured record is in the E0 execution section of
  `TASKS-v0.22-EXECUTION.md`; all five drafted gates are now classified and
  Step 2 is blocked on its named operator decision.
- entering-matrix acceptance: PASS. Clean constrained Python 3.11.4 and 3.12.13
  rebuilds resolved the same 21 packages and each passed shell **258/258** with
  the same one third-party Starlette warning. `./run ci-local` passed
  **20/20**, with **133** workspace tests, **55** net tests (**29 + 26**),
  warning-denied current and locked Rust 1.78 lanes, clean
  clippy/fmt/ShellCheck, `invariant-scan` **12/12 rules / 30 controls**,
  **206/206** pins, protected databases **2/2**, and embedded golden **11/11**.
  The standalone cycle, checklist, progress, version, invariant, artifact, and
  root export checks passed; `export-check` measured 90 derived sources, 7
  required paths, and 151 exported paths.
- G1 acceptance: CONFIRMED. `newest_closed_release` requires release name,
  release commit, and annotated-tag object from the closing section. Only the
  name is knowable before the containing commit. A disposable object
  construction changed both the containing commit when its prior hash was
  inserted and the tag object when the new target was tagged; both fixed-point
  comparisons were `no`. No permutation can make either dependent object name
  itself. The separate early-close clone failed with the four exact
  unavailable-input lines preserved in the runbook record.
- G2 acceptance: both `v0.8.0` and `v0.10.2` are **LOCAL-ONLY**. Their exact
  annotated objects, targets, local refs, and release commits exist; exhaustive
  remote inspection found neither tag nor any recorded object id. No ref or
  closed runbook changed.
- G3 acceptance: REFUTED. `ARCHITECTURE.md` already states the contributor-facing
  operator-local status, command behavior, deliberate local/hosted CI omission,
  and reason. `AGENTS.md` carries the two measured operating rules.
- G4 acceptance: CONFIRMED as an unexamined default. The manifest is 119,353
  bytes/characters at 206 pins; release totals are
  **161 → 176 → 191 → 206**, exactly +15 per cycle, and the full re-hash costs
  **0.10 s real / 0.05 s user / 0.04 s sys**. Existing immutable/append-only
  policy has no dated unbounded-growth acceptance, bound, or revisit trigger.
- G5 acceptance: CONFIRMED. Both third-party warnings are repeatedly recorded
  as non-blocking but neither has a trigger or permanent-acceptance decision.
- identity/integrity acceptance: PASS. Local and remote `v0.15.5` remain exact
  at tag object `f2bfeacc1dc8207841430e3827e7babed5605b47`, peeled release
  commit `b7c4b10eb506923e3ea854a32d1dc3f4c83b0eaa`; all **206/206** pins and
  protected databases **2/2** re-verified. `STATE.md` remained blob
  `03053b14137161423a4f1bca617b8bc85d91e86b`.
- golden-E2E delta: **0**. Mandatory standalone golden passed **11/11** after
  the E0 status edit.

### 2026-07-29 · CLOSE-FIELDS — tagged-closing Option C

- owner: Codex
- commit: 72b9d8f
- result: PASS. The operator answered `C`; implementation commit
  `72b9d8f06c650fafd4d6f3d4216128997a1ffd0b` adopts the two-commit
  tagged-closing protocol. Release commit `R` remains untagged, immediate child
  `C` records `R` without an annotated-tag-object field, and the annotated tag
  targets `C`.
- decision acceptance: PASS. The recorded cost is the option the operator
  selected: the runbook no longer stores the tag-object hash, and closure cites
  authenticated candidate evidence rather than published-head evidence. This
  is accepted because the closing tree contains only values knowable when
  committed, Git binds the tag to that tree and release parent, and a dated
  forward append pins the later tag object, closing commit, and hosted run.
  Published-head CI is forward confirmation, not the closing event.
- fail-before acceptance: PASS. The old checker rejected the selected shape
  with `closing record must contain exactly one annotated tag object; found 0`.
  The corrected checker rejected the pre-change active shape with
  `declared closed cycle must use the tagged-closing protocol and omit the
  Annotated tag object field; record that object in the dated post-push append`.
- failure-control acceptance: PASS. R12 has **13** registered fail-before
  mutations covering the active protocol, annotated-tag type, release parent,
  tagged tree, header assertions, pending status, unavailable refs and
  ancestry, and the complete dated post-push record. Every mutation detects its
  planted failures; the repository passes **12/12 rules / 36 controls**.
- contract acceptance: PASS. `AGENTS.md` and `cycle_check.py` describe the same
  sequence, tagged-tree checks, and required forward-record fields. Legacy
  release records through v0.15.5 retain their existing semantics.
- scope acceptance: PASS. No ref, closed runbook, published tree, crate,
  dependency, schema, protected artifact, database, or public surface changed.
  Only the declared checker, focused tests, invariant registry/harness,
  operating contract, active runbook, and status record changed.
- test acceptance: PASS. Focused `cycle_check` tests passed **34/34** on
  constrained Python 3.11.4 and 3.12.13. `./run ci-local` passed **20/20** with
  **133** workspace tests, **55** net tests (**29 + 26**), shell **266/266**,
  warning-denied current and locked Rust lanes, and clean
  clippy/fmt/ShellCheck gates. The independent Python 3.12.13 shell lane also
  passed **266/266**.
- golden-E2E delta: **0**. Mandatory standalone golden passed **11/11** after
  the status and runbook edits.
- protected artifact delta: **0**. All **206/206** pins and protected databases
  remain unchanged; no protected manifest or artifact path moved.
