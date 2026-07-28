# v0.18 LIVE-HARVEST — `arxiv-cs`

Observed on **2026-07-28**, beginning at **14:11:01Z**. The operator action was
one bare `./run harvest-arxiv`, timed without any `CORE_DB`, date-window, page,
port, or concurrency override.

## Isolation and process scope

- preflight: artifact schema v2 valid; all **146/146** pins matched; protected
  databases **2/2** exact
- before launch: port 8788 had no listener and no `cored` process existed
- harvester/core count: **1**; the harness started one core as PID **13809**
- fresh database: `data/live-20260728T141101Z-13711.db`
- database SHA-256:
  `11d2b6a6bdf15b27964eae2be971deb0b056d47546ea96dd47a6eb1e56e58d6a`
- database size/integrity: **10,166,272 bytes**, `pragma_integrity_check=ok`
- after launch: `./run down` left port 8788 with no listener
- after harvest: all **146/146** pins and both protected databases remained
  exact:
  `data/core.db=db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0`;
  `data/live-smoke.db=94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a`

The fresh database remains an ignored observation. No harvested document was
copied into the golden corpus, protected artifacts, evidence, or receipts.

## Policy and politeness

The generated live configuration covered **2026-07-25 through 2026-07-28** and
capped the smoke run at **3** pages. The reachability `Identify` probe returned
HTTP **200**.

The publisher's `/robots.txt` again returned `Unavailable(allow)`, matching the
Step 3 HTTP 404 observation. No publisher `Crawl-delay` existed. Every page
request reported `effective-crawl-delay=0.500s`, so the operator's 2-rps floor
governed and was not accelerated.

## Wire observations

- page 1: fresh request; cumulative documents **1,300**; a
  `resumptionToken` was returned
- page 2: the first token was followed; cumulative documents **2,600**; a
  second token was returned
- page 3: the second token was followed; cumulative documents **2,692**; last
  page, so the safety cap did not truncate another page
- page-request lines: **3**
- robots-gate lines: **3**, one per page request
- document redirects: **none observed**; a redirect re-enters the gated request
  loop, while the log contains no extra gate line or redirect/error line
- `503 Retry-After` events/retries: **none observed**; there is no 503,
  retry-after, or extra gated-attempt line
- document HTTP failures or other non-success statuses: **none observed**; all
  three bodies reached the parser and committed
- XML surprises: **none observed**; result `ok=true`, no parse/unexpected-shape
  log, and all three real OAI-PMH pages ingested
- result: `fetched=2692`, `new=2692`, source documents **2,692**
- retained canonical documents: **2,550**; **142** near-duplicate rows map to
  another canonical id
- persisted cursor row:
  `arxiv-cs | cursor=NULL | high_water=2026-07-28 | pending_high_water=NULL`
- total command wall time, including artifact preflight and net build:
  **46.38 seconds**

## Finding for WIRE-FINDINGS

**F1 — post-run inspection claim is false.** The harness printed “cored still
running on http://127.0.0.1:8788 for inspection,” but immediately after the
command returned PID 13809 no longer existed and `/health` failed to connect.
Step 5 must give F1 exactly one disposition; this report does not pre-decide
whether to preserve the process or correct the message.

No publisher XML, paging, cursor, redirect, retry, status, or politeness defect
was observed.
