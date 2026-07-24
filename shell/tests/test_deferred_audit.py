from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from tools.audit_deferred import control_measurements, evaluate


ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools" / "audit_deferred.py"


def test_synthetic_two_harvesters_and_writers_promote_both() -> None:
    rows = {row["id"]: row for row in evaluate(control_measurements())}
    assert rows["T7 robots single-flight"]["disposition"] == "promote"
    assert rows["Postgres"]["disposition"] == "promote"
    assert rows["pgvector"]["disposition"] == "defer"
    assert rows["Multi-host seam hardening"]["disposition"] == "defer"
    assert rows["/view materialization"]["disposition"] == "defer"


def test_control_command_exits_nonzero_and_names_both_triggers() -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(TOOL),
            "--control",
            "two-harvesters-two-writers",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode != 0
    assert "PROMOTE T7 robots single-flight" in result.stdout
    assert "PROMOTE Postgres" in result.stdout
    assert "CONTROL FIRED" in result.stdout


def test_each_row_keeps_its_unchanged_trigger() -> None:
    rows = evaluate(control_measurements())
    assert len(rows) == 5
    assert all(row["unchanged_trigger"] for row in rows)
