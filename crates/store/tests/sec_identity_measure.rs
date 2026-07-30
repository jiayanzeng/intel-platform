#[path = "../../analyze/src/lib.rs"]
mod shipped_analyze;

use intel_core::{
    Day, Document, Entity, EntityKind, License, Mention, Provenance, SectorId, SignalKind,
    SourceKind,
};
use intel_extract::{dedup_near, hamming, simhash, tokens, DedupResult};
use intel_store::SqliteStore;
use serde_json::Value;
use std::collections::{BTreeMap, BTreeSet};
use std::io::{Cursor, Read};
use std::path::{Path, PathBuf};
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

const SEC_SOURCE_ID: &str = "sec-edgar-usgaap";

struct DisposableDir(PathBuf);

impl DisposableDir {
    fn create() -> Self {
        let nonce = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .expect("system clock must be after the Unix epoch")
            .as_nanos();
        let path = std::env::temp_dir().join(format!(
            "intel-platform-sec-identity-{}-{nonce}",
            std::process::id()
        ));
        std::fs::create_dir(&path).expect("create identity-measure directory");
        Self(path)
    }
}

impl Drop for DisposableDir {
    fn drop(&mut self) {
        std::fs::remove_dir_all(&self.0).expect("remove identity-measure directory");
    }
}

fn root() -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("../..")
        .canonicalize()
        .expect("resolve repository root")
}

fn read_u32(reader: &mut Cursor<Vec<u8>>) -> usize {
    let mut bytes = [0; 4];
    reader.read_exact(&mut bytes).expect("read export u32");
    u32::from_le_bytes(bytes) as usize
}

fn read_string(reader: &mut Cursor<Vec<u8>>) -> String {
    let length = read_u32(reader);
    let mut bytes = vec![0; length];
    reader
        .read_exact(&mut bytes)
        .expect("read export string bytes");
    String::from_utf8(bytes).expect("export string must be UTF-8")
}

fn read_tag(reader: &mut Cursor<Vec<u8>>) -> bool {
    let mut tag = [0];
    reader.read_exact(&mut tag).expect("read export tag");
    match tag[0] {
        0 => false,
        1 => true,
        other => panic!("invalid export tag {other}"),
    }
}

fn read_optional_string(reader: &mut Cursor<Vec<u8>>) -> Option<String> {
    read_tag(reader).then(|| read_string(reader))
}

fn read_strings(reader: &mut Cursor<Vec<u8>>) -> Vec<String> {
    (0..read_u32(reader)).map(|_| read_string(reader)).collect()
}

fn read_document_export(path: &Path) -> Vec<Document> {
    let bytes = std::fs::read(path).expect("read parser-produced export");
    let mut reader = Cursor::new(bytes);
    let mut header = vec![0; b"INTEL-DOCUMENT-EXPORT-1\n".len()];
    reader.read_exact(&mut header).expect("read export header");
    assert_eq!(header, b"INTEL-DOCUMENT-EXPORT-1\n");

    let count = read_u32(&mut reader);
    let documents = (0..count)
        .map(|_| {
            let id = read_string(&mut reader);
            let sector = SectorId(read_string(&mut reader));
            let url = read_optional_string(&mut reader);
            let title = read_string(&mut reader);
            let body = read_string(&mut reader);
            let published_day = if read_tag(&mut reader) {
                let mut bytes = [0; 8];
                reader.read_exact(&mut bytes).expect("read export day");
                Some(Day(i64::from_le_bytes(bytes)))
            } else {
                None
            };
            let published_raw = read_optional_string(&mut reader);
            let authors = read_strings(&mut reader);
            let tags = read_strings(&mut reader);
            let source_id = read_string(&mut reader);
            let retrieved_from = read_string(&mut reader);
            let kind =
                SourceKind::parse(&read_string(&mut reader)).expect("known exported source kind");
            let license =
                License::parse(&read_string(&mut reader)).expect("known exported license");
            Document {
                id,
                sector,
                url,
                title,
                body,
                published_day,
                published_raw,
                authors,
                tags,
                provenance: Provenance {
                    source_id,
                    retrieved_from,
                    kind,
                    license,
                },
            }
        })
        .collect();
    assert_eq!(
        reader.position(),
        reader.get_ref().len() as u64,
        "no trailing or unread export bytes"
    );
    documents
}

fn parser_produced_documents(disposable: &DisposableDir) -> Vec<Document> {
    let root = root();
    let export_path = disposable.0.join("documents.bin");
    let nested_target = disposable.0.join("cargo-target");
    let output = Command::new(env!("CARGO"))
        .current_dir(&root)
        .env("CARGO_TARGET_DIR", nested_target)
        .env("INTEL_SEC_REPLAY_EXPORT_PATH", &export_path)
        .args([
            "test",
            "--offline",
            "--locked",
            "-p",
            "intel-ingest",
            "--test",
            "sec_observation_replay",
            "--",
            "--exact",
            "replays_sec_observation_through_shipped_rss_parser",
        ])
        .output()
        .expect("execute shipped-parser export test");
    assert!(
        output.status.success(),
        "parser export failed\nstdout:\n{}\nstderr:\n{}",
        String::from_utf8_lossy(&output.stdout),
        String::from_utf8_lossy(&output.stderr)
    );
    let documents = read_document_export(&export_path);
    assert_eq!(documents.len(), 208);
    documents
}

fn feature_count(document: &Document) -> usize {
    let count = tokens(&format!("{} {}", document.title, document.body)).len();
    if count >= 3 {
        count - 2
    } else {
        count
    }
}

fn count_distribution(values: impl IntoIterator<Item = usize>) -> BTreeMap<usize, usize> {
    let mut distribution = BTreeMap::new();
    for value in values {
        *distribution.entry(value).or_insert(0) += 1;
    }
    distribution
}

fn median(values: &mut [usize]) -> usize {
    values.sort_unstable();
    values[values.len() / 2]
}

fn distance_distribution(corpus: &[(Document, u64)]) -> BTreeMap<u32, usize> {
    let mut distribution = BTreeMap::new();
    for left in 0..corpus.len() {
        for right in (left + 1)..corpus.len() {
            *distribution
                .entry(hamming(corpus[left].1, corpus[right].1))
                .or_insert(0) += 1;
        }
    }
    distribution
}

fn cik(title: &str) -> Option<String> {
    title
        .split('(')
        .filter_map(|part| part.split(')').next())
        .find(|part| part.len() == 10 && part.bytes().all(|byte| byte.is_ascii_digit()))
        .map(ToOwned::to_owned)
}

fn drop_classes(result: &DedupResult, titles: &BTreeMap<String, String>) -> (usize, usize) {
    let mut same_issuer = 0;
    let mut cross_issuer = 0;
    for drop in &result.drops {
        let dropped_cik =
            cik(&titles[&drop.dropped_id]).expect("every dropped SEC title must carry a CIK");
        let kept_cik = cik(&titles[&drop.kept_id]).expect("every kept SEC title must carry a CIK");
        if dropped_cik == kept_cik {
            same_issuer += 1;
        } else {
            cross_issuer += 1;
        }
    }
    (same_issuer, cross_issuer)
}

fn contains_word(hay: &str, needle: &str) -> bool {
    if needle.is_empty() {
        return false;
    }
    let haystack = hay.as_bytes();
    let mut start = 0;
    while let Some(position) = hay[start..].find(needle) {
        let left = start + position;
        let right = left + needle.len();
        let left_ok = left == 0 || !(haystack[left - 1] as char).is_alphanumeric();
        let right_ok = right >= hay.len() || !(haystack[right] as char).is_alphanumeric();
        if left_ok && right_ok {
            return true;
        }
        start = right;
    }
    false
}

fn load_entities() -> Vec<Entity> {
    let raw = std::fs::read_to_string(root().join("config/entities.json"))
        .expect("read committed gazetteer");
    let value: Value = serde_json::from_str(&raw).expect("parse committed gazetteer");
    value["entities"]
        .as_array()
        .expect("entities array")
        .iter()
        .map(|entity| {
            let string = |key: &str| {
                entity[key]
                    .as_str()
                    .unwrap_or_else(|| panic!("entity {key}"))
                    .to_string()
            };
            let kind = match entity["kind"].as_str().expect("entity kind") {
                "Org" => EntityKind::Org,
                "Person" => EntityKind::Person,
                "Model" => EntityKind::Model,
                "Tech" => EntityKind::Tech,
                "Topic" => EntityKind::Topic,
                "Place" => EntityKind::Place,
                "Unknown" => EntityKind::Unknown,
                other => panic!("unknown entity kind {other}"),
            };
            let aliases = entity["aliases"]
                .as_array()
                .expect("entity aliases")
                .iter()
                .map(|alias| alias.as_str().expect("string alias").to_string())
                .collect();
            Entity {
                id: string("id"),
                name: string("name"),
                kind,
                aliases,
            }
        })
        .collect()
}

fn resolve_mentions(documents: &[Document], entities: &[Entity]) -> Vec<Mention> {
    let mut mentions = Vec::new();
    for document in documents {
        let haystack = format!("{} {}", document.title, document.body).to_lowercase();
        for entity in entities {
            if entity
                .aliases
                .iter()
                .chain(std::iter::once(&entity.name))
                .any(|name| contains_word(&haystack, &name.to_lowercase()))
            {
                mentions.push(Mention {
                    entity_id: entity.id.clone(),
                    doc_id: document.id.clone(),
                    day: document.published_day,
                    source_id: document.provenance.source_id.clone(),
                    sector: document.sector.clone(),
                });
            }
        }
    }
    mentions
}

fn day_distribution(documents: &[Document]) -> BTreeMap<String, usize> {
    let mut distribution = BTreeMap::new();
    for day in documents
        .iter()
        .filter_map(|document| document.published_day)
    {
        *distribution.entry(day.to_string()).or_insert(0) += 1;
    }
    distribution
}

#[test]
fn measures_shipped_identity_on_parser_produced_sec_documents() {
    let disposable = DisposableDir::create();
    let exported = parser_produced_documents(&disposable);
    let finance: Vec<_> = exported
        .iter()
        .filter(|document| document.sector.0 == "finance")
        .cloned()
        .collect();
    let news: Vec<_> = exported
        .iter()
        .filter(|document| {
            matches!(
                document.provenance.source_id.as_str(),
                "techwire" | "osdaily"
            )
        })
        .cloned()
        .collect();
    assert_eq!(finance.len(), 201);
    assert_eq!(news.len(), 7);
    assert_eq!(
        finance
            .iter()
            .filter(|document| document.provenance.source_id == SEC_SOURCE_ID)
            .count(),
        200
    );

    let store = SqliteStore::open(&disposable.0.join("identity.db"))
        .expect("open disposable shipped store");
    assert_eq!(
        store.append_new(&finance).expect("append finance corpus"),
        201
    );
    let stored = store
        .load_all_with_fingerprints()
        .expect("load persisted shipped fingerprints");
    assert_eq!(stored.len(), 201);
    assert!(stored.iter().all(|(document, fingerprint)| {
        *fingerprint == simhash(&format!("{} {}", document.title, document.body))
    }));

    let shipped = dedup_near(stored.clone(), 16);
    let mut store_drops = store.duplicates().expect("load store canonical drops");
    let mut extract_drops: Vec<_> = shipped
        .drops
        .iter()
        .map(|drop| (drop.dropped_id.clone(), drop.kept_id.clone()))
        .collect();
    store_drops.sort();
    extract_drops.sort();
    assert_eq!(
        store_drops, extract_drops,
        "append_new's private assign_canonical_ids_tx result must equal dedup_near"
    );

    let titles: BTreeMap<_, _> = stored
        .iter()
        .map(|(document, _)| (document.id.clone(), document.title.clone()))
        .collect();
    let (same_issuer, cross_issuer) = drop_classes(&shipped, &titles);
    assert_eq!((shipped.kept.len(), shipped.drops.len()), (173, 28));
    assert_eq!((same_issuer, cross_issuer), (8, 20));
    println!(
        "identity-shipped-threshold: threshold=16 input={} kept={} dropped={} \
         same_issuer={same_issuer} cross_issuer={cross_issuer}",
        stored.len(),
        shipped.kept.len(),
        shipped.drops.len()
    );
    for drop in &shipped.drops {
        let dropped_cik = cik(&titles[&drop.dropped_id]).expect("dropped CIK");
        let kept_cik = cik(&titles[&drop.kept_id]).expect("kept CIK");
        let class = if dropped_cik == kept_cik {
            "same-issuer"
        } else {
            "cross-issuer"
        };
        println!(
            "identity-drop: dropped={} kept={} distance={} class={class} \
             dropped_cik={dropped_cik} kept_cik={kept_cik}",
            drop.dropped_id, drop.kept_id, drop.distance
        );
    }

    let mut sweep = Vec::new();
    for threshold in [16, 15, 14, 13, 12, 10, 8] {
        let result = dedup_near(stored.clone(), threshold);
        let (same, cross) = drop_classes(&result, &titles);
        sweep.push((
            threshold,
            result.kept.len(),
            result.drops.len(),
            same,
            cross,
        ));
        println!(
            "identity-threshold-sweep: threshold={threshold} kept={} \
             dropped={} same_issuer={same} cross_issuer={cross}",
            result.kept.len(),
            result.drops.len()
        );
    }
    assert_eq!(
        sweep,
        vec![
            (16, 173, 28, 8, 20),
            (15, 187, 14, 6, 8),
            (14, 196, 5, 5, 0),
            (13, 197, 4, 4, 0),
            (12, 197, 4, 4, 0),
            (10, 199, 2, 2, 0),
            (8, 199, 2, 2, 0),
        ]
    );

    let sec_pairs: Vec<_> = stored
        .iter()
        .filter(|(document, _)| document.provenance.source_id == SEC_SOURCE_ID)
        .cloned()
        .collect();
    let news_pairs: Vec<_> = news
        .iter()
        .cloned()
        .map(|document| {
            let fingerprint = simhash(&format!("{} {}", document.title, document.body));
            (document, fingerprint)
        })
        .collect();
    let mut sec_feature_values: Vec<_> = sec_pairs
        .iter()
        .map(|(document, _)| feature_count(document))
        .collect();
    let mut news_feature_values: Vec<_> = news_pairs
        .iter()
        .map(|(document, _)| feature_count(document))
        .collect();
    let sec_features = count_distribution(sec_feature_values.iter().copied());
    let news_features = count_distribution(news_feature_values.iter().copied());
    let sec_feature_median = median(&mut sec_feature_values);
    let news_feature_median = median(&mut news_feature_values);
    let sec_distances = distance_distribution(&sec_pairs);
    let news_distances = distance_distribution(&news_pairs);
    let sec_inside_16: usize = sec_distances.range(..=16).map(|(_, count)| count).sum();
    let news_inside_16: usize = news_distances.range(..=16).map(|(_, count)| count).sum();
    let sec_distinct_fingerprints: BTreeSet<_> = sec_pairs
        .iter()
        .map(|(_, fingerprint)| fingerprint)
        .collect();
    let fixture_fingerprint = stored
        .iter()
        .find(|(document, _)| document.provenance.source_id == "filings-digest")
        .map(|(_, fingerprint)| *fingerprint)
        .expect("finance fixture fingerprint");
    let fixture_minimum_sec_distance = sec_pairs
        .iter()
        .map(|(_, fingerprint)| hamming(fixture_fingerprint, *fingerprint))
        .min()
        .expect("SEC fingerprints");
    assert_eq!(sec_distinct_fingerprints.len(), 198);
    assert_eq!(sec_inside_16, 35);
    assert_eq!(news_inside_16, 1);
    assert_eq!(fixture_minimum_sec_distance, 23);
    assert_eq!((sec_feature_median, news_feature_median), (5, 40));
    assert_eq!(
        sec_features,
        BTreeMap::from([(4, 40), (5, 86), (6, 48), (7, 20), (8, 5), (10, 1)])
    );
    assert_eq!(
        news_features,
        BTreeMap::from([(26, 1), (28, 1), (37, 1), (40, 2), (41, 1), (42, 1)])
    );
    println!(
        "identity-feature-distribution: sec={sec_features:?} \
         sec_median={sec_feature_median} news={news_features:?} \
         news_median={news_feature_median}"
    );
    println!(
        "identity-pairwise-distance-distribution: sec={sec_distances:?} \
         sec_pairs={} sec_inside_16={sec_inside_16} \
         sec_distinct_fingerprints={} news={news_distances:?} \
         news_pairs={} news_inside_16={news_inside_16} \
         filings_digest_minimum_sec_distance={fixture_minimum_sec_distance}",
        sec_pairs.len() * (sec_pairs.len() - 1) / 2,
        sec_distinct_fingerprints.len(),
        news_pairs.len() * (news_pairs.len() - 1) / 2
    );

    let entities = load_entities();
    let mentions = resolve_mentions(&shipped.kept, &entities);
    let resolved_entities: BTreeSet<_> = mentions
        .iter()
        .map(|mention| mention.entity_id.as_str())
        .collect();
    let analysis = shipped_analyze::analyze(
        &shipped.kept,
        &entities,
        &mentions,
        &[],
        &shipped_analyze::AnalyzeParams::default(),
    );
    let rising_scores: Vec<_> = analysis
        .signals
        .iter()
        .filter(|signal| signal.kind == SignalKind::RisingEntity)
        .map(|signal| signal.score)
        .collect();
    let edge_endpoint_bytes: usize = analysis
        .edges
        .iter()
        .map(|edge| edge.a.len() + edge.b.len())
        .sum();
    let minimum_day = shipped
        .kept
        .iter()
        .filter_map(|document| document.published_day)
        .min()
        .expect("minimum kept day");
    let maximum_day = shipped
        .kept
        .iter()
        .filter_map(|document| document.published_day)
        .max()
        .expect("maximum kept day");
    assert_eq!(
        day_distribution(&finance),
        BTreeMap::from([
            ("2026-07-03".to_string(), 1),
            ("2026-07-29".to_string(), 200),
        ])
    );
    assert_eq!(
        day_distribution(&shipped.kept),
        BTreeMap::from([
            ("2026-07-03".to_string(), 1),
            ("2026-07-29".to_string(), 172),
        ])
    );
    assert_eq!(maximum_day.0 - minimum_day.0, 26);
    assert!(mentions.is_empty());
    assert!(resolved_entities.is_empty());
    assert!(rising_scores.is_empty());
    assert!(analysis.signals.is_empty());
    assert!(analysis.edges.is_empty());
    assert_eq!(
        analysis.window_end.map(|day| day.to_string()).as_deref(),
        Some("2026-07-29")
    );
    println!(
        "identity-same-day-analysis: input_days={:?} kept_days={:?} \
         baseline_span_days={} mentions={} resolved_entities={:?} \
         rising_signals={} rising_z_scores={rising_scores:?} \
         total_signals={} edges={} edge_endpoint_bytes={edge_endpoint_bytes} \
         window_end={:?}",
        day_distribution(&finance),
        day_distribution(&shipped.kept),
        maximum_day.0 - minimum_day.0,
        mentions.len(),
        resolved_entities,
        analysis
            .signals
            .iter()
            .filter(|signal| signal.kind == SignalKind::RisingEntity)
            .count(),
        analysis.signals.len(),
        analysis.edges.len(),
        analysis.window_end.map(|day| day.to_string())
    );
}
