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
