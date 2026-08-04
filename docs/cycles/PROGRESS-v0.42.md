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
