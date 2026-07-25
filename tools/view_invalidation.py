#!/usr/bin/env python3
"""Design and failure-capable control for a restart-safe `/view` key."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sqlite3
import tempfile
from pathlib import Path
from typing import Any, Iterable

ALGORITHM_SCHEMA_VERSION = "view-v2-design-1"
MUTATION_CLASSES = (
    "append",
    "update",
    "delete",
    "canonical-id-rematerialization",
    "fingerprint-refresh",
    "embedding-write",
)


def _feed(digest: Any, label: str, values: Iterable[Any]) -> None:
    digest.update(label.encode("utf-8"))
    digest.update(b"\0")
    for value in values:
        if value is None:
            encoded = b"n"
        elif isinstance(value, bytes):
            encoded = b"b" + value
        elif isinstance(value, float):
            encoded = b"f" + value.hex().encode("ascii")
        elif isinstance(value, int):
            encoded = b"i" + str(value).encode("ascii")
        else:
            encoded = b"s" + str(value).encode("utf-8")
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)


def candidate_key(
    database: Path,
    sectors: list[str],
    *,
    algorithm_schema_version: str = ALGORITHM_SCHEMA_VERSION,
    omit_component: str | None = None,
) -> str:
    """Hash every key input without creating a derived database object."""
    digest = hashlib.sha256()
    _feed(digest, "archive-identity", [str(database.resolve())])
    _feed(digest, "sector-set", sorted(set(sectors)))
    _feed(digest, "algorithm-schema-version", [algorithm_schema_version])

    with sqlite3.connect(f"file:{database}?mode=ro", uri=True) as connection:
        schema = connection.execute(
            """
            SELECT type, name, tbl_name, COALESCE(sql, '')
            FROM sqlite_master
            WHERE name NOT LIKE 'sqlite_%'
            ORDER BY type, name
            """
        ).fetchall()
        for row in schema:
            _feed(digest, "sqlite-schema", row)

        for table, order_by, component in (
            ("documents", "id", "documents"),
            ("embeddings", "doc_id, model", "embeddings"),
        ):
            if omit_component == component:
                continue
            columns = [
                str(row[1])
                for row in connection.execute(
                    f"PRAGMA table_info({table})"
                ).fetchall()
            ]
            if not columns:
                continue
            _feed(digest, f"{table}-columns", columns)
            rows = connection.execute(
                f"SELECT * FROM {table} ORDER BY {order_by}"
            ).fetchall()
            for row in rows:
                _feed(digest, f"{table}-row", row)
    return digest.hexdigest()


def _create_fixture(path: Path) -> None:
    with sqlite3.connect(path) as connection:
        connection.executescript(
            """
            CREATE TABLE documents (
                id TEXT PRIMARY KEY,
                sector TEXT NOT NULL,
                title TEXT NOT NULL,
                body TEXT NOT NULL,
                canonical_id TEXT,
                simhash INTEGER
            );
            CREATE TABLE embeddings (
                doc_id TEXT NOT NULL,
                model TEXT NOT NULL,
                dim INTEGER NOT NULL,
                vec BLOB NOT NULL,
                PRIMARY KEY (doc_id, model)
            );
            INSERT INTO documents VALUES
                ('doc-a', 'science', 'Alpha', 'Body A', 'doc-a', 11),
                ('doc-b', 'science', 'Beta', 'Body B', 'doc-b', 22);
            """
        )


def _mutate(path: Path, mutation: str) -> None:
    statements = {
        "append": (
            "INSERT INTO documents VALUES "
            "('doc-c', 'science', 'Gamma', 'Body C', 'doc-c', 33)"
        ),
        "update": "UPDATE documents SET title = 'Alpha 2' WHERE id = 'doc-a'",
        "delete": "DELETE FROM documents WHERE id = 'doc-b'",
        "canonical-id-rematerialization": (
            "UPDATE documents SET canonical_id = 'doc-a' WHERE id = 'doc-b'"
        ),
        "fingerprint-refresh": (
            "UPDATE documents SET simhash = simhash + 1 WHERE id = 'doc-a'"
        ),
        "embedding-write": (
            "INSERT INTO embeddings VALUES "
            "('doc-a', 'model', 2, X'0000000000000000')"
        ),
    }
    with sqlite3.connect(path) as connection:
        connection.execute(statements[mutation])


def run_control(omit_component: str | None) -> int:
    detections: dict[str, bool] = {}
    with tempfile.TemporaryDirectory(
        prefix="intel-view-key-control-"
    ) as temp:
        temp_dir = Path(temp)
        base = temp_dir / "base.db"
        _create_fixture(base)

        for mutation in MUTATION_CLASSES:
            subject = temp_dir / f"{mutation}.db"
            shutil.copyfile(base, subject)
            before = candidate_key(
                subject,
                ["science"],
                omit_component=omit_component,
            )
            _mutate(subject, mutation)
            after = candidate_key(
                subject,
                ["science"],
                omit_component=omit_component,
            )
            detections[mutation] = before != after

        sector_before = candidate_key(base, ["science"])
        sector_after = candidate_key(base, ["finance", "science"])
        version_after = candidate_key(
            base,
            ["science"],
            algorithm_schema_version="view-v2-design-2",
        )
        archive_copy = temp_dir / "archive-copy.db"
        shutil.copyfile(base, archive_copy)
        archive_after = candidate_key(archive_copy, ["science"])

    for mutation, detected in detections.items():
        print(
            f"{mutation}: {'DETECTED' if detected else 'STALE-RESULT RISK'}"
        )
    print(
        "sector-set: "
        f"{'DETECTED' if sector_before != sector_after else 'MISSED'}"
    )
    print(
        "algorithm-schema-version: "
        f"{'DETECTED' if sector_before != version_after else 'MISSED'}"
    )
    print(
        "archive-identity: "
        f"{'DETECTED' if sector_before != archive_after else 'MISSED'}"
    )

    missed = [
        mutation for mutation, detected in detections.items() if not detected
    ]
    if sector_before == sector_after:
        missed.append("sector-set")
    if sector_before == version_after:
        missed.append("algorithm-schema-version")
    if sector_before == archive_after:
        missed.append("archive-identity")
    if missed:
        print("view-key control: FAIL: missed " + ", ".join(missed))
        return 1
    print("view-key control: PASS (9/9 invalidation inputs detected)")
    return 0


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(
        description="Compute or challenge the V2 candidate invalidation key."
    )
    subparsers = value.add_subparsers(dest="command", required=True)
    key = subparsers.add_parser("key")
    key.add_argument("database", type=Path)
    key.add_argument("--sectors", required=True)
    control = subparsers.add_parser("control")
    control.add_argument(
        "--omit-component",
        choices=("documents", "embeddings"),
    )
    return value


def main() -> int:
    args = parser().parse_args()
    if args.command == "key":
        sectors = [
            sector.strip()
            for sector in args.sectors.split(",")
            if sector.strip()
        ]
        if not sectors:
            raise SystemExit("--sectors must name at least one sector")
        print(candidate_key(args.database, sectors))
        return 0
    return run_control(args.omit_component)


if __name__ == "__main__":
    raise SystemExit(main())
