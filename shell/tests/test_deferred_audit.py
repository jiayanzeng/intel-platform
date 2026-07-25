from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from tools.audit_deferred import (
    attestation_boundary_measurement,
    control_measurements,
    evaluate,
)


ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools" / "audit_deferred.py"


def test_synthetic_measurements_promote_all_seven() -> None:
    rows = {row["id"]: row for row in evaluate(control_measurements())}
    assert len(rows) == 7
    assert all(row["disposition"] == "promote" for row in rows.values())


def test_control_command_exits_nonzero_and_names_both_triggers() -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(TOOL),
            "--control",
            "all-seven",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode != 0
    for item in (
        "T7 robots single-flight",
        "Postgres",
        "pgvector",
        "Multi-host seam hardening",
        "A4 untrusted-shell attestation boundary",
        "CI-runner evidence",
        "/view materialization",
    ):
        assert f"PROMOTE {item}" in result.stdout
    assert "CONTROL FIRED: all seven" in result.stdout


def test_each_row_keeps_its_unchanged_trigger() -> None:
    rows = evaluate(control_measurements())
    assert len(rows) == 7
    assert all(row["unchanged_trigger"] for row in rows)


def test_registry_trigger_text_is_not_an_affirmative_hc1_claim() -> None:
    measurement = attestation_boundary_measurement()
    assert measurement["hc1_invariant_under_shell_replacement_claims"] == []
