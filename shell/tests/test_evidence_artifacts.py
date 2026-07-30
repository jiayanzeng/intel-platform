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
    digest = _sha256(database)
    return {
        "schema_version": 2,
        "lifecycle": {
            "policy": "immutable_evidence",
            "live_harvest": "fresh_path_only",
            "admission": (
                "append_only_chained_records_with_wire_evidence_and_"
                "operator_approval"
            ),
        },
        "artifacts": [
            {
                "path": database.name,
                "sha256": digest,
                "bytes": database.stat().st_size,
                "purpose": "failure-capable test evidence",
                "provenance": "created inside one disposable pytest directory",
                "admission": {
                    "records": [
                        {
                            "task_id": "test/original",
                            "date": "2026-07-25",
                            "sha256": digest,
                            "prior_sha256": None,
                            "wire_evidence": [
                                {
                                    "command": "create disposable evidence DB",
                                    "output_ref": (
                                        "sha256:"
                                        "11111111111111111111111111111111"
                                        "11111111111111111111111111111111"
                                    ),
                                }
                            ],
                            "operator_approval": {
                                "approved_by": "pytest",
                                "approval_ref": "disposable test fixture",
                            },
                            "retroactive": False,
                        }
                    ]
                },
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
        "pinned_files": [],
    }


def _append_admission(
    artifact: dict[str, Any],
    digest: str,
    *,
    wire_evidence: list[dict[str, str]] | None = None,
    operator_approval: dict[str, str] | None = None,
) -> None:
    previous = artifact["admission"]["records"][-1]["sha256"]
    artifact["sha256"] = digest
    artifact["admission"]["records"].append(
        {
            "task_id": "test/change",
            "date": "2026-07-25",
            "sha256": digest,
            "prior_sha256": previous,
            "wire_evidence": (
                wire_evidence
                if wire_evidence is not None
                else [
                    {
                        "command": "mutate disposable evidence DB",
                        "output_ref": (
                            "sha256:"
                            "22222222222222222222222222222222"
                            "22222222222222222222222222222222"
                        ),
                    }
                ]
            ),
            "operator_approval": (
                operator_approval
                if operator_approval is not None
                else {
                    "approved_by": "pytest",
                    "approval_ref": "disposable mutation control",
                }
            ),
            "retroactive": False,
        }
    )


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
    _append_admission(artifact, _sha256(database))
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
    _append_admission(artifact, _sha256(database))
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


def test_expected_hash_change_requires_new_admission(tmp_path: Path) -> None:
    _, manifest_path, manifest = _fixture(tmp_path)
    manifest["artifacts"][0]["sha256"] = "3" * 64
    _write_manifest(manifest_path, manifest)

    checked = _run(tmp_path, manifest_path, "validate")

    assert checked.returncode != 0
    assert "artifacts[0].admission" in checked.stderr
    assert "add a complete admission record" in checked.stderr


def test_admission_requires_wire_evidence_and_operator_approval(
    tmp_path: Path,
) -> None:
    _, manifest_path, manifest = _fixture(tmp_path)
    artifact = manifest["artifacts"][0]
    original = artifact["sha256"]
    _append_admission(artifact, original, wire_evidence=[])
    _write_manifest(manifest_path, manifest)

    missing_wire = _run(tmp_path, manifest_path, "validate")

    assert missing_wire.returncode != 0
    assert "wire_evidence" in missing_wire.stderr

    artifact["admission"]["records"].pop()
    _append_admission(artifact, original)
    del artifact["admission"]["records"][-1]["operator_approval"]
    _write_manifest(manifest_path, manifest)

    missing_approval = _run(tmp_path, manifest_path, "validate")

    assert missing_approval.returncode != 0
    assert "operator_approval" in missing_approval.stderr


def test_admission_prior_hash_must_chain(tmp_path: Path) -> None:
    _, manifest_path, manifest = _fixture(tmp_path)
    artifact = manifest["artifacts"][0]
    _append_admission(artifact, artifact["sha256"])
    artifact["admission"]["records"][-1]["prior_sha256"] = "4" * 64
    _write_manifest(manifest_path, manifest)

    checked = _run(tmp_path, manifest_path, "validate")

    assert checked.returncode != 0
    assert "prior_sha256: chain break" in checked.stderr


def test_complete_chained_admission_verifies(tmp_path: Path) -> None:
    database, manifest_path, manifest = _fixture(tmp_path)
    with sqlite3.connect(database) as connection:
        connection.execute(
            "INSERT INTO documents VALUES ('source::two', 2, 'source::two')"
        )
    artifact = manifest["artifacts"][0]
    _append_admission(artifact, _sha256(database))
    artifact["bytes"] = database.stat().st_size
    artifact["expected"]["documents"] = 2
    _write_manifest(manifest_path, manifest)

    validated = _run(tmp_path, manifest_path, "validate")
    verified = _run(tmp_path, manifest_path, "verify")

    assert validated.returncode == 0, validated.stderr
    assert verified.returncode == 0, verified.stderr
    assert "protected evidence: 1/1 artifacts match" in verified.stdout


def test_pinned_evidence_file_is_checked_by_validate(tmp_path: Path) -> None:
    _, manifest_path, manifest = _fixture(tmp_path)
    evidence_dir = tmp_path / "evidence"
    evidence_dir.mkdir()
    report = evidence_dir / "report.json"
    report.write_text('{"complete":true}\n', encoding="utf-8")
    manifest["pinned_files"].append(
        {
            "path": "evidence/report.json",
            "grade": "supporting",
            "sha256": _sha256(report),
            "bytes": report.stat().st_size,
            "purpose": "corpus-free evidence hash-pin control",
            "provenance": "created inside one disposable pytest directory",
        }
    )
    _write_manifest(manifest_path, manifest)

    clean = _run(tmp_path, manifest_path, "validate")
    assert clean.returncode == 0, clean.stderr
    assert "PIN MATCH evidence/report.json" in clean.stdout

    report.write_text('{"complete":false}\n', encoding="utf-8")
    changed = _run(tmp_path, manifest_path, "validate")
    assert changed.returncode == 1
    assert "MISMATCH evidence/report.json field=sha256" in changed.stderr


def _candidate_pin(path: str, grade: str) -> dict[str, Any]:
    return {
        "path": path,
        "grade": grade,
        "sha256": "1" * 64,
        "bytes": 1,
        "purpose": "observation-prefix rejection control",
        "provenance": "disposable malformed fixture",
    }


def test_observation_path_rejects_non_observation_grade(
    tmp_path: Path,
) -> None:
    _, manifest_path, manifest = _fixture(tmp_path)
    manifest["pinned_files"].append(
        _candidate_pin("observations/body.xml", "supporting")
    )
    _write_manifest(manifest_path, manifest)

    checked = _run(tmp_path, manifest_path, "validate")

    assert checked.returncode == 2
    assert (
        "pinned_files[0].grade: expected one of ['observation'] "
        "for observations/body.xml"
    ) in checked.stderr
    print(f"observation-pin-rejection-1: {checked.stderr.strip()}")


def test_observation_grade_rejects_path_outside_observations(
    tmp_path: Path,
) -> None:
    _, manifest_path, manifest = _fixture(tmp_path)
    manifest["pinned_files"].append(
        _candidate_pin("evidence/report.json", "observation")
    )
    _write_manifest(manifest_path, manifest)

    checked = _run(tmp_path, manifest_path, "validate")

    assert checked.returncode == 2
    assert (
        "pinned_files[0].grade: expected one of "
        "['legacy', 'release', 'structural', 'supporting'] "
        "for evidence/report.json"
    ) in checked.stderr
    print(f"observation-pin-rejection-2: {checked.stderr.strip()}")


def test_pin_path_rejects_unregistered_prefix(tmp_path: Path) -> None:
    _, manifest_path, manifest = _fixture(tmp_path)
    manifest["pinned_files"].append(
        _candidate_pin("outside/body.xml", "observation")
    )
    _write_manifest(manifest_path, manifest)

    checked = _run(tmp_path, manifest_path, "validate")

    assert checked.returncode == 2
    assert (
        "pinned_files[0].path: pinned files must live beneath evidence/, "
        "observations/, or be an exact registered authorization surface"
    ) in checked.stderr
    print(f"observation-pin-rejection-3: {checked.stderr.strip()}")


def test_only_registered_authorization_pins_may_live_outside_evidence(
    tmp_path: Path,
) -> None:
    _, manifest_path, manifest = _fixture(tmp_path)
    controller = tmp_path / "tools" / "model_profiles.py"
    controller.parent.mkdir()
    controller.write_text("print('controller')\n")
    runner = tmp_path / "run"
    runner.write_text("#!/bin/sh\n")
    for path in (runner, controller):
        manifest["pinned_files"].append(
            {
                "path": str(path.relative_to(tmp_path)),
                "grade": "authorization",
                "sha256": _sha256(path),
                "bytes": path.stat().st_size,
                "purpose": "authorization-surface pin control",
                "provenance": "created inside one disposable pytest directory",
            }
        )
    _write_manifest(manifest_path, manifest)

    allowed = _run(tmp_path, manifest_path, "validate")
    assert allowed.returncode == 0, allowed.stderr

    manifest["pinned_files"].append(
        {
            "path": "outside.json",
            "grade": "supporting",
            "sha256": "1" * 64,
            "bytes": 1,
            "purpose": "unsafe path control",
            "provenance": "disposable malformed fixture",
        }
    )
    _write_manifest(manifest_path, manifest)

    checked = _run(tmp_path, manifest_path, "validate")
    assert checked.returncode == 2
    assert "must live beneath evidence/" in checked.stderr


def test_committed_pins_reject_one_byte_mutations(
    tmp_path: Path,
) -> None:
    manifest = json.loads(
        (ROOT / "config" / "protected-artifacts.json").read_text()
    )
    for pinned_file in manifest["pinned_files"]:
        source = ROOT / pinned_file["path"]
        destination = tmp_path / pinned_file["path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(source.read_bytes())
    manifest_path = tmp_path / "config" / "protected-artifacts.json"
    manifest_path.parent.mkdir(parents=True)
    _write_manifest(manifest_path, manifest)

    clean = _run(tmp_path, manifest_path, "validate")
    assert clean.returncode == 0, clean.stderr

    runner = tmp_path / "run"
    runner.write_bytes(runner.read_bytes() + b"\n")
    changed_runner = _run(tmp_path, manifest_path, "validate")
    assert changed_runner.returncode == 1
    assert "MISMATCH run field=sha256" in changed_runner.stderr
    runner.write_bytes((ROOT / "run").read_bytes())

    receipt = (
        tmp_path
        / "evidence"
        / "v0.10.1"
        / "deferred-audit"
        / "report.json"
    )
    receipt.write_bytes(receipt.read_bytes() + b"\n")
    changed = _run(tmp_path, manifest_path, "validate")

    assert changed.returncode == 1
    assert (
        "MISMATCH evidence/v0.10.1/deferred-audit/report.json field=sha256"
        in changed.stderr
    )
    receipt.write_bytes(
        (
            ROOT
            / "evidence"
            / "v0.10.1"
            / "deferred-audit"
            / "report.json"
        ).read_bytes()
    )

    observation = (
        tmp_path
        / "observations"
        / "v0.25"
        / "feed-shape"
        / "sec-edgar-usgaap.rss.xml"
    )
    mutated = bytearray(observation.read_bytes())
    mutated[-1] ^= 1
    observation.write_bytes(mutated)
    changed_observation = _run(tmp_path, manifest_path, "validate")

    assert changed_observation.returncode == 1
    assert (
        "MISMATCH observations/v0.25/feed-shape/"
        "sec-edgar-usgaap.rss.xml field=sha256"
    ) in changed_observation.stderr
    print(
        "observation-pin-byte-rejection: "
        f"{changed_observation.stderr.strip()}"
    )


def _append_report_pin(
    manifest: dict[str, Any],
    report: Path,
    *,
    grade: str,
) -> None:
    manifest["pinned_files"].append(
        {
            "path": str(report.relative_to(report.parents[1])),
            "grade": grade,
            "sha256": _sha256(report),
            "bytes": report.stat().st_size,
            "purpose": "deferred-audit evidence-grade control",
            "provenance": "created inside one disposable pytest directory",
        }
    )


def test_structural_report_cannot_be_pinned_as_release_grade(
    tmp_path: Path,
) -> None:
    _, manifest_path, manifest = _fixture(tmp_path)
    evidence_dir = tmp_path / "evidence"
    evidence_dir.mkdir()
    report = evidence_dir / "report.json"
    report.write_text(
        json.dumps(
            {
                "evidence_grade": "structural",
                "attestations_required": False,
                "measurements": {
                    "ci_runner": {"accepted_runner_receipts": []}
                },
            }
        )
        + "\n"
    )
    _append_report_pin(manifest, report, grade="release")
    _write_manifest(manifest_path, manifest)

    checked = _run(tmp_path, manifest_path, "validate")

    assert checked.returncode == 1
    assert (
        "PIN MISMATCH evidence/report.json field=evidence_grade"
        in checked.stderr
    )


def test_genuine_release_grade_report_pin_validates(tmp_path: Path) -> None:
    _, manifest_path, manifest = _fixture(tmp_path)
    evidence_dir = tmp_path / "evidence"
    evidence_dir.mkdir()
    receipt = evidence_dir / "receipt.json"
    receipt.write_text('{"receipt":true}\n')
    bundle = evidence_dir / "receipt.json.sigstore"
    bundle.write_text('{"bundle":true}\n')
    report = evidence_dir / "report.json"
    report.write_text(
        json.dumps(
            {
                "evidence_grade": "release",
                "attestations_required": True,
                "measurements": {
                    "ci_runner": {
                        "expected_source_digest": "a" * 40,
                        "expected_source_ref": "refs/heads/main",
                        "accepted_runner_receipts": [
                            {
                                "path": "evidence/receipt.json",
                                "attestation_bundle": (
                                    "evidence/receipt.json.sigstore"
                                ),
                                "attestation_verified": True,
                                "certificate_identity": (
                                    "https://example.test/workflow"
                                ),
                                "signer_digest": "a" * 40,
                                "source_digest": "a" * 40,
                                "source_ref": "refs/heads/main",
                            }
                        ]
                    }
                },
            }
        )
        + "\n"
    )
    _append_report_pin(manifest, report, grade="release")
    _append_report_pin(manifest, receipt, grade="supporting")
    _append_report_pin(manifest, bundle, grade="supporting")
    _write_manifest(manifest_path, manifest)

    checked = _run(tmp_path, manifest_path, "validate")

    assert checked.returncode == 0, checked.stderr
    assert "PIN MATCH evidence/report.json" in checked.stdout


def test_release_grade_report_rejects_unresolved_recorded_paths(
    tmp_path: Path,
) -> None:
    _, manifest_path, manifest = _fixture(tmp_path)
    evidence_dir = tmp_path / "evidence"
    evidence_dir.mkdir()
    report = evidence_dir / "report.json"
    report.write_text(
        json.dumps(
            {
                "evidence_grade": "release",
                "attestations_required": True,
                "measurements": {
                    "ci_runner": {
                        "expected_source_digest": "a" * 40,
                        "expected_source_ref": "refs/heads/main",
                        "accepted_runner_receipts": [
                            {
                                "path": "evidence/missing-receipt.json",
                                "attestation_bundle": (
                                    "evidence/missing-receipt.json.sigstore"
                                ),
                                "attestation_verified": True,
                                "certificate_identity": (
                                    "https://example.test/workflow"
                                ),
                                "signer_digest": "a" * 40,
                                "source_digest": "a" * 40,
                                "source_ref": "refs/heads/main",
                            }
                        ]
                    }
                },
            }
        )
        + "\n"
    )
    _append_report_pin(manifest, report, grade="release")
    _write_manifest(manifest_path, manifest)

    checked = _run(tmp_path, manifest_path, "validate")

    assert checked.returncode == 1
    assert (
        "field=accepted_runner_receipts: recorded receipt path is not pinned"
        in checked.stderr
    )
