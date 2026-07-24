from __future__ import annotations

import hashlib
import json
import sqlite3
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools" / "evidence_artifacts.py"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _create_database(path: Path) -> None:
    with sqlite3.connect(path) as connection:
        connection.executescript(
            """
            CREATE TABLE documents (
                id TEXT PRIMARY KEY,
                simhash INTEGER,
                canonical_id TEXT
            );
            CREATE TABLE cursors (
                source_id TEXT PRIMARY KEY,
                cursor TEXT,
                high_water TEXT,
                pending_high_water TEXT,
                updated_at TEXT NOT NULL
            );
            INSERT INTO documents VALUES ('source::one', 1, 'source::one');
            INSERT INTO cursors VALUES (
                'source', 'next-token', NULL, '2026-07-24',
                '2026-07-24 00:00:00'
            );
            """
        )


def _manifest(database: Path) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "lifecycle": {
            "policy": "immutable_evidence",
            "live_harvest": "fresh_path_only",
            "admission": (
                "explicit_task_with_captured_wire_evidence_and_operator_review"
            ),
        },
        "artifacts": [
            {
                "path": database.name,
                "sha256": _sha256(database),
                "bytes": database.stat().st_size,
                "purpose": "failure-capable test evidence",
                "provenance": "created inside one disposable pytest directory",
                "expected": {
                    "documents": 1,
                    "integrity_check": "ok",
                    "null_simhash": 0,
                    "null_canonical_id": 0,
                    "cursors": [
                        {
                            "source_id": "source",
                            "cursor": "next-token",
                            "high_water": None,
                            "pending_high_water": "2026-07-24",
                            "updated_at": "2026-07-24 00:00:00",
                        }
                    ],
                },
            }
        ],
    }


def _write_manifest(path: Path, manifest: dict[str, Any]) -> None:
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")


def _run(
    root: Path,
    manifest: Path,
    command: str,
    *args: str,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(TOOL),
            "--manifest",
            str(manifest),
            "--root",
            str(root),
            command,
            *args,
        ],
        text=True,
        capture_output=True,
        check=False,
    )


def _fixture(tmp_path: Path) -> tuple[Path, Path, dict[str, Any]]:
    database = tmp_path / "evidence.db"
    manifest_path = tmp_path / "manifest.json"
    _create_database(database)
    manifest = _manifest(database)
    _write_manifest(manifest_path, manifest)
    return database, manifest_path, manifest


def test_clean_manifest_verifies_and_report_is_deterministic(tmp_path: Path) -> None:
    _, manifest_path, _ = _fixture(tmp_path)

    verified = _run(tmp_path, manifest_path, "verify")
    assert verified.returncode == 0, verified.stderr
    assert "protected evidence: 1/1 artifacts match" in verified.stdout

    first = _run(tmp_path, manifest_path, "report")
    second = _run(tmp_path, manifest_path, "report")
    assert first.returncode == second.returncode == 0
    assert first.stdout == second.stdout
    report = json.loads(first.stdout)
    assert report["artifacts"][0]["documents"] == 1
    assert report["artifacts"][0]["cursors"][0]["cursor"] == "next-token"


def test_byte_mutation_names_sha256(tmp_path: Path) -> None:
    database, manifest_path, _ = _fixture(tmp_path)
    with database.open("ab") as handle:
        handle.write(b"planted-byte-mismatch")

    checked = _run(tmp_path, manifest_path, "verify")

    assert checked.returncode == 1
    assert "MISMATCH evidence.db field=sha256" in checked.stderr
    assert "expected:" in checked.stderr
    assert "actual:" in checked.stderr


def test_document_count_mismatch_survives_fresh_hash(tmp_path: Path) -> None:
    database, manifest_path, manifest = _fixture(tmp_path)
    with sqlite3.connect(database) as connection:
        connection.execute(
            "INSERT INTO documents VALUES ('source::two', 2, 'source::two')"
        )
    artifact = manifest["artifacts"][0]
    artifact["sha256"] = _sha256(database)
    artifact["bytes"] = database.stat().st_size
    _write_manifest(manifest_path, manifest)

    checked = _run(tmp_path, manifest_path, "verify")

    assert checked.returncode == 1
    assert "MISMATCH evidence.db field=documents" in checked.stderr
    assert "field=sha256" not in checked.stderr
    assert "field=bytes" not in checked.stderr


def test_cursor_mismatch_survives_fresh_hash(tmp_path: Path) -> None:
    database, manifest_path, manifest = _fixture(tmp_path)
    with sqlite3.connect(database) as connection:
        connection.execute(
            "UPDATE cursors SET cursor = 'wrong-token' WHERE source_id = 'source'"
        )
    artifact = manifest["artifacts"][0]
    artifact["sha256"] = _sha256(database)
    artifact["bytes"] = database.stat().st_size
    _write_manifest(manifest_path, manifest)

    checked = _run(tmp_path, manifest_path, "verify")

    assert checked.returncode == 1
    assert "MISMATCH evidence.db field=cursors.source.cursor" in checked.stderr
    assert "field=sha256" not in checked.stderr
    assert "field=bytes" not in checked.stderr


def test_protected_path_matching_resolves_aliases(tmp_path: Path) -> None:
    database, manifest_path, _ = _fixture(tmp_path)
    alias = tmp_path / "alias.db"
    alias.symlink_to(database)

    for target in (
        "evidence.db",
        "./evidence.db",
        str(database.resolve()),
        str(alias),
    ):
        checked = _run(tmp_path, manifest_path, "protected", target)
        assert checked.returncode == 0, checked.stderr
        assert checked.stdout.endswith("\tevidence.db\n")

    safe = _run(tmp_path, manifest_path, "protected", "fresh.db")
    assert safe.returncode == 1
