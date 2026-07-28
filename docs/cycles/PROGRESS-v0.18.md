# PROGRESS-v0.18.md — append-only execution record

This file records v0.18 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-28 · ACTIVATE — v0.18 admitted

- owner: Codex
- commit: 50ac8d0
- result: PASS for cycle activation only; E0 remains unchecked. Before
  activation, local `main` and the measured `origin/main` tracking ref were
  aligned at `f13c6129d608ab9259f421dce6ed419ce469c225`.
- worktree acceptance: PASS. The only pre-activation worktree item was the
  operator-supplied untracked `TASKS-v0.18-EXECUTION.md`; implementation commit
  `50ac8d0` contains only that runbook, the `AGENTS.md` v0.18 declaration, and
  this new append-only progress log.
- published-tag acceptance: PASS. Annotated `v0.15.1` remains tag object
  `d6a71c1a2afabd7ce7b335756b7ae66ff36cf1ba`, dereferencing exactly to release
  commit `a0ba69e0a3e8385287274bb404d5123f9a2b8ac7`.
- lifecycle acceptance: PASS. `./run cycle-check` reports active v0.18 open
  with fifteen closed execution runbooks. `./run checklist-audit` resolves the
  entering 144 checked tasks, reports the same three retractions, and finds zero
  exemptions. `git diff --check` passed.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the complete
  entering matrix and G1–G6 measurements.
- golden-E2E delta: NOT MEASURED; no claim.
- protected artifact delta: NOT MEASURED; no protected or pinned file changed.

### 2026-07-28 · E0 — entering state and incident boundary measured

- owner: Codex
- commit: 9222e18
- result: PASS. The read-only Gate was defined before the first E0 commit and
  contains the status/runbook acceptance surfaces; no product path, dependency,
  lockfile, protected artifact, or public surface changed.
- entering-matrix acceptance: PASS at activation-audit commit `af961f9` with
  `CARGO_TARGET_DIR=/private/tmp/intel-v018-e0-ci-target`. The first sandboxed
  attempt was a non-result because the net fixture could not bind loopback; the
  identical permitted invocation passed **20/20** jobs with **131** workspace
  tests, **55** net tests (**29** ingest plus **26** cored), Python 3.11.4 shell
  **244/244**, warning-denied offline/net builds, clippy, fmt, ShellCheck,
  locked Rust 1.78 check/test, `invariant-scan` **11/11 rules / 23 controls**,
  all **146/146** pins, both protected databases exact, and golden **11/11**.
- interpreter acceptance: PASS. Clean rebuilds resolved all **21/21** pinned
  packages and passed shell **244/244** under Python 3.11.4 and Python 3.12.13,
  with the same single third-party deprecation warning.
- G2 configured-URL acceptance: PASS. The live harness strips the fixture only
  from `arxiv-cs`; its configured `/oai?...` target is identical under old and
  corrected derivations. The three multi-segment `example.org` URLs differ but
  remain fixture-only and issue no publisher request.
- G2 redirect acceptance: PASS. The historically observed `/oai2?...` to
  `/oai?...` redirect is single-segment and identical under both derivations.
  The constructed multi-segment control `/oai/archive/page?cursor=abc`
  distinguishes old `/oai` from the corrected full target. No configured live
  URL or historically observed redirect was affected.
- G1 acceptance: PASS and closed clean. Direct helpers preserve scheme/host
  case, but production `get_text_with` parses the initial URL and joins every
  redirect through `reqwest::Url` before the sole production network call to
  `gate()`. A temporary executing mixed-case initial/redirect control passed
  **1/1** and observed only lowercase robots URLs, page URLs, and limiter keys;
  it was removed after measurement. ORIGIN-CASE must therefore skip.
- source-inventory acceptance: PASS. Configuration contains **4** sources:
  `arxiv-cs` is the sole real publisher; the other **3** are `example.org`
  placeholders.
- published-object/pin acceptance: PASS by live remote inspection. `main`
  remains `f13c6129…`; annotated `v0.15.1` remains tag object `d6a71c1…`
  peeled to release commit `a0ba69e0…`; manifest validation passes with
  **146/146** pins and both protected databases exact.
- golden-E2E delta: **0**; both the entering matrix and mandatory post-status
  standalone invocation passed **11/11**.

### 2026-07-28 · ORIGIN-CASE — skipped at the clean G1 gate

- owner: Codex
- commit: 56d1911
- result: SKIPPED exactly as the task Gate requires. E0 proved the case-sensitive
  helpers are not reachable with mixed-case authority bytes on the production
  network path because `reqwest::Url` normalizes the initial URL and every
  redirect before `gate()`.
- implementation acceptance: NOT APPLICABLE. No production or test source,
  dependency, lockfile, public surface, schema, or protected artifact changed.
  The production ingest blobs remain `773d7ffe…` for `lib.rs` and `09503192…`
  for `net.rs`.
- unchanged-behavior acceptance: PASS. The existing URL case-table and
  same-origin redirect controls each pass **1/1**. Path bytes and path case,
  explicit-port preservation, and userinfo exclusion remain unchanged because
  no normalization implementation was made.
- authority-encoding scope: RECORDED as out of scope for this skipped step. The
  shipped path continues to use `reqwest::Url` authority parsing; no second
  percent-encoding normalization layer was introduced.
- golden-E2E delta: **0**; the mandatory standalone invocation passed
  **11/11**.

### 2026-07-28 · ROBOTS-PREVIEW — live absence disposition recorded

- owner: Codex
- commit: 6ede754
- result: PASS with **GO** for LIVE-HARVEST. The sole configured network
  source, `arxiv-cs`, made exactly one request under the installed
  `intel-platform/0.15.1` crawler identity:
  `GET https://oaipmh.arxiv.org/robots.txt`. Redirects were disabled and none
  was followed; the configured contact was loaded from ignored `.env` and was
  not recorded.
- live-policy acceptance: PASS. The origin returned HTTP **404**,
  `Content-Type: text/html; charset=utf-8`, with **11,083** raw bytes. There was
  therefore no selected specific or `*` group, matched rule, `Allow` exception,
  or `Crawl-delay`. The per-source `robots_on_missing: "allow"` maps to
  `MissingPolicy::RfcAllowAll`, so the configured `/oai?...` target is allowed.
  Explicit policies and unreachable responses remain fail-closed.
- reproducibility acceptance: PASS. The raw response is committed at
  `observations/v0.18/robots-preview/arxiv-cs-robots.txt`, SHA-256
  `fe5a8ce88b89f96db55e8d9a7eb3d978f3d364bf31d48c4880422511e9035ab2`,
  with its command/result report alongside.
- robots-only acceptance: PASS. The feature-gated client constructs literal
  `/robots.txt`, disables redirects, and contains one send call. Its loopback
  control observed exactly one `/robots.txt` request with the installed
  identity; the live run reported request count **1**, path `/robots.txt`, and
  redirects **0**. No document or harvest URL was requested.
- fail-before/pass-after acceptance: PASS. Missing diagnostic matcher and
  preview-fetch surfaces first made their focused builds exit **101**.
  Pass-after suites report compliance diagnostics **40/40**, ingest preview
  library **30/30**, and preview binary **1/1**. A sandboxed loopback attempt
  was a non-result; its identical permitted invocation passed.
- scope acceptance: PASS. No dependency was added; `Cargo.lock`, default and
  `net`-only public APIs, `/v1/*`, SQLite schema, protected artifacts, and the
  harvest path are unchanged. The staged raw response and report passed R4's
  tracked-text credential scan.
- matrix acceptance: PASS. Local CI passed **20/20** with **131** workspace
  tests, **55** net tests (**29** ingest plus **26** cored), shell **244/244**,
  locked Rust 1.78, all **146/146** pins, protected databases **2/2**, and zero
  final rustc/clippy/fmt/ShellCheck failures. Supplemental preview clippy first
  caught two `needless_borrow` warnings; after the two call-site correction it
  passed with `-D warnings`.
- golden-E2E delta: **0**; the final mandatory standalone invocation passed
  **11/11**.

### 2026-07-28 · LIVE-HARVEST — corrected gate reached real OAI-PMH pages

- owner: Codex
- commit: 4b99c65
- result: PASS with one finding carried to WIRE-FINDINGS. One bare
  `./run harvest-arxiv` launched one core (PID 13809) against fresh ignored
  `data/live-20260728T141101Z-13711.db`; no pre-existing core or port-8788
  listener existed and no concurrent harvester was started.
- isolation acceptance: PASS. The fresh database is **10,166,272** bytes,
  SHA-256
  `11d2b6a6bdf15b27964eae2be971deb0b056d47546ea96dd47a6eb1e56e58d6a`,
  integrity `ok`. It is an observation, not evidence. No harvested document
  entered the golden/protected corpus. Preflight and post-run verification
  both passed all **146/146** pins and protected databases **2/2** exact;
  `./run down` left port 8788 free.
- policy/politeness acceptance: PASS. The live gate observed Step 3's
  404/`Unavailable(allow)` disposition on each page. No publisher
  `Crawl-delay` existed; all three requests reported the **0.500-second**
  operator floor.
- paging acceptance: PASS. Three real XML pages committed with cumulative
  counts **1,300**, **2,600**, and **2,692**. Two returned
  `resumptionToken`s were followed and page 3 was naturally final. The final
  persisted row is `cursor=NULL`, `high_water=2026-07-28`,
  `pending_high_water=NULL`.
- wire-shape acceptance: PASS. Exactly **3** page-request lines and **3**
  robots-gate lines appeared. No redirect, 503/Retry-After, extra attempt,
  status-error, parse-error, or unexpected XML-shape log appeared; source
  result was `ok=true`. The database holds **2,692** rows in **2,550**
  canonical groups, with **142** near-duplicate rows suppressed from analysis.
- duration acceptance: PASS. Total command wall time, including artifact
  preflight and the net build, was **46.38 seconds**.
- finding: **F1** — the harness said `cored` remained running for inspection,
  but after command exit PID 13809 was absent and `/health` refused connection.
  Step 5 must give this finding exactly one disposition. No publisher
  compliance, XML, paging, cursor, retry, redirect, or status defect was found.
- golden-E2E delta: **0**; the mandatory standalone invocation passed
  **11/11** after the harvest.

### 2026-07-28 · WIRE-FINDINGS — managed-core lifecycle made deterministic

- owner: Codex
- commit: dae015e
- result: PASS. Step 4 finding F1 has exactly one disposition: **fixed with an
  offline regression test**. `cmd_harvest_arxiv` now calls `cmd_down` after
  printing its evidence-backed checklist, reports the observation database and
  runtime log, and makes no false claim that its managed core remains running.
- regression acceptance: PASS. The executing fail-before removed the terminal
  shutdown and failed **1/1** with `cmd_harvest_arxiv must stop its managed
  core before returning`; the pass-after harness file passed **2/2**.
- fixture acceptance: PASS, no addition required. No real XML shape, status
  code, or redirect differed from existing fixture coverage, so no
  publisher-derived fixture was manufactured.
- corpus/scope acceptance: PASS. No publisher request, live database write,
  harvested fixture/document, protected database, evidence artifact/receipt,
  dependency, schema, model-profile behavior, or public-surface change
  occurred. No harvested document entered the protected or golden corpus.
- authorization-pin acceptance: PASS. `run` moved from
  `7351f2ffb7eb6def34c99c812a61a10690b6f690e9e1e44cee88790ca6dcc455`
  (**41,959** bytes) to
  `caae4e8007fc885241bf1ac7c844e397a149970048e036be285e356449030678`
  (**42,056** bytes); its model-profile functions and dispatch,
  `tools/model_profiles.py`, and the authorization policy remain unchanged.
  Manifest validation and `verify-artifacts` passed all **146/146** pins and
  protected databases **2/2** exact.
- matrix acceptance: PASS. Local CI passed **20/20** with **131** workspace
  tests, **55** net tests, shell **245/245** on both Python 3.11.4 and 3.12.13,
  locked Rust 1.78, zero rustc/clippy/fmt/ShellCheck failures, and
  `invariant-scan` **11/11 rules / 23 controls**. The first sandboxed Python
  3.12 attempt was a permission non-result; the identical authorized command
  passed.
- golden-E2E delta: **0**; the mandatory standalone invocation passed
  **11/11** byte-identically.
