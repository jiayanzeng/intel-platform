//! T5 measurement harness — run before writing any LSH, not after.
//!
//!     cargo run --release -p intel-extract --example dedup_bench
//!
//! `docs/T8-scale-design-note.md` asserts that `dedup_near`'s O(n^2) pairwise
//! scan is the swap most likely to be needed first. That is a hypothesis about
//! where the time goes. This measures it, and separately measures whether LSH
//! banding can even prune anything at the threshold this project actually uses
//! (hamming <= 16 on a 64-bit fingerprint).

use intel_extract::{hamming, simhash};
use std::collections::HashMap;
use std::time::Instant;

/// The production threshold (`ViewParams::dedup_max_distance`).
const MAX_DIST: u32 = 16;
/// Fingerprint width.
const BITS: u32 = 64;

/// Synthetic corpus with realistic body length and a sprinkling of near-dups
/// (syndicated copies), which is the shape the real corpus has.
fn corpus(n: usize) -> Vec<String> {
    let vocab = [
        "sparse",
        "attention",
        "mixture",
        "experts",
        "routing",
        "memory",
        "accelerator",
        "inference",
        "latency",
        "throughput",
        "quantization",
        "kernel",
        "cache",
        "context",
        "transformer",
        "checkpoint",
        "weights",
        "benchmark",
        "retrieval",
        "embedding",
        "cluster",
        "gradient",
        "distillation",
        "speculative",
        "decoding",
        "tokenizer",
    ];
    let mut out = Vec::with_capacity(n);
    let mut seed: u64 = 0x9E3779B97F4A7C15;
    let mut rnd = || {
        seed ^= seed << 13;
        seed ^= seed >> 7;
        seed ^= seed << 17;
        seed
    };
    for i in 0..n {
        // Every 20th doc is a light edit of the previous one — a syndicated copy.
        if i % 20 == 19 && !out.is_empty() {
            let prev: &String = out.last().unwrap();
            out.push(format!("Syndicated: {prev}"));
            continue;
        }
        // ~300 tokens ≈ a 2KB body, which is what the real feeds carry.
        let words: Vec<&str> = (0..300)
            .map(|_| vocab[(rnd() % vocab.len() as u64) as usize])
            .collect();
        out.push(words.join(" "));
    }
    out
}

/// Exhaustive: what `dedup_near` does today, given precomputed fingerprints.
/// Returns the set of (i, j) pairs within MAX_DIST, i < j.
fn exhaustive(fps: &[u64]) -> Vec<(usize, usize)> {
    let mut pairs = Vec::new();
    for i in 0..fps.len() {
        for j in (i + 1)..fps.len() {
            if hamming(fps[i], fps[j]) <= MAX_DIST {
                pairs.push((i, j));
            }
        }
    }
    pairs
}

/// Band layout for EXACT recall at distance d.
///
/// Pigeonhole: two fingerprints differing in d bits can touch at most d bands,
/// so if we have b > d bands, at least one band must be bit-identical and the
/// pair is guaranteed to collide in it. Exact recall at d <= 16 therefore needs
/// **b >= 17** bands. 64 bits / 17 bands = bands of 3 or 4 bits.
///
/// That is the whole problem, and it is arithmetic, not implementation: a
/// 4-bit band has 16 possible values, so an average bucket holds n/16 of the
/// corpus. Nearly everything collides with nearly everything.
fn bands() -> Vec<(u32, u32)> {
    // 13 bands of 4 bits + 4 bands of 3 bits = 52 + 12 = 64 bits, 17 bands.
    let mut v = Vec::new();
    let mut off = 0u32;
    for i in 0..17u32 {
        let w = if i < 13 { 4 } else { 3 };
        v.push((off, w));
        off += w;
    }
    assert_eq!(off, BITS);
    v
}

/// Banded LSH: index by band value, compare only within-band candidates.
/// Returns (pairs found, number of candidate pairs actually compared).
fn banded(fps: &[u64]) -> (Vec<(usize, usize)>, usize) {
    let layout = bands();
    let mut index: Vec<HashMap<u64, Vec<usize>>> = vec![HashMap::new(); layout.len()];
    for (i, fp) in fps.iter().enumerate() {
        for (b, (off, w)) in layout.iter().enumerate() {
            let key = (fp >> off) & ((1u64 << w) - 1);
            index[b].entry(key).or_default().push(i);
        }
    }

    let mut seen = std::collections::HashSet::new();
    let mut pairs = Vec::new();
    let mut compared = 0usize;
    for (b, (off, w)) in layout.iter().enumerate() {
        for (i, fp) in fps.iter().enumerate() {
            let key = (fp >> off) & ((1u64 << w) - 1);
            for &j in &index[b][&key] {
                if j <= i {
                    continue;
                }
                if !seen.insert((i, j)) {
                    continue; // already compared via an earlier band
                }
                compared += 1;
                if hamming(fps[i], fps[j]) <= MAX_DIST {
                    pairs.push((i, j));
                }
            }
        }
    }
    pairs.sort_unstable();
    (pairs, compared)
}

fn main() {
    println!("T5 measurement: dedup_near at threshold hamming <= {MAX_DIST} on {BITS}-bit SimHash");
    println!(
        "exact-recall banding needs b > d  =>  b >= {} bands  =>  bands of {:.1} bits\n",
        MAX_DIST + 1,
        BITS as f64 / (MAX_DIST + 1) as f64
    );

    println!(
        "{:>7} | {:>11} | {:>11} | {:>9} | {:>13} | {:>10} | {:>7}",
        "n", "simhash", "scan O(n^2)", "scan/tot", "banded total", "cand/pairs", "recall"
    );
    println!("{}", "-".repeat(88));

    for n in [1_000usize, 2_500, 5_000, 10_000, 20_000] {
        let docs = corpus(n);

        // 1. Fingerprinting — the linear term. dedup_near does this on EVERY
        //    call, for every document in the corpus.
        let t = Instant::now();
        let fps: Vec<u64> = docs.iter().map(|d| simhash(d)).collect();
        let t_simhash = t.elapsed();

        // 2. The pairwise scan — the quadratic term the design note blames.
        let t = Instant::now();
        let exact = exhaustive(&fps);
        let t_scan = t.elapsed();

        // 3. Banded LSH, exact-recall layout.
        //
        // Guarded: at 76% candidate density the de-dup set of candidate pairs is
        // itself O(n^2) *in memory*, and at n=20k it tries to allocate ~4.5 GB
        // and aborts. That is not a bug in this harness — it is the finding.
        // An index whose candidate set is a constant fraction of all pairs has
        // not indexed anything.
        let banded_result = if n <= 10_000 {
            let t = Instant::now();
            let (found, compared) = banded(&fps);
            Some((t.elapsed(), found, compared))
        } else {
            None
        };

        let total_pairs = n * (n - 1) / 2;
        let scan_share =
            t_scan.as_secs_f64() / (t_scan.as_secs_f64() + t_simhash.as_secs_f64()) * 100.0;

        match banded_result {
            Some((t_banded, found, compared)) => {
                let recall = if exact.is_empty() {
                    1.0
                } else {
                    let e: std::collections::HashSet<_> = exact.iter().collect();
                    found.iter().filter(|p| e.contains(p)).count() as f64 / exact.len() as f64
                };
                println!(
                    "{:>7} | {:>9.1}ms | {:>9.1}ms | {:>8.1}% | {:>11.1}ms | {:>9.1}% | {:>6.1}%",
                    n,
                    t_simhash.as_secs_f64() * 1e3,
                    t_scan.as_secs_f64() * 1e3,
                    scan_share,
                    t_banded.as_secs_f64() * 1e3,
                    compared as f64 / total_pairs as f64 * 100.0,
                    recall * 100.0,
                );
            }
            None => {
                println!(
                    "{:>7} | {:>9.1}ms | {:>9.1}ms | {:>8.1}% | {:>13} | {:>10} | {:>7}",
                    n,
                    t_simhash.as_secs_f64() * 1e3,
                    t_scan.as_secs_f64() * 1e3,
                    scan_share,
                    "OOM (~4.5GB)",
                    "n/a",
                    "n/a",
                );
            }
        }
    }

    println!("\nlegend:");
    println!("  simhash    = fingerprinting the corpus (the LINEAR term)");
    println!("  scan       = exhaustive pairwise hamming (the QUADRATIC term)");
    println!("  scan/tot   = share of dedup time the quadratic term is actually responsible for");
    println!(
        "  cand/pairs = fraction of all pairs banding still has to compare (100% = no pruning)"
    );
    println!("  recall     = fraction of true near-dup pairs banding finds (must be 100%)");
}
