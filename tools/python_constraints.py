#!/usr/bin/env python3
"""Verify that the active interpreter exactly matches pinned constraints."""

from __future__ import annotations

import argparse
import importlib.metadata
import re
import sys
from pathlib import Path

PIN_RE = re.compile(r"^([A-Za-z0-9][A-Za-z0-9._-]*)==([^\s;]+)$")
BOOTSTRAP_PACKAGES = {"pip", "setuptools", "wheel"}


class ConstraintError(ValueError):
    """A constraint file or installed environment is not reproducible."""


def canonical_name(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def load_constraints(path: Path) -> dict[str, str]:
    pins: dict[str, str] = {}
    for line_number, raw_line in enumerate(
        path.read_text(encoding="utf-8").splitlines(),
        start=1,
    ):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        match = PIN_RE.fullmatch(line)
        if match is None:
            raise ConstraintError(
                f"{path}:{line_number}: expected an exact name==version pin"
            )
        name = canonical_name(match.group(1))
        if name in pins:
            raise ConstraintError(
                f"{path}:{line_number}: duplicate pin for {name}"
            )
        pins[name] = match.group(2)
    if not pins:
        raise ConstraintError(f"{path}: expected at least one exact pin")
    return pins


def installed_versions() -> dict[str, str]:
    installed: dict[str, str] = {}
    for distribution in importlib.metadata.distributions():
        raw_name = distribution.metadata.get("Name")
        if not raw_name:
            raise ConstraintError(
                "installed distribution has no Name metadata: "
                f"{distribution!r}"
            )
        name = canonical_name(raw_name)
        if name in BOOTSTRAP_PACKAGES:
            continue
        if name in installed:
            raise ConstraintError(f"installed distribution is duplicated: {name}")
        installed[name] = distribution.version
    return installed


def compare(
    expected: dict[str, str],
    actual: dict[str, str],
) -> list[str]:
    problems: list[str] = []
    for name in sorted(expected.keys() - actual.keys()):
        problems.append(f"{name}: expected {expected[name]}, not installed")
    for name in sorted(expected.keys() & actual.keys()):
        if expected[name] != actual[name]:
            problems.append(
                f"{name}: expected {expected[name]}, found {actual[name]}"
            )
    for name in sorted(actual.keys() - expected.keys()):
        problems.append(f"{name}: unexpected installed version {actual[name]}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare this interpreter with an exact constraints file."
    )
    parser.add_argument("constraints", type=Path)
    args = parser.parse_args()

    try:
        expected = load_constraints(args.constraints)
        problems = compare(expected, installed_versions())
    except (ConstraintError, OSError) as error:
        print(f"python-constraints: FAIL: {error}", file=sys.stderr)
        return 1

    if problems:
        print("python-constraints: FAIL", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1

    print(
        "python-constraints: PASS "
        f"(python={sys.version.split()[0]}, packages={len(expected)})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
