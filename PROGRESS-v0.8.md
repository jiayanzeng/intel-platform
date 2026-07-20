# PROGRESS-v0.8.md — execution log

Append-only. One block per task, written **immediately** on completion
(`AGENTS.md §5`). This is the audit trail: it records what was *measured*, so a
claim in `STATE.md` can always be traced to a run. Do not edit past entries;
correct them with a new dated entry.

**Block format:**

```
### <date> · <task id> — <one-line result>
- owner: 🤖 Codex | 🧑 human-assisted
- measured: <the numbers / outputs you captured>
- acceptance: <criterion> ✅/❌ … (all of them)
- golden E2E: unchanged | <the delta, if the task changed it>
- commit: <hash>
- notes / gate: <anything deferred, skipped, or found false>
```

---

### 2026-07-20 · T2 (partial) — live arXiv harvest reached the wire

- owner: 🧑 on-site run (pre-Codex), recorded here for continuity
- measured: `./run harvest-arxiv` against `oaipmh.arxiv.org/oai`; page 1 = 1,300
  docs, page 2 = 1,764 (last page); `{"fetched":1764,"new":1764, ok:true,
  error:null}`; `documents_analyzed: 1708` (56 near-dups suppressed, all 1,764
  stored). Build `cored --features net` clean in 8.79 s on Rust 1.91.1.
- acceptance: real OAI-PMH XML parsed, 0 errors ✅ · `resumptionToken` paging
  across > 1 page on the wire ✅ · interruption-resume ❌ (not yet tested — see
  Step 2 / T2 in the runbook) · 503 / Retry-After ❌ (not observed; arXiv issued
  none)
- golden E2E: not run this session
- commit: (pack `repomix` v1.16.1, 82 files) — no code commit; ops run
- notes / gate: **T2 is not complete.** "Reached the wire" is progress; resume
  behavior is the remaining gate. Two follow-ups to carry into the next runs:
  (1) this run wrote 1,764 live docs into `data/core.db` — isolate live runs with
  `CORE_DB=data/live-smoke.db` before the next harvest so the 12-doc golden corpus
  stays clean; (2) the clippy dump from this session shows `items_after_test_module`
  still firing in `sqlite.rs`, contradicting `STATE.md`'s "fixed" claim (handled
  in Step 4 / T6).

---

<!-- Codex appends below, one block per completed step, newest at the bottom. -->

### 2026-07-20 · B0 — entering state verified and corrected

- owner: 🤖 Codex
- measured: clean Rust 1.91.1 baseline: workspace check 0 rustc warnings;
  workspace tests 80 passed; net cored check 0 rustc warnings; net ingest tests
  17 passed; shell tests 69 passed with 1 Starlette deprecation warning. Clippy
  exits 101 on one `items_after_test_module` diagnostic in `sqlite.rs`; with
  only that lint allowed, the remainder is clean. Fmt check exits 1 with diffs
  in 13 Rust files.
- acceptance: Rust/shell counts captured ✅ · 0 rustc warnings on offline and
  net configs ✅ · golden result captured and unchanged ✅ · clippy inventory
  captured, including the two accepted `unnecessary_map_or` allows ✅ · golden
  vs live DB paths answered and isolated ✅
- golden E2E: unchanged — fixture ingest 13; acme 13 → 12; dropped
  `techwire::tw-004` for `osdaily::osd-004` at hamming 12; DeepSeek RISING
  z=10.0; re-ingest +0; quant 1; `/v1/ask` 4 citations with
  `techwire::tw-004` suppressed.
- commit: this B0 baseline-verification commit (see git history)
- notes / gate: corrected `STATE.md`'s false claim that the test module had
  already been moved last; recorded the newly measured fmt failure and that CI
  is report-only rather than commented out (the ordered T6 step owns the stale
  wording in `TASKS-v0.8.md`). Golden ran on a temporary fixture DB;
  `data/core.db` remained 1,764 documents and byte-size/mtime unchanged. Port
  8788 is held by foreign PID 59269; operator command `kill 59269` is required
  before T2.

### 2026-07-20 · T2 — BLOCKED: capped live run clears its resume token

- owner: 🤖 Codex
- measured: after a clear-port/fresh-DB preflight,
  `HARVEST_MAX_PAGES=1 CORE_DB=data/live-smoke.db ./run harvest-arxiv` fetched
  and parsed 1,300 real page-1 records (`ok=true`, `error=null`), logged that
  more pages follow, and stopped at cap 1. The persisted row was
  `arxiv-cs | cursor=NULL | high_water='2026-07-20'`. Code inspection confirmed
  the capped break is followed by unconditional `complete()`, which clears the
  checkpoint and advances high-water. The existing fake test observes the
  intermediate checkpoint call but never checks final resume state.
- acceptance: run 1 non-NULL cursor ❌ (`NULL`) · run 2 resumes from token ❌
  (not run; no token exists, so a second run would test the prohibited
  high-water path) · real XML parse errors on run 1: 0 ✅, but the required
  two-run criterion remains incomplete · `data/core.db` untouched ✅ · 503 /
  Retry-After explicitly not observed ✅
- golden E2E: unchanged — acme 13 → 12; dropped `techwire::tw-004` for
  `osdaily::osd-004` at hamming 12; DeepSeek RISING z=10.0; re-ingest +0;
  quant 1; `/v1/ask` 4 citations with `techwire::tw-004` suppressed.
- commit: this T2 gate-result commit (see git history)
- notes / gate: **T2 is not complete.** The decision gate tripped at the first
  cursor assertion. No workaround and no misleading second run were attempted.
  Repair requires distinguishing capped exit from exhausted completion and a
  test that asserts final persisted resume state; that repair is outside this
  verification step and was not implemented here.

### 2026-07-20 · H1 — live harvest evidence now reflects actual outcomes

- owner: 🤖 Codex
- measured: positive live run against a fresh `data/live-smoke.db` fetched
  1,764 documents over two pages (1,300 then 1,764) with 0 parse errors. The
  robots section showed only real decisions:
  `https://oaipmh.arxiv.org -> Unavailable(allow)`, allowed=true, effective
  crawl-delay 0.500s. All four derived checklist boxes were checked. A
  controlled real zero-document run (`fetched=0, new=0, ok=true`) reported NOT
  VERIFIED and left all four boxes unchecked.
- acceptance: capped/live robots section shows a real disposition, not page
  output ✅ · positive checklist matches documents/pages/parse/cursor evidence
  ✅ · zero-document checklist is fully unchecked ✅ · workspace 80, net 17,
  shell 69 tests green and both rustc-warning checks clean ✅
- golden E2E: unchanged — acme 13 → 12; dropped `techwire::tw-004` for
  `osdaily::osd-004` at hamming 12; DeepSeek RISING z=10.0; re-ingest +0;
  quant 1; `/v1/ask` 4 citations with `techwire::tw-004` suppressed.
- commit: this H1 harness-evidence commit (see git history)
- notes / gate: logging/checklist only; no fetch, robots, cursor, or corpus
  outcome changed. `data/core.db` hash/size/mtime/count remained exact. T2's
  capped-run cursor bug remains blocked and was not worked around.
