from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools" / "python_constraints.py"
CONSTRAINTS = ROOT / "shell" / "constraints.txt"


def _run(constraints: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(TOOL), str(constraints)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def test_active_environment_exactly_matches_constraints() -> None:
    result = _run(CONSTRAINTS)

    assert result.returncode == 0, result.stderr
    assert "python-constraints: PASS" in result.stdout
    assert "packages=21" in result.stdout


def test_patch_drift_names_expected_and_installed_versions(
    tmp_path: Path,
) -> None:
    changed = tmp_path / "constraints.txt"
    changed.write_text(
        CONSTRAINTS.read_text(encoding="utf-8").replace(
            "fastapi==0.140.0",
            "fastapi==0.140.1",
        ),
        encoding="utf-8",
    )

    result = _run(changed)

    assert result.returncode != 0
    assert "fastapi: expected 0.140.1, found 0.140.0" in result.stderr


def test_non_exact_constraint_is_rejected(tmp_path: Path) -> None:
    unpinned = tmp_path / "constraints.txt"
    unpinned.write_text("fastapi>=0.110\n", encoding="utf-8")

    result = _run(unpinned)

    assert result.returncode != 0
    assert "expected an exact name==version pin" in result.stderr
