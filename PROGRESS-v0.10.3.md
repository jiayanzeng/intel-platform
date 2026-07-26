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
