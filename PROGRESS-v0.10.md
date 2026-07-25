# PROGRESS-v0.10.md — append-only execution record

This file records v0.10 tasks after their implementation commits exist. Each
entry names the measured result, every acceptance criterion, the golden delta,
and the real implementation commit. Entries are append-only; corrections are
new dated entries.

### 2026-07-25 · B0 — v0.10 entering state rebuilt and defect table confirmed

- owner: Codex
- commit: 86039925e519eee63814861c48e46370544085b5
- result: PASS. One entering hypothesis was false and was corrected before the
  cycle advanced: the operator-supplied `TASKS-v0.10-EXECUTION.md` made the
  worktree non-clean. Git/tag identity, versions, test counts, protected
  artifacts, golden behavior, local-CI count, lack of a remote, and all nine
  drafted defects were measured directly.
- gate: CORRECTED, then PASS. `git status --porcelain=v1` reported only
  `?? TASKS-v0.10-EXECUTION.md`; no unknown protected bytes or other worktree
  change was present.
- Git/version acceptance: PASS. Entering HEAD
  `280f6abfec0044104b830731c952883aa64b9703` was exactly one audit commit past
  release `4c59db2727eda1c81beae3ff38be883a26a92ae8`; annotated tag object
  `548ffdfec4e414570ddecf813aa2f2d616662487` dereferenced to that release.
  `./run version-check` passed at 0.9.0 with the expected ahead-of-tag warning,
  the newest changelog release matched, and `git remote -v` was empty.
- Rust acceptance: PASS. A clean target produced 98 warning-denied workspace
  tests and 20 warning-denied net tests on Rust/Cargo 1.91.1; clippy and fmt
  passed. Locked warning-denied Rust/Cargo 1.78.0 check and the same 98 tests
  passed.
- Python acceptance: PASS. Python 3.11.4 and 3.12.13 each passed 105 shell
  tests with one existing third-party Starlette warning. Python 3.11
  byte-compilation, ShellCheck 0.11.0, and Bash syntax passed. The initial
  sandboxed 98-pass/7-bind-failure attempts were non-results; permitted
  loopback reruns produced the counted 105/105 passes.
- artifact acceptance: PASS. `data/core.db` remained
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`,
  6,729,728 bytes, 1,764 documents, 0/0 NULL fingerprint/canonical rows,
  integrity `ok`, with its one complete cursor. `data/live-smoke.db` remained
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`,
  9,490,432 bytes, 2,600 documents, 0/0 NULL rows, integrity `ok`, with its
  one complete cursor. `./run verify-artifacts` passed 2/2.
- failure-capable control: PASS. A copy of `data/core.db` under
  `/private/tmp/intel-v010-b0-artifact.4WgqoY` initially matched the recorded
  hash. Adding a table only to that copy changed its hash to
  `f9f4c31f54c24ca57551870122a6a2f87b0bb84f24480e48e7ba95338ecb5e3e`;
  verification against the disposable manifest exited 1, printed expected and
  actual hashes, and named `core.db field=sha256`.
- defect acceptance: PASS. Direct line-numbered source reads confirmed all
  nine: hard-coded v0.9 progress target; v0.8/v0.9-only deferred-audit inputs;
  stale v0.9 authority in `AGENTS.md`; incomplete v0.9 provenance correction;
  present-tense v0.6/v0.7 authority plus the false 1.75 floor; no
  box-to-entry-to-commit auditor; floor-only Python requirements; prose-only
  protected admission; and one prompt against `gated[0]`.
- local CI acceptance: PASS. `./run ci-local` passed all entering 16/16 jobs.
  Its progress job still validated the closed v0.9 log, as defect 1 predicts.
- golden-E2E delta: none. `./run golden` passed 11/11 with the exact 13 → 12
  corpus, hamming-12 pair, DeepSeek z=10.0, +0 rerun, one quant document, and
  four-citation public answer anchors.
- protected artifact delta: none. Both expected hashes matched again after the
  controls and complete matrix; ports 8787/8788/8899 were clear.
- exact commands:

  ```bash
  git status --porcelain=v1
  git describe --tags --always --dirty
  git rev-parse HEAD
  git log --oneline -5
  git remote -v
  git cat-file -t v0.9.0
  git cat-file tag v0.9.0
  git rev-parse 'v0.9.0^{}'
  ./run version-check
  rustc --version
  cargo --version
  rustc +1.78.0 --version
  cargo +1.78.0 --version
  python3.11 --version
  python3.12 --version
  shellcheck --version
  cargo clean
  RUSTFLAGS='-D warnings' cargo check --workspace --locked --all-targets
  RUSTFLAGS='-D warnings' cargo test --workspace --locked
  RUSTFLAGS='-D warnings' cargo check -p cored --features net --locked --all-targets
  RUSTFLAGS='-D warnings' cargo test -p intel-ingest --features net --locked
  cargo clippy --workspace --locked --all-targets -- -D warnings
  cargo fmt --all -- --check
  RUSTFLAGS='-D warnings' cargo +1.78.0 check --workspace --locked --all-targets
  RUSTFLAGS='-D warnings' cargo +1.78.0 test --workspace --locked
  find tools shell -name '*.py' -type f -print0 |
    xargs -0 python3.11 -m py_compile
  shellcheck ./run
  bash -n ./run
  PYTHONPATH=shell .venv/bin/python -m pytest shell/tests -q
  PYTHONPATH=shell .venv/py312/bin/python -m pytest shell/tests -q
  ./run down
  lsof -nP -iTCP:8787 -sTCP:LISTEN
  lsof -nP -iTCP:8788 -sTCP:LISTEN
  lsof -nP -iTCP:8899 -sTCP:LISTEN
  ./run verify-artifacts
  shasum -a 256 data/core.db data/live-smoke.db
  sqlite3 -readonly data/core.db '<read-only census and complete cursors>'
  sqlite3 -readonly data/live-smoke.db '<read-only census and complete cursors>'
  ./run golden
  ./run ci-local
  rg -n '<each cited defect pattern>' '<each cited defect file>'
  ./run verify-artifacts --manifest \
    /private/tmp/intel-v010-b0-artifact.4WgqoY/manifest.json \
    --root /private/tmp/intel-v010-b0-artifact.4WgqoY
  ```

### 2026-07-25 · D0-GATE — runbook ordering cycle blocks a conforming auditor

- owner: Codex
- commit: acbbae4dcfe4d68152f07827c9fb585cf9ffc627
- result: BLOCKED before implementation. Single-source target derivation is
  feasible, but D0 cannot both enforce its stated closed-runbook rule and pass
  as the seventeenth blocking local-CI job against the current historical
  corpus.
- measurement: the four inactive execution runbooks contain respectively
  12, 10, 11, and 7 checked boxes, zero unchecked boxes, and zero dated closing
  records naming a release or explicit no-release disposition.
- additional findings: `TASKS-v0.6.md:3` and `TASKS-v0.7.md:3` retain
  present-tense authority claims. `TASKS-v0.9-EXECUTION.md:514-520` retains the
  unexecuted-cycle claim and a correction covering only B0/A1.
- dependency cycle: D0 requires those facts repaired before `cycle-check` can
  be blocking; D1 owns those repairs; D1 is ordered after A1; A1 requires D0's
  completed 17-job baseline.
- prohibited alternatives: no auditor exemption or relaxed rule was added, D1
  work was not silently folded into D0, and the ordered runbook was not changed
  without operator direction. D0 remains unchecked.
- golden-E2E delta: none. The documentation-only gate record was followed by a
  fresh `./run golden` pass at 11/11.
- protected artifact delta: none. `./run verify-artifacts` passed 2/2 before
  the fresh golden run.
- exact commands:

  ```bash
  for f in TASKS-v0.8-EXECUTION.md \
           TASKS-v0.8.1-EXECUTION.md \
           TASKS-v0.8.2-EXECUTION.md \
           TASKS-v0.9-EXECUTION.md; do
    rg -c '^- \[x\]' "$f"
    rg -c '^- \[ \]' "$f"
    rg -c '^\*\*(Closing record|Cycle closed|Closed cycle|Release identity|No-release disposition).*20[0-9]{2}-[0-9]{2}-[0-9]{2}' "$f"
  done
  rg -n 'This document is the authoritative task list' \
    TASKS-v0.6.md TASKS-v0.7.md
  rg -n 'tasks themselves have not been executed|Execution correction' \
    TASKS-v0.9-EXECUTION.md
  nl -ba TASKS-v0.10-EXECUTION.md | sed -n '181,270p'
  ./run version-check
  ./run verify-artifacts
  ./run golden
  ```

### 2026-07-25 · D1A — historical cycle closure bootstrapped

- owner: Codex
- commit: 9e53d325ff6fe00d5d5a470076fd9e8f4f825ce3
- result: PASS. The operator-approved ordering correction is recorded as
  B0 → D1A → D0 → A1 → D1, and the strict D0 auditor can now evaluate the
  production corpus without an exemption.
- gate: PASS. All release, tag-object, and implementation-commit identities
  were resolved from Git before being recorded. Historical rationale was
  preserved through dated appends and strikethrough corrections.
- closing-record acceptance: PASS. The v0.8 and v0.8.1 runbooks record
  annotated `v0.8.0`; v0.8.2 records an explicit no-separate-release
  disposition plus all 11 implementation commits; v0.9 records annotated
  `v0.9.0`, all seven task commits, the P2 live-completion commit, and every
  carried non-result required by D1.
- historical-authority acceptance: PASS. `TASKS-v0.6.md` and
  `TASKS-v0.7.md` carry dated superseded-cycle banners, their present-tense
  authority claims are struck, and v0.7's false 1.75 offline floor is struck
  in favor of the measured format-v4 lock floor of 1.78.
- checklist/rationale acceptance: PASS. The closed execution checklists remain
  12/12, 10/10, 11/11, and 7/7, each with zero unchecked boxes and exactly one
  cycle-closing record. No existing checklist disposition or historical
  measurement changed.
- version acceptance: PASS. `./run version-check` passed at 0.9.0 with the
  expected ahead-of-tag warning.
- golden-E2E delta: none. `./run golden` passed all 11/11 anchors.
- protected artifact delta: none. `./run verify-artifacts` passed 2/2 with
  `data/core.db` at
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and `data/live-smoke.db` at
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`.
- exact commands:

  ```bash
  git diff --check
  rg -c '^- \[x\]' TASKS-v0.{8,8.1,8.2,9}-EXECUTION.md
  rg -c '^- \[ \]' TASKS-v0.{8,8.1,8.2,9}-EXECUTION.md
  rg -c '^## Cycle closing record$' \
    TASKS-v0.{8,8.1,8.2,9}-EXECUTION.md
  git rev-parse v0.8.0
  git rev-parse 'v0.8.0^{}'
  git rev-parse v0.9.0
  git rev-parse 'v0.9.0^{}'
  git cat-file -t '<each recorded implementation commit>'
  ./run version-check
  ./run verify-artifacts
  ./run golden
  ```

### 2026-07-25 · D0 — active cycle identity made executable

- owner: Codex
- commit: 8b7cbacde7f4d4f77cc74a68f46c7f559ef9dcb2
- result: PASS. One fixed-shape `**Active cycle:** v0.10` declaration in
  `AGENTS.md` now drives the active runbook, progress log, lifecycle checker,
  default progress validation, and deferred-audit progress inputs.
- gate: PASS. Every affected tool derives its target without a cycle-specific
  filename fallback. No task/progress cycle filename literal remains under
  `tools/`.
- lifecycle acceptance: PASS. `./run cycle-check` validates the active v0.10
  runbook as open, four inactive execution runbooks as closed with real
  release/no-release identities, and three non-execution task files as dated
  historical rationale without effective present-tense authority claims.
- target acceptance: PASS. Default `./run progress-check` validated
  `PROGRESS-v0.10.md` at D1A commit
  `9e53d325ff6fe00d5d5a470076fd9e8f4f825ce3`; direct script and module
  invocations produced the same result. `audit_deferred.progress_paths()`
  returns the complete `PROGRESS-v*.md` glob, including the declared active
  log.
- failure-capable controls: PASS 4/4. In disposable copies under
  `/private/tmp/intel-cycle-controls.e25wL3`, `./run cycle-check` exited
  non-zero and named: nonexistent `TASKS-v99.99-EXECUTION.md`; fully checked
  active `TASKS-v0.10-EXECUTION.md`; a present-authority mutation in
  `TASKS-v0.9-EXECUTION.md`; and a mismatched `tools/progress_check.py`
  resolver with both its v0.9 result and the declared v0.10 target.
- local-CI acceptance: PASS. `./run ci-local` passed 17/17 jobs after adding
  active cycle consistency as a blocking job. The run included 98
  warning-denied workspace tests, 20 net tests, clippy/fmt, locked Rust 1.78
  check/tests, and 105 Python 3.11 shell tests with one existing third-party
  warning.
- golden-E2E delta: none. The local-CI golden job and a final direct
  `./run golden` each passed all 11/11 anchors.
- protected artifact delta: none. The local-CI artifact job and a final direct
  `./run verify-artifacts` each passed 2/2 with the exact protected hashes.
- exact commands:

  ```bash
  ./run cycle-check
  python3 tools/cycle_check.py
  ./run progress-check
  python3 tools/progress_check.py PROGRESS-v0.10.md
  rg -n \
    'TASKS-v0\.[0-9]+(?:\.[0-9]+)*-EXECUTION\.md|PROGRESS-v0\.[0-9]+\.md' \
    tools
  python3.11 -m py_compile tools/cycle_identity.py \
    tools/cycle_check.py tools/progress_check.py tools/audit_deferred.py
  shellcheck ./run
  bash -n ./run
  GIT_DIR=/Users/yzjia/intel-platform/.git \
    /private/tmp/intel-cycle-controls.e25wL3/final-missing/run cycle-check
  GIT_DIR=/Users/yzjia/intel-platform/.git \
    /private/tmp/intel-cycle-controls.e25wL3/final-closed-active/run cycle-check
  GIT_DIR=/Users/yzjia/intel-platform/.git \
    /private/tmp/intel-cycle-controls.e25wL3/final-closed-authority/run cycle-check
  GIT_DIR=/Users/yzjia/intel-platform/.git \
    /private/tmp/intel-cycle-controls.e25wL3/final-progress-target/run cycle-check
  ./run ci-local
  ./run golden
  ./run verify-artifacts
  ```

### 2026-07-25 · A1 — every checked task resolves to a real commit

- owner: Codex
- commit: ce9d8932f3d0e74bcc254fa83cc7a102722aad00
- result: PASS. `./run checklist-audit` now provides a blocking
  box-to-progress-to-Git proof for every checked execution task.
- gate: PASS. All 31 legacy narrative commit values were recoverable from Git;
  no exemption was needed, guessed, or fabricated.
- historical acceptance: PASS. `PROGRESS-v0.8.md` retains every original entry
  and appends 31 runbook-qualified, hash-only corrections: 12 for v0.8, 10 for
  v0.8.1, and nine for v0.8.2. The nine already-valid closed-cycle entries
  remain unchanged.
- audit acceptance: PASS. Before A1's required two-commit close, the production
  audit reported 43 checked, 43 matched, 43 resolved, zero exemptions. After
  this append supplied A1's real implementation hash, it reported **44/44/44**
  with zero exemptions.
- reporting acceptance: PASS. Every execution runbook reports its checked,
  matched, resolved, and exemption counts plus its derived progress log.
- exemption acceptance: PASS. The dated exemption registry is empty. The
  parser validates its schema and rejects malformed, duplicate, orphan, and
  provably false exemptions.
- failure-capable controls: PASS 3/3. Disposable copies under
  `/private/tmp/intel-checklist-controls.i7Fc47` rejected and named a checked
  D1 box without progress, a well-formed 40-zero nonexistent commit, and a
  false exemption for resolvable v0.9 B0.
- local-CI acceptance: PASS. `./run ci-local` passed all 18/18 jobs, including
  checked-task evidence as the new blocking job, 98 workspace tests, 20 net
  tests, and 105 Python 3.11 shell tests.
- golden-E2E delta: none. The local-CI run and final direct `./run golden` each
  passed all 11/11 anchors.
- protected artifact delta: none. The local-CI run and final direct
  `./run verify-artifacts` each passed 2/2 with exact hashes.
- exact commands:

  ```bash
  git log --all --format='%H%x09%s' -G \
    '^- \[x\] \*\*<task-id>(\*\*| —)' -- \
    TASKS-v0.8-EXECUTION.md
  ./run checklist-audit
  python3 tools/progress_check.py PROGRESS-v0.8.md
  python3.11 -m py_compile tools/checklist_audit.py
  shellcheck ./run
  bash -n ./run
  GIT_DIR=/Users/yzjia/intel-platform/.git \
    /private/tmp/intel-checklist-controls.i7Fc47/missing-entry/run \
    checklist-audit
  GIT_DIR=/Users/yzjia/intel-platform/.git \
    /private/tmp/intel-checklist-controls.i7Fc47/nonexistent-hash/run \
    checklist-audit
  GIT_DIR=/Users/yzjia/intel-platform/.git \
    /private/tmp/intel-checklist-controls.i7Fc47/false-exemption/run \
    checklist-audit
  ./run ci-local
  ./run golden
  ./run verify-artifacts
  ```

### 2026-07-25 · D1 — finished-cycle provenance validated and closed

- owner: Codex
- commit: 8fb74f01ffc608468bf340370f86e34fbcc7d8f4
- result: PASS. D0 and A1 now validate every historical closure, authority
  disposition, progress entry, and Git identity required by D1.
- gate: PASS. The D1A provenance repairs remain dated appends or explicit
  strikethrough corrections; no closed rationale or original progress entry
  was rewritten.
- closing-record acceptance: PASS. Four inactive execution runbooks each have
  exactly one dated closing record and zero unchecked boxes. v0.8/v0.8.1
  resolve to annotated v0.8.0; v0.8.2 has an 11-commit no-release record; v0.9
  resolves all seven tasks and annotated v0.9.0.
- carried-disposition acceptance: PASS. v0.9 preserves adversarial
  `NOT EXERCISED`, T7/Postgres/pgvector/multi-host deferrals, V2 promotion
  without materialization, protected-admission/constraints candidates, no
  remote, and no observed runner execution.
- historical-authority acceptance: PASS. v0.6/v0.7 are dated historical-only
  task files. Their authority sentences remain preserved inside
  strikethroughs; v0.7's false offline 1.75 claim remains preserved inside a
  strikethrough followed by the measured 1.78 correction.
- auditor acceptance: PASS. Before D1's two-commit close, `cycle-check` passed
  and `checklist-audit` reported 44/44/44 with zero exemptions. After this
  append supplied D1's implementation hash, both pass and checklist evidence
  is **45/45/45**, zero exemptions.
- failure-capable control: PASS. In
  `/private/tmp/intel-d1-controls.6juKqq`, restoring the v0.7 authority claim
  made `./run cycle-check` exit non-zero and name `TASKS-v0.7.md:8`; the
  corrected disposable tree passed before and after.
- local-CI acceptance: PASS. The exact implementation tree passed all 18/18
  local jobs, including both auditors, 98 workspace tests, 20 net tests, and
  105 Python 3.11 shell tests.
- golden-E2E delta: none. Local CI and the final direct `./run golden` each
  passed all 11/11 anchors.
- protected artifact delta: none. Local CI and the final direct
  `./run verify-artifacts` each passed 2/2 with exact hashes.
- exact commands:

  ```bash
  git rev-parse v0.9.0
  git rev-parse 'v0.9.0^{}'
  git cat-file -e '<each v0.9 task hash>^{commit}'
  ./run cycle-check
  ./run checklist-audit
  python3 - '<effective inactive-authority and v0.7 floor scan>'
  python3.11 -m py_compile tools/cycle_check.py
  GIT_DIR=/Users/yzjia/intel-platform/.git \
    /private/tmp/intel-d1-controls.6juKqq/restored-authority/run cycle-check
  GIT_DIR=/Users/yzjia/intel-platform/.git \
    /private/tmp/intel-d1-controls.6juKqq/base/run cycle-check
  ./run ci-local
  ./run golden
  ./run verify-artifacts
  ```
