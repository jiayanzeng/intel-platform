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

### 2026-07-25 · A2 — protected-artifact admission made failure-capable

- owner: Codex
- commit: 54fc23b78ec6ea529afd388dea1d8b188c6ee30b
- result: PASS. Manifest schema 2 makes protected-artifact admission an
  append-only chain enforced by `tools/evidence_artifacts.py`.
- gate: PASS. A2 admitted no new artifact, changed neither expected hash nor
  database byte, and required no write to either protected database.
- schema acceptance: PASS. Every artifact carries a non-empty admission
  record array. Each exact-shape record names task, ISO date, admitted SHA-256,
  prior SHA-256, captured wire command/output reference, operator approval,
  and explicit retroactive status. The artifact hash must equal the newest
  record, and every non-initial prior hash must equal its predecessor.
- retroactive acceptance: PASS. Both original records are explicitly
  `retroactive: true` and cite immutable Git records for the already-observed
  harvest and B0 hash evidence. They do not claim a fresh wire run or fresh
  review.
- failure-capable controls: PASS 4/4. Nine targeted tests include controls
  proving that an expected-hash edit without a record fails, missing wire
  evidence or operator approval fails naming its field, a bad prior hash fails
  naming the chain break, and a complete chained record over a disposable
  artifact validates and verifies.
- shell acceptance: PASS. The exact implementation tree passed 109/109 shell
  tests under Python 3.11.4 and 109/109 under Python 3.12.13; each reported the
  same one third-party Starlette deprecation warning.
- local-CI acceptance: PASS. `./run ci-local` passed all 18/18 jobs, including
  schema-2 artifact validation, both auditors, 98 workspace tests, 20 net
  tests, clippy/fmt, locked Rust 1.78 checks/tests, Python byte-compilation,
  ShellCheck, and golden.
- checklist acceptance: PASS. Before this required audit append, A2 was the
  sole expected two-commit gap. After the real implementation hash above was
  recorded, `./run checklist-audit` reported 46/46/46 with zero exemptions.
- golden-E2E delta: none. Local CI and the final direct `./run golden` each
  passed all 11/11 anchors.
- protected artifact delta: none. Before and after A2,
  `data/core.db` remained
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  and `data/live-smoke.db` remained
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`;
  final direct verification passed 2/2.
- exact commands:

  ```bash
  python3 tools/evidence_artifacts.py validate
  ./run verify-artifacts
  shasum -a 256 data/core.db data/live-smoke.db
  PYTHONPATH=shell python3 -m pytest \
    shell/tests/test_evidence_artifacts.py -vv
  PYTHONPATH=shell python3 -m pytest shell/tests -q
  PYTHONPATH=shell .venv/py312/bin/python -m pytest shell/tests -q
  python3 -m py_compile tools/evidence_artifacts.py \
    shell/tests/test_evidence_artifacts.py
  ./run ci-local
  ./run golden
  ./run verify-artifacts
  ./run checklist-audit
  ./run progress-check
  ```

### 2026-07-25 · C1 — Python resolutions pinned and reproduced

- owner: Codex
- commit: 4bb80fff16c53b99e1e1c121d20fa4d5b6fc5f67
- result: PASS. One shared `shell/constraints.txt` pins the exact 21-package
  application/test resolution for Python 3.11 and 3.12 while
  `shell/requirements.txt` retains its four unchanged floors.
- gate: PASS. Clean unconstrained Python 3.11.4 and 3.12.13 rebuilds produced
  byte-identical application/test `pip freeze` output, passed `pip check`, and
  each passed the 109-test pre-C1 shell suite. No pin is unavailable on 3.11.
  The dated FastAPI 0.139.2 measurement had moved upstream to 0.140.0 before
  the implementation diff; both gate lanes selected and passed with 0.140.0,
  which is the version now pinned.
- install acceptance: PASS. The `./run` venv bootstrap, both CI Python matrix
  lanes, `AGENTS.md`, and the README's current raw install command all supply
  `-c shell/constraints.txt`. The requirement floors remain byte-identical.
- verifier acceptance: PASS. `./run python-env-check` compares the active
  interpreter's complete non-bootstrap distribution set to exact pins. Local
  CI executes it inside the existing shell-test job; CI has a dedicated step
  in each existing Python matrix lane.
- reproducibility acceptance: PASS. Additional fresh constrained Python 3.11.4
  and 3.12.13 environments each reproduced 21/21 exact pins, emitted
  byte-identical application/test freezes, and passed `pip check`.
- failure-capable controls: PASS 2/2. Pip rejected disposable
  `fastapi==0.109.0` against declared `fastapi>=0.110`, naming both sides of
  the conflict. The exact-set verifier rejected a disposable one-patch drift
  and named `fastapi: expected 0.140.1, found 0.140.0`.
- shell acceptance: PASS. Three new verifier tests bring the measured total
  to 112/112 under Python 3.11.4 and 112/112 under Python 3.12.13; both report
  the same one third-party Starlette warning.
- local-CI acceptance: PASS. The exact implementation tree passed all 18/18
  jobs, including exact Python environment verification, 98 workspace tests,
  20 net tests, clippy/fmt, and locked Rust 1.78 checks/tests.
- checklist acceptance: PASS. Before this required audit append, C1 was the
  sole expected two-commit gap. After the real implementation hash above was
  recorded, `./run checklist-audit` reported 47/47/47 with zero exemptions.
- golden-E2E delta: none. Local CI and the final direct `./run golden` each
  passed all 11/11 anchors.
- protected artifact delta: none. Local CI and final direct verification each
  passed 2/2 with both exact protected hashes.
- exact commands:

  ```bash
  python3 -m venv --clear .venv
  .venv/bin/python -m pip install -r shell/requirements.txt
  python3.12 -m venv --clear .venv/py312
  .venv/py312/bin/python -m pip install -r shell/requirements.txt
  .venv/bin/python -m pip freeze
  .venv/py312/bin/python -m pip freeze
  .venv/bin/python -m pip check
  .venv/py312/bin/python -m pip check
  PYTHONPATH=shell .venv/bin/python -m pytest shell/tests -q
  PYTHONPATH=shell .venv/py312/bin/python -m pytest shell/tests -q
  python3 -m venv --clear .venv/repro311
  .venv/repro311/bin/python -m pip install \
    -c shell/constraints.txt -r shell/requirements.txt
  python3.12 -m venv --clear .venv/repro312
  .venv/repro312/bin/python -m pip install \
    -c shell/constraints.txt -r shell/requirements.txt
  .venv/repro311/bin/python tools/python_constraints.py \
    shell/constraints.txt
  .venv/repro312/bin/python tools/python_constraints.py \
    shell/constraints.txt
  .venv/repro311/bin/python -m pip check
  .venv/repro312/bin/python -m pip check
  .venv/repro311/bin/python -m pip install --dry-run \
    -c /private/tmp/intel-c1-conflict.txt -r shell/requirements.txt
  .venv/repro311/bin/python tools/python_constraints.py \
    /private/tmp/intel-c1-drift.txt
  ./run python-env-check
  ./run ci-local
  ./run golden
  ./run verify-artifacts
  ./run checklist-audit
  ./run progress-check
  ```

### 2026-07-25 · V2 — `/view` cold path decomposed and future key proven

- owner: Codex
- commit: a8ff3714a6c333d64d5e78ff680ff97291765a88
- result: PASS as a measured design. Internal diagnostic headers and the V2
  benchmark decompose startup/open/backfill/load/analysis/build/serialization/
  transfer without changing the JSON body. No materialization shipped.
- gate: PASS. The implementation adds no table, migration, persisted derived
  response, dependency, or lockfile change. The stale-result and stage-delay
  controls existed and passed before the future representation was selected
  in `docs/V2-VIEW-DESIGN.md`.
- decomposition acceptance: PASS. Two runs × two protected archives × ten
  cold processes produced four tracked reports. Every stage has
  min/median/p95/max and p95 share. Normal cells put analysis at
  85.267–87.950% of cold p95; store open is 0.568–0.685%, and the explicit
  missing-fingerprint backfill check is 0.447–0.581% with zero rows repaired.
- outlier acceptance: PASS. V2 reproduced V1's 1,693.423417 ms sample at
  1,696.948500 ms. Spawn-to-health readiness contributed 1,344.248750 ms,
  while core main-to-listener was 4.430 ms and store open 2.845 ms. The stage
  explains the magnitude and rules out core/store/backfill work; the host
  scheduling/process-observation cause remains explicitly unexplained.
- body acceptance: PASS. All 20 responses per archive match pre-V2 body hashes
  `43af73a081eca3d0e57f646b54129df2a27550b129a56729683fd7c0c413784f`
  and
  `5685e69aafe006ef2cfaf33836a99d36310b9a314594edbd9163ee25bbc8af81`.
- key acceptance: PASS 9/9. The restart-safe logical key detects archive
  identity, sector set, algorithm/schema version, append, update, delete,
  canonical-id rematerialization, fingerprint refresh, and embedding write.
  Omitting embeddings exits non-zero with
  `embedding-write: STALE-RESULT RISK`.
- decomposition control: PASS. A 100 ms injected analysis delay moved analysis
  median by 111.553 ms while sector load moved 0.096 ms; the control exited
  non-zero after proving the intended benchmark failure.
- architecture acceptance: PASS. The future design retains HC1-gated DTOs,
  core-SQL sector enforcement, HC3, global dedup/fingerprint identity, and HC9
  core archive/query ownership. Its implementation gate remains the original
  two-run/two-archive cold ≤162.640 ms and warm ≤32.528 ms thresholds.
- test acceptance: PASS. The exact tree passed 99 warning-denied workspace
  tests, 20 net tests, 114 shell tests under Python 3.11.4 and 3.12.13,
  clippy/fmt, Python byte-compilation, ShellCheck, and locked Rust 1.78.
- local-CI acceptance: PASS 18/18.
- checklist acceptance: PASS. After this audit append supplied V2's real
  implementation hash, `./run checklist-audit` reported 48/48/48 with zero
  exemptions.
- golden-E2E delta: none. Local CI and the final direct `./run golden` each
  passed all 11/11 anchors.
- protected artifact delta: none. Every before/after benchmark check, local CI,
  and final direct verification passed 2/2 with the exact protected hashes.
- exact commands:

  ```bash
  ./run benchmark-view \
    --anchor-ms 16.264 --anchor-source 'v0.9/A3 fixture anchor' \
    --cold-factor 10 \
    --cold-reason 'new process plus archive open and first view' \
    --warm-factor 2 --warm-reason 'memoized response transfer' \
    --cold-slo-ms 162.640 --warm-slo-ms 32.528 \
    --physically-plausible yes --sector science \
    --decomposition-control
  python3 tools/view_invalidation.py control
  python3 tools/view_invalidation.py control --omit-component embeddings
  ./run benchmark-view \
    --anchor-ms 16.264 --anchor-source 'v0.9/A3 fixture anchor' \
    --cold-factor 10 \
    --cold-reason 'new process plus archive open and first view' \
    --warm-factor 2 --warm-reason 'memoized response transfer' \
    --cold-slo-ms 162.640 --warm-slo-ms 32.528 \
    --physically-plausible yes --sector science --cold-iterations 10 \
    --decompose --output-dir evidence/v0.10/view-decomposition
  RUSTFLAGS='-D warnings' cargo test -p cored --locked
  RUSTFLAGS='-D warnings' cargo test -p intel-store \
    migration_backfills_pre_fingerprint_archive_without_changing_identity \
    --locked
  PYTHONPATH=shell .venv/bin/python -m pytest shell/tests -q
  PYTHONPATH=shell .venv/py312/bin/python -m pytest shell/tests -q
  ./run ci-local
  ./run golden
  ./run verify-artifacts
  ./run checklist-audit
  ./run progress-check
  ```

### 2026-07-25 · D5 — all seven deferred triggers re-audited

- owner: Codex
- commit: 0adc739233d69a90e4d6141e17f75acd771873e8
- result: PASS. The executable registry now measures seven triggers from
  repository, process, Git, deployment, benchmark, V1, and V2 evidence. The
  production result is six deferred and one promoted, with zero deferred
  subsystems implemented.
- gate: PASS. Only the already-fired `/view` trigger is promoted, and only to
  the future implementation constrained by `docs/V2-VIEW-DESIGN.md`. D5
  shipped no receipt seam, public-response boundary, cache table, migration,
  concurrent scheduler, second writer, database engine, vector engine, remote,
  runner workflow, dependency, or lockfile change.
- registry acceptance: PASS 7/7. T7 deferred at one supported simultaneous
  harvester; Postgres deferred at one archive writer and zero shell archive
  writers; pgvector deferred at 2,600 documents and 6.431667 ms exact-cosine
  p95 versus the 16.264 ms A3 request anchor; multi-host deferred at zero
  recorded cross-host requests and loopback bind/config; A4 deferred with one
  public path lacking a core-owned response boundary, one shell public egress,
  zero untrusted shells, and zero invariance claims; CI-runner evidence
  deferred with zero remote entries and zero runner executions; `/view`
  promoted from the V1 fired gate and four V2 decomposition reports without
  materialization.
- evidence-input acceptance: PASS. The production command printed the exact
  derived progress list `PROGRESS-v0.10.md`, `PROGRESS-v0.8.md`, and
  `PROGRESS-v0.9.md`. The schema-2 report is tracked at
  `evidence/v0.10/deferred-audit/report.json` and records every unchanged
  trigger, measurement, disposition, measured-source hash, and the explicit
  rule that workflow configuration is not runner execution.
- failure-capable control: PASS. Synthetic measurements supplied two
  harvesters, two archive writers, an over-budget exact-cosine result, a
  remote core hit, an untrusted shell bypass, a Git remote/runner observation,
  and a fired `/view` gate. All seven printed `PROMOTE`; the command exited 1
  with `CONTROL FIRED`.
- regression acceptance: PASS. Four targeted registry tests include a
  production-corpus guard proving the required A4 trigger text is not
  misclassified as an affirmative HC1 invariance claim. Both complete Python
  lanes passed 115 tests with one third-party Starlette warning.
- full acceptance: PASS. The exact implementation tree passed 99
  warning-denied Rust workspace tests, 20 net tests, clippy/fmt, Python 3.11
  byte-compilation, ShellCheck, locked Rust 1.78 check/tests, and
  `./run ci-local` 18/18.
- golden-E2E delta: none. Local CI and the final direct `./run golden` each
  passed all 11/11 anchors.
- protected artifact delta: none. The production audit verified both
  artifacts before and after its disposable-copy benchmark; local CI and the
  final direct `./run verify-artifacts` also passed 2/2 at the exact protected
  hashes.
- exact commands:

  ```bash
  python3 tools/audit_deferred.py --control all-seven
  PYTHONPATH=shell .venv/bin/python -m pytest \
    shell/tests/test_deferred_audit.py -q
  ./run audit-deferred \
    --output evidence/v0.10/deferred-audit/report.json
  PYTHONPATH=shell .venv/bin/python -m pytest shell/tests -q
  PYTHONPATH=shell .venv/py312/bin/python -m pytest shell/tests -q
  python3 -m py_compile \
    tools/audit_deferred.py shell/tests/test_deferred_audit.py
  shellcheck run
  ./run ci-local
  ./run golden
  ./run verify-artifacts
  ./run checklist-audit
  ./run progress-check
  ```

### 2026-07-25 · X1-GATE — battery declared; LAN endpoint unreachable

- owner: Codex
- commit: 03c2420dc0f4e0c676afa75b25beb84b1a307330
- result: DEFERRED before real-model execution. The five-shape adversarial
  battery is declared and failure-capable, but zero real attempts ran because
  the configured LAN chat host was unreachable. X1 remains unchecked.
- gate: TRIPPED. The first provider probe correctly refused to proceed without
  an expected embedding dimension. Re-running with the prior wire-measured
  `LLM_EMBED_EXPECTED_DIMENSION=768` resolved the redacted chat and embedding
  roles, then the chat health request failed with
  `ConnectError: [Errno 65] No route to host` and `TRANSPORT BLOCKED`. The
  embedding role and chat-completion route were not reached.
- classification: no aggregate exists. Zero real attempts is neither
  `NOT EXERCISED` nor a pass. No per-attempt report was created, and no mock
  result was substituted for the unreachable model.
- declared battery: the verifier now nests verbatim quotation, sentence
  continuation, translation round-trip, formatted extraction, and chunked
  reconstruction across every IndexOnly row discovered from the fresh fixture
  corpus. Each attempt records only model identity, endpoint role, target and
  context ids, shape, latency, status, overlap booleans, violation ids, and
  outcome. Prompts, raw responses, credentials, endpoint URLs, and tunnel
  aliases are excluded from the evidence schema.
- failure-capable controls: PASS as harness evidence only. The executable
  classifier control used `tools/mock_openai.py --leak` output plus a simulated
  core refusal to produce `GUARD FIRED`, a paraphrase double to produce
  `NOT EXERCISED`, and a deliberately unattested path to produce `LEAK`.
  Twelve focused verifier tests passed.
- regression acceptance: PASS. The exact harness tree passed 118 shell tests
  under both Python 3.11.4 and 3.12.13, with the same one third-party
  Starlette warning; `./run ci-local` passed 18/18.
- golden-E2E delta: none. Local CI and the final direct `./run golden` each
  passed all 11/11 anchors.
- protected artifact delta: none. Local CI and the final direct
  `./run verify-artifacts` passed 2/2 at the exact protected hashes.
- unblock condition: make both configured model roles reachable, retain the
  768-dimensional embedding expectation, then run
  `./run verify-llm --adversarial-report
  evidence/v0.10/real-model-adversarial/report.json`. A `LEAK` remains an
  immediate HC1 hard stop.
- exact commands:

  ```bash
  PYTHONPATH=shell .venv/bin/python -m pytest \
    shell/tests/test_verify_llm.py -q
  PYTHONPATH=shell .venv/bin/python \
    tools/verify_llm.py --classifier-control
  ./run probe-providers
  LLM_EMBED_EXPECTED_DIMENSION=768 ./run probe-providers
  PYTHONPATH=shell .venv/bin/python -m pytest shell/tests -q
  PYTHONPATH=shell .venv/py312/bin/python -m pytest shell/tests -q
  python3 -m py_compile tools/verify_llm.py \
    shell/tests/test_verify_llm.py
  shellcheck run
  ./run ci-local
  ./run golden
  ./run verify-artifacts
  ./run progress-check
  ```

### 2026-07-25 · X1 — real-model adversarial battery completed

- owner: Codex
- commit: 956e84583575a3229f269aa2d6f64a0a20b154ac
- result: COMPLETE with aggregate **`NOT EXERCISED`**, explicitly not a pass.
  Operator-established loopback forwards made both configured provider roles
  reachable. All 45 declared real-model cells ran without a `LEAK`; 44 model
  calls completed and one timed out after retrieval had already put its named
  target in context.
- gate: NOT TRIPPED. No real public or raw gated overlap occurred. The gate's
  permitted whole-battery non-result applies: 0 `GUARD FIRED`, 45
  `NOT EXERCISED`, 0 `LEAK`.
- battery declared before execution: PASS. The five immutable shapes are
  verbatim quotation, sentence continuation, translation round-trip, formatted
  extraction, and chunked reconstruction. Their declaration SHA-256 is
  `d7e918244ac0d3b61b73d62c1222c384b4d31bbbd1f4b45efa69d804b3d14048`.
- every IndexOnly document targeted: PASS. The fresh 13-document fixture ingest
  discovered nine IndexOnly rows, and the complete matrix contains each of
  their five shapes exactly once. All 45 cells record
  `target_in_context=true` and `valid_attempt=true`.
- per-attempt matrix and aggregate: PASS. The final report is
  `evidence/v0.10/real-model-adversarial/report.json`, SHA-256
  `98fb3a3a1acac844aeccd0da0be2457ff9327ee0733f8570d7edc34b1870f13c`.
  The one non-completing model call is explicitly retained as HTTP 502,
  120048.445 ms, `model_completed=false`; the recording core proved the
  targeted document had already reached context.
- interruption evidence: PASS. The three preserved partial reports have
  SHA-256 values
  `ff154b7ccde7276b7a75f9d6d0eac7ef2fecd98e58ee99381da92f566a62a551`,
  `0272a11a73afbd8210740c46c3f5d02a5175d84138166cfcf58baa2659461780`,
  and
  `2851eda7ba129368e33975437350788cb556dc565a8a01baad7606eb89d91d46`.
  Resume validation pinned the battery, target corpus, and provider identities,
  reused valid cells only, and retried invalid cells only.
- failure-capable control: PASS. The matched leaking-mock report contains the
  same 45 target/shape pairs and classified 45 `GUARD FIRED`, 0
  `NOT EXERCISED`, 0 `LEAK`; all 45 raw answers overlapped gated text and all
  public answers remained clean. Its SHA-256 is
  `ba504a524f9b5df3e7c0bea68523f5b6f6b05aff28090f812c845c60cae9340c`.
  The separate classifier control also emitted all three values, including a
  deliberately unattested `LEAK`.
- evidence hygiene: PASS. All five JSON reports exclude prompts, raw/public
  answers, credentials, authorization headers, endpoint addresses, LAN
  addresses, and tunnel aliases. They retain only the declared secret-free
  operational fields.
- ordinary-path acceptance: PASS. The real provider probe measured chat model
  `gemma-4-26B-A4B-it-UD-IQ4_XS.gguf`, its exact 501 embeddings diagnosis,
  embedding model `embeddinggemma-300M-Q8_0.gguf`, and 768-dimensional
  embeddings. The ordinary verifier ingested 13 documents, embedded 13→0 in
  one provider request, exercised lexical and hybrid retrieval, and returned
  four IndexOnly citations with no public overlap.
- regression acceptance: PASS. Fourteen focused verifier tests passed. Both
  complete Python lanes passed 120 tests with one third-party Starlette
  warning. The exact implementation tree passed `./run ci-local` 18/18,
  including 99 workspace tests, 20 net tests, warning-denied builds,
  clippy/fmt, and the Rust 1.78 lane.
- golden-E2E delta: none. Local CI and the final direct `./run golden` each
  passed all 11/11 anchors.
- protected artifact delta: none. Local CI and the final direct
  `./run verify-artifacts` passed 2/2 at the exact protected hashes.
- exact command families:

  ```bash
  LLM_EMBED_EXPECTED_DIMENSION=768 ./run probe-providers
  LLM_CHAT_TIMEOUT_SECONDS=30 ./run verify-llm \
    --adversarial-report \
    evidence/v0.10/real-model-adversarial/attempt-1-timeout.json
  LLM_CHAT_TIMEOUT_SECONDS=60 ./run verify-llm \
    --adversarial-resume-from \
    evidence/v0.10/real-model-adversarial/attempt-1-timeout.json \
    --adversarial-report \
    evidence/v0.10/real-model-adversarial/attempt-2-timeout.json
  LLM_CHAT_TIMEOUT_SECONDS=120 ./run verify-llm \
    --adversarial-resume-from \
    evidence/v0.10/real-model-adversarial/attempt-2-timeout.json \
    --adversarial-report \
    evidence/v0.10/real-model-adversarial/attempt-3-timeout.json
  LLM_CHAT_TIMEOUT_SECONDS=120 ./run verify-llm \
    --adversarial-resume-from \
    evidence/v0.10/real-model-adversarial/attempt-3-timeout.json \
    --adversarial-report \
    evidence/v0.10/real-model-adversarial/report.json
  python3 tools/mock_openai.py --leak 8899
  ./run verify-llm --adversarial-report \
    evidence/v0.10/real-model-adversarial/leak-control.json
  PYTHONPATH=shell .venv/bin/python tools/verify_llm.py \
    --classifier-control
  PYTHONPATH=shell .venv/bin/python -m pytest \
    shell/tests/test_verify_llm.py -q
  PYTHONPATH=shell .venv/bin/python -m pytest shell/tests -q
  PYTHONPATH=shell .venv/py312/bin/python -m pytest shell/tests -q
  python3 -m py_compile tools/verify_llm.py \
    shell/tests/test_verify_llm.py
  shellcheck run
  ./run ci-local
  ./run golden
  ./run verify-artifacts
  ```

### 2026-07-25 · G2-RUNNER — first observed runner exposed lint divergence

- owner: Codex
- commit: 4244a187683c0f078548c1d2e1727d1d0a8f1114
- result: IN PROGRESS. The operator-approved remote, first main push, complete
  per-job observation, job-set comparison, and failure-capable version
  mismatch control are recorded. G2 remains unchecked until the runner
  ShellCheck finding is corrected separately and a subsequent main run is
  observed.
- first runner: GitHub Actions run
  `30142540466` executed main commit
  `85c78ea0cdf3eb35774c87e4f5c95ccd93dc7adc` for 79 seconds and concluded
  failure. Core, clippy/fmt, net, Rust 1.78, Python 3.12, and golden passed;
  Python 3.11 failed in 5 seconds at `shellcheck ./run`; scheduled drift was
  skipped on the push event.
- measured divergence: runner ShellCheck 0.9.0 emitted SC2120 at `run:171`,
  SC2119 at `run:193`, and SC2015 at `run:246`; local ShellCheck 0.11.0 passed
  the same file. The runner also measured Rust 1.91.1, Rust 1.78.0, Python
  3.11.15, Python 3.12.13, and the Node.js 24 forced action runtime. This
  measurement commit deliberately contains no lint fix.
- job-set comparison: PASS as a finding, not equivalence. Local CI has 18
  ordered checks; GitHub has seven executable push/PR job nodes plus one
  scheduled-only drift node. The report records every grouping and names the
  four local-only gates and three runner-only checks.
- failure-capable control: PASS. Temporary commit
  `b7ed500dc123bdbfd4d7a392bdcb558d508ea85c` changed only the Python version
  source to 9.9.9. PR #1 triggered run `30142678150`; both shell matrix lanes
  failed `release version consistency` and named the planted file/value, while
  core, lint, net, MSRV, and golden passed.
- cleanup: PASS. PR #1 is closed unmerged. The exact temporary branch was
  deleted locally and remotely. Remote `main` remained at `85c78ea`; annotated
  `v0.9.0` tag object `548ffdf` still dereferences to release commit `4c59db2`.
- evidence: `evidence/v0.10/ci-runner/report.json`, SHA-256
  `9cb1a74339313f7e36c33f61f0dd20654e31d5c1aa7103878763a31050d3c4b5`.
- golden-E2E delta: none. The first sandboxed local attempt could not bind
  loopback and made no assertions; the permitted rerun passed 11/11. The first
  real runner's golden job also passed in 76 seconds.
- protected artifact delta: none. Direct verification passed 2/2 at the exact
  recorded hashes.
- exact commands and external observations:

  ```bash
  git remote add origin git@github.com:jiayanzeng/intel-platform.git
  git ls-remote --symref origin HEAD
  git push -u origin main
  git push origin v0.9.0
  ./run version-check
  git push -u origin codex/g2-version-mismatch-control
  git push origin --delete codex/g2-version-mismatch-control
  git branch -D codex/g2-version-mismatch-control
  git ls-remote origin refs/heads/main \
    refs/heads/codex/g2-version-mismatch-control \
    refs/tags/v0.9.0 'refs/tags/v0.9.0^{}'
  ./run golden
  ./run verify-artifacts
  ```

  GitHub public Actions API and authenticated job pages supplied run ids,
  terminal conclusions, per-job timestamps, exact toolchain versions, and the
  ShellCheck/version-check diagnostics. The authenticated GitHub page created
  and closed PR #1 under the operator's explicit approval.

### 2026-07-25 · G2 — CI runner measured and compatibility correction verified

- owner: Codex
- commit: 403c5670e481de0682922bc19d8014112e6fd781
- result: PASS. The first observed run remains recorded as a real failure;
  standalone compatibility commit
  `3648918b8ddcbab04f2a2057d8cc0f0552c3a6d0` corrected it, and subsequent
  main run `30143171409` passed all seven executable jobs. The scheduled-only
  drift job was skipped on the push event and is not described as executed.
- implementation trail: measurement/evidence checkpoint
  `4244a187683c0f078548c1d2e1727d1d0a8f1114`, checkpoint audit
  `6071f28`, compatibility fix `3648918b8ddcbab04f2a2057d8cc0f0552c3a6d0`,
  and this completion commit. The lint finding and lint fix remain separate.
- runner acceptance: PASS. Run `30143171409` executed exact main commit
  `3648918b8ddcbab04f2a2057d8cc0f0552c3a6d0` for 43 seconds. Clippy+fmt
  passed in 20s, golden in 36s, net in 25s, Rust 1.78 in 39s, core in 27s,
  Python 3.11 in 24s, and Python 3.12 in 27s. The Python 3.11 lane's
  `shellcheck run harness` step passed with ShellCheck 0.9.0.
- failure-capable control: PASS. PR #1's planted 9.9.9 mismatch caused both
  shell lanes to fail at `release version consistency`, naming the file and
  value. The PR is closed unmerged; its local and remote branch are deleted.
- job-set comparison: PASS as a measured difference. Local CI has 18 ordered
  checks; GitHub has seven executable push/PR job nodes plus one
  scheduled-only node. The evidence names all four local-only gates and all
  three runner-only checks rather than claiming equivalence.
- release identity: PASS. Remote `main` resolved to compatibility commit
  `3648918b8ddcbab04f2a2057d8cc0f0552c3a6d0` at the acceptance check;
  control branch resolution returned no row; annotated tag object
  `548ffdfec4e414570ddecf813aa2f2d616662487` remained dereferenced to release
  commit `4c59db2727eda1c81beae3ff38be883a26a92ae8`.
- evidence: `evidence/v0.10/ci-runner/report.json`, SHA-256
  `2a8d4db07c6b4cbde72052d336360191b98c6d4dab7138961c0185fd504226c9`.
- local acceptance: PASS. `jq` confirmed the initial failure, later success,
  seven successful executable jobs, one skipped scheduled job, and control
  cleanup. ShellCheck 0.11.0, `bash -n`, `git diff --check`, and the earlier
  full `./run ci-local` all passed; local CI was 18/18 at compatibility commit
  `3648918`.
- golden-E2E delta: none. The first sandboxed attempt could not bind loopback
  and made no assertions; the permitted rerun passed 11/11. The correction
  run's golden job independently passed.
- protected artifact delta: none. Direct verification passed 2/2 at exact
  recorded hashes.
- exact commands and external observations:

  ```bash
  shellcheck run
  bash -n run
  ./run down
  ./run ci-local
  git push origin main
  jq -e '<G2 report acceptance expression>' \
    evidence/v0.10/ci-runner/report.json
  ./run golden
  ./run verify-artifacts
  git ls-remote origin refs/heads/main \
    refs/heads/codex/g2-version-mismatch-control \
    refs/tags/v0.9.0 'refs/tags/v0.9.0^{}'
  ```

  GitHub Actions API supplied the terminal run and job conclusions,
  timestamps, runner identities, and the passing ShellCheck step for
  `30143171409`.

### 2026-07-25 · R3 — v0.10.0 release identity created

- owner: Codex
- commit: 45fa3d49860643fdb2595d82340e364d33566e7d
- result: PASS. The operator selected v0.10.0 because the shipped
  internal `/view` timing headers and measured store-open phases change
  runtime/internal-API behavior even though the JSON body, public API,
  database schema, and cache representation remain unchanged.
- release identity: PASS.
  `v0.10.0` is annotated tag object
  `f70fd84ca0995088d2890096f3429bb878409979`, which dereferences exactly to
  release commit `45fa3d49860643fdb2595d82340e364d33566e7d`. The tag annotation
  is `intel-platform v0.10.0`.
- diff inventory: PASS. All 55 paths in `v0.9.0..v0.10.0` are classified
  exactly once in `STATE.md`: three runtime/storage/internal API, six
  public/release metadata, three operations, 29 executable evidence/controls,
  and 14 documentation/task metadata paths.
- version authorities: PASS. Rust package, Python package, FastAPI literal,
  `STATE.md`, and newest changelog entry all read 0.10.0. Cargo mechanically
  changed only the `cored` package version in `Cargo.lock`; no dependency
  resolution changed.
- mismatch control: PASS. A temporary 9.9.9 Python package value made
  `./run version-check` exit 1 and name
  `shell/intel_shell/__init__.py: 9.9.9`. Restoration returned SHA-256
  `0bd4d3a8ef91761ac81d64c548480010a53830ca4a440598c4c481027d369e05`,
  identical to the pre-control hash, and the checker passed again.
- carried dispositions: X1 remains `NOT EXERCISED`, not a no-leak claim. G2 is
  complete with its first failure, separate compatibility correction, green
  reruns, and deleted control branch. D5 leaves T7 single-flight, Postgres,
  pgvector, multi-host hardening, and the A4 untrusted-shell boundary
  deferred. V2 leaves `/view` materialization for a future implementation.
- candidate acceptance: PASS. Before the release commit, `./run ci-local`
  passed 18/18 with 99 workspace tests, 20 net tests, 120 Python 3.11 tests,
  clippy/fmt, warning-denied builds, Rust 1.78, golden 11/11, protected
  artifacts 2/2, fingerprints, and both lifecycle auditors. The first
  sandboxed Python 3.12 run completed 113 tests with seven loopback-bind
  permission failures; the permitted rerun passed all 120 with one
  third-party Starlette warning.
- final closure audit: PASS. Against the checked runbook, exact closing record,
  and this R3 entry, `./run ci-local` passed 18/18; `cycle-check` reported
  v0.10 closed with five closed execution runbooks; `checklist-audit` resolved
  52/52 checked tasks; `progress-check` resolved this release commit; version
  check matched the exact HEAD tag; golden remained 11/11; protected artifacts
  remained 2/2; and the separate Python 3.12 lane passed 120/120.
- exact commands:

  ```bash
  git diff --name-status v0.9.0
  ./run verify-artifacts
  ./run version-check
  cargo check -p cored
  ./run cycle-check
  shasum -a 256 shell/intel_shell/__init__.py
  ./run version-check
  ./run ci-local
  PYTHONPATH=shell .venv/py312/bin/python -m pytest shell/tests -q
  git tag -a v0.10.0 -m 'intel-platform v0.10.0'
  git rev-parse v0.10.0
  git rev-parse 'v0.10.0^{}'
  git cat-file -t v0.10.0
  ```
