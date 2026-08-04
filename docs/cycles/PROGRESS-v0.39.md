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

### 2026-08-04 · EXPORT-TRUTH — review export images the checked tree

- owner: Codex
- runbook: `TASKS-v0.39-EXECUTION.md`
- commit: cdb281c2500ce0044e2ca26cd38e7333e6dfeeb1
- C15 acceptance: PASS. One bounded Repomix family exclusion,
  `docs/cycles/AMENDMENT-{r4,v0.36}-*.md`, excludes the three shared historical
  amendment families without a per-file list, leaves Git status visible, and
  does not cover future amendment families. The three files remain untracked,
  byte-untouched, and unstaged at **43,127 bytes** total.
- C16 acceptance: PASS against the real pin population. The existing Git
  `binary` byte-preservation attribute intersected with manifest-pinned
  observations derives exactly **4** raw-wire bodies. Configured exact
  observation exclusions equal that nonempty set in both directions; the
  v0.25 RSS and v0.38 privacy, robots, and RSS bodies are absent, while the
  small unmarked v0.25 robots policy remains a review source.
- tracked-tree acceptance: PASS. The checker contains no hand-maintained
  required-path, excluded-filename, excluded-prefix, source-root, or
  cycle-specific literal list. All **158/158** derived required paths are
  present; every one of the **158** exported entries is Git-tracked; no
  untracked defect, derived raw-wire body, or either manifest-derived
  structural archive is present.
- exact implementation export: tree=`cdb281c2500ce0044e2ca26cd38e7333e6dfeeb1`;
  bytes=`2675532`; entries=`158`; retained_cycles=`2`; remaining=`324468`.
- declared-scope acceptance: PASS. Every active clean pattern matched at least
  one of **587 tracked + 3 untracked** repository candidates. The exact
  annotated vacuous predecessor is rejected at the registered syntax control
  site and the corrected `docs/cycles/**` pattern passes.
- planted-control acceptance: PASS. R12 passes **47/47** reconstructible
  mutations, including untracked export entry, empty raw class, missing class
  exclusion, configured nonmember, and vacuous annotated pattern. The complete
  registered population passes **15/15 rules / 89 controls**; the focused
  export/cycle regression population passes **98/98**.
- full-gate acceptance: PASS. Permission-complete `ci-local` passes all
  **22/22** jobs, including Python 3.11 **377/377**, both Rust floor pairs,
  warning/lint/format gates, protected artifacts, and golden **11/11**. The
  separate Python 3.12 lane passes the identical **377/377** population with
  the same one accepted non-fatal Starlette warning.
- governing-record acceptance: PASS. `AGENTS.md`, `ARCHITECTURE.md`, and
  `STATE.md` state the derived tracked-tree/raw-wire/structural-archive
  contract; direct `cycle-check`, response-domain derivation, manifest
  validation, version restatement, and whitespace checks pass. The unchanged
  governed activation figure remains progress-backed while the open-cycle
  implementation measurement is reported separately.
- protected-input acceptance: PASS. No dependency, production source,
  protected byte, observation, fixture, publisher wire, entitlement/licensing
  outcome, golden input, or remote ref moved.
- stop conditions: none. The export remains below the unchanged 3,000,000-byte
  ceiling; Step 4 owns the separately declared pre-failure boundary correction.
- golden-E2E delta: **0** at **11/11**, confirmed both inside `ci-local` and by
  the required standalone `./run golden` entry point.

### 2026-08-04 · CEILING-TRIGGER — attention before export failure

- owner: Codex
- runbook: `TASKS-v0.39-EXECUTION.md`
- commit: 23d3b73f83a7eae4b650e13c3195735237911fa0
- C17 acceptance: PASS. The stated principle reserves two cycles at the latest
  positive adjacent governed-growth denominator. The executable derivation is
  `3,000,000 - (2 × 107,226) = 2,785,548 bytes`, strictly inside the unchanged
  3,000,000-byte ceiling.
- falsifier acceptance: PASS. The checker refuses no positive adjacent pair, a
  non-positive denominator, a reserve outside the ceiling, a written boundary
  that disagrees with the formula, or a denominator that disagrees with the
  already-checked governed series; it does not select a fallback value.
- crossing acceptance: PASS. `export-check` applies `>=` to generated bytes and
  requires a valid date plus a non-`none` `trigger-fired disposition:` in the
  governed Architecture row. `cycle-check` binds the same denominator and
  applies the same rule to the governed recorded value. The identical planted
  boundary construction fails without the disposition and passes with it.
- exact implementation export: tree=`23d3b73f83a7eae4b650e13c3195735237911fa0`;
  bytes=`2692723`; entries=`158`; retained_cycles=`2`;
  attention_boundary=`2785548`; attention_gap=`92825`;
  attention_state=`clear`.
- criterion-correction acceptance: PASS. The active deferral trigger now fires
  at or above the two-governed-growth-cycle attention boundary because the
  former ceiling-only wording announced the condition only after failure. The
  `Second STATE.md archival` trigger text is byte-unchanged and inherits the
  sharpened export trigger. The ceiling value itself remains **3,000,000**.
- planted-control acceptance: PASS. R12 passes **48/48** mutations, including
  the new real crossing guard, and the complete population passes **15/15
  rules / 90 controls**. Focused export/cycle tests pass **101/101**.
- full-gate acceptance: PASS. Permission-complete `ci-local` passes all
  **22/22** jobs, including Python 3.11 **380/380**, both Rust floor pairs,
  lint/format/warning gates, protected artifacts, and golden **11/11**. The
  separate Python 3.12 lane passes the identical **380/380** population.
- governing-record acceptance: PASS. The derived principle, exact predicate,
  criterion correction, unchanged ceiling, dated non-fired observation, and
  falsifier are recorded in `AGENTS.md`, `ARCHITECTURE.md`, `STATE.md`, and the
  active deferral row. Direct cycle, domain-manifest, artifact-manifest,
  whitespace, and review-export checks pass.
- protected-input acceptance: PASS. The three historical amendment inputs
  remain untracked and byte-untouched. No dependency, production source,
  protected byte, observation, fixture, publisher wire, entitlement/licensing
  outcome, golden input, or remote ref moved.
- stop conditions: none. The measured implementation remains **92,825 bytes**
  below the attention boundary, so no disposition or archival decision fired.
- golden-E2E delta: **0** at **11/11**, confirmed both inside `ci-local` and by
  the required standalone `./run golden` entry point.

### 2026-08-04 · WIRE-CONTRACT — bounded SEC egress registered

- owner: Codex
- runbook: `TASKS-v0.39-EXECUTION.md`
- commit: 06b2dd48f9bd3e3ae466392ca9c3309d4184d862
- C18 acceptance: PASS. `ARCHITECTURE.md` owns the invariant boundary a later
  publisher widening must preserve and `AGENTS.md` restates it at the operator
  entry point. New R16 is the honest registry home because the subject is one
  shell command/helper call chain rather than R8 crawler-identity construction
  or R12 release lifecycle.
- executable-guarantee acceptance: PASS. Ten reconstructible controls follow
  `./run harvest-sec` into `cmd_harvest_sec`, the artifact verifier, protected
  target helper, default/fresh path helpers, and exact finance-source config.
  They prove preflight before network-capable work, manifest-protected target
  refusal before bind and its failure return, required contact before bind,
  exactly one configured SEC request/result, fresh non-existing default path,
  `first_window` with all fetched documents new and an SEC-only archive, and no
  observation/fixture publisher-response input.
- handoff finding: strict fresh-path-only admission outran the executable for
  one case. An explicit unprotected `CORE_DB` override is admitted before the
  request without an absence-or-empty check. The governing claim is therefore
  limited to the no-override fresh default plus success-result freshness; Step
  5 did not change `run` to manufacture the broader claim.
- planted-control acceptance: PASS. R16 passes **10/10** mutations and the
  complete registered population passes **16/16 rules / 100 controls**. All
  expected finding lines are derived from unchanged text in each constructed
  mutant; there are **0** hand-typed absolute finding-line fields. Focused
  anti-vacuity, harvest-harness, and config tests pass **5/5**.
- exact implementation export: tree=`06b2dd48f9bd3e3ae466392ca9c3309d4184d862`;
  bytes=`2716611`; entries=`158`; retained_cycles=`2`;
  attention_boundary=`2785548`; attention_gap=`68937`;
  attention_state=`clear`.
- full-gate acceptance: PASS. Permission-complete `ci-local` passes all
  **22/22** jobs, including Python 3.11 **381/381**, both Rust floor pairs,
  lint/format/warning gates, protected artifacts, and embedded golden
  **11/11**. The separate Python 3.12 lane passes the identical **381/381**
  population with the same accepted non-fatal Starlette warning.
- governing-record acceptance: PASS. The claims name the actual executables
  and control numbers, the explicit-override limit is a finding rather than an
  invariant, affected deferral observations are fresh, and direct cycle,
  whitespace, review-export, and registered checks pass.
- protected-input acceptance: PASS. The three historical amendment inputs
  remain untracked at their exact **43,127** bytes and prior hashes. No
  dependency, production or operational source, protected byte, observation,
  fixture, publisher wire, entitlement/licensing outcome, golden input, or
  remote ref moved.
- stop conditions: none. The exact implementation export remains **68,937
  bytes** below the attention boundary, and State remains below its artifact
  boundary.
- golden-E2E delta: **0** at **11/11**, confirmed both inside `ci-local` and by
  the required final standalone `./run golden` entry point.

### 2026-08-04 · RE-MEASURE — exact candidate passed 9/9

- owner: Codex
- runbook: `TASKS-v0.39-EXECUTION.md`
- commit: 89d2753c8a5e035e20d867484c66c88fe69bfd79
- condition/result: PASS. Checker and governing-contract files moved, so the
  conditional hosted step ran against exact audited candidate
  `fa846095b7387bcf9e832d558dc8a70a6d29813b`.
- candidate/ref acceptance: PASS. Immediately before ref creation, the full
  remote snapshot kept `main` at
  `dd605acc037da405fa6b2b5366b09349c330c194` and every annotated/peeled tag
  through v0.17.5 at its recorded identity. `git ls-remote --exit-code`
  returned **2** with no output for fresh
  `refs/heads/codex/v0.39-evidence-fa84609`. One non-force push created exactly
  that ref at the candidate; no ref was reused, retried, forced, or moved.
- hosted-job acceptance: PASS. Workflow-dispatch run **30875346351**, attempt
  **1**, targeted the exact SHA/ref and concluded `success`. All **9/9**
  workflow-derived blocking identities passed; dependency drift was the sole
  report-only skip. The workflow was dispatched once and was not retried.
- authenticated-evidence acceptance: PASS. The run persisted **9** artifacts,
  each containing one receipt JSON and one Sigstore bundle. The repository's
  release-grade verifier accepted **9**, rejected **0**, verified all **9**
  bundles against the exact repository, workflow, source digest, and source
  ref, and derived a complete nine-identity matrix.
- population acceptance: PASS. Each hosted shell lane collected **381**,
  passed **380**, and skipped only named
  `tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
  with its declared protected-corpora/built-core reason and `on_site` marker.
  Both direct `tools/test_population.py` comparisons derive
  `equivalent=true`, `equivalent_passed=381`, and one allowed hosted skip.
- machine acceptance: PASS. The exact candidate's prior permission-complete
  local gate passed **22/22** identities with Python 3.11 **381/381**, scan
  **16/16 rules / 100 controls**, both Rust floor pairs, all protected
  artifacts, and golden **11/11**; its separate local Python 3.12 lane passed
  the identical **381/381** population. Hosted golden passed **11/11**, and
  both explicit net-floor jobs passed on their pinned effective toolchains.
- remote acceptance: PASS. Final `ls-remote` resolves the evidence ref to the
  exact candidate, keeps `main` at `dd605acc…`, and keeps every tag identity
  byte-for-byte at the pre-push snapshot. No publication ref moved; Grant C
  remains spent.
- exact implementation export: tree=`89d2753c8a5e035e20d867484c66c88fe69bfd79`;
  bytes=`2722638`; entries=`158`; retained_cycles=`2`;
  attention_boundary=`2785548`; attention_gap=`62910`;
  attention_state=`clear`.
- post-record local acceptance: PASS. Active-cycle and artifact-boundary
  checks pass with State **148,195 / 453,741 bytes** and manifest **200,440 /
  1,048,576 bytes**. The complete planted scan passes **16/16 rules / 100
  controls**, whitespace is clean, and the standalone permission-complete
  golden run passes **11/11**. Initial sandboxed export and golden attempts
  were non-measurements because npm DNS and loopback bind were denied; the
  required permission-capable reruns passed.
- protected-input acceptance: PASS. The three historical amendment inputs
  remain untracked and byte-untouched at exact **43,127** total bytes and their
  prior hashes. No workflow, dependency, production source, protected byte,
  observation, fixture, publisher wire, entitlement/licensing outcome,
  serialized response domain, or golden input moved.
- stop conditions: none. The hosted run passed, the evidence ref was fresh,
  and final remote readback shows no main or tag movement.
- golden-E2E delta: **0**. Hosted and final standalone local golden each passed
  **11/11**.

### 2026-08-04 · R-CLOSE — v0.17.6 tagged local close

- owner: Codex
- runbook: `TASKS-v0.39-EXECUTION.md`
- commit: acfa801102197ce2d94adaa5a14a3ad102893549
- result: PASS. DR20 selects patch **v0.17.6** because review-export truth,
  pre-failure attention, and bounded-egress controls change review and
  assurance behavior but no production runtime behavior, dependency,
  publisher configuration, protected byte, entitlement/licensing outcome, or
  serialized public response contract. The untagged release parent is the
  closing record's immediate parent; the annotated tag is created locally only
  after the closing tree exists.
- domain acceptance: PASS. Both the dependency-free derivation and installed
  FastAPI comparison report **0 differences** from the v0.17.4 baseline across
  **6 routes / 31 status-media response variants / 112 recursive field
  occurrences**. DR20's public-value-domain minor clause does not fire.
- version acceptance: PASS. `version-check` derives **0.17.6** from all five
  executable authorities, with **3** offline-MSRV pins at raw 1.78.0, **22**
  current offline-MSRV restatements at 1.78, and **3** current release
  restatements at 0.17.6. All **587** tracked files are classified and Cargo
  changes only cored's lockfile package value.
- evidence-anchor acceptance: PASS. Exact candidate
  `fa846095b7387bcf9e832d558dc8a70a6d29813b`, run `30875346351` attempt 1,
  passed **9/9** blocking identities and persisted **9 receipts / 9 Sigstore
  bundles** accepted by the release-grade verifier. Both local release-parent
  populations pass **381/381**; both hosted comparisons derive equivalent
  **381**-test populations with one named, reasoned, `on_site` skip; hosted and
  local golden pass **11/11**.
- governed review-export measurement: tree=`acfa801102197ce2d94adaa5a14a3ad102893549`; bytes=`2729600`
- governed-export acceptance: PASS. The exact release parent produced **158
  required / 158 tracked / 158 exported / 2,729,600 bytes**, retained exactly
  v0.38–v0.39, and excluded the exact four manifest-derived raw publisher
  response bodies, both structural archives, and the bounded historical
  untracked-input family. At the latest +107,226-byte adjacent-cycle
  denominator, **270,400 bytes / 9.01% / 2.52 cycles** remain below the fixed
  ceiling. This clears the 2.5-cycle target by **2,335 bytes** and remains
  **55,948 bytes** below the attention boundary. The final assembled closing
  tree exports **2,740,695 bytes**, leaving **259,305 bytes / 8.64% / 2.42
  cycles** and missing the 2.5-cycle target by exactly **8,760 bytes**, while
  remaining **44,853 bytes** below attention. The immediate audit child binds
  this later closing-tree measurement without superseding the governed field.
- artifact-boundary acceptance: PASS. Release-parent State is **149,239 /
  453,741 bytes**. The manifest remains **200,440 / 1,048,576 bytes** and two
  complete verifications each took **0.09 s real**. Neither governed artifact,
  timing, nor review-export attention trigger fires.
- deferral acceptance: PASS. Every active row carries its latest dated v0.39
  close observation. The version-literal trigger is discharged under declared
  release-authority precedence; DR20 discharges classification; the immediate
  audit child discharges the required closing-tree disclosure.
- invariant acceptance: PASS. The release-parent full gate passes **16/16
  rules / 100 controls** with **0** hand-typed absolute finding-line fields.
  The Step 1A publication-lifecycle controls remain unmodified and are
  re-executed on the mixed published/unpublished-local state after tagging.
- divergence acceptance: PASS. Published v0.17.5 reset the epoch count to
  **0**. v0.39 has no measured runtime-behavior difference or public-surface
  movement, so the count remains **0** and neither trigger fires. The local
  unpublished close does not reset the epoch.
- publication acceptance: PASS at DR21's boundary. Fresh direct pre-close
  readback found no local or remote v0.17.6 tag and kept remote `main` exact at
  `dd605acc037da405fa6b2b5366b09349c330c194`. Grant C is spent. No push,
  `main` movement, or v0.17.6 publication occurred. The local annotated tag
  targets only the closing commit after it exists; the immediate audit child
  owns the exact closing-tree export field before handoff.
- checklist acceptance: PASS at the assembled closing worktree: **310 checked
  / 3 retracted / 301 matched / 301 commits resolved / 9 exemptions**; v0.39
  is nonempty at **8 checked / 8 matched / 8 resolved**.
- full local acceptance: PASS **22/22** jobs at the exact release parent.
  Python 3.11 and 3.12 each pass **381/381** with the accepted warning, Rust
  1.78 and net 1.86 pass, net 1.85 produces the required locked-ICU refusal,
  all protected bytes match, and embedded golden passes **11/11**. The final
  audit child re-executes the full gate over the delivered head.
- golden-E2E delta: **0**. The release-parent embedded and standalone pipeline
  pass **11/11**; the assembled closing-worktree standalone run and final
  audit-child embedded run are reported at their executable points.
- scope acceptance: PASS. Only declared release authorities and active
  State/runbook/progress/Architecture records move. No dependency graph,
  protected byte, fixture, historical observation, closed-cycle document,
  publisher request, workflow, `main`, or remote release ref moves.
- stop conditions: none. The exact release parent clears the stated headroom
  target, no decision gate fired, and no publication beyond spent Grant C was
  attempted.
