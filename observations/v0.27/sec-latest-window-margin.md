# v0.27 WINDOW-MEASURE — SEC latest-window margin

Measured on **2026-07-30** from the pinned response body at
`observations/v0.25/feed-shape/sec-edgar-usgaap.rss.xml`. The point-of-use test
first enforces the committed 892,641-byte length and SHA-256
`154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3`;
it then derives this record from the XML rather than treating this table as its
input.

## Executed derivation

Command:

```text
cargo test -p intel-ingest --test sec_observation_replay \
  derives_sec_latest_window_timing_from_pinned_body --locked -- --nocapture
```

The test passed 1/1 and derived:

| Quantity | Result |
|---|---:|
| latest-window population | 200 items |
| oldest item | `Wed, 29 Jul 2026 16:13:52 EDT` |
| newest item | `Wed, 29 Jul 2026 17:31:22 EDT` |
| observed window span | 4,650 seconds / 77.5 minutes |
| consecutive gaps | 199 |
| median consecutive gap | 11 seconds |
| maximum consecutive gap | 215 seconds |
| EDT hour population | 16: 133; 17: 67 |

The test also derives the complete consecutive-gap histogram and checks that
its 199 gaps sum to the 4,650-second endpoint span. It reads both channel
`lastBuildDate` and `pubDate` as `Wed, 29 Jul 2026 21:50:03 EDT`.

## Coverage criterion and observed margin

For consecutive successful polls over a stable fixed latest-N identity set,
the polls cover the publisher's items **if and only if** the **poll interval**
is shorter than the **time required for the latest-N window to advance by N
items**. The two terms are not the same as a feed's rebuild interval: rebuild
cadence says when a representation may be refreshed; window-advance time says
when an unseen item can fall out.

Using this single observed 200-item span as the measured window-advance term,
the committed 600-second poll interval is:

- `4,650 / 600 = 7.75`: the observed window span is **7.75 times** the poll
  interval; equivalently,
- `600 / 4,650 = 0.1290`: the poll consumes **12.90%** of the observed span,
  leaving 4,050 seconds between one poll interval and the measured turnover.

This is a measured margin for this sample, not a universal publisher bound.

## Evidentiary limits

The margin rests on **one 77.5-minute post-close window on one Wednesday**. It
does not establish:

1. peak-season filing density;
2. deadline-day filing density; or
3. density during any hours neither live sample covered.

It also assumes polls complete successfully and the feed continues to expose a
stable latest-N identity set. Detection and failure behavior are separate
questions owned by the later coverage task.

## Idle-sample property and correction

The v0.25 body capture completed at `2026-07-30T03:34:00Z` and the v0.26
corrective content request began at `2026-07-30T09:18:39.680936Z`, or 23:34 and
05:18 Eastern. Both were outside filing hours. Their 892,641-byte bodies and
SHA-256 were identical, and both expose the unchanged channel
`lastBuildDate`.

The elapsed interval is **5h44m39.680936s (20,679.680936 seconds)**, not the
draft runbook's 7h28m. The committed timestamps refute that drafted duration;
the measurement is authoritative.

The unchanged observable body and `lastBuildDate` across far more than ten
minutes refute “updated every 10 minutes” as a description of observable
publisher behavior during this idle interval. At the same time, the observation
does **not** test window velocity: with no arriving filings, byte identity says
nothing about how quickly a busy latest-200 window advances.

## Boundary

This is replay of committed bytes, not a live-path claim. No publisher request
or schedule execution occurred, and `config/schedule.json` remains unchanged.
