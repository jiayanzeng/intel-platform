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
