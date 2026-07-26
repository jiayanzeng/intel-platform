# PROGRESS-v0.10.3.md — append-only execution record

This file records v0.10.3 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-26 · E0-GATE — supplied runbook admitted before baseline restart

- owner: Codex
- commit: f220e695dc93189d9fe919d80e373d96edd55851
- result: BLOCKED, then corrected without claiming E0 complete. The read-only
  opener found only the operator-supplied untracked
  `TASKS-v0.10.3-EXECUTION.md`; `AGENTS.md` still correctly declared the
  latest closed cycle, v0.10.2.
- identity evidence: entering HEAD was
  `6a7070b97bd4bef08345311644fa8815a58cd282`
  (`v0.10.2-1-g6a7070b`), local `main` was four commits ahead / zero behind
  `origin/main` at `817e7f3e7c1878c18f474532df4d50c2b17fcbdc`, and the
  remote tag census contained v0.10.0 and v0.10.1 but no v0.10.2.
- correction: committed the reviewed runbook unchanged, declared v0.10.3
  active, and created this progress log.
- lifecycle acceptance: `./run cycle-check` passed with active v0.10.3 and
  seven closed execution runbooks. `./run checklist-audit` resolved the
  entering 69/69 checked tasks with zero exemptions; `git diff --check`
  passed.
- test acceptance: NOT RUN at this gate checkpoint. E0 remains unchecked and
  restarts from the clean post-audit tree.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected file was touched.

### 2026-07-26 · E0 — entering state rebuilt and G1–G6 confirmed

- owner: Codex
- commit: ac9bf73a41fe62c35b8891253232bf45230a22cf
- result: PASS after the separately recorded cycle activation. Clean HEAD
  `4c70da5760a25fe5781ce7d09d6350cda69187d9` was
  `v0.10.2-3-g4c70da5`; the two activation commits explain local `main` being
  six ahead / zero behind remote `origin/main` at `817e7f3e…`. Local
  annotated v0.10.2 remained exact at tag object `d821f8b2…` and release
  commit `7d127aba…`; the authenticated remote census still had no v0.10.2
  tag.
- baseline acceptance: PASS. The sandboxed first `./run ci-local` attempt was
  an environment non-result because eight controls could not bind loopback or
  run `ps`. The permitted identical rerun passed **19/19** with 99 workspace
  tests, 20 net tests, warning-denied builds, clippy/fmt, locked Rust 1.78,
  156/156 Python 3.11 shell tests, golden 11/11, protected artifacts 2/2,
  three evidence pins, fingerprints, and lifecycle auditors.
- Python acceptance: PASS. The independent Python 3.12.13 lane passed
  156/156, and both interpreter lanes matched 21/21 exact packages.
- artifact acceptance: PASS. Standalone protected verification matched 2/2;
  manifest validation and an independent SHA-256 implementation both matched
  all three pins at 27,786 / `00cf14ae…`, 62,978 / `beec8bfa…`, and 28,968 /
  `4e11a8b3…` bytes/hash.
- defect acceptance: PASS. G1 counts job names and loses matrix identity; G2
  leaves authentication optional and its posture unread; G3 accepts the
  substitution contradiction; G4 pins neither source revision nor committed
  receipt/bundle bytes; G5 hard-codes the wrong task label and scans too
  narrowly; G6's undisclosed Step 2 contract rewrite was recovered by diffing
  Git blob `0eaef257…` against the first committed runbook.
- drafted-expectation correction: the broad G2 grep did not match only tests;
  it also found the option and writer in `tools/audit_deferred.py`, as it must.
  The finding was confirmed by the absence of any requiring invocation in
  `run` or `ci.yml` and any posture reader.
- CLI policy acceptance: PASS. Verbatim `gh attestation verify --help` from
  gh 2.96.0 exposed `--signer-digest`, `--source-digest`, and `--source-ref`;
  the current verifier passes none.
- lifecycle acceptance: PASS. Standalone `version-check`, `cycle-check`,
  `checklist-audit`, and `progress-check` passed; checklist entered at 69/69
  historical tasks with zero exemptions.
- golden-E2E delta: none. Standalone permitted `./run golden` passed 11/11
  with every exact anchor unchanged.
- protected artifact delta: none. Both protected databases and all three
  pinned JSON reports remained byte-exact.

### 2026-07-26 · MATRIX-ID — CI matrix identified instead of counted

- owner: Codex
- commit: da401507bd64ac9a2f07f37fc68b0d5b42fc7291
- result: PASS. Production receipt completeness is the exact seven-member
  `(job, matrix)` identity set: five single-leg jobs plus shell
  `python=3.11` and `python=3.12`. Accepted rows preserve matrix, workflow,
  repository, and event SHA.
- matrix-shape acceptance: PASS. Shell requires exactly one declared matrix
  value; single-leg jobs must omit the field. Missing shell matrix, unknown
  `python=3.13`, and a matrix on `core` each produce a distinct rejection.
- duplicate acceptance: PASS. Duplicate `(job, matrix)` subjects and duplicate
  receipt content digests produce separate findings; either empties the
  accepted set and records zero observed executions.
- failure-capable control: PASS. The selected fail-before set failed **5/5**
  under the old guard: two authenticated copies of the Python 3.11 bytes were
  counted as both shell legs, three malformed matrix shapes promoted, and
  accepted rows lost identity. Pass-after was **5/5**; the duplicated set
  records both duplicate findings, misses Python 3.12, and defers.
- legacy compatibility: PASS without inferred identity. Immutable reports and
  old runner bytes are unchanged. Rederivation explicitly recognizes the old
  count-contract report shape; the production report-creation path cannot
  select it and emits `expected_job_identities`. The pinned v0.10.1 report
  still re-derived with seven rows, five source dispositions, and seven
  triggers.
- workflow acceptance: PASS. The executable source assertion confirms exactly
  one workflow `matrix` field, on the shell job; all single-leg emitters omit
  it.
- Python acceptance: PASS. The focused module passed 28/28 and the full shell
  suite passed 160/160 under both Python 3.11.4 and 3.12.13, with the existing
  single Starlette warning. Python compilation and `git diff --check` passed.
- golden-E2E delta: none. `./run golden` passed 11/11 with every exact anchor
  unchanged.
- protected artifact delta: none. Both protected databases matched 2/2, all
  three JSON pins matched, and manifest validation passed.
