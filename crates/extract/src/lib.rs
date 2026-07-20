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

/// 64-bit SimHash over 3-token shingles (falls back to unigrams for very
/// short texts). Each feature votes on each bit; the majority wins.
pub fn simhash(text: &str) -> u64 {
    let toks = tokens(text);
    let feats: Vec<String> = if toks.len() >= 3 {
        toks.windows(3).map(|w| w.join(" ")).collect()
    } else {
        toks
    };
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

/// Collapses near-duplicates, keeping the earliest by (day, id).
pub fn dedup_near(mut docs: Vec<Document>, max_distance: u32) -> DedupResult {
    docs.sort_by(|a, b| {
        a.published_day
            .cmp(&b.published_day)
            .then_with(|| a.id.cmp(&b.id))
    });

    let mut kept: Vec<(u64, Document)> = Vec::new();
    let mut drops = Vec::new();

    for d in docs {
        let fp = simhash(&format!("{} {}", d.title, d.body));
        let mut matched: Option<(u32, String)> = None;
        for (kfp, k) in &kept {
            let dist = hamming(*kfp, fp);
            if dist <= max_distance {
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
            None => kept.push((fp, d)),
        }
    }

    DedupResult {
        kept: kept.into_iter().map(|(_, d)| d).collect(),
        drops,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn identical_texts_have_zero_distance() {
        let t = "DeepSeek opens V4 Pro weights for research use starting today";
        assert_eq!(hamming(simhash(t), simhash(t)), 0);
    }

    #[test]
    fn unrelated_texts_are_far_apart() {
        let a = simhash("Sparse mixture of experts routing under memory constraints on accelerators");
        let b = simhash("Coastal salinity trends from twenty years of public buoy measurements");
        assert!(hamming(a, b) > 10, "distance was {}", hamming(a, b));
    }

    #[test]
    fn light_edits_stay_close() {
        let a = simhash("DeepSeek said researchers can request the V4 Pro checkpoints starting today. Early adopters are serving the release through vLLM at launch.");
        let b = simhash("Syndicated: DeepSeek said researchers can request the V4 Pro checkpoints starting today. Early adopters are serving the release through vLLM at launch.");
        assert!(hamming(a, b) <= 10, "distance was {}", hamming(a, b));
    }
}
