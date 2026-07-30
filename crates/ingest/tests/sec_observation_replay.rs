use intel_compliance::{HostLimiters, RobotsGate};
use intel_core::{Day, License, SectorId, SourceKind};
use intel_ingest::rss::RssSource;
use intel_ingest::{MissingPolicy, Source, SourceContext};
use std::collections::{BTreeMap, BTreeSet};
use std::fmt::Write as _;
use std::path::{Path, PathBuf};
use std::sync::Arc;
use std::time::{SystemTime, UNIX_EPOCH};

const OBSERVATION_RECORD: &str = "observations/v0.25/feed-shape/sec-edgar-feed-shape.md";
const OBSERVATION_RELATIVE_PATH: &str =
    "../../observations/v0.25/feed-shape/sec-edgar-usgaap.rss.xml";
const EXPECTED_SHA256: &str = "154556cd81bda4fc2372386bf43aa7b4414335560dd1371c45bae09f1a8d9de3";
const EXPECTED_BYTES: usize = 892_641;
const EDGAR_NAMESPACE: &str = "https://www.sec.gov/Archives/edgar";
const SOURCE_ID: &str = "sec-edgar-usgaap";
const FEED_URL: &str = "https://www.sec.gov/Archives/edgar/usgaap.rss.xml";

struct DisposableDir(PathBuf);

impl DisposableDir {
    fn create() -> Self {
        let nonce = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .expect("system clock must be after the Unix epoch")
            .as_nanos();
        let path = std::env::temp_dir().join(format!(
            "intel-platform-sec-replay-{}-{nonce}",
            std::process::id()
        ));
        std::fs::create_dir(&path).expect("create disposable replay directory");
        Self(path)
    }
}

impl Drop for DisposableDir {
    fn drop(&mut self) {
        std::fs::remove_dir_all(&self.0).expect("remove disposable replay directory");
    }
}

fn observation_path() -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR")).join(OBSERVATION_RELATIVE_PATH)
}

fn sha256_hex(bytes: &[u8]) -> String {
    const K: [u32; 64] = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4,
        0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe,
        0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f,
        0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc,
        0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
        0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116,
        0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7,
        0xc67178f2,
    ];

    let mut state = [
        0x6a09e667u32,
        0xbb67ae85,
        0x3c6ef372,
        0xa54ff53a,
        0x510e527f,
        0x9b05688c,
        0x1f83d9ab,
        0x5be0cd19,
    ];
    let bit_length = (bytes.len() as u64)
        .checked_mul(8)
        .expect("observation length must fit SHA-256");
    let mut padded = bytes.to_vec();
    padded.push(0x80);
    while padded.len() % 64 != 56 {
        padded.push(0);
    }
    padded.extend_from_slice(&bit_length.to_be_bytes());

    for block in padded.chunks_exact(64) {
        let mut schedule = [0u32; 64];
        for (index, word) in block.chunks_exact(4).take(16).enumerate() {
            schedule[index] = u32::from_be_bytes(word.try_into().expect("four-byte word"));
        }
        for index in 16..64 {
            let s0 = schedule[index - 15].rotate_right(7)
                ^ schedule[index - 15].rotate_right(18)
                ^ (schedule[index - 15] >> 3);
            let s1 = schedule[index - 2].rotate_right(17)
                ^ schedule[index - 2].rotate_right(19)
                ^ (schedule[index - 2] >> 10);
            schedule[index] = schedule[index - 16]
                .wrapping_add(s0)
                .wrapping_add(schedule[index - 7])
                .wrapping_add(s1);
        }

        let mut a = state[0];
        let mut b = state[1];
        let mut c = state[2];
        let mut d = state[3];
        let mut e = state[4];
        let mut f = state[5];
        let mut g = state[6];
        let mut h = state[7];

        for index in 0..64 {
            let sum1 = e.rotate_right(6) ^ e.rotate_right(11) ^ e.rotate_right(25);
            let choose = (e & f) ^ ((!e) & g);
            let temp1 = h
                .wrapping_add(sum1)
                .wrapping_add(choose)
                .wrapping_add(K[index])
                .wrapping_add(schedule[index]);
            let sum0 = a.rotate_right(2) ^ a.rotate_right(13) ^ a.rotate_right(22);
            let majority = (a & b) ^ (a & c) ^ (b & c);
            let temp2 = sum0.wrapping_add(majority);

            h = g;
            g = f;
            f = e;
            e = d.wrapping_add(temp1);
            d = c;
            c = b;
            b = a;
            a = temp1.wrapping_add(temp2);
        }

        state[0] = state[0].wrapping_add(a);
        state[1] = state[1].wrapping_add(b);
        state[2] = state[2].wrapping_add(c);
        state[3] = state[3].wrapping_add(d);
        state[4] = state[4].wrapping_add(e);
        state[5] = state[5].wrapping_add(f);
        state[6] = state[6].wrapping_add(g);
        state[7] = state[7].wrapping_add(h);
    }

    let mut digest = String::with_capacity(64);
    for word in state {
        write!(&mut digest, "{word:08x}").expect("write SHA-256 hex");
    }
    digest
}

fn assert_observation_bytes(bytes: &[u8]) -> Result<(), String> {
    if bytes.len() != EXPECTED_BYTES {
        return Err(format!(
            "byte-length mismatch for {OBSERVATION_RECORD}: expected \
             {EXPECTED_BYTES}, observed {}",
            bytes.len()
        ));
    }
    let observed_sha256 = sha256_hex(bytes);
    if observed_sha256 != EXPECTED_SHA256 {
        return Err(format!(
            "SHA-256 mismatch for {OBSERVATION_RECORD}: expected \
             {EXPECTED_SHA256}, observed {observed_sha256}"
        ));
    }
    Ok(())
}

fn direct_text(item: roxmltree::Node<'_, '_>, name: &str) -> Option<String> {
    item.children()
        .find(|node| node.is_element() && node.tag_name().name() == name)
        .and_then(|node| node.text())
        .map(ToOwned::to_owned)
}

fn utc_day(raw: &str, local_day: Day) -> Option<Day> {
    let parts: Vec<&str> = raw.split_whitespace().collect();
    let time_index = parts.iter().position(|part| part.contains(':'))?;
    let time: Vec<i64> = parts[time_index]
        .split(':')
        .map(str::parse)
        .collect::<Result<_, _>>()
        .ok()?;
    if time.len() != 3 {
        return None;
    }
    let offset_minutes = match *parts.get(time_index + 1)? {
        "EDT" => -4 * 60,
        "EST" => -5 * 60,
        "GMT" | "UTC" => 0,
        _ => return None,
    };
    let local_minutes = time[0] * 60 + time[1];
    let utc_minutes = local_minutes - offset_minutes;
    Some(Day(local_day.0 + utc_minutes.div_euclid(24 * 60)))
}

fn quartile(sorted: &[usize], numerator: usize, denominator: usize) -> usize {
    let index = (sorted.len() - 1) * numerator / denominator;
    sorted[index]
}

#[tokio::test]
async fn replays_sec_observation_through_shipped_rss_parser() {
    let observation_path = observation_path();
    let bytes = std::fs::read(&observation_path).expect("read SEC observation");

    assert_observation_bytes(&bytes).unwrap_or_else(|error| panic!("{error}"));
    println!(
        "replay-byte-assertion: path={} bytes={} sha256={} record={OBSERVATION_RECORD}",
        observation_path.display(),
        bytes.len(),
        sha256_hex(&bytes)
    );

    let disposable = DisposableDir::create();
    let mut mutated = bytes.clone();
    let last = mutated
        .last_mut()
        .expect("the observation body must not be empty");
    *last ^= 1;
    let mutated_path = disposable.0.join("one-byte-mutated.xml");
    std::fs::write(&mutated_path, &mutated).expect("write disposable one-byte mutation");
    let rejection =
        assert_observation_bytes(&std::fs::read(&mutated_path).expect("read disposable mutation"))
            .expect_err("the point-of-use assertion must reject a one-byte mutation");
    assert!(rejection.contains("SHA-256 mismatch"));
    println!(
        "replay-byte-control-rejection: path={} rejection={rejection}",
        mutated_path.display()
    );

    let source = RssSource {
        id: SOURCE_ID.to_string(),
        sector: SectorId::new("finance"),
        feed_url: FEED_URL.to_string(),
        fixture_path: Some(observation_path.display().to_string()),
        license: License::PublisherPermitted,
        robots_on_missing: MissingPolicy::Deny,
    };
    let context = SourceContext {
        robots: RobotsGate::new(&[]),
        limiter: Arc::new(HostLimiters::per_second(1_000.0)),
        cursors: None,
        robots_cache: None,
    };
    let documents = source
        .fetch(&context)
        .await
        .expect("shipped RSS parser must accept the asserted observation");

    let xml = std::str::from_utf8(&bytes).expect("the asserted SEC observation must be UTF-8");
    let tree = roxmltree::Document::parse(xml).expect("inventory asserted observation");
    let items: Vec<_> = tree
        .descendants()
        .filter(|node| node.tag_name().name() == "item")
        .collect();
    assert_eq!(documents.len(), items.len());

    let mut extension_counts: BTreeMap<String, (usize, usize)> = BTreeMap::new();
    for (document, item) in documents.iter().zip(&items) {
        let title = direct_text(*item, "title").unwrap_or_default();
        let guid = direct_text(*item, "guid").unwrap_or_else(|| title.clone());
        let published_raw = direct_text(*item, "pubDate");
        assert_eq!(document.id, format!("{SOURCE_ID}::{guid}"));
        assert_eq!(document.sector, SectorId::new("finance"));
        assert_eq!(document.url, direct_text(*item, "link"));
        assert_eq!(document.title, title);
        assert_eq!(
            document.body,
            direct_text(*item, "description").unwrap_or_default()
        );
        assert_eq!(
            document.published_day,
            published_raw.as_deref().and_then(Day::parse_rfc822ish)
        );
        assert_eq!(document.published_raw, published_raw);
        assert_eq!(
            document.authors,
            direct_text(*item, "author").into_iter().collect::<Vec<_>>()
        );
        assert!(document.tags.is_empty());
        assert_eq!(document.provenance.source_id, SOURCE_ID);
        assert_eq!(document.provenance.retrieved_from, FEED_URL);
        assert_eq!(document.provenance.kind, SourceKind::Rss);
        assert_eq!(document.provenance.license, License::PublisherPermitted);

        let mut names_in_item = BTreeSet::new();
        for element in item.descendants().filter(|node| {
            node.is_element() && node.tag_name().namespace() == Some(EDGAR_NAMESPACE)
        }) {
            let name = element.tag_name().name().to_string();
            extension_counts.entry(name.clone()).or_default().1 += 1;
            names_in_item.insert(name);
        }
        for name in names_in_item {
            extension_counts.entry(name).or_default().0 += 1;
        }
    }

    let distinct_ids: BTreeSet<_> = documents.iter().map(|document| &document.id).collect();
    let id_max_bytes = documents
        .iter()
        .map(|document| document.id.len())
        .max()
        .expect("at least one document");
    let title_lengths: Vec<_> = documents
        .iter()
        .map(|document| document.title.chars().count())
        .collect();
    let title_min = *title_lengths.iter().min().expect("at least one title");
    let title_max = *title_lengths.iter().max().expect("at least one title");

    let mut body_lengths: Vec<_> = documents
        .iter()
        .map(|document| document.body.chars().count())
        .collect();
    body_lengths.sort_unstable();
    let mut body_length_counts = BTreeMap::new();
    for length in &body_lengths {
        *body_length_counts.entry(*length).or_insert(0usize) += 1;
    }
    let body_mean = body_lengths.iter().sum::<usize>() as f64 / body_lengths.len() as f64;

    let mut published_days = BTreeMap::new();
    for day in documents
        .iter()
        .filter_map(|document| document.published_day)
    {
        *published_days.entry(day.to_string()).or_insert(0usize) += 1;
    }
    let published_raw_present = documents
        .iter()
        .filter(|document| document.published_raw.is_some())
        .count();
    let distinct_published_raw: BTreeSet<_> = documents
        .iter()
        .filter_map(|document| document.published_raw.as_ref())
        .collect();
    let utc_day_differences = documents
        .iter()
        .filter(|document| {
            let (Some(raw), Some(local_day)) = (&document.published_raw, document.published_day)
            else {
                return false;
            };
            utc_day(raw, local_day).is_some_and(|day| day != local_day)
        })
        .count();
    let mut zones = BTreeMap::new();
    for raw in documents
        .iter()
        .filter_map(|document| document.published_raw.as_ref())
    {
        if let Some(zone) = raw.split_whitespace().last() {
            *zones.entry(zone.to_string()).or_insert(0usize) += 1;
        }
    }

    let documents_with_authors = documents
        .iter()
        .filter(|document| !document.authors.is_empty())
        .count();
    let author_values = documents
        .iter()
        .map(|document| document.authors.len())
        .sum::<usize>();
    let distinct_authors: BTreeSet<_> = documents
        .iter()
        .flat_map(|document| &document.authors)
        .collect();
    let urls_present = documents
        .iter()
        .filter(|document| document.url.is_some())
        .count();
    let distinct_urls: BTreeSet<_> = documents
        .iter()
        .filter_map(|document| document.url.as_ref())
        .collect();

    assert_eq!(documents.len(), 200);
    assert_eq!(distinct_ids.len(), 200);
    assert_eq!(id_max_bytes, 114);
    assert_eq!((title_min, title_max), (30, 80));
    assert_eq!(
        body_length_counts,
        BTreeMap::from([(3, 108), (4, 64), (5, 5), (6, 4), (7, 19)])
    );
    assert!((body_mean - 3.81).abs() < f64::EPSILON);
    assert_eq!(
        published_days,
        BTreeMap::from([("2026-07-29".to_string(), 200)])
    );
    assert_eq!(published_raw_present, 200);
    assert_eq!(distinct_published_raw.len(), 191);
    assert_eq!(published_days.values().sum::<usize>(), 200);
    assert_eq!(zones, BTreeMap::from([("EDT".to_string(), 200)]));
    assert_eq!(utc_day_differences, 0);
    assert_eq!(
        (
            documents_with_authors,
            author_values,
            distinct_authors.len()
        ),
        (0, 0, 0)
    );
    assert_eq!((urls_present, distinct_urls.len()), (200, 200));
    assert_eq!(
        extension_counts,
        BTreeMap::from([
            ("acceptanceDatetime".to_string(), (200, 200)),
            ("accessionNumber".to_string(), (200, 200)),
            ("assignedSic".to_string(), (170, 170)),
            ("assistantDirector".to_string(), (170, 170)),
            ("cikNumber".to_string(), (200, 200)),
            ("companyName".to_string(), (200, 200)),
            ("fileNumber".to_string(), (200, 200)),
            ("filingDate".to_string(), (200, 200)),
            ("fiscalYearEnd".to_string(), (194, 194)),
            ("formType".to_string(), (200, 200)),
            ("otherCikNumbers".to_string(), (7, 7)),
            ("period".to_string(), (200, 200)),
            ("xbrlFile".to_string(), (200, 2_339)),
            ("xbrlFiles".to_string(), (200, 200)),
            ("xbrlFiling".to_string(), (200, 200)),
        ])
    );
    assert!(documents.iter().all(|document| {
        document.provenance.kind == SourceKind::Rss
            && document.provenance.license == License::PublisherPermitted
    }));

    println!(
        "replay-field-inventory: items={} distinct_ids={} \
         id_construction={SOURCE_ID}::<guid> id_max_bytes={id_max_bytes} \
         title_chars_min={title_min} title_chars_max={title_max} \
         published_raw_present={published_raw_present} \
         published_raw_distinct={} documents_with_authors={} \
         author_values={author_values} distinct_authors={} \
         urls_present={urls_present} distinct_urls={} \
         license=PublisherPermitted source_kind=Rss",
        documents.len(),
        distinct_ids.len(),
        distinct_published_raw.len(),
        documents_with_authors,
        distinct_authors.len(),
        distinct_urls.len()
    );
    println!(
        "replay-body-length-distribution-chars: exact={body_length_counts:?} \
         min={} p25={} median={} p75={} max={} mean={body_mean:.3}",
        body_lengths[0],
        quartile(&body_lengths, 1, 4),
        quartile(&body_lengths, 1, 2),
        quartile(&body_lengths, 3, 4),
        body_lengths[body_lengths.len() - 1]
    );
    println!(
        "replay-published-day: local_distribution={published_days:?} \
         zones={zones:?} utc_day_differences={utc_day_differences} \
         semantics=Day::parse_rfc822ish slides a three-token window and \
         ignores the zone; EDT therefore records the publisher-local day"
    );
    println!(
        "replay-discarded-edgar-elements: \
         item_population_and_total_elements={extension_counts:?}; \
         none reaches a Document field"
    );
    println!(
        "replay-establishment-boundary: asserted real publisher bytes through \
         shipped code establish parser behavior for this response; they do \
         not establish paging, cursor durability, repeated fetches, wire \
         politeness, redirects, conditional requests, or the next response"
    );
}
