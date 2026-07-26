# TASKS-v0.10.3-EXECUTION.md — evidence-correction runbook for Codex

v0.10.3 is an **evidence-correction cycle**. v0.10.2 closed locally (annotated
tag object `d821f8b2eb6f39fe4a7d06a88cd61de771c7b0ba` dereferencing to release
commit `7d127abac0b993c9e98294ee1c03ff01153de9d0`, closing audit commit
`6a7070b9…`) with a green 19-job local matrix, 156/156 shell tests on both
Python lanes, golden 11/11, protected artifacts 2/2, three matching evidence
pins, a 69/69 checklist with zero exemptions, and — for the first time — seven
**authenticated** hosted CI-runner receipts accepted with zero rejections.

The v0.10.2 self-audit is **accurate**. All three findings reproduce against the
shipped tree, and every reported pass holds. It was also right to withhold
publication: `v0.10.2` is mechanically closed but not publication-ready.

The three findings share **one root cause**, and this cycle is organized around
naming it: *the guards were strengthened at the point of acceptance, but the
strengthening is optional, the accepted record is lossy, and nothing re-derives
it.* v0.10.2 built the right machine and then left the switch off. Concretely —
the authenticated tier exists but no release gate requires it; the matrix guard
counts receipts instead of identifying them; the accepted report drops the
identity fields that would let anyone re-check either claim; and the receipts and
bundles it rests on were never committed. This is the project's own doctrine
(`AGENTS.md §0` — a claimed property that nothing executes is not a property)
raised one level again: **a guard that the release path can decline to run is not
a guard, and evidence that cannot be re-derived from committed bytes is not
evidence.**

This cycle does five things and deliberately no more:

1. **identifies the matrix instead of counting it** — receipts must cover an
   exact set of `(job, matrix)` identities, and duplicate subjects are refused;
2. **makes authentication non-optional on the release path** — a release-grade
   receipt cannot be produced, pinned, or accepted in structural-only mode;
3. **enforces one-way classifier invariants on resume** — a resumed attempt
   whose overlap and violation fields contradict its label halts instead of
   being reused;
4. **makes the accepted record durable and re-derivable** — pin the signer
   revision, preserve every receipt identity field, and commit and hash-pin the
   raw receipts and Sigstore bundles;
5. **closes the recurring stale-cycle-literal class for good** — it escaped
   `AGENTS.md` into `tools/` and stamped the v0.10.2 evidence artifact with a
   v0.10.1 label.

It ships no new ingestion source, no subscriber-facing surface, no runtime or
public-API change, and no change to the golden regression. **Golden stays 11/11
byte-identical through every task in this file.** The default disposition at
R-CLOSE is a **patch release `v0.10.3`**.

---

## Entering state (asserted, not yet verified)

Taken from `STATE.md` (v0.10.2), the Codex closing report, and the v0.10.2
self-audit. **Every sentence here is a hypothesis until Step 1 (E0) measures
it.** Prior measurement is not permission to skip the entering-state run —
including when the prior measurement is your own or your predecessor's.

- Worktree clean; `./run ci-local` **19/19**; golden **11/11**; protected
  evidence **2/2 exact**; **3/3** evidence pins match; `cycle-check` reports the
  v0.10.2 runbook **closed**; `checklist-audit` **69/69** with zero exemptions.
- Rust **99 workspace / 20 net** tests, 0 rustc warnings. Python **3.11 and 3.12:
  156 shell tests each**; **21/21** exact packages on both interpreters.
- Release commit `7d127abac0b993c9e98294ee1c03ff01153de9d0`; annotated tag object
  `d821f8b2eb6f39fe4a7d06a88cd61de771c7b0ba` (`v0.10.2`), **local only**. HEAD is
  the later append-only audit commit `6a7070b9…`.
- Remote `main` is `817e7f3e…`. **No remote `v0.10.2` tag exists and none is
  authorized.** `v0.10.1` was published unchanged as authorized; its tag object
  `8ded63f79ed12b4180e8bcd0bcff4ef30a080a79` still dereferences to
  `e5af6bc5df8261cc004bd4d3247b70f8cbe930bb`.
- Hosted success run **30194678764** (seven jobs, both real shell matrix legs);
  hosted failure control **30194605219** (both planted shell failures rejected).
- Three hash-pinned evidence artifacts, independently re-hashed and confirmed
  byte-exact during review:

  | Pinned path | Bytes | sha256 |
  |---|---|---|
  | `evidence/v0.10.1/deferred-audit/report.json` | 27,786 | `00cf14ae…` |
  | `evidence/v0.10.1/real-model-adversarial/report.json` | 62,978 | `beec8bfa…` |
  | `evidence/v0.10.2/deferred-audit/report.json` | 28,968 | `4e11a8b3…` |

### Defects this runbook is drafted against (verify, do not trust)

Each was read out of the shipped tree on 2026-07-26 by path and line and is a
hypothesis until E0 confirms or refutes it. **G1, G3, and G4a** correspond to the
three v0.10.2 self-audit findings. **G2, G4b, G5, and G6** are additions from
independent re-verification and must be honored alongside them.

| # | Location | Claim to verify |
|---|---|---|
| **G1** [P1] | `tools/audit_deferred.py:45`, `:952-964` | `EXPECTED_RUNNER_JOB_COUNTS` declares `shell: 2` as a **count**, and `actual_counts` computes `sum(receipt["job"] == job)`. Two authenticated copies of the *same* Python 3.11 receipt therefore satisfy the claimed 3.11/3.12 matrix. There is no duplicate-subject rejection. |
| **G1** [augment] | `tools/audit_deferred.py:775-783`, `:875-878` | `required` omits `matrix`, so the field `ci.yml:410` emits is never validated; and `accepted = {"path": …, **{field: receipt[field] for field in required}}` **drops** it from the report. Only the `shell` job emits `matrix` at all — the fix must tolerate its absence on single-leg jobs and require its exact value on matrix jobs. |
| **G1** [augment] | `shell/tests/test_deferred_audit.py:135-156` | `_receipt_matrix` builds `("core","golden","lint","msrv","net","shell","shell")` and `_receipt()` never writes a `matrix` key — so the positive test **encodes the defect**. The two shell receipts in the passing test are indistinguishable. |
| **G2** [P1] | `tools/audit_deferred.py:1580-1584`, `:1620-1662` | `--require-attestations` is **opt-in and required by nothing**. `--expected-head` *is* enforced for production audits (`if not args.expected_head: raise`); authentication is not. It appears in no `./run` subcommand, no `ci.yml` job, and no release gate — `grep -rn require_attestations run tools .github shell/tests` returns matches only in `shell/tests/test_deferred_audit.py`. |
| **G2** [augment] | `tools/audit_deferred.py:978-983`; `tools/evidence_artifacts.py`; `:1365-1393` | The report records `attestations_required` and `attestation_verified`, but **nothing reads them**. `run_rederivation` compares row counts, source dispositions, and trigger texts — not the authentication posture. A future release receipt measured in structural-only mode would pin, validate, and re-derive identically. |
| **G3** [P2] | `tools/verify_llm.py:379-453` vs `:191-206` | `_completed_attempt_schema_valid` checks types and enumerated membership (`outcome in (GUARD_FIRED, NOT_EXERCISED, LEAK)`) but never cross-checks `outcome` against `public_overlap`, `raw_overlap`, or `violation_doc_ids`. The fresh path's truth table makes several of those combinations unreachable. |
| **G3** [augment] | `tools/verify_llm.py:475-509`, `:877-884` | `_resume_valid_attempts` halts only on a literal `outcome == LEAK`. The coverage check `len(report["attempts"]) == expected` bounds the *phantom-row* variant (46 ≠ 45 fails) but **not the substitution variant**: replacing a real cell's attempt with a tampered one under the same `(target_doc_id, shape)` key keeps the count at 45, conceals the leak behind a `NOT EXERCISED` label, and yields `WARN` once the positive control fires. Neither `target_doc_id ∈ battery.target_doc_ids`, nor `shape ∈ ADVERSARIAL_SHAPES`, nor `model` is bound to the report declaration. |
| **G4a** [P2] | `tools/audit_deferred.py:697-740` | `verify_attestation_bundle` invokes `gh attestation verify` with `--repo`, `--signer-workflow`, `--deny-self-hosted-runners`. It pins the workflow **path**, not the workflow **revision** — a workflow at the same path on any ref satisfies it. This matters more now than it looks: `ci.yml:57` checks out `inputs.audit_sha \|\| github.sha`, so the signing workflow ref and the audited commit are *deliberately different*. |
| **G4b** [P2] | `evidence/ci-runs/`; `evidence/v0.10.2/deferred-audit/report.json`; `tools/audit_deferred.py:679-694` | The accepted receipts record paths `evidence/ci-runs/30194678764-1-*.json`. **Those files are not in the repository** — `evidence/ci-runs/` holds only the older `30187058897-*` set, and no `.sigstore` bundle is committed anywhere. `_display_receipt_path` rewrites a temp `--runner-receipts-dir` into an `evidence/ci-runs/` prefix, so the committed record *reads* as if the bytes are tracked. Combined with the dropped `matrix` field, the **only** thing in the committed record distinguishing the two shell legs is a filename substring — which is exactly why the duplicated-leg control is undetectable after the fact. |
| **G5** [P2] | `tools/audit_deferred.py:1497`; `tools/cycle_check.py:225-256`; `run:957-959` | `"task": "v0.10.1 RECEIPT"` is hard-coded, so the **v0.10.2 evidence artifact is self-labeled v0.10.1** — and byte-pinned that way. `check_contract_cycle_paths` scans only `identity.declaration` (`AGENTS.md`) and only for `TASKS-v*-EXECUTION.md` / `PROGRESS-v*.md` filename literals; it never scans `tools/`, `run`, or bare version strings. Third consecutive cycle for this class (v0.10 vs v0.9; v0.10.1 §1/§5; now `tools/`). |
| **G6** [P3] | `TASKS-v0.10.2-EXECUTION.md:103-118` vs `:218-289` | The dated *Approved cycle-activation correction* block discloses two amendments (cycle activation; the PUBLISH dependency). It does **not** disclose that RCPT-AUTH's **Objective, Acceptance criteria, and “Done when” were rewritten in place** — including replacing “a fabricated one is provably refused” with “deliberately deferred until Step 6.” The rewrite was substantively correct. Undisclosed in-place edits to acceptance criteria are still how a runbook stops being a contract. |

**On G6, for the record:** the three disclosed v0.10.2 amendments were reviewed
and are **sound**. The cycle-activation correction was necessary — E0's clean-tree
gate genuinely cannot admit an untracked runbook — and it correctly refused to
launder preparatory work as E0 evidence. The PUBLISH restructure fixed a real
dependency the original draft got wrong: the hardened workflow must exist on a
published ref before it can attest a checkout of v0.10.1, and `audit_sha` is the
right mechanism. The RCPT-AUTH restatement is *more* honest than what it
replaced. G6 is about disclosure, not substance.

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task: check the gate first, implement, run and capture every
acceptance criterion, run `./run golden`, update `STATE.md`, append
`PROGRESS-v0.10.3.md`, check the box here, and commit. Implementation commit and
audit-record commit stay separate. Do not batch status updates.

- **🤖 = Codex executes and self-verifies end to end**, with no live model
  endpoint, no publication, and no push. These tasks' correctness is provable
  offline against synthetic evidence.
- **🧑 = exactly one named operator action or decision is required** (a clean
  worktree at the released commit, or explicit authorization to publish).

### Cycle activation (before E0)

`AGENTS.md` correctly declares the latest closed cycle, v0.10.2, and this runbook
arrives untracked. In a **separate preparatory implementation/audit pair** before
E0: commit this reviewed runbook, declare v0.10.3 active in the `AGENTS.md`
header, and create `PROGRESS-v0.10.3.md`. Run `cycle-check` and
`checklist-audit`. **Do not claim E0's test, golden, or artifact acceptance from
this preparatory correction.**

### Session opener (run before reading further)

```bash
git status --porcelain=v1
git describe --tags --always --dirty
git rev-parse HEAD
git remote -v
git rev-list --left-right --count origin/main...HEAD
git tag --list 'v0.10.*'
git ls-remote --tags origin 'v0.10.*'
sed -n '1,20p' AGENTS.md
sed -n '1,6p' STATE.md
```

### Global definition of done

Protected hashes exact; all **three** v0.10.x evidence pins still match
(`validate` re-hashes them and runs on runners); golden **11/11 byte-identical**;
`./run version-check` green; zero rustc warnings on offline and net builds; all
Rust tests green; all shell tests green under Python 3.11 **and** 3.12; clippy,
fmt, ShellCheck, floor byte-compilation, and locked Rust 1.78 green. No mock,
fixture, double, health response, hand-authored receipt, or workflow
configuration is promoted to wire evidence.

**The `ci-local` job count enters this cycle at 19.** G1, G2, G3, and G4 add tests
inside the existing `shell pytest` job; G5 strengthens assertions inside the
existing `active cycle consistency` job. If Step 6 adds a committed-receipt
integrity check that cannot live inside an existing job, it may raise the count to
20 — and if it does, the new count is recorded in `STATE.md` and
`PROGRESS-v0.10.3.md` **in the same task**, with the reason. **Every check this
cycle adds must run on `ci.yml` runners too, so it may touch only source, config,
and git — never the built `cored` binary or the protected DBs.**

---

## Deferred means deferred

None of the six standing deferral triggers fires in this cycle. The CI-runner
row's trigger — tightened in v0.10.2 to *an authenticated runner receipt set for
the released commit* — is **tightened again** here (identified matrix legs,
mandatory authentication, durable committed evidence), not implemented into a new
subsystem.

| Deferred item | Unchanged trigger | v0.10.3 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none |
| Postgres | a second archive writer | none |
| pgvector | exact cosine stops fitting the measured request budget | none |
| Multi-host seam hardening | an actual core/shell host split | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none |
| CI-runner evidence | **tightened** → an authenticated receipt set with *identified* matrix legs, durably committed | strengthen the guard and the record; do not fake a receipt |
| `/view` materialization | already fired in v0.10; promoted to a future implementation | none |

---

## Step 1 · E0 — Rebuild the entering state and re-confirm the six defects 🤖

**Objective.** Reproduce the v0.10.2 closed state from commands, and confirm or
refute G1–G6 against HEAD before changing anything.

**Gate.** If the worktree is not clean, or `git describe` does not resolve to the
v0.10.2 release commit `7d127aba…` or its append-only audit descendant
`6a7070b9…`, stop and report. Do not measure from an unknown subject.

**Steps.**

1. Capture the full offline matrix: `./run ci-local`, `./run golden`,
   `./run verify-artifacts`, `./run version-check`, `./run cycle-check`,
   `./run checklist-audit`, `./run progress-check`. Record exact counts.
2. Independently re-hash every pinned artifact and compare against
   `config/protected-artifacts.json` — do not accept `validate`'s own summary as
   the only witness.
3. Confirm or refute each defect **with captured command output**:
   - **G1** — `sed -n '45,53p;940,972p' tools/audit_deferred.py`;
     `sed -n '775,783p;875,879p' tools/audit_deferred.py`;
     `sed -n '135,157p' shell/tests/test_deferred_audit.py`. Confirm the count
     semantics, the omission of `matrix` from `required` and from `accepted`, and
     that `_receipt_matrix` emits two identity-free `shell` receipts.
   - **G2** — `grep -rn 'require.attestations' run tools .github shell scripts`
     (expect matches **only** in `shell/tests/test_deferred_audit.py`);
     `sed -n '1645,1662p' tools/audit_deferred.py` (expect `--expected-head`
     enforced, authentication not); `grep -rn 'attestations_required\|attestation_verified' tools run`
     (expect no reader outside the measurement that writes it).
   - **G3** — `sed -n '191,206p;379,455p;475,510p' tools/verify_llm.py`. Then run
     the substitution control in-process: take a committed valid attempt, set
     `outcome="NOT EXERCISED"`, `public_overlap=True`, `raw_overlap=True`, and a
     non-empty `violation_doc_ids`, and assert `_completed_attempt_schema_valid`
     currently returns `True`.
   - **G4a** — `sed -n '697,740p' tools/audit_deferred.py`; capture
     `gh attestation verify --help` and record **which** digest/ref policy flags
     the installed CLI actually exposes. Bind Step 6 to that captured output, not
     to this document's assumption.
   - **G4b** — `ls evidence/ci-runs/`; `find evidence -name '*.sigstore'`;
     `python3 -c "import json;print([a['path'] for a in json.load(open('evidence/v0.10.2/deferred-audit/report.json'))['measurements']['ci_runner']['accepted_runner_receipts']])"`.
     Confirm the recorded paths do not resolve on disk.
   - **G5** — `grep -n 'v0\.10\.1 RECEIPT' tools/audit_deferred.py`;
     `python3 -c "import json;print(json.load(open('evidence/v0.10.2/deferred-audit/report.json'))['task'])"`;
     `sed -n '225,256p' tools/cycle_check.py`;
     `grep -rn 'evidence/v0\.10' run`.
   - **G6** — diff the committed `TASKS-v0.10.2-EXECUTION.md` §Step 2 against the
     operator-supplied original and confirm the undisclosed Objective/Acceptance/
     Done-when rewrite.
4. Record the measured entering state in `STATE.md`.

**Failure-capable control.** E0 must be able to refute. If any of G1–G6 no longer
reproduces on HEAD, say so explicitly and strike that Step; do not perform a fix
whose precondition is gone.

**Acceptance criteria.** 19/19 · golden 11/11 · 2/2 exact + all three pins
`PIN MATCH` (independently re-hashed) · checklist 69/69 · each defect confirmed or
refuted by captured output · `gh attestation verify --help` captured verbatim ·
`STATE.md` re-stamped to the measured entering state.

**Done when** every downstream Step rests on a re-measured baseline, not on this
document's assertions.

---

## Step 2 · MATRIX-ID (G1) — Identify the matrix instead of counting it 🤖

**Objective.** Replace count-based completeness with an exact **identity set**.
The guard must require precisely one receipt per declared `(job, matrix)` pair,
reject duplicate subjects, and reject unknown or missing matrix dimensions.

**Gate.** Corpus-free and offline-provable — touches `tools/audit_deferred.py`,
`.github/workflows/ci.yml` receipt metadata, and synthetic-receipt tests only. Do
not weaken the release-commit, `success`, single-run, or ancestry checks; add to
them.

**Steps.**

1. Replace `EXPECTED_RUNNER_JOB_COUNTS` with an exact identity set —
   `EXPECTED_RUNNER_JOB_IDENTITIES = {("core", None), ("golden", None),
   ("lint", None), ("msrv", None), ("net", None), ("shell", "python=3.11"),
   ("shell", "python=3.12")}`. Keep the name in the report payload stable enough
   that `run_rederivation` still resolves, or migrate both sides in this task.
2. Add `matrix` to the validated fields with **absence-aware** semantics: a
   single-leg job must not carry `matrix`; a matrix job must carry exactly one of
   its declared values. Reject an unknown value, a missing value on a matrix job,
   and an unexpected value on a single-leg job — each with a distinct reason
   string.
3. Reject duplicate subjects. Two receipts resolving to the same `(job, matrix)`
   identity is a `matrix_findings` entry, not a silently-counted pair. Also
   reject two receipts with identical content digests regardless of filename.
4. Preserve identity in the accepted record. Add `matrix`, `workflow`,
   `repository`, and `event_sha` to the fields carried into
   `accepted_runner_receipts` (this is the half of G4b that lives here).
5. Fix the complicit fixture. `_receipt()` gains a `matrix` parameter;
   `_receipt_matrix` emits `shell` receipts at `python=3.11` and `python=3.12`.
6. Tests (synthetic, corpus-free, so they run on `ci.yml`) — extend
   `shell/tests/test_deferred_audit.py`:
   - **the permanent duplicated-leg control**: two authenticated copies of the
     Python 3.11 receipt (distinct filenames, valid bundles, same identity) must
     produce `observed_runner_executions == 0`, `single_run_matrix_complete
     == False`, a duplicate-subject `matrix_findings` entry, and `defer`.
     Fail-before/pass-after against the pre-change guard;
   - a `shell` receipt with **no** `matrix` field → rejected;
   - a `shell` receipt with an **unknown** `matrix` value (`python=3.13`) →
     rejected;
   - a `core` receipt that **carries** a `matrix` field → rejected;
   - the complete identified matrix (7 distinct identities) → promotes, and the
     accepted rows carry `matrix`/`workflow`/`repository`/`event_sha`.

**Failure-capable control.** The duplicated-leg control is the one that matters:
it must fail against the v0.10.2 guard and pass against the v0.10.3 guard, with
both outcomes captured in `PROGRESS-v0.10.3.md`.

**Acceptance criteria.** Completeness is an identity set, not a count · duplicate
subjects and duplicate digests rejected · absence-aware `matrix` validation with
distinct reasons · identity fields preserved in the accepted report · the
duplicated-leg control demonstrated fail-before/pass-after · synthetic tests pass
on 3.11 and 3.12 · golden 11/11 · protected 2/2 + 3/3 pins match.

**Done when** the guard can prove the claim RCPT-AUTH stated: that both real
Python matrix legs were present, rather than that two files said `shell`.

---

## Step 3 · AUTH-REQUIRED (G2) — Make authentication non-optional on the release path 🤖

**Objective.** v0.10.2 built the authenticated tier and left it opt-in. Make it
impossible to produce, pin, or accept a **release-grade** receipt in
structural-only mode, and make the posture re-derivable from the committed bytes.

**Gate.** Corpus-free and offline-provable. Structural-only mode must **remain
available and remain token-free** for local and runner use — the point is not to
require network everywhere, it is to stop a structural-only report from being
mistaken for, or pinned as, a release receipt. Do not make `ci.yml` require a
token.

**Steps.**

1. Make the posture explicit at the CLI. Add a required
   `--evidence-grade {structural,release}` argument to production audits.
   `release` implies `--require-attestations` and errors without
   `--attestation-bundles-dir`, `--expected-repository`, and
   `--expected-workflow`. `structural` is permitted but stamps the report
   accordingly.
2. Record the posture where it cannot be lost. Write `evidence_grade` alongside
   `attestations_required` at the report top level (not only inside
   `measurements.ci_runner`), and include every accepted receipt's
   `attestation_bundle` and `attestation_verified`.
3. **Make something read it.** Extend `committed_rederivation_snapshot` /
   `measurements_rederivation_snapshot` so `evidence_grade`,
   `attestations_required`, and the per-receipt `attestation_verified` flags are
   part of the re-derived comparison. A structural-only report that claims
   `release` must now fail `./run audit-deferred --rederive`.
4. Gate the pin. In `tools/evidence_artifacts.py`, add a `grade` field to each
   `pinned_files` entry and require that any artifact pinned as a
   release-grade deferred-audit receipt actually declares
   `evidence_grade == "release"` and `attestations_required == true`. `validate`
   must enforce this on runners, using only committed JSON — no DB, no corpus, no
   network.
5. Tests: a structural-only report pinned as release-grade → `validate` fails; a
   report claiming `release` with `attestations_required == false` → rederive
   fails; a genuine release-grade report → both pass. Assert the token-free path
   still works end to end so `ci.yml` is unaffected.

**Failure-capable control.** Take the committed v0.10.2 report, flip
`attestations_required` to `false` in a temporary copy, and show `--rederive`
now rejects it where the v0.10.2 tooling accepted it.

**Acceptance criteria.** `--evidence-grade` required on production audits ·
`release` implies authenticated verification · posture recorded at report top
level · re-derivation and `validate` both read it · structural-only remains
token-free and runner-safe · all controls demonstrated · golden 11/11 · protected
2/2 + 3/3 pins match.

**Done when** the sentence “this release receipt was authenticated” is enforced by
something that runs, rather than by the operator having remembered a flag.

---

## Step 4 · RESUME-INVARIANT (G3) — Enforce one-way classifier invariants on resume 🤖

**Objective.** Stop resume from accepting attempt states the fresh path cannot
produce. The schema currently validates *shape*; it must also validate
*consistency*, and bind each attempt to the report's own declaration.

**Gate.** Touches only `tools/verify_llm.py` and its tests — a harness, not the
product surface. Do not change the fresh-path classifier's truth table; derive
the invariants **from** it so the two cannot drift.

**Steps.**

1. Encode the fresh-path truth table (`verify_llm.py:191-206`) as one-way
   invariants checked on every resumed attempt:
   - `public_overlap` ⟹ `outcome == LEAK`;
   - `raw_overlap` ⟹ `outcome ∈ {GUARD_FIRED, LEAK}` — never `NOT EXERCISED`;
   - `outcome == GUARD_FIRED` ⟹ `raw_overlap` **and** not `public_overlap`
     **and** `violation_doc_ids` non-empty;
   - `outcome == NOT_EXERCISED` ⟹ not `raw_overlap` **and** not `public_overlap`;
   - `outcome == LEAK` ⟹ `raw_overlap` **or** `public_overlap`.
2. Add the telemetry cross-check: a `gated_match_telemetry.longest_common_gated_token_run`
   at or above `ATTEST_NGRAM` is inconsistent with `raw_overlap == False`.
3. Bind the attempt to the declaration: `target_doc_id ∈ report["battery"]["target_doc_ids"]`,
   `shape ∈ {s["id"] for s in ADVERSARIAL_SHAPES}`, and `model` equal to the
   declared chat model in `report["provider_roles"]`.
4. Choose the failure mode deliberately and state it in the code: an attempt that
   violates a **one-way invariant** is evidence of tampering, not transport
   noise — **halt** with a distinct error (as resumed `LEAK` does today) rather
   than silently discarding and re-running the cell. A silently-discarded
   contradiction is an unreported tamper signal.
5. Tests, each fail-before/pass-after:
   - the audit's control — `NOT EXERCISED` + both overlaps true + a violation ID
     → halts;
   - `GUARD FIRED` with empty `violation_doc_ids` → halts;
   - `LEAK` with both overlaps false → halts;
   - `longest_common_gated_token_run >= ATTEST_NGRAM` with `raw_overlap: false`
     → halts;
   - an out-of-battery `target_doc_id`, an unknown `shape`, and a mismatched
     `model` → each halts;
   - a genuinely consistent resume file still reuses all its attempts and the
     45-cell accounting is unchanged.

**Acceptance criteria.** All five one-way invariants enforced · telemetry
cross-check enforced · attempt bound to the declared battery, shapes, and model ·
contradictions halt with a distinct error · every control fail-before/pass-after ·
existing X-REGEN evidence still validates unchanged · golden 11/11.

**Done when** no resumed attempt can carry a label that contradicts its own
evidence, and the substitution variant the coverage check cannot see is refused
on its own terms.

---

## Step 5 · EVIDENCE-DURABLE (G4a + G4b) — Pin the signer revision and commit the raw evidence 🤖🧑

**Objective.** Make the accepted record independently re-checkable years from now:
bind verification to a workflow **revision**, and commit the bytes it rests on
instead of leaving them in artifact retention.

**Gate.** The digest-pinning half is 🤖 and offline-provable against a recorded
`gh attestation verify --help`. Downloading the hosted artifacts is 🧑 (it needs
the operator's authenticated `gh`). Do not invent flag names — use exactly what
E0 captured from the installed CLI.

**Steps.**

1. Extend `verify_attestation_bundle` to pass the source-revision policy flags the
   installed `gh` exposes (per E0's captured `--help`), threaded from new
   `--expected-source-digest` / `--expected-source-ref` arguments. If a needed
   flag is **absent** from the installed CLI, say so plainly in
   `PROGRESS-v0.10.3.md`, implement the strongest available binding, and record
   the residual gap — do not claim a binding the tool cannot make.
2. Persist the signer identity. Record the pinned source digest/ref and the
   verified certificate identity in each accepted receipt row, so the report
   states *which* workflow revision signed it.
3. Commit the raw evidence. Establish `evidence/ci-runs/<run_id>-<attempt>/` as
   the durable home for each run's seven receipts **and** their `.sigstore`
   bundles, and move the existing `30187058897-*` set into that layout in the
   same task so there is one convention, not two.
4. Stop the path-remapping fiction. `_display_receipt_path`'s
   `logical_receipt_root` rewrite must either resolve to a path that exists in
   the repository or record the true measurement path plus an explicit
   `logical_path` field. A committed record must never imply a tracked file that
   is not tracked.
5. Hash-pin the raw receipts and bundles in `config/protected-artifacts.json`
   with `purpose`/`provenance` naming the run id, and let `validate` re-hash them
   on runners.
6. 🧑 **Operator action, once:** download run **30194678764**'s seven receipts and
   seven bundles with authenticated `gh`, place them under the new layout, and
   confirm each bundle still verifies. If retention has already expired, record
   that as the finding it is — it is the exact argument for this Step — and pin
   only what survives.
7. Tests: a receipt whose recorded path does not resolve → rejected; a bundle
   whose source digest does not match the pinned revision → rejected (mockable
   verifier); `validate` re-hashes the committed receipts and bundles on a
   runner.

**Acceptance criteria.** Verification pins the workflow revision (or the residual
gap is recorded) · signer identity persisted in the report · raw receipts and
bundles committed under one convention and hash-pinned · no recorded path implies
an untracked file · controls demonstrated · golden 11/11 · pin count updated in
`STATE.md` in the same task.

**Done when** anyone with the repository alone — no GitHub account, no artifact
retention — can re-verify which runner produced the accepted evidence.

---

## Step 6 · LITERAL-NEUTRAL (G5 + G6) — Close the recurring stale-literal class 🤖

**Objective.** The stale-cycle-literal class has now recurred three cycles
running and has escaped the file `AGENTS-NEUTRAL` hardened. Remove the hard-coded
literal, widen the assertion to where the class actually lives, and add the
amendment-disclosure check that keeps a runbook a contract.

**Gate.** Source, docs, and one assertion. Do not change any invariant in
`ARCHITECTURE.md`. **Do not byte-edit the closed, pinned `v0.10.2` report** —
correct it by annotation, not mutation.

**Steps.**

1. Derive, don't hard-code. Replace `"task": "v0.10.1 RECEIPT"`
   (`audit_deferred.py:1497`) with a value resolved from
   `tools/cycle_identity.py`, or accepted as an explicit required argument. No
   cycle string is literal in `tools/`.
2. Correct the record without touching the bytes. Append a dated
   **`> **Closed-cycle status correction — 2026-07-DD.**`** banner —
   the form `cycle_check.HISTORICAL_BANNER_RE` already recognizes — to
   `PROGRESS-v0.10.2.md` and `STATE.md`, recording that
   `evidence/v0.10.2/deferred-audit/report.json` carries a `task` field of
   `v0.10.1 RECEIPT`, that the label is wrong, that the artifact is immutable and
   correctly pinned at `4e11a8b3…`, and that v0.10.3 derives the field. The pin
   does not move.
3. Widen the guard. Extend `check_contract_cycle_paths` (or add a sibling) to
   scan `tools/`, `run`, and `.github/workflows/` for cycle-specific literals —
   both the `TASKS-`/`PROGRESS-` filename forms **and** bare `v<major>.<minor>[.<patch>]`
   version strings in evidence paths and report labels — allowing them only
   inside the active declaration or an explicitly registered historical record.
   Update `run`'s usage examples, which still name `evidence/v0.10/…` and
   `evidence/v0.10.1/…`.
4. Add the amendment-disclosure assertion (G6). If the active runbook contains a
   dated correction block, `cycle-check` requires that each Step whose
   **Objective**, **Acceptance criteria**, or **Done when** differs from the
   committed original is named in it. Implement it the cheapest honest way: a
   `## Runbook amendments` section listing `Step N — <what changed> — <date>`,
   asserted to be non-empty whenever the runbook's tracked diff touches those
   headings after its first commit. If that assertion cannot be made executable
   in this cycle, **say so and record the gap** rather than shipping a
   documentation-only promise — the whole point of this Step is that a
   documentation-only promise is what failed.
5. Tests: a planted `v0.10.1` literal in `tools/` → `cycle-check` fails; a
   planted stale evidence path in `run` → fails; an undisclosed acceptance-criteria
   edit → fails; the clean tree → passes.

**Acceptance criteria.** Zero hard-coded cycle literals in `tools/` and `run` ·
`cycle-check` fails on a planted literal in each widened location · v0.10.2's
mislabeled artifact corrected by dated annotation with its pin unmoved ·
amendment-disclosure assertion executable **or** its gap explicitly recorded ·
golden 11/11.

**Done when** the class that has recurred three cycles running is caught by
something that runs, in every directory where it has actually appeared.

---

## Step 7 · RE-MEASURE — Produce the authenticated v0.10.3 receipt 🧑

**One operator decision: authorize the hosted dispatch that produces authenticated
evidence for the v0.10.3 candidate.** Everything else is Codex's.

**Objective.** Every guard above is inert until a real receipt passes through it.
Produce a fresh release-grade `evidence/v0.10.3/deferred-audit/report.json` under
the new identity, authentication, durability, and labeling rules.

**Gate.** Clean worktree at the v0.10.3 candidate commit. `--expected-head`
required. `--evidence-grade release` required. Never re-measure onto an existing
evidence path; never move the `v0.10.1` or `v0.10.2` tags.

**Steps.**

1. 🧑 Dispatch `ci.yml` from remote `main` with `audit_sha=<v0.10.3 candidate>`
   and `publish_evidence=true`. Confirm every expected job passes, each checkout
   is exactly the candidate, and each job emits one receipt **carrying its
   `matrix` identity** plus a persisted bundle. Capture run id and attempt.
2. Download the receipts and bundles into the Step 5 committed layout; confirm
   seven **distinct** `(job, matrix)` identities — this is the first live
   exercise of the Step 2 guard.
3. On a clean worktree at the candidate, run the production audit with
   `--expected-head`, `--evidence-grade release`, `--require-attestations`, and
   the Step 5 source-revision pin. Write `evidence/v0.10.3/deferred-audit/report.json`,
   confirm `{promoted:2, deferred:5}` and the restated CI-runner trigger, and
   hash-pin it.
4. Re-run `./run audit-deferred --rederive` on the new report and confirm the
   posture fields now participate in re-derivation (Step 3 exercised on real
   evidence).
5. **Negative control, on a throwaway branch only:** dispatch with one planted
   failing job and confirm the guard rejects the `conclusion:"failure"` receipt;
   then dispatch a duplicated-leg receipt set and confirm the Step 2 guard
   rejects it. Delete the branch. Never on a release commit or tag.

**Acceptance criteria.** Seven authenticated receipts with seven distinct
`(job, matrix)` identities accepted, zero rejected · both negative controls fire ·
new report is release-grade, correctly labeled, hash-pinned, and re-derives ·
raw receipts and bundles committed · golden 11/11 · protected 2/2 + all pins
match · `v0.10.1` and `v0.10.2` tags unmoved.

**Done when** every guard this cycle added has refused something real and
accepted something real.

---

## Step 8 · R-CLOSE — Close the cycle with one explicit release identity 🧑

**Objective.** Record the cycle's disposition and, if releasing, tag exactly one
commit.

**Gate.** Release only if the full definition of done holds, both Step 7 negative
controls fired, and no residual gap recorded in Step 5 or Step 6 is
publication-blocking. If a residual gap **is** publication-blocking, the correct
outcome is a recorded no-release with its trigger — as v0.10.2 correctly chose.

**Steps.**

1. Reconcile `README.md`, `CHANGELOG.md`, `STATE.md`, `ARCHITECTURE.md`, and
   `AGENTS.md` to the closing state; run `./run version-check`, `cycle-check`,
   `checklist-audit`, `progress-check`.
2. Append the **Cycle closing record** to this file: date, disposition, release,
   release commit, annotated tag object, and the per-Step implementation commits.
3. Record explicitly whether `v0.10.2` remains local and unpublished, and whether
   this cycle changes that. **`v0.10.2`'s local tag does not move under any
   circumstance.**
4. State the publication disposition for `v0.10.3` as a decision with a trigger,
   not a default.

**Acceptance criteria.** Release/no-release rationale recorded with its trigger ·
every diff path accounted for · checklist fully checked and `checklist-audit`
green · all pins match · golden 11/11.

**Done when** v0.10.3's disposition is a recorded, measured decision.

---

## Cycle checklist

- [x] **E0** — entering state re-measured at v0.10.2; G1–G6 confirmed or refuted; `gh attestation verify --help` captured
- [x] **MATRIX-ID** — completeness is an exact `(job, matrix)` identity set; duplicate subjects and digests rejected; duplicated-leg control fail-before/pass-after; identity fields preserved
- [x] **AUTH-REQUIRED** — `--evidence-grade` required; `release` implies authenticated verification; posture read by both `--rederive` and `validate`; structural mode still token-free
- [x] **RESUME-INVARIANT** — five one-way invariants + telemetry cross-check enforced; attempt bound to declaration; contradictions halt; all controls fail-before/pass-after
- [x] **EVIDENCE-DURABLE** — signer revision pinned (or gap recorded); raw receipts and bundles committed and hash-pinned; no recorded path implies an untracked file
- [x] **LITERAL-NEUTRAL** — zero cycle literals in `tools/` and `run`; guard widened; v0.10.2's mislabeled artifact corrected by annotation with its pin unmoved; amendment-disclosure assertion executable or gap recorded
- [x] **RE-MEASURE** — seven authenticated distinct-identity receipts accepted; both negative controls fired; release-grade report pinned and re-derived
- [ ] **R-CLOSE** — release disposition recorded with its trigger and, if applicable, `v0.10.3` tagged

---

## Standing prohibitions

- Do not mutate, delete, vacuum, or "refresh" `data/core.db` or
  `data/live-smoke.db`, and do not alter or re-pin the three existing v0.10.x
  evidence JSONs; their hashes are frozen. **This includes the `task` field of
  `evidence/v0.10.2/deferred-audit/report.json`** — it is corrected by dated
  annotation, never by byte edit. New evidence goes to fresh `evidence/v0.10.3/…`
  paths.
- Do not weaken the release-commit, `success`, single-run, ancestry, or
  attestation checks; the pin re-hash in `validate`; or the source-deterministic
  re-derivation. This cycle only strengthens the acceptance bar.
- Do not count two receipts as two matrix legs without two distinct identities,
  and do not accept a receipt a runner did not emit (HC13).
- Do not reuse a resumed adversarial attempt whose classifier fields contradict
  its label, and never silently reuse or silently discard a resumed contradiction.
- Do not record a receipt path that implies a tracked file which is not tracked.
- Do not re-tag `v0.10.1` or `v0.10.2`, rewrite published history, or push
  anything the operator has not explicitly authorized.
- Do not add a job or test that calls `production_measurements()`,
  `exact_cosine_measurement()`, `view_measurement()` benchmarks, or
  `verify-artifacts` unconditionally to `ci.yml` — runners have no built `cored`
  and no protected DBs. Guard corpus-dependent checks to skip on runnerless
  environments, and keep every new check token-free.
- Do not hand-edit `Cargo.lock` (HC12), raise the offline Rust 1.78 floor, lower
  the Python 3.11 floor, let core call an LLM (HC3), or change the `/v1/ask` or
  `/view` JSON bodies.
- Do not commit `.env`, provider keys, tunnel aliases, or raw secret-bearing
  responses. The `192.168.0.192` tunnel and its `18080`/`18081` local ports are
  operator infrastructure and appear in no committed file.
- Do not batch `STATE.md` / `PROGRESS-v0.10.3.md` updates or combine two tasks in
  one commit.
- **If any Step's Objective, Acceptance criteria, or "Done when" is amended after
  this file is first committed, name the amendment in a dated
  `## Runbook amendments` block in the same commit.** Undisclosed in-place edits
  to acceptance criteria are prohibited — that is G6.

---

## Provenance of this draft

Every defect above was read out of the repomix export of the v0.10.2 tree on
2026-07-26 by path and line, and each is written as a hypothesis for E0 to
confirm or refute — not as a settled fact.

**The v0.10.2 self-audit was independently verified and is accurate.** All three
findings reproduce: the matrix guard counts rather than identifies (`shell: 2` at
`audit_deferred.py:45`, `sum(receipt["job"] == job)` at `:952-964`, and a test
helper at `test_deferred_audit.py:142` that emits two identity-free `shell`
receipts); the resume schema validates enumerated membership without cross-checking
overlap or violation fields (`verify_llm.py:379-453` against the fresh-path truth
table at `:191-206`); and attestation verification pins the workflow path but not
its revision (`:697-740`). Its positive claims also hold: `require_production_subject`
genuinely validates hex format, exact HEAD, and clean worktree **before** any
measurement runs, and `--expected-head` is genuinely mandatory for production
audits; `ci-local` is exactly 19 jobs; and all three evidence pins re-hash
byte-exactly (27,786 / `00cf14ae…`; 62,978 / `beec8bfa…`; 28,968 / `4e11a8b3…`).
Its recommendation to withhold publication was correct.

Four things were added by independent re-verification:

- **G2 is the deeper P1 and subsumes G4a.** Pinning the signer revision is worth
  doing, but it does not matter while `--require-attestations` is optional.
  Authentication appears in no `./run` subcommand, no `ci.yml` job, and no
  release gate; nothing reads `attestations_required` or `attestation_verified`
  outside the tests; and `run_rederivation` compares dispositions and triggers
  but not posture. A future release receipt measured in structural-only mode
  would pin, validate, and re-derive identically to this one. **The authenticated
  tier is currently a claimed property that nothing on the release path
  executes** — the project's signature failure mode, in the very cycle that was
  meant to close it.
- **G4b makes G1 permanently unfalsifiable in the committed record.** The seven
  accepted receipts cite `evidence/ci-runs/30194678764-1-*.json`, but only the
  older `30187058897-*` set is tracked and no `.sigstore` bundle is committed
  anywhere. `_display_receipt_path` rewrites a temp directory into an
  `evidence/ci-runs/` prefix, so the record reads as though the bytes are
  tracked. Because `matrix` is also dropped from `accepted_runner_receipts`, the
  only surviving distinction between the two shell legs is a filename substring —
  which is precisely why the duplicated-leg control cannot be detected after the
  fact.
- **G5 is the third consecutive recurrence of the stale-literal class.**
  `"task": "v0.10.1 RECEIPT"` is hard-coded at `audit_deferred.py:1497`, so the
  v0.10.2 evidence artifact is self-labeled v0.10.1 — and byte-pinned that way.
  `AGENTS-NEUTRAL` is complete for its stated scope, but
  `check_contract_cycle_paths` scans only `AGENTS.md` and only for
  `TASKS-`/`PROGRESS-` filename literals; it never looks at `tools/` or `run`,
  whose usage examples still carry `evidence/v0.10/…` paths. The class was
  hardened in the one file where it had last been noticed rather than in the
  places it lives.
- **G6 concerns the runbook, not the code.** The committed v0.10.2 runbook
  rewrote RCPT-AUTH's Objective, Acceptance criteria, and "Done when" in place —
  including replacing "a fabricated one is provably refused" with "deliberately
  deferred until Step 6" — without naming that change in its dated correction
  block, which discloses only the cycle activation and the PUBLISH dependency.
  The rewrite was substantively correct and more honest than what it replaced.
  The problem is the silence: an acceptance criterion that can be edited to match
  the implementation, without a record, is not an acceptance criterion.

The through-line for this cycle: **v0.10.2 built the right guards and left them
optional, lossy, and unread.** G1 is a guard that counts instead of identifying;
G2 is a guard the release path may decline to run; G3 is a guard that checks
shape but not consistency; G4 is a record that cannot be re-derived from
committed bytes; G5 is a guard installed one directory away from the defect; G6
is a contract that can be edited to fit its outcome. Each is the same failure at
a different altitude: **a property is only real where something refuses to
proceed without it.**
