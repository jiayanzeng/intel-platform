use intel_core::{Document, License, Provenance, SectorId, SourceKind};
use intel_store::SqliteStore;
use rusqlite::Connection;
use std::path::PathBuf;
use std::time::{SystemTime, UNIX_EPOCH};

fn unique_db_path() -> PathBuf {
    let nonce = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .expect("system clock after epoch")
        .as_nanos();
    std::env::temp_dir().join(format!(
        "intel-store-license-compat-{}-{nonce}.db",
        std::process::id()
    ))
}

fn document(license: License) -> Document {
    Document {
        id: "publisher::document".to_string(),
        sector: SectorId::new("finance"),
        url: Some("https://publisher.invalid/document".to_string()),
        title: "Publisher permission".to_string(),
        body: "publisher permits reuse under its stated terms".to_string(),
        published_day: None,
        published_raw: None,
        authors: Vec::new(),
        tags: Vec::new(),
        provenance: Provenance {
            source_id: "publisher".to_string(),
            retrieved_from: "https://publisher.invalid/feed".to_string(),
            kind: SourceKind::Rss,
            license,
        },
    }
}

#[test]
fn publisher_permission_round_trips_and_unknown_rows_fail_closed() {
    let path = unique_db_path();
    let store = SqliteStore::open(&path).expect("open store");
    assert_eq!(
        store
            .append_new(&[document(License::PublisherPermitted)])
            .expect("append document"),
        1
    );
    assert_eq!(
        store.load_all().expect("load document")[0]
            .provenance
            .license,
        License::PublisherPermitted
    );
    let hit = store
        .search("publisher", &["finance".to_string()], 10)
        .expect("search document")
        .remove(0);
    assert_eq!(hit.license, License::PublisherPermitted);
    assert!(hit.snippet.is_some());
    drop(store);

    let connection = Connection::open(&path).expect("reopen raw database");
    let stored: String = connection
        .query_row(
            "SELECT license FROM documents WHERE id = ?1",
            ["publisher::document"],
            |row| row.get(0),
        )
        .expect("read stored license");
    assert_eq!(stored, "PublisherPermitted");
    connection
        .execute(
            "UPDATE documents SET license = ?1 WHERE id = ?2",
            ["FutureLicense", "publisher::document"],
        )
        .expect("plant unknown future license");
    drop(connection);

    let store = SqliteStore::open(&path).expect("reopen store");
    assert_eq!(
        store.load_all().expect("load fallback document")[0]
            .provenance
            .license,
        License::IndexOnly
    );
    let hit = store
        .search("publisher", &["finance".to_string()], 10)
        .expect("search fallback document")
        .remove(0);
    assert_eq!(hit.license, License::IndexOnly);
    assert!(hit.snippet.is_none());
    drop(store);

    std::fs::remove_file(path).expect("remove temporary database");
}
