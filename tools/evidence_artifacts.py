#!/usr/bin/env python3
"""Verify and report immutable evidence artifacts without modifying them."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sqlite3
import sys
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "config" / "protected-artifacts.json"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
GIT_OUTPUT_REF_RE = re.compile(
    r"^git:[0-9a-f]{40}:[^:#\s]+(?:#[^\s]+)?$"
)
HASH_OUTPUT_REF_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
CURSOR_FIELDS = (
    "cursor",
    "high_water",
    "pending_high_water",
    "updated_at",
)


class ManifestError(ValueError):
    """The evidence manifest is malformed."""


def _exact_keys(value: dict[str, Any], expected: set[str], context: str) -> None:
    actual = set(value)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise ManifestError(
            f"{context}: keys differ; missing={missing}, extra={extra}"
        )


def _non_empty_string(value: Any, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ManifestError(f"{context}: expected a non-empty string")
    return value


def _non_negative_int(value: Any, context: str) -> int:
    if type(value) is not int or value < 0:
        raise ManifestError(f"{context}: expected a non-negative integer")
    return value


def _validate_cursor(value: Any, context: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ManifestError(f"{context}: expected an object")
    _exact_keys(value, {"source_id", *CURSOR_FIELDS}, context)
    _non_empty_string(value["source_id"], f"{context}.source_id")
    for field in CURSOR_FIELDS:
        if value[field] is not None and not isinstance(value[field], str):
            raise ManifestError(f"{context}.{field}: expected string or null")
    return value


def _sha256_string(value: Any, context: str) -> str:
    digest = _non_empty_string(value, context)
    if SHA256_RE.fullmatch(digest) is None:
        raise ManifestError(f"{context}: expected 64 lowercase hex digits")
    return digest


def _iso_date(value: Any, context: str) -> str:
    raw = _non_empty_string(value, context)
    try:
        parsed = dt.date.fromisoformat(raw)
    except ValueError as error:
        raise ManifestError(f"{context}: expected an ISO date") from error
    if parsed.isoformat() != raw:
        raise ManifestError(f"{context}: expected an ISO date")
    return raw


def _validate_wire_evidence(value: Any, context: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ManifestError(f"{context}: expected an object")
    _exact_keys(value, {"command", "output_ref"}, context)
    _non_empty_string(value["command"], f"{context}.command")
    output_ref = _non_empty_string(value["output_ref"], f"{context}.output_ref")
    if (
        GIT_OUTPUT_REF_RE.fullmatch(output_ref) is None
        and HASH_OUTPUT_REF_RE.fullmatch(output_ref) is None
    ):
        raise ManifestError(
            f"{context}.output_ref: expected "
            "'git:<40-hex-commit>:<path>[#anchor]' or 'sha256:<64-hex>'"
        )
    return value


def _validate_admission_record(
    value: Any,
    context: str,
    previous_sha256: str | None,
) -> str:
    if not isinstance(value, dict):
        raise ManifestError(f"{context}: expected an object")
    _exact_keys(
        value,
        {
            "task_id",
            "date",
            "sha256",
            "prior_sha256",
            "wire_evidence",
            "operator_approval",
            "retroactive",
        },
        context,
    )
    _non_empty_string(value["task_id"], f"{context}.task_id")
    _iso_date(value["date"], f"{context}.date")
    digest = _sha256_string(value["sha256"], f"{context}.sha256")
    prior = value["prior_sha256"]
    if prior is not None:
        _sha256_string(prior, f"{context}.prior_sha256")
    if prior != previous_sha256:
        raise ManifestError(
            f"{context}.prior_sha256: chain break; "
            f"expected {previous_sha256!r}, found {prior!r}"
        )

    wire_evidence = value["wire_evidence"]
    if not isinstance(wire_evidence, list) or not wire_evidence:
        raise ManifestError(
            f"{context}.wire_evidence: expected a non-empty array"
        )
    for index, evidence in enumerate(wire_evidence):
        _validate_wire_evidence(
            evidence,
            f"{context}.wire_evidence[{index}]",
        )

    approval = value["operator_approval"]
    if not isinstance(approval, dict):
        raise ManifestError(f"{context}.operator_approval: expected an object")
    _exact_keys(
        approval,
        {"approved_by", "approval_ref"},
        f"{context}.operator_approval",
    )
    _non_empty_string(
        approval["approved_by"],
        f"{context}.operator_approval.approved_by",
    )
    _non_empty_string(
        approval["approval_ref"],
        f"{context}.operator_approval.approval_ref",
    )
    if type(value["retroactive"]) is not bool:
        raise ManifestError(f"{context}.retroactive: expected a boolean")
    return digest


def _validate_admission(
    value: Any,
    context: str,
    artifact_sha256: str,
) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ManifestError(f"{context}: expected an object")
    _exact_keys(value, {"records"}, context)
    records = value["records"]
    if not isinstance(records, list) or not records:
        raise ManifestError(f"{context}.records: expected a non-empty array")
    previous: str | None = None
    for index, record in enumerate(records):
        previous = _validate_admission_record(
            record,
            f"{context}.records[{index}]",
            previous,
        )
    if previous != artifact_sha256:
        raise ManifestError(
            f"{context}: newest admission sha256 {previous!r} does not match "
            f"artifact sha256 {artifact_sha256!r}; add a complete admission "
            "record for the new expected hash"
        )
    return value


def _validate_artifact(value: Any, index: int) -> dict[str, Any]:
    context = f"artifacts[{index}]"
    if not isinstance(value, dict):
        raise ManifestError(f"{context}: expected an object")
    _exact_keys(
        value,
        {
            "path",
            "sha256",
            "bytes",
            "purpose",
            "provenance",
            "admission",
            "expected",
        },
        context,
    )
    raw_path = _non_empty_string(value["path"], f"{context}.path")
    path = PurePosixPath(raw_path)
    if (
        path.is_absolute()
        or ".." in path.parts
        or "|" in raw_path
        or "\t" in raw_path
    ):
        raise ManifestError(
            f"{context}.path: expected a safe repository-relative path"
        )
    digest = _sha256_string(value["sha256"], f"{context}.sha256")
    _non_negative_int(value["bytes"], f"{context}.bytes")
    _non_empty_string(value["purpose"], f"{context}.purpose")
    _non_empty_string(value["provenance"], f"{context}.provenance")
    _validate_admission(
        value["admission"],
        f"{context}.admission",
        digest,
    )

    expected = value["expected"]
    if not isinstance(expected, dict):
        raise ManifestError(f"{context}.expected: expected an object")
    _exact_keys(
        expected,
        {
            "documents",
            "integrity_check",
            "null_simhash",
            "null_canonical_id",
            "cursors",
        },
        f"{context}.expected",
    )
    _non_negative_int(expected["documents"], f"{context}.expected.documents")
    _non_empty_string(
        expected["integrity_check"], f"{context}.expected.integrity_check"
    )
    _non_negative_int(
        expected["null_simhash"], f"{context}.expected.null_simhash"
    )
    _non_negative_int(
        expected["null_canonical_id"],
        f"{context}.expected.null_canonical_id",
    )
    cursors = expected["cursors"]
    if not isinstance(cursors, list):
        raise ManifestError(f"{context}.expected.cursors: expected an array")
    checked = [
        _validate_cursor(cursor, f"{context}.expected.cursors[{cursor_index}]")
        for cursor_index, cursor in enumerate(cursors)
    ]
    source_ids = [cursor["source_id"] for cursor in checked]
    if len(source_ids) != len(set(source_ids)):
        raise ManifestError(
            f"{context}.expected.cursors: source_id values must be unique"
        )
    return value


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        raw = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise ManifestError(f"{path}: {error}") from error
    if not isinstance(raw, dict):
        raise ManifestError(f"{path}: top level must be an object")
    _exact_keys(raw, {"schema_version", "lifecycle", "artifacts"}, str(path))
    if raw["schema_version"] != 2:
        raise ManifestError(f"{path}: schema_version must be 2")

    lifecycle = raw["lifecycle"]
    if not isinstance(lifecycle, dict):
        raise ManifestError(f"{path}: lifecycle must be an object")
    _exact_keys(
        lifecycle,
        {"policy", "live_harvest", "admission"},
        f"{path}: lifecycle",
    )
    if lifecycle["policy"] != "immutable_evidence":
        raise ManifestError(f"{path}: lifecycle.policy must be immutable_evidence")
    if lifecycle["live_harvest"] != "fresh_path_only":
        raise ManifestError(f"{path}: lifecycle.live_harvest must be fresh_path_only")
    if (
        lifecycle["admission"]
        != "append_only_chained_records_with_wire_evidence_and_operator_approval"
    ):
        raise ManifestError(f"{path}: lifecycle.admission has an unknown policy")

    artifacts = raw["artifacts"]
    if not isinstance(artifacts, list) or not artifacts:
        raise ManifestError(f"{path}: artifacts must be a non-empty array")
    checked = [
        _validate_artifact(artifact, index)
        for index, artifact in enumerate(artifacts)
    ]
    paths = [artifact["path"] for artifact in checked]
    if len(paths) != len(set(paths)):
        raise ManifestError(f"{path}: artifact paths must be unique")
    return raw


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _database_measurements(path: Path) -> dict[str, Any]:
    uri = f"{path.resolve().as_uri()}?mode=ro"
    connection = sqlite3.connect(uri, uri=True)
    try:
        connection.execute("PRAGMA query_only = ON")
        documents, null_simhash, null_canonical_id = connection.execute(
            """
            SELECT
                COUNT(*),
                COUNT(*) - COUNT(simhash),
                COUNT(*) - COUNT(canonical_id)
            FROM documents
            """
        ).fetchone()
        integrity_rows = [
            row[0] for row in connection.execute("PRAGMA integrity_check")
        ]
        cursor_rows = connection.execute(
            """
            SELECT source_id, cursor, high_water, pending_high_water, updated_at
            FROM cursors
            ORDER BY source_id
            """
        ).fetchall()
    finally:
        connection.close()
    return {
        "documents": documents,
        "integrity_check": (
            "ok" if integrity_rows == ["ok"] else "; ".join(integrity_rows)
        ),
        "null_simhash": null_simhash,
        "null_canonical_id": null_canonical_id,
        "cursors": [
            {
                "source_id": row[0],
                "cursor": row[1],
                "high_water": row[2],
                "pending_high_water": row[3],
                "updated_at": row[4],
            }
            for row in cursor_rows
        ],
    }


def measure_artifact(root: Path, artifact: dict[str, Any]) -> dict[str, Any]:
    path = (root / artifact["path"]).resolve()
    if not path.is_file():
        raise FileNotFoundError(path)
    return {
        "path": artifact["path"],
        "sha256": _sha256(path),
        "bytes": path.stat().st_size,
        **_database_measurements(path),
    }


def _show(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False)


def _compare(
    artifact_path: str,
    field: str,
    expected: Any,
    actual: Any,
) -> bool:
    if expected == actual:
        return True
    print(f"MISMATCH {artifact_path} field={field}", file=sys.stderr)
    print(f"  expected: {_show(expected)}", file=sys.stderr)
    print(f"  actual:   {_show(actual)}", file=sys.stderr)
    return False


def verify(manifest: dict[str, Any], root: Path) -> int:
    matched_artifacts = 0
    failures = 0
    for artifact in manifest["artifacts"]:
        artifact_path = artifact["path"]
        try:
            actual = measure_artifact(root, artifact)
        except (OSError, sqlite3.Error) as error:
            print(
                f"MISMATCH {artifact_path} field=readable: {error}",
                file=sys.stderr,
            )
            failures += 1
            continue

        artifact_ok = True
        artifact_ok &= _compare(
            artifact_path, "sha256", artifact["sha256"], actual["sha256"]
        )
        artifact_ok &= _compare(
            artifact_path, "bytes", artifact["bytes"], actual["bytes"]
        )
        for field in (
            "documents",
            "integrity_check",
            "null_simhash",
            "null_canonical_id",
        ):
            artifact_ok &= _compare(
                artifact_path,
                field,
                artifact["expected"][field],
                actual[field],
            )

        expected_cursors = {
            cursor["source_id"]: cursor
            for cursor in artifact["expected"]["cursors"]
        }
        actual_cursors = {
            cursor["source_id"]: cursor for cursor in actual["cursors"]
        }
        artifact_ok &= _compare(
            artifact_path,
            "cursors.source_ids",
            sorted(expected_cursors),
            sorted(actual_cursors),
        )
        for source_id in sorted(set(expected_cursors) & set(actual_cursors)):
            for field in CURSOR_FIELDS:
                artifact_ok &= _compare(
                    artifact_path,
                    f"cursors.{source_id}.{field}",
                    expected_cursors[source_id][field],
                    actual_cursors[source_id][field],
                )

        if artifact_ok:
            print(
                f"MATCH {artifact_path} "
                f"sha256={actual['sha256']} "
                f"bytes={actual['bytes']} "
                f"documents={actual['documents']} "
                f"integrity={actual['integrity_check']} "
                f"null_simhash={actual['null_simhash']} "
                f"null_canonical_id={actual['null_canonical_id']} "
                f"cursors={len(actual['cursors'])}"
            )
            matched_artifacts += 1
        else:
            failures += 1

    total = len(manifest["artifacts"])
    if failures:
        print(
            f"protected evidence: {matched_artifacts}/{total} artifacts match",
            file=sys.stderr,
        )
        return 1
    print(f"protected evidence: {matched_artifacts}/{total} artifacts match")
    return 0


def report(manifest: dict[str, Any], root: Path) -> int:
    measured: list[dict[str, Any]] = []
    for artifact in manifest["artifacts"]:
        try:
            measured.append(measure_artifact(root, artifact))
        except (OSError, sqlite3.Error) as error:
            print(
                f"evidence-report: ERROR: {artifact['path']}: {error}",
                file=sys.stderr,
            )
            return 1
    print(json.dumps({"artifacts": measured}, indent=2, sort_keys=True))
    return 0


def protected_match(
    manifest: dict[str, Any], root: Path, target: Path
) -> tuple[str, str] | None:
    target_path = target if target.is_absolute() else root / target
    target_resolved = target_path.resolve()
    for artifact in manifest["artifacts"]:
        artifact_resolved = (root / artifact["path"]).resolve()
        if target_resolved == artifact_resolved:
            return artifact["sha256"], artifact["path"]
    return None


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help="evidence manifest (default: config/protected-artifacts.json)",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="root used to resolve artifact paths (default: repository root)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("verify")
    subparsers.add_parser("report")
    subparsers.add_parser("validate")
    protected = subparsers.add_parser("protected")
    protected.add_argument("target", type=Path)
    return parser


def main() -> int:
    args = _parser().parse_args()
    try:
        manifest = load_manifest(args.manifest.resolve())
    except ManifestError as error:
        print(f"evidence-manifest: ERROR: {error}", file=sys.stderr)
        return 2
    root = args.root.resolve()

    if args.command == "verify":
        return verify(manifest, root)
    if args.command == "report":
        return report(manifest, root)
    if args.command == "validate":
        print(
            f"evidence-manifest: PASS "
            f"(schema=2, artifacts={len(manifest['artifacts'])})"
        )
        return 0
    if args.command == "protected":
        match = protected_match(manifest, root, args.target)
        if match is None:
            return 1
        print(f"{match[0]}\t{match[1]}")
        return 0
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
