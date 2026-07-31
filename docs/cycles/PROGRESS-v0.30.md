# PROGRESS-v0.30.md — append-only execution record

This file records v0.30 task and gate events after their implementation
commits exist. Each entry names the measured result, every applicable
acceptance criterion, the golden delta, and the real implementation commit.
Entries are append-only; corrections are new dated entries.

### 2026-07-31 · ACTIVATE — v0.30 preparatory cycle activation

- owner: Codex
- commit: bea40e64849015fdfc9b471f2adb7ab3ce4fcbf7
- result: PASS for the runbook-defined preparatory activation. The sole
  pre-activation worktree item was the operator-supplied untracked
  `docs/cycles/TASKS-v0.30-EXECUTION.md`; tracked and staged diffs were empty.
  The implementation commit contains only that runbook, the `AGENTS.md`
  declaration moving the active cycle to v0.30, this progress skeleton, and
  the required `repomix.config.json` retention edit.
- entering-ref acceptance: PASS. Before activation, HEAD was v0.29 audit
  commit `d824be06582dfb76b9fe4b5d70ff33f4a505d6cc`, whose immediate parent was
  v0.29 closure commit `20ddf90bb2b1d8654b410cdafe8f67e6d006a115`.
  The local remote-tracking `origin/main` and peeled v0.17.0 tag both resolved
  to `4af2841816dd3e43fb8423153b91aa22ccb87537`; HEAD was 44 commits ahead
  and zero behind that remote-tracking ref. Local `main` remained at
  `eb2d9df8b3ffd3e0380d506e958fb5a3adb2d42e`. No ref moved, and no mutable
  `origin/main` hash was added to `STATE.md`'s header.
- retention rejection acceptance: PASS. With active v0.30 present and before
  the retention edit, the real checker emitted exactly:
  `cycle-check: ERROR: repomix.config.json: review-export retention pattern for v0.30 must be 'docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-7]}{.md,.*.md,-*.md}'; found ['docs/cycles/{TASKS,PROGRESS}-v0.{[0-9],1[0-9],2[0-6]}{.md,.*.md,-*.md}']`.
  The implementation then changed only that final retained range.
- lifecycle acceptance: EXPECTED PENDING at the preparatory checkpoint. After
  the activation commit, `cycle-check` rejected exactly the three
  trigger-bearing `ARCHITECTURE.md` rows because they still named v0.29.
  The activation section explicitly assigns their measured v0.30 rewrite to
  E0; no other lifecycle defect was reported. Before this entry existed,
  `progress-check` correctly rejected the empty progress skeleton.
- test acceptance: NOT RUN at this preparatory checkpoint; E0 owns the clean
  rebuild, the complete 20-job matrix, both constrained Python populations,
  both protected-artifact timing runs, and the activation-tree export.
- golden-E2E delta: NOT MEASURED; E0 owns the first post-activation golden
  measurement.
- publisher/ref acceptance: PASS. Activation used only repository and local
  Git inspection. It issued no publisher request, ran no scheduler, and
  created, moved, or deleted no ref.

### 2026-07-31 · E0 — entering state rebuilt and G1–G6 settled

- owner: Codex
- commit: 2b0b890c988de9facd901ccef444a1ed0dad5c58
- result: PASS. The supplied runbook was the sole pre-activation worktree
  item; v0.29 audit `d824be06…` and closure `20ddf90b…` were exactly where the
  entering state placed them. The stale retention pattern produced the exact
  required v0.30 rejection before activation changed `2[0-6]` to `2[0-7]`.
  The activation pair is `bea40e64…` plus audit `e7b2c588…`.
- decision-gate acceptance: PASS after the runbook-required activation
  rewrite. The first clean Python 3.11 execution collected 306, passed 305,
  failed the one current-trigger-table test, and skipped zero because the
  three architecture governed rows still named v0.29. This is a measured
  non-pass. E0 rewrote those rows with v0.30 measurements as the activation
  section requires; the result-of-record rerun and every complete local gate
  then passed. No remaining E0 gate tripped.
- complete-suite acceptance: PASS. `./run ci-local` passed all **20/20** jobs:
  warning-denied **146** workspace tests and **62** net tests (**32 ingest +
  30 cored**), locked Rust 1.78 check/test, clean rustc/clippy/fmt/ShellCheck,
  shell pytest, embedded golden **11/11**, protected artifacts, persisted
  fingerprints, lifecycle checks, and registered `invariant-scan` **12 rules /
  51 controls**. Focused cycle tests passed **53/53**.
- constrained-Python acceptance: PASS. Clean Python **3.11.4** and
  **3.12.13** environments each resolved all **21** constraints, collected
  **306**, passed **306**, failed **0**, and skipped **0**. Each emitted the
  same one accepted `StarletteDeprecationWarning`.
  `tools/test_population.py` derived `collected=306`, `equivalent=true`, and
  `equivalent_passed=306`, with both populations passed 306 / skipped 0.
- protected-artifact acceptance: PASS. Manifest validation reported schema 2,
  **2 artifacts / 331 pinned files**. Two complete verifications matched every
  pin and both databases at **0.09 s / 0.10 s real**. The unchanged manifest
  is **191,395 bytes**, leaving **857,181 bytes** to 1 MiB.
- G1 acceptance: PASS by execution. Exactly four forward-boundary constants
  and all six pair relations were classified. Scope is independent of all
  three trigger boundaries; freshness must not follow identity or floor;
  identity and floor are mutually independent. A real throwaway checker
  passed before and after identity moved from `(0, 28)` to `(0, 22)`, while a
  stale governed cell still produced the exact v0.30 identity error. The
  lowered declaration is silently always-on whenever freshness is reachable
  and is itself unobservable. BOUNDARY-COVER is unblocked without a live P1
  reclassification.
- G2 acceptance: PASS by execution and exhaustive search. The two `run` pins
  carry `1.78.0`; the hosted pin carries `1.78`; normalization derived one
  value, `1.78`, with multiplicity three. Live `STATE.md:3763` instead stated
  offline `1.75`. The local net entry point is ambient and hosted net pins
  1.91; exact searches found **0** `rustup 1.86`, `cargo +1.86`, or workflow
  `toolchain: 1.86` constructions.
- G2 inventory acceptance: PASS. Exact tracked-text enumeration found **582**
  floor-stating lines: **300** in cycle documents, **205** in State archives,
  **24** in live State, and **53** elsewhere. Current executable pins and
  restatements are enumerated in `STATE.md`; historical records are classified
  separately. Identical syntax occurs in present and historical prose, so no
  general scan can distinguish them without metadata. FLOOR-BIND must carry a
  named, hand-maintained current-restatement registry and a permanent
  historical-exclusion obligation.
- G3 acceptance: PASS by execution in both full Git trees. At synthetic
  `v1.0`, automated `cycle-check` rejected the unrepresentable retention
  derivation and operator-local `export-check` passed at **2,524,391 bytes /
  152 files**. At synthetic `v1.3`, `cycle-check` passed while `export-check`
  rejected **4,605,031 bytes / 203 files**, **51** outside-depth cycle
  documents, and the ceiling. Automated lanes catch the loud `v1.0` case;
  none catches the silent `v1.3` case because export-check is operator-local.
- G4 acceptance: PASS by exhaustive search. Only `cycle_check.py`, its test,
  and the invariant self-test touch the governed table; none compares measured
  numeric content. The v0.29 audit child grew its progress record by exactly
  **4,965 repository bytes**, matching the delivered-export delta from
  **2,516,822** to **2,521,787**. That one appended audit-entry size is the
  named fixed-point residual; MARGIN-BIND owns the executable rule and empty
  record state.
- G5 acceptance: PASS. Comparable export points are v0.28 delivered
  **2,530,129**, v0.29 delivered **2,521,787** (−8,342), and v0.30 activation
  audit tree `e7b2c588…` **2,464,445** (−57,342). Three points yield only two
  interval observations, both negative, and support no growth rate. The exact
  activation export retained v0.28–v0.30 across **152** files and left
  **535,555 bytes / 17.85%**. Under the existing explicit planning
  denominators, State is nearer its trigger at **8.72 cycles** versus the
  export's **17.19**.
- G6 acceptance: PASS. The production and test SQL ordering clause bodies
  were byte-identical at **123 bytes**, SHA-256
  `47c5f7d45b5b92974f3f33de54be41cfeb06305db8221c7877f1c0a944f453aa`.
  A `macro_rules!` constructor can expand the one clause with distinct
  compile-time select/tail literals and no runtime formatting or allocation.
  ORDER-CONST is therefore unblocked rather than skipped.
- governed-record acceptance: PASS. All **20** deferred rows now carry
  v0.30-measured observations; the three architecture rows carry the exact
  activation export, manifest/timings, and clean two-lane warning result.
  `cycle-check` passed with active v0.30 open.
- control acceptance: PASS. `checklist-audit` remained **232 checked / 3
  retracted / 232 matched / 232 commits resolved / 0 exemptions** before the
  mandatory E0 checkbox. E0 edited neither `cycle_check.py` nor `sqlite.rs` and
  re-derived **0** planted-control line values. Focused SEC identity kept all
  **200 SEC** rows and dropped **0**.
- golden-E2E delta: **0** — embedded and final standalone executions each
  passed **11/11** byte-identically.
- publisher/ref acceptance: PASS. E0 issued no publisher request, ran no
  scheduler or model-profile command, and changed no cadence, dependency,
  schema, production source, manifest, protected byte, version authority, tag,
  or working-repository ref.
