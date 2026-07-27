//! cored: the Rust core daemon — the stable, performance-critical engine
//! behind a minimal internal JSON API.
//!
//! The core-shell contract, stated once and enforced here:
//!
//! - **The core never knows clients exist.** No API keys, no subscriptions,
//!   no billing. Every endpoint takes an explicit `sectors` list; the shell
//!   decides which sectors a caller is entitled to. Sector filtering is
//!   still enforced in core SQL/memory, so a buggy shell can at worst grant
//!   the wrong sectors — never bypass the filter mechanism itself.
//!
//! - **The core never talks to an LLM.** The shell embeds queries and
//!   documents (that is provider/prompt business) and posts vectors back;
//!   the core stores them and does the math: BM25, cosine, RRF, SimHash,
//!   z-scores, PMI.
//!
//! - **License enforcement that must be impossible to forget stays here.**
//!   Search snippets and view-evidence excerpts are gated in the core
//!   (store + hydration below), so no amount of shell iteration can
//!   accidentally leak IndexOnly text to subscribers. Full bodies ARE
//!   served on the internal /retrieve and /docs endpoints: passing gated
//!   text to a model as context is analysis, which is the position the
//!   original design took; the shell's prompt discourages verbatim
//!   reproduction, and `/attest` structurally inspects the model answer before
//!   the shell returns it on a public path. This is an internal seam, not a
//!   public API.
//!
//! Binding is structurally restricted to loopback: every address resolved from
//! CORE_BIND is checked before a socket is opened, and startup refuses any
//! non-loopback address. Optional defense-in-depth: set CORE_TOKEN and the shell
//! sends `x-core-token` on every request.
//!
//! Env: CORE_CONFIG (config/core.json), CORE_ENTITIES (config/entities.json),
//!      CORE_DB (data/intel.db), CORE_BIND (127.0.0.1:8788), CORE_TOKEN.

use axum::body::Body;
use axum::extract::{Query, State};
use axum::http::{HeaderMap, HeaderValue, StatusCode};
use axum::response::{IntoResponse, Response};
use axum::routing::{get, post};
use axum::{Json, Router};
use intel_compliance::{HostLimiters, RobotsCache, RobotsGate};
use intel_core::{attest_answer, Attestation, Day, Document, Signal};
use intel_enrich::Gazetteer;
use intel_extract::hamming;
use intel_ingest::{CursorStore, SourceContext};
use intel_registry::{select_sources, CoreConfig};
use intel_store::{SqliteStore, StoreOpenTimings};
use intel_view::{compute_view, entity_names, ViewParams};
use serde::{Deserialize, Serialize};
use std::collections::{HashMap, HashSet, VecDeque};
use std::net::{SocketAddr, ToSocketAddrs};
use std::path::Path;
use std::sync::atomic::{AtomicU64, AtomicUsize, Ordering};
use std::sync::{Arc, Mutex};
use std::time::{Duration, Instant};

struct AppState {
    store: SqliteStore,
    gaz: Gazetteer,
    cfg: CoreConfig,
    token: Option<String>,
    /// Bumped whenever the archive changes. A cached view is valid only for the
    /// generation it was computed in, which makes invalidation a comparison
    /// rather than a bookkeeping exercise — there is no way to forget to evict.
    generation: AtomicU64,
    /// Memoized `/view` responses, keyed by the sector set. `/view` re-runs the
    /// whole pipeline (dedup, gazetteer scan, bursts, PMI) over the entire
    /// corpus, so recomputing it per request was pure waste: between ingests the
    /// answer cannot change. (T9.2)
    view_cache: Mutex<ViewCache>,
    /// Counts actual recomputations — lets a test prove the cache is doing
    /// something rather than merely returning equal values.
    view_computes: AtomicUsize,
    /// Startup diagnostics are immutable facts from this process. They are
    /// exposed only as internal `/view` headers for V2 decomposition.
    store_open_timings: StoreOpenTimings,
    process_main_to_listener_ready_us: AtomicU64,
    /// Politeness clocks, per publisher — **process-scoped, not request-scoped**.
    ///
    /// These used to be built fresh inside the `/ingest` handler, which meant
    /// two ingests a second apart each started with a clean slate and neither
    /// waited for the other. A politeness promise that resets every time we
    /// decide to make a request is not a politeness promise.
    limiter: Arc<HostLimiters>,
    /// Fetched `robots.txt` policy, per origin (T2). `None` on a build without
    /// `--features net`: nothing can be fetched, so there is nothing to ask
    /// permission for, and the configured `RobotsGate` governs alone.
    ///
    /// This has to live here rather than in the handler for the same reason as
    /// the limiter, only more so: a per-request cache would re-fetch every
    /// publisher's `robots.txt` on every single ingest. That is *more* traffic
    /// to them than we send today, so a "compliance" feature would have made us
    /// a worse citizen. The TTL only means something if the cache outlives the
    /// request.
    robots_cache: Option<Arc<RobotsCache>>,
}

struct CachedView {
    generation: u64,
    resp: ViewResp,
}

/// `/view` results can hold evidence and graph data for an entire sector set.
/// Keep the process-scoped memo bounded just as the robots cache is bounded:
/// callers must not be able to turn distinct query strings into permanent
/// process memory. Eviction is oldest insertion first.
const VIEW_CACHE_CAPACITY: usize = 256;

#[derive(Default)]
struct ViewCache {
    entries: HashMap<String, CachedView>,
    oldest: VecDeque<String>,
}

impl ViewCache {
    fn get(&self, key: &str) -> Option<&CachedView> {
        self.entries.get(key)
    }

    fn insert(&mut self, key: String, value: CachedView) {
        if self.entries.remove(&key).is_some() {
            self.oldest.retain(|existing| existing != &key);
        }
        while self.entries.len() >= VIEW_CACHE_CAPACITY {
            let Some(oldest) = self.oldest.pop_front() else {
                break;
            };
            self.entries.remove(&oldest);
        }
        self.oldest.push_back(key.clone());
        self.entries.insert(key, value);
    }

    #[cfg(test)]
    fn len(&self) -> usize {
        self.entries.len()
    }
}

/// Our default politeness floor: 2 requests/second to any one publisher. A
/// publisher's own `Crawl-delay` can slow this down but never speed it up.
const DEFAULT_RPS: f64 = 2.0;

/// Builds the live `robots.txt` cache. Only exists on a `net` build, because
/// only a `net` build can fetch anything.
#[cfg(feature = "net")]
const CRAWLER_CONTACT_ENV: &str = "INTEL_CRAWLER_CONTACT";

#[cfg(feature = "net")]
fn required_crawler_contact(contact: Option<&str>) -> Result<&str, String> {
    let contact = contact
        .map(str::trim)
        .filter(|value| !value.is_empty())
        .ok_or_else(|| format!("{CRAWLER_CONTACT_ENV} is required for a net-enabled harvester"))?;
    let lowercase = contact.to_ascii_lowercase();
    if ["example.com", "you@", "changeme"]
        .iter()
        .any(|placeholder| lowercase.contains(placeholder))
    {
        return Err(format!(
            "{CRAWLER_CONTACT_ENV} must name a real operator contact, not placeholder {contact:?}"
        ));
    }
    Ok(contact)
}

#[cfg(feature = "net")]
fn build_robots_cache_for_contact(
    limiter: Arc<HostLimiters>,
    contact: Option<&str>,
) -> Result<(Arc<RobotsCache>, String), String> {
    use intel_ingest::net::{
        crawler_user_agent, install_crawler_user_agent, HttpRobotsFetcher, ROBOTS_CAPACITY,
        ROBOTS_TTL,
    };

    let contact = required_crawler_contact(contact)?;
    let user_agent = crawler_user_agent(env!("CARGO_PKG_VERSION"), contact);
    let installed = install_crawler_user_agent(env!("CARGO_PKG_VERSION"), contact)
        .map_err(|error| format!("could not configure crawler identity: {error}"))?;
    let fetcher = HttpRobotsFetcher::new()
        .map_err(|error| format!("could not build the robots.txt HTTP client: {error}"))?;
    let cache = Arc::new(RobotsCache::new(
        Arc::new(fetcher),
        limiter,
        installed,
        ROBOTS_TTL,
        ROBOTS_CAPACITY,
    ));
    Ok((cache, user_agent))
}

#[cfg(feature = "net")]
fn build_robots_cache(limiter: Arc<HostLimiters>) -> Option<Arc<RobotsCache>> {
    let contact = std::env::var(CRAWLER_CONTACT_ENV).ok();
    // Missing identity or a client-construction failure would start a
    // network-enabled harvester without a truthful publisher-facing identity
    // or without its robots gate. Both are fail-open on the reason this
    // function exists, so startup refuses instead.
    let (cache, _) = build_robots_cache_for_contact(limiter, contact.as_deref())
        .unwrap_or_else(|error| panic!("cored refused to start: {error}"));
    Some(cache)
}

/// Offline build: nothing is fetched, so no publisher is asked.
#[cfg(not(feature = "net"))]
fn build_robots_cache(_limiter: Arc<HostLimiters>) -> Option<Arc<RobotsCache>> {
    None
}

impl AppState {
    #[cfg(test)]
    fn new(store: SqliteStore, gaz: Gazetteer, cfg: CoreConfig, token: Option<String>) -> Self {
        Self::new_with_startup(store, gaz, cfg, token, StoreOpenTimings::default())
    }

    fn new_with_startup(
        store: SqliteStore,
        gaz: Gazetteer,
        cfg: CoreConfig,
        token: Option<String>,
        store_open_timings: StoreOpenTimings,
    ) -> Self {
        let limiter = Arc::new(HostLimiters::per_second(DEFAULT_RPS));
        Self {
            store,
            gaz,
            cfg,
            token,
            generation: AtomicU64::new(0),
            view_cache: Mutex::new(ViewCache::default()),
            view_computes: AtomicUsize::new(0),
            store_open_timings,
            process_main_to_listener_ready_us: AtomicU64::new(0),
            robots_cache: build_robots_cache(limiter.clone()),
            limiter,
        }
    }

    /// The archive changed: every cached view is now stale.
    fn bump_generation(&self) {
        self.generation.fetch_add(1, Ordering::SeqCst);
    }
}

type ApiErr = (StatusCode, String);

/// Bridges the ingest crate's paged-harvest seam to the core store. Page
/// documents, the next resumptionToken, and pending high-water are committed in
/// one SQLite transaction; a failure aborts the source instead of advancing a
/// cursor past data that never landed.
struct CursorAdapter {
    state: Arc<AppState>,
    committed_docs: Mutex<HashMap<String, usize>>,
    new_docs: AtomicUsize,
}

impl CursorAdapter {
    fn new(state: Arc<AppState>) -> Self {
        Self {
            state,
            committed_docs: Mutex::new(HashMap::new()),
            new_docs: AtomicUsize::new(0),
        }
    }

    fn committed_for(&self, source_id: &str) -> usize {
        self.committed_docs
            .lock()
            .unwrap()
            .get(source_id)
            .copied()
            .unwrap_or(0)
    }

    fn new_count(&self) -> usize {
        self.new_docs.load(Ordering::SeqCst)
    }
}

impl CursorStore for CursorAdapter {
    fn resume_token(&self, source_id: &str) -> Option<String> {
        self.state
            .store
            .get_cursor(source_id)
            .ok()
            .flatten()
            .and_then(|c| c.cursor)
    }
    fn high_water(&self, source_id: &str) -> Option<String> {
        self.state
            .store
            .get_cursor(source_id)
            .ok()
            .flatten()
            .and_then(|c| c.high_water)
    }
    fn commit_page(
        &self,
        source_id: &str,
        docs: &[Document],
        next_token: Option<&str>,
        page_high_water: Option<&str>,
    ) -> Result<usize, String> {
        let new = self
            .state
            .store
            .commit_harvest_page(source_id, docs, next_token, page_high_water)
            .map_err(|error| error.to_string())?;
        *self
            .committed_docs
            .lock()
            .unwrap()
            .entry(source_id.to_string())
            .or_default() += docs.len();
        self.new_docs.fetch_add(new, Ordering::SeqCst);
        if new > 0 {
            self.state.bump_generation();
        }
        Ok(new)
    }
}

fn internal<E: std::fmt::Display>(e: E) -> ApiErr {
    (StatusCode::INTERNAL_SERVER_ERROR, e.to_string())
}

/// Optional shared-secret check. This is belt-and-braces for an interface
/// that already binds to loopback; real auth (who is the caller, what may
/// they see) is the SHELL's job.
fn guard(state: &AppState, headers: &HeaderMap) -> Result<(), ApiErr> {
    match &state.token {
        None => Ok(()),
        Some(t) => {
            let sent = headers.get("x-core-token").and_then(|v| v.to_str().ok());
            if sent == Some(t.as_str()) {
                Ok(())
            } else {
                Err((
                    StatusCode::UNAUTHORIZED,
                    "missing or bad x-core-token".into(),
                ))
            }
        }
    }
}

fn parse_csv(raw: &str) -> Vec<String> {
    raw.split(',')
        .map(|s| s.trim().to_string())
        .filter(|s| !s.is_empty())
        .collect()
}

fn configured_view_sectors(state: &AppState, raw: &str) -> Vec<String> {
    let configured: HashSet<&str> = state
        .cfg
        .sectors
        .iter()
        .map(|sector| sector.id.as_str())
        .collect();
    let mut sectors: Vec<String> = parse_csv(raw)
        .into_iter()
        .filter(|sector| configured.contains(sector.as_str()))
        .collect();
    sectors.sort();
    sectors.dedup();
    sectors
}

fn sector_corpus(state: &AppState, sectors: &[String]) -> Result<Vec<(Document, u64)>, ApiErr> {
    state.store.documents_in_sectors(sectors).map_err(internal)
}

/// One-line excerpt, whitespace-normalized, hard-capped. (Moved here from
/// the old brief renderer: the CAP and the GATE are core concerns; the copy
/// around them is shell business.)
fn snippet(t: &str, n: usize) -> String {
    let one: String = t.split_whitespace().collect::<Vec<_>>().join(" ");
    if one.chars().count() <= n {
        one
    } else {
        let cut: String = one.chars().take(n).collect();
        format!("{cut}...")
    }
}

fn doc_dto(d: &Document) -> DocDto {
    DocDto {
        doc_id: d.id.clone(),
        sector: d.sector.0.clone(),
        title: d.title.clone(),
        body: d.body.clone(),
        url: d.url.clone(),
        source_id: d.provenance.source_id.clone(),
        day: d.published_day.map(|x| x.to_string()),
        license: d.provenance.license.as_str().to_string(),
        authors: d.authors.clone(),
        tags: d.tags.clone(),
    }
}

fn persisted_fingerprint(
    fingerprints: &HashMap<String, u64>,
    document_id: &str,
) -> Result<u64, ApiErr> {
    fingerprints.get(document_id).copied().ok_or_else(|| {
        (
            StatusCode::INTERNAL_SERVER_ERROR,
            format!(
                "persisted simhash is missing for document '{document_id}'; \
                 run ./run verify-fingerprints <database>"
            ),
        )
    })
}

// --- DTOs -------------------------------------------------------------------

#[derive(Serialize)]
struct HealthResp {
    status: &'static str,
    documents: usize,
    version: &'static str,
}

#[derive(Serialize)]
struct SourceInfo {
    id: String,
    r#type: String,
    license: String,
}

#[derive(Serialize)]
struct SectorInfo {
    id: String,
    display_name: String,
    sources: Vec<SourceInfo>,
}

#[derive(Deserialize)]
struct IngestReq {
    sectors: Vec<String>,
    /// Optional per-source filter. When present, run exactly these source ids
    /// (each still validated against the `sectors` entitlement above); when
    /// absent, run every source in the requested sectors — byte-identical to
    /// the original sector-only behavior.
    #[serde(default)]
    sources: Option<Vec<String>>,
}

#[derive(Serialize)]
struct IngestSourceResult {
    sector: String,
    source_id: String,
    ok: bool,
    documents: usize,
    error: Option<String>,
}

#[derive(Serialize)]
struct IngestResp {
    fetched: usize,
    new: usize,
    results: Vec<IngestSourceResult>,
}

#[derive(Deserialize)]
struct SectorsQ {
    sectors: String,
}

#[derive(Serialize, Clone)]
struct EvidenceDto {
    doc_id: String,
    title: String,
    url: Option<String>,
    source_id: String,
    day: Option<String>,
    license: String,
    /// null when the source license forbids redistribution — the gate lives
    /// HERE so the shell renderer cannot leak what it never receives.
    excerpt: Option<String>,
}

#[derive(Serialize, Clone)]
struct SignalDto {
    kind: String,
    headline: String,
    score: f64,
    detail: String,
    entity_ids: Vec<String>,
    evidence: Vec<EvidenceDto>,
}

#[derive(Serialize, Clone)]
struct EdgeDto {
    a: String,
    b: String,
    a_name: String,
    b_name: String,
    weight: usize,
    pmi: f64,
}

#[derive(Serialize, Clone)]
struct DropDto {
    dropped_id: String,
    kept_id: String,
    distance: u32,
}

#[derive(Serialize, Clone)]
struct DiscoveredDto {
    surface: String,
    doc_ids: Vec<String>,
}

#[derive(Serialize, Clone)]
struct ViewResp {
    window_end: Option<String>,
    documents_analyzed: usize,
    kept_doc_ids: Vec<String>,
    mentions: usize,
    near_duplicates: Vec<DropDto>,
    signals: Vec<SignalDto>,
    edges: Vec<EdgeDto>,
    discovered: Vec<DiscoveredDto>,
}

#[derive(Clone, Copy, Default)]
struct ViewStageTimings {
    sector_load_us: u64,
    analysis_us: u64,
    response_build_us: u64,
}

struct ViewHttpResponse {
    headers: HeaderMap,
    body: ViewResp,
    stages: ViewStageTimings,
    handler_started: Instant,
}

impl IntoResponse for ViewHttpResponse {
    fn into_response(mut self) -> Response {
        let serialization_started = Instant::now();
        diagnostic_delay("serialization");
        let body = serde_json::to_vec(&self.body).expect("ViewResp must serialize");
        let serialization_us = elapsed_us(serialization_started);
        let handler_total_us = elapsed_us(self.handler_started);

        insert_timing_header(
            &mut self.headers,
            "x-intel-view-stage-sector-load-us",
            self.stages.sector_load_us,
        );
        insert_timing_header(
            &mut self.headers,
            "x-intel-view-stage-analysis-us",
            self.stages.analysis_us,
        );
        insert_timing_header(
            &mut self.headers,
            "x-intel-view-stage-response-build-us",
            self.stages.response_build_us,
        );
        insert_timing_header(
            &mut self.headers,
            "x-intel-view-stage-serialization-us",
            serialization_us,
        );
        insert_timing_header(
            &mut self.headers,
            "x-intel-view-stage-handler-total-us",
            handler_total_us,
        );
        self.headers
            .insert("content-type", HeaderValue::from_static("application/json"));

        let mut response = Response::new(Body::from(body));
        *response.headers_mut() = self.headers;
        response
    }
}

#[derive(Deserialize)]
struct SearchQ {
    q: String,
    sectors: String,
    #[serde(default = "default_limit")]
    limit: usize,
}

fn default_limit() -> usize {
    10
}

#[derive(Serialize)]
struct SearchHitResp {
    doc_id: String,
    title: String,
    sector: String,
    source_id: String,
    url: Option<String>,
    license: String,
    /// null when the source license forbids redistribution.
    snippet: Option<String>,
    rank: f64,
}

#[derive(Deserialize)]
struct RetrieveReq {
    q: String,
    sectors: Vec<String>,
    #[serde(default = "default_k")]
    k: usize,
    /// Embedding model name, when the shell embedded the query.
    model: Option<String>,
    /// The query embedding, computed BY THE SHELL. The core never calls a
    /// model; it only does cosine over vectors it is given.
    query_vector: Option<Vec<f32>>,
}

fn default_k() -> usize {
    5
}

#[derive(Serialize)]
struct DocDto {
    doc_id: String,
    sector: String,
    title: String,
    body: String,
    url: Option<String>,
    source_id: String,
    day: Option<String>,
    license: String,
    authors: Vec<String>,
    tags: Vec<String>,
}

#[derive(Serialize)]
struct RetrieveResp {
    bm25: Vec<String>,
    vector: Vec<String>,
    fused: Vec<String>,
    notes: Vec<String>,
    /// fused-order context documents, near-duplicates suppressed at
    /// assembly (a syndicated copy must never waste a context slot).
    context: Vec<DocDto>,
    suppressed: Vec<String>,
}

#[derive(Deserialize)]
struct AttestReq {
    answer: String,
    context_doc_ids: Vec<String>,
    sectors: Vec<String>,
}

#[derive(Deserialize)]
struct MissingQ {
    model: String,
    sectors: String,
}

#[derive(Deserialize)]
struct ModelQ {
    model: String,
}

#[derive(Serialize)]
struct MissingDoc {
    doc_id: String,
    title: String,
    body: String,
}

#[derive(Serialize)]
struct EmbeddingStatsResp {
    count: usize,
    dim: Option<usize>,
    inconsistent_dimensions: bool,
}

#[derive(Deserialize)]
struct EmbedItem {
    doc_id: String,
    vector: Vec<f32>,
}

#[derive(Deserialize)]
struct UpsertReq {
    model: String,
    items: Vec<EmbedItem>,
}

#[derive(Serialize)]
struct UpsertResp {
    upserted: usize,
    total_for_model: usize,
}

#[derive(Deserialize)]
struct RecordReq {
    client: String,
    /// "YYYY-MM-DD" or null.
    window_end: Option<String>,
    signals: Vec<Signal>,
}

#[derive(Serialize)]
struct RecordResp {
    recorded: usize,
}

#[derive(Deserialize)]
struct DocsQ {
    ids: String,
    sectors: String,
}

// --- handlers -----------------------------------------------------------------

async fn health(State(st): State<Arc<AppState>>) -> Json<HealthResp> {
    Json(HealthResp {
        status: "ok",
        documents: st.store.count().unwrap_or(0),
        version: env!("CARGO_PKG_VERSION"),
    })
}

async fn sectors(
    State(st): State<Arc<AppState>>,
    headers: HeaderMap,
) -> Result<Json<Vec<SectorInfo>>, ApiErr> {
    guard(&st, &headers)?;
    Ok(Json(
        st.cfg
            .sectors
            .iter()
            .map(|s| SectorInfo {
                id: s.id.clone(),
                display_name: s.display_name.clone(),
                sources: s
                    .sources
                    .iter()
                    .map(|src| SourceInfo {
                        id: src.id.clone(),
                        r#type: src.source_type.clone(),
                        license: src.license.as_str().to_string(),
                    })
                    .collect(),
            })
            .collect(),
    ))
}

async fn ingest(
    State(st): State<Arc<AppState>>,
    headers: HeaderMap,
    Json(req): Json<IngestReq>,
) -> Result<Json<IngestResp>, ApiErr> {
    guard(&st, &headers)?;
    let want: HashSet<&str> = req.sectors.iter().map(|s| s.as_str()).collect();
    let only: Option<HashSet<&str>> = req
        .sources
        .as_ref()
        .map(|v| v.iter().map(|s| s.as_str()).collect());
    let selection = select_sources(&st.cfg, &want, only.as_ref());

    let cursor_adapter = Arc::new(CursorAdapter::new(st.clone()));
    let ctx = SourceContext {
        // The operator's own deny-list. It sits on top of whatever the
        // publisher's robots.txt says and can only ever refuse more (T2).
        robots: RobotsGate::new(&["/private", "/admin"]),
        // Process-scoped, so politeness carries across ingests rather than
        // resetting on every request.
        limiter: st.limiter.clone(),
        robots_cache: st.robots_cache.clone(),
        // Persist OAI-PMH resumptionToken + datestamp high-water in the store,
        // so harvests resume after an interrupt and fetch incrementally.
        // Connectors that don't page (RSS) ignore this.
        cursors: Some(cursor_adapter.clone()),
    };

    let mut fetched: Vec<Document> = Vec::new();
    let mut fetched_count = 0usize;
    let mut results = Vec::new();
    for sel in &selection.selected {
        match sel.source.fetch(&ctx).await {
            Ok(mut docs) => {
                fetched_count += docs.len();
                results.push(IngestSourceResult {
                    sector: sel.sector_id.clone(),
                    source_id: sel.source.id().to_string(),
                    ok: true,
                    documents: docs.len(),
                    error: None,
                });
                fetched.append(&mut docs);
            }
            Err(e) => {
                // Earlier pages may already be durable when a later request
                // fails. Report those documents rather than claiming zero.
                let committed = cursor_adapter.committed_for(sel.source.id());
                fetched_count += committed;
                results.push(IngestSourceResult {
                    sector: sel.sector_id.clone(),
                    source_id: sel.source.id().to_string(),
                    ok: false,
                    documents: committed,
                    error: Some(e.to_string()),
                });
            }
        }
    }
    // Requested source ids that matched no eligible connector: a structured
    // per-id error, never a panic.
    for id in &selection.unknown_ids {
        results.push(IngestSourceResult {
            sector: String::new(),
            source_id: id.clone(),
            ok: false,
            documents: 0,
            error: Some("unknown or not entitled source id".to_string()),
        });
    }
    let tail_new = st.store.append_new(&fetched).map_err(internal)?;
    if tail_new > 0 {
        // append_new committed both documents and canonical identity, so no
        // fallible work may sit between that durability point and invalidation.
        st.bump_generation();
    }
    let new = cursor_adapter.new_count() + tail_new;
    Ok(Json(IngestResp {
        fetched: fetched_count,
        new,
        results,
    }))
}

async fn view(
    State(st): State<Arc<AppState>>,
    headers: HeaderMap,
    Query(q): Query<SectorsQ>,
) -> Result<ViewHttpResponse, ApiErr> {
    let handler_started = Instant::now();
    guard(&st, &headers)?;
    let sectors = configured_view_sectors(&st, &q.sectors);

    // Only configured sectors become cache keys. An all-unknown request still
    // receives the empty view but cannot allocate a permanent cache entry.
    let key = sectors.join(",");
    let gen = st.generation.load(Ordering::SeqCst);

    let cached = st
        .view_cache
        .lock()
        .unwrap()
        .get(&key)
        .filter(|hit| hit.generation == gen)
        .map(|hit| hit.resp.clone());
    if let Some(response) = cached {
        return Ok(ViewHttpResponse {
            headers: view_cache_headers(&st, "hit", gen),
            body: response,
            stages: ViewStageTimings::default(),
            handler_started,
        });
    }

    let (resp, stages) = compute_view_resp(&st, &sectors)?;
    if !sectors.is_empty() {
        st.view_cache.lock().unwrap().insert(
            key,
            CachedView {
                generation: gen,
                resp: resp.clone(),
            },
        );
    }
    Ok(ViewHttpResponse {
        headers: view_cache_headers(&st, "miss", gen),
        body: resp,
        stages,
        handler_started,
    })
}

fn elapsed_us(started: Instant) -> u64 {
    u64::try_from(started.elapsed().as_micros()).unwrap_or(u64::MAX)
}

fn diagnostic_delay(stage: &str) {
    if std::env::var("CORE_VIEW_DIAGNOSTIC_DELAY_STAGE").as_deref() != Ok(stage) {
        return;
    }
    let delay_ms = std::env::var("CORE_VIEW_DIAGNOSTIC_DELAY_MS")
        .ok()
        .and_then(|raw| raw.parse::<u64>().ok())
        .unwrap_or(0)
        .min(10_000);
    if delay_ms > 0 {
        std::thread::sleep(Duration::from_millis(delay_ms));
    }
}

fn insert_timing_header(headers: &mut HeaderMap, name: &'static str, value: u64) {
    headers.insert(
        name,
        HeaderValue::from_str(&value.to_string())
            .expect("u64 timing is always a valid header value"),
    );
}

fn view_cache_headers(st: &AppState, status: &'static str, generation: u64) -> HeaderMap {
    let mut headers = HeaderMap::new();
    headers.insert("x-intel-view-cache", HeaderValue::from_static(status));
    headers.insert(
        "x-intel-view-generation",
        HeaderValue::from_str(&generation.to_string())
            .expect("u64 generation is always a valid header value"),
    );
    insert_timing_header(
        &mut headers,
        "x-intel-view-stage-process-main-to-listener-ready-us",
        st.process_main_to_listener_ready_us.load(Ordering::SeqCst),
    );
    insert_timing_header(
        &mut headers,
        "x-intel-view-stage-store-open-us",
        st.store_open_timings.total_us,
    );
    insert_timing_header(
        &mut headers,
        "x-intel-view-stage-store-connection-us",
        st.store_open_timings.connection_us,
    );
    insert_timing_header(
        &mut headers,
        "x-intel-view-stage-store-schema-fts-us",
        st.store_open_timings.schema_fts_us,
    );
    insert_timing_header(
        &mut headers,
        "x-intel-view-stage-store-cursor-migration-us",
        st.store_open_timings.cursor_migration_us,
    );
    insert_timing_header(
        &mut headers,
        "x-intel-view-stage-store-fingerprint-backfill-us",
        st.store_open_timings.fingerprint_backfill_us,
    );
    headers.insert(
        "x-intel-view-fingerprints-backfilled",
        HeaderValue::from_str(&st.store_open_timings.fingerprints_backfilled.to_string())
            .expect("usize count is always a valid header value"),
    );
    headers
}

/// The actual work behind `/view` — everything the cache is there to avoid.
fn compute_view_resp(
    st: &Arc<AppState>,
    sectors: &[String],
) -> Result<(ViewResp, ViewStageTimings), ApiErr> {
    st.view_computes.fetch_add(1, Ordering::SeqCst);

    let load_started = Instant::now();
    diagnostic_delay("sector_load");
    let corpus = sector_corpus(st, sectors)?;
    let sector_load_us = elapsed_us(load_started);

    let analysis_started = Instant::now();
    diagnostic_delay("analysis");
    let v = compute_view(corpus, &st.gaz, &ViewParams::default());
    let analysis_us = elapsed_us(analysis_started);

    let response_started = Instant::now();
    diagnostic_delay("response_build");
    let docs: HashMap<&str, &Document> = v.dd.kept.iter().map(|d| (d.id.as_str(), d)).collect();
    let names = entity_names(&st.gaz.entities);

    let signals: Vec<SignalDto> = v
        .analysis
        .signals
        .iter()
        .map(|s| SignalDto {
            kind: format!("{:?}", s.kind),
            headline: s.headline.clone(),
            score: s.score,
            detail: s.detail.clone(),
            entity_ids: s.entity_ids.clone(),
            evidence: s
                .evidence
                .iter()
                .filter_map(|id| docs.get(id.as_str()))
                .map(|d| EvidenceDto {
                    doc_id: d.id.clone(),
                    title: d.title.clone(),
                    url: d.url.clone(),
                    source_id: d.provenance.source_id.clone(),
                    day: d.published_day.map(|x| x.to_string()),
                    license: d.provenance.license.as_str().to_string(),
                    excerpt: if d.provenance.license.redistributable() {
                        Some(snippet(&d.body, 140))
                    } else {
                        None
                    },
                })
                .collect(),
        })
        .collect();

    let edges: Vec<EdgeDto> = v
        .analysis
        .edges
        .iter()
        .map(|e| EdgeDto {
            a: e.a.clone(),
            b: e.b.clone(),
            a_name: names.get(e.a.as_str()).copied().unwrap_or(&e.a).to_string(),
            b_name: names.get(e.b.as_str()).copied().unwrap_or(&e.b).to_string(),
            weight: e.weight,
            pmi: e.pmi,
        })
        .collect();

    let response = ViewResp {
        window_end: v.analysis.window_end.map(|d| d.to_string()),
        documents_analyzed: v.dd.kept.len(),
        kept_doc_ids: v.dd.kept.iter().map(|d| d.id.clone()).collect(),
        mentions: v.mentions.len(),
        near_duplicates: v
            .dd
            .drops
            .iter()
            .map(|d| DropDto {
                dropped_id: d.dropped_id.clone(),
                kept_id: d.kept_id.clone(),
                distance: d.distance,
            })
            .collect(),
        signals,
        edges,
        discovered: v
            .discovered
            .iter()
            .map(|d| DiscoveredDto {
                surface: d.surface.clone(),
                doc_ids: d.doc_ids.clone(),
            })
            .collect(),
    };
    let response_build_us = elapsed_us(response_started);
    Ok((
        response,
        ViewStageTimings {
            sector_load_us,
            analysis_us,
            response_build_us,
        },
    ))
}

async fn search(
    State(st): State<Arc<AppState>>,
    headers: HeaderMap,
    Query(p): Query<SearchQ>,
) -> Result<Json<Vec<SearchHitResp>>, ApiErr> {
    guard(&st, &headers)?;
    let sectors = parse_csv(&p.sectors);
    let hits = st
        .store
        .search(&p.q, &sectors, p.limit.min(50))
        .map_err(|_| {
            (
                StatusCode::BAD_REQUEST,
                "invalid FTS5 query syntax".to_string(),
            )
        })?;
    Ok(Json(
        hits.into_iter()
            .map(|h| SearchHitResp {
                doc_id: h.doc_id,
                title: h.title,
                sector: h.sector,
                source_id: h.source_id,
                url: h.url,
                license: h.license.as_str().to_string(),
                snippet: h.snippet,
                rank: h.rank,
            })
            .collect(),
    ))
}

async fn retrieve(
    State(st): State<Arc<AppState>>,
    headers: HeaderMap,
    Json(req): Json<RetrieveReq>,
) -> Result<Json<RetrieveResp>, ApiErr> {
    guard(&st, &headers)?;
    let qv = req.model.as_deref().zip(req.query_vector.as_deref());
    let r = intel_retrieve::hybrid(&st.store, &req.q, &req.sectors, req.k.min(8), qv)
        .map_err(internal)?;

    // Materialize fused docs, suppressing near-duplicates at context assembly:
    // retrieval runs over the raw archive, so a syndicated copy can ride in
    // alongside its original.
    //
    // The fingerprints are now READ (persisted at ingest, T9.1) rather than
    // recomputed per request. The suppression POLICY, though, deliberately
    // stays rank-aware: we keep whichever of a near-dup pair the query ranked
    // higher, not the corpus-canonical one. Filtering by `canonical_id` in SQL
    // — the obvious-looking "proper fix" — would force the canonical copy into
    // context even when the other one is the better answer to *this* question.
    // Canonical id is a property of the corpus; relevance is a property of the
    // query, and context assembly is a question about the query.
    let fused_ids: Vec<&str> = r.fused.iter().map(|(id, _)| id.as_str()).collect();
    let all = st
        .store
        .documents_by_ids_in_sectors(&fused_ids, &req.sectors)
        .map_err(internal)?;
    let by_id: HashMap<&str, &Document> = all.iter().map(|d| (d.id.as_str(), d)).collect();
    let prints = st.store.fingerprints().map_err(internal)?;

    let mut context = Vec::new();
    let mut suppressed = Vec::new();
    let mut fingerprints: Vec<u64> = Vec::new();
    for (doc_id, _) in r.fused.iter() {
        let Some(d) = by_id.get(doc_id.as_str()) else {
            continue;
        };
        let fp = persisted_fingerprint(&prints, doc_id)?;
        if fingerprints.iter().any(|k| hamming(*k, fp) <= 16) {
            suppressed.push(d.id.clone());
            continue;
        }
        fingerprints.push(fp);
        context.push(doc_dto(d));
    }

    Ok(Json(RetrieveResp {
        bm25: r.bm25,
        vector: r.vector,
        fused: r.fused.into_iter().map(|(id, _)| id).collect(),
        notes: r.notes,
        context,
        suppressed,
    }))
}

async fn attest(
    State(st): State<Arc<AppState>>,
    headers: HeaderMap,
    Json(req): Json<AttestReq>,
) -> Result<Json<Attestation>, ApiErr> {
    guard(&st, &headers)?;
    if req.context_doc_ids.len() > 8 {
        return Err((
            StatusCode::BAD_REQUEST,
            "attestation accepts at most 8 context documents".to_string(),
        ));
    }

    let requested_ids: Vec<&str> = req.context_doc_ids.iter().map(String::as_str).collect();
    let all = st
        .store
        .documents_by_ids_in_sectors(&requested_ids, &req.sectors)
        .map_err(internal)?;
    let by_id: HashMap<&str, &Document> = all
        .iter()
        .map(|document| (document.id.as_str(), document))
        .collect();
    let mut seen = HashSet::new();
    let mut context = Vec::with_capacity(req.context_doc_ids.len());
    for doc_id in &req.context_doc_ids {
        if !seen.insert(doc_id.as_str()) {
            continue;
        }
        let Some(document) = by_id.get(doc_id.as_str()) else {
            return Err((
                StatusCode::BAD_REQUEST,
                "unknown context document id".to_string(),
            ));
        };
        context.push(*document);
    }

    Ok(Json(attest_answer(&req.answer, &context)))
}

async fn embeddings_missing(
    State(st): State<Arc<AppState>>,
    headers: HeaderMap,
    Query(p): Query<MissingQ>,
) -> Result<Json<Vec<MissingDoc>>, ApiErr> {
    guard(&st, &headers)?;
    let sectors = parse_csv(&p.sectors);
    let docs = st
        .store
        .docs_missing_embeddings(&p.model, &sectors)
        .map_err(internal)?;
    Ok(Json(
        docs.into_iter()
            .map(|d| MissingDoc {
                doc_id: d.id,
                title: d.title,
                body: d.body,
            })
            .collect(),
    ))
}

async fn embeddings_stats(
    State(st): State<Arc<AppState>>,
    headers: HeaderMap,
    Query(p): Query<ModelQ>,
) -> Result<Json<EmbeddingStatsResp>, ApiErr> {
    guard(&st, &headers)?;
    let stats = st.store.embeddings_stats(&p.model).map_err(internal)?;
    Ok(Json(EmbeddingStatsResp {
        count: stats.count,
        dim: stats.dim,
        inconsistent_dimensions: stats.inconsistent_dimensions,
    }))
}

async fn embeddings_upsert(
    State(st): State<Arc<AppState>>,
    headers: HeaderMap,
    Json(req): Json<UpsertReq>,
) -> Result<Json<UpsertResp>, ApiErr> {
    guard(&st, &headers)?;
    let items: Vec<(String, Vec<f32>)> = req
        .items
        .into_iter()
        .map(|i| (i.doc_id, i.vector))
        .collect();
    let upserted = st
        .store
        .upsert_embeddings(&req.model, &items)
        .map_err(internal)?;
    let total = st.store.embeddings_count(&req.model).map_err(internal)?;
    Ok(Json(UpsertResp {
        upserted,
        total_for_model: total,
    }))
}

async fn signals_record(
    State(st): State<Arc<AppState>>,
    headers: HeaderMap,
    Json(req): Json<RecordReq>,
) -> Result<Json<RecordResp>, ApiErr> {
    guard(&st, &headers)?;
    let day = req.window_end.as_deref().and_then(Day::parse_iso);
    st.store
        .record_signals(&req.client, day, &req.signals)
        .map_err(internal)?;
    Ok(Json(RecordResp {
        recorded: req.signals.len(),
    }))
}

async fn docs(
    State(st): State<Arc<AppState>>,
    headers: HeaderMap,
    Query(p): Query<DocsQ>,
) -> Result<Json<Vec<DocDto>>, ApiErr> {
    guard(&st, &headers)?;
    let ids = parse_csv(&p.ids);
    let sectors = parse_csv(&p.sectors);
    let id_refs: Vec<&str> = ids.iter().map(String::as_str).collect();
    let documents = st
        .store
        .documents_by_ids_in_sectors(&id_refs, &sectors)
        .map_err(internal)?;
    Ok(Json(documents.iter().map(doc_dto).collect()))
}

// --- main -----------------------------------------------------------------------

fn validate_loopback_addresses(
    bind: &str,
    addresses: Vec<SocketAddr>,
) -> Result<Vec<SocketAddr>, String> {
    if addresses.is_empty() {
        return Err(format!("CORE_BIND {bind:?} resolved to no addresses"));
    }
    if let Some(address) = addresses.iter().find(|address| !address.ip().is_loopback()) {
        return Err(format!(
            "CORE_BIND {bind:?} resolved to non-loopback address {address}; \
             non-loopback binding is the multi-host seam deferral and requires a design task"
        ));
    }
    Ok(addresses)
}

fn loopback_only(bind: &str) -> Result<Vec<SocketAddr>, String> {
    let addresses = bind
        .to_socket_addrs()
        .map_err(|error| format!("could not resolve CORE_BIND {bind:?}: {error}"))?
        .collect();
    validate_loopback_addresses(bind, addresses)
}

#[tokio::main]
async fn main() {
    let process_main_started = Instant::now();
    let config_path = std::env::var("CORE_CONFIG").unwrap_or_else(|_| "config/core.json".into());
    let entities_path =
        std::env::var("CORE_ENTITIES").unwrap_or_else(|_| "config/entities.json".into());
    let db_path = std::env::var("CORE_DB").unwrap_or_else(|_| "data/intel.db".into());
    let bind = std::env::var("CORE_BIND").unwrap_or_else(|_| "127.0.0.1:8788".into());
    let bind_addresses =
        loopback_only(&bind).unwrap_or_else(|error| panic!("cored refused to start: {error}"));
    let token = std::env::var("CORE_TOKEN").ok();

    let cfg: CoreConfig =
        serde_json::from_str(&std::fs::read_to_string(&config_path).expect("read core config"))
            .expect("parse core config");
    let gaz =
        Gazetteer::from_json(&std::fs::read_to_string(&entities_path).expect("read entities"))
            .expect("parse entities");
    let (store, store_open_timings) =
        SqliteStore::open_with_timings(Path::new(&db_path)).expect("open store");

    let n = store.count().unwrap_or(0);
    let state = Arc::new(AppState::new_with_startup(
        store,
        gaz,
        cfg,
        token,
        store_open_timings,
    ));

    let app = Router::new()
        .route("/health", get(health))
        .route("/sectors", get(sectors))
        .route("/ingest", post(ingest))
        .route("/view", get(view))
        .route("/search", get(search))
        .route("/retrieve", post(retrieve))
        .route("/attest", post(attest))
        .route("/embeddings/missing", get(embeddings_missing))
        .route("/embeddings/stats", get(embeddings_stats))
        .route("/embeddings", post(embeddings_upsert))
        .route("/signals/record", post(signals_record))
        .route("/docs", get(docs))
        .with_state(state.clone());

    let listener = tokio::net::TcpListener::bind(&bind_addresses[..])
        .await
        .expect("bind");
    state
        .process_main_to_listener_ready_us
        .store(elapsed_us(process_main_started), Ordering::SeqCst);
    println!(
        "cored on http://{bind}  (archive: {n} documents; token auth: {})",
        if std::env::var("CORE_TOKEN").is_ok() {
            "on"
        } else {
            "off"
        }
    );
    axum::serve(listener, app).await.expect("serve");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn loopback_bind_check_rejects_unspecified_and_lan_literals() {
        for bind in ["0.0.0.0:8788", "[::]:8788", "192.168.1.10:8788"] {
            let error = loopback_only(bind).expect_err("non-loopback bind must be refused");
            assert!(
                error.contains("non-loopback address"),
                "unexpected error for {bind}: {error}"
            );
            assert!(
                error.contains("multi-host seam deferral"),
                "refusal must identify the design seam: {error}"
            );
        }
    }

    #[test]
    fn loopback_bind_check_accepts_ipv4_ipv6_and_localhost() {
        for bind in ["127.0.0.1:8788", "[::1]:8788", "localhost:8788"] {
            let addresses = loopback_only(bind)
                .unwrap_or_else(|error| panic!("loopback bind {bind} should be accepted: {error}"));
            assert!(!addresses.is_empty());
            assert!(addresses.iter().all(|address| address.ip().is_loopback()));
        }
    }

    #[test]
    fn hostname_with_mixed_loopback_and_non_loopback_answers_is_rejected() {
        let loopback: SocketAddr = "127.0.0.1:8788".parse().unwrap();
        let non_loopback: SocketAddr = "192.168.1.10:8788".parse().unwrap();
        let error =
            validate_loopback_addresses("mixed-address.example:8788", vec![loopback, non_loopback])
                .expect_err("every resolved address must be loopback");

        assert!(error.contains("192.168.1.10:8788"));
        assert!(error.contains("multi-host seam deferral"));
    }

    #[cfg(not(feature = "net"))]
    #[test]
    fn offline_build_does_not_require_or_construct_a_crawler_identity() {
        let limiter = Arc::new(HostLimiters::per_second(DEFAULT_RPS));
        assert!(build_robots_cache(limiter).is_none());
    }

    #[cfg(feature = "net")]
    #[test]
    fn net_build_refuses_missing_empty_and_placeholder_contacts() {
        for contact in [
            None,
            Some(""),
            Some("   "),
            Some("ops@example.com"),
            Some("you@operator.test"),
            Some("changeme"),
            Some("MAILTO:CHANGEME@operator.test"),
        ] {
            let limiter = Arc::new(HostLimiters::per_second(DEFAULT_RPS));
            let error = match build_robots_cache_for_contact(limiter, contact) {
                Ok(_) => panic!("placeholder identity must refuse startup"),
                Err(error) => error,
            };
            assert!(
                error.contains(CRAWLER_CONTACT_ENV),
                "refusal must name the required setting: {error}"
            );
        }
    }

    #[cfg(feature = "net")]
    #[test]
    fn valid_contact_builds_one_versioned_identity_for_cache_and_clients() {
        let contact = "crawler-tests@unit.test";
        let expected = format!(
            "intel-platform/{} (research prototype; contact: {contact})",
            env!("CARGO_PKG_VERSION")
        );
        let limiter = Arc::new(HostLimiters::per_second(DEFAULT_RPS));
        let (_cache, cache_user_agent) = build_robots_cache_for_contact(limiter, Some(contact))
            .expect("real contact builds the live robots cache");

        assert_eq!(cache_user_agent, expected);
        assert_eq!(
            intel_ingest::net::crawler_user_agent(env!("CARGO_PKG_VERSION"), contact),
            expected
        );
    }

    // Workspace root, from this crate's manifest dir (apps/cored -> ../..).
    fn root() -> std::path::PathBuf {
        std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("..")
            .join("..")
            .canonicalize()
            .expect("workspace root")
    }

    fn tmp_db() -> std::path::PathBuf {
        // SystemTime alone is NOT unique: cargo runs tests as parallel threads
        // in ONE process, and two threads calling this within the same clock
        // tick (or on a coarse-resolution clock) get the same path and clobber
        // each other's DB — a real flake that showed up as a "fresh" test DB
        // already holding another test's rows. A process-global monotonic
        // counter guarantees a distinct path per call regardless of clock
        // resolution or timing; the pid keeps it distinct across processes too.
        use std::sync::atomic::{AtomicU64, Ordering};
        static SEQ: AtomicU64 = AtomicU64::new(0);
        let seq = SEQ.fetch_add(1, Ordering::Relaxed);
        let n = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .unwrap()
            .as_nanos();
        let pid = std::process::id();
        std::env::temp_dir().join(format!("cored-ingest-test-{pid}-{seq}-{n}.db"))
    }

    // A three-source config (two in `technology`, one in `finance`) backed by
    // the repo's committed fixtures via absolute paths, so it works regardless
    // of the test's working directory.
    fn test_state() -> Arc<AppState> {
        let root = root();
        let fixture = |name: &str| root.join("fixtures").join(name).display().to_string();
        let cfg_json = serde_json::json!({
            "sectors": [
                { "id": "technology", "display_name": "Technology", "sources": [
                    { "type": "rss", "id": "techwire", "url": "https://example.org/tw",
                      "fixture": fixture("techwire.xml"), "license": "CcBy" },
                    { "type": "rss", "id": "osdaily", "url": "https://example.org/os",
                      "fixture": fixture("osdaily.xml"), "license": "IndexOnly" }
                ]},
                { "id": "finance", "display_name": "Finance", "sources": [
                    { "type": "rss", "id": "filings-digest", "url": "https://example.org/fin",
                      "fixture": fixture("finance.xml"), "license": "PublicDomain" }
                ]}
            ]
        })
        .to_string();
        let cfg: CoreConfig = serde_json::from_str(&cfg_json).expect("parse test cfg");
        let gaz = Gazetteer::from_json(
            &std::fs::read_to_string(root.join("config/entities.json")).expect("read entities"),
        )
        .expect("parse entities");
        let store = SqliteStore::open(&tmp_db()).expect("open store");
        Arc::new(AppState::new(store, gaz, cfg, None))
    }

    fn empty_sector_state(sector_count: usize) -> Arc<AppState> {
        let root = root();
        let sectors: Vec<serde_json::Value> = (0..sector_count)
            .map(|index| {
                serde_json::json!({
                    "id": format!("sector-{index:03}"),
                    "display_name": format!("Sector {index:03}"),
                    "sources": []
                })
            })
            .collect();
        let cfg: CoreConfig = serde_json::from_value(serde_json::json!({
            "sectors": sectors
        }))
        .expect("parse empty-sector test config");
        let gaz = Gazetteer::from_json(
            &std::fs::read_to_string(root.join("config/entities.json")).expect("read entities"),
        )
        .expect("parse entities");
        let store = SqliteStore::open(&tmp_db()).expect("open store");
        Arc::new(AppState::new(store, gaz, cfg, None))
    }

    async fn do_ingest(
        st: &Arc<AppState>,
        sectors: &[&str],
        sources: Option<&[&str]>,
    ) -> IngestResp {
        let req = IngestReq {
            sectors: sectors.iter().map(|s| s.to_string()).collect(),
            sources: sources.map(|v| v.iter().map(|s| s.to_string()).collect()),
        };
        ingest(State(st.clone()), HeaderMap::new(), Json(req))
            .await
            .expect("ingest ok")
            .0
    }

    #[test]
    fn retrieve_refuses_a_fused_document_without_a_persisted_fingerprint() {
        let error = persisted_fingerprint(&HashMap::new(), "missing-retrieve-fingerprint")
            .expect_err("retrieve must fail closed rather than recompute");
        assert_eq!(error.0, StatusCode::INTERNAL_SERVER_ERROR);
        assert!(
            error.1.contains("missing-retrieve-fingerprint"),
            "{error:?}"
        );
        assert!(error.1.contains("verify-fingerprints"), "{error:?}");
    }

    #[tokio::test]
    async fn attest_endpoint_refuses_an_index_only_body() {
        let st = test_state();
        do_ingest(&st, &["technology"], Some(&["osdaily"])).await;
        let document = st
            .store
            .load_all()
            .expect("load documents")
            .into_iter()
            .find(|document| document.provenance.license == intel_core::License::IndexOnly)
            .expect("IndexOnly fixture document");
        let answer = format!("Copied from the source: {}", document.body);

        let response = attest(
            State(st.clone()),
            HeaderMap::new(),
            Json(AttestReq {
                answer,
                context_doc_ids: vec![document.id.clone()],
                sectors: vec!["technology".into()],
            }),
        )
        .await
        .expect("attest ok")
        .0;

        assert_eq!(response.clean_answer, intel_core::ATTEST_REFUSAL);
        assert_eq!(response.violations.len(), 1);
        assert_eq!(response.violations[0].doc_id, document.id);
    }

    #[tokio::test]
    async fn retrieve_final_hydration_filters_cross_sector_and_empty_sectors() {
        let st = test_state();
        do_ingest(&st, &["technology", "finance"], None).await;
        let technology_id = st
            .store
            .load_all()
            .unwrap()
            .into_iter()
            .find(|document| document.sector.0 == "technology")
            .expect("technology fixture document")
            .id;
        let ranked_ids = [technology_id.as_str()];
        let finance_sectors = vec!["finance".to_string()];

        // Inject a forged post-ranking id at the exact final hydration
        // boundary. The real ranking legs already filter by sector, so an
        // endpoint-only happy-path test cannot prove this independent guard.
        let cross_sector = st
            .store
            .documents_by_ids_in_sectors(&ranked_ids, &finance_sectors)
            .expect("retrieve final hydration");
        assert!(
            cross_sector.is_empty(),
            "a finance-scoped final hydration must discard a technology id"
        );

        let empty = retrieve(
            State(st),
            HeaderMap::new(),
            Json(RetrieveReq {
                q: "DeepSeek".into(),
                sectors: Vec::new(),
                k: 5,
                model: None,
                query_vector: None,
            }),
        )
        .await
        .expect("empty sectors return an empty internal result")
        .0;
        assert!(empty.bm25.is_empty());
        assert!(empty.vector.is_empty());
        assert!(empty.fused.is_empty());
        assert!(empty.context.is_empty());
    }

    #[tokio::test]
    async fn attest_cross_sector_oracle_and_empty_sectors_fail_closed() {
        let st = test_state();
        do_ingest(&st, &["technology", "finance"], None).await;
        let document = st
            .store
            .load_all()
            .unwrap()
            .into_iter()
            .find(|document| {
                document.sector.0 == "technology"
                    && document.provenance.license == intel_core::License::IndexOnly
            })
            .expect("technology IndexOnly fixture document");
        let answer = document
            .body
            .split_whitespace()
            .take(16)
            .collect::<Vec<_>>()
            .join(" ");
        assert_eq!(answer.split_whitespace().count(), 16);

        let cross_sector = attest(
            State(st.clone()),
            HeaderMap::new(),
            Json(AttestReq {
                answer: answer.clone(),
                context_doc_ids: vec![document.id.clone()],
                sectors: vec!["finance".into()],
            }),
        )
        .await;
        match cross_sector {
            Err(error) => {
                assert_eq!(
                    error,
                    (
                        StatusCode::BAD_REQUEST,
                        "unknown context document id".to_string()
                    )
                );
                assert!(
                    !error.1.contains(&document.id),
                    "the refusal must not name the out-of-sector document"
                );
            }
            Ok(_) => panic!("out-of-sector ids must be indistinguishable from nonexistent ids"),
        }

        let nonexistent = attest(
            State(st.clone()),
            HeaderMap::new(),
            Json(AttestReq {
                answer: answer.clone(),
                context_doc_ids: vec!["does-not-exist".into()],
                sectors: vec!["finance".into()],
            }),
        )
        .await
        .expect_err("nonexistent ids must be refused");
        assert_eq!(
            nonexistent,
            (
                StatusCode::BAD_REQUEST,
                "unknown context document id".to_string()
            )
        );

        let empty = attest(
            State(st),
            HeaderMap::new(),
            Json(AttestReq {
                answer,
                context_doc_ids: vec![document.id.clone()],
                sectors: Vec::new(),
            }),
        )
        .await;
        match empty {
            Err(error) => assert_eq!(
                error,
                (
                    StatusCode::BAD_REQUEST,
                    "unknown context document id".to_string()
                )
            ),
            Ok(_) => panic!("an empty sector set must fail closed"),
        }
    }

    #[tokio::test]
    async fn retrieve_reports_stored_embedding_dimension_mismatches() {
        let st = test_state();
        do_ingest(&st, &["technology"], Some(&["techwire"])).await;
        let doc_id = st.store.load_all().unwrap()[0].id.clone();
        st.store
            .upsert_embeddings("shared-model", &[(doc_id, vec![1.0; 32])])
            .unwrap();
        let stats = embeddings_stats(
            State(st.clone()),
            HeaderMap::new(),
            Query(ModelQ {
                model: "shared-model".into(),
            }),
        )
        .await
        .expect("embedding stats")
        .0;
        assert_eq!(stats.count, 1);
        assert_eq!(stats.dim, Some(32));
        assert!(!stats.inconsistent_dimensions);
        let upsert_error = match embeddings_upsert(
            State(st.clone()),
            HeaderMap::new(),
            Json(UpsertReq {
                model: "shared-model".into(),
                items: vec![EmbedItem {
                    doc_id: "different-document".into(),
                    vector: vec![1.0; 1024],
                }],
            }),
        )
        .await
        {
            Ok(_) => panic!("mixed dimensions must be refused by the endpoint"),
            Err(error) => error,
        };
        assert_eq!(upsert_error.0, StatusCode::INTERNAL_SERVER_ERROR);
        assert!(upsert_error.1.contains("shared-model"), "{upsert_error:?}");
        assert!(upsert_error.1.contains("32"), "{upsert_error:?}");
        assert!(upsert_error.1.contains("1024"), "{upsert_error:?}");

        let response = retrieve(
            State(st),
            HeaderMap::new(),
            Json(RetrieveReq {
                q: "DeepSeek".into(),
                sectors: vec!["technology".into()],
                k: 5,
                model: Some("shared-model".into()),
                query_vector: Some(vec![1.0; 1024]),
            }),
        )
        .await
        .expect("retrieve remains available with an explicit diagnostic")
        .0;

        assert!(
            response.notes.iter().any(|note| {
                note.contains("shared-model")
                    && note.contains("1 stored embedding")
                    && note.contains("1024")
            }),
            "dimension mismatch must be visible in /retrieve notes: {:?}",
            response.notes
        );
        assert!(response.vector.is_empty());
    }

    #[tokio::test]
    async fn docs_filters_requested_ids_by_sector_and_fails_closed_when_empty() {
        let st = test_state();
        do_ingest(&st, &["technology", "finance"], None).await;
        let all = st.store.load_all().unwrap();
        let technology_id = all
            .iter()
            .find(|document| document.sector.0 == "technology")
            .unwrap()
            .id
            .clone();
        let finance_id = all
            .iter()
            .find(|document| document.sector.0 == "finance")
            .unwrap()
            .id
            .clone();
        let ids = format!("{technology_id},{finance_id}");

        let entitled = docs(
            State(st.clone()),
            HeaderMap::new(),
            Query(DocsQ {
                ids: ids.clone(),
                sectors: "technology".into(),
            }),
        )
        .await
        .expect("sector-bound docs")
        .0;
        assert_eq!(entitled.len(), 1);
        assert_eq!(entitled[0].doc_id, technology_id);
        assert_eq!(entitled[0].sector, "technology");

        let empty = docs(
            State(st),
            HeaderMap::new(),
            Query(DocsQ {
                ids,
                sectors: String::new(),
            }),
        )
        .await
        .expect("empty sectors fail closed")
        .0;
        assert!(empty.is_empty());
    }

    #[tokio::test]
    async fn missing_embeddings_filters_by_sector_and_fails_closed_when_empty() {
        let st = test_state();
        do_ingest(&st, &["technology", "finance"], None).await;

        let finance = embeddings_missing(
            State(st.clone()),
            HeaderMap::new(),
            Query(MissingQ {
                model: "sector-bound-model".into(),
                sectors: "finance".into(),
            }),
        )
        .await
        .expect("sector-bound embedding queue")
        .0;
        assert!(!finance.is_empty());
        assert!(finance
            .iter()
            .all(|document| document.doc_id.starts_with("filings-digest::")));

        let empty = embeddings_missing(
            State(st),
            HeaderMap::new(),
            Query(MissingQ {
                model: "sector-bound-model".into(),
                sectors: String::new(),
            }),
        )
        .await
        .expect("empty sectors fail closed")
        .0;
        assert!(empty.is_empty());
    }

    // HC5 regression guard: a sector-only request runs every source in the
    // sector, in config order, with no source filtering artifacts.
    #[tokio::test]
    async fn sector_only_runs_all_sources_unchanged() {
        let st = test_state();
        let resp = do_ingest(&st, &["technology"], None).await;
        let ran: Vec<&str> = resp.results.iter().map(|r| r.source_id.as_str()).collect();
        assert_eq!(ran, vec!["techwire", "osdaily"]);
        assert!(resp.results.iter().all(|r| r.ok));
        assert_eq!(resp.new, resp.fetched); // fresh db: everything is new
        assert!(resp.fetched > 0);
    }

    // Per-source filtering: only the named source in the sector runs.
    #[tokio::test]
    async fn source_filter_runs_only_named_source() {
        let st = test_state();
        let resp = do_ingest(&st, &["technology"], Some(&["techwire"])).await;
        let ran: Vec<&str> = resp.results.iter().map(|r| r.source_id.as_str()).collect();
        assert_eq!(ran, vec!["techwire"]); // osdaily NOT fetched
        assert!(resp.results.iter().all(|r| r.ok));
    }

    // Two sources in one sector, addressed independently — the capability the
    // per-source scheduler cadence is built on.
    #[tokio::test]
    async fn each_source_in_a_sector_is_independently_addressable() {
        let st = test_state();
        let only_os = do_ingest(&st, &["technology"], Some(&["osdaily"])).await;
        let ran: Vec<&str> = only_os
            .results
            .iter()
            .map(|r| r.source_id.as_str())
            .collect();
        assert_eq!(ran, vec!["osdaily"]);
    }

    // Unknown / not-entitled source id -> structured error result, never a panic.
    #[tokio::test]
    async fn unknown_source_id_yields_structured_error() {
        let st = test_state();
        let resp = do_ingest(&st, &["technology"], Some(&["ghost"])).await;
        let err = resp
            .results
            .iter()
            .find(|r| r.source_id == "ghost")
            .expect("ghost reported");
        assert!(!err.ok);
        assert!(err
            .error
            .as_deref()
            .unwrap_or("")
            .contains("unknown or not entitled"));
        assert_eq!(resp.fetched, 0);
    }

    // A source in a sector the caller isn't entitled to is rejected (defense in
    // depth: the sector filter still applies even when a source id is named).
    #[tokio::test]
    async fn source_outside_entitlement_is_rejected() {
        let st = test_state();
        let resp = do_ingest(&st, &["technology"], Some(&["filings-digest"])).await;
        assert!(resp.results.iter().all(|r| !r.ok)); // nothing ran successfully
        assert_eq!(resp.fetched, 0);
        assert!(resp
            .results
            .iter()
            .any(|r| r.source_id == "filings-digest" && !r.ok));
    }

    #[tokio::test]
    async fn non_paged_rematerialization_failure_rolls_back_append_and_generation() {
        let st = test_state();
        let seeded = do_ingest(&st, &["finance"], Some(&["filings-digest"])).await;
        assert_eq!(seeded.new, 1);
        let before_count = st.store.count().unwrap();
        let before_generation = st.generation.load(Ordering::SeqCst);
        let seed_id = st.store.load_all().unwrap()[0].id.clone();
        assert_eq!(st.store.test_clear_fingerprint(&seed_id).unwrap(), 1);

        let result = ingest(
            State(st.clone()),
            HeaderMap::new(),
            Json(IngestReq {
                sectors: vec!["technology".into()],
                sources: Some(vec!["techwire".into()]),
            }),
        )
        .await;
        let error = match result {
            Ok(_) => panic!("injected rematerialization failure must return 500"),
            Err(error) => error,
        };

        assert_eq!(error.0, StatusCode::INTERNAL_SERVER_ERROR);
        assert!(error.1.contains(&seed_id), "{error:?}");
        assert_eq!(
            st.store.count().unwrap(),
            before_count,
            "a failed non-paged rematerialization committed appended rows"
        );
        assert_eq!(
            st.generation.load(Ordering::SeqCst),
            before_generation,
            "a failed ingest moved the view generation"
        );
    }

    #[tokio::test]
    async fn later_paged_failure_keeps_earlier_page_durable_and_generation_moved() {
        let donor = test_state();
        do_ingest(&donor, &["technology"], Some(&["techwire"])).await;
        let docs = donor.store.load_all().unwrap();
        assert!(docs.len() >= 4);

        let st = test_state();
        let adapter = CursorAdapter::new(st.clone());
        let first_page = &docs[..2];
        assert_eq!(
            adapter
                .commit_page(
                    "paged-fixture",
                    first_page,
                    Some("page-2-token"),
                    Some("2026-07-04"),
                )
                .unwrap(),
            2
        );
        assert_eq!(st.store.count().unwrap(), 2);
        assert_eq!(st.generation.load(Ordering::SeqCst), 1);
        for document in first_page {
            assert!(
                st.store.canonical_id(&document.id).unwrap().is_some(),
                "{} has no canonical identity after the first page",
                document.id
            );
        }

        assert_eq!(
            st.store.test_clear_fingerprint(&first_page[0].id).unwrap(),
            1
        );
        let error = adapter
            .commit_page("paged-fixture", &docs[2..], None, Some("2026-07-05"))
            .expect_err("the injected later-page failure must fire");
        assert!(error.contains(&first_page[0].id), "{error}");

        assert_eq!(
            st.store.count().unwrap(),
            2,
            "the failed later page itself must roll back"
        );
        assert_eq!(
            st.generation.load(Ordering::SeqCst),
            1,
            "the failed later page must not bump generation again"
        );
        assert_eq!(adapter.committed_for("paged-fixture"), 2);
        assert_eq!(adapter.new_count(), 2);
        let cursor = st.store.get_cursor("paged-fixture").unwrap().unwrap();
        assert_eq!(cursor.cursor.as_deref(), Some("page-2-token"));
        for document in first_page {
            assert!(
                st.store.canonical_id(&document.id).unwrap().is_some(),
                "{} lost its earlier-page canonical identity",
                document.id
            );
        }
    }

    // --- T9.2: /view caching ------------------------------------------------

    async fn do_view_with_headers(st: &Arc<AppState>, sectors: &str) -> (HeaderMap, ViewResp) {
        let response = view(
            State(st.clone()),
            HeaderMap::new(),
            Query(SectorsQ {
                sectors: sectors.to_string(),
            }),
        )
        .await
        .expect("view ok");
        (response.headers, response.body)
    }

    async fn do_view(st: &Arc<AppState>, sectors: &str) -> ViewResp {
        do_view_with_headers(st, sectors).await.1
    }

    #[tokio::test]
    async fn view_excludes_documents_outside_the_sql_sector_filter() {
        let st = test_state();
        do_ingest(&st, &["technology", "finance"], None).await;
        let finance_ids: Vec<String> = st
            .store
            .documents_in_sectors(&["finance".to_string()])
            .unwrap()
            .into_iter()
            .map(|(document, _)| document.id)
            .collect();
        assert!(!finance_ids.is_empty());

        let technology = do_view(&st, "technology").await;
        assert!(
            finance_ids
                .iter()
                .all(|id| !technology.kept_doc_ids.contains(id)),
            "unentitled finance document escaped the SQL filter"
        );
    }

    #[tokio::test]
    async fn view_is_memoized_between_ingests_and_refreshed_after_one() {
        let st = test_state();
        do_ingest(&st, &["technology"], None).await;

        let (first_headers, first) = do_view_with_headers(&st, "technology").await;
        assert_eq!(first_headers["x-intel-view-cache"], "miss");
        assert_eq!(st.view_computes.load(Ordering::SeqCst), 1);

        // Nothing changed, so the second call must not recompute.
        let (second_headers, second) = do_view_with_headers(&st, "technology").await;
        assert_eq!(second_headers["x-intel-view-cache"], "hit");
        assert_eq!(
            first_headers["x-intel-view-generation"],
            second_headers["x-intel-view-generation"]
        );
        assert_eq!(
            st.view_computes.load(Ordering::SeqCst),
            1,
            "cache was not used"
        );
        assert_eq!(first.documents_analyzed, second.documents_analyzed);

        // A different sector set is a different question: it computes.
        do_view(&st, "finance").await;
        assert_eq!(st.view_computes.load(Ordering::SeqCst), 2);

        // An ingest that adds documents invalidates the cache...
        let ing = do_ingest(&st, &["finance"], None).await;
        assert!(ing.new > 0);
        let after = do_view(&st, "finance").await;
        assert_eq!(
            st.view_computes.load(Ordering::SeqCst),
            3,
            "stale view served"
        );
        assert!(after.documents_analyzed > 0);
    }

    #[tokio::test]
    async fn view_diagnostic_headers_cover_startup_and_request_stages() {
        let st = test_state();
        do_ingest(&st, &["technology"], None).await;
        let response = view(
            State(st),
            HeaderMap::new(),
            Query(SectorsQ {
                sectors: "technology".to_string(),
            }),
        )
        .await
        .expect("view ok")
        .into_response();

        for name in [
            "x-intel-view-stage-process-main-to-listener-ready-us",
            "x-intel-view-stage-store-open-us",
            "x-intel-view-stage-store-schema-fts-us",
            "x-intel-view-stage-store-cursor-migration-us",
            "x-intel-view-stage-store-fingerprint-backfill-us",
            "x-intel-view-stage-sector-load-us",
            "x-intel-view-stage-analysis-us",
            "x-intel-view-stage-response-build-us",
            "x-intel-view-stage-serialization-us",
            "x-intel-view-stage-handler-total-us",
        ] {
            assert!(
                response.headers().get(name).is_some(),
                "missing diagnostic header {name}"
            );
        }
        assert_eq!(response.headers()["content-type"], "application/json");
    }

    #[tokio::test]
    async fn a_no_op_ingest_does_not_invalidate_the_cache() {
        let st = test_state();
        do_ingest(&st, &["technology"], None).await;
        do_view(&st, "technology").await;
        assert_eq!(st.view_computes.load(Ordering::SeqCst), 1);

        // Re-ingesting the same fixtures adds nothing (+0 new), so the view
        // cannot have changed and the cached answer is still correct.
        let again = do_ingest(&st, &["technology"], None).await;
        assert_eq!(again.new, 0);
        do_view(&st, "technology").await;
        assert_eq!(st.view_computes.load(Ordering::SeqCst), 1);
    }

    #[tokio::test]
    async fn view_cache_is_bounded_and_unknown_sectors_do_not_enter_it() {
        let st = empty_sector_state(300);

        for index in 0..300 {
            do_view(&st, &format!("sector-{index:03}")).await;
            assert!(
                st.view_cache.lock().unwrap().len() <= VIEW_CACHE_CAPACITY,
                "view cache exceeded its declared bound"
            );
        }
        assert_eq!(st.view_cache.lock().unwrap().len(), VIEW_CACHE_CAPACITY);

        // The newest valid entry survived eviction and remains a cache hit.
        let computes = st.view_computes.load(Ordering::SeqCst);
        do_view(&st, "sector-299").await;
        assert_eq!(st.view_computes.load(Ordering::SeqCst), computes);

        let cached = st.view_cache.lock().unwrap().len();
        for index in 0..50 {
            do_view(&st, &format!("nonexistent-{index:02}")).await;
        }
        assert_eq!(
            st.view_cache.lock().unwrap().len(),
            cached,
            "unknown sectors must not create cache entries"
        );
    }
}
