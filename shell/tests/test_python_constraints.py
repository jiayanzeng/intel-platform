from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

import tools.python_constraints as python_constraints
from tools.python_constraints import (
    ConstraintError,
    compare,
    installed_versions,
    load_constraints,
)

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
) -> None:
    expected = load_constraints(CONSTRAINTS)
    expected["fastapi"] = "0.140.1"
    distributions = [
        SimpleNamespace(metadata={"Name": name}, version=version)
        for name, version in load_constraints(CONSTRAINTS).items()
    ]

    problems = compare(expected, installed_versions(distributions))

    assert problems == ["fastapi: expected 0.140.1, found 0.140.0"]


def test_patch_drift_ignores_an_ambient_duplicate_inventory(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    expected = load_constraints(CONSTRAINTS)
    expected["fastapi"] = "0.140.1"
    constrained = [
        SimpleNamespace(metadata={"Name": name}, version=version)
        for name, version in load_constraints(CONSTRAINTS).items()
    ]
    ambient = [
        *constrained,
        SimpleNamespace(metadata={"Name": "colorama"}, version="0.4.6"),
        SimpleNamespace(metadata={"Name": "colorama"}, version="0.4.6"),
    ]
    monkeypatch.setattr(
        python_constraints.importlib.metadata,
        "distributions",
        lambda: ambient,
    )

    problems = compare(expected, installed_versions(constrained))

    assert problems == ["fastapi: expected 0.140.1, found 0.140.0"]
    with pytest.raises(
        ConstraintError,
        match="installed distribution is duplicated: colorama",
    ):
        installed_versions()


def test_duplicate_injected_distribution_is_rejected() -> None:
    duplicate = [
        SimpleNamespace(metadata={"Name": "fastapi"}, version="0.140.0"),
        SimpleNamespace(metadata={"Name": "FastAPI"}, version="0.140.0"),
    ]

    with pytest.raises(
        ConstraintError,
        match="installed distribution is duplicated: fastapi",
    ):
        installed_versions(duplicate)


def test_non_exact_constraint_is_rejected(tmp_path: Path) -> None:
    unpinned = tmp_path / "constraints.txt"
    unpinned.write_text("fastapi>=0.110\n", encoding="utf-8")

    result = _run(unpinned)

    assert result.returncode != 0
    assert "expected an exact name==version pin" in result.stderr
