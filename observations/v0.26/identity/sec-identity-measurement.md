# SEC identity measurement — 2026-07-30

## Executed path

From the repository root:

```text
RUSTFLAGS="-D warnings" cargo test -p intel-store \
  --test sec_identity_measure --locked -- --nocapture
```

Result: **1 passed; 0 failed**.

The committed store integration test invoked the committed REPLAY integration
test with an offline, disposable Cargo target and a test-only binary export
path. That test asserted the v0.25 observation bytes and ran shipped
`RssSource::fetch`; it also ran the shipped RSS parser over the committed
finance, TechWire, and OS Daily fixtures. No manually parsed XML or copied
fixture became an identity input.

The store test passed the 201 finance `Document` values to
`SqliteStore::append_new`. That public shipped path calls the private
`assign_canonical_ids_tx` at the shipped threshold of 16. The test then loaded
the fingerprints persisted by the store, executed shipped `dedup_near` at 16,
and asserted that both implementations returned the same 28
`(dropped_id, kept_id)` pairs.

## Shipped threshold result

The input is 200 SEC documents plus
`filings-digest::fin-001`. The fixture document is retained. At threshold 16:

- total kept: **173** (172 SEC plus the fixture)
- total dropped: **28**
- same-issuer drops: **8**
- cross-issuer drops: **20**

All IDs in the table expand from the displayed path to
`sec-edgar-usgaap::https://www.sec.gov/Archives/edgar/<path>`.

| Dropped path | Kept path | Distance | Class | Dropped CIK | Kept CIK |
|---|---|---:|---|---|---|
| `data/1101239/000110123926000148/0001101239-26-000148-xbrl.zip` | `data/1101239/000110123926000147/0001101239-26-000147-xbrl.zip` | 11 | same | 0001101239 | 0001101239 |
| `data/1340476/000119312526324177/0001193125-26-324177-xbrl.zip` | `data/1340476/000119312526324175/0001193125-26-324175-xbrl.zip` | 16 | same | 0001340476 | 0001340476 |
| `data/1433270/000110465926088204/0001104659-26-088204-xbrl.zip` | `data/1433270/000110465926088153/0001104659-26-088153-xbrl.zip` | 15 | same | 0001433270 | 0001433270 |
| `data/1481582/000119312526323780/0001193125-26-323780-xbrl.zip` | `data/1422143/000119312526324202/0001193125-26-324202-xbrl.zip` | 16 | cross | 0001481582 | 0001422143 |
| `data/1562528/000156252826000025/0001562528-26-000025-xbrl.zip` | `data/1562528/000156252826000024/0001562528-26-000024-xbrl.zip` | 14 | same | 0001562528 | 0001562528 |
| `data/1576018/000157601826000085/0001576018-26-000085-xbrl.zip` | `data/1045609/000119312526323746/0001193125-26-323746-xbrl.zip` | 15 | cross | 0001576018 | 0001045609 |
| `data/16875/000119312526324144/0001193125-26-324144-xbrl.zip` | `data/16875/000001687526000024/0000016875-26-000024-xbrl.zip` | 0 | same | 0000016875 | 0000016875 |
| `data/1690334/000169033426000021/0001690334-26-000021-xbrl.zip` | `data/1690334/000169033426000020/0001690334-26-000020-xbrl.zip` | 11 | same | 0001690334 | 0001690334 |
| `data/1818383/000181838326000200/0001818383-26-000200-xbrl.zip` | `data/1314727/000131472726000086/0001314727-26-000086-xbrl.zip` | 16 | cross | 0001818383 | 0001314727 |
| `data/1879403/000121390026082895/0001213900-26-082895-xbrl.zip` | `data/1340476/000119312526324175/0001193125-26-324175-xbrl.zip` | 15 | cross | 0001879403 | 0001340476 |
| `data/2060934/000110465926088209/0001104659-26-088209-xbrl.zip` | `data/1035201/000110465926088159/0001104659-26-088159-xbrl.zip` | 16 | cross | 0002060934 | 0001035201 |
| `data/2061174/000182912626008025/0001829126-26-008025-xbrl.zip` | `data/1828673/000149315226035233/0001493152-26-035233-xbrl.zip` | 16 | cross | 0002061174 | 0001828673 |
| `data/2092574/000119312526324213/0001193125-26-324213-xbrl.zip` | `data/1897245/000149315226035219/0001493152-26-035219-xbrl.zip` | 16 | cross | 0002092574 | 0001897245 |
| `data/46250/000004625026000034/0000046250-26-000034-xbrl.zip` | `data/1085392/000108539226000016/0001085392-26-000016-xbrl.zip` | 15 | cross | 0000046250 | 0001085392 |
| `data/5513/000000551326000075/0000005513-26-000075-xbrl.zip` | `data/1506707/000110465926088236/0001104659-26-088236-xbrl.zip` | 16 | cross | 0000005513 | 0001506707 |
| `data/60714/000119312526323751/0001193125-26-323751-xbrl.zip` | `data/1596967/000119312526323758/0001193125-26-323758-xbrl.zip` | 15 | cross | 0000060714 | 0001596967 |
| `data/70318/000007031826000037/0000070318-26-000037-xbrl.zip` | `data/1085392/000108539226000016/0001085392-26-000016-xbrl.zip` | 16 | cross | 0000070318 | 0001085392 |
| `data/717806/000119312526323809/0001193125-26-323809-xbrl.zip` | `data/717806/000119312526323778/0001193125-26-323778-xbrl.zip` | 0 | same | 0000717806 | 0000717806 |
| `data/730272/000119312526323773/0001193125-26-323773-xbrl.zip` | `data/1314727/000131472726000086/0001314727-26-000086-xbrl.zip` | 16 | cross | 0000730272 | 0001314727 |
| `data/832101/000083210126000022/0000832101-26-000022-xbrl.zip` | `data/1410636/000141063626000120/0001410636-26-000120-xbrl.zip` | 16 | cross | 0000832101 | 0001410636 |
| `data/860731/000086073126000050/0000860731-26-000050-xbrl.zip` | `data/1138118/000113811826000024/0001138118-26-000024-xbrl.zip` | 15 | cross | 0000860731 | 0001138118 |
| `data/876437/000087643726000028/0000876437-26-000028-xbrl.zip` | `data/1085392/000108539226000016/0001085392-26-000016-xbrl.zip` | 16 | cross | 0000876437 | 0001085392 |
| `data/885639/000119312526323775/0001193125-26-323775-xbrl.zip` | `data/23194/000119312526323767/0001193125-26-323767-xbrl.zip` | 16 | cross | 0000885639 | 0000023194 |
| `data/890394/000121390026082911/0001213900-26-082911-xbrl.zip` | `data/1433607/000149315226035220/0001493152-26-035220-xbrl.zip` | 16 | cross | 0000890394 | 0001433607 |
| `data/897448/000119312526323845/0001193125-26-323845-xbrl.zip` | `data/897448/000119312526323841/0001193125-26-323841-xbrl.zip` | 16 | same | 0000897448 | 0000897448 |
| `data/918646/000119312526323823/0001193125-26-323823-xbrl.zip` | `data/1085392/000108539226000016/0001085392-26-000016-xbrl.zip` | 16 | cross | 0000918646 | 0001085392 |
| `data/920522/000114036126030060/0001140361-26-030060-xbrl.zip` | `data/2018064/000119312526324176/0001193125-26-324176-xbrl.zip` | 15 | cross | 0000920522 | 0002018064 |
| `data/944695/000094469526000014/0000944695-26-000014-xbrl.zip` | `data/1045609/000119312526323746/0001193125-26-323746-xbrl.zip` | 16 | cross | 0000944695 | 0001045609 |

## Threshold sweep

The fixture remains kept and is included in each kept count.

| Threshold | Kept | Dropped | Same issuer | Cross issuer |
|---:|---:|---:|---:|---:|
| 16 | 173 | 28 | 8 | 20 |
| 15 | 187 | 14 | 6 | 8 |
| 14 | 196 | 5 | 5 | 0 |
| 13 | 197 | 4 | 4 | 0 |
| 12 | 197 | 4 | 4 | 0 |
| 10 | 199 | 2 | 2 | 0 |
| 8 | 199 | 2 | 2 | 0 |

This is a measurement of this 2026-07-30 corpus, not a recommendation or a
calibration claim. Fourteen is the largest swept radius with zero cross-issuer
drops here. The fixture's minimum distance from any SEC fingerprint is **23**,
so it participates in no collapse.

## Feature-count and distance mechanism

The shipped fingerprint input is `"{title} {body}"`. Shipped `tokens` and the
production three-token shingle rule produced:

- SEC shingle counts: `{4: 40, 5: 86, 6: 48, 7: 20, 8: 5, 10: 1}`;
  median **5**.
- Golden news RSS shingle counts:
  `{26: 1, 28: 1, 37: 1, 40: 2, 41: 1, 42: 1}`; median **40**.

The SEC set has 198 distinct fingerprints. Its complete 19,900-pair Hamming
distribution is:

```text
{0: 2, 11: 2, 14: 1, 15: 9, 16: 21, 17: 30, 18: 49, 19: 94,
 20: 186, 21: 247, 22: 386, 23: 552, 24: 725, 25: 928, 26: 1132,
 27: 1310, 28: 1489, 29: 1628, 30: 1620, 31: 1643, 32: 1571,
 33: 1435, 34: 1254, 35: 1106, 36: 833, 37: 637, 38: 392,
 39: 260, 40: 163, 41: 85, 42: 55, 43: 24, 44: 18, 45: 8,
 46: 3, 47: 2}
```

Exactly **35** SEC pairs are at or inside radius 16. First-match canonical
selection turns those pair relations into 28 actual drops.

The seven golden news RSS documents have 21 pairs:

```text
{12: 1, 25: 1, 26: 2, 28: 1, 29: 1, 30: 2, 32: 2, 35: 1,
 36: 4, 37: 2, 38: 2, 41: 1, 44: 1}
```

One news pair is at or inside radius 16: the intended golden near-duplicate at
distance 12. On this corpus, the feature-count claim is confirmed as the
mechanism behind the failure: SEC fingerprints are built from 4–10 features
while news fingerprints use 26–42, and the shipped news radius admits the
true-positive pair while the sparse SEC set produces 20 cross-issuer drops.
This is corpus evidence, not a general causal calibration.

## Same-day concentration

Before deduplication the finance sector has one fixture document on
`2026-07-03` and all 200 SEC documents on `2026-07-29`. After shipped
threshold-16 deduplication it has 1 and 172 respectively.

The committed gazetteer resolved **0 mentions / 0 entities** in the kept
finance documents. Executed shipped `analyze` therefore had a 26-day corpus
window but constructed no per-entity burst baseline, calculated no z-score,
emitted 0 rising signals, 0 total signals, and 0 graph edges. Its `window_end`
was `2026-07-29`. This concentration is recorded and not acted on; it is not
the subject of v0.26.

## Prediction disposition

The draft correctly predicted the 200 SEC items, 198 distinct fingerprints,
one SEC day, mean body length 3.81, SEC median of 5 shingles, 35 SEC pairs
inside radius 16, 172 SEC kept / 28 dropped with 20 cross-issuer drops, fixture
minimum distance 23, and threshold 14 as the largest swept value with zero
cross-issuer collapse.

The draft's “28–36” news-feature comparison was wrong. The executed news range
is **26–42** and its median is **40**. This is an author-side prediction error,
not an implementation defect; the shipped measurement above is the result.

No production source, configuration, fixture, golden input, protected
artifact, database, or publisher was changed or contacted.
