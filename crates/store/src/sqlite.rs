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
use rusqlite::types::Type;
use rusqlite::{params, Connection, OptionalExtension, Transaction};
use std::path::Path;
use std::sync::Mutex;
use std::time::Instant;

const DEDUP_MAX_DISTANCE: u32 = 16;

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
    -- The document this one collapses to under near-dup detection. The column
    -- remains nullable so legacy archives can be inspected, but every insert
    -- sets it and canonical assignment refuses a missing fingerprint rather
    -- than leaving the id silently NULL. The verifier reports either defect.
    -- `canonical_id = id` means "this is the original". (T9.1/A2)
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
    -- Max datestamp seen in the current paged harvest. It survives a capped
    -- run and is promoted only when the final page commits.
    pending_high_water TEXT,
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);
"#;

fn elapsed_us(started: Instant) -> u64 {
    u64::try_from(started.elapsed().as_micros()).unwrap_or(u64::MAX)
}

pub struct SqliteStore {
    // rusqlite::Connection is !Sync; a Mutex makes the store shareable from
    // async handlers. Queries here are short and never held across awaits.
    // Production: a connection pool (r2d2/deadpool) or sqlx.
    conn: Mutex<Connection>,
}

#[derive(Clone, Copy, Debug, Default)]
pub struct StoreOpenTimings {
    pub total_us: u64,
    pub connection_us: u64,
    pub schema_fts_us: u64,
    pub cursor_migration_us: u64,
    pub fingerprint_backfill_us: u64,
    pub fingerprints_backfilled: usize,
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
        Self::open_with_timings(path).map(|(store, _)| store)
    }

    /// Open the archive and expose startup-only diagnostics without changing
    /// the database contract. `/view` decomposition consumes these timings;
    /// ordinary callers keep using `open`.
    pub fn open_with_timings(path: &Path) -> rusqlite::Result<(Self, StoreOpenTimings)> {
        let total_started = Instant::now();
        if let Some(dir) = path.parent() {
            let _ = std::fs::create_dir_all(dir);
        }

        let connection_started = Instant::now();
        let mut conn = Connection::open(path)?;
        let connection_us = elapsed_us(connection_started);

        let schema_started = Instant::now();
        conn.execute_batch(SCHEMA)?;
        let schema_fts_us = elapsed_us(schema_started);

        let cursor_started = Instant::now();
        migrate_cursor_schema(&conn)?;
        let cursor_migration_us = elapsed_us(cursor_started);

        let backfill_started = Instant::now();
        let fingerprints_backfilled = backfill_simhashes(&mut conn)?;
        let fingerprint_backfill_us = elapsed_us(backfill_started);

        let timings = StoreOpenTimings {
            total_us: elapsed_us(total_started),
            connection_us,
            schema_fts_us,
            cursor_migration_us,
            fingerprint_backfill_us,
            fingerprints_backfilled,
        };
        Ok((
            Self {
                conn: Mutex::new(conn),
            },
            timings,
        ))
    }

    /// Adding documents and rematerializing canonical identity are one durability unit.
    pub fn append_new(&self, docs: &[Document]) -> rusqlite::Result<usize> {
        let mut conn = self.conn.lock().unwrap();
        let tx = conn.transaction()?;
        let n = append_new_tx(&tx, docs)?;
        if n > 0 {
            assign_canonical_ids_tx(&tx, DEDUP_MAX_DISTANCE)?;
        }
        tx.commit()?;
        Ok(n)
    }

    /// Load the whole archive for integrity/export operations and tests.
    ///
    /// Request handlers that answer a sector- or id-scoped question must use
    /// the SQL-filtered methods below rather than materializing every body.
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

    /// Documents paired with the fingerprints persisted at ingest/migration.
    /// A missing value is an error: silently recomputing here would let a
    /// broken migration look healthy and put the hot-path cost back.
    pub fn load_all_with_fingerprints(&self) -> rusqlite::Result<Vec<(Document, u64)>> {
        let conn = self.conn.lock().unwrap();
        let mut stmt = conn.prepare(
            "SELECT id, sector, url, title, body, published_day, published_raw,
                    authors, tags, source_id, retrieved_from, source_kind, license,
                    simhash
             FROM documents",
        )?;
        let rows = stmt.query_map([], |row| {
            let document = row_to_document(row)?;
            let fingerprint = row
                .get::<_, Option<i64>>(13)?
                .ok_or_else(|| missing_fingerprint_error(13, &document.id))?;
            Ok((document, fingerprint as u64))
        })?;
        rows.collect()
    }

    /// Documents in the requested sectors, paired with persisted fingerprints.
    ///
    /// HC2 lives in this SQL predicate. An empty entitlement returns no rows.
    pub fn documents_in_sectors(
        &self,
        sectors: &[String],
    ) -> rusqlite::Result<Vec<(Document, u64)>> {
        if sectors.is_empty() {
            return Ok(Vec::new());
        }
        let conn = self.conn.lock().unwrap();
        let placeholders = sectors.iter().map(|_| "?").collect::<Vec<_>>().join(",");
        let sql = format!(
            "SELECT id, sector, url, title, body, published_day, published_raw,
                    authors, tags, source_id, retrieved_from, source_kind, license,
                    simhash
             FROM documents
             WHERE sector IN ({placeholders})"
        );
        let mut stmt = conn.prepare(&sql)?;
        let mut bind: Vec<&dyn rusqlite::ToSql> = Vec::with_capacity(sectors.len());
        for sector in sectors {
            bind.push(sector);
        }
        let rows = stmt.query_map(bind.as_slice(), |row| {
            let document = row_to_document(row)?;
            let fingerprint = row
                .get::<_, Option<i64>>(13)?
                .ok_or_else(|| missing_fingerprint_error(13, &document.id))?;
            Ok((document, fingerprint as u64))
        })?;
        rows.collect()
    }

    /// Fetch only the named documents. Every id is a bound parameter.
    pub fn documents_by_ids(&self, ids: &[&str]) -> rusqlite::Result<Vec<Document>> {
        if ids.is_empty() {
            return Ok(Vec::new());
        }
        let conn = self.conn.lock().unwrap();
        let placeholders = ids.iter().map(|_| "?").collect::<Vec<_>>().join(",");
        let sql = format!(
            "SELECT id, sector, url, title, body, published_day, published_raw,
                    authors, tags, source_id, retrieved_from, source_kind, license
             FROM documents
             WHERE id IN ({placeholders})"
        );
        let mut stmt = conn.prepare(&sql)?;
        let mut bind: Vec<&dyn rusqlite::ToSql> = Vec::with_capacity(ids.len());
        for id in ids {
            bind.push(id);
        }
        let rows = stmt.query_map(bind.as_slice(), row_to_document)?;
        rows.collect()
    }

    /// Fetch only the named documents in the explicit sector allow-list.
    /// Empty ids or sectors fail closed.
    pub fn documents_by_ids_in_sectors(
        &self,
        ids: &[&str],
        sectors: &[String],
    ) -> rusqlite::Result<Vec<Document>> {
        if ids.is_empty() || sectors.is_empty() {
            return Ok(Vec::new());
        }
        let conn = self.conn.lock().unwrap();
        let id_placeholders = ids.iter().map(|_| "?").collect::<Vec<_>>().join(",");
        let sector_placeholders = sectors.iter().map(|_| "?").collect::<Vec<_>>().join(",");
        let sql = format!(
            "SELECT id, sector, url, title, body, published_day, published_raw,
                    authors, tags, source_id, retrieved_from, source_kind, license
             FROM documents
             WHERE id IN ({id_placeholders})
               AND sector IN ({sector_placeholders})"
        );
        let mut stmt = conn.prepare(&sql)?;
        let mut bind: Vec<&dyn rusqlite::ToSql> = Vec::with_capacity(ids.len() + sectors.len());
        for id in ids {
            bind.push(id);
        }
        for sector in sectors {
            bind.push(sector);
        }
        let rows = stmt.query_map(bind.as_slice(), row_to_document)?;
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
    /// This is a maintenance API, not the ingest hot path. A successful edit
    /// rematerializes canonical identity over the full corpus inside the same
    /// transaction; the corpus-wide cost is the deliberate correctness
    /// tradeoff for corrections that can change content or publication order.
    ///
    /// A plain `UPDATE` is used rather than `INSERT OR REPLACE` on purpose:
    /// REPLACE only fires DELETE triggers when `recursive_triggers` is on, so
    /// it would silently leave the old terms in the index on a default
    /// connection. This is exactly the kind of quiet divergence T9.5 is about.
    pub fn update_document(&self, doc: &Document) -> rusqlite::Result<bool> {
        let mut conn = self.conn.lock().unwrap();
        let tx = conn.transaction()?;
        let n = tx.execute(
            "UPDATE documents SET
                 sector = ?2, url = ?3, title = ?4, body = ?5,
                 published_day = ?6, published_raw = ?7, authors = ?8, tags = ?9,
                 source_id = ?10, retrieved_from = ?11, source_kind = ?12,
                 license = ?13, simhash = ?14
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
                fingerprint_of(doc) as i64,
            ],
        )?;
        if n > 0 {
            assign_canonical_ids_tx(&tx, DEDUP_MAX_DISTANCE)?;
        }
        tx.commit()?;
        Ok(n > 0)
    }

    /// Remove a document and its embeddings; the AFTER DELETE trigger evicts it
    /// from the search index. Returns false if it wasn't there.
    ///
    /// This is likewise a maintenance API, not the ingest hot path. A
    /// successful takedown pays the corpus-wide canonical rematerialization
    /// cost inside its transaction so no survivor can name the deleted row.
    pub fn delete_document(&self, id: &str) -> rusqlite::Result<bool> {
        let mut conn = self.conn.lock().unwrap();
        let tx = conn.transaction()?;
        tx.execute("DELETE FROM embeddings WHERE doc_id = ?1", params![id])?;
        let n = tx.execute("DELETE FROM documents WHERE id = ?1", params![id])?;
        if n > 0 {
            assign_canonical_ids_tx(&tx, DEDUP_MAX_DISTANCE)?;
        }
        tx.commit()?;
        Ok(n > 0)
    }
}

fn append_new_tx(tx: &Transaction<'_>, docs: &[Document]) -> rusqlite::Result<usize> {
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
                // Fingerprint once, here, rather than on every request. A
                // fresh document starts as its own canonical id; the global
                // assignment below rematerializes near-duplicate identity.
                fingerprint_of(d) as i64,
            ],
        )?;
    }
    Ok(n)
}

/// The text a document is fingerprinted on — title + body, exactly as the
/// analysis-time dedup does it, so the persisted fingerprint and the computed
/// one can never disagree.
fn fingerprint_of(d: &Document) -> u64 {
    fingerprint_text(&d.title, &d.body)
}

fn fingerprint_text(title: &str, body: &str) -> u64 {
    intel_extract::simhash(&format!("{title} {body}"))
}

/// Upgrade cursor rows created before interrupted harvests retained their
/// pending datestamp across process restarts.
fn migrate_cursor_schema(conn: &Connection) -> rusqlite::Result<()> {
    let has_pending = conn
        .prepare("PRAGMA table_info(cursors)")?
        .query_map([], |row| row.get::<_, String>(1))?
        .collect::<rusqlite::Result<Vec<_>>>()?
        .iter()
        .any(|name| name == "pending_high_water");
    if !has_pending {
        conn.execute("ALTER TABLE cursors ADD COLUMN pending_high_water TEXT", [])?;
    }
    Ok(())
}

/// Upgrade archives created before the persisted fingerprint column existed,
/// then fill every missing value from the same title+body rule used at ingest.
/// Existing fingerprints and canonical ids are untouched.
fn backfill_simhashes(conn: &mut Connection) -> rusqlite::Result<usize> {
    let has_column = {
        let mut stmt = conn.prepare("PRAGMA table_info(documents)")?;
        let names = stmt.query_map([], |row| row.get::<_, String>(1))?;
        names
            .collect::<rusqlite::Result<Vec<_>>>()?
            .iter()
            .any(|name| name == "simhash")
    };
    if has_column {
        let missing = conn.query_row(
            "SELECT COUNT(*) FROM documents WHERE simhash IS NULL",
            [],
            |row| row.get::<_, i64>(0),
        )?;
        if missing == 0 {
            return Ok(0);
        }
    }

    let tx = conn.transaction()?;
    if !has_column {
        tx.execute("ALTER TABLE documents ADD COLUMN simhash INTEGER", [])?;
    }
    let missing = {
        let mut stmt = tx.prepare("SELECT id, title, body FROM documents WHERE simhash IS NULL")?;
        let rows = stmt.query_map([], |row| {
            Ok((
                row.get::<_, String>(0)?,
                row.get::<_, String>(1)?,
                row.get::<_, String>(2)?,
            ))
        })?;
        rows.collect::<rusqlite::Result<Vec<_>>>()?
    };

    // The external-content FTS trigger listens to every UPDATE, even when only
    // simhash changes. Suspending it avoids deleting/reinserting unchanged text
    // (and makes migration safe for an archive whose FTS index is not populated).
    // DDL is transactional in SQLite, so interruption restores the old trigger.
    tx.execute("DROP TRIGGER IF EXISTS documents_au", [])?;
    for (id, title, body) in &missing {
        tx.execute(
            "UPDATE documents SET simhash = ?2 WHERE id = ?1",
            params![id, fingerprint_text(title, body) as i64],
        )?;
    }
    tx.execute_batch(
        "CREATE TRIGGER documents_au AFTER UPDATE ON documents BEGIN
            INSERT INTO documents_fts(documents_fts, rowid, title, body)
            VALUES ('delete', old.rowid, old.title, old.body);
            INSERT INTO documents_fts(rowid, title, body)
            VALUES (new.rowid, new.title, new.body);
        END;",
    )?;
    tx.commit()?;
    Ok(missing.len())
}

impl SqliteStore {
    /// Document ids whose persisted fingerprint is missing.
    ///
    /// This is an integrity query, not a repair path. Callers that enforce the
    /// persisted-fingerprint invariant can name the exact broken rows.
    pub fn missing_fingerprints(&self) -> rusqlite::Result<Vec<String>> {
        let conn = self.conn.lock().unwrap();
        let mut stmt =
            conn.prepare("SELECT id FROM documents WHERE simhash IS NULL ORDER BY id")?;
        let rows = stmt.query_map([], |r| r.get(0))?;
        rows.collect()
    }

    /// Test-only fault injection for callers that must prove a failed global
    /// rematerialization cannot partially commit a surrounding operation.
    #[cfg(feature = "test-support")]
    #[doc(hidden)]
    pub fn test_clear_fingerprint(&self, id: &str) -> rusqlite::Result<usize> {
        self.conn
            .lock()
            .unwrap()
            .execute("UPDATE documents SET simhash = NULL WHERE id = ?1", [id])
    }

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
        let changed = assign_canonical_ids_tx(&tx, max_distance)?;
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

fn assign_canonical_ids_tx(tx: &Transaction<'_>, max_distance: u32) -> rusqlite::Result<usize> {
    // (sector, published_day, id, simhash), in the dedup's own order.
    let rows: Vec<(String, Option<i64>, String, u64)> = {
        let mut stmt = tx.prepare(
            "SELECT sector, published_day, id, simhash FROM documents
             ORDER BY sector, published_day, id",
        )?;
        let it = stmt.query_map([], |r| {
            let id = r.get::<_, String>(2)?;
            let fingerprint = r
                .get::<_, Option<i64>>(3)?
                .ok_or_else(|| missing_fingerprint_error(3, &id))?;
            Ok((
                r.get::<_, String>(0)?,
                r.get::<_, Option<i64>>(1)?,
                id,
                fingerprint as u64,
            ))
        })?;
        it.collect::<rusqlite::Result<Vec<_>>>()?
    };

    let mut assignments: Vec<(String, String)> = Vec::new();
    let mut sector = String::new();
    let mut kept: Vec<(u64, String)> = Vec::new();
    for (sec, _day, id, fp) in rows {
        if sec != sector {
            sector = sec;
            kept.clear();
        }
        match kept
            .iter()
            .find(|(kept_fp, _)| intel_extract::hamming(*kept_fp, fp) <= max_distance)
        {
            Some((_, canonical)) => assignments.push((id, canonical.clone())),
            None => {
                kept.push((fp, id.clone()));
                assignments.push((id.clone(), id));
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
    Ok(changed)
}

fn missing_fingerprint_error(column: usize, id: &str) -> rusqlite::Error {
    rusqlite::Error::InvalidColumnType(
        column,
        format!(
            "persisted simhash for document '{id}' is NULL; \
             run ./run verify-fingerprints <database>"
        ),
        Type::Null,
    )
}

fn lexical_max(left: Option<&str>, right: Option<&str>) -> Option<String> {
    match (left, right) {
        (Some(a), Some(b)) => Some(if a >= b { a } else { b }.to_string()),
        (Some(a), None) => Some(a.to_string()),
        (None, Some(b)) => Some(b.to_string()),
        (None, None) => None,
    }
}

/// A harvest cursor: what a resumable/incremental source needs to remember
/// between runs. `cursor` is the in-flight resumptionToken (None when the last
/// harvest finished cleanly); `high_water` is the max datestamp seen by the
/// last completed harvest; `pending_high_water` is the max seen so far in the
/// interrupted harvest identified by `cursor`.
#[derive(Debug, Clone, Default, PartialEq, Eq)]
pub struct Cursor {
    pub source_id: String,
    pub cursor: Option<String>,
    pub high_water: Option<String>,
    pub pending_high_water: Option<String>,
    pub updated_at: Option<String>,
}

impl SqliteStore {
    /// Read a source's cursor, or None if it has never harvested.
    pub fn get_cursor(&self, source_id: &str) -> rusqlite::Result<Option<Cursor>> {
        let conn = self.conn.lock().unwrap();
        let row = conn
            .query_row(
                "SELECT source_id, cursor, high_water, pending_high_water, updated_at
                 FROM cursors WHERE source_id = ?1",
                [source_id],
                |r| {
                    Ok(Cursor {
                        source_id: r.get(0)?,
                        cursor: r.get(1)?,
                        high_water: r.get(2)?,
                        pending_high_water: r.get(3)?,
                        updated_at: r.get(4)?,
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

    /// Persist one parsed harvest page as a single durability unit: documents,
    /// global canonical-id materialization, next resumptionToken, and pending
    /// datestamp. If any write fails the transaction rolls back all of them, so
    /// the cursor can never advance past documents that did not land.
    pub fn commit_harvest_page(
        &self,
        source_id: &str,
        docs: &[Document],
        next_token: Option<&str>,
        page_high_water: Option<&str>,
    ) -> rusqlite::Result<usize> {
        let mut conn = self.conn.lock().unwrap();
        let tx = conn.transaction()?;
        let new = append_new_tx(&tx, docs)?;
        if new > 0 {
            assign_canonical_ids_tx(&tx, DEDUP_MAX_DISTANCE)?;
        }

        let existing = tx
            .query_row(
                "SELECT high_water, pending_high_water FROM cursors WHERE source_id = ?1",
                [source_id],
                |row| {
                    Ok((
                        row.get::<_, Option<String>>(0)?,
                        row.get::<_, Option<String>>(1)?,
                    ))
                },
            )
            .optional()?;
        let (completed, pending) = existing.unwrap_or((None, None));
        let pending = lexical_max(pending.as_deref(), page_high_water);
        let (cursor, high_water, pending_high_water) = match next_token {
            Some(token) => (Some(token), completed, pending),
            None => (
                None,
                lexical_max(completed.as_deref(), pending.as_deref()),
                None,
            ),
        };

        tx.execute(
            "INSERT INTO cursors
             (source_id, cursor, high_water, pending_high_water, updated_at)
             VALUES (?1, ?2, ?3, ?4, datetime('now'))
             ON CONFLICT(source_id) DO UPDATE SET
                 cursor = excluded.cursor,
                 high_water = excluded.high_water,
                 pending_high_water = excluded.pending_high_water,
                 updated_at = datetime('now')",
            params![source_id, cursor, high_water, pending_high_water],
        )?;
        tx.commit()?;
        Ok(new)
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

#[derive(Debug)]
pub enum EmbeddingWriteError {
    Database(rusqlite::Error),
    DimensionMismatch {
        model: String,
        existing_dim: usize,
        received_dim: usize,
    },
}

impl std::fmt::Display for EmbeddingWriteError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::Database(error) => error.fmt(f),
            Self::DimensionMismatch {
                model,
                existing_dim,
                received_dim,
            } => write!(
                f,
                "embedding dimension mismatch for model '{model}': \
                 existing dimension {existing_dim}, received {received_dim}"
            ),
        }
    }
}

impl std::error::Error for EmbeddingWriteError {
    fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
        match self {
            Self::Database(error) => Some(error),
            Self::DimensionMismatch { .. } => None,
        }
    }
}

impl From<rusqlite::Error> for EmbeddingWriteError {
    fn from(error: rusqlite::Error) -> Self {
        Self::Database(error)
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct EmbeddingStats {
    pub count: usize,
    pub dim: Option<usize>,
    pub inconsistent_dimensions: bool,
}

#[derive(Debug, Clone, PartialEq)]
pub struct VectorSearchResult {
    pub hits: Vec<(String, f64)>,
    pub dimension_mismatches: usize,
}

impl SqliteStore {
    /// Documents that have no embedding yet for the given model — the
    /// backfill work queue.
    pub fn docs_missing_embeddings(
        &self,
        model: &str,
        sectors: &[String],
    ) -> rusqlite::Result<Vec<Document>> {
        if sectors.is_empty() {
            return Ok(Vec::new());
        }
        let conn = self.conn.lock().unwrap();
        let sector_placeholders = sectors.iter().map(|_| "?").collect::<Vec<_>>().join(",");
        let sql = format!(
            "SELECT d.id, d.sector, d.url, d.title, d.body, d.published_day,
                    d.published_raw, d.authors, d.tags, d.source_id,
                    d.retrieved_from, d.source_kind, d.license
             FROM documents d
             LEFT JOIN embeddings e ON e.doc_id = d.id AND e.model = ?
             WHERE e.doc_id IS NULL
               AND d.sector IN ({sector_placeholders})"
        );
        let mut stmt = conn.prepare(&sql)?;
        let mut bind: Vec<&dyn rusqlite::ToSql> = Vec::with_capacity(1 + sectors.len());
        bind.push(&model);
        for sector in sectors {
            bind.push(sector);
        }
        let rows = stmt.query_map(bind.as_slice(), row_to_document)?;
        rows.collect()
    }

    pub fn upsert_embeddings(
        &self,
        model: &str,
        items: &[(String, Vec<f32>)],
    ) -> Result<usize, EmbeddingWriteError> {
        let mut conn = self.conn.lock().unwrap();
        let tx = conn.transaction()?;
        let mut expected_dim = tx
            .query_row(
                "SELECT dim FROM embeddings WHERE model = ?1 LIMIT 1",
                [model],
                |row| row.get::<_, i64>(0),
            )
            .optional()?
            .map(|dim| dim as usize);
        for (_, vector) in items {
            match expected_dim {
                Some(existing_dim) if vector.len() != existing_dim => {
                    return Err(EmbeddingWriteError::DimensionMismatch {
                        model: model.to_string(),
                        existing_dim,
                        received_dim: vector.len(),
                    });
                }
                None => expected_dim = Some(vector.len()),
                Some(_) => {}
            }
        }

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

    pub fn embeddings_stats(&self, model: &str) -> rusqlite::Result<EmbeddingStats> {
        let conn = self.conn.lock().unwrap();
        let (count, min_dim, max_dim) = conn.query_row(
            "SELECT COUNT(*), MIN(dim), MAX(dim)
             FROM embeddings WHERE model = ?1",
            [model],
            |row| {
                Ok((
                    row.get::<_, i64>(0)?,
                    row.get::<_, Option<i64>>(1)?,
                    row.get::<_, Option<i64>>(2)?,
                ))
            },
        )?;
        let inconsistent_dimensions = min_dim != max_dim;
        Ok(EmbeddingStats {
            count: count as usize,
            dim: if inconsistent_dimensions {
                None
            } else {
                min_dim.map(|dim| dim as usize)
            },
            inconsistent_dimensions,
        })
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
    ) -> rusqlite::Result<VectorSearchResult> {
        if sectors.is_empty() || query.is_empty() {
            return Ok(VectorSearchResult {
                hits: Vec::new(),
                dimension_mismatches: 0,
            });
        }
        let conn = self.conn.lock().unwrap();
        let placeholders = sectors.iter().map(|_| "?").collect::<Vec<_>>().join(",");
        let sql = format!(
            "SELECT e.doc_id, e.dim, e.vec FROM embeddings e
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
            Ok((
                r.get::<_, String>(0)?,
                r.get::<_, i64>(1)?,
                r.get::<_, Vec<u8>>(2)?,
            ))
        })?;
        let mut scored: Vec<(String, f64)> = Vec::new();
        let mut dimension_mismatches = 0;
        for row in rows {
            let (doc_id, recorded_dim, blob) = row?;
            let v = blob_to_vec(&blob);
            if recorded_dim < 0 || recorded_dim as usize != v.len() || v.len() != query.len() {
                dimension_mismatches += 1;
                continue;
            }
            match cosine(query, &v) {
                Some(score) => scored.push((doc_id, score)),
                None => dimension_mismatches += 1,
            }
        }
        scored.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap_or(std::cmp::Ordering::Equal));
        scored.truncate(limit);
        Ok(VectorSearchResult {
            hits: scored,
            dimension_mismatches,
        })
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

fn cosine(a: &[f32], b: &[f32]) -> Option<f64> {
    if a.len() != b.len() || a.is_empty() {
        return None;
    }
    let (mut dot, mut na, mut nb) = (0.0f64, 0.0f64, 0.0f64);
    for i in 0..a.len() {
        dot += a[i] as f64 * b[i] as f64;
        na += (a[i] as f64).powi(2);
        nb += (b[i] as f64).powi(2);
    }
    if na == 0.0 || nb == 0.0 {
        Some(0.0)
    } else {
        Some(dot / (na.sqrt() * nb.sqrt()))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn tmp_path() -> std::path::PathBuf {
        use std::sync::atomic::{AtomicU64, Ordering};
        static SEQ: AtomicU64 = AtomicU64::new(0);
        let seq = SEQ.fetch_add(1, Ordering::Relaxed);
        let n = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .unwrap()
            .as_nanos();
        let pid = std::process::id();
        std::env::temp_dir().join(format!("intel-store-{pid}-{seq}-{n}.db"))
    }

    fn tmp_store() -> SqliteStore {
        SqliteStore::open(&tmp_path()).unwrap()
    }

    #[test]
    fn cursor_absent_then_page_checkpoint_then_completion() {
        let s = tmp_store();
        assert_eq!(s.get_cursor("arxiv-cs").unwrap(), None);

        s.commit_harvest_page("arxiv-cs", &[], Some("tok-page2"), Some("2026-07-02"))
            .unwrap();
        let c = s.get_cursor("arxiv-cs").unwrap().unwrap();
        assert_eq!(c.cursor.as_deref(), Some("tok-page2"));
        assert_eq!(c.high_water, None);
        assert_eq!(c.pending_high_water.as_deref(), Some("2026-07-02"));

        s.commit_harvest_page("arxiv-cs", &[], None, Some("2026-07-04"))
            .unwrap();
        let c = s.get_cursor("arxiv-cs").unwrap().unwrap();
        assert_eq!(c.cursor, None);
        assert_eq!(c.high_water.as_deref(), Some("2026-07-04"));
        assert_eq!(c.pending_high_water, None);
    }

    #[test]
    fn page_documents_and_cursor_roll_back_together() {
        let s = tmp_store();
        s.conn
            .lock()
            .unwrap()
            .execute_batch(
                "CREATE TRIGGER fail_cursor BEFORE INSERT ON cursors
                 BEGIN SELECT RAISE(ABORT, 'injected cursor failure'); END;",
            )
            .unwrap();

        let result = s.commit_harvest_page(
            "arxiv-cs",
            &[doc("page-1", "Original", "quantum widgets everywhere")],
            Some("page-2-token"),
            Some("2026-07-05"),
        );
        assert!(result.is_err(), "the injected cursor write must fail");
        assert_eq!(s.count().unwrap(), 0, "the page insert must roll back");
        assert_eq!(s.get_cursor("arxiv-cs").unwrap(), None);
    }

    #[test]
    fn completed_high_water_includes_pages_before_resume() {
        let path = tmp_path();
        let s = SqliteStore::open(&path).unwrap();
        s.commit_harvest_page(
            "arxiv-cs",
            &[doc("page-1", "First", "alpha")],
            Some("page-2-token"),
            Some("2026-07-05"),
        )
        .unwrap();
        drop(s);

        // Reopen the database to model a process stop between capped runs.
        let s = SqliteStore::open(&path).unwrap();
        let interrupted = s.get_cursor("arxiv-cs").unwrap().unwrap();
        assert_eq!(interrupted.cursor.as_deref(), Some("page-2-token"));
        assert_eq!(
            interrupted.pending_high_water.as_deref(),
            Some("2026-07-05")
        );
        assert_eq!(interrupted.high_water, None);

        s.commit_harvest_page(
            "arxiv-cs",
            &[doc("page-2", "Second", "beta")],
            None,
            Some("2026-07-04"),
        )
        .unwrap();
        drop(s);

        let s = SqliteStore::open(&path).unwrap();
        let completed = s.get_cursor("arxiv-cs").unwrap().unwrap();
        assert_eq!(completed.cursor, None);
        assert_eq!(completed.pending_high_water, None);
        assert_eq!(completed.high_water.as_deref(), Some("2026-07-05"));
        assert_eq!(s.count().unwrap(), 2);
    }

    #[test]
    fn old_cursor_table_gains_pending_high_water_column() {
        let path = tmp_path();
        let conn = Connection::open(&path).unwrap();
        conn.execute_batch(
            "CREATE TABLE cursors (
                source_id TEXT PRIMARY KEY,
                cursor TEXT,
                high_water TEXT,
                updated_at TEXT NOT NULL DEFAULT (datetime('now'))
             );",
        )
        .unwrap();
        drop(conn);

        let s = SqliteStore::open(&path).unwrap();
        let columns = s
            .conn
            .lock()
            .unwrap()
            .prepare("PRAGMA table_info(cursors)")
            .unwrap()
            .query_map([], |row| row.get::<_, String>(1))
            .unwrap()
            .collect::<rusqlite::Result<Vec<_>>>()
            .unwrap();
        assert!(columns.iter().any(|name| name == "pending_high_water"));
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
        let old_fingerprint = s.fingerprints().unwrap()["d1"];

        assert!(s
            .update_document(&doc("d1", "Revised", "photonic gizmos instead"))
            .unwrap());

        // The old term is gone from the index...
        assert_eq!(hits(&s, "quantum"), 0);
        // ...and the new one is present.
        assert_eq!(hits(&s, "photonic"), 1);
        // The archive itself agrees.
        assert_eq!(s.count().unwrap(), 1);
        let new_fingerprint = s.fingerprints().unwrap()["d1"];
        assert_ne!(new_fingerprint, old_fingerprint);
        assert_eq!(
            new_fingerprint,
            intel_extract::simhash("Revised photonic gizmos instead")
        );
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

    fn canonical_rows(s: &SqliteStore) -> Vec<(String, Option<String>)> {
        let conn = s.conn.lock().unwrap();
        let mut stmt = conn
            .prepare("SELECT id, canonical_id FROM documents ORDER BY id")
            .unwrap();
        stmt.query_map([], |row| Ok((row.get(0)?, row.get(1)?)))
            .unwrap()
            .collect::<rusqlite::Result<Vec<_>>>()
            .unwrap()
    }

    #[test]
    fn body_update_rematerializes_identity_after_the_old_canonical_moves_away() {
        let s = tmp_store();
        s.append_new(&[
            dup_doc("original", "2026-07-03", ORIGINAL),
            dup_doc("survivor", "2026-07-04", SYNDICATED),
        ])
        .unwrap();
        s.assign_canonical_ids(DEDUP_MAX_DISTANCE).unwrap();
        assert_eq!(
            s.canonical_id("survivor").unwrap().as_deref(),
            Some("original")
        );

        let changed = dup_doc(
            "original",
            "2026-07-03",
            "Unrelated coastal salinity observations from public ocean buoys.",
        );
        assert!(s.update_document(&changed).unwrap());
        assert_eq!(
            s.canonical_id("survivor").unwrap().as_deref(),
            Some("survivor")
        );
    }

    #[test]
    fn published_day_update_rematerializes_the_older_original_tie_break() {
        let s = tmp_store();
        s.append_new(&[
            dup_doc("alpha", "2026-07-04", ORIGINAL),
            dup_doc("beta", "2026-07-05", SYNDICATED),
        ])
        .unwrap();
        s.assign_canonical_ids(DEDUP_MAX_DISTANCE).unwrap();
        assert_eq!(s.canonical_id("beta").unwrap().as_deref(), Some("alpha"));

        let newly_older = dup_doc("beta", "2026-07-03", SYNDICATED);
        assert!(s.update_document(&newly_older).unwrap());
        assert_eq!(s.canonical_id("beta").unwrap().as_deref(), Some("beta"));
        assert_eq!(s.canonical_id("alpha").unwrap().as_deref(), Some("beta"));
    }

    #[test]
    fn deleting_a_canonical_row_rematerializes_every_survivor() {
        let s = tmp_store();
        s.append_new(&[
            dup_doc("original", "2026-07-03", ORIGINAL),
            dup_doc("survivor", "2026-07-04", SYNDICATED),
        ])
        .unwrap();
        s.assign_canonical_ids(DEDUP_MAX_DISTANCE).unwrap();

        assert!(s.delete_document("original").unwrap());
        assert_eq!(
            s.canonical_id("survivor").unwrap().as_deref(),
            Some("survivor")
        );
        let dangling: i64 = s
            .conn
            .lock()
            .unwrap()
            .query_row(
                "SELECT COUNT(*) FROM documents WHERE canonical_id = 'original'",
                [],
                |row| row.get(0),
            )
            .unwrap();
        assert_eq!(dangling, 0);
    }

    #[test]
    fn no_op_update_leaves_canonical_ids_byte_identical() {
        let s = tmp_store();
        let original = dup_doc("original", "2026-07-03", ORIGINAL);
        let survivor = dup_doc("survivor", "2026-07-04", SYNDICATED);
        s.append_new(&[original.clone(), survivor]).unwrap();
        s.assign_canonical_ids(DEDUP_MAX_DISTANCE).unwrap();
        let before = canonical_rows(&s);

        assert!(s.update_document(&original).unwrap());
        assert_eq!(canonical_rows(&s), before);
    }

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
    fn sector_and_id_scoped_queries_bind_and_filter_in_sql() {
        let s = tmp_store();
        let technology = doc("technology-doc", "Technology", "accelerators");
        let mut finance = doc("finance-doc", "Finance", "quarterly filing");
        finance.sector = SectorId("finance".into());
        let shaped_id = "quoted',finance-doc";
        let shaped = doc(shaped_id, "Bound id", "parameter control");
        s.append_new(&[technology, finance, shaped]).unwrap();

        let rows = s.documents_in_sectors(&["technology".to_string()]).unwrap();
        let ids: Vec<&str> = rows
            .iter()
            .map(|(document, _)| document.id.as_str())
            .collect();
        assert_eq!(ids.len(), 2);
        assert!(ids.contains(&"technology-doc"));
        assert!(ids.contains(&shaped_id));
        assert!(!ids.contains(&"finance-doc"));
        assert!(s.documents_in_sectors(&[]).unwrap().is_empty());

        let bound = s.documents_by_ids(&[shaped_id]).unwrap();
        assert_eq!(bound.len(), 1);
        assert_eq!(bound[0].id, shaped_id);
        assert!(s.documents_by_ids(&[]).unwrap().is_empty());

        let scoped = s
            .documents_by_ids_in_sectors(&[shaped_id, "finance-doc"], &["technology".to_string()])
            .unwrap();
        assert_eq!(scoped.len(), 1);
        assert_eq!(scoped[0].id, shaped_id);
        assert!(s
            .documents_by_ids_in_sectors(&[shaped_id], &[])
            .unwrap()
            .is_empty());
        assert!(s
            .documents_by_ids_in_sectors(&[], &["technology".to_string()])
            .unwrap()
            .is_empty());

        let missing = s
            .docs_missing_embeddings("sector-bound-model", &["finance".to_string()])
            .unwrap();
        assert_eq!(missing.len(), 1);
        assert_eq!(missing[0].id, "finance-doc");
        assert!(s
            .docs_missing_embeddings("sector-bound-model", &[])
            .unwrap()
            .is_empty());
    }

    #[test]
    fn view_load_names_a_document_with_a_missing_fingerprint() {
        let s = tmp_store();
        s.append_new(&[doc("missing-view-fingerprint", "T", "body")])
            .unwrap();
        s.conn
            .lock()
            .unwrap()
            .execute(
                "UPDATE documents SET simhash = NULL
                 WHERE id = 'missing-view-fingerprint'",
                [],
            )
            .unwrap();

        assert_eq!(
            s.missing_fingerprints().unwrap(),
            vec!["missing-view-fingerprint".to_string()]
        );
        let error = s
            .load_all_with_fingerprints()
            .expect_err("a missing fingerprint must fail the view load");
        let message = error.to_string();
        assert!(message.contains("missing-view-fingerprint"), "{message}");
        assert!(message.contains("verify-fingerprints"), "{message}");
    }

    #[test]
    fn canonical_assignment_refuses_a_missing_fingerprint() {
        let s = tmp_store();
        s.append_new(&[doc("missing-canonical-fingerprint", "T", "body")])
            .unwrap();
        s.conn
            .lock()
            .unwrap()
            .execute(
                "UPDATE documents SET simhash = NULL, canonical_id = NULL
                 WHERE id = 'missing-canonical-fingerprint'",
                [],
            )
            .unwrap();

        let error = s
            .assign_canonical_ids(16)
            .expect_err("canonical assignment must not silently skip the document");
        let message = error.to_string();
        assert!(
            message.contains("missing-canonical-fingerprint"),
            "{message}"
        );
        assert!(message.contains("verify-fingerprints"), "{message}");
        assert_eq!(
            s.canonical_id("missing-canonical-fingerprint").unwrap(),
            None
        );
    }

    #[test]
    fn one_model_name_cannot_mix_embedding_dimensions() {
        let s = tmp_store();
        s.append_new(&[
            doc("d1", "First", "first embedding"),
            doc("d2", "Second", "second embedding"),
        ])
        .unwrap();
        s.upsert_embeddings("shared-model", &[("d1".into(), vec![1.0; 32])])
            .unwrap();

        let err = s
            .upsert_embeddings("shared-model", &[("d2".into(), vec![1.0; 1024])])
            .expect_err("a model key must have exactly one stored dimension");
        let message = err.to_string();
        assert!(message.contains("shared-model"), "{message}");
        assert!(message.contains("32"), "{message}");
        assert!(message.contains("1024"), "{message}");
        assert_eq!(s.embeddings_count("shared-model").unwrap(), 1);
    }

    #[test]
    fn migration_backfills_pre_fingerprint_archive_without_changing_identity() {
        let path = tmp_path();
        let legacy = rusqlite::Connection::open(&path).unwrap();
        legacy
            .execute_batch(
                "CREATE TABLE documents (
                    id TEXT PRIMARY KEY,
                    sector TEXT NOT NULL,
                    url TEXT,
                    title TEXT NOT NULL,
                    body TEXT NOT NULL,
                    published_day INTEGER,
                    published_raw TEXT,
                    authors TEXT NOT NULL,
                    tags TEXT NOT NULL,
                    source_id TEXT NOT NULL,
                    retrieved_from TEXT NOT NULL,
                    source_kind TEXT NOT NULL,
                    license TEXT NOT NULL,
                    canonical_id TEXT
                );
                INSERT INTO documents VALUES
                    ('original', 'technology', NULL, 'Alpha', 'quantum widgets',
                     739071, '2026-07-04', '[]', '[]', 'test', 'legacy', 'rss',
                     'CC-BY', 'original'),
                    ('copy', 'technology', NULL, 'Beta', 'photonic gizmos',
                     739071, '2026-07-04', '[]', '[]', 'test', 'legacy', 'rss',
                     'CC-BY', 'original');",
            )
            .unwrap();
        let columns: Vec<String> = legacy
            .prepare("PRAGMA table_info(documents)")
            .unwrap()
            .query_map([], |row| row.get(1))
            .unwrap()
            .collect::<rusqlite::Result<_>>()
            .unwrap();
        assert!(!columns.iter().any(|name| name == "simhash"));
        drop(legacy);

        let (migrated, timings) = SqliteStore::open_with_timings(&path).unwrap();
        assert_eq!(timings.fingerprints_backfilled, 2);
        assert!(timings.total_us >= timings.fingerprint_backfill_us);
        assert_eq!(migrated.count().unwrap(), 2);
        let prints = migrated.fingerprints().unwrap();
        assert_eq!(prints.len(), 2);
        assert_eq!(
            prints["original"],
            intel_extract::simhash("Alpha quantum widgets")
        );
        assert_eq!(
            prints["copy"],
            intel_extract::simhash("Beta photonic gizmos")
        );
        assert_eq!(
            migrated.canonical_id("original").unwrap().as_deref(),
            Some("original")
        );
        assert_eq!(
            migrated.canonical_id("copy").unwrap().as_deref(),
            Some("original")
        );
        assert_eq!(migrated.load_all_with_fingerprints().unwrap().len(), 2);
    }

    #[test]
    fn high_water_is_monotonic() {
        let s = tmp_store();
        s.commit_harvest_page("arxiv-cs", &[], None, Some("2026-07-04"))
            .unwrap();
        // An older datestamp must not roll the mark backward.
        s.commit_harvest_page("arxiv-cs", &[], None, Some("2026-07-01"))
            .unwrap();
        assert_eq!(
            s.get_cursor("arxiv-cs")
                .unwrap()
                .unwrap()
                .high_water
                .as_deref(),
            Some("2026-07-04")
        );
        // A newer one advances it.
        s.commit_harvest_page("arxiv-cs", &[], None, Some("2026-07-09"))
            .unwrap();
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
