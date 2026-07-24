# PROGRESS-v0.9.md — measured execution record

Entries are append-only and follow the two-commit protocol in `AGENTS.md §5`:
the task implementation/status commit is created first, then its real hash is
recorded here in a separate audit-record commit.

### 2026-07-24 · B0 — v0.9 entering state rebuilt from commands

- owner: 🤖 Codex
- gate: clear. The draft's Git baseline and 92-test count were stale and are
  corrected in `STATE.md`; neither protected artifact changed, so the
  artifact-drift hard stop did not fire.
- Git measurement: the entering worktree was clean at
  `d09eda8cd611c3465aaad7a828465bdb8d8de26f`,
  `v0.8.0-15-gd09eda8`, with no configured remote. Annotated tag object
  `314c1dd914a3d8e9193445874a419ed762581e6e` dereferences to release commit
  `bfc8c5af85734583f966ee70d2ec521155432205`; that commit is an ancestor of
  HEAD, which was 15 commits ahead.
- version measurement: Rust package, Python package, FastAPI literal,
  `STATE.md`, and the newest `CHANGELOG.md` release all reported **0.8.0**.
  `CHANGELOG.md` names `v0.8.0 — 2026-07-24`, matching the existing tag;
  `version-check` passed with the expected ahead-of-tag warning.
- toolchains: pinned rustc/cargo **1.91.1**; floor rustc/cargo **1.78.0**;
  Python **3.11.4** and **3.12.13**; ShellCheck **0.11.0**.
- Rust acceptance: warning-denied locked workspace check passed; **98
  workspace tests** passed; warning-denied net check passed; **20 net ingest
  tests** passed; clippy and fmt passed. Warning-denied locked Rust 1.78
  workspace check and the same **98 tests** passed.
- shell acceptance: Python 3.11 byte-compiled every Python file and passed
  **88 tests**. The system 3.12 interpreter had no pytest, so that preliminary
  command stopped before collection and is not counted. The existing isolated
  3.12.13 environment from B0.2 passed `pip check` and **88 tests** without a
  download. Both counted lanes emitted the same single third-party
  Starlette deprecation warning. ShellCheck passed `run`.
- process/config measurement: `./run down` completed; ports 8787, 8788, and
  8899 were clear. Redacted configuration resolved LAN chat at
  `http://192.168.0.192:8080/v1`, model
  `gemma-4-26B-A4B-it-UD-IQ4_XS.gguf`, timeout 30s, and LAN embeddings at
  `http://192.168.0.192:8081/v1`, model
  `embeddinggemma-300M-Q8_0.gguf`, timeout 30s. The dimension remains the
  previously wire-evidenced **768**. B0 made no provider request and records no
  current availability claim.
- protected evidence:
  - `data/core.db`: SHA-256
    `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`;
    **6,729,728 bytes**; **1,764 documents**; 0 NULL `simhash`; 0 NULL
    `canonical_id`; integrity `ok`; cursor `arxiv-cs | NULL | 2026-07-20 |
    NULL | 2026-07-23 12:08:13`.
  - `data/live-smoke.db`: SHA-256
    `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`;
    **9,490,432 bytes**; **2,600 documents**; 0 NULL `simhash`; 0 NULL
    `canonical_id`; integrity `ok`; cursor `arxiv-cs |
    verb%3DListRecords%26metadataPrefix%3Doai_dc%26from%3D2026-07-22%26until%3D2026-07-22%26set%3Dcs%26skip%3D88
    | NULL | 2026-07-22 | 2026-07-22 23:45:38`.
- failure-capable control: a disposable byte-for-byte `core.db` copy and
  disposable one-entry manifest began at the real expected hash. Adding a
  table only to that copy changed its hash to
  `525370f250e4de32865dbc41f2dbd016f3da5fe754154080e25e1c9a2de28aea`.
  Verification exited **1**, printed expected and actual hashes, and reported
  **0/1 match**. The real manifest immediately passed **2/2**.
- golden E2E: unchanged — final post-status run passed **11/11**: 13/13
  initial ingest; acme complete and 12 analyzed; exact near-duplicate pair at
  hamming 12; DeepSeek RISING z=10.0 from three sources; second acme ingest +0;
  quant-desk 1; public ask four citations with `techwire::tw-004` suppressed;
  IndexOnly snippets NULL; search acme 6 / quant 0; bad-key 401.
- final isolation: protected artifacts **2/2 MATCH**, ports 8787/8788/8899
  clear, `Cargo.lock` untouched.
- acceptance: every entering claim confirmed or corrected ✅ · mismatch
  control failed loudly ✅ · both Python lanes and full Rust matrix green ✅ ·
  tag/HEAD relationship recorded ✅ · golden 11/11 ✅ · protected artifacts
  unchanged ✅
- exact Git/version/tool commands:

  ```bash
  git log --oneline -5
  git status --porcelain
  git describe --tags --always --dirty
  git remote -v
  git cat-file -t v0.8.0
  git rev-parse v0.8.0
  git rev-parse 'v0.8.0^{}'
  git show --no-patch \
    --format='tag-target=%H%nsubject=%s%nauthor-date=%aI%ncommit-date=%cI' \
    'v0.8.0^{}'
  git merge-base --is-ancestor 'v0.8.0^{}' HEAD
  git rev-list --count 'v0.8.0^{}'..HEAD
  sed -n '1,28p' CHANGELOG.md
  ./run version-check
  rustc --version
  cargo --version
  rustup run 1.78.0 rustc --version
  rustup run 1.78.0 cargo --version
  python3.11 --version
  python3.12 --version
  shellcheck --version
  ```

- exact Rust/lint commands:

  ```bash
  RUSTFLAGS="-D warnings" cargo check --workspace --locked --all-targets
  RUSTFLAGS="-D warnings" cargo test --workspace --locked
  RUSTFLAGS="-D warnings" \
    cargo check -p cored --features net --locked --all-targets
  RUSTFLAGS="-D warnings" \
    cargo test -p intel-ingest --features net --locked
  cargo clippy --workspace --locked --all-targets -- -D warnings
  cargo fmt --all -- --check
  RUSTFLAGS="-D warnings" \
    rustup run 1.78.0 cargo check --workspace --locked --all-targets
  RUSTFLAGS="-D warnings" \
    rustup run 1.78.0 cargo test --workspace --locked
  ```

- exact shell commands:

  ```bash
  find tools shell -type f -name '*.py' -print0 |
    xargs -0 python3.11 -m py_compile
  shellcheck ./run
  PYTHONPATH=shell python3.11 -m pytest shell/tests -q
  PYTHONPATH=shell python3.12 -m pytest shell/tests -q
  /private/tmp/intel-platform-py312-baseline.wqTLIV/venv/bin/python --version
  /private/tmp/intel-platform-py312-baseline.wqTLIV/venv/bin/python -m pip check
  PYTHONPATH=shell \
    /private/tmp/intel-platform-py312-baseline.wqTLIV/venv/bin/python \
    -m pytest shell/tests -q
  ```

- exact port/config/artifact commands:

  ```bash
  ./run down
  lsof -nP -iTCP:8787 -sTCP:LISTEN
  lsof -nP -iTCP:8788 -sTCP:LISTEN
  lsof -nP -iTCP:8899 -sTCP:LISTEN
  ./run config
  ./run verify-artifacts
  shasum -a 256 data/core.db data/live-smoke.db
  stat -f 'bytes=%z mtime=%Sm' -t '%Y-%m-%dT%H:%M:%S%z' \
    data/core.db data/live-smoke.db
  sqlite3 -readonly data/core.db \
    "SELECT COUNT(*), SUM(simhash IS NULL), SUM(canonical_id IS NULL) FROM documents;"
  sqlite3 -readonly data/core.db \
    "SELECT integrity_check FROM pragma_integrity_check;"
  sqlite3 -readonly data/core.db \
    "SELECT source_id,cursor,high_water,pending_high_water,updated_at FROM cursors ORDER BY source_id;"
  sqlite3 -readonly data/live-smoke.db \
    "SELECT COUNT(*), SUM(simhash IS NULL), SUM(canonical_id IS NULL) FROM documents;"
  sqlite3 -readonly data/live-smoke.db \
    "SELECT integrity_check FROM pragma_integrity_check;"
  sqlite3 -readonly data/live-smoke.db \
    "SELECT source_id,cursor,high_water,pending_high_water,updated_at FROM cursors ORDER BY source_id;"
  ./run golden
  ./run test
  ./run golden
  ./run verify-artifacts
  ```

- implementation: rolled `AGENTS.md` to the v0.9 task/progress files, corrected
  `STATE.md`, checked B0, and taught the progress checker to select the new
  cycle when its file exists while accepting a valid first entry. A disposable
  one-entry progress file passed; the old v0.8 default still passed before this
  file existed.
- commit: 1054994

### 2026-07-24 · A1 — protected evidence has one executable provenance manifest

- owner: 🤖 Codex
- gate: clear. Pre-edit `./run verify-artifacts` matched both B0 hashes, and
  the proposed external JSON record required no SQLite mutation.
- implementation: replaced the hash-only
  `config/protected-artifacts.sha256` with the single atomic
  `config/protected-artifacts.json` authority. Each record carries path,
  SHA-256, bytes, purpose/provenance, document count, integrity and NULL
  expectations, and complete cursor rows. The standard-library verifier checks
  the manifest schema and all recorded facts through read-only SQLite; the new
  deterministic `./run evidence-report` reports measured values without
  changing the manifest or databases.
- lifecycle/guard: the checked manifest policy declares evidence immutable,
  live harvests fresh-path-only, and new admission contingent on an explicit
  task with captured wire evidence and operator review. Relative,
  `./`-relative, absolute, and symlink aliases of the two protected paths were
  each refused before reachability with exit 2 using that same manifest.
- failure-capable controls:
  - byte control: adding a table only to a disposable `core.db` copy retained
    the original record, exited 1, and named `core.db field=sha256`; actual
    SHA-256 was
    `811d8b6c32f9bb976bd4dc9e49a524940ac3183faec9d31044bc59196d987482`.
  - logical corpus control: deleting one copied document and refreshing the
    disposable record's hash/size exited 1 only on `core.db field=documents`,
    with 1,764 expected and 1,763 actual.
  - logical cursor control: setting the copied `arxiv-cs` cursor to
    `a1-control` and refreshing hash/size exited 1 only on
    `core.db field=cursors.arxiv-cs.cursor`.
  - the five committed disposable-database tests passed and preserve those
    failures, deterministic reporting, and canonical alias resolution.
- verification: `./run test` began with the stronger 2/2 verification and
  passed **98 workspace**, **20 net**, and **93 Python 3.11 shell** tests.
  The isolated Python **3.12.13** lane independently passed the same **93**
  shell tests. `./run ci-local` passed all **16/16** jobs: version,
  Python-floor compilation, ShellCheck, warning-denied workspace/net checks and
  tests, clippy, fmt, locked Rust 1.78 check/tests, shell tests, golden,
  protected artifacts, persisted fingerprints, and progress validation. CI
  now validates the committed manifest schema and runs the disposable verifier
  controls; no CI runner execution is claimed.
- golden-E2E delta: **none**. The output-preserving task passed all **11/11**
  named assertions with the same 13→12 corpus, near-duplicate decision,
  DeepSeek z=10.0 signal, quant-desk count, and four-citation public answer.
- final isolation: `data/core.db` remained
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  / 6,729,728 bytes / 1,764 documents, and `data/live-smoke.db` remained
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`
  / 9,490,432 bytes / 2,600 documents. Both had integrity `ok`, zero NULL
  fingerprint/identity fields, and one matching cursor. `Cargo.lock` was
  untouched.
- acceptance: one authoritative manifest ✅ · hash and logical metadata
  checked ✅ · refusal covers both paths and canonical aliases ✅ · three
  controls fail on their intended fields ✅ · protected bytes unchanged ✅ ·
  golden unchanged ✅
- exact verification commands:

  ```bash
  python3 tools/evidence_artifacts.py validate
  ./run verify-artifacts
  ./run evidence-report
  ./run evidence-report > /private/tmp/intel-evidence-report-1.json
  ./run evidence-report > /private/tmp/intel-evidence-report-2.json
  cmp /private/tmp/intel-evidence-report-1.json \
    /private/tmp/intel-evidence-report-2.json
  PYTHONPATH=shell .venv/bin/python \
    -m pytest shell/tests/test_evidence_artifacts.py -q
  bash -n run
  shellcheck ./run
  ./run ci-local
  ./run test
  PYTHONPATH=shell \
    /private/tmp/intel-platform-py312-baseline.wqTLIV/venv/bin/python \
    -m pytest shell/tests -q
  ./run version-check
  ./run verify-artifacts
  shasum -a 256 data/core.db data/live-smoke.db
  ```

- commit: 2adf486

### 2026-07-24 · D3 — v0.9 runbook reconciled with measured state

- owner: 🤖 Codex
- gate: clear. Before any tracked edit, `./run verify-artifacts` matched both
  protected records exactly and `./run golden` passed all **11/11** named
  assertions. No rule, command, source file, dependency, lockfile, or protected
  artifact changed.
- entering/provenance corrections: the original v0.9 entering-state and closing
  drafting paragraphs remain intact. Dated additions record B0 `1054994` and
  A1 `2adf486`: clean
  `d09eda8cd611c3465aaad7a828465bdb8d8de26f`,
  `v0.8.0-15-gd09eda8`, 15 commits after release commit `bfc8c5a` and annotated
  tag object `314c1dd`; **98 workspace / 20 net / 88 shell** tests at B0 and
  **93 shell** tests after A1; and
  `config/protected-artifacts.json` as the sole expected-hash authority after
  A1 deleted the legacy SHA-256 list. The closing correction records B0 and A1
  as executed on 2026-07-24.
- id/numbering disposition: no committed record outside the active runbook
  cited the old P2/V1/deferred-audit/R2 step-number assignments. D3 therefore
  became **Step 3** and P2/V1/D4/R2 became **Steps 4–7**; the Step 2A fallback
  was not used. The colliding unstarted v0.9 `D1` is now `D4`. The already
  committed v0.9 `A1` is retained and explicitly distinguished from v0.8.2's
  fingerprint-verifier `A1`.
- remaining-task correction: V1's recommended thresholds now derive from A3's
  **0.016264 s** post-change `POST /retrieve` measurement on the 2,600-row
  archive (`learning`, sector `science`, `k=8`). The predeclared recommendation
  is cold p95 **10× = 162.640 ms** and warm p95 **2× = 32.528 ms**, with anchor,
  factors/reasons, exact firing values, and host plausibility recorded before
  timing. An SLO that cannot fire is a defect. V1 requires disposable copies of
  both 1,764- and 2,600-row archives, both distributions and their slope,
  sectors drawn from `config/core.json`, non-zero counts for every sample, and
  warm cache hits against an unmoved generation; an empty-sector warm path
  fails. V1 now has 🤖 + 🧑 ownership. P2 ships its harness half under a
  transport block but keeps the live leg an exact unchecked non-result for an
  in-cycle rerun. R2 must state the disposition of every carried non-result.
- STATE corrections: a dated addition supersedes P1's preserved present-tense
  reference to the deleted hash list without editing the P1 body. A second
  dated addition records that manifest admission is not executable: code
  validates the fixed `admission` literal, but nothing records or verifies the
  claimed wire evidence and operator review when an expected hash changes.
  Git review remains the sole prose control. A failure-capable admission control
  is a v0.10 candidate triggered before the first proposed protected-artifact
  admission or expected-hash change; D3 implemented no control.
- Python-lane order: the old counted Python 3.12 lane and the Python 3.11 lane
  were frozen, in that order, before `.venv/py312` was cleared or populated.
  The exact commands were:

  ```bash
  /private/tmp/intel-platform-py312-baseline.wqTLIV/venv/bin/python -m pip freeze
  .venv/bin/python -m pip freeze
  ```

- old Python 3.12 lane `pip freeze` stdout, verbatim:

  ```text
  annotated-doc==0.0.4
  annotated-types==0.8.0
  anyio==4.14.2
  certifi==2026.7.22
  click==8.4.2
  fastapi==0.139.2
  h11==0.16.0
  httpcore==1.0.9
  httpx==0.28.1
  idna==3.18
  iniconfig==2.3.0
  packaging==26.2
  pluggy==1.6.0
  pydantic==2.13.4
  pydantic_core==2.46.4
  Pygments==2.20.0
  pytest==9.1.1
  starlette==1.3.1
  typing-inspection==0.4.2
  typing_extensions==4.16.0
  uvicorn==0.51.0
  ```

- Python 3.11 lane `pip freeze` stdout, verbatim:

  ```text
  annotated-doc==0.0.4
  annotated-types==0.7.0
  anyio==4.14.2
  certifi==2026.6.17
  click==8.4.2
  fastapi==0.139.2
  h11==0.16.0
  httpcore==1.0.9
  httpx==0.28.1
  idna==3.18
  iniconfig==2.3.0
  packaging==26.2
  pluggy==1.6.0
  pydantic==2.13.4
  pydantic_core==2.46.4
  Pygments==2.20.0
  pytest==9.1.1
  starlette==1.3.1
  typing-inspection==0.4.2
  typing_extensions==4.16.0
  uvicorn==0.51.0
  ```

- Python-lane finding: the frozen lanes differ only at `annotated-types`
  (3.11 **0.7.0**, old 3.12 **0.8.0**) and `certifi` (3.11 **2026.6.17**,
  old 3.12 **2026.7.22**). After both freezes, Python 3.12.13 created the
  ignored `.venv/py312`; installation from the unchanged
  `shell/requirements.txt` resolved byte-for-byte to the old 3.12 freeze,
  `pip check` reported no broken requirements, and the lane passed **93 shell
  tests** with one Starlette warning. The requirements are floors, not pins,
  so the command is repeatable but the resolved environment is not
  reproducible. Pinning or a constraints file is a v0.10 candidate; D3 did not
  edit the build input. The old temp lane remains present.
- exact Python 3.12 rebuild/verification commands:

  ```bash
  python3.12 -m venv --clear .venv/py312
  .venv/py312/bin/python -m pip install -r shell/requirements.txt
  .venv/py312/bin/python -m pip check
  PYTHONPATH=shell .venv/py312/bin/python -m pytest shell/tests -q
  ```

- measured matrix: `./run ci-local` passed all **16/16** jobs: version
  consistency; Python 3.11 byte-compilation; ShellCheck; warning-denied locked
  workspace check and **98 tests**; warning-denied locked net check and
  **20 tests**; clippy; fmt; warning-denied locked Rust 1.78 check and
  **98 tests**; **93 Python 3.11 shell tests** with one Starlette warning;
  golden **11/11**; protected artifacts **2/2** exact; persisted-fingerprint
  fixture; and progress validation. The new Python 3.12.13 lane independently
  passed **93 shell tests** with the same single warning. Final
  `./run version-check`, `./run verify-artifacts`, ShellCheck, Python 3.11
  byte-compilation, and golden **11/11** also passed.
- golden-E2E delta: **none**. The final run retained all eleven named
  assertions: 13 initial documents, 12 analyzed, the exact hamming-12
  near-duplicate decision, DeepSeek RISING at z=10.0, zero second-ingest
  additions, quant-desk count one, four citations with the duplicate
  suppressed, NULL IndexOnly snippets, sector-disjoint search counts, and
  bad-key 401.
- protected evidence: final verification retained
  `data/core.db` at
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`,
  6,729,728 bytes, 1,764 documents, and `data/live-smoke.db` at
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`,
  9,490,432 bytes, 2,600 documents; both records matched all logical facts.
- grep 1 — old step-number citations in committed records outside the active
  runbook. Exit **1** with no stdout means no citation:

  ```bash
  git grep -nE \
    '(Step 3.{0,80}P2|P2.{0,80}Step 3|Step 4.{0,80}V1|V1.{0,80}Step 4|Step 5.{0,80}D1|D1.{0,80}Step 5|Step 6.{0,80}R2|R2.{0,80}Step 6)' \
    HEAD -- '*.md' ':!TASKS-v0.9-EXECUTION.md'
  ```

  ```text
  <no matches>
  ```

- grep 2 — live old id and unstarted closed-runbook task-heading collisions.
  Both commands exited **1** with no stdout:

  ```bash
  grep -nE '(^|[^[:alnum:]_])D1([^[:alnum:]_]|$)' \
    TASKS-v0.9-EXECUTION.md
  grep -nE \
    '^## (Step [^ ]+ · )?(P2|V1|D4|R2)([[:space:]]|—|·)' \
    TASKS-v0.8.md TASKS-v0.8-EXECUTION.md \
    TASKS-v0.8.1-EXECUTION.md TASKS-v0.8.2-EXECUTION.md
  ```

  ```text
  <no live v0.9 D1 matches>
  <no closed-runbook P2/V1/D4/R2 task-heading matches>
  ```

- grep 3 — all remaining legacy hash-list references:

  ```bash
  grep -rn --include='*.md' --exclude-dir=.git --exclude-dir=.venv \
    --exclude-dir=target --exclude-dir=data \
    'protected-artifacts.sha256' .
  ```

  ```text
  ./PROGRESS-v0.9.md:173:  `config/protected-artifacts.sha256` with the single atomic
  ./PROGRESS-v0.8.md:521:  `config/protected-artifacts.sha256` ✅ · canonicalized protected paths refused
  ./STATE.md:72:`config/protected-artifacts.sha256` has been removed, and
  ./STATE.md:159:`config/protected-artifacts.sha256` is historical. A1 deleted that file;
  ./STATE.md:1475:- `config/protected-artifacts.sha256` records the complete B0.1 hashes for
  ./TASKS-v0.8.2-EXECUTION.md:22:documents), recorded in `config/protected-artifacts.sha256`.
  ./TASKS-v0.9-EXECUTION.md:17:with hashes recorded in `config/protected-artifacts.sha256`. The dedicated LAN
  ./TASKS-v0.9-EXECUTION.md:28:> deleting `config/protected-artifacts.sha256`. The asserted paragraph above
  ./TASKS-v0.9-EXECUTION.md:119:**Objective.** `config/protected-artifacts.sha256` proves byte identity, but not
  ```

  The first hit is A1's completed append-only history; the second is
  closed-cycle P1 history; STATE lines 72 and 159 are the new A1 and D3 dated
  corrections; STATE line 1475 is P1's deliberately preserved historical
  body; the v0.8.2 hit is closed-cycle entering history; v0.9 line 17 is the
  preserved entering hypothesis, line 28 is its dated correction, and line 119
  is A1's historical objective. There are no live operational references.
- acceptance: entering state bannered, not rewritten ✅ · closing provenance
  appended ✅ · P1 superseded by dated addition, body untouched ✅ ·
  `D1`→`D4`, no live collision ✅ · committed A1 disambiguated, not renamed ✅ ·
  Step 3 / Steps 4–7 path recorded ✅ · V1 SLO anchored with exact firing
  values, both corpora, slope, and warm-path validity ✅ · V1 owner corrected
  ✅ · P2 blocked path and R2 non-result disposition defined ✅ · Python 3.12
  command executed and measured ✅ · floors-not-pins and manifest-admission
  risks recorded as v0.10 candidates ✅ · no source, rule, command, dependency,
  lockfile, or protected-data change ✅
- commit: d8d7551421242a9d32eb47077628607e0b06f565
- progress-check failure control: changing only the D3 value above to
  `NOT_A_HASH` made `./run progress-check` exit **1** and name the exact field:

  ```text
  progress-check: ERROR: PROGRESS-v0.9.md:457: commit must be 7-40 lowercase hexadecimal characters; found 'NOT_A_HASH'
  ```

  Restoring the real hash returned the file to its pre-control SHA-256
  byte-for-byte, and `./run progress-check` then passed while naming D3 and the
  real implementation hash.
- final grep disposition: after this append, D3 audit line 427 is the captured
  search command and lines 431–439 are its quoted nine-line output. Those ten
  self-hits belong to this dated correction entry: the command is evidence,
  while each quoted line is the already-enumerated historical or correction
  reference, not a new live operational authority.

### 2026-07-24 · P2 — provider-probe harness shipped; live leg blocked

- owner: 🤖 Codex + 🧑 operator route action pending
- gate: **tripped for the live leg only.** Both configured direct `/health`
  routes returned curl exit 7 / HTTP 000 / `Couldn't connect to server`; the
  operator-owned SSH-forward aliases were not listening. D3's blocked-path
  clause therefore permits the harness half to ship but leaves P2 unchecked.
  No mock result is promoted to wire evidence, no provider identity or
  dimension is re-measured, and no correction-cycle file is opened.
- implementation: added `./run probe-providers`, which uses the same resolved
  chat and embedding roles as the product path. The selected profile/direct
  role remains authoritative for provider endpoint, model, credential, and
  timeout. Per-command `LLM_CHAT_TRANSPORT_BASE_URL` and
  `LLM_EMBED_TRANSPORT_BASE_URL` values replace only the effective request
  route after identity resolution; loopback aliases ignore ambient proxies.
  `./run config` now prints both configured and effective endpoints, models,
  role timeouts, and the predeclared embedding dimension with keys redacted.
- capability sequence: the command captures chat `/health` and `/v1/models`,
  then requires the known HTTP 501 chat-embeddings diagnosis without failing
  the overall probe. It next captures embedding `/health` and `/v1/models`,
  requests one short embedding, requires exactly one finite vector at index 0,
  and compares its measured width to `LLM_EMBED_EXPECTED_DIMENSION`. It reports
  a bounded redacted body and status for every response; a transport failure
  explicitly reports `status=none body=none`.
- classifications: exactly `PASS`, `TRANSPORT BLOCKED`, `IDENTITY CHANGED`,
  and `CAPABILITY FAILED`. Only `PASS` exits zero. Missing/invalid expected
  dimension is a capability failure rather than an inferred value. A transport
  alias cannot weaken the non-loopback provider-model requirement in
  `verify-llm`.
- failure-capable controls:
  - passing local doubles returned chat's known 501 and one four-dimensional
    embedding. Both doubles echoed their Authorization values; neither secret
    appeared in probe output and both were replaced with `[REDACTED]`.
  - a wrong chat model produced `IDENTITY CHANGED`, exit non-zero.
  - an empty embedding item list produced `CAPABILITY FAILED`, exit non-zero.
  - a five-dimensional vector against expected width four produced
    `IDENTITY CHANGED`, exit non-zero.
  - a real 200 ms delayed health response under a 50 ms embedding-role timeout
    raised `ReadTimeout`, produced `TRANSPORT BLOCKED`, and exited non-zero.
  The targeted provider/config command passed **15/15** tests.
- direct-route live disposition:

  ```text
  http://192.168.0.192:8080/health
  curl exit=7 status=000 after 1 ms
  curl: (7) Failed to connect ... Couldn't connect to server

  http://192.168.0.192:8081/health
  curl exit=7 status=000 after 1 ms
  curl: (7) Failed to connect ... Couldn't connect to server
  ```

  With expected dimension 768, the new command stopped at its first live
  prerequisite and exited 1:

  ```text
  chat health: route=http://192.168.0.192:8080/health status=none body=none error=ConnectError: [Errno 65] No route to host
  TRANSPORT BLOCKED: chat health could not complete on http://192.168.0.192:8080/health
  ```

- transport-alias disposition: the configured identities remained the LAN
  Gemma and EmbeddingGemma roles, while `./run config` showed effective
  loopback routes `127.0.0.1:18080/18081`. The probe returned
  `[Errno 61] Connection refused` at chat `:18080/health`; an independent
  bounded curl to embedding `:18081/health` returned exit 7 / HTTP 000 /
  `Couldn't connect to server` after 0 ms. No forward was inferred from T4's
  historical evidence.
- live acceptance: **non-result, P2 remains open.** `./run verify-llm` was not
  invoked because the minimal probe did not pass. Required next action:
  operator starts the same SSH forwards and confirms the route; Codex reruns
  the exact probe in-cycle and, only after `PASS`, runs one fresh uninterrupted
  verifier. P2's checkbox stays unchecked until both halves are recorded.
- measured matrix: `./run ci-local` passed all **16/16** jobs—version,
  Python-floor byte-compilation, ShellCheck, warning-denied workspace check and
  **98 tests**, warning-denied net check and **20 tests**, clippy, fmt, locked
  Rust 1.78 check/tests, **99 Python 3.11 shell tests**, golden **11/11**,
  protected artifacts **2/2**, persisted fingerprints, and progress
  validation. The rebuilt Python 3.12.13 lane independently passed the same
  **99 shell tests**; both lanes emitted one third-party Starlette warning.
  A separate golden run with hostile inherited transport aliases pointing to
  unused loopback ports still passed 11/11, proving the deterministic mock path
  clears live overrides.
- golden-E2E delta: **none**. All eleven named assertions remained exact.
- final isolation: `data/core.db` remained
  `db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`
  / 6,729,728 bytes / 1,764 documents; `data/live-smoke.db` remained
  `94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`
  / 9,490,432 bytes / 2,600 documents. Both records matched all logical
  fields. `Cargo.lock`, `shell/requirements.txt`, and `ARCHITECTURE.md` were
  untouched.
- exact harness commands:

  ```bash
  PYTHONPATH=shell .venv/bin/python \
    -m pytest shell/tests/test_provider_probe.py \
    shell/tests/test_llm_config.py -q
  PYTHONPATH=shell .venv/bin/python -m pytest shell/tests -q
  PYTHONPATH=shell .venv/py312/bin/python -m pytest shell/tests -q
  LLM_EMBED_EXPECTED_DIMENSION=768 ./run probe-providers
  LLM_CHAT_TRANSPORT_BASE_URL=http://127.0.0.1:18080/v1 \
  LLM_EMBED_TRANSPORT_BASE_URL=http://127.0.0.1:18081/v1 \
  LLM_EMBED_EXPECTED_DIMENSION=768 ./run config
  LLM_CHAT_TRANSPORT_BASE_URL=http://127.0.0.1:18080/v1 \
  LLM_EMBED_TRANSPORT_BASE_URL=http://127.0.0.1:18081/v1 \
  LLM_EMBED_EXPECTED_DIMENSION=768 ./run probe-providers
  ```

- exact regression commands:

  ```bash
  bash -n run
  shellcheck ./run
  ./run ci-local
  LLM_CHAT_TRANSPORT_BASE_URL=http://127.0.0.1:1/v1 \
  LLM_EMBED_TRANSPORT_BASE_URL=http://127.0.0.1:2/v1 ./run golden
  ./run verify-artifacts
  ```

- acceptance: harness half shipped ✅ · configured/effective roles redacted ✅ ·
  every request role-timeout-bounded ✅ · four classifications and non-zero
  failure exits proven ✅ · wrong model, short data, wrong dimension, and stall
  controls proven ✅ · keys absent from output ✅ · live leg recorded as an
  exact unchecked non-result ⏳ · protected artifacts exact ✅ · golden
  unchanged ✅
- commit: 18887f7113c27bb2f0b91d5a0b37fb396961ac64
