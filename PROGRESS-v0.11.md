# PROGRESS-v0.11.md — append-only execution record

This file records v0.11 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-27 · E0-GATE — supplied runbook admitted before baseline restart

- owner: Codex
- commit: 57e56b7268345ea17dda6641dd2682295b43ec55
- result: BLOCKED, then corrected without claiming E0 complete. The read-only
  opener found only the operator-supplied untracked
  `TASKS-v0.11-EXECUTION.md`; `AGENTS.md` still correctly declared the latest
  closed cycle, v0.10.3.
- identity evidence: entering HEAD was
  `d24f2b83c9657b1fa47d7f3315a4120181f2624e`
  (`v0.10.3-1-gd24f2b8`), and local `main` and `origin/main` were aligned at
  that commit with zero ahead / zero behind.
- correction: committed the reviewed runbook unchanged, declared v0.11
  active, and created this progress log.
- lifecycle acceptance: the pre-admission `./run cycle-check` correctly
  refused a runbook with no first committed version. After commit,
  `./run cycle-check` passed with active v0.11 and eight closed execution
  runbooks. `./run checklist-audit` resolved the entering 77/77 checked tasks
  with zero exemptions; `git diff --check` passed.
- test acceptance: NOT RUN at this gate checkpoint. E0 remains unchecked and
  restarts from the clean post-audit tree.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected file was touched.

### 2026-07-27 · E0 — entering state rebuilt and S1–S8 confirmed

- owner: Codex
- commit: 337e7c04b76ee8034b6cf2e75f5897869f538d6c
- result: PASS after the separately recorded activation pair. Clean HEAD
  `ac1b2ef9cc6b9913add42d22b2d4b23f10e2a29a` was
  `v0.10.3-3-gac1b2ef`; local `main` was two ahead / zero behind
  `origin/main` at `d24f2b83…`.
- baseline acceptance: PASS. The first sandboxed `./run ci-local` was an
  environment non-result: eight shell controls were denied `ps` or loopback
  binds after all earlier units passed. The permitted identical rerun passed
  **19/19** with 99 workspace tests, 20 net tests, warning-denied builds,
  clippy/fmt, locked Rust 1.78, 187/187 Python 3.11 shell tests, golden 11/11,
  protected artifacts 2/2, all 39 pins, fingerprints, and lifecycle auditors.
- Python acceptance: PASS. The independent Python 3.12.13 lane passed
  187/187, and both interpreters verified 21/21 constrained packages.
- artifact acceptance: PASS. Standalone protected verification matched 2/2;
  manifest validation and an independent `hashlib.sha256` witness each matched
  all **39/39** pins with zero mismatches.
- defect acceptance: PASS. Static source capture confirmed S1's unchecked bind
  and optional token; both S2 body endpoints' missing sector predicates; S3's
  single-group selection; S4's raw matching; S5's limiter replacement; S6's
  fail-open library seam and defect-encoding test; S7's event-by-event live
  mutation; and S8's maintenance writes without canonical rematerialization.
  Every augment row also reproduced.
- failure-capable controls: PASS. Three temporary compliance controls asserted
  and observed the ignored duplicate product-token group, the
  `/foo/bar/%62%61%7A` evasion, and the crawl-delay transition resetting the
  counter and allowing a zero-time first acquire. A temporary signed-webhook
  control observed HTTP 400 plus the first event's surviving live mutation.
  All scratch edits were removed before the E0 record.
- inherited-guard acceptance: PASS. The v0.10.3 report is release grade with
  attestations required, seven distinct expected/accepted identities, zero
  rejection, seven verified rows, and 14 tracked existing receipt/bundle
  paths. Fresh and resumed adversarial paths share one consistency checker.
- lifecycle acceptance: PASS. Standalone version, cycle, checklist, and
  progress checks passed; checklist entered at 77/77 historical tasks with
  zero exemptions.
- golden-E2E delta: none. Standalone `./run golden` passed **11/11** with every
  exact anchor unchanged.
- protected artifact delta: none. Both protected databases and all 39 existing
  pins remained byte-exact.
