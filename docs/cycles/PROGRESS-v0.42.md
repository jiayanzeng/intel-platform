# PROGRESS-v0.42.md — append-only execution record

This file records v0.42 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-08-05 · ACTIVATE — v0.42 cycle activation

- owner: Codex
- runbook: `TASKS-v0.42-EXECUTION.md`
- commit: 4d7346fa91fa37c914c9d469573d3acc2ff4e6a4
- declaration acceptance: PASS. The first post-activation `cycle-check`
  resolves v0.42 from `AGENTS.md` alone and reports `state=open`, verified
  local tag references, declared scope and trigger freshness accepted, both
  artifact boundaries and State regions bound, and every prior cycle closed.
- governed-row acceptance: PASS. All **31/31** deferral subjects carry dated
  v0.42 observations measured before the declaration moved; all four
  trigger-bearing Architecture rows name v0.42, and no template survives.
- pre-activation contract correction: PASS. The delivered semantic
  `## Cycle closing record` template was renamed before its first commit so
  the open cycle cannot masquerade as closed. The pre-commit lifecycle result
  then contained only the two predicted uncommitted-runbook/activation-anchor
  defects, and the first committed run passes.
- grant acceptance: PASS. Neither Grant E nor Grant F was issued. No
  structural archive, protected-manifest byte, tag, branch, or remote ref
  moved; their dormant steps retain their exact not-granted branches.
- retention acceptance: PASS. The configured pattern derives exactly
  v0.41–v0.42. Exact activation commit `4d7346fa…` exports **2,647,307 bytes /
  157 tracked files / 2 retained cycles**, with all **157/157** required paths
  present, all four raw-wire bodies, both structural archives, and the one
  mixed-use manifest source absent. Against the latest prior governed value
  **2,657,685**, activation is **10,378 bytes lower**.
- governed review-export measurement: tree=`4d7346fa91fa37c914c9d469573d3acc2ff4e6a4`; bytes=`2647307`
- boundary acceptance: PASS. Exact activation is **77,919 bytes above** the
  2,569,388-byte attention boundary and leaves **352,693 bytes / 11.76% /
  1.64 high-water cycles** below the unchanged 3,000,000-byte ceiling. Grant
  E remains an unheld **84,896-byte** lever under the structured disposition.
- artifact acceptance: PASS. Activation State is **197,684 / 453,741 bytes**.
  Manifest schema v2 remains **3 artifacts / 339 pins** at **200,440 /
  1,048,576 bytes**; two complete checks took **0.10 s / 0.10 s real**.
- executable acceptance: PASS. R15 reports **0 differences / 6 routes / 112
  field occurrences**; `version-check` derives **3** offline pins, **22** floor
  restatements, **3** release restatements, and classifies **593** tracked
  files; the registered self-test passes **16/16 rules / 115 controls**.
- remote acceptance: PASS. Fresh executed readback kept
  `main=993813c755e9f759a4ee165954c7a1df984f6b10`, v0.17.7/v0.17.8 exact, and
  v0.17.6 plus historical v0.8.0/v0.10.2 absent. Local HEAD before activation
  was one record-only commit ahead; no contradiction or ref movement occurred.
- protected-input acceptance: PASS. The three historical amendment inputs
  remain untouched and untracked. No dependency, production source, protected
  byte, observation, fixture, publisher wire, entitlement/licensing outcome,
  local tag, or remote ref moved.
- stop conditions: none. All hypotheses used by activation were measured or
  explicitly left for E0; the one numerical refutation is State at **194,412**,
  not 194,411 bytes before the activation record.
- golden-E2E delta: **0**. The sandbox-denied bind was a non-result; the
  permission-capable identical command passed **11/11**.

### 2026-08-05 · E0 — entering-state reconstruction

- owner: Codex
- runbook: `TASKS-v0.42-EXECUTION.md`
- commit: c8cd3f0d40378a7ad0845a5e7762fb0ccc2f0feb
- hypothesis acceptance: PASS. H1, H2, H4, H5, H6, and H8 are confirmed.
  H3 is truthfully refuted by one byte: the audit-child State append is
  **1,520 bytes**, not 1,519, while its post-push section is exactly **1,396
  bytes**. H7 confirms the **84,896-byte** archival lever and refutes entering
  State as **194,412**, not 194,411 bytes. Every H1–H8 verdict is dated in the
  runbook.
- graph acceptance: PASS. Git object reads prove release parent `5bd8052…` →
  closing commit `993813c…` → entering audit child `827192d…`, each as an
  immediate child, and annotated object `4a47772…` peels to the closing
  commit.
- remote acceptance: PASS. Direct `ls-remote` reads exact main, direct and
  peeled v0.17.7/v0.17.8 refs, and no v0.17.6 ref. A detached checkout of
  exact published main proves it lacks v0.41's cycle-ending export-audit
  field while the entering audit child contains it. At entry, local HEAD was
  main's exact one-commit descendant; no remote ref moved.
- remote-witness enumeration: PASS. `run` and every `tools/*.py` contain zero
  `ls-remote` occurrences. The runbook partitions locally witnessed object,
  topology, record-shape, and freshness facts from unwitnessed remote main,
  tag, evidence-ref, publication-topology, published-content, and hosted-run
  binding assertions. No transcribed remote assertion is promoted to an
  executed control claim.
- export acceptance: PASS. Exact entering commit `827192d…` exports
  **2,675,890 bytes / 157 tracked entries / 2 retained cycles**, all tracked,
  **106,502 bytes above** the **2,569,388-byte** attention boundary, leaving
  **324,110 bytes / 10.80% / 1.51 high-water cycles** below the ceiling at
  the **215,306-byte** high-water denominator.
- status acceptance: PASS. Entering status was exactly the three retained
  untracked amendment inputs plus the then-untracked v0.42 runbook. After
  ACTIVATE committed the runbook, status returned to exactly the same three
  untouched amendment inputs.
- executable acceptance: PASS. Clean rebuilt Python 3.11.4 and 3.12.13
  environments resolve the same pinned **21-package** set. Full `ci-local`
  passes **22/22**; both complete shell populations pass **396/396** with the
  same named `on_site` identity and no skip; registered invariants and the
  standalone self-test pass **16/16 rules / 115 controls**; `cycle-check`
  passes; the v0.41 closing checklist derives **325 checked / 3 retracted /
  316 matched / 316 resolved / 9 exemptions**.
- protected-input acceptance: PASS. No dependency, production source,
  protected byte, observation, fixture, publisher wire,
  entitlement/licensing outcome, tag, or remote ref moved.
- stop conditions: none. The two one-byte source-export discrepancies are
  corrected measurements, not architectural, scope, or decision-gate
  failures.
- golden-E2E delta: **0**. Integrated and post-record standalone runs each
  passed **11/11**.

### 2026-08-05 · REMOTE-WITNESS — executed publication state

- owner: Codex
- runbook: `TASKS-v0.42-EXECUTION.md`
- commit: 393c8478f7421d64e6eeb61ff07f0fd34c72a417
- C28 acceptance: PASS. `cycle-check` parses one structured current-State
  authority, executes a bounded non-interactive `git ls-remote`, compares
  expected and absent refs, checks expected remote-main ancestry against local
  HEAD, and reads a named published progress blob for audit-content claims.
  Complete post-push records derive their direct and peeled tag expectations;
  permanently withheld and operative unpublished-local records derive tag
  absences. The decision falsifier—an inexpressible current assertion or a
  failing permission-capable offline full gate—was not observed.
- verdict acceptance: PASS. Normal transport reports
  `verdict=measured remote=origin refs=27 audits=1`
  with exact `main=993813c755e9f759a4ee165954c7a1df984f6b10`.
  Deliberately disabled transport reports the visible non-failing
  `verdict=unavailable remote=origin exit-128`. R17/1 proves a completed
  disagreeing reading is a fatal result rather than either of those states.
- offline satisfiability acceptance: PASS. The proof was executed before the
  control's implementation commit. `GIT_SSH_COMMAND=/usr/bin/false ./run
  ci-local` passes all **22/22** jobs with the unavailable verdict; normal
  `./run ci-local` passes the same **22/22** with the measured verdict.
- C29 acceptance: PASS. AGENTS R-CLOSE owns the v0.42-forward order while
  `ARCHITECTURE.md` §8 retains its existing pointer to those mechanics. A
  cycle's own published main object must contain its own export audit;
  historical pre-v0.42 cross-cycle shapes remain admitted. The decision
  falsifier—retroactive rejection of the historical shape—was refuted by its
  passing control.
- planted-control acceptance: PASS. Registered R17/1–R17/4 respectively
  execute mismatch rejection, offline unavailability, v0.42 audit-outside-tip
  rejection, and historical cross-cycle admission. Every fail-before mutation
  failed at its registered production control site and the assembled suite
  passes **17/17 rules / 119 controls**.
- integration acceptance: PASS. R17/1 first exposed and corrected a synthetic
  fixture-isolation defect. The first full offline gate then truthfully failed
  **17** legacy fixture cases that lacked the new v0.42-forward State block;
  the fixture contract and audit-before-post-push topology were corrected.
  Focused cycle-check tests pass **96/96**, and each complete Python 3.11
  population passes **397/397** with the named `on_site` identity and no skip.
- protected-input acceptance: PASS. A nonessential `run` help edit was caught
  by protected deferred-evidence re-derivation and reverted before adoption.
  `run` remains SHA-256
  `e436d59b05f060a8ce78dd3fb23282ad99fbc8bd263abd73224978c74afeeadb`
  at **50,378 bytes**; the manifest remains unchanged and all protected checks
  pass. The three retained amendment inputs remain untouched and untracked.
- scope acceptance: PASS. Only declared Step 2 files and the standing State and
  runbook records moved. No dependency, production source, protected byte,
  observation, fixture, publisher wire, entitlement/licensing outcome, public
  route, response field/type, serialized value domain, local tag, or remote ref
  moved.
- stop conditions: none. The published v0.41 audit lag is measured as the
  expected `absent` audit content at exact remote main, not a contradiction.
- golden-E2E delta: **0**. Both integrated full gates and the post-record
  standalone run passed **11/11**.

### 2026-08-05 · ARCHIVE — Grant E not granted

- owner: Codex
- runbook: `TASKS-v0.42-EXECUTION.md`
- commit: 1396420164538c9a1a9e27dc58e15fffa8c7a88d
- grant acceptance: PASS. Neither the initiating request nor any operator
  message through Step 3 contains Grant E's exact required authorization. The
  dated not-granted branch executed; no partial or inferred authority was used.
- unrecovered-quantity acceptance: PASS. Direct extraction from the first
  v0.38 record through the byte before the permanent-tail marker measures
  exactly **84,896 bytes**. The active disposition remains
  `kind=unheld-lever`, `lever=Grant E`, `recoverable_bytes=84896` and claims
  zero recovered bytes.
- archive acceptance: PASS. `docs/state-archive/` still contains only the four
  prior archives through v0.13, v0.21, v0.28, and v0.35; no v0.38 archive was
  created and no existing archived byte moved.
- manifest acceptance: PASS. `config/protected-artifacts.json` is unchanged at
  **200,440 bytes / 339 pins**, SHA-256
  `f59d4520cfaa0190954442856b6bb1ab5576049f16d5b8b816f00f64495fefae`.
  The pin delta is exactly zero and complete verification matches all **3/3**
  protected artifacts.
- State acceptance: PASS. The exact implementation commit carries State at
  **208,626 / 453,741 bytes**; `cycle-check` reports both artifact boundaries
  and the State structural/current-restatement contract bound and measures the
  remote witness agreeing.
- executable acceptance: PASS. Full `ci-local` passes **22/22**, including
  **17/17 rules / 119 controls**, Python 3.11 at **397/397**, and embedded
  golden **11/11**. The first attempt stopped before substantive tests because
  ARCHIVE was checked before a resolvable implementation/progress pair; the box
  was restored, acceptance was rerun in contract order, and the corrected full
  run passed.
- protected-input acceptance: PASS. The three retained amendment inputs remain
  untouched and untracked. No dependency, production source, protected byte,
  observation, fixture, publisher wire, entitlement/licensing outcome, public
  surface, local tag, or remote ref moved.
- stop conditions: none. The not-granted quantity agrees with the activation
  measurement and no boundary or architectural invariant moved.
- golden-E2E delta: **0**. Embedded and post-record standalone runs each passed
  **11/11**.

### 2026-08-05 · REPAIR-TIP — Grant F not granted

- owner: Codex
- runbook: `TASKS-v0.42-EXECUTION.md`
- commit: 73a69e3ef68be0780bdd061b7eb4d2eab2883ee0
- grant acceptance: PASS. Neither the initiating request nor any operator
  message through Step 4 contains Grant F's exact one-ref fast-forward
  authorization. The dated not-granted branch executed; no push was attempted.
- remote acceptance: PASS. The executed witness measures all **27** expected
  and absent refs in agreement and exact remote
  `main=993813c755e9f759a4ee165954c7a1df984f6b10`. Every direct and peeled tag
  identity is unchanged; v0.17.8 remains exact and v0.17.6 remains absent.
- topology acceptance: PASS. Exact audit child
  `827192d2b3ed56fbe04ac0df0cc6536ef037e066` has remote main as its immediate
  parent and changes only `STATE.md` and `docs/cycles/PROGRESS-v0.41.md`.
- published-gap acceptance: PASS. The published v0.41 progress blob contains
  zero cycle-ending export-audit fields while the audit child contains one.
  Published State lacks the five-field post-push records for both v0.17.7 and
  v0.17.8 while the child contains both. Those three record elements are
  exactly what the published reader still cannot see.
- lifecycle acceptance: PASS. `cycle-check` reports the remote witness
  `measured`, local tag reconciliation verified, State at **209,991 / 453,741
  bytes**, both artifact boundaries bound or disposed as recorded, and the
  active cycle open and consistent.
- protected-input acceptance: PASS. No tag, branch, evidence ref, or other
  remote ref moved. The three retained amendment inputs remain untouched and
  untracked; no dependency, production source, protected byte, publisher wire,
  entitlement/licensing outcome, or public surface moved.
- stop conditions: none. The observed state is the expected one-commit
  published lag and does not contradict the complete local record.
- golden-E2E delta: **0**. The required standalone run passed **11/11**.

### 2026-08-05 · RE-MEASURE — exact candidate passed 9/9

- owner: Codex
- runbook: `TASKS-v0.42-EXECUTION.md`
- commit: ab01368b9ca797c7e9968b9a0fa9f85027d9f59c
- condition/result: PASS. Operational checker and lifecycle changes fired the
  conditional hosted step against exact audited candidate
  `1076316a47271c16cd4260dfdfe231bca1dcb5cd`.
- preflight acceptance: PASS. The immutable historical attestation population
  passes **7/7** under every strict flag with required and observed GitHub CLI
  **2.96.0**; the deliberately wrong signer is rejected.
- candidate/ref acceptance: PASS. A temporary structured absent-ref
  expectation made Step 2's command-entry control read origin before the push:
  it returned `verdict=measured`, **28** refs, one audit ref, exact
  `main=993813c755e9f759a4ee165954c7a1df984f6b10`, and no
  `refs/heads/codex/v0.42-evidence-1076316`. The first proposed push was blocked
  locally before network execution pending explicit external-egress approval.
  After approval, one non-force remote push created exactly that ref at the
  candidate; no ref was reused, forced, or remotely retried.
- hosted-job acceptance: PASS. GitHub-hosted Ubuntu workflow-dispatch run
  **30966236435**, attempt **1**, targeted the exact SHA/ref and concluded
  `success`. All **9/9** workflow-derived blocking identities passed: core,
  golden, lint, offline MSRV, net MSRV 1.85 refusal, net MSRV 1.86 success, net,
  shell Python 3.11, and shell Python 3.12. Dependency drift was the sole
  report-only skip; the workflow was dispatched once and not retried.
- authenticated-evidence acceptance: PASS after one disclosed non-result. The
  run persisted **9** artifacts, each carrying one receipt and one Sigstore
  bundle. In a clean detached candidate worktree carrying the exact three
  ignored protected corpora, the first wrapper invocation produced no report
  and therefore established no result. The direct verifier entry point and a
  second complete `./run audit-deferred` wrapper invocation each accepted
  **9**, rejected **0**, verified every attestation, authenticated the exact
  repository, workflow, source digest, and source ref, and derived a complete
  single-run nine-identity matrix. Protected artifacts matched **3/3** before
  and after the passing wrapper run.
- population acceptance: PASS after one disclosed sandbox non-measurement. The
  first local Python 3.11 attempt failed **8** tests solely on denied loopback
  socket binds and denied `ps` process inspection and is not repository
  evidence. Permission-capable local Python 3.11.4 and 3.12.13 each collected
  and passed **397/397**, including the named `on_site` test. Each GitHub-hosted
  lane collected **397**, passed **396**, and skipped only
  `tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
  with its named protected-corpora/built-core reason and `on_site` marker. Both
  direct `tools/test_population.py` comparisons derive `equivalent=true`,
  `equivalent_passed=397`, and exactly one allowed hosted skip.
- remote acceptance: PASS. Final direct origin readback resolves exactly one
  v0.42 evidence ref at the candidate, keeps
  `main=993813c755e9f759a4ee165954c7a1df984f6b10`, and leaves every direct and
  peeled release tag identical to Step 4. The resulting `cycle-check` executes
  the structured expected ref and reports `verdict=measured`, **28** refs, one
  audit ref, exact main, and PASS. No publication ref moved.
- protected/scope acceptance: PASS. Only standing State and runbook records
  moved in the implementation commit. No dependency, production source,
  protected byte, observation, fixture, publisher wire, public response domain,
  entitlement/licensing outcome, accepted boundary, tag, `main`, or audit ref
  moved. The three retained amendment inputs remain untouched and untracked.
- stop conditions: none. The pre-existing evidence ref falsifier was not
  observed, the hosted matrix was complete, and every authenticated receipt
  agreed with the exact candidate and ref.
- golden-E2E delta: **0**. Hosted golden and the post-record standalone local
  run each passed **11/11**.

### 2026-08-05 · R-CLOSE — v0.17.9 unpublished-local tagged close

- owner: Codex
- runbook: `TASKS-v0.42-EXECUTION.md`
- commit: 5452355945d2717cbd84ea2224148dbd0f4c1ac7
- result: PASS at the assembled release-parent boundary. DR38 selects patch
  **v0.17.9** because the cycle changes assurance controls, lifecycle ordering,
  and governing records but no production runtime behavior, dependency,
  publisher configuration, protected byte, entitlement/licensing outcome,
  route, response field/type, or serialized `/v1/*` value-domain value.
- domain acceptance: PASS. Dependency-free R15 derivation and installed
  FastAPI comparison report **0 differences across 6 routes / 31 status-media
  variants / 112 field occurrences**. Neither minor-version clause fires.
- version acceptance: PASS after two disclosed command-shape corrections. The
  initial README restatement wrapped the required tag-target sentence and the
  initial runtime-manifest command omitted `--release`; neither produced an
  accepted result. Corrected `version-check` derives **0.17.9** from all five
  executable authorities, with **3** offline pins, **22** current floor
  restatements, and **3** current release restatements across **593** tracked
  files; corrected runtime comparison is exact.
- evidence acceptance: PASS. Exact pre-version evidence candidate
  `1076316a47271c16cd4260dfdfe231bca1dcb5cd` and hosted run **30966236435**,
  attempt 1, passed **9/9** blocking identities and persisted **9 receipts / 9
  Sigstore bundles**, accepted **9 / rejected 0** by the release-grade verifier.
  Exact version-only release parent
  `5452355945d2717cbd84ea2224148dbd0f4c1ac7` passed the full local gate
  **22/22**; Python 3.11 and 3.12 each passed **397/397** with the accepted
  warning nonfatal. Both hosted comparisons derive equivalent **397**-test
  populations from hosted **396 passed + 1** named, reasoned, `on_site` skip.
- governed review-export measurement: tree=`5452355945d2717cbd84ea2224148dbd0f4c1ac7`; bytes=`2710728`
- governed-export acceptance: PASS after one disclosed sandbox non-result. The
  first exact-parent export attempt failed before measurement on sandbox DNS.
  The permission-capable project-root entry point produced **157 derived / 157
  exported / 2,710,728 bytes / 2 retained cycles**, retaining v0.41–v0.42. It
  stands **141,340 bytes above** attention and leaves **289,272 bytes / 9.64% /
  1.34 high-water cycles** below the unchanged ceiling, missing the 2.5-cycle
  target by **248,993 bytes**. Relative to v0.41's governed value, the exact
  change is **+53,043 bytes**.
- recovery attribution: PASS. Grant E was not issued, contributes **0 bytes**,
  and leaves **84,896 bytes** unrecovered; spending it alone would leave a
  **56,444-byte** attention shortfall. No other capacity lever executed.
- artifact-boundary acceptance: PASS. Assembled State is **220484 / 453,741
  bytes**. The manifest remains **200,440 / 1,048,576 bytes**; the latest timed
  pair matched **3/3 artifacts / 339 pins** in **0.11 s / 0.10 s real**. Neither
  artifact boundary nor timing trigger fires.
- pre-tag control acceptance: PASS at the assembled worktree. Direct local
  v0.17.9 resolution returned absent; `cycle-check` reported
  `local-tag-reconciliation=pre-tag`,
  `tag-independent-assertions=verified`, and exact release parent
  `5452355945d2717cbd84ea2224148dbd0f4c1ac7` before any tag existed.
- post-tag control at the assembled worktree: not applicable. Local v0.17.9
  resolution is absent at this pre-tag boundary, so no post-tag PASS or tag
  object is claimed in the closing tree.
- deferral acceptance: PASS. All **31/31** active rows carry their latest dated
  v0.42 close observations. The archival and capacity rows name structured
  dispositions, each lever's contribution, and the exact remaining shortfall.
- invariant acceptance: PASS. The permission-capable exact release-parent gate
  passes **22/22**, the registered suite passes **17/17 rules / 119 controls**
  with **0** hand-typed absolute finding-line fields, both Rust floor pairs
  behave as specified, and all protected bytes match.
- divergence acceptance: PASS. Published v0.17.8 reset the epoch at exact
  remote main. The 14-commit distance to the release parent carries no measured
  runtime-behavior or public-surface difference, so no count starts and neither
  trigger fires.
- publication acceptance: PASS at the pre-tag boundary. Executed remote
  readback keeps `main=993813c755e9f759a4ee165954c7a1df984f6b10`, the v0.42
  evidence ref exact, published tags exact, and v0.17.6 plus both historical
  tags absent. Fresh direct local and remote v0.17.9 lookup returned absent. No
  publication, main movement, tag movement, deletion, or force operation
  occurred.
- checklist acceptance: PASS at the assembled closing worktree: **332 checked /
  3 retracted / 323 matched / 323 commits resolved / 9 exemptions**; v0.42 is
  nonempty at **7 checked / 7 matched / 7 resolved**.
- scope acceptance: PASS. Only declared release authorities and active
  State/runbook/progress/Architecture records move at R-CLOSE. No dependency
  graph, protected byte, fixture, observation, closed-cycle document, publisher
  request, workflow, or unauthorized remote ref moves.
- stop conditions: none. Disclosed sandbox failures were non-measurements whose
  permission-capable reruns passed; R15 is exact and no immutable record,
  accepted boundary, or publication ref was contradicted.
- golden-E2E delta: **0**. The release-parent full gate and standalone run, and
  the assembled closing-worktree standalone run, pass **11/11**.
- cycle-ending review-export audit: closing_tree=`0382622bbfaeaf7092830460d6432a2eb777b031`; bytes=`2730969`; audit_delta=`+20241`
