# STATE.md — intel-platform handoff

**As of:** 2026-08-05 · **Version:** v0.17.9 (core-shell) · **Status:** **v0.17.9 is closed locally and unpublished; v0.17.7 and v0.17.8 are published, v0.17.6 remains permanently withheld and local-only, and v0.17.5 remains published exactly.** Untagged release commit `5452355945d2717cbd84ea2224148dbd0f4c1ac7` carries the v0.17.9 authorities and is the immediate parent of the assembled closing tree. Historical v0.17.8 parent `5bd805214cb72ed694c83e9eec1ce6d17396a69e` precedes closing commit `993813c755e9f759a4ee165954c7a1df984f6b10`; published annotated object `4a477722df218059097ff648a07379ec5683dd08` peels to that closing tree, which is exact remote `main`. Historical v0.17.7 parent `b8fe1c2c1c2c842868a70581dee390939ef68595` precedes closing commit `cd4fd58b39c855cc769d3696a6b389f735066022`; published annotated object `2287b41558e69bb86490df71b6907a2f0eb73310` peels to that tree. Withheld v0.17.6 parent `acfa801102197ce2d94adaa5a14a3ad102893549` precedes closing commit `7c9305f01219412048ec75236f2bf1e61112c178`; local annotated object `66ee2cbbe374b99722bec49b8176571777aaa899` peels to that tree and remains local-only. Historical v0.17.5 parent `37f552c0c326098bdcf8f19de7eac19670d74680` precedes closing commit `55045ae481ce8d1ef285522b3c0a57c91fe5cb54`; audit child `dd605acc037da405fa6b2b5366b09349c330c194` is preserved in published history. Published v0.17.5 annotated object `946bdc015446182727d8f705697e378f8fe8f7eb` peels to that closing tree. Push-triggered hosted run `30927918916`, attempt **1**, concluded `success` on exact published closing commit `993813c755e9f759a4ee165954c7a1df984f6b10` and passed all **9/9** blocking identities; dependency drift was the sole report-only skip. Exact v0.40 evidence candidate `52a5c44b060a795894aa120fb8cd0b1ab0d5cf09` passed hosted run `30896642221`, attempt **1**, at **9/9** blocking identities with **9/9** release-grade attestations accepted. Final exact v0.41 evidence candidate `5bd805214cb72ed694c83e9eec1ce6d17396a69e` passed hosted run `30925977431`, attempt **1**, at **9/9** blocking identities with **9/9** release-grade attestations accepted. v0.40 and v0.41 change lifecycle/review tooling, executable controls, and governing records; neither changes production runtime behavior, dependency, publisher configuration, protected byte, entitlement/licensing outcome, route, response field/type, or serialized `/v1/*` value-domain value. Exact v0.42 evidence candidate `1076316a47271c16cd4260dfdfe231bca1dcb5cd` passed hosted run `30966236435`, attempt **1**, at **9/9** blocking identities with **9/9** release-grade attestations accepted. The exact v0.17.9 release-parent worktree passed the full local gate **22/22**; its Python 3.11 and 3.12 populations each pass **397/397**. Both repository-computed hosted comparisons derive **397** equivalent tests from local **397/397** and hosted **396 passed + 1** named, reasoned, `on_site` skip. The current registered suite passes **17/17 rules / 119 controls** with **0** hand-typed absolute finding-line fields; the response-domain manifest remains release-baselined at v0.17.4 and exact at v0.17.9, and golden passes **11/11**. The exact v0.17.8 release-parent gate passed **22/22** local identities; exact release-parent Python 3.11 and 3.12 populations each passed **396/396** with one named `on_site` identity, and their repository-computed hosted comparisons each derived **396** equivalent tests from local **396/396** and hosted **395 passed + 1** named, reasoned, `on_site` skip. The accepted warning trigger did not fire and the retraction count remains **3**. Publication of v0.17.8 resets the published-release-divergence count to **0** at closing commit `993813c755e9f759a4ee165954c7a1df984f6b10`; v0.40, v0.41, and v0.42 carry no measured runtime-behavior difference or public-surface movement.

## Remote witness expectations

- **Remote witness remote:** `origin`
- **Remote witness expected ref:** `refs/heads/main` = `993813c755e9f759a4ee165954c7a1df984f6b10`
- **Remote witness expected ref:** `refs/heads/codex/v0.36-evidence-f50db67` = `f50db6744df726434db7f5aeffa1a08bbbf521fc`
- **Remote witness expected ref:** `refs/heads/codex/v0.37-evidence-2e5921f` = `2e5921f0d0d3f4d64bde56b95325216d33caa59b`
- **Remote witness expected ref:** `refs/heads/codex/v0.37-evidence-99012c8` = `99012c86dcdda8ea32f1b1afa016f793118e9087`
- **Remote witness expected ref:** `refs/heads/codex/v0.38-evidence-816a064` = `816a0648c0dd9f4be1caad01ed3395997671cf25`
- **Remote witness expected ref:** `refs/heads/codex/v0.39-evidence-fa84609` = `fa846095b7387bcf9e832d558dc8a70a6d29813b`
- **Remote witness expected ref:** `refs/heads/codex/v0.40-evidence-52a5c44` = `52a5c44b060a795894aa120fb8cd0b1ab0d5cf09`
- **Remote witness expected ref:** `refs/heads/codex/v0.41-evidence-4405882` = `44058820d25834d2b89d54cda48ed723a3dfa77f`
- **Remote witness expected ref:** `refs/heads/codex/v0.41-evidence-5bd8052` = `5bd805214cb72ed694c83e9eec1ce6d17396a69e`
- **Remote witness expected ref:** `refs/heads/codex/v0.42-evidence-1076316` = `1076316a47271c16cd4260dfdfe231bca1dcb5cd`
- **Remote witness absent ref:** `refs/tags/v0.8.0`
- **Remote witness absent ref:** `refs/tags/v0.8.0^{}`
- **Remote witness absent ref:** `refs/tags/v0.10.2`
- **Remote witness absent ref:** `refs/tags/v0.10.2^{}`
- **Remote witness main relation:** `ancestor-of-head`
- **Remote witness published audit:** `v0.41` = `absent`

**v0.43 E0 — entering state reconstructed (measured 2026-08-05).** H1–H6
and H8 are confirmed by repository commands. H7 is partly confirmed and partly
refuted by one byte: the v0.38-to-permanent-tail lever is exactly **84,896
bytes**, while actual entering `STATE.md` is **221,818 / 453,741 bytes**, not
221,817. The lower number is the Repomix content payload after the terminal
newline; the repository file byte count governs the artifact boundary.

The local graph is exact: annotated object
`a7852c55deba9b509c0235dfba38e2a0426c2501` peels to closing commit
`0382622bbfaeaf7092830460d6432a2eb777b031`, whose immediate parent is release
parent `5452355945d2717cbd84ea2224148dbd0f4c1ac7`; entering audit child
`6f07edf84c3ce40f1ef4c9e97e5d101242490243` immediately follows the closing
commit. Permission-capable direct remote readback returns exact
`main=993813c755e9f759a4ee165954c7a1df984f6b10`, exact v0.17.7/v0.17.8 direct
and peeled tags, and no v0.17.6, v0.17.9, v0.8.0, or v0.10.2 tag. The exact
entering distance is **16 first-parent commits**, spanning v0.41's audit child
through v0.42's. A detached annotated-v0.17.9 checkout passes the real
`cycle-check` as a closed v0.42 tree with its governed export bound.

The exact entering export passes at **2,732,434 bytes / 157 tracked entries /
2 retained cycles**, **163,046 bytes above** attention with **267,566 bytes /
8.92% / 1.24 high-water cycles** to the ceiling. Its retained cycle documents
total **178,284 bytes / 6.52%**. Exact comparison with the prior delivered
**2,675,890-byte** export places the new v0.42 runbook first at **+63,834
bytes**, followed by State **+27,406**, v0.42 progress **+24,831**, and the
cycle checker **+13,157**. Both carried deferral sections have **31** subjects
and measure exactly **11,124** and **11,294 bytes**. Source tracing confirms the
prior-runbook carry-forward comparison reads worktree files; export retention
does not supply those bytes to the checker.

The permission-capable full local matrix passes **22/22**. It includes
`cycle-check` with R17's measured **30-ref / 1-audit** witness, the registered
self-test at **17/17 rules / 119 controls**, default and net Rust tests with
zero warnings, Rust 1.78 success, net Rust 1.86 success and 1.85 refusal,
clippy, formatting, artifact integrity, Python 3.11 at **397/397**, and embedded
golden **11/11**. The separately rebuilt Python 3.12 population passes
**397/397** with the same accepted non-fatal warning. Checklist audit passes at
**333 checked / 3 retracted / 324 matched / 324 resolved / 9 exemptions**,
including v0.42 at **7/7/7**. The entering status was exactly the three retained
untracked amendment inputs plus the then-untracked v0.43 runbook; current status
has only those same three untouched amendments. No dependency, production
source, protected byte, observation, fixture, publisher wire, entitlement or
licensing outcome, tag, branch, or remote ref moved, and no E0 gate or stop
condition fired.

**v0.43 ACTIVATE — canonical-ledger and document-boundary cycle declared
(measured 2026-08-05).** The activation worktree moves the declaration to
v0.43, creates its append-only progress record, and advances the one derived
depth-two review-retention pattern from v0.41–v0.42 to v0.42–v0.43. All
**31/31** carried deferral rows were populated with dated v0.43 measurements
before the declaration moved; the four trigger-bearing Architecture rows now
name the same cycle. The delivered semantic closing-record heading was renamed
to the established non-semantic assembly template before first commit so the
open cycle cannot masquerade as closed.

Permission-capable R17 readback measured remote
`main=993813c755e9f759a4ee165954c7a1df984f6b10` with every structured expected
and absent ref in agreement. Entering HEAD
`6f07edf84c3ce40f1ef4c9e97e5d101242490243` is its **16-commit** descendant;
no ref moved. Dependency-free R15 remains exact at **0 differences / 6 routes /
112 field occurrences**. `version-check` derives **3** offline pins, **22**
current floor restatements, **3** release restatements, and **593** tracked
files. The registered scan passes **17/17 rules / 119 controls**. Permission-
capable Python 3.11 and Python 3.12 populations each pass **397/397** with the
accepted warning non-fatal. The initial sandboxed populations are disclosed
non-measurements because denied loopback binds and process inspection produced
their failures.

Before this record, State measures **221,818 / 453,741 bytes**. The protected
manifest remains **200,440 / 1,048,576 bytes** at **3 artifacts / 339 pins**;
two complete verifications took **0.10 s / 0.10 s real**. Neither artifact
trigger fired. The permission-capable project-root export check passes at
**2,691,054 bytes / 157 tracked files / 2 retained cycles**, retaining exactly
v0.42–v0.43 with all required paths present and all derived exclusions absent.
It stands **121,666 bytes above** the 2,569,388-byte attention boundary and
leaves **308,946 bytes / 10.30% / 1.43 high-water cycles** below the unchanged
ceiling, a **19,674-byte decrease** from v0.42's governed figure. Grants E, G, and H were
not issued; no dormant branch executes. The entering untracked population is
exactly the three protected amendment inputs plus the v0.43 runbook; none was
edited except the runbook being activated. No dependency, production source,
protected byte, observation, fixture, publisher wire, entitlement/licensing
outcome, tag, branch, or remote ref moved, and no stop condition fired.

**v0.42 R-CLOSE — v0.17.9 assembled close (measured 2026-08-05).** DR34
separates the cycle-ending export audit from the later post-push record, and
DR35's same-cycle publication order now lives only in AGENTS R-CLOSE while
ARCHITECTURE §8 delegates to it. DR36's author-side lifecycle gap and 52%
archival projection error remain recorded. DR37 leaves the operator-selected
3,000,000-byte ceiling and two-cycle retention depth unchanged. DR38 selects
patch **v0.17.9** from dependency-free and installed R15 results of **0
differences across 6 routes / 31 status-media variants / 112 recursive field
occurrences**. DR39 keeps this close unpublished-local because neither dormant
grant authorizes v0.42 publication.

Exact release parent `5452355945d2717cbd84ea2224148dbd0f4c1ac7`
carries all five executable authorities at 0.17.9. `version-check` reports
**3** executable offline pins, **22** current floor restatements, **3** release
restatements, and **593** tracked files. Its permission-capable full local gate
passes **22/22**; Python 3.11 and 3.12 each pass **397/397**, invariant self-test
passes **17/17 rules / 119 controls** with **0** hand-typed absolute finding-line
fields, both Rust floor pairs behave as specified, all protected bytes match,
and embedded plus standalone golden pass **11/11** with delta zero. Exact
pre-version candidate `1076316a47271c16cd4260dfdfe231bca1dcb5cd` and hosted
run **30966236435**, attempt **1**, pass **9/9** blocking identities; its nine
receipt/bundle pairs are accepted **9 / rejected 0** under the pinned GitHub
CLI **2.96.0** and exact repository, workflow, source digest, and source ref.
The assembled pre-tag `cycle-check` passes with local v0.17.9 absent,
`local-tag-reconciliation=pre-tag`, `tag-independent-assertions=verified`, and
the exact release parent above; this closing tree contains no tag-object field.

The exact release-parent project-root export passes at **2,710,728 bytes / 157
tracked entries / 2 retained cycles**. It is **141,340 bytes above** the
2,569,388-byte attention boundary and leaves **289,272 bytes / 9.64% / 1.34
high-water cycles** below the unchanged ceiling, missing the 2.5-cycle target by
**248,993 bytes**. The exact governed change from v0.41 is **+53,043 bytes**.
Grant E was not issued, contributes **0 bytes**, and leaves its **84,896-byte**
lever unspent; applied alone it would leave a **56,444-byte** attention
shortfall. Assembled State is **220484 / 453,741 bytes**. The protected manifest
is **200,440 / 1,048,576 bytes**, and the latest complete verification pair
matches **3/3 artifacts / 339 pins** in **0.11 s / 0.10 s real**.

C28 placed the remote witness at `cycle-check`: it reads the structured current
expectations when transport is available, fails on disagreement, and reports a
visible non-failing `unavailable` verdict without transport. It now executes
current assertions for remote main, every declared evidence ref, published tag
objects and peels, absent v0.17.6 and historical tags, v0.41's missing published
audit, and main's relationship to HEAD. Historical statements about intermediate
ref states and past push mechanics cannot be reconstructed from today's ref
advertisement and remain dated command evidence; no current declared ref identity
is unwitnessed when transport is available. C29 chose AGENTS as the single
mechanics authority, with planted same-cycle-fail and historical-cross-cycle-pass
controls. C30 measured the authorized boundary at **84,896 bytes** but remained
dormant because Grant E was not issued. C31 admitted the remote/lifecycle
controls E0 surfaced. None of their stated falsifiers appeared.

Grant F was also not issued. Executed readback therefore keeps remote
`main=993813c755e9f759a4ee165954c7a1df984f6b10`, one commit short of v0.41's
complete local record, and keeps the v0.42 evidence ref exact without moving a
publication ref. A published reader still cannot see v0.41's cycle-ending export
audit or its two post-push records; the new witness makes that lag executable and
visible. The independently approved evidence-ref action created only the one
immutable candidate ref. All **31/31** deferral rows carry their latest v0.42
close observations, the publication-epoch count remains **0**, and no stop
condition fired. The initial sandbox DNS/export failure and sandbox-only Python
failures are disclosed non-measurements; their permission-capable reruns passed.

The v0.43 findings are bounded. Attention now fires for four consecutive closed
cycles. Grant E alone still misses by **56,444 bytes**. The v0.41 published-record
gap remains, though it is now an executed disagreement between published and
local completeness rather than an invisible transcription. The first
`audit-deferred` wrapper invocation produced no report before the direct verifier
and second wrapper invocation passed, which is a tool-path behavior worth
reproducing. No runtime, public-surface, dependency, evidence-integrity,
publisher-wire, or immutable-record contradiction emerged.

The overdue operator capacity question is numeric: this exact export is
**141,340 bytes above** attention with **1.34 high-water cycles** to the ceiling.
Ceiling movement alone must add at least **141,341 bytes**, to **3,141,341**;
after the unissued Grant E it must add at least **56,445 bytes**, to
**3,056,445**. The other ask-first levers are reducing retention to one cycle,
structurally archiving an as-yet-unmeasured eligible subset of the **83,771-byte**
`CHANGELOG.md`, or redefining review source. The retained v0.41 task/progress
pair is **89,621 raw bytes**, not an asserted export recovery. The open decision
for v0.43 is which bounded combination, if any, the operator authorizes.

**v0.42 closing-export audit and unpublished-local observation (measured
2026-08-05).** Local annotated v0.17.9 object
`a7852c55deba9b509c0235dfba38e2a0426c2501` peels to closing commit
`0382622bbfaeaf7092830460d6432a2eb777b031`, whose immediate parent is exact
v0.17.9 release parent `5452355945d2717cbd84ea2224148dbd0f4c1ac7`.
The project-root export of that exact closing commit passes at **2,730,969
bytes / 157 exported files / 2 retained cycles**, a truthful **+20,241-byte**
difference from the release parent's 2,710,728-byte governed field. This
immediate audit child records the measured closing-tree delta and does not
predict its own content-addressed identity.

After the local tag was created, direct origin lookup for the direct and peeled
v0.17.9 refs exited successfully with empty output. Executed remote witnessing
also kept `main=993813c755e9f759a4ee165954c7a1df984f6b10`, every published tag and
evidence ref exact, and the v0.41 published-audit absence visible. No release
tag or main push was authorized or attempted, and no post-push result is
claimed.

- **Publication observation date:** 2026-08-05
- **Publication observation release:** `v0.17.9`
- **Publication observation status:** `unpublished-local-close`
- **Publication observation remote:** `origin`
- **Publication observation tag ref:** `absent`

**v0.42 R-CLOSE release-parent preparation (measured 2026-08-05).** DR38
selects patch **v0.17.9**. Dependency-free R15 derivation and the installed
FastAPI runtime comparison report **0 differences across 6 routes / 31
status-media response variants / 112 recursive field occurrences**. Remote
witnessing, same-cycle audit ordering, and their planted lifecycle controls
change assurance behavior only: no production runtime behavior, dependency,
publisher configuration, protected byte, entitlement/licensing outcome,
public route, response field/type, or serialized `/v1/*` value-domain value
moved. Neither minor-version clause fires.

All five executable release authorities and all three registered current
restatements identify **0.17.9**; Cargo changes only cored's package version in
the lockfile. Exact evidence candidate
`1076316a47271c16cd4260dfdfe231bca1dcb5cd` and GitHub-hosted run
**30966236435**, attempt **1**, pass all **9/9** blocking identities with
**9/9** release-grade attestations accepted. Fresh local and remote reads found
no direct or peeled v0.17.9 tag. DR39 selects an unpublished-local close: no
operator grant authorizes publishing v0.17.9 or moving remote `main` to a v0.42
object, and release-parent preparation moved no ref.

**v0.42 RE-MEASURE — exact candidate passed authenticated hosted verification
(measured 2026-08-05).** The operational checker and lifecycle changes fired
the conditional hosted step. Before any ref creation, `attestation-preflight`
accepted the immutable historical **7/7** population under every strict flag
with required and observed GitHub CLI **2.96.0**, and its deliberately wrong
signer was rejected. A temporary structured absent-ref expectation made the
new Step 2 control read origin at the command entry point: it returned
`verdict=measured`, **28** refs, one audit ref, exact
`main=993813c755e9f759a4ee165954c7a1df984f6b10`, and no
`refs/heads/codex/v0.42-evidence-1076316`. The first proposed push was blocked
locally before network execution pending explicit external-egress approval.
After that approval, one non-force remote push created exactly that ref at
candidate `1076316a47271c16cd4260dfdfe231bca1dcb5cd`; no ref was reused,
forced, or remotely retried.

GitHub-hosted Ubuntu workflow-dispatch run **30966236435**, attempt **1**,
targeted that exact ref and SHA and concluded `success`. All **9/9**
workflow-derived blocking identities passed: core, golden, lint, offline MSRV,
net MSRV 1.85 refusal, net MSRV 1.86 success, net, shell Python 3.11, and shell
Python 3.12. Dependency drift was the sole report-only skip. The run persisted
**9** artifacts, each with one runner receipt and one Sigstore bundle. In a
clean detached candidate worktree carrying the exact three ignored protected
corpora, the release-grade verifier accepted **9**, rejected **0**, verified
every attestation, bound the exact repository, workflow, source digest, and
source ref, and derived the complete single-run nine-identity matrix. The first
wrapper invocation produced no report and therefore established no result;
the direct verifier entry point and a second complete `./run audit-deferred`
wrapper invocation each produced the authenticated passing report while
protected artifacts matched **3/3** before and after.

On this MacBook, permission-capable Python 3.11.4 and 3.12.13 each collected
and passed **397/397**, including the named `on_site` test. The first sandboxed
Python 3.11 attempt is a disclosed non-measurement: its eight failures were
solely denied loopback binds and denied `ps` inspection. Each GitHub-hosted
lane collected **397**, passed **396**, and skipped only
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
with its named protected-corpora/built-core reason and `on_site` marker. Both
direct `tools/test_population.py` comparisons derive `equivalent=true`,
`equivalent_passed=397`, and exactly one allowed hosted skip. Final direct
origin readback keeps `main` exact, resolves the one new evidence ref to the
candidate, and leaves every direct and peeled release tag identical to the
Step 4 reading; no publication ref moved.

**v0.42 REPAIR-TIP — Grant F not granted; the published v0.41 record remains
one commit short (measured 2026-08-05).** The initiating request and every
operator message through this step were checked against Grant F's exact
fast-forward authorization. No such authorization was issued. The dormant push
branch therefore did not execute; this is a dated not-granted observation, not
an inferred refusal.

The executed witness freshly measures all **27** expected and absent refs in
agreement and keeps remote `main` at exact v0.41 closing commit
`993813c755e9f759a4ee165954c7a1df984f6b10`. Exact audit child
`827192d2b3ed56fbe04ac0df0cc6536ef037e066` has that closing commit as its
immediate parent and changes only `STATE.md` and
`docs/cycles/PROGRESS-v0.41.md`. The published progress blob contains no
`cycle-ending review-export audit`; the child contains exactly one. The
published State blob lacks the five-field post-push records for both v0.17.7
and v0.17.8; the child contains both. Those are exactly the complete-record
bytes a reader of published history still cannot see.

No branch, tag, direct or peeled tag identity, evidence ref, or other remote ref
moved. In particular, v0.17.8 remains exact and v0.17.6 remains absent. The
measured state is the expected published lag and does not contradict the local
record, so no Step 4 stop condition fired.

**v0.42 ARCHIVE — Grant E not granted; second archival remains dormant
(measured 2026-08-05).** The initiating request and every operator message
through this step were checked against Grant E's exact required content. No
such authorization was issued. This is the runbook's dated not-granted branch,
not an inferred refusal and not partial authority.

C30 therefore does not move a byte. A direct byte measurement from the first
v0.38 record through the byte before the permanent-tail marker returns exactly
**84,896 unrecovered bytes**. `docs/state-archive/` still contains only the four
previously admitted archives through v0.13, v0.21, v0.28, and v0.35; no v0.38
archive exists. `config/protected-artifacts.json` remains exact at **200,440
bytes / 339 pins**, SHA-256
`f59d4520cfaa0190954442856b6bb1ab5576049f16d5b8b816f00f64495fefae`,
and complete artifact verification matches all **3/3** protected artifacts.
State measured **206,895 / 453,741 bytes** before this observation and its
structural regions and current-restatement contract pass. The active deferral
remains `kind=unheld-lever`, `lever=Grant E`,
`recoverable_bytes=84896`; it claims neither recovery nor a new structural pin.
The first full `ci-local` attempt stopped at checklist audit before substantive
tests because ARCHIVE had been checked before its implementation commit and
progress entry existed. The box was restored to unchecked and the contract
sequence corrected. The resulting exact worktree passes the full gate
**22/22**, including **17/17 rules / 119 controls**, Python 3.11 at
**397/397**, and embedded golden **11/11**. State is **208,626 / 453,741
bytes** with its structural and semantic contracts bound. No Step 3 stop
condition fired.

**v0.42 REMOTE-WITNESS — published state is now executed (measured
2026-08-05).** C28 places the control at `cycle-check`, the lifecycle entry
point that already owns local publication reconciliation. Its structured
authority is the current State block immediately above: explicit expected and
absent refs, one named remote, the required main-to-local-HEAD ancestry
relation, and published cycle-audit expectations. Complete post-push records
derive their direct and peeled release-tag expectations automatically;
permanently withheld and unpublished-local records derive their tag absences.
The command executes one bounded, non-interactive `git ls-remote`, compares the
reading to those authorities, checks remote main's local ancestry, and reads
the named progress blob at the expected main object when an audit-content
assertion is present.

The result has three non-interchangeable states. A successful agreeing read is
`measured`; a timeout, transport refusal, process failure, malformed response,
or unavailable local object is visibly `unavailable` and non-failing; an
executed contradictory ref, ancestry, or published-audit reading is
`disagreeing` and fails `cycle-check`. With normal transport the real gate
reports `verdict=measured`, **27 refs**, **1 audit**, and exact remote
`main=993813c755e9f759a4ee165954c7a1df984f6b10`. With
`GIT_SSH_COMMAND=/usr/bin/false`, the identical gate reports
`verdict=unavailable remote=origin exit-128` and passes. C28's falsifier would
have been either a current remote assertion that the structured authority could
not express or a permission-capable transport-denied full gate that failed;
the exhaustive H4 set is expressible and the offline full gate passes.

C29 follows the existing pointer discipline. `ARCHITECTURE.md` §8 continues to
delegate tag and publication mechanics to AGENTS R-CLOSE; it does not duplicate
the ordering. AGENTS R-CLOSE now specifies the prospective v0.42 same-cycle
shape: release parent → closing commit and tag → immediate audit child carrying
the cycle-ending export audit → authorized atomic publication of main at that
audit child and the tag at the closing commit → later post-push verification
child. The executable property is deliberately narrower than that prose: every
v0.42-forward published cycle's expected main object must contain its own export
audit. Historical pre-v0.42 cross-cycle publication remains admitted. C29's
falsifier would have been an unavoidable rejection of the historical shape;
the backward control passes.

Registered R17 anchors all four required planted controls at production control
sites. R17/1 rejects a transcribed remote mismatch, R17/2 executes the offline
`unavailable` pass, R17/3 rejects a v0.42 audit outside the published tip, and
R17/4 admits the historical cross-cycle shape. The assembled self-test passes
**17/17 rules / 119 controls**. Its first R17/1 construction exposed a fixture-
isolation defect because a later synthetic ancestry check could still fail; the
fixture was narrowed to a no-relation case and all four controls then passed.
The first full offline `ci-local` correctly exposed **17** cycle-check fixture
failures because v0.42-forward synthetic States lacked the new authority block.
Those States now carry the contract, and the publication fixture now commits the
audit child before the post-push child; focused cycle-check tests pass **96/96**.

A nonessential attempt to mention the witness in `run` help moved its protected
byte and was caught by deferred-evidence re-derivation. That attempt was
reverted; `run` is again exact at SHA-256
`e436d59b05f060a8ce78dd3fb23282ad99fbc8bd263abd73224978c74afeeadb`,
**50,378 bytes**, and the protected manifest passes unchanged. The final full
offline and online `ci-local` executions each pass **22/22** jobs. Each Python
3.11 population passes **397/397** with the same named `on_site` identity and
no skip; golden passes **11/11** with zero delta. The only lane difference is
the intended witness verdict: visible unavailable versus measured agreement.
No dependency, production source, protected byte, publisher wire, local tag,
remote ref, entitlement/licensing outcome, public route, response field/type,
or serialized value domain moved. No Step 2 stop condition fired.

**v0.42 E0 — entering state reconstructed (measured 2026-08-05).** All
eight source-export hypotheses were executed rather than copied forward. H1,
H2, H4, H5, H6, and H8 are confirmed. H3 is refuted by one byte: the exact
audit-child State append is **1,520 bytes**, not 1,519; its post-push section
is exactly **1,396 bytes**, and the same commit contains v0.41's cycle-ending
export-audit field. H7 is partly confirmed and partly refuted: the v0.38-to-
permanent-tail lever is exactly **84,896 bytes**, while entering State is
**194,412 / 453,741 bytes**, not 194,411.

The local graph is exact: release parent `5bd805214cb72ed694c83e9eec1ce6d17396a69e`
is the immediate parent of closing commit `993813c755e9f759a4ee165954c7a1df984f6b10`,
whose immediate child is entering audit commit
`827192d2b3ed56fbe04ac0df0cc6536ef037e066`; annotated object
`4a477722df218059097ff648a07379ec5683dd08` peels to the closing commit.
Fresh direct remote readback returns main at that closing commit, exact v0.17.7
and v0.17.8 annotated and peeled refs, and no v0.17.6 ref. At entry, HEAD was
main's exact one-commit descendant. ACTIVATE has since added its required local
implementation and audit commits; no remote ref moved.

A detached checkout of exact published main proves that it lacks v0.41's
cycle-ending export-audit field while the entering audit child contains it.
The entering-tree export passes at **2,675,890 bytes / 157 tracked entries / 2
retained cycles**, **106,502 bytes above** the **2,569,388-byte** attention
boundary, leaving **324,110 bytes / 10.80% / 1.51 high-water cycles** below the
ceiling at the **215,306-byte** denominator.

H4's exhaustive partition found no executed remote witness. `run` and every
`tools/*.py` file contain zero `ls-remote` occurrences. Existing controls
execute local annotated-object type, peel, parent/tree, ancestry, header,
post-push-record shape, local object/target freshness, and nonzero hosted-run
fields. They do not refresh remote main identity, release-tag presence or
absence, direct or peeled tag identity, evidence-ref absence or identity,
publication topology, the published tip's export-audit content, or the binding
between a recorded remote ref and a hosted conclusion. A non-force push guards
only its mutation attempt; an unpublished-local record explicitly admits that
offline Git cannot refresh remote absence. Step 1's manual remote read and
detached checkout measured those facts but do not turn them into a standing
control.

The entering status population was exactly the three retained untracked
amendment inputs plus the then-untracked v0.42 runbook. After ACTIVATE committed
the runbook, status again contains exactly those three amendment inputs. Fresh
clean environments resolve **21 pinned packages** byte-identically on Python
3.11.4 and 3.12.13. Full `ci-local` passes **22/22**; both complete Python
populations pass **396/396** with the same named `on_site` identity and no
skip; registered invariants pass **16/16 rules / 115 controls**; the v0.41
closing checklist derives **325 checked / 3 retracted / 316 matched / 316
resolved / 9 exemptions**; golden passes **11/11** with delta zero. No E0 gate,
architectural invariant, protected-byte constraint, or stop condition fired.

**v0.42 ACTIVATE — published-state control cycle declared (measured
2026-08-05).** The activation worktree moves the declaration to v0.42,
creates the append-only progress record, and advances the single derived
review-retention pattern from v0.40–v0.41 to exactly v0.41–v0.42. All
**31/31** deferral rows were populated from dated v0.42 measurements before
the declaration moved; the four trigger-bearing Architecture rows now name
the same cycle. No observation template survives.

The delivered draft's semantic `## Cycle closing record` heading made the
untracked open runbook look closed to the real lifecycle entry point. It was
renamed to a non-semantic assembly template before activation, matching the
established correction. With the runbook staged but not yet committed,
`cycle-check` reports only the two predicted inability-to-resolve the first
committed runbook and activation-anchor facts; every semantic, scope,
retention, trigger, artifact, and publication check is otherwise clean.

The pre-activation export check truthfully failed on the untracked v0.42
draft and its position outside v0.41 retention. After staging the derived
v0.41–v0.42 set, the pre-record activation candidate passes at **2,643,992
bytes / 157 tracked files / 2 retained cycles**, with all **157/157** required
paths present, all four raw-wire bodies, both structural archives, and the one
mixed-use manifest source absent. It stands **74,604 bytes above** the
2,569,388-byte attention boundary and leaves **356,008 bytes / 11.87% / 1.65
high-water cycles** below the unchanged 3,000,000-byte ceiling. Grant E was
not issued; its exact v0.38-to-permanent-tail lever remeasures at **84,896
bytes** and remains unheld.

Fresh read-only remote measurement confirms `main=993813c755e9f759a4ee165954c7a1df984f6b10`,
v0.17.7 and v0.17.8 exact, and v0.17.6 plus historical v0.8.0/v0.10.2 absent.
Local HEAD `827192d2b3ed56fbe04ac0df0cc6536ef037e066` is the closing commit's
immediate child and differs from published main only in `STATE.md` and
`docs/cycles/PROGRESS-v0.41.md`. The local progress blob contains v0.41's
cycle-ending export-audit field while the published blob does not. This
confirms a published lag, not a contradiction, and no ref moved.

Before this record, State is **194,412 / 453,741 bytes** and the protected
manifest is **200,440 / 1,048,576 bytes**. Two complete artifact checks match
**3/3 artifacts / 339 pins** in **0.10 s / 0.10 s real**. The registered
self-test passes **16/16 rules / 115 controls**, R15 remains exact at **0
differences / 6 routes / 112 field occurrences**, and version authorities
remain **0.17.8**. No dependency, production source, protected byte,
observation, fixture, publisher wire, entitlement/licensing outcome, local
tag, or remote ref moved; neither Grant E nor Grant F was issued.

The first golden attempt was a sandbox-denied loopback-bind non-result. The
permission-capable identical command passes **11/11** with delta zero.

Including this record and the fully populated runbook, the staged activation
candidate exports **2,647,307 bytes / 157 tracked files / 2 retained cycles**,
stands **77,919 bytes above** attention, and leaves **352,693 bytes / 11.76% /
1.64 high-water cycles** below the unchanged ceiling.

**v0.41 post-push publication audit (measured 2026-08-04).** One authorized,
atomic, non-force push moved remote `main` to exact closing commit
`993813c755e9f759a4ee165954c7a1df984f6b10`, published v0.17.7 and v0.17.8,
and left permanently withheld v0.17.6 absent remotely. Direct readback found
v0.17.7 annotated object `2287b41558e69bb86490df71b6907a2f0eb73310`
peeling to `cd4fd58b39c855cc769d3696a6b389f735066022` and v0.17.8 annotated
object `4a477722df218059097ff648a07379ec5683dd08` peeling to exact remote
`main`. Push-triggered hosted run **30927918916**, attempt **1**, concluded
`success` on that exact v0.17.8 closing commit with all **9/9** blocking
identities passed; dependency drift was the sole report-only skip. The
successful publication resets the divergence epoch to **0** at the published
v0.17.8 closing commit.

- **Post-push verification date:** 2026-08-04
- **Post-push release:** `v0.17.7`
- **Post-push annotated tag object:** `2287b41558e69bb86490df71b6907a2f0eb73310`
- **Post-push closing commit:** `cd4fd58b39c855cc769d3696a6b389f735066022`
- **Post-push hosted run:** `30927918916`

- **Post-push verification date:** 2026-08-04
- **Post-push release:** `v0.17.8`
- **Post-push annotated tag object:** `4a477722df218059097ff648a07379ec5683dd08`
- **Post-push closing commit:** `993813c755e9f759a4ee165954c7a1df984f6b10`
- **Post-push hosted run:** `30927918916`

**v0.41 R-CLOSE — v0.17.8 assembled close (measured 2026-08-04).** DR32
selects patch **v0.17.8**. R15 derives **0 differences across 6 routes / 31
status-media response variants / 112 recursive field occurrences**, so neither
the named-surface nor serialized-value-domain minor clause fires. Exact parent
`5bd805214cb72ed694c83e9eec1ce6d17396a69e` carries all five executable
authorities and all three registered release restatements at 0.17.8; Cargo
changes only cored's package version in the lockfile.

Initial evidence candidate `44058820d25834d2b89d54cda48ed723a3dfa77f`
and hosted run **30917725112** passed before the assembled full self-test found
that R12/53 still hard-coded v0.40's governed export value and therefore no
longer mutated the live row. Final release parent
`5bd805214cb72ed694c83e9eec1ce6d17396a69e` derives both planted values from
the one live governed row. Fresh immutable ref
`refs/heads/codex/v0.41-evidence-5bd8052` and hosted run **30925977431**,
attempt **1**, pass all **9/9** blocking identities and **9/9** release-grade
attestations; the earlier refs remain unchanged. The final release-parent full
local gate passes **22/22**; Python 3.11 and 3.12 each pass **396/396**, the
registered suite passes **16/16 rules / 115 controls** with **0** hand-typed
absolute finding-line fields, both Rust floor pairs behave as specified, every
protected byte matches, and embedded plus standalone golden pass **11/11**
with delta zero.

The exact release-parent export passes at **2,657,685 bytes / 157 tracked
entries / 2 retained cycles**. It recovers **146,241 bytes** from the entering
tree, all through REVIEW-SOURCE; Grant E was not issued, contributed **0
bytes**, and leaves its **84,896-byte** lever unspent. The export remains
**88,297 bytes above** the 2,569,388-byte attention boundary and leaves
**342,315 bytes / 11.41% / 1.59 high-water cycles** below the unchanged
3,000,000-byte ceiling. It misses the 2.5-cycle target by **195,950 bytes**.
The substantive disposition records the measured change; the separate State-
archival row truthfully names the unheld lever.

State measures **192892 / 453,741 bytes** at the assembled worktree. The
manifest remains **200,440 / 1,048,576 bytes** with all **339** pins unchanged;
two consecutive complete checks take **0.15 s / 0.10 s real**. All **31/31**
deferral rows carry dated v0.41 close observations. Publication-epoch count is
still **0** before publication because neither v0.17.7 nor v0.41 adds a measured
runtime-behavior difference or public-surface movement.

Fresh pre-close inspection found no local v0.17.8 tag and no remote v0.17.6,
v0.17.7, or v0.17.8 tag. Remote `main` remained
`dd605acc037da405fa6b2b5366b09349c330c194`; the exact v0.40/v0.41 evidence
refs were unchanged and no publication ref had moved. At this assembled
worktree, `cycle-check` reports `local-tag-reconciliation=pre-tag` and
`tag-independent-assertions=verified` against release parent
`5bd805214cb72ed694c83e9eec1ce6d17396a69e`. No post-tag PASS or annotated-tag
object is claimed in this tree.

**v0.41 R-CLOSE release-parent preparation (measured 2026-08-04).** DR32
selects patch **v0.17.8**. The dependency-free R15 derivation and installed
FastAPI runtime comparison report **0 differences across 6 routes / 31
status-media response variants / 112 recursive field occurrences**. Review
projection, trigger reachability, and disposition substance change assurance
behavior only: no production runtime behavior, dependency, publisher
configuration, protected byte, entitlement/licensing outcome, public route,
response field/type, or serialized `/v1/*` value-domain value moved. Neither
minor-version clause fired.

All five executable release authorities and all three current restatements
identify **0.17.8**; Cargo changes only cored's package version in the lockfile.
The initiating operator authorization covers publication of `main`, v0.17.7,
and v0.17.8; it does not cover v0.17.6 or issue Grant E. Fresh local and remote
reads found no v0.17.8 tag, remote `main` remained exact at
`dd605acc037da405fa6b2b5366b09349c330c194`, and neither v0.17.6 nor v0.17.7
existed remotely. The two standing evidence refs are the only v0.40/v0.41
remote mutations; no publication ref moved during release-parent preparation.
State measures **189669 / 453,741 bytes** after this preparation record.

**v0.41 E0 — entering state reconstructed (measured 2026-08-04).** Every
runbook hypothesis now has a dated verdict from repository commands. The exact
entering object graph and remote/local tag topology are confirmed, and a fresh
detached v0.17.7 tag checkout passes lifecycle reconciliation. Remote `main`
remains `dd605acc…`; v0.17.2–v0.17.5 remain present and v0.17.6/v0.17.7 absent.
The expected entering untracked set was exactly the three protected amendment
inputs plus the then-uncommitted v0.41 runbook; after activation, only the same
three untouched amendment inputs remain untracked.

Exact entering export is confirmed at **2,803,926 bytes / 158 tracked entries**,
with **234,538 bytes** above attention and **196,074 bytes / 0.91 high-water
cycles** below failure. The manifest is **200,440**, not 200,439 bytes; its pin
array payload is 194,173 bytes, while the keyed pin field is the hypothesized
**194,191** bytes, and exactly **9/339** pins intersect the export. Initial
State was **172,660 / 453,741 bytes**, leaving **281,081**, not 281,082 bytes.
The v0.38/v0.37/v0.36 suffix hypotheses are each one byte low at **128,860 /
105,647 / 81,842**; their actually movable regions ending before the permanent
tail are **84,896 / 61,683 / 37,878** bytes.

The named “export ceiling trigger” does not exist. The live predicate is the
attention boundary, and a direct call at its real entry point returned no error
for the dated disposition `aware`, proving the substance gap rather than merely
reading it. Direct derivation confirms **16/16 rules / 108 controls**, **9**
exemptions, **3** retractions, and the v0.40 closing checklist at **317 / 3 /
308 / 308 / 9**, with v0.40 at **7/7/7**. Full `./run ci-local` passes **22/22**;
fresh Python 3.11 and separately rebuilt Python 3.12 environments each pass
**391/391** with the same named on-site identity; standalone invariant self-test
passes **16/16 / 108**, and standalone golden passes **11/11** with delta zero.
No E0 decision gate or stop condition fired, and no repository state other than
the required governing records moved.

**v0.41 Step 2 — archival trigger reaches the real predicate (measured
2026-08-04).** The pinned State-archival row now names **the review-export
attention predicate**, not the nonexistent “export ceiling trigger.” Its text
is derived from a registry of named predicates, and the actual lifecycle entry
point rejects a governed artifact spec naming an undefined predicate. With the
governed export at **2,789,050** and the attention boundary at **2,569,388**,
`cycle-check` evaluates attention as fired while State remains below its
**453,741-byte** boundary; a row without a dated trigger-fired disposition is
therefore rejected. Grant E remains unissued, so the truthful disposition names
the measured **84,896-byte** unexecuted lever rather than claiming recovery.

Both new R12 constructions are non-vacuous: the undefined-predicate fixture
fails at the predicate-registry control site, and the attention-fired/unfired-row
fixture fails at the predicate-evaluation site. The threshold truth table at
**2,569,387 / 2,569,388 / 2,569,389** is **false / true / true** for both the
review-export predicate and the archival export clause, proving no export state
was widened. The State byte-boundary clause and both accepted ceilings remain
unchanged.

The focused lifecycle population passes **96/96** after replacing the retired
trigger text in its shared positive fixture and two exact-string negative
constructions. The permission-complete local matrix then passes **22/22** jobs,
including Python 3.11 at **391/391**, all Rust floor/lint lanes, protected
artifacts, embedded golden, and the append-only audit gate. Standalone golden
also passes **11/11** with zero delta. The complete registered suite is now
**16/16 rules / 110 controls**. No Step 2 stop condition fired.

**v0.41 Step 3 — fired dispositions require measurable substance (measured
2026-08-04).** Before adopting the predicate in either live governed row, the
proposed parser rejected `trigger-fired disposition: aware.`, accepted the
truthful unheld form naming **Grant E / 84,896 recoverable bytes**, and accepted
a measured-change form only when baseline and current byte values differed.
This proves C24 satisfiable against the entering state without inventing a
grant, recovery, or improvement.

The adopted grammar applies to every governed trigger crossing the checker can
evaluate, not only the review-export row. Exactly one disposition prefix must
carry exactly one of two forms: `measured-change` with a named subject and
distinct baseline/current byte values, or `unheld-lever` with a named lever and
positive recoverable bytes. Both export attention and governed artifact
triggers consume the same parser. The live Architecture and State-archival rows
therefore use `kind=unheld-lever`, `lever=Grant E`, and
`recoverable_bytes=84896`; this is answerable by the next export measurement
without falsely claiming Step 5 ran.

R12's new substance construction passes its registered fail-before mutation as
control **33**; the complete suite passes **16/16 rules / 111 controls**. The
focused export/lifecycle population passes **111/111**. The permission-complete
local matrix passes **22/22** with Python 3.11 at **391/391**, and standalone
golden passes **11/11** with zero delta. No dependency, production source,
protected byte, response domain, accepted threshold, tag, or remote ref moved;
no Step 3 stop condition fired.

**v0.41 Step 4 — review source carries only usable manifest pins (measured
2026-08-04).** C25 retains the review-relevant manifest head without adding a
new artifact: the existing tracked and unpinned operations document carries a
deterministic projection sourced by its own marker from
`config/protected-artifacts.json`. The projection copies every non-pin field
and retains exactly those pin records whose referenced paths survive the prior
Git-derived review partition. The real derivation yields **1 manifest / 339
total pins / 9 retained / 330 omitted**. Both a visible and a non-visible pin
are required for membership, so this is a semantic mixed-use class rather than
a threshold selected to reach the capacity target.

The exact configured manifest exclusions must equal that derived class in both
directions. R12 plants an empty class, an unexcluded derived member, a
configured nonmember, and a stale projection; all four fail-before mutations
are detected at their registered control sites. The focused export population
passes **20/20**. The protected manifest remains byte-identical at **200,440
bytes**, SHA-256 `f59d4520cfaa0190954442856b6bb1ab5576049f16d5b8b816f00f64495fefae`, with all **339** pins intact.
No protected byte or integrity authority moved.

The resulting project-root export passes at **2638599 bytes / 157 tracked
entries / 2 retained cycles**, **69,211 bytes above** the **2,569,388-byte**
attention boundary and **361401 bytes / 12.05% / 1.68 high-water cycles** below
the fixed ceiling. Against the exact entering export, review-source selection
recovers **165327 bytes** despite the checker, test, projection, and dated-record
growth added by the task. The attention predicate therefore remains fired;
this measured change answers the disposition without claiming the unissued
Grant E lever ran. The complete registered suite is **16/16 rules / 115
controls**. The permission-complete local matrix passes **22/22**, with Python
3.11 at **396/396**; standalone golden passes **11/11** with zero delta. No C25
falsifier or Step 4 stop condition fired.

**v0.41 Step 5 — Grant E not granted; archival remains dormant (measured
2026-08-04).** The initiating authorization and every subsequent operator
message through this step were checked against Grant E's exact required
content. The operator authorized publication, but did not issue the separate
irreversible archival grant. This is the runbook's dated **not-granted** branch,
not an inferred refusal and not partial authority.

The C26 move therefore did not execute. No byte was created under
`docs/state-archive/`, and `config/protected-artifacts.json` remains exact at
**200,440 bytes / 339 pins**, SHA-256
`f59d4520cfaa0190954442856b6bb1ab5576049f16d5b8b816f00f64495fefae`.
The eligible v0.38-to-permanent-marker region remains **84,896 unrecovered
bytes**. State measures **185054 / 453,741 bytes** after this observation. The
review-export attention predicate remains fired after REVIEW-SOURCE, so the
archival deferral truthfully retains `kind=unheld-lever`, `lever=Grant E`, and
`recoverable_bytes=84896`; it claims neither an archive nor a pin.

The permission-complete local matrix passed **22/22** jobs, including **16/16
rules / 115 controls**, Python 3.11 at **396/396**, and embedded golden
**11/11**. The separately required golden run also passed **11/11** with zero
delta. No Step 5 stop condition fired.

**v0.41 Step 6 — exact hosted candidate passed (measured 2026-08-04).**
Checker changes made RE-MEASURE mandatory. Historical attestation preflight
passed **7/7** bundles under every strict flag with required and observed
GitHub CLI **2.96.0**, and the deliberately wrong signer was rejected. The
full pre-push snapshot kept remote `main` and every recorded annotated/peeled
release tag exact. The required absence pre-check for
`refs/heads/codex/v0.41-evidence-4405882` returned exit **2** with no output.
One non-force push then created exactly that one v0.41 ref at audited candidate
`44058820d25834d2b89d54cda48ed723a3dfa77f`; it was not retried, reused,
forced, or moved.

Workflow-dispatch run **30917725112**, attempt **1**, targeted that exact SHA
and ref and concluded `success`. All **9/9** workflow-derived blocking
identities passed: core, golden, lint, offline MSRV, net MSRV 1.85 refusal, net
MSRV 1.86 success, net, shell Python 3.11, and shell Python 3.12. Dependency
drift was the sole report-only skip. The run persisted **9** receipts and **9**
Sigstore bundles. After the clean candidate worktree received the ignored
protected corpora required by the verifier, strict release-grade verification
accepted **9**, rejected **0**, authenticated the exact repository, workflow,
source digest, and source ref, and derived one complete nine-identity matrix.
The earlier clean-worktree attempt without those ignored databases stopped
before receipt acceptance and is a setup non-result, not evidence.

Fresh permission-capable local Python 3.11 and 3.12 runs each collected and
passed **396/396**, including the named `on_site` protected-corpus test. Each
hosted lane collected **396**, passed **395**, and skipped only
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
with its declared protected-corpora/built-core reason and `on_site` marker.
Both direct `tools/test_population.py` comparisons derive
`equivalent=true`, `equivalent_passed=396`, and exactly one allowed hosted
skip. Initial sandboxed local attempts failed **8** tests solely because socket
binds and `ps` inspection were denied; they are disclosed non-measurements and
were replaced by the clean permission-capable runs.

Final remote readback resolves the evidence ref to the exact candidate, keeps
`main=dd605acc037da405fa6b2b5366b09349c330c194`, and keeps every release tag
byte-for-byte at the pre-push snapshot; v0.17.6 and v0.17.7 remain absent. The
exact candidate project-root export passes at **2645906 bytes / 157 tracked
entries / 2 retained cycles**, **76,518 bytes above** the **2,569,388-byte**
attention boundary and **354094 bytes / 11.80% / 1.64 high-water cycles** below
the unchanged ceiling. State measures **188277 / 453,741 bytes** after this
record. No production source, dependency, protected byte, observation,
fixture, publisher wire, public response domain, entitlement/licensing
outcome, local tag, `main`, or release tag moved; no Step 6 stop condition
fired.

**v0.41 ACTIVATE — capacity-relief cycle declared (measured 2026-08-04).**
The declaration, runbook, progress skeleton, and review-retention pattern now
select v0.41 and exactly the v0.40–v0.41 task/progress pairs. All **31/31**
deferral subjects carry dated v0.41 observations measured before activation;
the four trigger-bearing Architecture rows name the same cycle. The delivered
closing-record template used the semantic closed-cycle heading, so it was
renamed before activation without weakening a lifecycle predicate. No
observation template survives.

The initiating operator statement is recorded verbatim in the runbook:
“I authorize you to publish before you begin the current task.” It authorizes
publication of v0.17.7 and the v0.41 release under R-CLOSE, while the permanent
v0.17.6 withholding remains exact. It does not issue Grant E; the archival step
therefore remains dormant unless that grant's exact content later appears.

Exact entering commit `2c457feb870d62b16a5f9d9ca06aefcb3dc4cf8b`
passes its project-root export at **2,803,926 bytes / 158 tracked entries / 2
retained cycles**, **234,538 bytes above** attention and **196,074 bytes / 6.54%
/ 0.91 high-water cycles** below failure. The untracked draft worktree instead
measured **2,851,841 bytes / 159 entries** and correctly failed on its untracked,
out-of-retention v0.41 runbook. After staging the derived v0.40–v0.41 retention
set, the pre-record activation candidate passes at **2,768,569 bytes / 158
tracked entries / 2 retained cycles** with the attention predicate still
firing. This is a measured transition, not an assertion copied from the draft.

Fresh remote readback keeps `main` at `dd605acc…`, v0.17.2 through v0.17.5
exact, and v0.17.6/v0.17.7 absent. Local v0.17.7 remains annotated object
`2287b415…` peeling to closing commit `cd4fd58…`; a detached checkout of that
real tag passes `cycle-check` with `local-tag-reconciliation=verified`.
Manifest schema v2 remains **3 artifacts / 339 pins** at **200,440 / 1,048,576
bytes**; two complete checks took **0.10 s / 0.10 s real**. State before this
record was **172,701 / 453,741 bytes**. R15 remains exact at **0 differences /
6 routes / 112 field occurrences**, `version-check` derives **3** offline pins,
**22** current floor restatements, and **3** release restatements over **589**
tracked files, and the registered suite passes **16/16 rules / 108 controls**.
The first golden attempt was a sandbox-denied loopback-bind non-result; the
permission-capable identical run passes **11/11** with delta zero.

Three delivered numeric hypotheses are already refuted rather than normalized:
State was **172,660**, not 172,659 bytes before the status edit; the manifest is
**200,440**, not 200,439 bytes; and the v0.38/v0.37/v0.36 suffixes are each one
byte larger than stated. The movable closed-record region beginning at v0.38
and ending before the permanent tail is **84,896 bytes**. Before the activation commit exists,
`cycle-check` reports only the two predicted inability-to-resolve the first
committed runbook and activation anchor facts. No dependency, production
source, protected byte, observation, fixture, publisher wire, entitlement or
licensing outcome, local tag, or remote ref moved; no activation stop condition
fired.

**v0.40 cycle-ending audit — v0.17.7 tagged tree passes (measured
2026-08-04).** Local annotated object
`2287b41558e69bb86490df71b6907a2f0eb73310` peels to closing commit
`cd4fd58b39c855cc769d3696a6b389f735066022`, whose immediate parent is exact
0.17.7 authority commit `b8fe1c2c1c2c842868a70581dee390939ef68595`.
A fresh detached checkout of tag v0.17.7 passes `cycle-check` with
`local-tag-reconciliation=verified`, passes checklist audit at **317 checked /
3 retracted / 308 matched / 308 resolved / 9 exemptions** with v0.40 at
**7/7/7**, and passes `version-check` as the exact 0.17.7 HEAD tag. This is the
measured post-tag verdict; unlike v0.17.6, the tag checkout itself is clean.

The immutable closing tree's project-root export passes at **2,801,474 bytes /
158 tracked entries / 2 retained cycles**, exactly **+12,424 bytes** from the
governed release-parent figure. It leaves **198,526 bytes / 6.62% / 0.92
high-water cycles** below the unchanged ceiling and stands **232,086 bytes
above** attention. The append-only progress audit field binds that closing
tree without superseding the governed parent measurement.

Post-close remote readback keeps `main` exact at
`dd605acc037da405fa6b2b5366b09349c330c194`, keeps the sole authorized v0.40
evidence ref at `52a5c44b060a795894aa120fb8cd0b1ab0d5cf09`, and returns no
direct or peeled v0.17.6/v0.17.7 tag. No publication, main movement, force
operation, tag movement, deletion, or additional push occurred.

- **Publication observation date:** 2026-08-04
- **Publication observation release:** `v0.17.7`
- **Publication observation status:** `unpublished-local-close`
- **Publication observation remote:** `origin`
- **Publication observation tag ref:** `absent`

The v0.41 findings are three bounded facts: governed export headroom is only
**0.98** high-water cycles and the closing tree is at **0.92**; a post-tag
verdict cannot be content-addressed into the tag target that must exist before
the verdict, so the immediate audit child remains its truthful evidence point;
and publishing v0.17.7 would place the superseded v0.17.6 closing tree in
published branch ancestry without publishing its release tag, which requires
an explicit operator adjudication. No additional runtime, public-surface,
dependency, evidence-integrity, or wire finding emerged.

**v0.40 R-CLOSE — v0.17.7 assembled close (measured 2026-08-04).** DR26
selects patch **v0.17.7**. R15 derives **0 differences across 6 routes / 31
status-media response variants / 112 recursive field occurrences**, so neither
the public-surface nor serialized-value-domain minor clause fires. Exact parent
`b8fe1c2c1c2c842868a70581dee390939ef68595` carries all five executable
authorities and all three registered release restatements at 0.17.7; Cargo
changes only cored's package version in the lockfile.

The permission-capable parent gate passes **22/22** jobs. Python 3.11 passes
**391/391**, the registered scan passes **16/16 rules / 108 controls** with
**0** hand-typed absolute finding-line fields, both Rust floor pairs behave as
specified, protected artifacts match, and embedded plus standalone golden pass
**11/11** with delta zero. The exact parent export passes at **2,789,050 bytes
/ 158 tracked entries / 2 retained cycles**. It leaves **210,950 bytes / 7.03%
/ 0.98 high-water cycles** below the unchanged 3,000,000-byte ceiling, misses
the 2.5-cycle target by **327,315 bytes**, and stands **219,662 bytes above**
the corrected 2,569,388-byte attention boundary. The trigger-fired disposition
retains the fixed ceiling, two-cycle retention, and nondecreasing 215,306-byte
high-water denominator.

Fresh pre-close local and remote reads found no v0.17.7 tag. Remote `main`
remained `dd605acc037da405fa6b2b5366b09349c330c194`, neither v0.17.6 nor
v0.17.7 existed remotely, and the only v0.40 remote mutation remained the
authorized evidence ref. At this assembled worktree, no v0.17.7 tag existed;
therefore no post-tag PASS is claimed in this pre-tag measurement.

**v0.40 R-CLOSE release-parent preparation (measured 2026-08-04).** DR26
selects patch **v0.17.7**. The dependency-free R15 derivation and installed
FastAPI runtime comparison report **0 differences across 6 routes / 31
status-media response variants / 112 recursive field occurrences**. The
lifecycle checker, withheld-state control, and review-export attention basis
change assurance behavior only: no production runtime behavior, dependency,
publisher configuration, protected byte, entitlement/licensing outcome,
public route, response field/type, or serialized `/v1/*` value-domain value
moved. Neither minor-version clause fired.

All five executable release authorities and all three current restatements
identify **0.17.7**; Cargo changes only cored's package version in the lockfile.
Fresh local and remote reads found no v0.17.7 tag, remote `main` remained exact
at `dd605acc037da405fa6b2b5366b09349c330c194`, and neither v0.17.6 nor
v0.17.7 existed remotely. The only v0.40 remote mutation remains the authorized
evidence ref; no publication ref moved.

**v0.40 RE-MEASURE — exact hosted candidate passed (measured 2026-08-04).**
Checker and governing-contract changes made hosted execution mandatory. Exact
audited candidate `52a5c44b060a795894aa120fb8cd0b1ab0d5cf09` passed the
permission-complete local matrix before dispatch at **22/22** identities,
including Python 3.11 and 3.12 **391/391**, registered scan **16/16 rules /
108 controls**, both Rust floor pairs, protected artifacts, and golden
**11/11**. The historical attestation preflight accepted **7/7** immutable
bundles under every strict flag and rejected the deliberately wrong signer.

Immediately before ref creation, fresh remote readback kept `main` at
`dd605acc037da405fa6b2b5366b09349c330c194` and every annotated and peeled tag
through v0.17.5 at its recorded identity. `git ls-remote --exit-code` returned
**2** with no output for fresh
`refs/heads/codex/v0.40-evidence-52a5c44`. One non-force push created exactly
that ref at the candidate; it was not retried, forced, reused, or moved.

Workflow-dispatch run **30896642221**, attempt **1**, targeted the exact SHA
and ref and concluded `success`. All **9/9** workflow-derived blocking
identities passed; dependency drift was the sole report-only skip. The run
persisted **9 receipts / 9 Sigstore bundles**. The release-grade verifier
accepted **9**, rejected **0**, verified all **9** against the exact repository,
workflow, source digest, and source ref, and derived a complete single-run
nine-identity matrix.

Each hosted shell lane collected **391**, passed **390**, and skipped only
named
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
with its declared protected-corpora/built-core reason and `on_site` marker.
The first local comparison was a non-result because the disposable candidate
clone lacked its own built `cored` and therefore also skipped that test. After
building `cored` from the exact candidate in that clean clone, Python 3.11 and
3.12 each passed **391/391** locally. Both direct
`tools/test_population.py` comparisons derive `equivalent=true` and
`equivalent_passed=391` from those raw logs.

Final remote readback resolves the evidence ref to the exact candidate, keeps
`main` at `dd605acc037da405fa6b2b5366b09349c330c194`, and keeps every tag
identity byte-for-byte at the pre-push snapshot; v0.17.6 remains absent
remotely. No publication ref, tag, workflow byte, dependency, production
source, protected byte, observation, fixture, publisher wire,
entitlement/licensing outcome, serialized response domain, or golden input
moved. The required standalone local golden run passes **11/11** with delta
zero.

**v0.40 ATTENTION-BASIS — a quiet cycle cannot shrink the reserve (measured
2026-08-04).** The estimator now derives every positive adjacent governed
delta through the evaluation cycle and selects their maximum. The recorded
high-water is v0.34 **2,527,180 →** v0.35 **2,742,486**, or **+215,306
bytes**. The two-cycle reserve is therefore **430,612 bytes**, compared with
the prior latest-positive reserve of **214,452 bytes**: it widens by **216,160
bytes** at the same activation tree. The attention boundary moves from
**2,785,548** to **2,569,388 bytes**; the accepted **3,000,000-byte failure
ceiling is unchanged**.

The exact activation measurement of **2,712,884 bytes** is **143,496 bytes
above** the corrected boundary, so the attention trigger fired. The recorded
disposition retains the ceiling and two-cycle retention, adopts the
nondecreasing high-water reserve, and requires the final release-tree
remeasurement. The pre-record task worktree's operator-local export passes at
**2,775,132 bytes / 158 tracked files / 2 retained cycles** with
`attention_state=trigger-fired-disposed`; it is **205,744 bytes above** the
warning boundary and **224,868 bytes / 1.04 high-water cycles** below failure.

The governed margin explicitly continues to share the high-water denominator
because it expresses the same remaining ceiling capacity; using the lower
latest delta there would understate the observed risk. A later positive
adjacent governed delta above **215,306** falsifies and replaces the current
numeric basis. A structural epoch remains unobserved by the checker and would
require an independent machine-readable authority before it could partition
the series. The dedicated quiet-cycle fixture has an older **+20** high-water
followed by a **+10** latest increase: the previous selector rejects its
high-water declaration, while the implemented selector accepts it and keeps
the lower boundary. The focused cycle population passes **96/96**.

The permission-complete local matrix passes **22/22** jobs. Python 3.11 and
3.12 each pass the complete **391/391** population with the same one accepted
warning; the registered suite passes **16/16 rules / 108 controls**, including
R12's quiet-cycle series mutation. Embedded and required standalone golden
each pass **11/11** with delta zero. R15 remains exact at **0 differences / 6
routes / 112 field occurrences**. No dependency, production runtime byte,
protected byte, observation, fixture, publisher wire, entitlement/licensing
outcome, public response domain, local tag, or remote ref moved.

**v0.40 WITHHELD-STATE — permanent refusal is explicit (measured
2026-08-04).** v0.17.6 now has one consequential, reasoned
`permanently-withheld` record with the exact `local-only-never-remote` tag
expectation. The live handoff calls the decision settled and contains no
pending or outstanding publication question. Local full verification still
requires and validates the immutable annotated tag. Hosted-shaped verification
without the portable skip may omit only the tag of an exactly recorded
withheld release and returns the distinct `withheld-hosted` reconciliation;
an ordinary unpublished release with the same missing-tag topology fails.

Five direct tests cover local tag validation plus hosted absence, a missing
reason, the withheld/pending contradiction, ordinary hosted absence, and local
withheld absence. R12 adds six independent mutations for the record parser,
closing-record admission, hosted publication admission, and the two
ordinary-release non-exemptions. Its test harness measures both hosted-shaped
entry points rather than inferring their behavior from the parser alone. The
registered suite passes **16/16 rules / 108 controls**; the permission-complete
local matrix passes **22/22** jobs; Python 3.11 and 3.12 each pass the expanded
**390/390** population with the same one accepted warning; and golden passes
**11/11** with delta zero. No dependency, production runtime byte, protected
byte, observation, fixture, publisher wire, entitlement/licensing outcome,
public response domain, local tag, or remote ref moved.

**v0.40 PRE-TAG-GATE — stale closing identity is preventable (measured
2026-08-04).** The publication assertion partition is now derived from its
actual inputs. State/header admission, the mutable-branch-ref prohibition, and
tagged-closing release-parent freshness require no tag and execute before both
portable-mode and tag-resolution returns. Legacy object/target assertions,
annotated type, closing-parent/tree identity, ancestry, reachable-tag pending
status, and descendant disposition remain tag-dependent. An assembled closing
worktree receives the distinct
`local-tag-reconciliation=pre-tag tag-independent-assertions=verified` verdict
only while the tag is absent, the closing record has no tag-object field, and
`HEAD` equals its recorded release parent. A missing tag fails again after the
closing commit exists.

An in-memory execution of the exact pre-change `8c93c00…` checker reports
`freshness=false / unavailable=true / pre_tag=false` for both stale and correct
tagless headers. The implemented checker reports `freshness=true /
unavailable=false / pre_tag=true` for the stale case and fails overall, while
the correct case reports no error and the verified pre-tag verdict. Portable
mode also rejects the stale identity. Four direct lifecycle tests cover correct
pre-tag admission, stale local refusal, stale portable refusal, and refusal of
a missing tag once the closing commit exists.

R12 now carries **50** independently executable mutations and the registered
suite passes **16/16 rules / 102 controls**. The two new mutations independently
remove closing-record pre-tag admission and the normal pre-tag publication
branch; the existing release-commit mutation now also proves stale local and
portable tagless identities are caught. Its test double can answer downstream
object, target, parent, tree, and `HEAD` queries when an earlier guard is
mutated away, so no planted control depends on a double that crashes before the
guard under test can speak.

The permission-complete local matrix passes **22/22** jobs. Python 3.11 and
3.12 each pass the expanded **385/385** population with the same one accepted
warning; all Rust floor, warning, lint, protected-artifact, and fingerprint
checks pass. Golden passes **11/11** with delta zero. No dependency, production
runtime byte, protected byte, observation, fixture, publisher wire,
entitlement/licensing outcome, public response domain, or remote ref moved.

**v0.40 E0 — entering state reconstructed (measured 2026-08-04).** The
pre-activation object graph is exact: v0.17.6 release parent
`acfa801102197ce2d94adaa5a14a3ad102893549` is the immediate parent of closing
commit `7c9305f01219412048ec75236f2bf1e61112c178`, local annotated tag object
`66ee2cbbe374b99722bec49b8176571777aaa899` peels to that closing commit, and
audit child `5885529a5f33e9c773f81d8d9434e47d77161d34` is its immediate child. Fresh
remote readback keeps `main` exact at
`dd605acc037da405fa6b2b5366b09349c330c194`, confirms remote v0.17.2 through
v0.17.5, and returns no v0.17.6 tag while the local tag remains present.

A detached checkout of the real v0.17.6 tag reproduces the single disclosed
publication-assertion freshness defect: the header spends the strict phrase on
historical v0.17.5 parent `37f552c0c326098bdcf8f19de7eac19670d74680`
while the checker derives expected v0.17.6 parent `acfa801…`. The same immutable
header also names `acfa801…` outside that assertion and the closing record names
it correctly, so the tagged tree is self-contradictory rather than simply
missing the correct identity. Source tracing and a disposable no-tag clone show
that both freshness inputs already exist before tag creation, but tag-resolution
failure returns before the strict assertion loop. Deleting only the disposable
clone's v0.17.6 tag makes full verification fail on both local-tag resolution
and publication-verification unavailability; the real tag was not moved.

The full local gate passes **22/22** jobs. Python 3.11 and a separately rebuilt
Python 3.12 environment each pass **381/381** tests with the same one accepted
warning. The registered suite passes **16/16 rules / 100 controls**; direct
checklist derivation is **311 checked / 3 retracted / 302 matched / 302 resolved
/ 9 exemptions**, refuting the draft's stale 303 / 3 / 294 / 294 / 9 figures.
Golden passes **11/11** with delta zero. The entering commit export passes at
**2,743,797 bytes / 158 tracked entries / 2 retained cycles**, exactly **41,751
bytes** below the old **2,785,548-byte** attention boundary. Entering State is
**152,810 / 453,741 bytes**, refuting the draft by one byte; the protected
manifest remains **200,440 / 1,048,576 bytes**. The measured governed series
still makes v0.37 **2,674,055** to v0.38 **2,781,281**, or **+107,226**, the
latest positive adjacent delta; both worked-example branches recompute exactly.
At the E0 recording point, `git status --porcelain` contains only this task's
runbook edit plus the exact three pre-existing untracked historical amendment
inputs; those inputs remain untouched.

**v0.40 ACTIVATE — corrective cycle declared (measured 2026-08-04).** The
activation worktree advances the declaration and derived review retention to
v0.40 and exactly v0.39–v0.40. All **31/31** deferral subjects carry dated
v0.40 observations measured before the activation commit; the four
trigger-bearing Architecture rows name the same active cycle. The supplied
draft repeated v0.39's already-measured semantic-heading defect by using the
literal `## Cycle closing record` for an unassembled template. Before semantic
acceptance it was renamed `## Closing-record assembly template`, preserving
the Step 6 instructions without causing an open cycle to masquerade as closed.

The staged project-root export passes at **2,710,665 bytes / 158 tracked files
/ 2 retained cycles**, with all **158/158** derived required paths present,
exactly **4/4** derived raw-wire exclusions, and both structural archives
absent. At the entering **107,226-byte** denominator it leaves **289,335 bytes
/ 9.64% / 2.70 cycles** below the unchanged 3,000,000-byte ceiling and is
**74,883 bytes** below the entering 2,785,548-byte attention boundary. The
pre-activation worktree result at **2,788,376 bytes** was correctly rejected
for its untracked v0.40 runbook, unexpected cycle document, and crossing of the
old boundary; it is a measured non-acceptance, not evidence for the activated
tree.

Manifest schema v2 remains **3 artifacts / 339 pins** at **200,440 /
1,048,576 bytes**. Two complete artifact checks pass in **0.11 s / 0.09 s
real**. Pre-record State is **152,810 / 453,741 bytes**. Fresh R15 derivation
reports **0 differences across 6 routes / 112 field occurrences**;
`version-check` derives **3** offline pins, **22** current floor restatements,
and **3** release restatements over all **587** entering tracked files. The
registered suite passes **16/16 rules / 100 controls**. The first sandboxed
golden attempt was a loopback-bind permission non-result; the identical
permission-capable run passes **11/11** with delta zero. No dependency,
production source, protected byte, observation, fixture, publisher wire,
entitlement/licensing outcome, or remote ref moved. Before the activation
commit exists, `cycle-check` reports only the two expected inability-to-resolve
the uncommitted runbook/activation-anchor facts; all semantic, trigger,
retention, artifact, and publication checks are otherwise clean.

**v0.39 R-CLOSE — v0.17.6 release parent measured (2026-08-04).** DR20 selects
patch **v0.17.6**. The release-baselined R15 derivation and installed FastAPI
runtime comparison report no public response-domain difference across **6
routes / 31 status-media response variants / 112 recursive field
occurrences**. Review-export truth, attention, and bounded-egress controls add
no production runtime behavior, dependency, publisher configuration,
entitlement/licensing outcome, protected-evidence movement, or serialized
field-domain value. Neither minor clause fires.

Exact untagged release parent
`acfa801102197ce2d94adaa5a14a3ad102893549` moves all five executable
authorities to 0.17.6. `version-check` reports **3** offline pins, **22**
current offline-floor restatements, **3** current release restatements, and all
**587** tracked files classified. Its permission-complete full gate passes
**22/22** jobs; Python 3.11 and 3.12 each pass **381/381**, the registered scan
passes **16/16 rules / 100 controls**, both Rust floor pairs behave as
specified, protected artifacts match, and embedded plus standalone golden pass
**11/11** with delta zero.

The exact release parent exports **2,729,600 bytes / 158 tracked entries / 2
retained cycles**. It leaves **270,400 bytes / 9.01% / 2.52 measured cycles**
below the fixed ceiling, clearing the 2.5-cycle target by **2,335 bytes** and
remaining **55,948 bytes** below the executable attention boundary. The
assembled closing tree exports **2,740,695 bytes**, leaving **259,305 bytes /
8.64% / 2.42 cycles** and missing the 2.5-cycle target by exactly **8,760
bytes**, while remaining **44,853 bytes** below attention. These fixed-width
fields are replaced from the final assembled-tree measurement before commit.
The
protected manifest remains **200,440 / 1,048,576 bytes** and two complete
artifact checks each took **0.09 s real**. Release-parent State is **149,239 /
453,741 bytes**. Neither governed artifact, attention, or timing trigger fires.

Fresh pre-close local/remote readback found no v0.17.6 tag and kept remote
`main` exact at published v0.17.5 audit child
`dd605acc037da405fa6b2b5366b09349c330c194`. DR21 therefore closes v0.17.6
locally: no push, remote main move, or new release publication is authorized.
Every active deferral row carries a latest dated v0.39 observation, and the
mandatory immediate audit child owns the later closing-tree export disclosure.

Post-close remote readback again kept `main` exact at
`dd605acc037da405fa6b2b5366b09349c330c194` and returned no annotated or
peeled v0.17.6 tag ref. This is the dated unpublished-local observation for the
audit-child descendant; it is not a publication receipt and does not authorize
any ref movement.

- **Publication observation date:** 2026-08-04
- **Publication observation release:** `v0.17.6`
- **Publication observation status:** `unpublished-local-close`
- **Publication observation remote:** `origin`
- **Publication observation tag ref:** `absent`

- **Withheld release decision date:** 2026-08-04
- **Withheld release:** `v0.17.6`
- **Withheld release status:** `permanently-withheld`
- **Withheld release reason:** Its immutable tagged closing tree fails strict publication-assertion freshness because its State header spends the release-commit assertion on historical v0.17.5 parent `37f552c0c326098bdcf8f19de7eac19670d74680` instead of recorded v0.17.6 parent `acfa801102197ce2d94adaa5a14a3ad102893549`; DR22 forbids moving or publishing it.
- **Withheld release tag expectation:** `local-only-never-remote`

**v0.39 closing-export audit and tagged-tree finding (measured 2026-08-04).**
Local annotated tag object `66ee2cbbe374b99722bec49b8176571777aaa899`
peels to closing commit `7c9305f01219412048ec75236f2bf1e61112c178`,
whose immediate parent is exact release commit
`acfa801102197ce2d94adaa5a14a3ad102893549`. The project-root export of that
closing commit passed at **2,740,695 bytes / 158 tracked files / 2 retained
cycles**, a truthful **+11,095-byte** difference from the 2,729,600-byte
governed release-parent field. This append-only child is the immediate next
commit after the tag target and does not predict its own content-addressed id
or move any remote ref.

The first post-tag `cycle-check` verified the annotated-tag topology but failed
publication-assertion freshness: the tagged State header's exact generic phrase
`Untagged release commit` still named historical v0.17.5 parent `37f552c…`, so
the checker compared that stale assertion with current v0.17.6 release parent
`acfa801…`. The live header above is forward-corrected to reserve that exact
phrase for v0.17.6 and names the older object as a historical release parent.
The local tag is not moved or deleted: the standing prohibition makes the
tagged closing-tree defect immutable, and this record does not claim that a
checkout of the tag itself passes `cycle-check`. v0.17.6 must not be published.

**v0.39 RE-MEASURE — exact hosted candidate passed (measured 2026-08-04).**
The checker and governing-contract work made hosted execution mandatory. Exact
candidate `fa846095b7387bcf9e832d558dc8a70a6d29813b` had already passed the
permission-complete local matrix at **22/22** identities, including Python
3.11 **381/381**, both Rust floor pairs, scan **16/16 rules / 100 controls**,
protected artifacts, lint/format, and golden **11/11**; the separate local
Python 3.12 lane passed the identical **381/381** population.

Immediately before ref creation, the remote readback kept `main` at
`dd605acc037da405fa6b2b5366b09349c330c194` and every annotated and peeled tag
through v0.17.5 at its recorded identity. `git ls-remote --exit-code` returned
**2** with no output for fresh
`refs/heads/codex/v0.39-evidence-fa84609`. One non-force push created exactly
that ref at the candidate; no ref was reused, retried, forced, or moved.

Workflow-dispatch run **30875346351**, attempt **1**, targeted the exact
candidate/ref and concluded `success`. All **9/9** workflow-derived blocking
identities passed; dependency drift was the sole report-only skip. The run
persisted **9 receipt artifacts**, each containing one JSON receipt and one
Sigstore bundle. The repository's release-grade verifier accepted **9**,
rejected **0**, verified all **9** attestations against the exact repository,
workflow, source digest, and source ref, and found a complete identity matrix.

Each hosted shell lane collected **381**, passed **380**, and skipped only
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
with its declared protected-corpora/built-core reason and `on_site` marker.
Direct `tools/test_population.py` comparisons for Python 3.11 and 3.12 each
derive `equivalent=true` and `equivalent_passed=381`. Hosted golden passed
**11/11**, and the explicit 1.86 success and 1.85 refusal jobs passed with their
pinned effective toolchains.

Final remote readback resolves the evidence ref to the exact candidate, keeps
`main` at `dd605acc037da405fa6b2b5366b09349c330c194`, and keeps every tag
identity byte-for-byte at the pre-push snapshot. Grant C remains spent; no
publication ref, tag, workflow byte, dependency, protected byte, publisher
wire, entitlement/licensing outcome, serialized response domain, or golden
input moved.

**v0.39 WIRE-CONTRACT — bounded SEC egress registered (measured
2026-08-04).** C18 places the invariant claim in `ARCHITECTURE.md` and its
operator-facing restatement in `AGENTS.md`: architecture owns the safety
boundary a later publisher widening must preserve, while the operating
contract names the command an agent may execute. A new R16 is the honest home
rather than an R8 or R12 extension because it owns one coherent shell entry
point and helper call chain, not crawler-identity construction or release
lifecycle.

R16 follows the actual `./run harvest-sec` dispatcher into
`cmd_harvest_sec`, `cmd_verify_artifacts`, `refuse_protected_harvest`,
`harvest_db_path`, `fresh_harvest_db_path`, and the exact finance-source
membership in `config/core.json`. Ten reconstructible controls
prove: artifact verification precedes environment setup and network-capable
work; the protected-target call precedes bind and its manifest match returns
failure; nonempty crawler contact precedes bind; one exact configured SEC
source is requested and validated; the no-override default selects a
non-existing timestamped path and skips existing candidates; success requires
`first_window`, every fetched document new, and an SEC-only archive; and no
observation or fixture is used as
publisher-response input. The verifier's integrity read of pinned evidence is
explicitly preflight rather than a response-body substitute.

One belief outran the executable and is a handoff finding: an explicit
unprotected `CORE_DB` override is admitted before the wire request without an
absence-or-empty check. Later response/archive validation can reject a
non-fresh result but cannot make the preceding request fresh. The documents
therefore claim fresh pathname selection only for the no-override default and
do not claim strict fresh-path-only admission for explicit overrides. Step 5
does not change `run` to manufacture the proposed claim.

The unmodified registry and all ten R16 mutations pass at **16/16 rules /
100 controls** with expected finding lines derived from unchanged mutant text,
not hand-typed absolute line fields. Focused harvest/config tests pass **4/4**.
After correcting an initially overlapping expected anchor caught by the
existing anti-vacuity test, the complete local gate passes **22/22** jobs;
Python 3.11 and Python 3.12 each pass the identical **381/381** population with
the accepted warning nonfatal, and the required standalone golden run passes
**11/11**. The final pre-box project-root export passes at **2,716,614 bytes / 158
tracked entries / 2 retained cycles**, leaving **68,934 bytes** before the
2,785,548-byte attention boundary; its attention state is `clear`. No live
wire, publisher config, production source, protected byte, observation,
fixture, dependency, entitlement/licensing outcome, golden input, or remote ref
moved.

**v0.39 CEILING-TRIGGER — attention before failure (measured 2026-08-04).**
C17 selects a reserve of two governed-growth cycles at the checker-derived
latest positive adjacent governed denominator. The executable formula is
`3,000,000 - (2 × 107,226) = 2,785,548 bytes`; the accepted 3,000,000-byte
ceiling is unchanged. The principle preserves two measured growth cycles for
action rather than announcing only after failure. It is falsified, and the
checker refuses the boundary, if no positive adjacent governed pair exists, if
the denominator is non-positive, if the reserve does not land strictly inside
the ceiling, or if the written value disagrees with the formula.

`export-check` now measures generated bytes against that derived boundary and
requires a valid date plus non-`none` `trigger-fired disposition:` in the
governed Architecture row at or above it. `cycle-check` independently binds the
boundary denominator to the already-checked governed progress series and
applies the same disposition rule to the recorded governed figure. The
registered R12 mutation disables the actual `>=` crossing guard; the undisposed
boundary construction then fails, while the identical disposed construction
passes. The active `Review-export capacity` trigger is forward-corrected from
the post-failure ceiling predicate to this pre-failure predicate; the separately
pinned `Second STATE.md archival` trigger remains byte-unchanged and inherits
the sharper meaning through “the export ceiling trigger fires.”
R12 passes **48/48** mutations and the complete registered suite passes
**15/15 rules / 90 controls**. The complete local gate passes **22/22** jobs;
Python 3.11 and Python 3.12 each pass the identical **380/380** population with
the same accepted non-fatal warning, and golden remains **11/11**. The final
worktree export passes at **2,692,723 bytes / 158 tracked entries / 2 retained
cycles**, leaving **92,825 bytes** before the attention boundary; its reported
attention state is `clear` and no disposition is required.

**v0.39 EXPORT-TRUTH — export images the checked tree (measured
2026-08-04).** C15 selects one Repomix family exclusion,
`docs/cycles/AMENDMENT-{r4,v0.36}-*.md`, for the three historical amendment
inputs. It is one declarative class rather than three per-file literals, leaves
Git status visible, does not touch or admit the scope-forbidden historical
files, and does not hide a future amendment family. The selection would have
changed if the inputs did not share those two bounded historical families or
if their review value required tracked admission under an authorized scope; in
that case a broader exclusion would have hidden unrelated future evidence.
Their bytes remain exact **16,834 + 18,906 + 7,387 = 43,127**, their three
SHA-256 values remain `02c254c1…`, `fb45efb0…`, and `dd8122cd…`, and all three
remain untracked and byte-untouched.

C16 selects the existing Git `binary` byte-preservation attribute as the class
seam, intersected with manifest-pinned `observation` files. The real pin
population derives exactly **4** raw-wire bodies: the v0.25 RSS body and the
v0.38 privacy, robots, and RSS bodies. Repomix now carries exactly those four
exact observation exclusions: derived-minus-configured **0** and
configured-minus-derived **0**. The small unmarked v0.25 robots policy remains
a review source rather than being swept into the class. Manifest-derived
structural-archive prefixes remain exactly `docs/state-archive/`. The seam
would be rejected if a binary-marked pinned observation were a review source,
if a raw no-review body lacked the mark, or if either set difference became
nonzero; the bidirectional registered controls make those states failures.

The generated project-root export passes at **2,675,532 bytes / 158 entries /
2 retained cycles**. Its partition is exhaustive by construction: all **158**
entries are Git-tracked, **0** are untracked defects, all **158/158** derived
required paths are present, all **4/4** derived raw bodies are absent, and both
structural archives are absent. The three untracked amendment inputs are absent
without being edited. Every active declared-scope pattern was also evaluated
over **587 tracked + 3 untracked** repository candidates: every clean pattern
matched at least one path, while the exact annotated vacuous predecessor fails
the new syntax guard and the corrected `docs/cycles/**` form passes.

R12 adds five reconstructible mutations for an untracked export entry, an
empty raw-wire population, a missing raw-wire exclusion, an extra non-wire
observation exclusion, and the vacuous annotated scope row. All **47/47** R12
controls and **15/15 rules / 89 controls** overall pass. The complete Python
3.11 and Python 3.12 populations each pass **377/377** with the same one
accepted non-fatal Starlette warning, and the complete local gate passes all
**22/22** jobs. The edited export tool
contains no hand-maintained required-path list, excluded filename list,
excluded prefix list, or cycle-specific literal. No dependency, production
source, protected byte, observation, fixture, publisher wire, entitlement or
licensing outcome, golden input, or remote ref moved.

**v0.39 PUBLISH-V17-5 — Grant C spent exactly (measured 2026-08-04).**
The operator's initiating request issued the named runbook Grant C, whose
verbatim text was recorded in the progress log before any ref movement.
Immediately before the push, `git ls-remote` reported only `main` at
`a7d6c80e7e5ccd963e8ebb46ee054b30af88abb0` and no v0.17.5 tag. That remote
head was proven an ancestor of exact audit child
`dd605acc037da405fa6b2b5366b09349c330c194`; local annotated object
`946bdc015446182727d8f705697e378f8fe8f7eb` peeled to exact closing commit
`55045ae481ce8d1ef285522b3c0a57c91fe5cb54`. No precondition was refuted.

One non-force branch push advanced only `origin/main` to the audit child; one
non-force tag push created only `v0.17.5`. Fresh readback resolves the branch,
annotated object, and peeled target to those three exact values. Push-triggered
run **30868419182**, attempt **1**, concluded `success` on exact head
`dd605acc037da405fa6b2b5366b09349c330c194`: all **9/9** blocking identities
passed, and dependency drift was the sole report-only skip. No ref was forced,
deleted, or moved beyond Grant C. The historical unpublished-local observation
remains untouched as a true dated pre-publication measurement. Grant C is
spent and supplies no authority for v0.17.6 or any other ref.

- **Post-push verification date:** 2026-08-04
- **Post-push release:** `v0.17.5`
- **Post-push annotated tag object:** `946bdc015446182727d8f705697e378f8fe8f7eb`
- **Post-push closing commit:** `55045ae481ce8d1ef285522b3c0a57c91fe5cb54`
- **Post-push hosted run:** `30868419182`

**v0.39 E0 — entering state reconstructed (measured 2026-08-04).** Every
H1–H9 source-export statement was treated as a hypothesis. H1, H2, H3, H7,
and H9 are confirmed; H4 is confirmed for registry/exemption/retraction counts
and refuted for its checklist total; H5 and H8 are numerically refuted; H6's
previously unmeasured whole partition is now measured.

The v0.17.5 graph is exact: release parent `37f552c0…` is the immediate parent
of closing commit `55045ae4…`; annotated object `946bdc01…` peels to that
closing commit; audit child `dd605acc…` is its immediate child and was the
pre-activation entering ref. Fresh remote readback keeps `main` exact at
`a7d6c80e7e5ccd963e8ebb46ee054b30af88abb0`, with v0.17.2–v0.17.4 exact
and v0.17.5, v0.8.0, and v0.10.2 absent. The branch is an ancestor of current
HEAD. Grant C's identities therefore remain eligible for their separate
immediate pre-push remeasurement; E0 itself moved no ref.

State is **132,770 / 453,741 bytes** and the manifest is **200,440 /
1,048,576 bytes** at **3 artifacts / 339 pins**. State contains **3** complete
post-push records and **4** historical unpublished-local observations, with
v0.17.5 current before publication. Direct data counts give **15 rules / 84
controls / 9 exemptions / 3 retractions**. The live checklist is **303 checked
/ 3 retracted / 294 matched / 294 resolved / 9 exemptions**, one higher than
H4 because ACTIVATE is already checked and resolved.

The project-root delivered worktree export passes at **2,778,858 bytes / 163
entries / 2 retained cycles**, not H5's 2,799,094. Its complete set partition
is **160 Git-tracked + 3 existing untracked + 0 synthetic = 163**. The three
exceptions are exactly the amendment inputs at **16,834 + 18,906 + 7,387 =
43,127 raw bytes**; no other exported entry is outside Git. The four
`.gitattributes`-classified raw publisher bodies partition as two excluded RSS
bodies and two present v0.38 bodies: the **90,192-byte HTML** page and
**2,622-byte robots** file. H7 is therefore confirmed.

Retention advances through v0.37 and retains exactly v0.38–v0.39, but H8's
source-byte arithmetic is off by nine: the v0.37 task/progress pair is
**75,859 bytes**, and the current raw recoverable population is **211,800
bytes** when combined with the two present raw bodies and three amendment
inputs. Export framing means Step 3 still owns the actual artifact delta. The
checker independently selects the latest positive adjacent governed pair
v0.37→v0.38 at **+107,226 bytes/cycle**, confirming H9.

The permission-complete `ci-local` passes all **22/22** jobs: **15/15 rules /
84 controls**, Python 3.11 **373/373**, both Rust floor pairs, all warning/lint/
format gates, protected artifacts, and embedded golden **11/11**. A separate
Python 3.12 lane passes the identical **373/373** population; both supported
versions retain the one non-fatal accepted warning. No dependency, production
source, protected byte, fixture, observation, publisher wire,
entitlement/licensing outcome, golden input, or unauthorized ref moved. No E0
stop condition fired.

**v0.39 ACTIVATE — truthful-export cycle declared (measured 2026-08-04).**
The declaration, runbook, progress skeleton, and derived retention boundary land
in exact activation commit `752b2d56ac0e937f91035497225b352a55d3a472`.
All **30/30** carried deferral subjects have dated v0.39 observations before
semantic acceptance, and the four trigger-bearing Architecture rows are
refreshed to the same cycle. Direct post-activation `cycle-check` passes with
`active=v0.39`, `state=open`, both artifact boundaries bound, State regions
bound, and all prior cycles closed.

The draft's literal `## Cycle closing record` template was an author-side
lifecycle defect: the real entry point correctly rejected an open runbook that
mixed seven unchecked boxes with that heading. Before accepting activation, the
unpublished local activation commit was replaced so its non-semantic template
heading cannot be mistaken for an assembled close. The corrected first
post-activation run passed; no checker or lifecycle predicate was weakened.

The staged project-root export passed at **2,774,259 bytes / 163 files / 2
retained cycles**, exactly v0.38–v0.39, while the exact activation commit in a
detached worktree passed at **2,730,852 bytes / 160 files / 2 retained cycles**.
The **43,407-byte / 3-file** difference is the three untouched untracked
amendment inputs and their export framing; E0 owns the exhaustive partition and
Step 3 owns the mechanism. Exact activation leaves **269,148 bytes / 8.97% /
2.51 cycles** under the unchanged 3,000,000-byte ceiling at the checker-derived
+107,226-byte denominator. Two complete artifact checks match **3 artifacts /
339 pins** at **0.10 s / 0.11 s real**. The permission-complete golden pipeline
passes **11/11** with zero delta after the sandbox-denied bind was classified as
a non-result. No dependency, production source, protected byte, observation,
fixture, live wire, or remote ref moved during activation.

**v0.38 PUBLISH-V17-4 — Grant A spent exactly (measured 2026-08-04).**
The operator's initiating request issued the runbook-defined Grant A before
execution. Immediately before the ref movement, `git ls-remote` reported only
`main` at `e068cacc76685791c54ab47c84be6abbd592271d` and no v0.17.4 tag.
That commit was an ancestor of exact audit child
`a7d6c80e7e5ccd963e8ebb46ee054b30af88abb0`; local annotated object
`902d30f046c7e9f493fe3a18eefd5275ca5c5afe` peeled to exact closing commit
`f4f2690a442d7a77f1dabb53fb3a120a2c987e97`. No precondition was refuted.

One non-force branch push advanced only `origin/main` to the audit child; one
non-force tag push created only `v0.17.4`. Fresh readback resolves the branch,
annotated object, and peeled target to those three exact values. Push-triggered
run **30841505130**, attempt **1**, concluded `success`: all **9/9** blocking
identities passed, and dependency drift was the sole report-only skip. No ref
was forced, deleted, or moved beyond Grant A. The historical unpublished-local
observation remains untouched as a true dated pre-publication measurement.

- **Post-push verification date:** 2026-08-04
- **Post-push release:** `v0.17.4`
- **Post-push annotated tag object:** `902d30f046c7e9f493fe3a18eefd5275ca5c5afe`
- **Post-push closing commit:** `f4f2690a442d7a77f1dabb53fb3a120a2c987e97`
- **Post-push hosted run:** `30841505130`

**v0.38 ACTIVATE — admission cycle declared (measured 2026-08-04).** The
pre-activation entry point read the untracked v0.38 runbook as an older open
cycle and failed with exactly **7 unchecked boxes** plus **1 missing closing
record**. The explicit activation fallback therefore committed the declaration,
runbook, progress skeleton, and derived review-retention boundary before P1's
repository record, while Grant A's exact remote actions remained the first
milestone execution.

The supplied short deferral table omitted trigger-bearing subjects from the
immediately prior runbook, lacked both governed artifact byte authorities, and
assigned its non-none actions to a nonnumeric `Step W1` heading that the real
lifecycle entry point does not recognize as a discharging Step N. ACTIVATE
restores the full derived carry-forward population, both byte-identical
authorities, and the structurally equivalent `Step 2A` heading before any
semantic acceptance. Direct `cycle-check` then passed with active cycle v0.38
and open governed-export state.

Exact activation commit `e6d68c89aa1cf018c10ad289a42674350e3d7d1e`
exports at **2,596,652 bytes / 158 files / 2 retained cycles**. It retains
exactly the v0.37–v0.38 task/progress pairs, excludes both protected byte
classes, and leaves **403,348 bytes / 13.44% / 2.81 cycles** below the ceiling
at the +143,456-byte denominator. Two complete artifact checks matched both
databases and all **333** pins in **0.11 s / 0.11 s real**. The
permission-complete golden pipeline passed **11/11** with zero delta after the
sandbox-denied loopback bind was classified as a non-result. No dependency,
production source, protected byte, observation, fixture, or unauthorized ref
moved during activation.

**v0.38 REHEARSAL-COMPLETE — lifecycle clauses partitioned before wire
(measured 2026-08-04).** The admission checklist is now derived from the
protected-artifact lifecycle, configured SEC source and cadence, the hard
licensing/entitlement/robots invariants, and HC13. It is recorded clause by
clause in the active runbook with an executing fixture witness or a named
wire-only residue. The only current external facts left for Step 2A are the
live robots/terms/RSS responses, actual outbound identity and request timing,
the live feed's production-parser path, fresh database facts, current
entitlement/license results, and the admission record binding those facts to
Grant B. Recurrence, concurrency, conditional GET/304, backfill, and a second
fetch remain deferred; the rehearsal claims none of them and made no publisher
request.

The replay now exact-byte checks both v0.25 robots and terms pins. Production
robots parsing allows the configured RSS target, preserves a real publisher
denial, composes the operator deny-list, denies missing/typo policy, and rejects
a planted target-path denial. Terms consumption requires the affirmative
determination, all three reviewed pages, the monitored-contact condition, and
operator responsibility; a planted `Undetermined` value fails. The
parser-produced SEC corpus persists at **201 input / 201 kept / 0 dropped**;
finance retrieval returns a `PublisherPermitted` SEC hit with a snippet, while
a disjoint sector is empty and the unknown-license negative remains
`IndexOnly`.

A new bounded `./run harvest-sec` entry point supplies the exact Step 2A path:
artifact preflight first, fresh-only target, protected-target refusal, declared
contact required before bind, one `finance/sec-edgar-usgaap` request, strict
first-window/result checks, SQLite integrity and license facts, and
deterministic cleanup. Its structure test includes failing missing-preflight and
wrong-source mutations and proves it cannot consume an observation file. The
changed script is re-pinned at **50,378 bytes** and SHA-256
`e436d59b05f060a8ce78dd3fb23282ad99fbc8bd263abd73224978c74afeeadb`;
artifact validation and complete verification match **2 artifacts / 333 pinned
files**, with the manifest at **194,717 / 1,048,576 bytes**. Two consecutive
complete checks take **0.09 s / 0.09 s real**. The exact pre-record
project-root review export is **2,638,292 bytes / 158 files / 2 retained cycles**, leaving
**361,708 bytes / 12.06% / 2.52 cycles** at +143,456 bytes/cycle.

Focused, no-wire measurements pass SEC replay **4/4**, SEC store identity
**3/3**, compliance **40/40**, live-feature ingest **29/29**, shell
harvest/config/scheduler **14/14**, artifact fixtures **21/21**, `bash -n`,
`shellcheck`, and Rust formatting. The full permission-complete `ci-local`
passes **22/22** identities, including Python 3.11 at **371/371**, both Rust
floors, all warning gates, artifact verification, and golden **11/11** with
zero delta. A separate permission-complete Python 3.12 lane passes the identical
**371/371** population with no skips. Its earlier sandboxed attempt was a
non-result: all eight failures were explicit loopback-bind or process-inspection
permission denials. The registered scan remains **15/15 rules / 84 controls**.
No live SEC wire or fresh observation byte has yet been touched.

**v0.38 WIRE-ADMISSION — SEC EDGAR admitted under Grant B (measured
2026-08-04).** The operator's initiating Grant B authorized exactly the SEC
robots, published-terms, and configured RSS wire; dated observation-grade
writes; and admission conditional on compatibility. Evidence ran before the
harvest. One sequential request per URL used the declared contact-bearing
`intel-platform/0.17.4` identity, disabled redirect following and retries, and
respected the 0.500-second floor. Robots, terms, and RSS all returned HTTP 200
with no `Location`. Fresh robots are byte-identical to v0.25. The current terms
preserve the pinned determination's user-agent/contact, rate, responsibility,
and public-information reuse conditions. The current RSS body changes with
filings but preserves the measured **200-item** shape: title, GUID, date, link,
and description are nonempty **200/200**; author is absent **200/200**; all
GUIDs are unique and all links remain on `www.sec.gov`. DR12 passed per
artifact; no re-determination or compatibility patch occurred.

The separate production `./run harvest-sec` path consumed the live configured
feed—not an observation file—into fresh
`data/live-20260803T195324Z-37051.db`. It measured `first_window`, **200
fetched / 200 new / 200 stored**, production robots `Body(allow)` for
`/Archives/edgar/usgaap.rss.xml`, a **0.500-second** effective delay, and clean
shutdown. The archive is **253,952 bytes** at SHA-256
`fb1046b79e7501d51e2dde3fd89fb7dfe0094defa6205b12afb39a21dff06044`.
SQLite integrity is `ok`; all **200** rows are exact
`finance/sec-edgar-usgaap/PublisherPermitted`; null SimHashes and canonical ids
are **0**; noncanonical rows are **0**; distinct canonical identities are
**200**; and cursors, embeddings, and signal-history rows are all **0**.

The actual public shell/core boundary re-measured both committed subscriptions
against that archive. `acme-research`, entitled only to science and technology,
analyzed **0** documents. `quant-desk`, entitled to finance, analyzed **200**;
both responses named the correct client/sectors and reported zero
near-duplicate collapses. The sole intended entitlement movement is the named
**200-document finance addition for `quant-desk`**. No subscription, schedule,
source configuration, dependency resolution, public route/field/value domain,
or golden input changed.

The protected manifest now carries a non-retroactive initial admission record
whose exact wire hashes and operator-approval citation bind Grant B. The five
capture files plus the admission report are six new observation pins; both
artifact entry points accept **3 artifacts / 339 pinned files**. The manifest
is **200,440 / 1,048,576 bytes**, and consecutive complete checks take **0.09
s / 0.09 s real**, so neither retention trigger clause fired. This was one
manual single-source admission harvest. Recurrence, concurrency, conditional
GET/304, repeated fetch, retry/redirect behavior of the parser request, and
historical backfill remain unmeasured and unclaimed.

The first full-gate attempt truthfully failed only the on-site deferred audit:
its historical cosine measurement sorted every `artifacts[]` record and
asserted the manifest contained exactly the prior **1,764 / 2,600** document
pair, so the valid new 200-document admission produced `[200, 1764, 2600]` and
aborted before measurement. The runbook's clean-`ci-local` criterion and new
archive admission could not both fit its original scope; Step 2A therefore
records the exact author-contract correction and allows
`tools/audit_deferred.py`. The auditor now selects its two immutable historical
inputs by exact path, and a new test plants the third SEC-shaped record and
requires the same two-input selection. No receipt, disposition, protected
byte, or historical measurement changed.

The first project-root export attempt then failed before inspection because
its checker assumed exactly one SEC RSS body under `observations/**`; the new
required pin made two. The simultaneous fresh-evidence and bounded-export
criteria could not fit that original assumption, so the runbook records a
second exact author-contract correction and adds `tools/export_check.py` to
Step 2A's scope. `repomix.config.json` now registers both raw RSS bodies by
exact path. The checker derives and verifies those configured paths, rejects
wildcards, missing bytes, and non-observation targets, and a regression proves
that removing either planted capture fails. The permission-complete project-
root entry point passes at **2,766,436 bytes / 163 files / 2 retained cycles**,
leaving **233,564 bytes / 7.79% / 1.63 cycles** at the +143,456-byte
denominator. Both raw feeds remain independently pinned and outside the review
artifact; every source and evidence record stays review-visible.

The permission-complete corrected `ci-local` passes all **22/22** identities:
registered scan **15/15 rules / 84 controls**, Python 3.11 **373/373**, Rust
1.78 offline, Rust 1.86 net success, Rust 1.85 declared-floor refusal, all
warning/lint/format gates, **3/3** artifacts, and golden **11/11** with zero
delta. A separate permission-complete Python 3.12 run passes the identical
**373/373** population with no skips. The prior 370/371 shell run remains a
recorded failed attempt, not acceptance evidence.

**v0.38 RE-MEASURE — exact hosted candidate passed (measured 2026-08-04).**
The operational `run` path and executable controls moved, so Step 3 selected
hosted verification. Exact candidate
`816a0648c0dd9f4be1caad01ed3395997671cf25` first passed the complete
permission-capable local matrix at **22/22** identities, including Python 3.11
**373/373**, scan **15/15 rules / 84 controls**, both Rust floor pairs,
artifact verification, and golden **11/11**. Its separate local Python 3.12
population passed the identical **373/373** with no skips.

The required immediate `ls-remote --exit-code` returned **2** with no output
for fresh `refs/heads/codex/v0.38-evidence-816a064`. An initial push command
used an incorrect guessed full SHA behind that correct short id; both ends
reported `bad object` / `remote unpack failed`, no ref was created, and a
fresh absence check again returned **2** with no output. `git rev-parse` then
resolved the exact candidate, and one non-force push created exactly the named
ref. The rejected bad-object attempt is a non-result: no pre-existing ref was
retried, moved, or forced.

Workflow-dispatch run **30852480662**, attempt **1**, completed `success` at
the exact SHA/ref. All **9/9** blocking identities passed and persisted **9
receipts / 9 Sigstore bundles**; dependency drift was the sole report-only
skip. Both hosted shell lanes collected **373**, passed **372**, and skipped
only the named, reasoned, `on_site`
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`
node. Direct `tools/test_population.py` comparisons for Python 3.11 and 3.12
each derived `equivalent=true`, `equivalent_passed=373`, with one allowed
hosted skip. Hosted golden passed **11/11**.

Final remote readback resolves the evidence ref to the exact candidate, keeps
`main` at `a7d6c80e7e5ccd963e8ebb46ee054b30af88abb0`, and keeps the v0.17.2,
v0.17.3, and v0.17.4 annotated objects unchanged. No tag, publication ref,
workflow byte, dependency, protected byte, publisher wire,
entitlement/licensing outcome, or public response domain moved.

**v0.38 R-CLOSE release-parent preparation (measured 2026-08-04).** DR13
selects patch **v0.17.5**. The dependency-free release-baselined domain check
and the installed FastAPI runtime comparison each pass at **6 routes / 31
status-media response variants / 112 recursive field occurrences**, with
**0 differences** from v0.17.4. Admission enables bounded harvesting of the
already-configured SEC source and adds the intended 200-document finance
result for `quant-desk`; it adds no route, response field, field type, or
serialized `/v1/*` field-domain value. No subscription configuration or
license-enum semantic changes. DR13's minor clause does not fire.

The release parent moves all five executable authorities to **0.17.5**:
`apps/cored/Cargo.toml`, `shell/intel_shell/__init__.py`,
`shell/intel_shell/app.py`, this State header, and `CHANGELOG.md`. README's
three current restatements move with them, and Cargo changes only cored's
lockfile package value. The release parent remains untagged. Its immediate
child will carry the checked closing record; only that child becomes the local
annotated-tag target, followed immediately by the required closing-export
audit child. Direct local and remote checks found no v0.17.5 tag before this
preparation. Remote `main` remained exact published v0.17.4 audit child
`a7d6c80e7e5ccd963e8ebb46ee054b30af88abb0`; DR14 authorizes no publication.

**v0.38 R-CLOSE — v0.17.5 patch release closed locally (measured
2026-08-04).** Release disposition: release (as of 2026-08-04). Untagged
release commit `37f552c0c326098bdcf8f19de7eac19670d74680` is the immediate
parent of the checked closing record. DR13 selects patch because SEC admission
enables bounded harvesting of the already-configured source and adds the
intended 200-document finance result for `quant-desk`, while the dependency-
free domain derivation and installed FastAPI comparison each report **0
differences** across **6 routes / 31 status-media response variants / 112
recursive field occurrences**. No route, response field, field type, or
serialized `/v1/*` field-domain value moves, so the minor clause does not fire.

`version-check` derives **0.17.5** from all five executable authorities and
reports **3** offline-MSRV pins, **22** current offline-MSRV restatements, and
**3** current release restatements. Exact evidence candidate
`816a0648c0dd9f4be1caad01ed3395997671cf25` and hosted run `30852480662`,
attempt 1, passed **9/9** blocking identities with **9 receipts / 9 Sigstore
bundles**. Both release-parent shell lanes pass **373/373**, both hosted
populations derive equivalent **373**-test results with one named, reasoned
`on_site` skip, and hosted and local golden pass **11/11**.

The exact release-parent export is **2,781,281 / 3,000,000 bytes** across 163
files with two retained cycles. It retains exactly v0.37–v0.38, excludes both
protected raw RSS bodies and all structural archives, and leaves **218,719
bytes / 7.29% / 2.04 cycles** at the latest positive +107,226-byte adjacent-
cycle denominator. The assembled closing State is **129,970 /
453,741 bytes**. The manifest remains **200,440 / 1,048,576 bytes**, leaving
**848,136 bytes**; the latest timed verification pair is **0.09 s / 0.09 s**.
The release-parent local gate passes all **22/22** jobs, including **15/15
rules / 84 controls**, both shell lanes, all **3 artifacts / 339 pins**, and
embedded golden **11/11**.

Publication of v0.17.4 reset the publication-epoch count to **0**. v0.38 is
the first subsequent closed cycle with a measured runtime-behavior difference,
so the consecutive count becomes **1**. R15 reports no public-surface change;
neither the three-cycle nor immediate trigger fires, and an unpublished local
close does not reset the epoch. Every active deferral row carries its latest
dated v0.38 observation. Direct local and remote pre-close checks found no
v0.17.5 tag and kept remote `main` exact at the published v0.17.4 audit child.
No push, remote `main` movement, or release-tag publication is authorized or
performed. The closing record contains no tag-object field; its local annotated
tag is created only after that commit exists, and the immediate audit child
records the measured closing-tree export before handoff.

- **Publication observation date:** 2026-08-04
- **Publication observation release:** `v0.17.5`
- **Publication observation status:** `unpublished-local-close`
- **Publication observation remote:** `origin`
- **Publication observation tag ref:** `absent`

**v0.38 closing-export audit child (measured 2026-08-04).** Local annotated
tag object `946bdc015446182727d8f705697e378f8fe8f7eb` peels to closing
commit `55045ae481ce8d1ef285522b3c0a57c91fe5cb54`, whose immediate parent is
exact release commit `37f552c0c326098bdcf8f19de7eac19670d74680`. The project-root
export of that closing commit passed at **2,798,114 bytes / 163 files / 2
retained cycles**, a truthful **+16,833-byte** difference from the closing
tree's 2,781,281-byte governed release-parent field. This append-only child is
the immediate next commit after the tag target and the final v0.38 commit; it
does not predict its own content-addressed id, move any remote ref, or defer the
audit to publication.

**v0.38 E0 — entering-state reconstruction (measured 2026-08-04).** The seven
runbook rows were treated as hypotheses and checked at their real entry points.
H1's local graph is confirmed: release parent
`514bec6c95e47017fafab452775ac4b8824ca6b9` has parent
`11cad3c22f1eebb8bb838389d8f7e75abfd9426d`; closing commit
`f4f2690a442d7a77f1dabb53fb3a120a2c987e97` has the release parent as its
immediate parent; and audit child
`a7d6c80e7e5ccd963e8ebb46ee054b30af88abb0` has the closing commit as its
immediate parent. Annotated object
`902d30f046c7e9f493fe3a18eefd5275ca5c5afe` peels to that closing commit,
and `e068cacc76685791c54ab47c84be6abbd592271d` is an ancestor of the audit
child. Grant A truthfully superseded H1's remote half: immediately before P1,
remote `main` was `e068cacc…` and v0.17.4 was absent; fresh E0 readback is
`main=a7d6c80e…`, tag object `902d30f0…`, and peeled target `f4f2690a…`.

H2 is partly refuted after publication. Before this E0 record, `STATE.md` is
**110,556 / 453,741 bytes**, not 107,454. Structural archive
`docs/state-archive/STATE-through-v0.35.md` is confirmed at **258,658 bytes**
and SHA-256
`fb1114f68755cbb8fc5d1fdad9e2ec114bf2604871102fa84d280f2bc90191a7`,
matching its manifest pin. State now contains **3** complete post-push records,
not 2, plus the same **3** truthful historical unpublished-local observations;
the v0.17.4 post-push record now takes precedence over its historical absence
observation. The manifest is **193,830 / 1,048,576 bytes**, and complete
verification matches **2 artifacts / 333 pinned files**.

H3 is corrected at the measured units. The live registry passes **15 rules /
84 planted controls**, with **9** checklist exemptions and **3** historical
retractions. Before E0's box was checked, the checklist population was **297
checked / 288 matched / 288 resolved / 9 exemptions**, not 295/286+9. The
v0.17.4 response-domain baseline is exact **47,135 bytes** over **6 routes /
31 status-media response variants / 112 recursive field occurrences**;
`domain_manifest.py check` passes. H4 is confirmed: `config/core.json` names
`sec-edgar-usgaap`, exact real RSS URL
`https://www.sec.gov/Archives/edgar/usgaap.rss.xml`, license
`PublisherPermitted`, and `robots_on_missing=deny`. All four substantive v0.25
observation pins plus their directory `.gitattributes` match, and the focused
shipped-parser replay passes **3/3** over the pinned RSS body.

H5 remains deliberately unmeasured until Step 2 derives the admission clauses;
E0 does not convert fixture evidence into wire evidence or predeclare that
partition. H6 is refuted: `config/schedule.json` already schedules both
`filings-digest=7200` and `sec-edgar-usgaap=600` for `quant-desk`. Step 2A
therefore must not edit the schedule merely to enable SEC; it must exercise the
already-scheduled source through the normal fresh path and append the required
admission record. H7 is refuted by the exact activation-tree export:
**2,596,652 bytes / 158 files / 2 retained cycles**, leaving **403,348 bytes /
13.44% / 2.81 cycles** at +143,456 bytes/cycle. The derived retention boundary
excludes through v0.36 and retains exactly v0.37–v0.38, not through v0.35.

The standing entering gate passed with no stop. Initial porcelain named exactly
the three historical untracked amendment inputs, all still untouched. Full
permission-complete `./run ci-local` passed **22/22** identities. It executed
the registered self-test at **15/15 rules / 84 controls**, the Rust 1.78
offline lanes, the Rust 1.86 net success and Rust 1.85 declared-MSRV refusal,
Python 3.11 at **370/370**, SEC replay at **3/3**, artifact verification, and
golden at **11/11**. A separate Python 3.12 run collected the identical
**370/370** population with no skips. `version-check` derives **3** executable
offline pins at 1.78, **22** offline-floor current restatements, and **3**
release-version restatements at 0.17.4 across the classified **579** tracked
files. No dependency, protected byte, golden input, entitlement/licensing
outcome, production source, fixture, observation, or unauthorized ref moved.

**v0.37 PUBLISH — v0.17.2 and v0.17.3 published exactly under DR7
(measured 2026-08-03).** Immediately before the one-time grant was spent,
`git ls-remote origin refs/heads/main refs/tags/v0.17.2
'refs/tags/v0.17.2^{}' refs/tags/v0.17.3 'refs/tags/v0.17.3^{}'`
reported only `main` at
`f02379f03ccdfd1b019413234f2ad014d169fb04`; both tag refs were absent.
`git merge-base --is-ancestor f02379f03ccdfd1b019413234f2ad014d169fb04
e068cacc76685791c54ab47c84be6abbd592271d` exited **0**. Local object
inspection matched annotated objects
`16ee7bcb2214859156edbceeb5e314ac1a67f39b` and
`0fe42d7a6a86e94bb95a93a86b7a4b09917b97f4`, peeling respectively to
`9996c6820d720160b64607575d0270d2e5393ef9` and
`a5afab9e6842a1b6c00a7d17fdeaa3e254edf80f`. No DR7 precondition was
refuted.

The repository-order measurement took the declared fallback. Before activation,
direct `cycle-check` read the untracked v0.37 runbook as an older open cycle and
failed with exactly **8 unchecked boxes** plus **1 missing closing record**.
Activation commit `5884ef7754431ffe5017dc1f2fde5902aef2ed52` therefore landed
before this repository append, and PUBLISH remained the first active step.
After activation and the four fresh v0.37 governed-row observations, direct
`cycle-check` passed on the real published path.

The post-implementation call-chain audit refuted PUBLISH's stronger
dual-release checker claim. `check_publication_status()` calls
`newest_closed_release()` once and reconciles only the returned release; its
real success report names `release=v0.17.3` and does not read the older
v0.17.2 post-push record. The v0.17.2 record is structurally complete and its
object/target fields independently equal the fresh `ls-remote` result, but the
stated `cycle-check`-for-both acceptance is **not measured**. This is an
author-side acceptance refutation, not a false published record: the exact
remote facts remain true and immutable. PUBLISH stops only this control claim
and defers historical multi-release reconciliation; the remaining cycle work
is unaffected under §2's continue-unaffected-work rule.

The non-force branch push advanced only `origin/main` from `f02379f…` to
`e068cacc…`; the subsequent non-force tag push created only `v0.17.2` and
`v0.17.3`. A fresh `ls-remote` then resolved all five direct/peeled ref facts
to the granted objects. Push-triggered hosted run **30824053490**, attempt
**1**, on exact `e068cacc76685791c54ab47c84be6abbd592271d` completed with
conclusion **success** and passed all **9** blocking job identities. This
publication makes the v0.35 and v0.36 closing records published history; no
ref was forced, deleted, or moved beyond DR7's exact three-ref grant.

- **Post-push verification date:** 2026-08-03
- **Post-push release:** `v0.17.2`
- **Post-push annotated tag object:** `16ee7bcb2214859156edbceeb5e314ac1a67f39b`
- **Post-push closing commit:** `9996c6820d720160b64607575d0270d2e5393ef9`
- **Post-push hosted run:** `30824053490`

- **Post-push verification date:** 2026-08-03
- **Post-push release:** `v0.17.3`
- **Post-push annotated tag object:** `0fe42d7a6a86e94bb95a93a86b7a4b09917b97f4`
- **Post-push closing commit:** `a5afab9e6842a1b6c00a7d17fdeaa3e254edf80f`
- **Post-push hosted run:** `30824053490`

**v0.37 E0 — entering-state reconstruction (measured 2026-08-03).** The
runbook's nine source-review figures were treated as hypotheses and checked
against the repository and remote, not copied forward. H1, H3, H7, H8, and H9
were confirmed; H4 and H6 were refuted; H2 was confirmed for its entering DR7
measurement and then superseded by the exact publication result; H5 was partly
confirmed and otherwise refuted by commit-exact exports.

The object graph is exact: release parent
`9946cedae75d99c53d17a6f8b5507d10cb9bd959` is the immediate parent of closing
commit `a5afab9e6842a1b6c00a7d17fdeaa3e254edf80f`; annotated tag object
`0fe42d7a6a86e94bb95a93a86b7a4b09917b97f4` peels to that closing commit; and
audit child `e068cacc76685791c54ab47c84be6abbd592271d` has the closing commit as
its immediate parent. Immediately before PUBLISH, `main` was exact
`f02379f03ccdfd1b019413234f2ad014d169fb04`, that commit was an ancestor of
the audit child, and both tags were absent. E0's fresh post-publication
measurement instead finds `main` at the audit child and both annotated tag
objects and peeled targets exact; it does not preserve the stale "tags absent"
half of H2 as current state.

The entering `DisposableDir::create` combined process id with nanoseconds and
called `create_dir(...).expect(...)`. A test-only forced seam pre-created the
exact candidate for nonce `u128::MAX`; the constructor then produced the
caught `AlreadyExists` panic deterministically and the focused test passed
**1/1**. This confirms H3 without changing production code and supplies the
fail-before witness for TEST-ISOLATION.

The live invariant registry is **14 rules / 81 controls**, with **9** active
checklist exemptions and **3** historical retractions. The pre-E0 checklist is
**289 checked / 3 retracted / 280 matched / 280 resolved / 9 exemptions**, not
H4's **287 / 3 / 278+9**. The v0.35 task/progress pair is exactly
**78,419 + 69,632 = 148,051 bytes**, but commit-exact export measurements are
**2,858,294 bytes / 151 files / 2 retained cycles** at entering audit child
`e068cacc…` and **2,746,484 / 151 / 2** at activation commit `5884ef77…`.
The earlier **2,901,790 / 154** source-review figure described a worktree that
also contained the three untracked amendment inputs, not a delivered commit.
The arithmetic estimate **2,753,739** is therefore **7,255 bytes** above the
exact activation result; H5 is only partly confirmed.

Before this E0 record was added, `STATE.md` measured **345,139 bytes**, not
H6's **342,163**. The literal
`STATE_ARCHIVE_PERMANENT_TAIL:START` occurs exactly once and the two historical
publication-absence observations remain, but PUBLISH has also added two exact
post-push records. The six public route decorators — `/v1/signals`,
`/v1/search`, `/v1/brief`, `/v1/ask`, `/v1/billing/webhook`, and
`/v1/billing/stripe` — are all in `shell/intel_shell/app.py`. Runtime FastAPI
introspection finds exactly **6** such routes and every route has
`response_model=None`; five handlers return raw dictionaries and `brief`
returns `PlainTextResponse`. C8 therefore selects the response-model
introduction path. `.github/workflows/ci.yml` lines 19–21 still trigger on a
push to `main`, confirming H8 without a workflow edit.

H9's arithmetic is confirmed. Using the measured v0.36 governed-field growth
of **143,456 bytes**, a **2,600,000-byte** post-archive export leaves
**400,000 bytes**, or **2.79 cycles**, under the **3,000,000-byte** ceiling.
The minimum **2.5-cycle** reserve is **358,640 bytes**, so any export at or
below **2,641,360 bytes** satisfies C10.

The standing entering gate also passed. `git status --porcelain` named exactly
the three untracked amendment inputs before the test-only reproduction was
written; those inputs remain untouched. Permission-complete `./run ci-local`
passed all **22/22** identities: the registered scan passed **14/14 rules / 81
controls**, the default and Rust 1.78 store identity lanes each passed **3/3**
including the reproduction, net tests passed **29 ingest / 3 replay / 30
cored**, the Rust 1.86 success and Rust 1.85 declared-MSRV refusal lanes both
held, clippy and rustfmt were clean, artifact verification matched **2
databases / 332 pinned files**, and golden passed **11/11** with zero delta.
The permission-complete Python 3.11 and 3.12 lanes each passed **368/368** with
the one accepted `StarletteDeprecationWarning` and identical machine-readable
populations. The first Python 3.12 attempt was a sandbox-denied non-result
(two loopback binds and `ps`); the identical authorized rerun is the recorded
pass. No E0 gate, architecture, dependency, protected-byte, or golden stop
condition fired.

**v0.37 TEST-ISOLATION — identity scratch directories are collision-proof by
construction (measured 2026-08-03).** The test-only `DisposableDir` still uses
the process id and clock-derived nonce as its candidate prefix, but atomic
`create_dir` now appends a monotonically increasing attempt component and
retries only `AlreadyExists`. Every other filesystem error remains an immediate
failure. The executable witness pre-creates attempt zero for a fixed nonce and
proves the same constructor succeeds at attempt one; the focused control passed
**1/1**.

The complete `intel-store` test suite ran under default parallelism **10
consecutive times**. Every repetition passed **24 unit tests + 1 license test +
3 identity-measure tests + 0 doctests**, including the parser-produced SEC
measurement, with **0** `AlreadyExists` failures. The mechanism is std-only,
adds no dependency, and changes no production source: the entire implementation
remains in `crates/store/tests/sec_identity_measure.rs`. The final golden
pipeline passed **11/11** with zero delta; no task gate or stop condition fired.

**v0.37 STATE-ARCHIVE — current epoch plus one prior retained (measured
2026-08-03).** C10's semantic boundary keeps the current v0.37 publication
epoch, the immediately prior v0.36 body, and the permanent numbered tail in
live State; the cut therefore begins at v0.35 rather than at a selected line
number. Historical bodies v0.29 through v0.35 moved byte-for-byte to
`docs/state-archive/STATE-through-v0.35.md`. The pre-cut State was **350,925
bytes** at SHA-256
`7db0bc5ff34b35da174805914c1725248357b746d7f0783e16d5264ee7cf5cf5`.
Its exact components were **48,303-byte retained prefix + 258,658-byte archive
+ 43,964-byte permanent tail**. Concatenating those components reproduced all
**350,925 bytes** and the same SHA-256; the post-cut, pre-record live complement
was **92,267 bytes**.

The new archive is pinned at structural grade, SHA-256
`fb1114f68755cbb8fc5d1fdad9e2ec114bf2604871102fa84d280f2bc90191a7`,
and **258,658 bytes**. The exact-path validator registry admits this path and
no prefix; its focused schema suite passed **20/20**, including rejection of an
unregistered sibling. This required one pre-implementation gate correction:
the supplied scope forbade `tools/evidence_artifacts.py` while DR8 required a
new exact registry member. The active scope now permits only this bounded
registry/control change. Manifest schema v2 validates **2 artifacts / 333
pinned files** at **193,830 bytes**. Two complete verifications matched the new
archive, the prior archive, all other pins, and both protected databases in
**0.09 s / 0.10 s real**; neither the 1 MiB nor two-run 1.00-second trigger
fired.

The final project-root delivered worktree export is **2,558,258 bytes / 154
files / 2 retained cycles**, exactly v0.36–v0.37, with both excluded protected
byte classes absent. It is **41,742 bytes** below C10's 2,600,000-byte target
and leaves **441,742 bytes / 14.72% / 3.08 cycles** under the 3,000,000-byte
ceiling at the measured +143,456-byte v0.36 denominator. The permanent-tail
marker remains at column zero exactly once; both post-push records, all v0.37
and v0.36 bodies, the publication header, and every State field parsed by the
lifecycle/version controls remain live. `cycle-check`, manifest validation,
artifact verification, and the focused validator suite pass; no protected
database, observation-grade byte, dependency, production path, payload, or
accepted boundary moved.

The exact implementation commit
`882c698d607b9a36c253c0f3b0a316772063c90b`, measured without the three
untracked amendment inputs, exports **2,514,762 bytes / 151 files / 2 retained
cycles**. That governed baseline is **85,238 bytes** below C10's target and
leaves **485,238 bytes / 16.17% / 3.38 cycles** at the standing denominator.

**v0.37 DOMAIN-MANIFEST — public response domains are derived and guarded
(measured 2026-08-03).** C8 selected the model-introduction branch after E0
found `response_model=None` on all six public routes. The shipped shell now
uses explicit Pydantic serialization authorities for `/v1/signals`,
`/v1/search`, `/v1/brief`, `/v1/ask`, `/v1/billing/webhook`, and
`/v1/billing/stripe`, including their declared error variants. The new
`tools/domain_manifest.py` dependency-freely reads the actual route-decorator
and Pydantic-annotation AST, requires a response model and declared errors on
every member of that exact route set, and recursively records fields,
requiredness, primitive and container types, nullability, object openness, and
literal values. The installed shell population separately requires that result
to equal the actual FastAPI OpenAPI document, including the pinned native 422
domain. The v0.17.4 baseline is **47,135 bytes**, covers **6 routes / 31
status-media variants / 112 field occurrences**, and both its fresh source
derivation and runtime comparison have **0 differences**.

Registered R15 executes that same entry point. Its unmutated scan passed, and
its three control-site mutations independently proved rejection of an added
`Signal.kind` enum value, removal of `SignalsResponse.graph`, and conversion
of `SearchHit.rank` from number to string. The complete scan passed **15/15
rules / 84 controls**. The response-model syntax also exposed a stale
single-line-decorator assumption in the source-deterministic deferred audit;
that tool now locates the real FastAPI decorators through the Python AST, and
the three affected receipt-rederivation tests pass under both supported Python
versions.

The complete configured-subscription witness exercised all six routes as both
configured subscribers where applicable, producing **10 successful response
records**. Its canonical envelope is byte-identical before and after model
introduction at **6,869 bytes**, SHA-256
`dfec8ff81d68526dd5468ce22660be9d7678c6a8fdd8e52d6ac921c83371cef3`.
Permission-complete Python 3.11 and 3.12 each passed the identical **370/370**
collected population with no skips and the one accepted
`StarletteDeprecationWarning`. The authoritative golden pipeline passed
**11/11** with zero delta. Exact hosted evidence run **30834599847**, attempt
**1**, subsequently passed all **9/9** blocking identities on the audited
v0.37 candidate. The native OpenAPI description now makes the
already-serialized field/domain contract explicit, but no `/v1/*` route,
response byte, field name, field domain, entitlement, licensing outcome,
dependency, or protected artifact moved. DR9 clause 2 therefore has an
executed zero-diff input; no §3.4 stop condition fired.

**v0.37 RE-MEASURE first candidate — pre-install invariant dependency found
(measured 2026-08-03).** The fresh evidence ref
`refs/heads/codex/v0.37-evidence-2e5921f` was absent immediately before one
non-force push created it at exact audited candidate
`2e5921f0d0d3f4d64bde56b95325216d33caa59b`; remote `main`, v0.17.2, and
v0.17.3 remained exact. Workflow-dispatch run **30832624982**, attempt **1**,
then passed **8/9** blocking identities and failed only Python 3.11's
pre-install `registered static repository invariants` step. Its actual entry
point reached R1–R14, then R15's subprocess exited **1** with no parseable
manifest difference because importing the FastAPI app before the workflow's
install step could not load its third-party packages. Python 3.12 intentionally
does not run the pre-install invariant phase and later passed its installed
**370-test** population; the other eight blocking identities, including
golden, Rust floors, net, core, and lint, passed. This is a real topology
finding, not a retryable hosted transient.

R15 now has two executed phases matching that topology. Its blocking check is
dependency-free: Python AST derivation reads the actual route decorators and
Pydantic type annotations, including declared errors and the pinned native 422
domain. The installed population separately requires that source derivation
to equal FastAPI's runtime OpenAPI result. A Python 3.11 `-S` run, with site
packages disabled, passed the full **15/15 rules / 84 controls**; the installed
runtime comparison passed at **6 routes / 112 field occurrences**, and the
focused payload/runtime test passed under Python 3.11 and 3.12 without changing
the **370-test** population. The failed evidence ref remains immutable and no
run was retried; RE-MEASURE remains open until a fresh candidate/ref completes
all nine identities.

**v0.37 RE-MEASURE — fresh audited candidate passed 9/9 (measured
2026-08-03).** After the topology repair and its separate audit record, exact
candidate `99012c86dcdda8ea32f1b1afa016f793118e9087` passed the complete
permission-capable local matrix at **22/22** jobs. The first sandboxed matrix
attempt was a measured non-result only at the live-client loopback-bind test;
the identical permission-complete run passed the net suite, Rust 1.78 and net
1.86 lanes, the expected locked-graph Rust 1.85 refusal, all **15/15 rules / 84
controls**, Python 3.11 at **370/370**, golden at **11/11**, every protected
artifact, and the append-only progress check.

Fresh ref `refs/heads/codex/v0.37-evidence-99012c8` was absent immediately
before one non-force push created it at that exact candidate. The pre-push and
final readbacks kept remote `main` exact at
`e068cacc76685791c54ab47c84be6abbd592271d`, v0.17.2 tag object/target exact at
`16ee7bcb2214859156edbceeb5e314ac1a67f39b` /
`9996c6820d720160b64607575d0270d2e5393ef9`, and v0.17.3 exact at
`0fe42d7a6a86e94bb95a93a86b7a4b09917b97f4` /
`a5afab9e6842a1b6c00a7d17fdeaa3e254edf80f`. The failed first-candidate ref
also remained exact at `2e5921f0d0d3f4d64bde56b95325216d33caa59b`; no ref was
reused, forced, deleted, or repurposed.

Workflow-dispatch run **30834599847**, attempt **1**, completed `success` at
the declared SHA/ref. All **9/9** blocking identities passed and persisted
**9 receipts / 9 Sigstore bundles**; dependency drift was the only declared
report-only skip. The run was dispatched once and not retried. The repository
comparator independently derived both supported Python populations: local
3.11 and 3.12 each passed **370/370**; each hosted lane collected **370**,
passed **369**, and skipped only
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`,
with its explicit `on_site` marker and protected-corpus reason. Both
comparisons reported `equivalent=true` and `equivalent_passed=370`. Hosted and
local golden remained **11/11**. No workflow, dependency, protected byte,
publisher wire, entitlement/licensing outcome, public value domain, release
ref, or publication authority moved; Step 5's condition is fully discharged.

**v0.37 R-CLOSE release-parent preparation (measured 2026-08-03).** DR9
selects patch **v0.17.4**. DOMAIN-MANIFEST's complete configured witness is
byte-identical at **6,869 bytes**, SHA-256
`dfec8ff81d68526dd5468ce22660be9d7678c6a8fdd8e52d6ac921c83371cef3`,
and the release-baselined manifest has **0 differences** across **6 routes / 31
status-media variants / 112 field occurrences**. Explicit response models make
the already-serialized contract visible in native OpenAPI, but no `/v1/*`
route, named runtime surface, response payload byte, field, field-domain value,
entitlement, or licensing outcome moves. Neither DR9 minor clause fires.

The release parent moves all five executable authorities to **0.17.4**:
`apps/cored/Cargo.toml`, `shell/intel_shell/__init__.py`,
`shell/intel_shell/app.py`, this State header, and `CHANGELOG.md`. README's
three current restatements move with them, and Cargo changes only cored's
lockfile package value. The release parent remains untagged. Its immediate
child will carry the checked closing record; only that child becomes the local
annotated-tag target, followed immediately by the required closing-export
audit child. Direct local and remote checks found no v0.17.4 tag before this
preparation, and DR10 authorizes no publication.

**v0.37 R-CLOSE — v0.17.4 patch release closed locally (measured
2026-08-03).** Release disposition: release (as of 2026-08-03). Untagged
release commit `514bec6c95e47017fafab452775ac4b8824ca6b9` is the immediate
parent of the checked closing record. DR9 selects patch because explicit
response models and the release-baselined manifest expose and validate the
already-serialized contract without adding a route or observable named
runtime surface. The complete configured witness remains byte-identical at
**6,869 bytes**, SHA-256
`dfec8ff81d68526dd5468ce22660be9d7678c6a8fdd8e52d6ac921c83371cef3`,
and the manifest reports **0 differences** across **6 routes / 31 status-media
variants / 112 field occurrences**. No response payload byte, field, or
serialized `/v1/*` value-domain value moves, so neither DR9 minor clause fires.

`version-check` derives **0.17.4** from all five executable authorities and
reports **3** offline-MSRV pins, **22** current offline-MSRV restatements, and
**3** current release restatements. Exact evidence candidate
`99012c86dcdda8ea32f1b1afa016f793118e9087` and hosted run `30834599847`,
attempt 1, passed **9/9** blocking identities with **9 receipts / 9 Sigstore
bundles**. Both local shell lanes pass **370/370**, both hosted populations
derive equivalent **370**-test results with one named, reasoned `on_site` skip,
and hosted and local golden pass **11/11**.

The exact release-parent export is **2,674,055 / 3,000,000 bytes** across 158
files with two retained cycles. It retains exactly v0.36–v0.37, excludes both
protected byte classes, and leaves **325,945 bytes / 10.86% / 2.27 cycles** at
the latest positive +143,456-byte adjacent-cycle denominator. STATE-ARCHIVE's
delivered baseline met C10 at **2,558,258 bytes**; subsequent manifest,
evidence, and closing records put the release parent **74,055 bytes** above
that step target without firing the architectural ceiling. The assembled
closing State is **106,707 / 453,741 bytes**. The manifest remains
**193,830 / 1,048,576 bytes**, leaving **854,746 bytes / 842.11 cycles** at
+1,015 bytes/cycle. The release-parent local gate passes all **22/22** jobs,
including **15/15 rules / 84 controls**, both shell lanes, all **333** pins,
both protected databases, and embedded golden **11/11**.

This close remains in v0.17.3's publication epoch at divergence count **0**:
there is no measured runtime-behavior or public-surface difference to start a
new count, and an unpublished local close does not reset the epoch. Every
active deferral row carries its latest dated v0.37 observation. Direct local
and remote pre-close checks found no v0.17.4 tag. No push, remote `main`
movement, or release-tag publication is authorized or performed. The closing
record contains no tag-object field; its local annotated tag is created only
after that commit exists, and the immediate audit child records the measured
closing-tree export before handoff.

- **Publication observation date:** 2026-08-03
- **Publication observation release:** `v0.17.4`
- **Publication observation status:** `unpublished-local-close`
- **Publication observation remote:** `origin`
- **Publication observation tag ref:** `absent`

**v0.37 closing-export audit child (measured 2026-08-03).** Local annotated
tag object `902d30f046c7e9f493fe3a18eefd5275ca5c5afe` peels to closing
commit `f4f2690a442d7a77f1dabb53fb3a120a2c987e97`, whose immediate parent is
exact release commit `514bec6c95e47017fafab452775ac4b8824ca6b9`. The project-root
export of that closing commit passed at **2,689,149 bytes / 158 files / 2
retained cycles**, a truthful **+15,094-byte** difference from the closing
tree's 2,674,055-byte governed release-parent field. This append-only child is
the immediate next commit after the tag target and the final v0.37 commit; it
does not predict its own content-addressed id or defer the audit to publication.

**v0.36 AUTONOMY stop-and-report (measured 2026-08-03).** The runbook's
pre-activation ordering was attempted first. `ci-local` rejected a v0.36 task
path while v0.35 remained declared and treated the new runbook as an incomplete
older cycle, so the explicit Step 0e exception was taken. Activation landed as
implementation `f44681c1dce0c5c2efc0d3fb4a30900fdb4163f5` with audit record
`8c798cd`. The declared retention set is exactly v0.35–v0.36, and the
permission-complete activation golden run passed **11/11**.

The Step 0 experiment then generalized R6 from its one hard-coded authority
name to the derived union of marker names. Before the Operations mirror was
added, the real scan failed on missing `CYCLE_AUTONOMY_AUTHORITY` START/END
markers. With the exact mirror present, the focused test and full self-test
passed **12/12 rules / 74 controls**, including a planted missing-START control.
Two consecutive artifact checks matched all **332** pins and both protected
databases in **0.12 s / 0.13 s real**; `run` remained exactly **45,409 bytes**
at its authorization-grade hash. Project-root `export-check` passed at
**100 derived / 7 required / 152 exported / 2,724,915 bytes / 2 retained
cycles**, exactly v0.35–v0.36, with both protected byte classes excluded.

The exact acceptance entry point `./run ci-local`, run with normal loopback and
process-inspection permissions, passed release-version consistency and then
stopped at active-cycle consistency with exactly two defects:

1. `AGENTS.md:635: stale/cycle-specific task path
   'TASKS-v0.36-EXECUTION.md' appears outside the active declaration`. The
   runbook simultaneously requires the marker block verbatim, including that
   literal, while the existing `check_contract_cycle_paths` rule rejects every
   cycle-specific task path below AGENTS §0.
2. `STATE.md: publication post-push record required: expected exactly one
   complete record for v0.17.2; found 0`. Local annotated tag `v0.17.2` points
   at closing commit `9996c6820d720160b64607575d0270d2e5393ef9`; activation makes
   HEAD its descendant, so the current R-CLOSE checker requires the record that
   the contract defines as post-publication. The tag is explicitly unpublished,
   no hosted publication run exists, and publication is the runbook's retained
   ask-first gate.

This is the runbook's stop-and-report condition for an instruction that cannot
be executed without violating another instruction. No post-push record was
fabricated, the local release tag was not deleted, publication was not
performed, the verbatim block was not weakened, and the scope-forbidden
`tools/cycle_check.py` was not changed. The unaccepted Step 0 implementation
was restored; its checkbox remains open. The restored standing self-test passes
**12/12 rules / 73 controls**, manifest schema validation passes for **2
artifacts / 332 pinned files**, and the post-restore golden pipeline passes
**11/11** with zero delta. The operator-supplied amendment remains untracked
and untouched. Because the runbook says everything requires Step 0 complete,
E0 and Steps 2–7 were not started.

**v0.36 A1r2 author-side correction (measured 2026-08-03).** Amendment
application commit `6a3c108dd19378549a503c220c8917c7b34055ea` changes only the
active runbook. It replaces the stale cycle-specific authority text, adds
Step 1A's truthful unpublished-local-close lifecycle objective, removes the
forbid-before-allow scope contradictions, records H11–H13, and gates every
later step on Step 1A. The two amendment inputs remain untracked and untouched.

The real post-amendment `cycle-check` now reports exactly the one expected
interim defect: the absent v0.17.2 post-push record. It reports no authority
literal, declared-scope, amendment-disclosure, trigger-freshness, retention, or
artifact-boundary defect. This is the amendment's deliberate A4 state until
Step 1A changes the lifecycle predicate; it is not accepted as a clean close.
The amendment-only golden run passed **11/11** with zero delta. No production
source, protected byte, dependency, tag, or remote ref changed. Corrected Step
0 is therefore reopened and runs next; this forward correction does not alter
the truthful earlier stop-and-report measurement.

**v0.36 corrected AUTONOMY completion (measured 2026-08-03).** The corrected,
cycle-neutral authority block is present exactly once in `AGENTS.md` and once
in `docs/intel-platform-OPERATIONS.md`. Generalized R6 derives both authority
names from the documents, requires one ordered START/END pair in each, and
compares corresponding inclusive blocks byte-for-byte. Its real missing-START
mutation and existing mismatch mutation both fail; the full registered scan
passes **12/12 rules / 74 controls**. The adjacent operator-local clarification
states that the term names the execution environment rather than the executing
party. `run` did not change and remains **45,409 bytes** at its existing
authorization-grade pin.

The contract-path regex found exactly two task-runbook literals, at AGENTS
lines **16–17**, both above the `## 0.` boundary at line **25**; the authority
block contributed zero matches. Direct `cycle-check` reported exactly one
defect, the deliberately pending absent v0.17.2 post-push record, and no
authority, scope, amendment, trigger, retention, or artifact-boundary defect.
This is A1r2's explicit interim state until Step 1A; no publication field was
fabricated and no tag or remote ref moved.

All **22/22** `ci-local` identities were exercised individually. Version
consistency, invariant self-test, deferred evidence, Python byte-compile,
ShellCheck, workspace check/test, net check/test, net 1.86 floor success, net
1.85 refusal, clippy, rustfmt, Rust 1.78 check/test, shell pytest, golden,
protected artifacts, persisted fingerprints, and progress-check passed. The
permission-complete Python 3.11 lane passed **366/366** with the one accepted
`StarletteDeprecationWarning`; the golden pipeline passed **11/11**. The first
net-test attempt was an environment-denied loopback-bind non-result; the same
lane with loopback permission passed **29** ingest tests, **3** SEC replay
tests, and **30** cored tests. Artifact verification matched **332** pinned
files and both protected databases.

Two identities did not pass, and neither was hidden. Direct `cycle-check` has
the one expected Step 1A lifecycle defect above. `checklist-audit` reported the
ACTIVATE box unmatched even though its progress entry exists: the entry's
qualified `runbook` value is the repository-relative path, while the auditor
compares that value with the runbook basename. This is a measured G2/G4/G5
instance owned by Step 2; repairing it during AUTONOMY would violate task
ordering. No identity was omitted. The current project-root export passes its
real-byte, retained-set, and exclusion controls at **153 files / 2 retained
cycles**; its exact byte figure is recorded in the governed Architecture row
after the final Step 0 worktree measurement.

**v0.36 E0 entering-state reconstruction (measured 2026-08-03).** Every H1–H13
hypothesis was executed. H2–H6 and H10–H13 were confirmed; H1, H8, and H9 were
refuted in part or whole; H7's previously unknown answer is now measured. The
complete dated verdict table lives in the active runbook and is summarized
here without replacing its captured values.

The checklist population at the E0 worktree is **270 checked / 268 matched /
268 resolved / 3 retracted**, not the hypothesized 268 checked. v0.35 still
contributes **0/9** checked lines because its nine boxes use the plain form;
v0.34 contributes **7** audited task boxes among **17** checked lines, with the
other **10** belonging to closing checklists. The three retractions name one
v0.11 and two v0.12 boxes, and both runbooks remain tracked while falling
outside the two-cycle export retention set. The two v0.36 boxes fail for a
second, separately measured reason: qualified progress entries store the
repository-relative runbook path while `matching_commit` compares it with a
basename. Step 2 owns both syntax and qualification repairs.
After E0's own box was marked, the live pre-audit population became **271
checked / 268 matched**, with all three v0.36 boxes unmatched for that same
qualification defect; the entering-state H1 measurement above remains 270/268.

The pre-E0 equivalence witness printed `store=[] extract=[]` immediately before
its equality assertion and then reported **201 kept / 0 dropped**. E0 adds the
first real multi-sector canonical-identity witness: two identical 43-feature
documents in science and technology persist as self-canonical in the store,
while the unpartitioned view keeps science and drops technology at Hamming
distance **0**. The entering tree's only other multi-sector store test checks
SQL query scoping and never asserts canonical identity. A fresh production
fixture ingest then measured **6 science / 7 technology / 42 cross-sector
pairs**; the full distance distribution spans **22–41** and contains **zero**
pairs at or below 16. Thus the shipped fixture does not happen to trigger G1,
while the configured multi-sector runtime and explicit witness prove the path
is reachable.

Fresh project-root exports at the exact v0.17.2 release parent and tagged
closing commit measured **2,725,527 / 151 files** and **2,737,957 / 151 files**.
The hypothesized sizes and 152-file count were false; the **+12,430-byte** delta
was correct. The release object graph is: release parent
`d4258883645a99f9499895bf064e453de9be1281`, tree
`c2ab865cf9a6cbb685554568ddf9d94354747784`; closing commit
`9996c6820d720160b64607575d0270d2e5393ef9`, tree
`2fbb5ef5323ef010c2cbacddfcd713375881a4e6`; annotated tag object
`16ee7bcb2214859156edbceeb5e314ac1a67f39b`, peeling to the closing commit.
The closing commit's immediate parent is the release parent. A read-only
`git ls-remote origin` found none of those five object ids; published `main`
and v0.17.1 both remain at `f02379f03ccdfd1b019413234f2ad014d169fb04`.
Contrary to H9, the full closing hash is now tracked in State and the active
runbook; the full tag-object hash remains absent. The release-parent and its
tree were already recorded.

The lifecycle source confirms the post-push rule is reached on
`head != measured_target` without measuring publication. For a valid descendant
of the tagged close, the hosted-only `--skip-local-tag-verification` early
return is the sole preceding path that avoids the rule; using it locally would
also skip published-release verification. `cmd_ci_local` has **22** ordered
jobs and executes `ci_local_job "$label" "$target" || return $?`, proving the
job-2 abort behavior. The worktree has exactly the two expected untracked
amendment inputs; both remain untouched.

All **22/22** local identities were again exercised individually for E0.
Twenty passed, including workspace and Rust 1.78 tests with the new witness,
net 1.86 success and 1.85 refusal, **366/366** shell tests with the one accepted
warning, **332** protected pins, and golden **11/11**. Direct `cycle-check`
retains only Step 1A's expected missing-post-push defect. `checklist-audit`
truthfully retains the two v0.36 qualification defects assigned to Step 2. No
identity was omitted; no dependency, production source, protected byte, v0.35
byte, tag, or remote ref changed.

**v0.36 Step 1A publication predicate decision (measured 2026-08-03).** No
non-self-reported offline Git predicate can prove that a tag remains absent
from a remote: local remote-tracking refs can be stale, and Git has no distinct
remote-tag namespace after fetch. The least-bad truthful representation is
therefore an explicit dated observation backed by the exact read-only command
`git ls-remote origin refs/tags/v0.17.2 'refs/tags/v0.17.2^{}'`. It exited 0
with empty output on 2026-08-03. This is measurement-backed but not
self-refreshing; `cycle-check` reports that limitation instead of disguising it
as an independent offline fact. A future complete post-push record takes
precedence over this historical absence observation. A durable signed hosted
publication receipt available offline would have changed the choice.

- **Publication observation date:** 2026-08-03
- **Publication observation release:** `v0.17.2`
- **Publication observation status:** `unpublished-local-close`
- **Publication observation remote:** `origin`
- **Publication observation tag ref:** `absent`

The implemented lifecycle admits that record only when no post-push record is
present, exactly one release-matching observation exists, its date is valid,
and the live header says the release is closed locally and unpublished. Direct
`./run cycle-check` now passes and reports
`publication=unpublished-local-close bound=dated origin tag-absence
observation; offline Git cannot independently refresh remote absence`.

The two-direction control is non-vacuous. Before the new admission branch, the
planted valid observation failed with `publication post-push record required`;
afterward it passes. The separately planted published descendant still fails
without its post-push record, and a complete post-push record takes precedence
over the older absence observation. Both branches are bound to distinct R12
control-site markers. The full mutation suite passes **12/12 registered rules /
75 controls**.

The exact permission-complete `./run ci-local` then passed all **22/22** jobs:
workspace and Rust 1.78 checks/tests, net checks/tests with Rust 1.86 success and
1.85 refusal, clippy, rustfmt, shell **366/366** with the one accepted warning,
golden **11/11**, all **332** pinned files and both protected databases, and the
remaining lifecycle/evidence jobs. The earlier sandbox-denied loopback bind
was an environment non-result; the approved net lane passed all **29** ingest,
**3** SEC replay, and **30** cored tests. No production source, dependency,
protected byte, v0.35 byte, tag, remote ref, or amendment input changed.

**v0.36 Step 2 box-coverage decision and result (measured 2026-08-03).**
C2 selects the runbook's own Step headings as the nonempty structural
population. Across all **34** tracked execution runbooks the fixed audit
derives **283 Step headings / 287 task boxes** with no missing or ambiguous
Step-to-box mapping. A sole box inside a Step section is authoritative;
otherwise the full heading id or its derived label resolves a centralized
cycle checklist. Progress/declaration-backed extras account for activation and
measured corrective tasks. There is no per-cycle task list, minimum count, or
line-form exclusion list. A Step with no box is now a named error, while an
unchecked but present future box remains correctly outside checked-task
resolution.

C3 requires forward qualifiers because the tracked corpus contains a real
collision: `T4` is a checked task in both `TASKS-v0.8-EXECUTION.md` and
`TASKS-v0.8.1-EXECUTION.md`, both resolve through `PROGRESS-v0.8.md`, and that
record also contains multiple older unqualified `T4` entries. Its later
runbook-qualified corrections are what make the present selection independent
of cross-runbook file order. The first structurally derived plain-task-box
runbook establishes the forward-only qualifier epoch; this derives v0.35
without naming a cycle floor and preserves earlier immutable records under
their original contract. No real shared-id collision, or a structurally
one-runbook-per-progress mapping, would have changed the decision.

Before the fix, v0.35 contributed **0/9** task boxes and the whole audit passed
vacuously. After the fix and before Step 3 declarations, every one of its nine
plain boxes is visible and the audit fails for the real measured reason:
`PROGRESS-v0.35.md` has zero runbook-qualified entries. The complete interim
population is **281 checked / 272 matched / 272 resolved / 0 exemptions / 3
retractions**; v0.35 reports **8 Steps / 9 task boxes / 9 checked / 0 matched /
0 resolved** and v0.36 reports **9 Steps / 10 task boxes / 4 checked / 4
matched / 4 resolved**.

Registered R13 executes four independent fixtures: an all-unbolded valid
runbook, an id absent from progress, a derived Step with no box, and an
unqualified forward task. Each corresponding mutation fails at its unique
control-site marker. The complete suite passes **13/13 rules / 79 controls**
with zero absolute finding-line fields. The permission-complete standalone
golden run passes **11/11** with zero delta; the sandboxed bind attempt was an
environment non-result. No production source, dependency, protected byte,
v0.35 byte, tag/ref, or amendment input changed.

**v0.36 Step 3 v0.35 declaration (measured 2026-08-03).** The v0.35 closing
record's **268 checked / 3 retracted / 268 matched / 268 resolved** figures are
a true historical tool output over the boxes the old bold-only parser could
see. They do not evidence v0.35's nine plain task boxes: that population was
exactly zero at close. Creating the missing executable links now would require
editing the closed runbook or its dated progress record, so DR2 requires a
forward declaration rather than reconstruction.

`config/checklist-exemptions.json` now carries exactly **9** dated entries,
one for each v0.35 task box, accepted by the repository operator through the
active Step 3. `ACTIVATE` names the missing runbook qualifier; each Step box
also records its measured box-id/progress-id namespace mismatch. The file-level
date and acceptance statement no longer claim every checked task is
resolvable. No retraction was added: the historical output is true, v0.35 is
unpublished, and DR4's twice-verified published-false bar is not met.

With Step 3 still unchecked for its pre-commit acceptance measurement,
`checklist-audit` passes at **282 checked / 3 retracted / 273 matched / 273
resolved / 9 exemptions**. v0.35 is explicitly **8 Steps / 9 task boxes / 9
checked / 0 matched / 0 resolved / 9 exemptions**; v0.36 is **9 Steps / 10
task boxes / 5 checked / 5 matched / 5 resolved**. The v0.35 runbook and
progress worktree blobs equal their `HEAD` blobs exactly:
`1a5424c704ab56bf9a0ce3c261a20e92eabc7bc5` and
`510d27f22f2687f6dfd48c49eacd7442d60bb77f`; targeted `git diff --exit-code`
returned 0. No v0.35 byte, production source, dependency, protected byte,
tag/ref, or amendment input changed.

**v0.36 Step 4 identity-scope decision and result (measured 2026-08-03).**
C1 selects the existing shared `intel-extract` dependency as the one compiled
identity seam. Entering-state inspection refuted the old architectural premise
that no common module was available: store and view already depended on
`intel-extract`, so the threshold-authority trigger fired without a new crate,
manifest edge, type-boundary dependency, lockfile change, or MSRV movement.
`assign_dedup_identity` now owns the `(published_day, id)` ordering, sector-keyed
kept sets, feature eligibility, distance comparison, and canonical selection.
Store persistence and view collapse translate their boundary values into that
same rule. The radius remains boundary-local and synchronized by R5.

The before witness used two identical **43-feature** documents. Store persisted
science and technology as self-canonical, while view kept science and dropped
technology at distance **0**. The after witness adds a later same-sector science
duplicate so equality cannot pass on empty sets: both layers keep the
cross-sector documents separate and produce the same nonempty drop
`science::cross-sector-duplicate → science::cross-sector-witness` at distance
**0**. The shipped-fixture H7 measurement is unchanged before and after:
**6 science / 7 technology / 42 cross-sector pairs**, distribution
`{22:1, 23:1, 25:1, 27:1, 28:1, 29:5, 30:3, 31:3, 32:2, 33:6,
34:3, 35:7, 36:1, 37:4, 39:2, 41:1}`, and **0** pairs at or below 16.

Registered R14 failed on the entering tree at `dedup_near`,
`assign_canonical_ids_tx`, and the absent shared sector partition. After the
change it passes, and all three executable mutations independently catch the
removed view call, removed store call, and replaced sector key. The full suite
passes **14/14 rules / 81 controls**. R5 now observes the shared implementation's
single eligibility call, and R1 remains the five durability-caller topology
control; its positional source anchor was re-measured as
`ARCHITECTURE.md:118-124` after the architectural edit.

The observable-output answer is **no configured `/v1/*` response moved**.
Disposable builds of the Step 3 tree and Step 4 worktree ingested all configured
sectors, then exercised signals, brief, search, and ask for both configured
subscriptions plus both billing routes. Their canonical payloads were
byte-identical at **15,719 bytes**, SHA-256
`0c2ec212b9e398eddd38053c7157b8dd283f35f3908ad1b8c2f6481a912f09ea`.
`acme-research`, the two-sector case, remains **12 documents / 1 collapse**;
`quant-desk` remains **1 / 0**. The unchanged search license fields, withheld
snippets, ask attestation output, sectors, and response bodies demonstrate that
no licensing or entitlement outcome moved. Golden independently passes
**11/11** with zero delta.

For DR5 clause 2, partitioning can change which documents are selected on the
explicit counterexample corpus, but it does not add, remove, or redefine any
value in a serialized `/v1/*` field's domain. The configured fixture selects
the same documents and produces byte-identical public output. This is a runtime
behavior correction, not a public value-domain change, so it does not require
a minor version; absent a later higher-precedence finding, DR5 selects patch.

The exact permission-complete `./run ci-local` passed all **22/22** jobs:
workspace and Rust 1.78 checks/tests, net checks/tests with Rust 1.86 success and
1.85 refusal, clippy, rustfmt, shell **368/368** with the one accepted warning,
golden **11/11**, all **332** pinned files and both protected databases, and all
remaining lifecycle/evidence jobs. No protected byte, v0.35 byte, amendment
input, tag, or remote ref moved.

**v0.36 Step 5 audit-child completion (measured 2026-08-03).** An isolated
clone checked out the existing v0.35 closing commit
`9996c6820d720160b64607575d0270d2e5393ef9`; its Git tree object is
`2fbb5ef5323ef010c2cbacddfcd713375881a4e6` and its immediate parent is release
commit `d4258883645a99f9499895bf064e453de9be1281`. Project-root
`./run export-check` at that exact detached checkout independently measured
**100 derived sources / 7 required paths / 151 exported files / 2,737,957
bytes / 2 retained cycles**. Direct `git show` of the closing commit's v0.35
progress record supplies its last governed figure, **2,742,486 bytes**, and
independent arithmetic gives **2,737,957 − 2,742,486 = −4,529**.

- cycle-ending review-export audit: closing_tree=`9996c6820d720160b64607575d0270d2e5393ef9`; bytes=`2737957`; audit_delta=`-4529`

The field's historical name `closing_tree` denotes the measured closing
**commit**, as in the v0.33/v0.34 audit records; the distinct Git tree object is
reported above so the two object types are not conflated. This is a v0.36
append that discharges v0.35's missed Step 7 criterion. It is deliberately in
the live State record rather than the open v0.36 progress log: `cycle-check`
forbids a current cycle-ending audit field while that current cycle is open,
and DR2 forbids editing the closed v0.35 progress record.

H8's independently reconstructed exact-tree figures remain **2,725,527 bytes
at the release parent → 2,737,957 bytes at the closing commit**, a **+12,430**
raw exact-tree increase. The required `audit_delta` instead compares the
closing export with the last governed field visible in that closing tree. The
historical governed figure is **16,959 bytes larger** than H8's exact
release-parent re-export; `+16,959 + (−4,529) = +12,430`. The discrepancy is
therefore exposed rather than absorbed: H8 refutes the historical field's
exact-tree characterization, while the immutable field remains the binding
baseline used by the lifecycle checker. No v0.35 byte, production source,
dependency, protected byte, tag, remote ref, or amendment input moved.

**v0.36 Step 6 hosted RE-MEASURE (measured 2026-08-03).** The exact audited
candidate is `f50db6744df726434db7f5aeffa1a08bbbf521fc`. Pinned `gh` **2.96.0**
first passed the standing preflight: **7/7** immutable historical bundles were
accepted with every strict flag, and the deliberately wrong signer was
rejected. Immediately before the only push, `git ls-remote` exited **0** with
no entry for fresh ref
`refs/heads/codex/v0.36-evidence-f50db67`. One non-force push created exactly
that ref; immediate and final readback resolved it to the candidate. No ref was
reused, forced, moved, deleted, or repurposed.

Workflow-dispatch run **30810557834**, attempt **1**, targeted that exact SHA
and ref with evidence signing. All **9/9** blocking identities passed: `core`,
`golden`, `lint`, `msrv`, `net`, `net-msrv-1-85`, `net-msrv-1-86`, and both
shell matrices. Dependency drift was the sole declared report-only skip. Every
receipt emission, attestation, bundle copy, and artifact persistence step
passed; the run was dispatched exactly once and was not retried. Hosted golden
passed **11/11**.

The release-grade audit used canonical single-bundle JSON, qualified workflow
`jiayanzeng/intel-platform/.github/workflows/ci.yml`, exact source/signer
digest `f50db6744df726434db7f5aeffa1a08bbbf521fc`, exact source ref
`refs/heads/codex/v0.36-evidence-f50db67`, the GitHub-hosted-runner denial, and
every strict verifier flag. It accepted **9**, rejected **0**, found the
complete matrix, and independently matched every bundle's certificate identity
to
`https://github.com/jiayanzeng/intel-platform/.github/workflows/ci.yml@refs/heads/codex/v0.36-evidence-f50db67`.
The operator-local report is **41,096 bytes**, SHA-256
`ab767a456411029fd4529bb8c1dc97dc135869765c33cf078add510e98ef05f7`,
and remains under `/private/tmp`, outside the repository and manifest.

Three executed `jq -e` assertions proved `msrv=1.78.0`,
`net-msrv-1-86=1.86.0`, and `net-msrv-1-85=1.85.0`; all exited **0**. Local
Python 3.11.4 and 3.12.13 each collected and passed **368/368**. Each hosted
lane collected **368**, passed **367**, and skipped exactly
`tests/test_deferred_audit.py::test_on_site_production_measurements_match_committed_receipt`,
marked `on_site`, for reason `on-site production audit requires protected
corpora and built cored`. Both `tools/test_population.py` comparisons derived
`collected=368`, `equivalent=true`, and `equivalent_passed=368`; no population
count was accepted by transcription.

The workflow stayed byte-identical at **39,177 bytes**, SHA-256
`4ebf2c2193fe3fb11e7710b20c1c000fd073103656dc0b155bce945b57bff871`.
Final direct remote measurement kept `main` and peeled `v0.17.1` at
`f02379f03ccdfd1b019413234f2ad014d169fb04` and the v0.17.1 annotated tag
object at
`14912f134e45277e2b4fd10b7f5bf8b4900ca20d`; v0.17.2 still has no remote tag
entry. No `main` push, tag publication, production/source change, dependency
change, protected-byte change, publisher request, or retry occurred.

**v0.36 Step 7 pre-implementation gate trip and C4 disposition (measured
2026-08-03).** The per-task gate review required by `AGENTS.md` found that Step
7's stated gate covered Step 1A/prior-step completion and publication authority,
but did not contain its mandatory criterion that the cycle-ending export-audit
field exist before the Step 7 box is checked. Widening the gate to that criterion
exposed an author-side rule with no satisfying assignment; the task therefore
stopped before release implementation.

The executed lifecycle has two exclusive active states. With any unchecked box
and no closing record it selects `active_state="open"`; in that state
`check_governed_export_margin` rejects every parsed cycle-ending field. It
selects `active_state="closed"` only with zero unchecked boxes and exactly one
closing record. An isolated clone of exact audit commit
`0d2e8b24bcc1ec0758027e52b13ecf91458e0395` planted one syntactically valid
audit field after the latest governed field while R-CLOSE remained unchecked.
The real `./run cycle-check` exited **1** with exactly one defect:
`cycle-ending review-export audit is unavailable while the active cycle is
open`.

Reordering cannot supply a truthful construction. Tagged R-CLOSE requires the
checked closing commit to be the recorded release commit's immediate child and
to contain the complete closing record. Its own content-addressed commit id
does not exist until that tree is committed, so that same tree cannot truthfully
record itself as `closing_tree`. An intervening measurement commit breaks the
immediate-parent rule; the normal append-only audit child occurs after the box
is checked and therefore violates this cycle's explicit before-check clause.
No hash was predicted, no checker or criterion was weakened, and no release
authority, local tag, `main`, or remote tag moved. The Step 7 box remains open.

C4 is deferred under its own rule, not partially implemented. The six `/v1/*`
routes declare no response models and return dynamic dictionaries or plain text.
Their serialized values include subscriber/query input, configuration-derived
sector/client strings, core-provided nested objects, and model-generated free
text. The repository has no machine-readable, release-versioned authority that
exhaustively states every field's semantic value domain, and the declared scope
forbids the shell production changes needed to introduce one. A generated
control over only currently typed or observed fields would have an incomplete
witness and is expressly disallowed. A complete response-model/domain manifest
covering every success and error body, with an independently versioned baseline,
would change this determination. The existing deferral row retains the trigger.

DR5's measured classification remains patch: Step 4 added no route or named
surface, and its complete configured comparison was byte-identical at **15,719
bytes** with no added, removed, or redefined serialized field-domain value. If
the ordering defect is author-corrected without a higher-precedence finding,
the next available patch is **v0.17.3**. That is a conditional classification,
not a closing disposition or a version-authority change.

**v0.36 A2 Step 7 ordering correction (measured 2026-08-03).** Reviewer A2
affirms E3 as the sixth author-side unsatisfiable rule in its declared family
and preserves the four-clause impossibility proof above. Application commit
`c9ecfa404ebe0f93049765ac073c7a70865084e3` changes only the active runbook:
the closing commit now checks Step 7, the local annotated tag targets that
commit, and the immediate next commit carries the measured closing-export
audit before handoff. Every other Step 7 criterion remains evaluated at the
assembled closing worktree.

Direct `cycle-check` passes with v0.36 still truthfully open and names no
further undisclosed interaction. `version-check` remains at **0.17.2** with
**3** executable offline-MSRV pins, **22** current offline-MSRV restatements,
and **3** current release restatements. `checklist-audit` remains internally
consistent at **286 checked / 3 retracted / 277 matched / 277 resolved / 9
exemptions**. The amendment-only golden run passes **11/11** with zero delta.
The reviewer text is now the third untracked amendment input; all three remain
untracked and are excluded from the implementation commit.

**v0.36 R-CLOSE release-parent preparation (measured 2026-08-03).** DR5
selects patch **v0.17.3**. Step 4's explicit cross-sector witness proves a real
runtime document-selection correction: both sectors now retain their own
representative, while a later same-sector duplicate still collapses under the
shared rule. The complete configured-subscription comparison across signals,
brief, search, ask, and both billing routes remains byte-identical at **15,719
bytes**, SHA-256
`0c2ec212b9e398eddd38053c7157b8dd283f35f3908ad1b8c2f6481a912f09ea`.
No route, named surface, response-body schema, field type, serialized field-
domain value, entitlement, or licensing outcome moves, so neither DR5 minor
clause fires. The patch reason names the runtime movement rather than implying
that no behavior changed.

The release parent moves all five executable authorities to **0.17.3**:
`apps/cored/Cargo.toml`, `shell/intel_shell/__init__.py`,
`shell/intel_shell/app.py`, this State header, and `CHANGELOG.md`. README's
three current restatements move with them, and Cargo regenerates only cored's
lockfile package value. The release parent remains untagged. Its immediate
child will carry the checked closing record; only that child becomes the local
annotated-tag target, followed immediately by A2's audit child.

**v0.36 R-CLOSE — v0.17.3 patch release closed locally (measured
2026-08-03).** Release disposition: release (as of 2026-08-03). Release commit
`9946cedae75d99c53d17a6f8b5507d10cb9bd959` is untagged and is the immediate
parent of the checked closing record. DR5 selects patch because DR1 corrects
reachable cross-sector runtime document selection while the complete
configured-subscription comparison remains byte-identical at **15,719 bytes**,
SHA-256
`0c2ec212b9e398eddd38053c7157b8dd283f35f3908ad1b8c2f6481a912f09ea`.
No route, named surface, response-body shape, field type, serialized `/v1/*`
value-domain value, entitlement, or licensing outcome moves; the disposition
reason expressly names the runtime correction.

`version-check` derives **0.17.3** from all five executable authorities and
reports **3** offline-MSRV pins, **22** current offline-MSRV restatements, and
**3** current release restatements. Exact candidate `f50db674…` and hosted run
30810557834 passed **9/9** blocking identities; the pinned verifier accepted
all nine bundles and the shell comparator derived equivalent **368**-test
populations. The release-parent full local gate passed **22/22**, including
**14/14 rules / 81 controls**, both **368/368** shell lanes, the Rust 1.78 and
net 1.86 success lanes, the required net 1.85 locked-ICU refusal, all **332**
pins plus both protected databases, and embedded golden **11/11**.

The exact release-parent export is **2,885,942 / 3,000,000 bytes** across 154
files with two retained cycles. Against v0.35's **2,742,486-byte** governed
field, its +143,456-byte adjacent-cycle denominator leaves **114,058 bytes /
3.80% / 0.80 cycles**. The assembled closing State is **339,913 / 453,741
bytes**, leaving **113,828 bytes / 2.73 cycles** against the
v0.35 release-parent State basis of 298,251 bytes. The manifest remains
**193,057 / 1,048,576 bytes**, leaving **855,519 bytes / 842.88 cycles**.
Export is nearest.

This close is the first consecutive cycle in published v0.17.1's current epoch
whose unpublished distance carries the measured cross-sector runtime-behavior
difference, so the count is **1**. No public surface moved and local close does
not reset the epoch. C4 remains deferred: all six `/v1/*` routes lack an
exhaustive machine-readable response/domain authority, and a partial observed-
field control would be vacuous. Every active deferral row carries a dated
v0.36 observation.

Direct pre-close `git ls-remote` exited 0 with no remote
`refs/tags/v0.17.3` entry, and no local tag existed. No push, remote `main`
movement, or release-tag publication is authorized. The closing commit contains
no tag-object field; the annotated tag is created locally only after that
commit exists. Per A2, its immediate append-only child measures the closing
tree and carries the cycle-ending export-audit field before handoff.

**v0.36 closing-export audit child (measured 2026-08-03).** The local
annotated `v0.17.3` tag object is
`0fe42d7a6a86e94bb95a93a86b7a4b09917b97f4` and peels to closing commit
`a5afab9e6842a1b6c00a7d17fdeaa3e254edf80f`, whose immediate parent is exact
release commit `9946cedae75d99c53d17a6f8b5507d10cb9bd959`. The project-root export of
that closing commit passed at **2,898,371 bytes / 154 files / 2 retained
cycles**, a truthful **+12,429-byte** difference from the closing tree's
2,885,942-byte governed release-parent field. This append-only child is the
immediate next commit after the tag target and is the final v0.36 commit; it
does not predict its own content-addressed id or defer the audit to post-push.

The first full-gate attempt on the audit child passed the first **16** jobs,
including all **14/14 rules / 81 controls**, then the Rust 1.78 workspace-test
lane failed in `sec_identity_measure`: one of its two parallel tests found the
other test's process-scoped temporary directory already present and
`create_dir` returned `AlreadyExists`. Both tests call the same
`DisposableDir::create()`, whose name is only process id plus one clock sample
and has no collision retry. The cross-sector test itself passed in the failed
run, and an exact isolated Rust 1.78 rerun passed **2/2**. This is a v0.37 test-
harness finding, not a production or identity-result regression; v0.36 does
not change the already-tagged closing tree to repair a newly discovered test
flakiness. The complete final-head gate is rerun from the start and only that
rerun may support a 22/22 handoff claim.

After the local tag was created, direct `git ls-remote origin
refs/tags/v0.17.3 'refs/tags/v0.17.3^{}'` again exited 0 with empty output.
This dated per-release observation is the C7 input for the second unpublished
local close. It is intentionally weaker than a signed publication receipt and
does not widen the separately planted rule that a published descendant must
carry its complete post-push record.

- **Publication observation date:** 2026-08-03
- **Publication observation release:** `v0.17.3`
- **Publication observation status:** `unpublished-local-close`
- **Publication observation remote:** `origin`
- **Publication observation tag ref:** `absent`

<!-- STATE_ARCHIVE_PERMANENT_TAIL:START -->
## 1. Architecture

```text
SHELL (Python, product)   app.py /v1/* · auth.py keys→sectors · llm.py chat+embed
                          prompts.py · briefing.py · pipeline.py · enrichment.py
                          scheduler.py — per-SOURCE and per-sector cadence (v0.6)
        │  CoreClient (core_client.py) — the ONLY door; httpx, injectable transport
        ▼  minimal JSON API, 127.0.0.1:8788, optional x-core-token
CORE (Rust, engine)       apps/cored: /health /sectors /ingest /view /search
                          /retrieve /attest /embeddings(/missing)
                          /signals/record /docs
                          crates: core compliance ingest extract enrich analyze
                                  store registry view retrieve
```

**Config split:** `config/core.json` (sectors/sources/licenses) + `config/entities.json` (gazetteer) are core-owned; `config/subscriptions.json` (clients/sectors/keys) and `config/schedule.json` are shell-owned. Demo keys: `ak_acme_7f3d9c` (science+technology), `ak_quant_2b81aa` (finance).

## 2. Load-bearing placement decisions (do not move these casually)

1. **License gating stays in the CORE, with the A4 trust boundary stated exactly.** `store.search` nulls snippets for IndexOnly; `/view` hydrates evidence with `excerpt: Option<String>` gated by `License::redistributable()`; `/attest` refuses a model answer sharing a measured 16-token normalized phrase with IndexOnly context. `briefing.py` never receives gated text. The shipped `/v1/ask` path submits all cited context ids and uses the returned clean answer, so copied gated context is refused there. A rewritten shell can omit the call or choose a false scope; A4 proved that a context receipt alone cannot make that shell-owned public response non-bypassable. The shell therefore remains in the trusted computing base until public egress itself crosses a core-owned attestation boundary.
2. **Entitlement DECISION in the shell, sector FILTERING in the core.** A shell bug can grant wrong sectors, never bypass filtering.
3. **The core never calls an LLM.** Shell pulls `GET /embeddings/missing`, calls the provider, `POST /embeddings` vectors back. `/retrieve` accepts `model` + `query_vector`; `/attest` only inspects a string the shell hands it.
4. **Full bodies ARE served on internal `/retrieve` and `/docs`** — passing IndexOnly text to a model as context is analysis, not redistribution; loopback-internal, not public.
5. **`/view`'s `kind` is `format!("{:?}", SignalKind)`**, so the shell can post signals straight back to `/signals/record`.
6. All v0.1–v0.3 invariants unchanged: dedup (hamming ≤16) BEFORE all statistics; mentions per (entity, doc); Corroborated suppressed when Rising; discovery on bodies only; FNV-1a determinism; RRF k=60.
7. **(v0.6) Source selection is core business, not shell business.** `/ingest` takes `{sectors, sources?}`. `sources` names connector ids; **each is still validated against `sectors`**, so a named source outside the caller's entitlement is refused, not run — the sector filter is not a suggestion that a source id can bypass (HC2). Selection lives in `registry::select_sources`, which returns `unknown_ids` as **structured per-id errors rather than panicking**. Omitting `sources` entirely preserves the exact pre-v0.6 behavior (every source in the sectors, in config order) — a regression test pins this (HC5).
8. **(v0.6, hardened v0.8/T2) Harvest cursors live in the core store, not the shell.** The `cursors(source_id, cursor, high_water, pending_high_water, updated_at)` row is committed in the **same SQLite transaction** as each parsed page's documents and canonical-id rematerialization. `cursor` is the next OAI-PMH `resumptionToken`; `pending_high_water` retains the max datestamp seen across capped/restarted pages; only a final-page commit clears both and advances completed `high_water`. This prevents either half of the old split-write failure: advancing past documents still in memory, or losing an earlier page's maximum datestamp after restart. High-water advance remains monotonic (ISO dates ⇒ lexicographic max is chronological max). Under HC9's ownership scope, cursors are recorded core-archive state: they belong in SQLite beside the documents whose page commit they make atomic. Connectors that don't page (RSS) ignore the seam entirely.

9. **(v0.6/T6) Provider vocabulary is normalized INTO the neutral one, never the other way round.** `billing.apply_event` speaks `subscription.created|updated|deleted|key_rotated` and nothing else. Stripe enters through `adapters/stripe.py`, which verifies Stripe's signature scheme and maps `customer.subscription.*` onto those events. Consequences worth keeping: a second provider is a second adapter, not a change to the store or the entitlement model; and the freshness check on Stripe's signed timestamp is load-bearing, because a *genuine* captured request replayed later carries a perfectly valid MAC — the timestamp is the only thing that refuses it. Keys are compared against a *set* of active hashes, so rotation has a grace window and revocation is just rotation with none.
10. **(v0.6/T9, closed v0.8.2/A2) Dedup identity is a function of the corpus, not of arrival order.** `dedup_near` keeps the earliest document by `(published_day, id)` — a global property. So `canonical_id` is persisted as a **re-materialization of that same rule on every ingest that adds rows**, NOT as a first-seen-wins assignment at insert. This matters more since T3: sources now run on independent clocks, so arrival order genuinely varies, and an incremental assignment would let two runs over the same 13 documents disagree about which copy is canonical. Relatedly, `/retrieve` deliberately does **not** filter by `canonical_id`: it keeps whichever of a near-dup pair *the query* ranked higher. Canonical id is a property of the corpus; relevance is a property of the question, and context assembly is a question about the question. T3 materializes `simhash(title + body)` at ingest/migration and refreshes it on document update. A2 closes all three consumers: `/view` maps a NULL to a document-naming error; `/retrieve` refuses a fused id absent from the persisted-fingerprint map; canonical assignment reads every row and errors on the first NULL instead of silently excluding it. No request path recomputes a missing fingerprint. `missing_fingerprints()` and `./run verify-fingerprints` name broken rows. B0.2 measured zero such rows and zero NULL canonical ids in both protected archives, so this repair closes the structural guarantee without changing their corpus identity.

**2.11 — robots.txt is DISCOVERED, and the two gates compose one way only (T2, v0.7).**
There are now two robots checks, and the order and direction matter:

- The **publisher's** policy, fetched from their real `/robots.txt` (`RobotsCache`, in `crates/compliance`). Per-origin, TTL 24h, bounded to 512 origins, and the fetch itself goes through the same per-host politeness limiter — it would be a strange kind of respect to skip the rate limit for the one file that describes how to be respectful.
- The **operator's** configured deny-list (`RobotsGate::new(&["/private","/admin"])`), which applies *on top* and can only ever refuse **more**. A publisher blessing `/private` does not oblige us to crawl it.

Three decisions inside this that are easy to get wrong and are therefore pinned:

- **Fail-closed, and the 4xx/5xx distinction is not cosmetic.** RFC 9309 gives three outcomes, not two. **2xx** ⇒ the body governs (an *empty* body is a valid allow-all, and is **not** the same thing as a 404). **5xx / DNS / TLS / timeout** ⇒ "Unreachable" (§2.3.1.4): we do not know the policy, so we take nothing. **4xx** ⇒ "Unavailable" (§2.3.1.3): the RFC permits full access, and here we **knowingly diverge** — `MissingPolicy::Deny` is the default, because we fetch a small operator-configured set of publishers rather than discovering the open web, and the cost of wrongly fetching from someone who never published a policy is a compliance incident while the cost of wrongly *not* fetching is a log line. `MissingPolicy::RfcAllowAll` is available and named, so the divergence is a choice rather than a buried `else`.
- **A fixture read is not a request.** `gate()` takes a `Reach` (`Network` | `Fixture`). A fixture-backed source never fetches `robots.txt` — an "offline, deterministic" run that quietly phones example.org for permission to read a file already on disk would be both a surprise and a lie about what offline means. Tested directly: `a_fixture_fetch_never_asks_the_publisher_for_permission` asserts **zero** fetches even on a `net` build with a cache wired in.
- **A published `Crawl-delay` can only slow us down.** `apply_crawl_delay` adopts a publisher's stated cadence only if it is *slower* than our own floor (2 rps). A `robots.txt` must not be able to talk us into hammering a server faster than we would have gone anyway.

**Consequence, and it is the reason this could not just be dropped into the handler:** politeness state is now **process-scoped**, not request-scoped. `HostLimiters` and `RobotsCache` moved into `AppState`. They used to be rebuilt inside `/ingest`, which meant two ingests a second apart each started with a clean limiter and neither waited for the other — and a per-request robots cache would have re-fetched every publisher's `robots.txt` on *every ingest*, i.e. a "compliance" feature that made us a **worse** citizen than before. A TTL only means something if the cache outlives the request.

**2.12 — the 404 disposition is PER-SOURCE, and the operator's config is the opt-in (v0.7.1).**
v0.7 made the 404 decision cache-wide (`MissingPolicy::Deny`, with an `RfcAllowAll` override on the whole cache). The first live harvest proved that granularity wrong: arXiv's OAI-PMH host serves no robots.txt, and one blanket policy forces a false choice — fail closed and block a cooperative source, or open the 404 door for *every* source at once. Neither is right.

So the disposition now lives on the **source**, threaded `SourceCfg.robots_on_missing → {RssSource, ArxivOaiSource} → gate(…, on_missing) → RobotsCache::allowed(…, on_missing)`. Three properties are load-bearing and pinned:

- **Default is `Deny`, and a typo fails closed.** `MissingPolicy::from_config_str` maps `"allow"` (and synonyms) to `RfcAllowAll` and *everything else, including absent and misspelled,* to `Deny`. A source you forget to annotate, or annotate wrong, is conservative — never accidentally permissive. Every source except `arxiv-cs` is `Deny` today.
- **Opting in reinterprets ABSENCE ONLY.** `robots_on_missing: "allow"` changes the 404 case and nothing else. An explicit `Disallow` from a real robots.txt is still obeyed (tested: `opting_in_does_not_bypass_an_explicit_arxiv_disallow`), and an `Unreachable` origin (5xx/timeout) still fails closed. "Allow if absent" must never quietly become "ignore robots.txt."
- **The justification is the architecture's own principle, applied.** Entitlement decisions live with the operator, not in the fetch layer; the publisher's robots.txt is a *technical* access policy layered on top. An operator configuring `arxiv-cs` against a standards-compliant, harvest-designed endpoint *is* the opt-in. Encoding that as one auditable per-source line is the correct shape — as opposed to a global flip, which is what the on-site tester reached for (and which, being applied to a `#[default]`-attribute default via `sed` on the literal string, changed a doc comment and nothing else).



**Toolchain matrix (v0.7 — every cell RUN, none inferred). The 1.75 and 1.76 rows are new, and they are why §5's floor claim changed:**

| toolchain | `check`/`test --workspace --locked` | `-p cored --features net` |
|---|---|---|
| 1.75.0 (stock Ubuntu 24.04 `rustc`) | ❌ `lock file version 4 requires -Znext-lockfile-bump` | ❌ `failed to download replaced source registry` (the edition2024 masquerade) |
| 1.76.0 | ❌ same lockfile parse failure | ❌ |
| **1.78.0 — the floor** | **0 warnings, 75 green** | ❌ |
| **1.91.1 (pinned)** | **0 warnings, 75 green** | ✅ **clean, `--locked`, `-D warnings`** |

- **The v0.6.2 lockfile bug, measured.** Against the committed **v4** lock, cargo **1.75 and 1.76 cannot even parse it** — v4 needs cargo ≥ 1.78. v0.6.2's "verified green on 1.75" was therefore impossible; it had never been run.
- **And the fix that looked obvious is a trap, which is worth more than the fix.** Re-encoding the lock to **v3** genuinely restores 1.75 (verified: **75 green**, and the package set diffed **byte-identical** — same names, versions, checksums, so it is a format change and not a resolution change). But **cargo 1.91 rewrites the lock back to v4 as soon as it modifies it** — confirmed here by bumping `cored`'s version and watching a plain `cargo check` silently re-emit v4. v3 is a hand-edit with a half-life. **We therefore ship the sustainable floor (1.78) rather than the flattering one (1.75)**; local commands enforce it, and v0.10/G2 observed the configured runner job pass.
- `cargo check --workspace --locked --all-targets` with `RUSTFLAGS=-D warnings`: **0 warnings**. Same for `-p cored --features net --locked --all-targets`.
- `cargo test`: **75 green** — compliance **26** (was 7), ingest **14** (was 7), core 7, cored 7, registry 4, retrieve 3, extract 3, enrich 2, store 9. `cargo test -p intel-ingest --features net --locked`: 14 green.
- `pytest shell/tests`: **69 green**, unchanged — T2 is entirely below the seam, and the shell suite still needs no Rust toolchain.
- **T4's own testing objective, executed:** a deliberate warning (`let x = 1;` unused) introduced into `crates/extract` makes `RUSTFLAGS="-D warnings" cargo check --locked` exit **101**. The gate bites. Restored; clean.
- **Golden E2E re-verified live from a clean DB after T2 — every number identical:** acme ingests **13** (Finance skipped), dedup drops `techwire::tw-004` keeping `osdaily::osd-004` (hamming **12**) ⇒ **12 analyzed**; **DeepSeek RISING z=10.0** corroborated by 3 sources (arxiv-cs, osdaily, techwire); vLLM RISING z≈**2.67**; NVIDIA + Qwen **CORROBORATED**; **"Helios Labs" EMERGING**; immediate re-run **+0 new**; quant-desk sees only its **1** doc.
- **Public API spot-checks live:** bad key ⇒ **401**; entitlement-disjoint search (**acme 6 hits vs quant 0** for "deepseek"); all 4 IndexOnly hits return `snippet: null`; the brief renders "excerpt withheld" (10 occurrences).
- **T2 live-path proof, offline:** the `RobotsFetcher` seam is driven by a fake through every branch — 200-with-body, 200-empty, 404, 500, unreachable, malformed HTML-served-as-200 — so fail-closed is *tested*, not asserted. TTL expiry is tested deterministically with `tokio::time::pause()`, not by sleeping.

## 4. Next steps

**Done in v0.7:** ~~T2 (real robots.txt)~~ · **T4 workflow configured + MSRV
verified locally; no CI runner evidence** · **T5 built, measured, and rejected**
(§6c).
**Deferred in v0.7, each with the gate that deferred it:**

1. **T1 — the first live arXiv harvest. DEFERRED: no egress. Verified, not assumed.** `curl -sI https://export.arxiv.org/oai2?verb=Identify` ⇒ **HTTP 403, `x-deny-reason: host_not_allowed`** — the sandbox proxy refuses the host, exactly as in v0.6. The task's own gate is explicit ("no egress ⇒ defer and say so; **do not mock a live harvest and mark it done** — the entire value of this task is that it is not a mock"), so nothing was faked. **This is now the single highest-value item in the project, and it is not a code problem:** `--features net` builds, paging + cursors are implemented and unit-tested, the limiter and `Retry-After` handling exist, and **as of T2 the robots gate will do a real fetch before the first request**. On any box that can reach arXiv: `cargo build -p cored --features net --locked`, drop the `"fixture"` key from `arxiv-cs` in `config/core.json`, `POST /ingest {"sectors":["science"],"sources":["arxiv-cs"]}`. **HC13 stands: fixtures prove the state machine, not the wire.** The things that genuinely cannot be tested here are a real `503 Retry-After` under load, observed ≥3s page spacing on the wire, real-world XML edge cases, and cursor durability across a real interrupt.
2. **T4 (v0.7/T3) — point the LLM at a real endpoint. DEFERRED at the credential/configuration gate, and deliberately NOT mocked-and-declared-done.** Re-probed 2026-07-20: DeepSeek and OpenAI now both return unauthenticated **401**, so egress is available; however `LLM_BASE_URL` and `LLM_API_KEY` are absent and no local vLLM listener exists on 8000/8899/11434. `./run verify-llm` exits 2 before model work. A configured endpoint and credential from the operator are still required; then `tools/verify_llm.py` runs the checklist.
3. **T6 — seam hardening for multi-host. DEFERRED: condition still not met.** Core and shell still run on one host (`cored` binds `127.0.0.1:8788`; `deploy/intel-pipeline.service` sets `CORE_URL=http://127.0.0.1:8788`). `CORE_TOKEN` is implemented on both sides. Per the task's own instruction, no speculative UDS and no mTLS were written. **Trigger:** the first genuine cross-host split.
4. **T7 — scale swaps. DEFERRED (design-level), and T5 *removed* LSH from this bucket rather than promoting it.** Postgres remains a **concurrency** trigger (a second writer), not a size one, and may never fire.
5. **T8 — known-limitation pick-ups. All three SKIPPED on their own stated preconditions, which were checked rather than assumed.** (a) Materialize `/view`: the precondition is "if warm-up cost shows up" — the corpus is 12 documents; it has not. (b) One SQLite connection behind a `Mutex`: the trigger is a second writer; there is none. (c) A rebuild tool for pre-v0.6 `Day` encodings: the task says *"check before building it"* — **checked, and no such archive exists.** `/data` is gitignored and archives are never shipped; every DB reachable on this box was created fresh this session from fixtures, on the new encoding. Building the tool would have been building for a hypothetical.

**The recommended top of the v0.8 queue, in order:**

1. **The live arXiv harvest** (T1 above), the moment a box with egress exists. Everything is ready; nothing else can falsify the paging.
2. ~~**Persist the SimHash fingerprint.**~~ **COMPLETED in v0.8/T3.** The column and ingest write already existed when the step began, but `/view` still recomputed every fingerprint and no pre-column migration existed. Dedup now accepts persisted fingerprints, document updates refresh them, and the backfill was verified over a disposable pre-column copy of all 1,764 live rows with zero fingerprint or canonical-id mismatches. The golden result did not move.
3. ~~**Turn on `clippy` + `rustfmt` in CI.**~~ **CONFIGURED in v0.8/T6; first observed in v0.10/G2.** The job was not commented out; it was report-only, and B0 measured one clippy diagnostic plus 13 files of fmt drift. T6 fixed those findings in `097b017`, verified both commands clean locally, then configured the job as blocking in the separate gate commit. G2's first real runner execution observed the blocking job pass in 44 seconds.

## 5. Known limitations (documented, not hidden)

- ~~**Robots policy is configured, not discovered.**~~ **RESOLVED in v0.7 (T2)** — see §2.11 and §6b.
- ~~**"Rust 1.75 + `--locked` still builds the offline path."**~~ **FALSE, and it is the most important correction in this document.** The committed `Cargo.lock` is format **v4**, unparseable by cargo before **1.78**, so the claim could never have held — it had simply never been run. **The offline floor is now declared as 1.78**, measured locally across 1.75/1.76/1.78/1.91 and observed on the v0.10/G2 runner as Rust 1.78.0. Re-encoding the lock to v3 *does* buy back 1.75 (75 tests green, resolution byte-identical) but cargo ≥ 1.78 rewrites it to v4 on the next lock modification, so that floor cannot be held. **The general lesson: a claimed property that nothing executes is not a property, it is a wish** — the same failure that let `--features net` sit broken for two cycles and that let "robots-compliant" mean "compliant with a policy we wrote ourselves."
- ~~**The `--features net` 1.86 floor had no executable lane.**~~ **RESOLVED in v0.35 Step 5.** The locked net graph is `cored` → `intel-ingest` → `reqwest` 0.11.27 → `url` 2.5.8 → `idna` 1.1.0 → `idna_adapter` 1.2.2 → `icu_*` 2.2.0. Rust 1.86 builds it; Rust 1.85 exits on the dependencies' explicit `requires rustc 1.86` declarations, including `idna_adapter@1.2.2`. Local and hosted lane pairs execute both sides. The older registry-download failure was a non-result, not evidence of the floor.
- **Correction to a v0.5 note** (unchanged from v0.6): `/v1/ask`'s `context_suppressed` names `techwire::tw-004`, not `osdaily::osd-004`, for the question actually tested. Suppression at context assembly is **rank-aware by design**, so which copy of a syndicated story is dropped depends on which one the query ranked higher. Treat *"one of the pair is suppressed"* as the golden, not a specific id.
- **`Day` values changed scale (T9.3).** `published_day` is days-since-1970. Pre-v0.6 archives spanning a month boundary would need a rebuild — **checked in v0.7: no such archive exists**, so no tool was built (T8.3).
- ~~**`dedup_near` recomputes every fingerprint on every pass.**~~ **RESOLVED in v0.8/T3.** The store materializes the fingerprint and `/view` passes it into `dedup_near`; a deliberately violating test double proves the function consumes the supplied value rather than recomputing it.
- `/view` is memoized per (sector-set, generation) rather than materialized; a restart re-warms it. Cost is unmeasurable at 12 docs.
- One SQLite connection behind a `Mutex` (fine: the shell is the single caller); `cored` binds loopback by design.
- ~~**HC1 was not enforced on `/v1/ask`, and its test was vacuous.**~~
  **RESOLVED in v0.8/T1.** The model still receives capped IndexOnly bodies as
  internal analysis context, but its answer now goes to core `POST /attest`
  with the exact context document ids before any public response. The core
  checks normalized 16-token overlap only against `IndexOnly` bodies and
  replaces the entire answer with a constant refusal on any violation; `CcBy`
  quotation remains allowed. `tools/mock_openai.py --leak` deliberately emits
  a source sentence. Both the shell test and a real Rust↔HTTP↔Python E2E proved
  that sentence cannot pass, while the ordinary golden answer is unchanged.
  **A4 scope correction (2026-07-24):** this is structural for the shipped
  shell path, not for an arbitrary shell rewrite. The proposed receipt lacks a
  non-shell-controlled correlation to the prompt and cannot force the shell to
  call the endpoint, so that stronger claim is an accepted risk with the
  trigger recorded in §2.1 rather than a shipped mechanism.
- ~~**The robots gate was checked only on the configured origin while reqwest followed redirects automatically.**~~ **RESOLVED in v0.8/T5.** Both HTTP clients now set `Policy::none()`. Document redirects are resolved manually with the full gate before each next request; robots-file redirects fail closed. A failure-capable cross-origin 302 test makes the second body available, configures that origin to disallow it, proves both robots policies were fetched, and proves the second document request never happened. A same-origin redirect makes two document requests with exactly one robots fetch.
- **The robots cache does not de-duplicate concurrent misses.** Two simultaneous first-requests to the same origin can both fetch `/robots.txt`. Bounded, harmless (the limiter still spaces them). **T7 rechecked the trigger on 2026-07-20 and deferred the lock:** the supported scheduler remains one synchronous writer and the deployment unit is one-shot; revisit only when a second concurrent harvester actually exists.

## 6. Decision log

### 6a. Why `feed-rs` was NOT adopted (v0.6/T2)

The task set a three-clause gate; the swap tripped **all three** in v0.6.1, and the gate was **re-run** in v0.6.2 because clause 1 was a statement about a toolchain we had just changed. A decision log that keeps a dead reason is worse than no decision log.

1. ~~**It doesn't build on our toolchain.**~~ **STRUCK — no longer true.** `feed-rs 2.x` builds clean on 1.91.
2. **Footprint. STILL TRIPS.** 56 unique transitive crates, against 16 for the entirety of `intel-ingest`. It drags `chrono`, `quick-xml`, `regex`, `url`, `aho-corasick`, `mediatype`, `serde_json` to parse two small formats `roxmltree` already parses.
3. **Parse-equivalence breaks. STILL TRIPS.** `feed_rs::model` types timestamps as `Option<DateTime<Utc>>` (chrono, not our ordinal `Day`) and differs on id fallback. Adopting it would **silently move document ids** — the one thing a swap in this crate must never do.

**Decision unchanged: skipped**, now resting on cost and correctness rather than on a compiler we no longer run.

### 6b. Why `texting_robots` was NOT adopted (v0.7/T2)

The same three-clause shape, run against the crate the task named as "the noted drop-in."

1. **Builds on 1.91? PASSES.** It compiles cleanly.
2. **Transitive footprint? FAILS, and disqualifyingly.** It resolves **45 transitive crates** into `intel-compliance`, which today has **one** dependency (`tokio`) — 7 crates in its whole tree. Worse than the count: it pulls `url` → `idna` → `idna_adapter` → **`icu_collections` / `icu_normalizer` / `icu_properties` / `icu_provider` 2.2.0, all declaring `rust-version = 1.86`.** Those are *the exact crates* that walled this project for two cycles (§5). And `intel-compliance` is a **non-optional dependency of `intel-ingest`, which is in the default build graph** — so adopting it would have dragged the icu chain into the **offline** build and silently raised the offline MSRV from 1.75 to 1.86, destroying the very property v0.6.2 fought for and `rust-toolchain.toml` still promises. *We would have re-created the disaster we had just finished cleaning up, in the name of compliance.*
3. **Does it change any existing allow/deny outcome? NO — and this is the clause that paid for the whole evaluation.** Rather than take the dependency, `texting_robots` was used **out of tree, once, as a differential oracle** against the hand-rolled parser: **16 `robots.txt` bodies × 22 paths + crawl-delay = 368 verdicts, 0 divergences.** Wildcards, `$` anchors, `Allow` exceptions, equal-specificity ties, longest-UA-token-wins, a `User-agent` line after a rule starting a *new* group, empty `Disallow:` meaning allow-all, comments-only files, rules before any UA line, and an HTML error page served as a 200 — all agree.

**Decision: skipped.** We shipped a **zero-new-dependency** parser (`async-trait` was already in the graph; the `Cargo.lock` diff is **one line and zero new crates**, versus 45) that is *proven* equivalent to the battle-tested one. The correctness assurance was the valuable part of the crate; the dependency was the expensive part. We took the first and left the second.

### 6c. Why LSH banding was BUILT, MEASURED, and REJECTED (v0.7/T5)

`docs/T8-scale-design-note.md` called LSH "the swap most likely to be needed first." That was a **hypothesis about where the time goes**, and T5's gate demanded exact recall at hamming ≤ 16. So it was built and measured (`cargo run --release -p intel-extract --example dedup_bench`, committed). **Both halves of the hypothesis are false.**

| n | simhash (linear) | pairwise scan (quadratic) | scan share | banded LSH | pairs still compared | recall |
|---|---|---|---|---|---|---|
| 1,000 | 69.6 ms | 1.3 ms | 1.8% | 90.2 ms | 76.2% | 100% |
| 5,000 | 359.7 ms | 31.7 ms | 8.1% | 5,801 ms | 76.1% | 100% |
| **10,000** | **734.3 ms** | **125.9 ms** | **14.6%** | **30,962 ms** | **76.1%** | **100%** |
| 20,000 | 1,473.9 ms | 509.8 ms | 25.7% | **OOM (~4.5 GB)** | — | — |

1. **The quadratic scan is not the bottleneck.** At n = 10k it is **14.6%** of dedup time. The other **85%** is *fingerprinting* — `dedup_near` recomputes `simhash()` for every document on every call. A hamming comparison is one XOR and a popcount (~1 ns); fingerprinting a 2 KB body costs ~70 µs. The quadratic term does not overtake the linear one until roughly **n > 100k**. We were about to optimize the cheap half.
2. **Banding cannot prune at this threshold anyway — and this is arithmetic, not implementation.** `dedup_max_distance` is **16** on a **64-bit** fingerprint. Exact recall requires, by pigeonhole, *more bands than the distance* (b ≥ 17), so bands are 64/17 ≈ **3.8 bits** wide. A 4-bit band has 16 possible values, so an average bucket holds n/16 of the corpus and nearly everything collides with nearly everything. Measured: it still compares **76% of all pairs** and runs **246× slower** than the scan it replaces. Recall *is* exactly 100%, as the math promises — **the index is correct and useless.** At n = 20k the candidate set alone tries to allocate ~4.5 GB and aborts.

**The rule worth keeping:** *an LSH band's selectivity depends on the threshold as a **fraction** of fingerprint width, not its absolute value.* 16/64 = 25% divergence is far outside the regime where any exact Hamming index beats a linear scan. Widening the fingerprint does not help if the threshold widens with it; it helps only if the *absolute* distance stays at 16 (e.g. 16/128), and that is **a different similarity rule** — it changes which documents are duplicates, which is corpus corruption, not an optimization. T5's gate says stop, and it was right to.

**Decision: not merged.** The design note has been corrected in place, and the swap it should have named — **persist the fingerprint** — is now the recommendation in §4.

### 6d. Why non-loopback `CORE_BIND` has no override (v0.11/BIND-LOOPBACK)

**Decision:** resolve `CORE_BIND`, require every result to be loopback, and
refuse startup if any address is not. There is deliberately no warning-only
mode and no override environment variable. An override would preserve the
original unauthenticated remote-exposure defect behind one extra setting. A
real requirement to bind beyond one host is the documented multi-host seam
trigger: it needs a design task that defines transport authentication,
authorization, and deployment topology before the boundary can move.

`CORE_TOKEN` remains optional. With loopback enforced structurally, the token
is defense-in-depth against unrelated local processes, not the mechanism that
makes the core private and not a substitute for shell entitlement. Making it
mandatory would break existing same-host deployments while adding no remote
protection beyond the enforced bind. Operators that need the extra local
boundary may continue to set it; the shipped launcher and service contract are
unchanged.

### 6e. Why `/embeddings/missing` has no HC2 exception (v0.11/SECTOR-BIND)

**Decision:** take the preferred sector-bound outcome. `/embeddings/missing`
enumerates document bodies, so it now requires an explicit sector list and
enforces it in core SQL just like `/docs`; HC2 has zero unnamed or named
body-returning exceptions. The alternative maintenance exception was rejected
because the predicate is cheap and an exception would preserve the broader
enumeration seam that triggered this task.

The embedding worker sends the core's full configured sector set, not the
current subscriber's entitlements. Backfill is archive maintenance and must
not become dependent on which subscriber runs first; the explicit full set
keeps that intent visible while the core still refuses an empty scope. `/docs`,
by contrast, receives the current subscriber's entitled sectors because it
serves that subscriber's downstream enrichment path.

### 6f. Why network reach and publisher policy remain runtime-checked (v0.11/GATE-CLOSED)

**Decision:** reject `Reach::Network` plus `robots_cache: None` at the shared
gate rather than redesign `SourceContext` in this patch cycle. The type-level
alternative would make that state unrepresentable, for example by separating
offline and network contexts or coupling reach and cache in an enum. It would
also change the connector trait boundary and every fixture, cursor, registry,
and builder call site even though the shipped net builder already constructs
the cache correctly.

That broader migration is deferred because its boundary cost is disproportionate
to this dormant single-field omission seam. The runtime check sits at the last
shared point before every network fetch, has a dedicated error, and is covered
by the inverted defect control. If new connector kinds make context construction
harder to audit, the type-level design should be reconsidered as its own
architectural task rather than folded into this narrow correction.

### 6g. Why private-network coordinates are documentation, not credentials (v0.12/INFRA-POLICY)

**Decision: Option A, selected by the operator on 2026-07-27.** The repository
may document RFC 1918 host `192.168.0.192` and loopback-forward ports such as
`18080`/`18081`; neither grants access without already having the operator's
LAN or local-machine route. The enforceable prohibition is against
secret-bearing material: tracked `.env` files, provider keys, tokens, private
key material, concrete long bearer values, non-placeholder secret assignments,
and raw secret-bearing response fields.

The v0.11 standing clause saying that the host and forwarded ports “appear in
no committed file” was false when written and unexecuted for its entire life.
v0.12 E0's tracked-path scan found 11 matching paths, including the already
committed `.env.example`, `README.md`, `shell/tests/test_llm_config.py`,
`PROGRESS-v0.9.md`, and `STATE.md`; ten of the 11 predated the v0.12 runbook.
No guard ever evaluated that clause. Option B was rejected because no specific
threat model makes private coordinates confidential, while append-only
historical records would make a host/port ban permanently incomplete.

Registered invariant R4 now scans every Git-tracked text file and makes the
credential rule executable. The clean tree passes. In a detached scratch
worktree, a planted fake `sk-proj-…` provider key at `README.md:1` produced
`invariant-scan: R4 FAIL: README.md:1: provider-key-shaped value`; the scratch
worktree was then removed.

### 6h. Why model-profile authority is L1 now and L2 scheduled (v0.12/OPS-AUTHORITY)

**Decision: L1 now, L2 scheduled, selected by the operator on 2026-07-27.**
Free-form remote transition strings were rejected because the standing
authorization named a narrow lifecycle while the mutable controller could
construct arbitrary shell. L1 converts transitions to structured tuples and
routes every remote payload through one compiled allowlist before SSH. It is
offline-testable, and planted lifecycle, creation, destructive-path, and
unknown-container commands prove the boundary can refuse.

Hash-pinning both executable surfaces and byte-comparing the policy copies make
edits visible, but they do not make L1 invariant under an agent that edits the
controller and its pin together. That residual is accepted temporarily and
stated without qualification. L2 is scheduled for the next
operator-authorized server-administration session, before any additional model
profile is admitted. Its forced-command `authorized_keys` wrapper must be
tested from both directions so the server, rather than the Mac controller,
enforces the lifecycle set. This is the operations analogue of A4; it neither
narrows nor closes A4's core-shell trust boundary.

### 6i. Why publisher-granted reuse is `PublisherPermitted` and a minor release (v0.25/LICENSE-SEMANTICS)

**Decision: extend/minor, selected by the operator on 2026-07-30.** The
licensing enum names the ground for redistribution: public domain, a CC grant,
client ownership, or a publisher's own express permission. SEC's measured
statement supports the fourth ground without establishing any of the first
three. `IndexOnly` was rejected as a supposedly conservative default because it
would record a restriction opposite to the measured permission and would
forfeit the only prospective real-content exercise of the redistributable
branch.

`PublisherPermitted` is redistributable and makes no underlying-copyright
claim. Its config, public, and SQLite spelling is exactly the Rust identifier.
The core control enumerates all five variants and proves the existing four
spellings, redistribution outcomes, and attestation outcomes did not move.
SQLite's existing unconstrained text mapping required no production edit; its
integration control proves both the new round trip and the safe
unknown-row-to-`IndexOnly` fallback.

The release is minor because adding a value to an existing public field changes
the contract seen by exhaustive consumers even when the route and body shape
stay fixed. The symmetric dated rule now lives in `AGENTS.md §5` and is
reconciled in `ARCHITECTURE.md §8`. It is intentionally prose adjudicated at
R-CLOSE: no source scan can decide whether a semantic value was added, removed,
or redefined, so no new invariant rule or vacuous planted control was created.

### 6j. Why SEC terms stay operator-adjudicated (v0.25/TERMS-GATE)

**Decision: affirmative identity; operator-owned terms review, selected
2026-07-30.** The SEC publishes two separate facts: its Internet Security
Policy refuses “unclassified” automated tools, while its Webmaster FAQ directs
programmatic EDGAR downloaders to declare an organization-and-contact
User-Agent. It publishes no glossary or registration state that the product can
query. The operator confirmed that the structurally required contact is
monitored and therefore determined that the current identity satisfies the
published direction for the reviewed SEC path.

A runtime terms boolean was rejected because it would turn publisher-specific
natural-language judgment into an asserted machine decision without a
machine-readable input. The executable boundary remains the fetched
`robots.txt` plus the operator deny-list; a dated publisher-specific operator
review owns the additional terms determination before admission. This is
narrower and more truthful than calling robots permission terms permission, and
it generalizes nothing from the SEC to another publisher.

### 6k. Why observed feed shape is affirmative without a parser-success claim (v0.25/FEED-SHAPE)

**Decision: the shape gate is affirmative; parser success remains unmeasured.**
E0 found no mandatory per-item field in the repository RSS parser. The one
authorized feed response contained 200 items; every optional field except
`author` was present and non-empty in all 200, and `author` was absent in all
200. The empty mandatory set is therefore satisfied, and Step 5 may reach its
separate admission decision.

That result does not turn an independent XPath count into a repository-parser
test. Step 4 deliberately did not run the parser against the body. Its behavior
record is conditional and derived from the already-measured source branches;
parser execution belongs to admission testing. Keeping those claims separate
preserves HC13's distinction between observed wire shape and program behavior.

### 6l. Why the admitted SEC source fails closed when robots policy is absent (v0.25/ADMIT)

**Decision: admit with `robots_on_missing: "deny"`, selected by the operator
on 2026-07-30.** The reviewed publisher serves a `robots.txt`, and both v0.24
and the fresh v0.25 Step 4 request measured the intended path as allowed.
Admission therefore binds to the presence and evaluation of that policy.
Treating a future 404 as permission would introduce a new condition never
reviewed; it does not follow from today's allow verdict.

The arXiv `allow` setting is a narrow absence-only exception for a
standards-designed harvesting endpoint that served no policy. It is not a
default for network sources. SEC remains on the conservative branch: missing
policy denies, an explicit disallow denies, and an unreachable origin denies.
The configured source establishes none of those live outcomes by itself; the
first live RSS harvest remains separately deferred to v0.26.

## 7. Run reference

```bash
# toolchain (v0.6.2 claim, retained): offline needs >= 1.75; --features net needs >= 1.86.
# current correction: offline needs >= 1.78; net >= 1.86 is executed by paired 1.86-pass / 1.85-declared-MSRV-refute lanes.
# Ubuntu 24.04 ships both, no rustup required:
apt-get install -y rustc-1.91 cargo-1.91
export PATH=/usr/lib/rust-1.91/bin:$PATH
cargo build -p cored --features net --locked            # live HTTP; builds since v0.6.2

cargo run -p cored                                     # core on :8788
pip install -r shell/requirements.txt
PYTHONPATH=shell python3 -m intel_shell.pipeline --client acme-research
PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787   # public API on :8787

# with the mock LLM (embeddings + /v1/ask):
python3 tools/mock_openai.py &
LLM_BASE_URL=http://127.0.0.1:8899/v1 PYTHONPATH=shell python3 -m intel_shell.pipeline

cargo test && PYTHONPATH=shell python3 -m pytest shell/tests   # v0.6 baseline: 49 Rust + 69 shell; v0.30 measured: 146 Rust + 317 shell

# v0.6 — per-source ingest (the `sources` filter is optional; omit it for whole sectors):
curl -X POST localhost:8788/ingest -H 'content-type: application/json' \
     -d '{"sectors":["technology"],"sources":["techwire"]}'
PYTHONPATH=shell python3 -m intel_shell.scheduler --dry-run   # per-source + per-sector jobs
PYTHONPATH=shell python3 -m intel_shell.scheduler --once      # run due jobs (cron/systemd)

# v0.5 — hashed keys + billing webhook:
PYTHONPATH=shell python3 tools/hash_subscriptions.py config/subscriptions.json \
  --out config/subscriptions.hashed.json
SUBSCRIPTIONS_PATH=config/subscriptions.hashed.json BILLING_WEBHOOK_SECRET=whsec_… \
  PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787

# v0.6 (T6) — key rotation, Stripe, SQLite-backed subscriptions:
PYTHONPATH=shell python3 tools/admin_keys.py list
PYTHONPATH=shell python3 tools/admin_keys.py rotate \
  --client acme-research --new-key ak_NEW --grace 86400   # omit --grace = revoke now
PYTHONPATH=shell python3 tools/migrate_subscriptions.py config/subscriptions.json \
  --to sqlite:///var/lib/intel/subs.db
SUBSCRIPTIONS_PATH=sqlite:///var/lib/intel/subs.db STRIPE_WEBHOOK_SECRET=whsec_… \
  PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787   # POST /v1/billing/stripe

# T7, when a real LLM endpoint exists (this is the whole deferred checklist):
LLM_BASE_URL=http://vllm-box:8000/v1 LLM_API_KEY=… \
  PYTHONPATH=shell python3 tools/verify_llm.py
```

**Env — core:** `CORE_CONFIG` `CORE_ENTITIES` `CORE_DB` `CORE_BIND` `CORE_TOKEN`.
**Env — shell:** `CORE_URL` `CORE_TOKEN` `SUBSCRIPTIONS_PATH` (a path, or `sqlite:///…`) `LLM_BASE_URL` `LLM_API_KEY` `LLM_CHAT_MODEL`/`LLM_EMBED_MODEL`, `API_KEY_PEPPER`, `BILLING_WEBHOOK_SECRET`; **new in T6:** `STRIPE_WEBHOOK_SECRET` (unset ⇒ `/v1/billing/stripe` returns 503), `STRIPE_PRICE_SECTORS` (JSON price→sectors map, so entitlements follow what was purchased).

**Note (T9.6):** the default subscriptions path is now anchored to the repo root rather than the process CWD — `uvicorn intel_shell.app:app` launched from anywhere but the repo root used to silently find zero clients and 401 every request.

**Scheduler config (`config/schedule.json`) — v0.6 shape:** a job's `sources` map is now **source id → cadence** (true per-feed clocks: `techwire` every 900s and `osdaily` every 1800s, though both live in `technology`), and the new `sectors` map is **sector id → cadence** for whole-sector jobs. A job with neither runs a single full pipeline.
