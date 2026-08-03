#[path = "../../analyze/src/lib.rs"]
mod shipped_analyze;

use intel_core::{
    Day, Document, Entity, EntityKind, License, Mention, Provenance, SectorId, SignalKind,
    SourceKind,
};
use intel_extract::{
    dedup_eligible, dedup_near, hamming, simhash, simhash_feature_count, DEDUP_MIN_FEATURES,
};
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
        Self::create_with_nonce(nonce)
    }

    fn candidate_path(nonce: u128, attempt: u64) -> PathBuf {
        std::env::temp_dir().join(format!(
            "intel-platform-sec-identity-{}-{nonce}-{attempt}",
            std::process::id()
        ))
    }

    fn create_with_nonce(nonce: u128) -> Self {
        let mut attempt = 0_u64;
        loop {
            let path = Self::candidate_path(nonce, attempt);
            match std::fs::create_dir(&path) {
                Ok(()) => return Self(path),
                Err(error) if error.kind() == std::io::ErrorKind::AlreadyExists => {
                    attempt = attempt
                        .checked_add(1)
                        .expect("exhausted identity-measure directory candidates");
                }
                Err(error) => panic!("create identity-measure directory {path:?}: {error}"),
            }
        }
    }
}

impl Drop for DisposableDir {
    fn drop(&mut self) {
        std::fs::remove_dir_all(&self.0).expect("remove identity-measure directory");
    }
}

#[test]
fn retries_disposable_directory_collision_deterministically() {
    let nonce = u128::MAX;
    let occupied = DisposableDir::candidate_path(nonce, 0);
    std::fs::create_dir(&occupied).expect("pre-create forced-collision directory");

    let created = DisposableDir::create_with_nonce(nonce);
    assert_eq!(
        created.0,
        DisposableDir::candidate_path(nonce, 1),
        "creation must advance past the occupied candidate"
    );
    assert!(created.0.is_dir(), "the retry must create its candidate");

    drop(created);
    std::fs::remove_dir(&occupied).expect("remove forced-collision directory");
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
    simhash_feature_count(&format!("{} {}", document.title, document.body))
}

fn cross_sector_document(id: &str, sector: &str, day: &str, body: &str) -> Document {
    Document {
        id: id.to_string(),
        sector: SectorId(sector.to_string()),
        url: None,
        title: "Identical cross-sector identity witness".to_string(),
        body: body.to_string(),
        published_day: Day::parse_iso(day),
        published_raw: Some(day.to_string()),
        authors: Vec::new(),
        tags: Vec::new(),
        provenance: Provenance {
            source_id: format!("{sector}-fixture"),
            retrieved_from: "fixture".to_string(),
            kind: SourceKind::Rss,
            license: License::CcBy,
        },
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
fn measures_nonempty_cross_sector_store_view_identity_equivalence() {
    let disposable = DisposableDir::create();
    let body = (0..40)
        .map(|index| format!("identityfeature{index}"))
        .collect::<Vec<_>>()
        .join(" ");
    let science = cross_sector_document(
        "science::cross-sector-witness",
        "science",
        "2026-07-01",
        &body,
    );
    let technology = cross_sector_document(
        "technology::cross-sector-witness",
        "technology",
        "2026-07-02",
        &body,
    );
    let science_duplicate = cross_sector_document(
        "science::cross-sector-duplicate",
        "science",
        "2026-07-03",
        &body,
    );
    assert!(feature_count(&science) >= DEDUP_MIN_FEATURES);
    assert_eq!(feature_count(&science), feature_count(&technology));

    let store = SqliteStore::open(&disposable.0.join("cross-sector.db"))
        .expect("open disposable cross-sector store");
    assert_eq!(
        store
            .append_new(&[
                science.clone(),
                technology.clone(),
                science_duplicate.clone(),
            ])
            .expect("append cross-sector witness"),
        3
    );
    let store_ids = vec![
        (
            science.id.clone(),
            store
                .canonical_id(&science.id)
                .expect("science canonical id")
                .expect("science canonical id present"),
        ),
        (
            technology.id.clone(),
            store
                .canonical_id(&technology.id)
                .expect("technology canonical id")
                .expect("technology canonical id present"),
        ),
        (
            science_duplicate.id.clone(),
            store
                .canonical_id(&science_duplicate.id)
                .expect("science duplicate canonical id")
                .expect("science duplicate canonical id present"),
        ),
    ];
    let view = dedup_near(
        store
            .load_all_with_fingerprints()
            .expect("load persisted cross-sector fingerprints"),
        16,
    );
    let view_drops: Vec<_> = view
        .drops
        .iter()
        .map(|drop| (drop.dropped_id.clone(), drop.kept_id.clone(), drop.distance))
        .collect();
    println!(
        "cross-sector-identity-witness: features={} store={store_ids:?} \
         view_kept={} view_drops={view_drops:?}",
        feature_count(&science),
        view.kept.len()
    );
    assert_eq!(
        store_ids,
        vec![
            (science.id.clone(), science.id.clone()),
            (technology.id.clone(), technology.id.clone()),
            (science_duplicate.id.clone(), science.id.clone()),
        ]
    );
    let mut store_drops = store.duplicates().expect("load witness canonical drops");
    let mut view_drop_ids: Vec<_> = view
        .drops
        .iter()
        .map(|drop| (drop.dropped_id.clone(), drop.kept_id.clone()))
        .collect();
    store_drops.sort();
    view_drop_ids.sort();
    assert!(
        !store_drops.is_empty(),
        "the identity witness must be nonempty"
    );
    assert_eq!(
        store_drops, view_drop_ids,
        "store and view must apply one sector-partitioned identity rule"
    );
    assert_eq!(view_drops, vec![(science_duplicate.id, science.id, 0)]);
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
    assert!(finance
        .iter()
        .filter(|document| document.provenance.source_id == SEC_SOURCE_ID)
        .all(|document| document.provenance.license == License::PublisherPermitted));
    assert!(License::PublisherPermitted.redistributable());

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

    let finance_sectors = ["finance".to_string()];
    let broadstone_hits = store
        .search("Broadstone", &finance_sectors, 10)
        .expect("search captured SEC corpus");
    let broadstone = broadstone_hits
        .iter()
        .find(|hit| hit.source_id == SEC_SOURCE_ID)
        .expect("captured SEC result must pass the finance sector filter");
    assert_eq!(broadstone.license, License::PublisherPermitted);
    assert!(
        broadstone.snippet.is_some(),
        "PublisherPermitted captured text must pass the core search licence gate"
    );
    assert!(store
        .search("Broadstone", &["science".to_string()], 10)
        .expect("search disjoint sector")
        .is_empty());
    println!(
        "captured-sec-license-gate: query=Broadstone source={} license={} \
         snippet={} finance_hits={} disjoint_hits=0",
        broadstone.source_id,
        broadstone.license.as_str(),
        broadstone.snippet.is_some(),
        broadstone_hits.len()
    );

    let shipped = dedup_near(stored.clone(), 16);
    let mut store_drops = store.duplicates().expect("load store canonical drops");
    let mut extract_drops: Vec<_> = shipped
        .drops
        .iter()
        .map(|drop| (drop.dropped_id.clone(), drop.kept_id.clone()))
        .collect();
    store_drops.sort();
    extract_drops.sort();
    println!("identity-equivalence-vectors: store={store_drops:?} extract={extract_drops:?}");
    assert_eq!((shipped.kept.len(), shipped.drops.len()), (201, 0));
    assert!(store_drops.is_empty());
    assert!(extract_drops.is_empty());
    println!(
        "identity-guarded-threshold: threshold=16 feature_floor={} input={} \
         kept={} dropped={} cross_issuer=0",
        DEDUP_MIN_FEATURES,
        stored.len(),
        shipped.kept.len(),
        shipped.drops.len()
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
    assert!(
        sec_feature_values
            .iter()
            .all(|features| *features < DEDUP_MIN_FEATURES),
        "every measured SEC document must stay below the calibrated floor"
    );
    assert!(
        news_feature_values
            .iter()
            .all(|features| *features >= DEDUP_MIN_FEATURES),
        "every measured news document must remain eligible"
    );
    assert!(!dedup_eligible(10, DEDUP_MIN_FEATURES));
    assert!(dedup_eligible(DEDUP_MIN_FEATURES, DEDUP_MIN_FEATURES));
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
            ("2026-07-29".to_string(), 200),
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
