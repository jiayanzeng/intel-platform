# V1 `/view` SLO predeclaration — 2026-07-24

Recorded before the first V1 timing sample, with operator approval.

- Anchor: **16.264 ms**, A3's post-change `POST /retrieve` measurement on a
  disposable copy of the 2,600-row archive (`learning`, sector `science`,
  `k=8`).
- Cold p95 firing value: **162.640 ms** (**10×** anchor). The factor covers a
  new `cored` process, SQLite open, sector-scoped corpus load, and `/view`
  analysis absent from the retrieval anchor.
- Warm p95 firing value: **32.528 ms** (**2×** anchor). A valid generation-cache
  hit should remain close to the already-measured local HTTP/store cost.
- Physical plausibility: **yes on this host**. Both values are above the
  measured local request anchor yet low enough for the delayed control to
  breach. A threshold that the delayed control cannot fire is a benchmark
  defect, not a pass.
- Gate: materialization remains deferred only if both the 1,764- and 2,600-row
  archives meet both thresholds in two independent runs. Two misses for the
  same archive/path fire the design trigger. A single-run miss is reported as
  an outlier and requires another recorded run.
- p95 method: nearest rank, `sorted_samples[ceil(0.95 × n) - 1]`.
