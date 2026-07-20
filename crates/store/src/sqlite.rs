//! SqliteStore: the archive grows up.
//!
//! SQLite is a deliberate choice here, not a compromise: it is embedded
//! (no external service to run, matching the platform's no-gatekeeper
//! ethos), transactional, and FTS5 provides genuine BM25-ranked full-text
//! search. For a single-node product this is production-legitimate.
//!
//! The scale-up path, behind this same method surface:
//! - Postgres via `sqlx` when multi-writer / multi-node arrives;
//! - `pgvector` for embedding columns (semantic retrieval + RAG over the
//!   archive) — add an `embedding BLOB` column here first if you want to
//!   prototype with brute-force cosine before the Postgres move;
//! - `tantivy` if search volume outgrows FTS5.
//!
//! Notes:
//! - ingestion is append-only (INSERT OR IGNORE on id), which is what makes a
//!   re-run idempotent. Editing and deletion exist for corrections/takedowns
//!   (`update_document`, `delete_document`) and the FTS index follows them via
//!   AFTER UPDATE/DELETE triggers — an external-content FTS5 table will not do
//!   that by itself.
//! - `signals_history` records what was reported to whom and when — the
//!   audit trail of the product's own claims, and the raw material for
//!   "how did this signal evolve" features later.

use intel_core::{Day, Document, License, Provenance, SectorId, Signal, SourceKind};
use rusqlite::{params, Connection};
use std::path::Path;
use std::sync::Mutex;

const SCHEMA: &str = r#"
CREATE TABLE IF NOT EXISTS documents (
    id            TEXT PRIMARY KEY,
    sector        TEXT NOT NULL,
    url           TEXT,
    title         TEXT NOT NULL,
    body          TEXT NOT NULL,
    published_day INTEGER,
    published_raw TEXT,
    authors       TEXT NOT NULL,
    tags          TEXT NOT NULL,
    source_id     TEXT NOT NULL,
    retrieved_from TEXT NOT NULL,
    source_kind   TEXT NOT NULL,
    license       TEXT NOT NULL,
    -- SimHash fingerprint, computed once at ingest instead of re-derived on
    -- every /view and /retrieve request. Stored as INTEGER (u64 bit-cast).
    simhash       INTEGER,
    -- The document this one collapses to under near-dup detection. A document
    -- that is nobody's duplicate is its own canonical id, so `canonical_id` is
    -- always set and `canonical_id = id` means "this is the original". (T9.1)
    canonical_id  TEXT
);
CREATE INDEX IF NOT EXISTS idx_documents_sector ON documents(sector);
CREATE INDEX IF NOT EXISTS idx_documents_canonical ON documents(canonical_id);

CREATE VIRTUAL TABLE IF NOT EXISTS documents_fts USING fts5(
    title, body, content='documents', content_rowid='rowid'
);
CREATE TRIGGER IF NOT EXISTS documents_ai AFTER INSERT ON documents BEGIN
    INSERT INTO documents_fts(rowid, title, body)
    VALUES (new.rowid, new.title, new.body);
END;
-- An external-content FTS5 index does NOT follow its content table on its own:
-- the index must be told to forget the old terms, using the 'delete' command
-- with the OLD column values. Without these two triggers an edited document
-- stays findable under text it no longer contains, and a deleted one stays
-- findable at all — the index quietly diverges from the archive. (T9.5)
CREATE TRIGGER IF NOT EXISTS documents_ad AFTER DELETE ON documents BEGIN
    INSERT INTO documents_fts(documents_fts, rowid, title, body)
    VALUES ('delete', old.rowid, old.title, old.body);
END;
CREATE TRIGGER IF NOT EXISTS documents_au AFTER UPDATE ON documents BEGIN
    INSERT INTO documents_fts(documents_fts, rowid, title, body)
    VALUES ('delete', old.rowid, old.title, old.body);
    INSERT INTO documents_fts(rowid, title, body)
    VALUES (new.rowid, new.title, new.body);
END;

CREATE TABLE IF NOT EXISTS embeddings (
    doc_id TEXT NOT NULL,
    model  TEXT NOT NULL,
    dim    INTEGER NOT NULL,
    vec    BLOB NOT NULL,
    PRIMARY KEY (doc_id, model)
);

CREATE TABLE IF NOT EXISTS signals_history (
    client      TEXT NOT NULL,
    window_end  INTEGER,
    kind        TEXT NOT NULL,
    headline    TEXT NOT NULL,
    score       REAL NOT NULL,
    detail      TEXT NOT NULL,
    evidence    TEXT NOT NULL,
    created_at  TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Harvest cursors for incremental, resumable ingestion (OAI-PMH and any
-- other paged/incremental source). `cursor` is the in-flight resumptionToken
-- (NULL when idle/complete); `high_water` is the max datestamp of the last
-- completed harvest, replayed as `from=` on the next run.
CREATE TABLE IF NOT EXISTS cursors (
    source_id  TEXT PRIMARY KEY,
    cursor     TEXT,
    high_water TEXT,
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);
"#;

pub struct SqliteStore {
    // rusqlite::Connection is !Sync; a Mutex makes the store shareable from
    // async handlers. Queries here are short and never held across awaits.
    // Production: a connection pool (r2d2/deadpool) or sqlx.
    conn: Mutex<Connection>,
}

#[derive(Debug)]
pub struct SearchHit {
    pub doc_id: String,
    pub title: String,
    pub sector: String,
    pub source_id: String,
    pub url: Option<String>,
    pub license: License,
    /// BM25-highlighted body snippet — populated ONLY when the source
    /// license permits redistribution. The gate lives in the store so no
    /// caller can forget it.
    pub snippet: Option<String>,
    pub rank: f64,
}

impl SqliteStore {
    pub fn open(path: &Path) -> rusqlite::Result<Self> {
        if let Some(dir) = path.parent() {
            let _ = std::fs::create_dir_all(dir);
        }
        let conn = Connection::open(path)?;
        conn.execute_batch(SCHEMA)?;
        Ok(Self {
            conn: Mutex::new(conn),
        })
    }

    /// Idempotent append: returns how many documents were genuinely new.
    pub fn append_new(&self, docs: &[Document]) -> rusqlite::Result<usize> {
        let mut conn = self.conn.lock().unwrap();
        let tx = conn.transaction()?;
        let mut n = 0;
        for d in docs {
            n += tx.execute(
                "INSERT OR IGNORE INTO documents
                 (id, sector, url, title, body, published_day, published_raw,
                  authors, tags, source_id, retrieved_from, source_kind, license,
                  simhash, canonical_id)
                 VALUES (?1,?2,?3,?4,?5,?6,?7,?8,?9,?10,?11,?12,?13,?14,?1)",
                params![
                    d.id,
                    d.sector.0,
                    d.url,
                    d.title,
                    d.body,
                    d.published_day.map(|x| x.0),
                    d.published_raw,
                    serde_json::to_string(&d.authors).unwrap_or_default(),
                    serde_json::to_string(&d.tags).unwrap_or_default(),
                    d.provenance.source_id,
                    d.provenance.retrieved_from,
                    d.provenance.kind.as_str(),
                    d.provenance.license.as_str(),
                    // Fingerprint once, here, rather than on every request.
                    // A fresh document starts out as its own canonical (?1);
                    // `assign_canonical_ids` then collapses near-dups.
                    fingerprint_of(d) as i64,
                ],
            )?;
        }
        tx.commit()?;
        Ok(n)
    }

    pub fn load_all(&self) -> rusqlite::Result<Vec<Document>> {
        let conn = self.conn.lock().unwrap();
        let mut stmt = conn.prepare(
            "SELECT id, sector, url, title, body, published_day, published_raw,
                    authors, tags, source_id, retrieved_from, source_kind, license
             FROM documents",
        )?;
        let rows = stmt.query_map([], row_to_document)?;
        rows.collect()
    }

    pub fn count(&self) -> rusqlite::Result<usize> {
        let conn = self.conn.lock().unwrap();
        conn.query_row("SELECT COUNT(*) FROM documents", [], |r| r.get::<_, i64>(0))
            .map(|n| n as usize)
    }

    /// BM25-ranked full-text search, entitlement-filtered in SQL.
    /// Invalid FTS syntax surfaces as an Err for callers to map to 400.
    pub fn search(
        &self,
        query: &str,
        sectors: &[String],
        limit: usize,
    ) -> rusqlite::Result<Vec<SearchHit>> {
        if sectors.is_empty() {
            return Ok(Vec::new());
        }
        let conn = self.conn.lock().unwrap();
        let placeholders = sectors.iter().map(|_| "?").collect::<Vec<_>>().join(",");
        let sql = format!(
            "SELECT d.id, d.title, d.sector, d.source_id, d.url, d.license,
                    snippet(documents_fts, 1, '[', ']', ' ... ', 12),
                    bm25(documents_fts)
             FROM documents_fts
             JOIN documents d ON d.rowid = documents_fts.rowid
             WHERE documents_fts MATCH ?1 AND d.sector IN ({placeholders})
             ORDER BY bm25(documents_fts)
             LIMIT {limit}"
        );
        let mut stmt = conn.prepare(&sql)?;
        let mut bind: Vec<&dyn rusqlite::ToSql> = vec![&query];
        for s in sectors {
            bind.push(s);
        }
        let rows = stmt.query_map(bind.as_slice(), |r| {
            let license = License::parse(&r.get::<_, String>(5)?).unwrap_or(License::IndexOnly);
            let raw_snippet: String = r.get(6)?;
            Ok(SearchHit {
                doc_id: r.get(0)?,
                title: r.get(1)?,
                sector: r.get(2)?,
                source_id: r.get(3)?,
                url: r.get(4)?,
                license,
                snippet: if license.redistributable() {
                    Some(raw_snippet)
                } else {
                    None
                },
                rank: r.get(7)?,
            })
        })?;
        rows.collect()
    }

    /// Records what was reported to a client — the platform's audit trail.
    pub fn record_signals(
        &self,
        client: &str,
        window_end: Option<Day>,
        signals: &[Signal],
    ) -> rusqlite::Result<()> {
        let mut conn = self.conn.lock().unwrap();
        let tx = conn.transaction()?;
        for s in signals {
            tx.execute(
                "INSERT INTO signals_history
                 (client, window_end, kind, headline, score, detail, evidence)
                 VALUES (?1,?2,?3,?4,?5,?6,?7)",
                params![
                    client,
                    window_end.map(|d| d.0),
                    format!("{:?}", s.kind),
                    s.headline,
                    s.score,
                    s.detail,
                    serde_json::to_string(&s.evidence).unwrap_or_default(),
                ],
            )?;
        }
        tx.commit()?;
        Ok(())
    }

    pub fn signals_recorded(&self) -> rusqlite::Result<usize> {
        let conn = self.conn.lock().unwrap();
        conn.query_row("SELECT COUNT(*) FROM signals_history", [], |r| {
            r.get::<_, i64>(0)
        })
        .map(|n| n as usize)
    }

    /// Rewrite an existing document's content in place (matched by id), keeping
    /// the FTS index in step via the AFTER UPDATE trigger. Returns false if no
    /// such document exists.
    ///
    /// A plain `UPDATE` is used rather than `INSERT OR REPLACE` on purpose:
    /// REPLACE only fires DELETE triggers when `recursive_triggers` is on, so
    /// it would silently leave the old terms in the index on a default
    /// connection. This is exactly the kind of quiet divergence T9.5 is about.
    pub fn update_document(&self, doc: &Document) -> rusqlite::Result<bool> {
        let conn = self.conn.lock().unwrap();
        let n = conn.execute(
            "UPDATE documents SET
                 sector = ?2, url = ?3, title = ?4, body = ?5,
                 published_day = ?6, published_raw = ?7, authors = ?8, tags = ?9,
                 source_id = ?10, retrieved_from = ?11, source_kind = ?12, license = ?13
             WHERE id = ?1",
            params![
                doc.id,
                doc.sector.0,
                doc.url,
                doc.title,
                doc.body,
                doc.published_day.map(|x| x.0),
                doc.published_raw,
                serde_json::to_string(&doc.authors).unwrap_or_default(),
                serde_json::to_string(&doc.tags).unwrap_or_default(),
                doc.provenance.source_id,
                doc.provenance.retrieved_from,
                doc.provenance.kind.as_str(),
                doc.provenance.license.as_str(),
            ],
        )?;
        Ok(n > 0)
    }

    /// Remove a document and its embeddings; the AFTER DELETE trigger evicts it
    /// from the search index. Returns false if it wasn't there.
    pub fn delete_document(&self, id: &str) -> rusqlite::Result<bool> {
        let mut conn = self.conn.lock().unwrap();
        let tx = conn.transaction()?;
        tx.execute("DELETE FROM embeddings WHERE doc_id = ?1", params![id])?;
        let n = tx.execute("DELETE FROM documents WHERE id = ?1", params![id])?;
        tx.commit()?;
        Ok(n > 0)
    }
}

/// The text a document is fingerprinted on — title + body, exactly as the
/// analysis-time dedup does it, so the persisted fingerprint and the computed
/// one can never disagree.
fn fingerprint_of(d: &Document) -> u64 {
    intel_extract::simhash(&format!("{} {}", d.title, d.body))
}

impl SqliteStore {
    /// Every document's persisted fingerprint, by id.
    pub fn fingerprints(&self) -> rusqlite::Result<std::collections::HashMap<String, u64>> {
        let conn = self.conn.lock().unwrap();
        let mut stmt =
            conn.prepare("SELECT id, simhash FROM documents WHERE simhash IS NOT NULL")?;
        let rows = stmt.query_map([], |r| {
            Ok((r.get::<_, String>(0)?, r.get::<_, i64>(1)? as u64))
        })?;
        rows.collect()
    }

    /// Collapse near-duplicates onto a canonical id, persistently.
    ///
    /// Deliberately a *materialization of the existing global rule*, not an
    /// incremental first-seen-wins assignment. `dedup_near` keeps the earliest
    /// document by `(published_day, id)` — a property of the corpus, not of the
    /// order things happened to arrive in. Assigning canonical ids at insert
    /// time would instead let ingest order decide the winner, and since T3 gave
    /// every source its own clock, that order is now genuinely variable: the
    /// same 13 documents could canonicalize differently between two runs. So
    /// the assignment is recomputed over the corpus whenever it changes, which
    /// keeps it a deterministic function of content.
    ///
    /// Scoped per sector, because that is the only scope in which two documents
    /// are ever compared.
    pub fn assign_canonical_ids(&self, max_distance: u32) -> rusqlite::Result<usize> {
        let mut conn = self.conn.lock().unwrap();
        let tx = conn.transaction()?;

        // (sector, published_day, id, simhash), in the dedup's own order.
        let rows: Vec<(String, Option<i64>, String, u64)> = {
            let mut stmt = tx.prepare(
                "SELECT sector, published_day, id, simhash FROM documents
                 WHERE simhash IS NOT NULL
                 ORDER BY sector, published_day, id",
            )?;
            let it = stmt.query_map([], |r| {
                Ok((
                    r.get::<_, String>(0)?,
                    r.get::<_, Option<i64>>(1)?,
                    r.get::<_, String>(2)?,
                    r.get::<_, i64>(3)? as u64,
                ))
            })?;
            it.collect::<rusqlite::Result<Vec<_>>>()?
        };

        let mut assignments: Vec<(String, String)> = Vec::new(); // (id, canonical_id)
        let mut sector = String::new();
        let mut kept: Vec<(u64, String)> = Vec::new();
        for (sec, _day, id, fp) in rows {
            if sec != sector {
                sector = sec;
                kept.clear();
            }
            match kept
                .iter()
                .find(|(kfp, _)| intel_extract::hamming(*kfp, fp) <= max_distance)
            {
                Some((_, canonical)) => assignments.push((id, canonical.clone())),
                None => {
                    kept.push((fp, id.clone()));
                    assignments.push((id.clone(), id)); // its own canonical
                }
            }
        }

        let mut changed = 0usize;
        for (id, canonical) in &assignments {
            changed += tx.execute(
                "UPDATE documents SET canonical_id = ?2
                 WHERE id = ?1 AND (canonical_id IS NULL OR canonical_id <> ?2)",
                params![id, canonical],
            )?;
        }
        tx.commit()?;
        Ok(changed)
    }

    /// What a document collapses to. A document that is nobody's duplicate is
    /// its own canonical id.
    pub fn canonical_id(&self, id: &str) -> rusqlite::Result<Option<String>> {
        let conn = self.conn.lock().unwrap();
        match conn.query_row(
            "SELECT canonical_id FROM documents WHERE id = ?1",
            [id],
            |r| r.get::<_, Option<String>>(0),
        ) {
            Ok(c) => Ok(c),
            Err(rusqlite::Error::QueryReturnedNoRows) => Ok(None),
            Err(e) => Err(e),
        }
    }

    /// Documents that were collapsed onto some other document, as
    /// (duplicate_id, canonical_id) pairs.
    pub fn duplicates(&self) -> rusqlite::Result<Vec<(String, String)>> {
        let conn = self.conn.lock().unwrap();
        let mut stmt = conn.prepare(
            "SELECT id, canonical_id FROM documents
             WHERE canonical_id IS NOT NULL AND canonical_id <> id
             ORDER BY id",
        )?;
        let rows = stmt.query_map([], |r| Ok((r.get(0)?, r.get(1)?)))?;
        rows.collect()
    }
}

/// A harvest cursor: what a resumable/incremental source needs to remember
/// between runs. `cursor` is the in-flight resumptionToken (None when the last
/// harvest finished cleanly); `high_water` is the max datestamp seen by the
/// last completed harvest.
#[derive(Debug, Clone, Default, PartialEq, Eq)]
pub struct Cursor {
    pub source_id: String,
    pub cursor: Option<String>,
    pub high_water: Option<String>,
    pub updated_at: Option<String>,
}

impl SqliteStore {
    /// Read a source's cursor, or None if it has never harvested.
    pub fn get_cursor(&self, source_id: &str) -> rusqlite::Result<Option<Cursor>> {
        let conn = self.conn.lock().unwrap();
        let row = conn
            .query_row(
                "SELECT source_id, cursor, high_water, updated_at
                 FROM cursors WHERE source_id = ?1",
                [source_id],
                |r| {
                    Ok(Cursor {
                        source_id: r.get(0)?,
                        cursor: r.get(1)?,
                        high_water: r.get(2)?,
                        updated_at: r.get(3)?,
                    })
                },
            )
            .map(Some);
        match row {
            Ok(c) => Ok(c),
            Err(rusqlite::Error::QueryReturnedNoRows) => Ok(None),
            Err(e) => Err(e),
        }
    }

    /// Checkpoint an in-flight resumptionToken mid-harvest (`None` clears it),
    /// preserving any existing high-water mark. Called after each page so an
    /// interrupted harvest can resume from exactly where it stopped.
    pub fn set_cursor_token(&self, source_id: &str, token: Option<&str>) -> rusqlite::Result<()> {
        let conn = self.conn.lock().unwrap();
        conn.execute(
            "INSERT INTO cursors (source_id, cursor, high_water, updated_at)
             VALUES (?1, ?2, NULL, datetime('now'))
             ON CONFLICT(source_id) DO UPDATE SET
                 cursor = excluded.cursor,
                 updated_at = datetime('now')",
            params![source_id, token],
        )?;
        Ok(())
    }

    /// Mark a harvest complete: clear the in-flight token and advance the
    /// high-water mark to `max(existing, new)`. Datestamps are ISO
    /// (YYYY-MM-DD), so lexicographic max is chronological max.
    pub fn complete_cursor(
        &self,
        source_id: &str,
        high_water: Option<&str>,
    ) -> rusqlite::Result<()> {
        let existing = self.get_cursor(source_id)?.and_then(|c| c.high_water);
        let advanced = match (existing.as_deref(), high_water) {
            (Some(old), Some(new)) => {
                if new > old {
                    Some(new)
                } else {
                    Some(old)
                }
            }
            (Some(old), None) => Some(old),
            (None, new) => new,
        };
        let conn = self.conn.lock().unwrap();
        conn.execute(
            "INSERT INTO cursors (source_id, cursor, high_water, updated_at)
             VALUES (?1, NULL, ?2, datetime('now'))
             ON CONFLICT(source_id) DO UPDATE SET
                 cursor = NULL,
                 high_water = excluded.high_water,
                 updated_at = datetime('now')",
            params![source_id, advanced],
        )?;
        Ok(())
    }
}

fn row_to_document(r: &rusqlite::Row<'_>) -> rusqlite::Result<Document> {
    let authors: Vec<String> = serde_json::from_str(&r.get::<_, String>(7)?).unwrap_or_default();
    let tags: Vec<String> = serde_json::from_str(&r.get::<_, String>(8)?).unwrap_or_default();
    Ok(Document {
        id: r.get(0)?,
        sector: SectorId(r.get(1)?),
        url: r.get(2)?,
        title: r.get(3)?,
        body: r.get(4)?,
        published_day: r.get::<_, Option<i64>>(5)?.map(Day),
        published_raw: r.get(6)?,
        authors,
        tags,
        provenance: Provenance {
            source_id: r.get(9)?,
            retrieved_from: r.get(10)?,
            kind: SourceKind::parse(&r.get::<_, String>(11)?).unwrap_or(SourceKind::Rss),
            license: License::parse(&r.get::<_, String>(12)?).unwrap_or(License::IndexOnly),
        },
    })
}

// --- vector layer -------------------------------------------------------------
//
// Brute-force cosine over BLOB-encoded f32 vectors: exact and instant at
// thousands of documents. The scale-up is pgvector (HNSW/IVFFlat) behind
// these same three methods — callers never learn the difference.

impl SqliteStore {
    /// Documents that have no embedding yet for the given model — the
    /// backfill work queue.
    pub fn docs_missing_embeddings(&self, model: &str) -> rusqlite::Result<Vec<Document>> {
        let conn = self.conn.lock().unwrap();
        let mut stmt = conn.prepare(
            "SELECT d.id, d.sector, d.url, d.title, d.body, d.published_day,
                    d.published_raw, d.authors, d.tags, d.source_id,
                    d.retrieved_from, d.source_kind, d.license
             FROM documents d
             LEFT JOIN embeddings e ON e.doc_id = d.id AND e.model = ?1
             WHERE e.doc_id IS NULL",
        )?;
        let rows = stmt.query_map([model], row_to_document)?;
        rows.collect()
    }

    pub fn upsert_embeddings(
        &self,
        model: &str,
        items: &[(String, Vec<f32>)],
    ) -> rusqlite::Result<usize> {
        let mut conn = self.conn.lock().unwrap();
        let tx = conn.transaction()?;
        let mut n = 0;
        for (doc_id, vec) in items {
            n += tx.execute(
                "INSERT OR REPLACE INTO embeddings (doc_id, model, dim, vec)
                 VALUES (?1, ?2, ?3, ?4)",
                params![doc_id, model, vec.len() as i64, vec_to_blob(vec)],
            )?;
        }
        tx.commit()?;
        Ok(n)
    }

    pub fn embeddings_count(&self, model: &str) -> rusqlite::Result<usize> {
        let conn = self.conn.lock().unwrap();
        conn.query_row(
            "SELECT COUNT(*) FROM embeddings WHERE model = ?1",
            [model],
            |r| r.get::<_, i64>(0),
        )
        .map(|n| n as usize)
    }

    /// Cosine-ranked nearest documents, entitlement-filtered in SQL.
    pub fn vector_search(
        &self,
        model: &str,
        query: &[f32],
        sectors: &[String],
        limit: usize,
    ) -> rusqlite::Result<Vec<(String, f64)>> {
        if sectors.is_empty() || query.is_empty() {
            return Ok(Vec::new());
        }
        let conn = self.conn.lock().unwrap();
        let placeholders = sectors.iter().map(|_| "?").collect::<Vec<_>>().join(",");
        let sql = format!(
            "SELECT e.doc_id, e.vec FROM embeddings e
             JOIN documents d ON d.id = e.doc_id
             WHERE e.model = ?1 AND d.sector IN ({placeholders})"
        );
        let mut stmt = conn.prepare(&sql)?;
        let model_owned = model.to_string();
        let mut bind: Vec<&dyn rusqlite::ToSql> = vec![&model_owned];
        for s in sectors {
            bind.push(s);
        }
        let rows = stmt.query_map(bind.as_slice(), |r| {
            Ok((r.get::<_, String>(0)?, r.get::<_, Vec<u8>>(1)?))
        })?;
        let mut scored: Vec<(String, f64)> = Vec::new();
        for row in rows {
            let (doc_id, blob) = row?;
            let v = blob_to_vec(&blob);
            scored.push((doc_id, cosine(query, &v)));
        }
        scored.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap_or(std::cmp::Ordering::Equal));
        scored.truncate(limit);
        Ok(scored)
    }
}

fn vec_to_blob(v: &[f32]) -> Vec<u8> {
    let mut out = Vec::with_capacity(v.len() * 4);
    for x in v {
        out.extend_from_slice(&x.to_le_bytes());
    }
    out
}

fn blob_to_vec(b: &[u8]) -> Vec<f32> {
    b.chunks_exact(4)
        .map(|c| f32::from_le_bytes([c[0], c[1], c[2], c[3]]))
        .collect()
}

fn cosine(a: &[f32], b: &[f32]) -> f64 {
    if a.len() != b.len() || a.is_empty() {
        return 0.0;
    }
    let (mut dot, mut na, mut nb) = (0.0f64, 0.0f64, 0.0f64);
    for i in 0..a.len() {
        dot += a[i] as f64 * b[i] as f64;
        na += (a[i] as f64).powi(2);
        nb += (b[i] as f64).powi(2);
    }
    if na == 0.0 || nb == 0.0 {
        0.0
    } else {
        dot / (na.sqrt() * nb.sqrt())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn tmp_store() -> SqliteStore {
        use std::sync::atomic::{AtomicU64, Ordering};
        static SEQ: AtomicU64 = AtomicU64::new(0);
        let seq = SEQ.fetch_add(1, Ordering::Relaxed);
        let n = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .unwrap()
            .as_nanos();
        let pid = std::process::id();
        let path = std::env::temp_dir().join(format!("intel-store-{pid}-{seq}-{n}.db"));
        SqliteStore::open(&path).unwrap()
    }

    #[test]
    fn cursor_absent_then_checkpoint_then_complete() {
        let s = tmp_store();
        assert_eq!(s.get_cursor("arxiv-cs").unwrap(), None);

        // Mid-harvest checkpoint of a resumptionToken.
        s.set_cursor_token("arxiv-cs", Some("tok-page2")).unwrap();
        let c = s.get_cursor("arxiv-cs").unwrap().unwrap();
        assert_eq!(c.cursor.as_deref(), Some("tok-page2"));
        assert_eq!(c.high_water, None);

        // Completing clears the token and records the high-water mark.
        s.complete_cursor("arxiv-cs", Some("2026-07-04")).unwrap();
        let c = s.get_cursor("arxiv-cs").unwrap().unwrap();
        assert_eq!(c.cursor, None);
        assert_eq!(c.high_water.as_deref(), Some("2026-07-04"));
    }

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
                source_id: "techwire".into(),
                retrieved_from: "fixture".into(),
                kind: SourceKind::Rss,
                license: License::CcBy,
            },
        }
    }

    fn hits(s: &SqliteStore, q: &str) -> usize {
        s.search(q, &["technology".to_string()], 10).unwrap().len()
    }

    // T9.5: an external-content FTS index does not follow its table on its own.
    #[test]
    fn edited_document_is_searchable_under_new_text_only() {
        let s = tmp_store();
        s.append_new(&[doc("d1", "Original", "quantum widgets everywhere")])
            .unwrap();
        assert_eq!(hits(&s, "quantum"), 1);

        assert!(s
            .update_document(&doc("d1", "Revised", "photonic gizmos instead"))
            .unwrap());

        // The old term is gone from the index...
        assert_eq!(hits(&s, "quantum"), 0);
        // ...and the new one is present.
        assert_eq!(hits(&s, "photonic"), 1);
        // The archive itself agrees.
        assert_eq!(s.count().unwrap(), 1);
    }

    #[test]
    fn deleted_document_leaves_the_index() {
        let s = tmp_store();
        s.append_new(&[doc("d1", "T", "quantum widgets")]).unwrap();
        assert_eq!(hits(&s, "quantum"), 1);

        assert!(s.delete_document("d1").unwrap());
        assert_eq!(hits(&s, "quantum"), 0);
        assert_eq!(s.count().unwrap(), 0);
        // Deleting something absent is a clean false, not an error.
        assert!(!s.delete_document("d1").unwrap());
    }

    #[test]
    fn updating_an_absent_document_is_a_clean_false() {
        let s = tmp_store();
        assert!(!s.update_document(&doc("ghost", "t", "b")).unwrap());
    }

    // --- T9.1: persisted fingerprints + canonical ids -----------------------

    fn dup_doc(id: &str, day: &str, body: &str) -> Document {
        let mut d = doc(id, "Shared headline about DeepSeek V4", body);
        d.published_day = Day::parse_iso(day);
        d.published_raw = Some(day.to_string());
        d
    }

    // The near-dup pair from the real fixtures: a syndicated copy of the same
    // story, published the same day by two different outlets.
    const ORIGINAL: &str = "DeepSeek said researchers can request the V4 Pro \
        checkpoints starting today. Early adopters are serving the release \
        through vLLM at launch.";
    const SYNDICATED: &str = "Syndicated: DeepSeek said researchers can request \
        the V4 Pro checkpoints starting today. Early adopters are serving the \
        release through vLLM at launch.";

    #[test]
    fn duplicate_ingest_maps_to_one_canonical_id() {
        let s = tmp_store();
        s.append_new(&[
            dup_doc("osdaily::osd-004", "2026-07-04", ORIGINAL),
            dup_doc("techwire::tw-004", "2026-07-04", SYNDICATED),
        ])
        .unwrap();
        s.assign_canonical_ids(16).unwrap();

        // Both collapse onto ONE canonical id — the earliest by (day, id), which
        // for a same-day pair is the lexicographically smaller: osdaily.
        assert_eq!(
            s.canonical_id("osdaily::osd-004").unwrap().as_deref(),
            Some("osdaily::osd-004")
        );
        assert_eq!(
            s.canonical_id("techwire::tw-004").unwrap().as_deref(),
            Some("osdaily::osd-004")
        );
        assert_eq!(
            s.duplicates().unwrap(),
            vec![(
                "techwire::tw-004".to_string(),
                "osdaily::osd-004".to_string()
            )]
        );
        // Both documents are still IN the archive — canonicalization is an
        // identity, not a deletion.
        assert_eq!(s.count().unwrap(), 2);
    }

    /// The property that forced this to be a recomputed materialization rather
    /// than a first-seen-wins assignment at insert: after T3 gave each source
    /// its own clock, ingest order is variable, and the answer must not be.
    #[test]
    fn canonical_assignment_does_not_depend_on_ingest_order() {
        let a = tmp_store();
        a.append_new(&[dup_doc("techwire::tw-004", "2026-07-04", SYNDICATED)])
            .unwrap();
        a.append_new(&[dup_doc("osdaily::osd-004", "2026-07-04", ORIGINAL)])
            .unwrap();
        a.assign_canonical_ids(16).unwrap();

        let b = tmp_store();
        b.append_new(&[dup_doc("osdaily::osd-004", "2026-07-04", ORIGINAL)])
            .unwrap();
        b.append_new(&[dup_doc("techwire::tw-004", "2026-07-04", SYNDICATED)])
            .unwrap();
        b.assign_canonical_ids(16).unwrap();

        assert_eq!(a.duplicates().unwrap(), b.duplicates().unwrap());
        assert_eq!(
            a.canonical_id("techwire::tw-004").unwrap(),
            b.canonical_id("techwire::tw-004").unwrap()
        );
    }

    #[test]
    fn unrelated_documents_are_their_own_canonical() {
        let s = tmp_store();
        s.append_new(&[
            doc(
                "d1",
                "Sparse mixture of experts routing",
                "memory constraints on accelerators",
            ),
            doc(
                "d2",
                "Coastal salinity trends",
                "twenty years of public buoy measurements",
            ),
        ])
        .unwrap();
        s.assign_canonical_ids(16).unwrap();
        assert_eq!(s.canonical_id("d1").unwrap().as_deref(), Some("d1"));
        assert_eq!(s.canonical_id("d2").unwrap().as_deref(), Some("d2"));
        assert!(s.duplicates().unwrap().is_empty());
    }

    #[test]
    fn fingerprints_are_persisted_at_ingest() {
        let s = tmp_store();
        s.append_new(&[doc("d1", "T", "quantum widgets")]).unwrap();
        let prints = s.fingerprints().unwrap();
        assert_eq!(prints.len(), 1);
        // The stored fingerprint is exactly what the analysis-time dedup uses.
        assert_eq!(prints["d1"], intel_extract::simhash("T quantum widgets"));
    }

    #[test]
    fn high_water_is_monotonic() {
        let s = tmp_store();
        s.complete_cursor("arxiv-cs", Some("2026-07-04")).unwrap();
        // An older datestamp must not roll the mark backward.
        s.complete_cursor("arxiv-cs", Some("2026-07-01")).unwrap();
        assert_eq!(
            s.get_cursor("arxiv-cs")
                .unwrap()
                .unwrap()
                .high_water
                .as_deref(),
            Some("2026-07-04")
        );
        // A newer one advances it.
        s.complete_cursor("arxiv-cs", Some("2026-07-09")).unwrap();
        assert_eq!(
            s.get_cursor("arxiv-cs")
                .unwrap()
                .unwrap()
                .high_water
                .as_deref(),
            Some("2026-07-09")
        );
    }
}
