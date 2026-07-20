//! intel-core: the shared vocabulary of the platform.
//!
//! Everything downstream of ingestion speaks these types. The design intent:
//! raw documents are the *bottom* of the value pyramid; the product is the
//! derived layer built on top of them:
//!
//! ```text
//! briefs / Q&A  (rendered for subscribers — now in the SHELL)
//!    signals    (rising entities, corroboration, emerging entities)
//!  entity graph (who co-occurs with whom, how strongly)
//!    mentions   (resolved entities in documents)
//!    archive    (normalized, deduplicated, license-tagged documents)
//! ```
//!
//! A news aggregator stops at the archive. This platform's moat is the rest.

use serde::{Deserialize, Serialize};
use std::fmt;

// ---------------------------------------------------------------------------
// Sectors
// ---------------------------------------------------------------------------

/// A sector is config-defined, never hard-coded: adding "education" later is
/// a JSON edit plus (optionally) new connectors, not a core change.
#[derive(Clone, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, Serialize, Deserialize)]
pub struct SectorId(pub String);

impl SectorId {
    pub fn new(s: &str) -> Self {
        Self(s.to_string())
    }
}

// ---------------------------------------------------------------------------
// Provenance & licensing
// ---------------------------------------------------------------------------

/// How a document was acquired. Every channel here is legal and involves no
/// paid commercial data gatekeeper.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Serialize, Deserialize)]
pub enum SourceKind {
    /// Publisher-offered syndication feed.
    Rss,
    /// OAI-PMH harvesting endpoint (arXiv, institutional repositories).
    OaiPmh,
    /// Official bulk dataset / open-data download.
    BulkDataset,
    /// robots.txt- and ToS-compliant crawl of public pages.
    CompliantCrawl,
    /// Data a client uploaded about themselves.
    ClientUpload,
}

/// The licensing dimension governs a *paid* product: analysis is almost
/// always fine; redistributing someone else's full text verbatim is a
/// separate, license-gated act. Enforced in the CORE (store + view
/// hydration) so no shell iteration can forget it.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Serialize, Deserialize)]
pub enum License {
    PublicDomain,
    CcBy,
    ClientOwned,
    /// May index and analyze; must not resell the raw text.
    IndexOnly,
}

impl License {
    pub fn redistributable(self) -> bool {
        matches!(
            self,
            License::PublicDomain | License::CcBy | License::ClientOwned
        )
    }

    pub fn as_str(self) -> &'static str {
        match self {
            License::PublicDomain => "PublicDomain",
            License::CcBy => "CcBy",
            License::ClientOwned => "ClientOwned",
            License::IndexOnly => "IndexOnly",
        }
    }

    pub fn parse(s: &str) -> Option<Self> {
        Some(match s {
            "PublicDomain" => License::PublicDomain,
            "CcBy" => License::CcBy,
            "ClientOwned" => License::ClientOwned,
            "IndexOnly" => License::IndexOnly,
            _ => return None,
        })
    }
}

impl SourceKind {
    pub fn as_str(self) -> &'static str {
        match self {
            SourceKind::Rss => "Rss",
            SourceKind::OaiPmh => "OaiPmh",
            SourceKind::BulkDataset => "BulkDataset",
            SourceKind::CompliantCrawl => "CompliantCrawl",
            SourceKind::ClientUpload => "ClientUpload",
        }
    }

    pub fn parse(s: &str) -> Option<Self> {
        Some(match s {
            "Rss" => SourceKind::Rss,
            "OaiPmh" => SourceKind::OaiPmh,
            "BulkDataset" => SourceKind::BulkDataset,
            "CompliantCrawl" => SourceKind::CompliantCrawl,
            "ClientUpload" => SourceKind::ClientUpload,
            _ => return None,
        })
    }
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Provenance {
    pub source_id: String,
    pub retrieved_from: String,
    pub kind: SourceKind,
    pub license: License,
}

// ---------------------------------------------------------------------------
// Time (seed-grade)
// ---------------------------------------------------------------------------

/// An ordinal day for windowed analytics: **days since 1970-01-01**, proleptic
/// Gregorian.
///
/// This used to be `y*372 + (m-1)*31 + (d-1)`, which is monotonic and exact
/// *within* a month but leaves phantom ordinals at every month boundary (there
/// is no Feb 30th, yet the encoding reserves a slot for one). That was not
/// merely untidy: `analyze` builds a burst baseline by walking every ordinal in
/// `[window_start, window_end)` and zero-filling the gaps, so a window spanning
/// a month boundary swept in days that *cannot* hold documents. Those spurious
/// zeros drag the baseline mean down and push z-scores up — i.e. the phantom
/// days manufactured RISING signals. Since "is this entity actually surging?"
/// is the product's central claim, the encoding had to become honest.
///
/// The conversion is Howard Hinnant's `days_from_civil` / `civil_from_days`:
/// exact for all years, no lookup tables, no dependency. Leap years are handled
/// by shifting the year to start in March, which makes the leap day the *last*
/// day of the year and so a pure function of the year's length.
///
/// NOTE: absolute `Day` values changed with this fix, so `published_day`
/// integers written by an older build are on the old scale. Differences within
/// a single month are identical under both encodings (which is why the golden
/// E2E numbers are unmoved), but an archive carrying pre-v0.6 rows should be
/// rebuilt if it spans month boundaries. Fresh ingests are unaffected.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, Serialize, Deserialize)]
pub struct Day(pub i64);

/// Days in month `m` of year `y` (Gregorian leap rule).
fn days_in_month(y: i64, m: i64) -> i64 {
    match m {
        1 | 3 | 5 | 7 | 8 | 10 | 12 => 31,
        4 | 6 | 9 | 11 => 30,
        2 => {
            if (y % 4 == 0 && y % 100 != 0) || y % 400 == 0 {
                29
            } else {
                28
            }
        }
        _ => 0,
    }
}

impl Day {
    /// Days since the 1970-01-01 epoch. Assumes a valid (y, m, d).
    pub fn from_ymd(y: i64, m: i64, d: i64) -> Self {
        // Shift the year to begin in March so the leap day lands at the end.
        let y = if m <= 2 { y - 1 } else { y };
        let era = if y >= 0 { y } else { y - 399 } / 400;
        let yoe = y - era * 400; // [0, 399]
        let mp = (m + 9) % 12; // Mar=0 ... Feb=11
        let doy = (153 * mp + 2) / 5 + d - 1; // [0, 365]
        let doe = yoe * 365 + yoe / 4 - yoe / 100 + doy; // [0, 146096]
        Day(era * 146097 + doe - 719468)
    }

    /// The inverse of `from_ymd`.
    pub fn to_ymd(self) -> (i64, i64, i64) {
        let z = self.0 + 719468;
        let era = if z >= 0 { z } else { z - 146096 } / 146097;
        let doe = z - era * 146097; // [0, 146096]
        let yoe = (doe - doe / 1460 + doe / 36524 - doe / 146096) / 365; // [0, 399]
        let y = yoe + era * 400;
        let doy = doe - (365 * yoe + yoe / 4 - yoe / 100); // [0, 365]
        let mp = (5 * doy + 2) / 153; // [0, 11]
        let d = doy - (153 * mp + 2) / 5 + 1; // [1, 31]
        let m = if mp < 10 { mp + 3 } else { mp - 9 }; // [1, 12]
        (if m <= 2 { y + 1 } else { y }, m, d)
    }

    /// Validating constructor: rejects impossible dates (2026-02-30, month 13).
    pub fn from_ymd_checked(y: i64, m: i64, d: i64) -> Option<Self> {
        if !(1..=12).contains(&m) || d < 1 || d > days_in_month(y, m) {
            return None;
        }
        Some(Self::from_ymd(y, m, d))
    }

    /// Parses "YYYY-MM-DD" (optionally with a time suffix, e.g. ISO-8601).
    pub fn parse_iso(s: &str) -> Option<Self> {
        let s = s.get(0..10)?;
        let mut it = s.split('-');
        let y: i64 = it.next()?.parse().ok()?;
        let m: i64 = it.next()?.parse().ok()?;
        let d: i64 = it.next()?.parse().ok()?;
        Self::from_ymd_checked(y, m, d)
    }

    /// Parses RFC-822-style dates as used in RSS pubDate,
    /// e.g. "Sat, 04 Jul 2026 09:00:00 GMT".
    pub fn parse_rfc822ish(s: &str) -> Option<Self> {
        let parts: Vec<&str> = s.split_whitespace().collect();
        for w in parts.windows(3) {
            if let (Ok(d), Some(m), Ok(y)) = (
                w[0].parse::<i64>(),
                month_num(w[1]),
                w[2].parse::<i64>(),
            ) {
                if let Some(day) = Self::from_ymd_checked(y, m, d) {
                    return Some(day);
                }
            }
        }
        None
    }
}

fn month_num(s: &str) -> Option<i64> {
    if s.len() < 3 {
        return None;
    }
    Some(match &s.to_ascii_lowercase()[..3] {
        "jan" => 1,
        "feb" => 2,
        "mar" => 3,
        "apr" => 4,
        "may" => 5,
        "jun" => 6,
        "jul" => 7,
        "aug" => 8,
        "sep" => 9,
        "oct" => 10,
        "nov" => 11,
        "dec" => 12,
        _ => return None,
    })
}

impl fmt::Display for Day {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let (y, m, d) = self.to_ymd();
        write!(f, "{y:04}-{m:02}-{d:02}")
    }
}

// ---------------------------------------------------------------------------
// Documents
// ---------------------------------------------------------------------------

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Document {
    pub id: String,
    pub sector: SectorId,
    pub url: Option<String>,
    pub title: String,
    pub body: String,
    pub published_day: Option<Day>,
    pub published_raw: Option<String>,
    pub authors: Vec<String>,
    /// Source-side classification, e.g. arXiv categories ("cs.LG").
    pub tags: Vec<String>,
    pub provenance: Provenance,
}

// ---------------------------------------------------------------------------
// Entities & mentions (the resolution layer)
// ---------------------------------------------------------------------------

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub enum EntityKind {
    Org,
    Person,
    Model,
    Tech,
    Topic,
    Place,
    Unknown,
}

/// A canonical entity with its alias table. The alias table IS the entity
/// resolution mechanism: "DeepSeek-V4", "DeepSeek V4 Pro" and "DeepSeek" all
/// resolve to one node, which is what makes cross-source signals possible.
#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Entity {
    pub id: String,
    pub name: String,
    pub kind: EntityKind,
    pub aliases: Vec<String>,
}

/// One (entity, document) resolution. Deliberately per-document, not
/// per-occurrence: burst statistics count *documents mentioning*, which is
/// robust to keyword stuffing inside a single article.
#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Mention {
    pub entity_id: String,
    pub doc_id: String,
    pub day: Option<Day>,
    pub source_id: String,
    pub sector: SectorId,
}

/// A surface form found by discovery heuristics that is NOT yet a known
/// entity. These are the gazetteer's growth loop: review, promote, repeat.
#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Discovered {
    pub surface: String,
    pub doc_ids: Vec<String>,
}

// ---------------------------------------------------------------------------
// Signals (the product layer)
// ---------------------------------------------------------------------------

#[derive(Clone, Copy, Debug, PartialEq, Eq, Serialize, Deserialize)]
pub enum SignalKind {
    /// Entity's document frequency today is a statistical outlier vs baseline.
    RisingEntity,
    /// Entity independently reported by multiple distinct sources.
    Corroborated,
    /// Unrecognized surface form recurring across documents.
    EmergingEntity,
}

/// A signal is a claim + a score + *evidence*. Evidence-linking is what
/// separates intelligence from vibes: every line in a brief traces back to
/// specific documents with provenance.
#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Signal {
    pub kind: SignalKind,
    pub headline: String,
    pub score: f64,
    pub entity_ids: Vec<String>,
    pub evidence: Vec<String>,
    pub detail: String,
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn day_iso_roundtrip() {
        let d = Day::parse_iso("2026-07-04").unwrap();
        assert_eq!(d.to_string(), "2026-07-04");
        assert_eq!(Day::parse_iso("2026-07-04T12:00:00Z").unwrap(), d);
    }

    #[test]
    fn day_rfc822() {
        let d = Day::parse_rfc822ish("Sat, 04 Jul 2026 09:00:00 GMT").unwrap();
        assert_eq!(d, Day::from_ymd(2026, 7, 4));
    }

    #[test]
    fn day_ordering() {
        assert!(Day::from_ymd(2026, 7, 3) < Day::from_ymd(2026, 7, 4));
    }

    // --- T9.3: no phantom days at month boundaries ---------------------------

    /// The bug this replaced: consecutive calendar days must be consecutive
    /// ordinals, or `analyze`'s zero-filled baseline invents empty days that
    /// never existed and inflates burst z-scores across the boundary.
    #[test]
    fn consecutive_days_are_consecutive_ordinals_across_month_boundaries() {
        // Jan -> Feb (31-day month)
        assert_eq!(
            Day::from_ymd(2026, 2, 1).0 - Day::from_ymd(2026, 1, 31).0,
            1
        );
        // Feb -> Mar, non-leap year: the old encoding left 3 phantom days here.
        assert_eq!(
            Day::from_ymd(2026, 3, 1).0 - Day::from_ymd(2026, 2, 28).0,
            1
        );
        // Feb -> Mar, leap year: Feb 29 exists and is exactly one day.
        assert_eq!(
            Day::from_ymd(2024, 3, 1).0 - Day::from_ymd(2024, 2, 29).0,
            1
        );
        // Dec -> Jan (year boundary)
        assert_eq!(
            Day::from_ymd(2027, 1, 1).0 - Day::from_ymd(2026, 12, 31).0,
            1
        );
        // Apr -> May (30-day month)
        assert_eq!(
            Day::from_ymd(2026, 5, 1).0 - Day::from_ymd(2026, 4, 30).0,
            1
        );
    }

    /// A whole-year walk: every ordinal in the range is a real date, and the
    /// count is exactly the year's length. This is the property `analyze`
    /// relies on when it iterates `[window_start, window_end)`.
    #[test]
    fn a_year_of_ordinals_contains_no_gaps() {
        for (year, len) in [(2026_i64, 365_i64), (2024, 366)] {
            let start = Day::from_ymd(year, 1, 1).0;
            let end = Day::from_ymd(year + 1, 1, 1).0;
            assert_eq!(end - start, len, "year {year} length");
            // Every ordinal round-trips to a date inside that year.
            for o in start..end {
                let (y, m, d) = Day(o).to_ymd();
                assert_eq!(y, year);
                assert!((1..=12).contains(&m) && d >= 1 && d <= days_in_month(y, m));
                assert_eq!(Day::from_ymd(y, m, d).0, o);
            }
        }
    }

    #[test]
    fn impossible_dates_are_rejected() {
        assert!(Day::parse_iso("2026-02-30").is_none()); // Feb never has 30
        assert!(Day::parse_iso("2026-02-29").is_none()); // 2026 is not a leap year
        assert!(Day::parse_iso("2024-02-29").is_some()); // 2024 is
        assert!(Day::parse_iso("2026-13-01").is_none());
        assert!(Day::parse_iso("2026-00-10").is_none());
        assert!(Day::parse_iso("2026-04-31").is_none()); // April has 30
    }

    #[test]
    fn epoch_and_known_dates_are_exact() {
        assert_eq!(Day::from_ymd(1970, 1, 1).0, 0);
        assert_eq!(Day::from_ymd(2000, 3, 1).0, 11017);
        assert_eq!(Day::parse_iso("2026-07-04").unwrap().to_string(), "2026-07-04");
    }
}
