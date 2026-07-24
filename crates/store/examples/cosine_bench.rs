use intel_store::SqliteStore;
use serde_json::json;
use std::env;
use std::path::Path;
use std::time::Instant;

fn usage() -> ! {
    eprintln!("usage: cosine_bench <disposable-db> <dimension> <samples> <sector>");
    std::process::exit(2);
}

fn deterministic_vector(seed: u64, dimension: usize) -> Vec<f32> {
    let mut state = seed | 1;
    (0..dimension)
        .map(|index| {
            state ^= state << 13;
            state ^= state >> 7;
            state ^= state << 17;
            let centered = ((state ^ index as u64) & 0xffff) as f32 - 32_767.5;
            centered / 32_767.5
        })
        .collect()
}

fn percentile_nearest_rank(samples: &[f64], percentile: f64) -> f64 {
    let mut ordered = samples.to_vec();
    ordered.sort_by(f64::total_cmp);
    let rank = (percentile * ordered.len() as f64).ceil() as usize;
    ordered[rank.saturating_sub(1)]
}

// `usize::is_multiple_of` is newer than the offline Rust 1.78 floor.
#[allow(clippy::manual_is_multiple_of)]
fn median(samples: &[f64]) -> f64 {
    let mut ordered = samples.to_vec();
    ordered.sort_by(f64::total_cmp);
    let middle = ordered.len() / 2;
    if ordered.len() % 2 == 0 {
        (ordered[middle - 1] + ordered[middle]) / 2.0
    } else {
        ordered[middle]
    }
}

fn main() {
    let mut args = env::args().skip(1);
    let database = args.next().unwrap_or_else(|| usage());
    let dimension = args
        .next()
        .and_then(|value| value.parse::<usize>().ok())
        .filter(|value| *value > 0)
        .unwrap_or_else(|| usage());
    let sample_count = args
        .next()
        .and_then(|value| value.parse::<usize>().ok())
        .filter(|value| *value > 0)
        .unwrap_or_else(|| usage());
    let sector = args
        .next()
        .filter(|value| !value.is_empty())
        .unwrap_or_else(|| usage());
    if args.next().is_some() {
        usage();
    }

    let store = SqliteStore::open(Path::new(&database)).expect("open disposable database");
    let documents = store.load_all().expect("load disposable corpus");
    assert!(!documents.is_empty(), "benchmark corpus must not be empty");
    assert!(
        documents.iter().all(|document| document.sector.0 == sector),
        "benchmark sector must cover every document"
    );

    let model = format!("d4-exact-cosine-{dimension}");
    for (batch_index, batch) in documents.chunks(128).enumerate() {
        let items: Vec<(String, Vec<f32>)> = batch
            .iter()
            .enumerate()
            .map(|(index, document)| {
                let seed =
                    ((batch_index * 128 + index + 1) as u64).wrapping_mul(0x9e3779b97f4a7c15);
                (document.id.clone(), deterministic_vector(seed, dimension))
            })
            .collect();
        store
            .upsert_embeddings(&model, &items)
            .expect("seed deterministic embeddings");
    }

    let query = deterministic_vector(0xd4d4d4d4d4d4d4d5, dimension);
    let sectors = vec![sector.clone()];
    let warmup = store
        .vector_search(&model, &query, &sectors, 8)
        .expect("warm exact-cosine search");
    assert_eq!(warmup.hits.len(), 8, "warmup must return eight hits");
    assert_eq!(
        warmup.dimension_mismatches, 0,
        "warmup must have no dimension mismatches"
    );

    let mut samples_ms = Vec::with_capacity(sample_count);
    for _ in 0..sample_count {
        let started = Instant::now();
        let result = store
            .vector_search(&model, &query, &sectors, 8)
            .expect("exact-cosine search");
        let elapsed = started.elapsed().as_secs_f64() * 1_000.0;
        assert_eq!(result.hits.len(), 8, "sample must return eight hits");
        assert_eq!(
            result.dimension_mismatches, 0,
            "sample must have no dimension mismatches"
        );
        samples_ms.push(elapsed);
    }

    let minimum = samples_ms.iter().copied().fold(f64::INFINITY, f64::min);
    let maximum = samples_ms.iter().copied().fold(f64::NEG_INFINITY, f64::max);
    let report = json!({
        "engine": "intel_store::SqliteStore::vector_search",
        "algorithm": "brute-force exact cosine",
        "database": database,
        "documents": documents.len(),
        "sector": sector,
        "dimension": dimension,
        "limit": 8,
        "warmup_samples": 1,
        "measured_samples": sample_count,
        "minimum_ms": minimum,
        "median_ms": median(&samples_ms),
        "p95_ms": percentile_nearest_rank(&samples_ms, 0.95),
        "maximum_ms": maximum,
        "p95_method": "nearest-rank: sorted_samples[ceil(0.95*n)-1]",
        "samples_ms": samples_ms,
        "dimension_mismatches": 0,
    });
    println!(
        "{}",
        serde_json::to_string(&report).expect("serialize benchmark report")
    );
}
