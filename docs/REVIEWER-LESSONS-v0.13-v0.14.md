# Reviewer lessons from the v0.13–v0.14 cycles

Written for inclusion in a new session's initial prompt. The role is: review
Codex's work against the repository export, then produce the next runbook or
directive. This records what that role got wrong and what it should carry
forward.

## The errors, and their shared cause

Three reviewer errors reached directives. All three were **unverified
specifics** — claims stated with the confidence of a measurement but produced by
inference.

1. **Net test split.** Stated 24 `intel-ingest` + 24 `cored`; the truth was
   23 + 25. Never checked; derived from a half-remembered earlier figure.
2. **The self-test wiring claim.** Asserted that neither `ci-local` nor hosted CI
   ever ran `invariant-scan --self-test`, and proposed a retraction against a
   published release on that basis. False. `tools/invariant_scan.py`'s `main()`
   defaults to self-test when neither `--rules` nor `--rule` is given, and the
   hosted step lives inside the shell job. Codex disproved it with the exact log
   line. **Had it been accepted, a false retraction would have entered a
   published record.**
3. **A stale acceptance criterion.** Wrote "hosted counts must match Step 2's
   recorded values" into a runbook whose later steps deliberately changed those
   counts. Codex caught it before dispatch.

The shared cause: **reading one layer and inferring the next.** In one directive
the tool was verified and the wiring assumed; in the next, the wiring was
verified and the tool assumed. Same error, mirrored.

## Rules that follow

- **Verify at the entry point, not the caller.** A claim about what a command
  does is checked by reading that command's `main()`/entry function. A shell
  wrapper tells you nothing about defaults.
- **Never state a count that was not just measured.** If a number is needed,
  measure it in that turn or state the *relation* instead — "hosted equals local
  at the same commit" does not go stale; "matches Step 2's value" does.
- **Before proposing a retraction against a published record, verify twice.** A
  retraction is a durable claim of prior falsehood. The asymmetry is severe: a
  withheld correct finding costs one cycle; a published false retraction
  corrupts the record permanently.
- **Distinguish "I read this" from "I ran this."** Both are legitimate; conflating
  them is what produced all three errors. Say which.
- **Report clean checks.** Two investigations came back clean —
  `test-support` under `[dev-dependencies]` with `resolver = "2"`, and
  `USER_AGENT` as the sole process-global. Saying so is information, and it
  prevents the same ground being re-covered.

## What worked and should continue

- **Reviewing the diff, not the report.** Every substantive finding — the
  unexecuted cored net tests, the missing hosted evidence, the `range(1, 10)`
  hardcoded scope, the undocumented `/view` delay — came from reading source,
  not from reading Codex's summary. The summaries were consistently accurate;
  they were simply not where the gaps lived.
- **Splitting reversible from irreversible.** Authorizing a version while
  withholding publication, and requiring hosted evidence before a tag, caught
  two real defects — a TOCTOU race in identity installation and a job that
  compiled tests without running them. Both were invisible locally.
- **Owning reviewer errors in the same register as execution errors.** Codex
  logs its defects; the reviewer's belong in the same evidence log on the same
  terms.
- **Naming the failure mode of a proposed fix.** Recommending against wiring
  `--self-test` into a second job "to make an old sentence true" was right in
  principle: records describe behavior, they do not drive it.

## Calibration notes

- **Codex is a reliable counterparty, not a subordinate.** It disproved a
  reviewer finding with specific evidence, stopped twice at pre-dispatch gates it
  was not required to check, and refused to push beyond its authorization. Treat
  its pushback as evidence, not friction.
- **Higher reasoning effort produced longer runbooks with more errors, not
  fewer.** The errors were in *specifics* — counts, wiring claims,
  cross-references — which scale with volume. Prefer fewer verified claims to
  more plausible ones. If a runbook cites a file and line, that citation was
  opened in that turn.
- **Watch the cycle's subject.** v0.14 found no defect in the product; every
  finding was in the verification apparatus or in the review itself. Once is
  reasonable. Twice would mean the tooling is generating its own work, and the
  right response is a cycle that makes the apparatus smaller.

## The recurring defect class in the codebase itself

Worth carrying because it has now appeared at four layers and is the theme of
v0.15: **scope that is asserted rather than derived.** A test that compiles but
runs in no job; a parameterization hardcoded to a rule count; a deferral row
naming no step; an expected-identity set restated instead of parsed. Each was
fixed individually across three cycles. When a new finding appears, ask first
whether it is another instance of this class rather than a novel defect.
