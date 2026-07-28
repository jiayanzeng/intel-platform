# TASKS-v0.16-EXECUTION.md — propagation, seam, and layout runbook for Codex

v0.16 has one theme: **a check that cannot fail is not a check — including the
harness that runs every other check.**

v0.13 made rules provably able to fire. v0.14 made each control prove *where* it
fired. v0.15 derived scope instead of asserting it, and registered **R10** to
prove the local and hosted check sets correspond.

R10 proved correspondence. **Nothing proved propagation.** `run`'s `ci_local_job`
invokes each job inside `if "$@"`, and every one of the 20 call sites is
`ci_local_job "…" fn || return $?`. Both constructs place the job in a context
where bash suppresses `errexit`, so a multi-command job function continues past
an internal failure and reports the status of its last command. Parity was
verified; exit propagation was assumed.

That is the same error shape the v0.13–v0.14 review lessons name — reading one
layer and inferring the next — now standing in the code rather than in a
directive. It is also why the reduction this cycle owes is not optional: the
apparatus grew for three cycles on a foundation that could not fail.

This cycle does five things and deliberately no more:

1. **moves the cycle documents out of the repository root** and gives their
   location one resolver;
2. **makes a failing `ci-local` job impossible to report as PASS**, and makes
   the runner's own help text describe what it actually does;
3. **reduces R10's enumerated exemptions to derived classes**, so the exemption
   count becomes an output of the parser rather than an input to it;
4. **closes the config-ownership seam violation** in shell enrichment;
5. **makes the `cored` test entry point relocatable.**

**The public `/v1/*` JSON bodies, the SQLite schema, and the golden
regression's 11 invariants are unchanged unless Step 5 states otherwise.
Golden stays 11/11 byte-identical through every task.**

**Version disposition — decided at Step 5, not inherited here.** Default is a
patch release **`v0.14.2`**, because Steps 2, 3, 4, and 6 touch harness, tooling,
tests, and documentation. **`v0.15.0`** applies if and only if Step 5 adds a
core-owned route, changes a `/v1/*` body, or otherwise moves an observable
surface. Record the fired trigger in Step 5.

**The cycle identifier and the release version are different things.** Cycle
v0.15 shipped `v0.14.1`; cycle v0.16 ships `v0.14.2` or `v0.15.0`. Do not rename
any cycle artifact to reconcile them. Step 2 records this convention in
`ARCHITECTURE.md` in one sentence so the next reader does not try to fix it.

---

## Entering state (asserted, not yet verified)

**Every sentence here is a hypothesis until Step 1 (E0) measures it.**

- `v0.14.1` is published. Annotated tag object
  `deea217b8913ae42399a22424dcf91595ce80240` dereferences to release commit
  `5c3b6d7fddc30b4691e1e1ee0a6e42831626a1ba`. `origin/main` is
  `fb2d501e850fd7c67045b83c475e089f5c5fa535`; publication run **30336006396**
  passed. Release evidence remains dispatch run **30333331839** attempt 1
  against the separate evidence candidate
  `6d197e562315b4fc6feb20c35b5fadc75b6b44a4`. **None of this is reopened.**
- v0.15 is closed: all eight checklist boxes checked, `Cycle closed: 2026-07-28`,
  `Release disposition: release (as of 2026-07-28)`.
- `./run ci-local` **20/20**; Rust **125** workspace / **48** net (**23**
  `intel-ingest` + **25** `cored`); shell **237/237** on Python 3.11.4 and
  3.12.13 with **21/21** exact packages; `invariant-scan` **10 rules / 18
  controls**; golden **11/11**; pins **116** (**114** evidence + **2**
  authorization); protected databases **2/2**; retractions **three**.
- **That 20/20 is conditional.** The audit at
  `0a25c50f9de6a020fa6a04b04847f6242b809f7e` reports 18 of 24 `cored` tests
  failing in the existing checkout because the cached test binary embeds a
  deleted absolute path, and passing under a fresh `CARGO_TARGET_DIR`. E0 must
  record which target directory produced its measurement.
- `A4`, the **editable-L1 controller residual**, the **stated R3/R4 open-bottom
  limitations**, and the **active-runbook measured-value heuristic limitation**
  all remain open. **L2** remains scheduled and is not executed in this cycle.
- **`ci-local` enters at 20 jobs and exits at 20.**

### Gaps this runbook is drafted against (verify, do not trust)

| # | Location | Claim to verify |
|---|---|---|
| **F1** [P1] | `run:26` (`set -euo pipefail`); `ci_local_job`'s `if "$@"; then`; all 20 call sites of the form `ci_local_job "…" fn \|\| return $?` | **A failing `ci-local` job can report PASS.** Both the `if` condition and the call-site `\|\| return $?` suppress `errexit` for the whole job function, so a multi-command body runs past an internal failure and returns its last command's status. The audit demonstrated five: `ci_net_test`, `cmd_golden`, `verify_fingerprint_fixture`, `ci_pytest`, `ci_deferred_evidence`. **Treat five as a lower bound, not the scope.** |
| **F1b** [P1] | `verify_fingerprint_fixture` | Its last command is `rm -rf "$fixture_dir"`. Under the suppressed context the function therefore returns `rm`'s status, which on an existing temp directory is **always 0**. This job is not merely mask-capable; verify whether it can fail at all. |
| **F2** [P2] | `shell/intel_shell/pipeline.py:140`; `ARCHITECTURE.md §2` | **The shell reads core-owned config directly.** `with open("config/entities.json", …)` during LLM enrichment bypasses the CoreClient seam, ignores `CORE_ENTITIES`, and depends on the process working directory. `ARCHITECTURE.md §2` assigns `config/entities.json` to **core**. Scheduled or CLI enrichment can therefore compare model output against a different gazetteer from the one `cored` loaded, or fall back to demo names. |
| **F3** [P2] | `apps/cored/src/main.rs` test helper using `env!("CARGO_MANIFEST_DIR")` | **The `cored` test binary embeds a compile-time absolute path.** With a shared or relocated `CARGO_TARGET_DIR`, the documented entry point fails against a checkout that is not the one the binary was compiled in. This is a verification-reproducibility defect, not a product failure — say which in the record. |
| **F4** [P3] | `run`'s `usage()`: *“ci-local execute the configured 19-job CI matrix, stopping on failure”* | **Two false claims in one line.** The matrix is 20, and “stopping on failure” is exactly the contract F1 breaks. Fixing the number without fixing the contract would leave the sentence false in the more important half. |
| **F5** [P2] | `config/invariant-rules.json` R10 control whose `find` literal is `  ci_local_job "net test (-D warnings)" ci_net_test \|\| return $?\n` | **R10's site control is coupled to the defective call-site shape.** Any Step 3 change to the call sites invalidates that literal. This is a coupling to handle in the same commit, not a finding. |
| **F6** [P3] | 15 `TASKS-*.md` and 11 `PROGRESS-*.md` at repository root; `root.glob("TASKS-v*-EXECUTION.md")`, `root.glob("TASKS-v*.md")`, `root.glob("PROGRESS-v*.md")`, `root / f"TASKS-{name}-EXECUTION.md"`, `root / f"PROGRESS-{cycle}.md"` across `tools/` and `shell/tests/` | **The document location is asserted at every consumer.** No pin in `config/protected-artifacts.json` names a root markdown file, so the paths are movable — but the location is restated at each call site, which is the same defect class as the last three cycles at the document layer. |

---

## Measured input from the review turn

These were **run**, not read, in the review session that produced this runbook,
on **GNU bash 5.2.21 (x86_64-pc-linux-gnu)**. The operator's shell may differ.
**Re-verify each on the operator's `bash --version` before relying on it.**

| Mechanism | Restores `errexit`? |
|---|---|
| `if fn; then …` | **No** — masks the failure |
| `if ( set -e; fn ); then …` | **No** — the commonly-cited subshell workaround does **not** work |
| `if ( set +e; set -e; fn ); then …` | **No** |
| `fn \|\| status=$?` | **No** |
| plain `fn` in a wrapper, wrapper called **plainly** | **Yes** — aborts at the failing command |
| plain `fn` in a wrapper, wrapper called with `\|\| return $?` | **No** — the call site alone is sufficient to suppress |
| `( fn ) & wait "$!"` inside a wrapper reached through `\|\| return $?` | **No** — the suppression is inherited by the subshell |
| `bash -euo pipefail -c '"$@"' _ fn` (**separate process**) | **Yes**, and it survives a `\|\| return $?` call site |

Two consequences the audit did not state, and which the fix must address:

1. **Fixing `ci_local_job`'s `if` alone changes nothing**, because every call
   site independently suppresses `errexit`.
2. A wrapper that keeps the job in-process only works if **both** the wrapper
   body and all 20 call sites are plain — and that design needs an `EXIT` trap
   for the summary, which `cmd_golden`'s own `trap … EXIT` was observed to
   replace. The separate-process design has neither constraint.

Choose whichever mechanism you can demonstrate; do not choose one this table
marks **No**.

---

## How to run this file

Execute top to bottom, one task and one commit at a time. Follow `AGENTS.md §5`
after **every** task. Implementation and audit-record commits stay separate. Do
not batch status updates.

- **🤖 = Codex executes and self-verifies end to end** — no live model endpoint,
  no live server session, no publication, no push.
- **🧑 = exactly one named operator action or decision.**

**Dependency gates.** Step 2 runs first, because every later step touches a path
or a document the reorganization moves. Step 4 is blocked by Step 3, because
R10's parser reads the call-site shape Step 3 rewrites. Steps 5 and 6 are
independent and may run in any order after Step 2. Step 7 is blocked by every
preceding implementation step. Step 8 is blocked by Step 7.

### Cycle activation (before E0)

This runbook arrives as `TASKS-v0.16-EXECUTION.md` **at the repository root**,
matching the glob the current tooling uses. Step 2 moves it. In a separate
preparatory implementation/audit pair: confirm the worktree is clean and
`origin/main` is `fb2d501e…`; commit **only** this runbook, the `AGENTS.md`
header declaring v0.16 active, and a new `PROGRESS-v0.16.md`; run `cycle-check`
and `checklist-audit`. **Do not claim E0's acceptance from this commit.**

### Session opener

```bash
git status --porcelain=v1
git rev-parse HEAD
git rev-list --left-right --count origin/main...HEAD
git tag --list 'v0.14*' --format='%(refname:short) %(objectname) %(*objectname)'
bash --version | head -1
sed -n '1,20p' AGENTS.md
sed -n '1,6p' STATE.md
```

### Global definition of done

Protected hashes exact; all **116** pins match until Step 7 adds more; golden
**11/11 byte-identical**; `./run version-check` green; zero rustc warnings on
offline and net builds; all Rust tests green; all shell tests green under Python
3.11 **and** 3.12; clippy, fmt, ShellCheck, floor byte-compilation, and locked
Rust 1.78 green. No mock, fixture, double, health response, hand-authored
receipt, or workflow configuration is promoted to wire evidence.

`invariant-scan` enters at **10 rules / 18 controls**. **Every rule and control
count after Step 3 is measured and recorded by the step that produces it, never
predicted here.** State counts as measured relations wherever a relation will do.

---

## Deferred means deferred

| Deferred item | Unchanged trigger | v0.16 action before the trigger |
|---|---|---|
| T7 robots single-flight | a second concurrent harvester | none |
| Postgres | a second archive writer | none |
| pgvector | exact cosine stops fitting the measured request budget | none |
| Multi-host seam hardening | an actual core/shell host split | none |
| A4 untrusted-shell boundary | a third-party/untrusted shell, or any claim HC1 is invariant under shell replacement | none — **Step 5 narrows a config seam, not A4; do not conflate them** |
| L2 forced-command wrapper | an operator server session | none — remains scheduled, not executed |
| R3/R4 open-bottom coverage | a provider or credential spelling outside registered vocabulary | none — the stated limitations stand and are not narrowed |
| CI-runner evidence | an authenticated receipt set with identified matrix legs, durably committed | **re-measure at the new release commit — discharged by Step 7** |

---

## Step 1 · E0 — Rebuild the entering state and confirm F1–F6 🤖

**Objective.** Reproduce the post-v0.14.1 state from commands, and confirm or
refute every gap against HEAD before changing anything.

**Steps.**

1. Run the full entering matrix: `./run ci-local`, standalone `./run golden`,
   `./run verify-artifacts`, `./run cycle-check`, `./run checklist-audit`,
   `./run progress-check`, `./run version-check`, `./run invariant-scan`.
   **Record the `CARGO_TARGET_DIR` each measurement used**, and whether a fresh
   one was required (F3).
2. **Reproduce F1 by derivation, not by example.** Parse `run` for every
   `errexit`-suppressing context around a function call — condition position,
   `&&`/`||` operand, `!` negation — and produce the complete list of job
   functions reachable through one. Then inject a failure into the **first**
   command of each and record which report PASS. The audit found five; report
   the derived number, whatever it is.
3. **Reproduce F1b specifically**: determine whether `verify_fingerprint_fixture`
   can return non-zero at all through `ci_local_job`, given its trailing
   `rm -rf`. Record the answer as yes or no, with the command that shows it.
4. **Re-verify the mechanism table above on the operator's bash.** Record the
   version and any row whose result differs. A differing row is a finding.
5. **Confirm F2** by reading `pipeline.py`'s enrichment path and
   `ARCHITECTURE.md §2`, and by showing what happens when `CORE_ENTITIES` points
   somewhere other than `config/entities.json`.
6. **Confirm F3** by building the `cored` tests in one checkout and running them
   from a relocated one, sharing `CARGO_TARGET_DIR`.
7. **Confirm F5** by locating R10's control literal, and **F6** by listing root
   markdown files and grepping every consumer of their paths.
8. **Test the hosted blast radius.** Determine whether `.github/workflows/ci.yml`
   reaches any check through `ci_local_job`. If every hosted step invokes its
   command directly, **F1 does not touch hosted evidence** — state that as a
   measured conclusion, because it is the fact that decides Step 1's last item.
9. **Record the disposition of the published record.** If hosted evidence is
   unaffected and the audit's independent re-runs all passed, then no published
   count is false and **no retraction is owed** — only a forward correction to
   `STATE.md`, which currently records the net-test case alone.

**Acceptance criteria.** Entering matrix captured in full with its target
directory named · F1 reproduced by derivation with the complete affected set ·
F1b answered yes or no · mechanism table re-verified on the operator's bash ·
F2, F3, F5, F6 confirmed or refuted · hosted blast radius measured · published
`v0.14.1` tag, commit, and all 116 pins unchanged and re-verified · golden 11/11.

**Done when** the scope of F1 is a measured set rather than an example list.

---

## Step 2 · DOC-LAYOUT (F6) — One location, one resolver 🤖

**Objective.** Move the cycle documents out of the root and stop restating where
they live.

**Gate.** `tools/cycle_identity.py` and every consumer of a document path, plus
`README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `repomix.config.json`, and
`.github/workflows/ci.yml` if either names a path. **No source under `crates/`
or `apps/` changes.**

**Target layout.**

```
docs/
  cycles/     every TASKS-v*.md and PROGRESS-v*.md, including this cycle's
  intel-platform-OPERATIONS.md
```

Root retains only `README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `STATE.md`,
`CHANGELOG.md`, and the build/config files (`run`, `Cargo.toml`, `Cargo.lock`,
`rust-toolchain.toml`, `repomix.config.json`, `.env.example`, `.gitignore`).

**Steps.**

1. State the retention criterion before moving: **root holds what a reader
   consults at the start of every session; everything else lives under `docs/`.**
   Apply it, and report any file whose classification is arguable rather than
   deciding silently.
2. `git mv` every cycle document into `docs/cycles/`, including this runbook and
   `PROGRESS-v0.16.md`. **Content must not change.** Capture SHA-256 for every
   moved file before and after and assert equality.
3. Give the location **one resolver**, in `tools/cycle_identity.py`. Every other
   tool and test imports it. **Do not introduce a second glob root, a manifest,
   or a fallback that searches both places** — a compatibility shim is a second
   location rule and reproduces the defect.
4. Derive the full consumer set by search rather than from F6's list; report any
   consumer F6 missed.
5. Record the cycle-identifier-versus-release-version convention in
   `ARCHITECTURE.md` in one sentence, with cycle v0.15 → `v0.14.1` as the example.
6. 🧑 **Optional, operator-supplied:** if `REVIEWER-LESSONS-v0.13-v0.14.md` is
   provided, commit it at `docs/REVIEWER-LESSONS-v0.13-v0.14.md`, so `AGENTS.md`'s
   two review-discipline rules cite a document that exists in the repository.
   Skip silently if it is not supplied.

**Acceptance criteria.** Every moved file byte-identical, demonstrated by hash ·
one resolver, no second location rule, no fallback search · `cycle-check`,
`checklist-audit`, and `progress-check` green with **identical totals and the
same three retractions** as Step 1 measured · all 116 pins validate unchanged ·
`repomix` still picks up `Cargo.lock` from project root · golden 11/11.

**Done when** adding a cycle document requires no edit outside `docs/cycles/`.

---

## Step 3 · JOB-PROPAGATION (F1, F1b, F4, F5) — A failing job cannot pass 🤖

**Objective.** Make it impossible for `ci-local` to report PASS for a job whose
body failed, and make the runner's help describe what the runner does.

**Gate.** `run`, `config/invariant-rules.json` (F5's control literal), the shell
tests that cover the harness, and `config/protected-artifacts.json` only for the
required forward update to the changed `run` authorization-surface pin. The
manifest path was added before implementation because leaving the old forward
pin would make `verify-artifacts` and `ci-local` fail; no historical manifest,
release commit, tag, evidence byte, or protected database changes.

**Steps.**

1. **Choose the mechanism against the measured table**, not against convention.
   Record which rows you re-verified on the operator's bash and why the chosen
   mechanism survives a call site that suppresses `errexit`. If you keep jobs
   in-process, you must fix **all 20 call sites and** the wrapper, and you must
   handle the `cmd_golden` `EXIT`-trap replacement observed in the review turn.
2. Implement it. `ci-local` must still print its per-job PASS/FAIL summary and
   still stop at the first failure — that is the contract `usage()` already
   claims.
3. **Cover every job by derivation.** The failure controls must be generated
   from the parsed job list, so a twenty-first job is covered without editing a
   test. A hand-written list of 20 controls is the defect this cycle is about.
4. **Resolve F1b explicitly.** If `verify_fingerprint_fixture` cannot fail
   because of its trailing `rm -rf`, fix the ordering so the cleanup cannot
   become the return value — and add that shape to the derived control set, not
   as a one-off.
5. **Update R10's coupled control literal in the same commit** (F5), and confirm
   R10 still PASSes on HEAD with `ci-local` still at **20**.
6. **Fix `usage()` (F4): both halves.** Derive the job count rather than writing
   a new literal, and state the stopping contract only as strongly as Step 3
   makes true.
7. Measure and record the resulting rule and control counts. **Do not predict
   them anywhere in this file.**

**Acceptance criteria.** A failure injected into the first command of **every**
derived job makes `ci-local` report FAIL and exit non-zero, demonstrated · the
control set is generated from the parsed job list · F1b resolved with the
mechanism named · R10 green with its literal updated · `ci-local` still **20** ·
help text derived and true in both halves · measured rule/control counts recorded
in `STATE.md` and `PROGRESS-v0.16.md` · golden 11/11.

**Done when** no `ci-local` job can report PASS on a body that failed.

---

## Step 4 · EXEMPT-DERIVE — The exemption count becomes an output 🤖

**Objective.** Replace R10's enumerated exemptions with derived classes. This is
the reduction v0.15's closing record proposed.

**Gate.** `tools/invariant_scan.py`, `config/invariant-rules.json`, and
`shell/tests/test_invariant_scan.py`. **Blocked by Step 3.**

**Context.** R10 currently reports 45 explicit exemptions against 24 local and 23
hosted normalized checks — a hand-maintained list nearly as large as the check
sets it exempts from. Two of its categories look derivable by structural
property rather than by name: runner setup steps, and receipt/attestation
persistence steps.

**Steps.**

1. For each exemption category, state a **membership criterion** in prose and
   implement it, so a new step of that kind is exempt without an edit. Where a
   criterion exists — a step declaring `uses:` rather than `run:`, a step inside
   the publish-evidence guarded block, a job carrying `continue-on-error: true` —
   use it.
2. **Where no criterion exists, keep the entry enumerated and say so in
   writing.** The operator-local protected-database check is expected to remain
   named, because its reason is environmental rather than structural. An invented
   criterion that happens to select the right 24 steps today is worse than an
   honest list.
3. The exemption **count must become an output** of the parser: measured and
   reported, never asserted by a test that pins a number. Replace the pinned
   count with an assertion that no check is exempt without matching a declared
   criterion or appearing in the residual named list.
4. Demonstrate that coverage did not narrow: every check exempt before is either
   still exempt under a stated criterion, still named, or **now checked**.
   Report any check that moved into coverage — that is a finding, and a welcome
   one.
5. Measure and record the resulting exemption count, rule count, and control
   count.

**Acceptance criteria.** Each exemption category carries a stated criterion or an
explicit written reason for remaining enumerated · the count is measured, not
pinned · no check silently lost coverage, demonstrated · R10 PASSes on HEAD ·
`--self-test` green across all rules · measured counts recorded · golden 11/11.

**Done when** adding a runner setup step or a receipt step needs no exemption
edit, and the exemption list can no longer grow by hand without a stated reason.

---

## Step 5 · SEAM (F2) — The shell stops reading core-owned config 🧑🤖

**Objective.** Remove the direct read of `config/entities.json` from shell
enrichment.

**Gate.** `shell/intel_shell/pipeline.py`, `shell/intel_shell/enrichment.py`,
the CoreClient, their shell tests, and — because the selected design requires a
core-owned route — `apps/cored/src/main.rs` and its tests. The repo-wide absence
criterion also includes `tools/invariant_scan.py`,
`config/invariant-rules.json`, and `shell/tests/test_invariant_scan.py`.
`ARCHITECTURE.md` and `README.md` are included because both enumerate the core
route contract.
**🧑 One operator decision: whether a new core-owned route ships, which sets the
version.**

**Steps.**

1. **State the options and their costs before implementing.** Either the shell
   obtains the gazetteer through a core-owned boundary, or the comparison moves
   inside the core. A third option — keeping the direct read but honouring
   `CORE_ENTITIES` and resolving the path absolutely — fixes the working-directory
   and divergence symptoms **without** fixing the ownership violation. If you
   choose it, say plainly that the seam remains crossed and record it as an open
   item rather than a closed one.
2. Implement the chosen option. The shell must not depend on the process working
   directory, and must not silently fall back to demo names when the gazetteer
   is unreachable — a missing gazetteer is an error, not a default.
3. Add a test that fails if the shell reads a core-owned config path directly.
   Prefer expressing it as an `invariant-scan` rule if the existing rule schema
   fits; if it does not, say why, and do not force it.
4. **Record the version trigger here.** No new route and no `/v1/*` change ⇒
   `v0.14.2`. A new core-owned route or any observable surface change ⇒
   `v0.15.0`. State which fired and why.
5. **Do not claim this narrows A4.** A4 is the untrusted-shell public egress
   boundary; this is config ownership. Two different seams.

**Operator decision and measured disposition (2026-07-28): Option B — compare
inside core.** Returning
the gazetteer through a core-owned boundary would stop the filesystem read but
would duplicate the core's complete entity vocabulary into the shell. Moving
only the comparison into core keeps that state private: the shell still calls
the model, sends the extracted candidate names to a narrow authenticated
internal route, and receives only the unknown subset. Keeping a corrected
direct read was rejected because it would leave the ownership violation open.
This decision adds a core-owned route, so the `v0.15.0` trigger fires. A4 is
unchanged: the new route is internal config ownership, not the untrusted-shell
public-egress boundary. The implemented authenticated `POST /entities/unknown`
accepts extracted candidate names and returns only the unknown subset. A live
alternate-`CORE_ENTITIES` control classified that file's name and alias as
known; an unavailable comparison returned pipeline status 1. R11 fails on the
removed direct shell read and now measures 11 rules / 19 controls. Golden
remained 11/11.

**Acceptance criteria.** No direct read of a core-owned config path from the
shell, or an explicit written statement that the seam remains crossed and why ·
`CORE_ENTITIES` honoured · no silent demo-name fallback · a test or rule fails
before the fix, demonstrated · version trigger recorded in this step · **golden
11/11 byte-identical**, which is what shows the fix is behaviour-preserving on
the golden path · A4 unchanged and still recorded open.

**Done when** shell enrichment cannot compare against a different gazetteer from
the one the core loaded.

---

## Step 6 · RELOCATABLE (F3) — The test entry point survives relocation 🤖

**Objective.** Stop the `cored` test binary embedding a compile-time absolute
path.

**Gate.** `apps/cored/src/main.rs` test support and any sibling helper using
`env!("CARGO_MANIFEST_DIR")`. **Test-only code; no product path changes.**

**Steps.**

1. Enumerate every `env!("CARGO_MANIFEST_DIR")` use and classify each as
   fixture-locating or otherwise. Fix the class, not the one site the audit
   named.
2. Resolve fixture paths at run time from a location that does not bake the
   build-time checkout into the binary.
3. Demonstrate the fix the way the defect appeared: build in one checkout, run
   from a relocated one sharing `CARGO_TARGET_DIR`, and show pass-after against
   the recorded fail-before.
4. Record whether this changes any product path. If it does not, say so — that
   is the claim that keeps this a verification fix.

**Entering classification (2026-07-28, before implementation).** The derived
set is three uses and all three are fixture-locating: the `cored` test module's
workspace-root helper locates root fixtures and the entity file; the two
`intel-ingest` `arxiv_oai` test helpers locate, respectively, crate-local
paging fixtures and the workspace-root single-page fixture. There are zero
non-fixture uses.

**Measured disposition (2026-07-28).** All three fixture helpers now resolve
the workspace at test run time from the current checkout; the Rust tree has
zero remaining `env!("CARGO_MANIFEST_DIR")` uses. The E0 fail-before reused
`/private/tmp/intel-v016-f3-shared` after moving its build checkout and failed
18/24 `cored` tests. The pass-after built in
`/private/tmp/intel-v016-step6.LX1zfx/build`, moved to
`/private/tmp/intel-v016-step6.LX1zfx/relocated`, and reused
`/private/tmp/intel-v016-step6.LX1zfx/shared-target`; its second cargo run
performed no compilation and passed all 126 workspace tests. The full
20-job matrix passed while reusing the uncleared Step 5 target, and golden
remained 11/11. Every code change is within a `#[cfg(test)]` module; no product
runtime path changed.

**Acceptance criteria.** Fail-before and pass-after both captured under a shared
target directory across two checkout locations · every `CARGO_MANIFEST_DIR` use
classified · no product runtime path changed · Rust tests green offline and with
`--features net` · golden 11/11.

**Done when** `./run ci-local` is reproducible without clearing the target
directory.

---

## Step 7 · RE-MEASURE 🤖🧑

**Objective.** Produce release-grade hosted evidence for the v0.16 candidate.

**Gate.** 🧑 **One narrow authorization: a non-`main` branch push.** No tag, no
`main` advance, no publication.

**Steps.**

1. Push the candidate to `candidate/<version decided at Step 5>`. Record branch
   and commit. **The branch name follows Step 5's decision — do not write it
   before that decision exists.**
2. **Read the remote branch's `ci.yml` and confirm it contains every invocation
   you expect before dispatching.**
3. Dispatch on that branch with `publish_evidence: true` and `audit_sha` set to
   the candidate.
4. **Read every count out of the hosted log**, not from job status: workspace,
   both net legs, both shell legs, the invariant rule and control counts, R10's
   derived exemption count, and golden. Compare each against the local
   measurement **at the same commit** — that equality is the criterion, not any
   number written earlier in this file.
5. Commit the signed receipt/bundle set, re-run `./run verify-artifacts` and
   `./run evidence-report`, and record the new pin count in `STATE.md`,
   `PROGRESS-v0.16.md`, and the pending closing record.
6. Confirm the hosted identity set matches the derived value.
7. Run `./run audit-deferred` in release posture with attestations required.

**Acceptance criteria.** Hosted run id pinned to the candidate · every count read
from the log and equal to the local measurement at that commit · identity set
matches the derived value · signed set committed and re-derived · new pin count
in three places · `origin/main` unchanged, no tag · golden 11/11.

**Done when** v0.16's hosted evidence exists at the same grade as v0.14.1's.

---

## Step 8 · R-CLOSE 🧑🤖

**Objective.** Close the cycle with a measured record.

**Gate.** Steps 1–7 complete and boxed. Worktree clean. **🧑 One operator
decision: publication.**

**Steps.**

1. Re-run the complete definition of done at the release commit and capture it.
2. Record the version choice, citing the trigger **fired in Step 5**.
3. Record evidence candidate and release commit as **separate named fields**.
4. **State the release disposition as of a date**, in the form `cycle-check`
   requires — read that form from the checker's own validator, not from a
   remembered example.
5. **Correct the `STATE.md` scope claim forward.** It records the net-test case
   alone; Step 1 measured the real set. **Do not retract any published record**
   unless Step 1 measured hosted evidence to be affected, and even then verify
   twice before proposing one.
6. Classify every diff path exactly once in `STATE.md`; update `CHANGELOG.md`,
   `README.md`, and the release authorities. **`README.md` must point at the new
   document locations.**
7. Reconcile `ARCHITECTURE.md`. **A4, the L1 controller residual, the R3/R4
   open-bottom limitations, the measured-value heuristic limitation, and any
   limitation Step 5 states must all read as open.**
8. Check R-CLOSE's box and replace the pending heading with the canonical
   `Cycle closed:` record **in one commit**.
9. State the publication disposition as a decision with a trigger.

**Acceptance criteria.** Version cites Step 5's trigger · evidence candidate and
release commit separate · disposition dated · `STATE.md` scope claim corrected
forward with no retraction unless measured · every diff path classified ·
`ARCHITECTURE.md` matches enforced reality · all open items recorded as open ·
all pins match · golden 11/11.

**Done when** v0.16's disposition is a recorded, measured, dated decision.

---

## Cycle checklist

- [x] **E0** — entering matrix captured with its target directory; F1 reproduced
  by derivation; F1b answered; mechanism table re-verified on the operator's
  bash; F2/F3/F5/F6 confirmed or refuted; hosted blast radius measured
- [x] **DOC-LAYOUT** — every moved file byte-identical; one resolver, no second
  location rule; tool totals and retraction count unchanged; 116 pins validate
- [x] **JOB-PROPAGATION** — every derived job fails when its first command fails;
  controls generated from the parsed list; F1b resolved; R10 literal updated;
  help true in both halves; `ci-local` still 20
- [x] **EXEMPT-DERIVE** — every exemption carries a criterion or a written reason;
  count is measured not pinned; no check lost coverage
- [x] **SEAM** — no direct core-owned config read, or the residual stated as open;
  `CORE_ENTITIES` honoured; no silent fallback; version trigger recorded here;
  golden byte-identical
- [x] **RELOCATABLE** — fail-before and pass-after across two checkouts sharing a
  target directory; every `CARGO_MANIFEST_DIR` use classified
- [ ] **RE-MEASURE** — hosted run pinned; every count equals local at the same
  commit; new pin count in three places
- [ ] **R-CLOSE** — version cites Step 5; candidate and release commit separate;
  disposition dated; `STATE.md` scope corrected forward; all open items open

---

## Standing prohibitions

- **Do not touch published releases.** `v0.14.1`, `v0.14.0`, `v0.13.0`,
  `v0.12.0`, `v0.11.0`, `v0.10.3`, and unpublished `v0.10.2` are immutable —
  tags, commits, pins, receipts.
- **Do not retract a published record on account of F1.** A local harness that
  could mask a failure is not evidence that a published count is wrong. A
  retraction is a durable claim of prior falsehood; it requires measurement that
  the published number is false, verified twice.
- **Do not fix F1 by patching the five named functions.** Five is a lower bound
  produced by example. Fix the mechanism and derive the coverage.
- **Do not adopt an `errexit` workaround the measured table marks No**, and do
  not adopt one from convention without re-running it on the operator's bash.
- **Do not edit the content of any closed runbook or progress log.** Moving is
  permitted in Step 2; bytes must be identical, proven by hash. Corrections go
  forward.
- **Do not add a second document-location rule**, a compatibility fallback, or a
  manifest of document paths.
- **Do not replace R10's exemption list with an invented criterion** that
  happens to select today's set. An honest enumeration beats a false derivation.
- **Do not add a ci-local job.** The count enters at 20 and exits at 20.
- **Do not add an `invariant-scan` rule without site-specific controls**, and do
  not let `invariant-scan` acquire a runtime dependency.
- **Do not claim any task closes or narrows A4**, the L1 residual, or the R3/R4
  open-bottom limitations. Step 5 addresses config ownership, which is a
  different seam.
- **Do not predict a count this file has not measured.** Where a quantity is
  needed, state the relation instead.
- **Do not run a live server session.** L2 remains scheduled.
- Do not change the public `/v1/*` JSON bodies, the SQLite schema, or the golden
  regression's 11 invariants except as Step 5 explicitly decides and records.
  Golden stays 11/11 after **every** task.
- Do not hand-edit `Cargo.lock` (HC12), raise the offline Rust 1.78 floor, lower
  the Python 3.11 floor, or let core call an LLM (HC3).
- Do not commit `.env`, provider keys, tokens, or private key material.
- Do not batch `STATE.md` / `PROGRESS-v0.16.md` updates or combine two tasks in
  one commit.
