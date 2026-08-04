# PROGRESS-v0.39.md — append-only execution record

This file records v0.39 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

## Operator grant recorded before execution

The operator issued the dormant publication grant in the initiating request.
The grant text is recorded verbatim before the gated step runs:

> Please read agents.md and ARCHITECTURE.md first, then read the newly added file "docs/cycles/TASKS-v0.39-EXECUTION.md" and execute it strictly in accordance with the architectural design and constraints. Before the task begins, I will first authorize you to “PUBLISH-V17-5 — dormant, Grant C”

Under the exact scope defined by the runbook, the quoted label activates Grant
C's one non-force fast-forward of `origin/main` to the exact v0.38 audit child
and creation of annotated tag `v0.17.5` at the verified v0.38 closing commit.
It authorizes no other ref movement or later release publication.

### 2026-08-04 · ACTIVATE — v0.39 cycle activation

- owner: Codex
- runbook: `TASKS-v0.39-EXECUTION.md`
- commit: 752b2d56ac0e937f91035497225b352a55d3a472
- declaration acceptance: PASS. Direct post-activation `cycle-check` resolves
  v0.39 from the declaration and reports `state=open`, with local tag
  reconciliation, declared scope, trigger freshness, artifact boundaries,
  State regions, and every prior closed cycle accepted.
- governed-row acceptance: PASS. All **30/30** deferral subjects carry dated
  v0.39 observations; the four trigger-bearing Architecture rows also name
  v0.39. No template observation survives.
- author-contract correction: PASS before acceptance. The draft's literal
  `## Cycle closing record` template made the real lifecycle entry point reject
  an open cycle with seven unchecked boxes. The unpushed local activation
  commit was replaced with a non-semantic template heading; the next direct
  run passed, and no checker predicate was weakened.
- retention acceptance: PASS. The derived configuration advances from
  v0.37–v0.38 to exactly v0.38–v0.39. The staged project-root check passed at
  **2,774,259 bytes / 163 files / 2 retained cycles**; an exact detached
  activation-commit check passed at **2,730,852 bytes / 160 files / 2 retained
  cycles**. The **43,407-byte / 3-file** difference is the untouched untracked
  amendment-input population that E0 partitions and Step 3 resolves.
- governed review-export measurement: tree=`752b2d56ac0e937f91035497225b352a55d3a472`; bytes=`2730852`
- boundary acceptance: PASS. Exact activation leaves **269,148 bytes / 8.97% /
  2.51 cycles** under the unchanged 3,000,000-byte ceiling at the latest
  +107,226-byte checker-derived denominator. State is **130,819 / 453,741
  bytes** and the manifest is **200,440 / 1,048,576 bytes**.
- artifact acceptance: PASS. Complete checks match **3 artifacts / 339 pins**
  at **0.10 s / 0.11 s real**; neither manifest trigger clause fired.
- protected-input acceptance: PASS. The three historical amendment inputs
  remain byte-untouched and untracked. No dependency, production source,
  protected byte, observation, fixture, publisher wire, or remote ref moved.
- stop conditions: none. The draft-heading rejection was corrected inside
  ACTIVATE before semantic acceptance and did not trip a retained gate.
- golden-E2E delta: **0**. The sandbox-denied bind was a non-result; the
  permission-complete identical command passed **11/11**.

### 2026-08-04 · E0 — entering-state reconstruction

- owner: Codex
- runbook: `TASKS-v0.39-EXECUTION.md`
- commit: 45228b88371d5fecba8206863c5f75e85f53336e
- hypothesis acceptance: PASS. Every H1–H9 row carries a dated confirmed,
  partly-confirmed, or refuted verdict from its named entry point. H1/H2's
  object and remote graph, H3's record population, H7's raw-body partition,
  and H9's denominator are confirmed; H4's checklist, H5's delivered export,
  and H8's source-byte figures are corrected rather than copied.
- full-partition acceptance: PASS by complete set arithmetic, not sampling.
  The **163** export entries partition as **160 Git-tracked + 3 existing
  untracked + 0 synthetic**. The three non-Git entries are named individually
  in the runbook and total **43,127 raw bytes**; the partition sum is exact.
- review-export acceptance: PASS. The delivered worktree export is **2,778,858
  bytes / 163 entries / 2 retained cycles** and retains exactly v0.38–v0.39.
  The four `.gitattributes`-classified raw bodies partition into two absent
  configured RSS exclusions and two present v0.38 bodies. The dropped v0.37
  pair is **75,859 bytes** and the raw recoverable population is **211,800
  bytes**; Step 3 owns the separately measured framing delta.
- graph/publication acceptance: PASS. The local v0.17.5 release/closing/tag/
  audit objects match exactly; remote `main` remains exact v0.17.4 and an
  ancestor; v0.17.2–v0.17.4 are exact remotely; v0.17.5 is absent. Grant C's
  preconditions are deliberately remeasured again immediately before push.
- boundary acceptance: PASS. State is **132,770 / 453,741 bytes** and the
  manifest is **200,440 / 1,048,576 bytes** at **3 artifacts / 339 pins**.
  The checker-derived denominator is confirmed at **+107,226 bytes/cycle**.
- checklist/control acceptance: PASS. Direct populations are **15 rules / 84
  controls / 9 exemptions / 3 retractions**; the live checklist is **303
  checked / 3 retracted / 294 matched / 294 resolved / 9 exemptions**.
- full-gate acceptance: PASS. Permission-complete `ci-local` passes all
  **22/22** jobs, including Python 3.11 **373/373**, both Rust floor pairs,
  warning/lint/format gates, artifact verification, and golden **11/11**. A
  separate Python 3.12 run passes the identical **373/373** population.
- protected-input acceptance: PASS. The three amendment inputs remain
  byte-untouched and untracked. No dependency, production source, protected
  byte, fixture, observation, publisher wire, entitlement/licensing outcome,
  golden input, or unauthorized ref moved.
- stop conditions: none.
- golden-E2E delta: **0** at **11/11**.

### 2026-08-04 · PUBLISH-V17-5 — Grant C spent exactly

- owner: Codex
- runbook: `TASKS-v0.39-EXECUTION.md`
- commit: 56e9141bda468c6eec4161cb8965840fb531bfb6
- grant acceptance: PASS. The initiating request's verbatim named Grant C is
  recorded above before the action; it supplied authority only for the two
  runbook-defined non-force ref movements and is now spent.
- precondition acceptance: PASS immediately before push. Remote `main` was
  exact `a7d6c80e7e5ccd963e8ebb46ee054b30af88abb0`; both direct and peeled
  v0.17.5 refs were absent; that remote head was an ancestor of exact audit
  child `dd605acc037da405fa6b2b5366b09349c330c194`; and local annotated object
  `946bdc015446182727d8f705697e378f8fe8f7eb` peeled to exact closing commit
  `55045ae481ce8d1ef285522b3c0a57c91fe5cb54`.
- publication acceptance: PASS. One non-force branch push advanced only
  `origin/main` to the audit child; one non-force tag push created only
  v0.17.5. Fresh readback matched the branch, annotated object, and peeled
  target exactly. No ref was forced, deleted, or moved beyond Grant C.
- hosted acceptance: PASS. Push-triggered run **30868419182**, attempt **1**,
  concluded `success` on exact head `dd605acc…`. All **9/9** blocking job
  identities passed: core, clippy+fmt, live-fetch 1.85 refusal, golden E2E,
  live-fetch 1.86 success, offline 1.78, live-fetch path, Python 3.11, and
  Python 3.12. Dependency drift was the sole report-only skip.
- lifecycle acceptance: PASS. The current header states that v0.17.5 is
  published and Grant C is spent; the exact five-field post-push record is at
  column zero; the historical unpublished-local observation remains untouched.
  Direct `cycle-check` passes on the published path and reconciles the local
  annotated tag exactly.
- planted-control acceptance: PASS unmodified at **15/15 rules / 84
  controls**, including the missing-record refusal for a published descendant.
  R15 remains exact at **6 routes / 112 field occurrences** with no public
  response-domain difference.
- divergence acceptance: PASS. Exact v0.17.5 publication resets the
  publication epoch to **0** at closing commit `55045ae481ce8d1ef285522b3c0a57c91fe5cb54`;
  the v0.38 runtime difference is included in that published commit, and this
  step adds no runtime or public-surface change.
- protected-input acceptance: PASS. The three historical amendment inputs
  remain byte-untouched and untracked. No dependency, production source,
  protected byte, observation, fixture, publisher wire, entitlement/licensing
  outcome, or golden input moved.
- stop conditions: none. Every Grant C precondition and the post-push hosted
  gate passed.
- golden-E2E delta: **0** at **11/11**.
