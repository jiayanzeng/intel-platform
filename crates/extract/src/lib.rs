//! intel-extract: normalization + near-duplicate collapse.
//!
//! Syndication means the same story arrives from multiple feeds with cosmetic
//! edits. If you count those as independent observations, every downstream
//! statistic (bursts, corroboration) is corrupted. SimHash fingerprints make
//! near-duplicates cheap to detect: similar texts differ in only a few of the
//! 64 bits.
//!
//! Seed-grade choices (and their production swaps):
//! - FNV-1a feature hashing -> xxhash/ahash for speed (FNV is deterministic
//!   and dependency-free, which the persistent store relies on);
//! - O(n^2) pairwise comparison -> LSH banding over fingerprint chunks so
//!   dedup stays sub-linear at archive scale;
//! - keep-first policy by (day, id) -> keep-canonical policy (prefer the
//!   original publisher over the syndicator via source ranking).

use intel_core::Document;

/// The radius-16 identity rule is calibrated only for documents with at least
/// this many SimHash features. Step 3 measured 26 as the smallest feature count
/// in the golden news corpus; the SEC corpus had at most 10. Keeping the floor
/// at the measured boundary avoids extrapolating into the unmeasured 11–25
/// range.
pub const DEDUP_MIN_FEATURES: usize = 26;

/// Deterministic 64-bit FNV-1a. Stability across runs matters because
/// fingerprints can be persisted alongside documents.
pub fn fnv1a64(bytes: &[u8]) -> u64 {
    let mut h: u64 = 0xcbf29ce484222325;
    for b in bytes {
        h ^= *b as u64;
        h = h.wrapping_mul(0x100000001b3);
    }
    h
}

pub fn tokens(text: &str) -> Vec<String> {
    text.to_lowercase()
        .split(|c: char| !c.is_alphanumeric())
        .filter(|s| !s.is_empty())
        .map(|s| s.to_string())
        .collect()
}

fn features(text: &str) -> Vec<String> {
    let toks = tokens(text);
    if toks.len() >= 3 {
        toks.windows(3).map(|window| window.join(" ")).collect()
    } else {
        toks
    }
}

pub fn simhash_feature_count(text: &str) -> usize {
    features(text).len()
}

pub fn dedup_eligible(left_features: usize, right_features: usize) -> bool {
    left_features >= DEDUP_MIN_FEATURES && right_features >= DEDUP_MIN_FEATURES
}

/// 64-bit SimHash over 3-token shingles (falls back to unigrams for very
/// short texts). Each feature votes on each bit; the majority wins.
pub fn simhash(text: &str) -> u64 {
    let feats = features(text);
    if feats.is_empty() {
        return 0;
    }
    let mut v = [0i64; 64];
    for f in &feats {
        let h = fnv1a64(f.as_bytes());
        for (b, slot) in v.iter_mut().enumerate() {
            if (h >> b) & 1 == 1 {
                *slot += 1;
            } else {
                *slot -= 1;
            }
        }
    }
    let mut out = 0u64;
    for (b, slot) in v.iter().enumerate() {
        if *slot > 0 {
            out |= 1u64 << b;
        }
    }
    out
}

pub fn hamming(a: u64, b: u64) -> u32 {
    (a ^ b).count_ones()
}

pub struct DedupDrop {
    pub dropped_id: String,
    pub kept_id: String,
    pub distance: u32,
}

pub struct DedupResult {
    pub kept: Vec<Document>,
    pub drops: Vec<DedupDrop>,
}

/// Collapses near-duplicates from fingerprints persisted by the store, keeping
/// the earliest by (day, id).
pub fn dedup_near(mut docs: Vec<(Document, u64)>, max_distance: u32) -> DedupResult {
    docs.sort_by(|(a, _), (b, _)| {
        a.published_day
            .cmp(&b.published_day)
            .then_with(|| a.id.cmp(&b.id))
    });

    let mut kept: Vec<(u64, usize, Document)> = Vec::new();
    let mut drops = Vec::new();

    for (d, fp) in docs {
        let feature_count = simhash_feature_count(&format!("{} {}", d.title, d.body));
        let mut matched: Option<(u32, String)> = None;
        for (kfp, kept_features, k) in &kept {
            let dist = hamming(*kfp, fp);
            if dedup_eligible(*kept_features, feature_count) && dist <= max_distance {
                matched = Some((dist, k.id.clone()));
                break;
            }
        }
        match matched {
            Some((distance, kept_id)) => drops.push(DedupDrop {
                dropped_id: d.id,
                kept_id,
                distance,
            }),
            None => kept.push((fp, feature_count, d)),
        }
    }

    DedupResult {
        kept: kept.into_iter().map(|(_, _, d)| d).collect(),
        drops,
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use intel_core::{Day, License, Provenance, SectorId, SourceKind};

    fn doc(id: &str, title: &str, body: &str) -> Document {
        Document {
            id: id.into(),
            sector: SectorId("technology".into()),
            url: None,
            title: title.into(),
            body: body.into(),
            published_day: Day::parse_iso("2026-07-04"),
            published_raw: Some("2026-07-04".into()),
            authors: vec![],
            tags: vec![],
            provenance: Provenance {
                source_id: "test".into(),
                retrieved_from: "fixture".into(),
                kind: SourceKind::Rss,
                license: License::CcBy,
            },
        }
    }

    #[test]
    fn identical_texts_have_zero_distance() {
        let t = "DeepSeek opens V4 Pro weights for research use starting today";
        assert_eq!(hamming(simhash(t), simhash(t)), 0);
    }

    #[test]
    fn unrelated_texts_are_far_apart() {
        let a =
            simhash("Sparse mixture of experts routing under memory constraints on accelerators");
        let b = simhash("Coastal salinity trends from twenty years of public buoy measurements");
        assert!(hamming(a, b) > 10, "distance was {}", hamming(a, b));
    }

    #[test]
    fn light_edits_stay_close() {
        let a = simhash("DeepSeek said researchers can request the V4 Pro checkpoints starting today. Early adopters are serving the release through vLLM at launch.");
        let b = simhash("Syndicated: DeepSeek said researchers can request the V4 Pro checkpoints starting today. Early adopters are serving the release through vLLM at launch.");
        assert!(hamming(a, b) <= 10, "distance was {}", hamming(a, b));
    }

    #[test]
    fn dedup_consumes_supplied_fingerprints_instead_of_recomputing() {
        let first = doc(
            "a",
            "Sparse mixture of experts routing under memory constraints",
            "Researchers measured deterministic accelerator scheduling across many independent \
             inference workloads and published the complete reproducible evaluation today for \
             independent verification across laboratories worldwide",
        );
        let second = doc(
            "b",
            "Coastal salinity trends from public buoy measurements",
            "Oceanographers compared twenty years of estuary observations across seasonal \
             currents and released the complete reproducible marine dataset today for independent \
             verification across coastal research institutes worldwide",
        );
        assert!(
            simhash_feature_count(&format!("{} {}", first.title, first.body)) >= DEDUP_MIN_FEATURES
        );
        assert!(
            simhash_feature_count(&format!("{} {}", second.title, second.body))
                >= DEDUP_MIN_FEATURES
        );
        let fresh_first = simhash(&format!("{} {}", first.title, first.body));
        let fresh_second = simhash(&format!("{} {}", second.title, second.body));
        assert!(hamming(fresh_first, fresh_second) > 16);

        // This deliberately violating double gives unrelated documents the
        // same stored value. Recomputing would keep both; consuming the supplied
        // fingerprints must collapse the second and report distance zero.
        let result = dedup_near(vec![(first, 7), (second, 7)], 16);
        assert_eq!(result.kept.len(), 1);
        assert_eq!(result.drops.len(), 1);
        assert_eq!(result.drops[0].dropped_id, "b");
        assert_eq!(result.drops[0].kept_id, "a");
        assert_eq!(result.drops[0].distance, 0);
    }

    #[test]
    fn sparse_documents_remain_distinct_even_with_identical_fingerprints() {
        let first = doc("a", "Quarterly filing", "Revenue increased");
        let second = doc("b", "Quarterly filing", "Revenue increased");
        let first_features = simhash_feature_count(&format!("{} {}", first.title, first.body));
        let second_features = simhash_feature_count(&format!("{} {}", second.title, second.body));
        assert!(first_features < DEDUP_MIN_FEATURES);
        assert!(second_features < DEDUP_MIN_FEATURES);
        assert!(!dedup_eligible(first_features, second_features));

        let result = dedup_near(vec![(first, 7), (second, 7)], 16);
        assert_eq!(result.kept.len(), 2);
        assert!(result.drops.is_empty());
    }
}
