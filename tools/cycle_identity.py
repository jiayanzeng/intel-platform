#!/usr/bin/env python3
"""Resolve the repository's active execution cycle from its operating contract."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ACTIVE_CYCLE_RE = re.compile(
    r"^\*\*Active cycle:\*\* (v[0-9]+(?:\.[0-9]+)*)$"
)
HISTORICAL_KEY_RE = re.compile(r"^[a-z][a-z0-9-]*$")
HISTORICAL_REGISTRY = Path("config/cycle-history.json")


class CycleIdentityError(RuntimeError):
    """The active-cycle declaration is absent or ambiguous."""


@dataclass(frozen=True)
class CycleIdentity:
    name: str
    declaration: Path
    runbook: Path
    progress: Path


def historical_artifacts(root: Path) -> dict[str, Path]:
    root = root.resolve()
    registry = root / HISTORICAL_REGISTRY
    try:
        raw: Any = json.loads(registry.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise CycleIdentityError(f"{registry}: {error}") from error
    if (
        not isinstance(raw, dict)
        or raw.get("schema_version") != 1
        or not isinstance(raw.get("artifacts"), dict)
    ):
        raise CycleIdentityError(
            f"{registry}: expected schema_version 1 and an artifacts object"
        )
    resolved: dict[str, Path] = {}
    seen_paths: set[Path] = set()
    for key, relative in raw["artifacts"].items():
        if (
            not isinstance(key, str)
            or HISTORICAL_KEY_RE.fullmatch(key) is None
            or not isinstance(relative, str)
            or not relative
        ):
            raise CycleIdentityError(
                f"{registry}: artifact keys/paths must be non-empty strings"
            )
        relative_path = Path(relative)
        if relative_path.is_absolute() or ".." in relative_path.parts:
            raise CycleIdentityError(
                f"{registry}: historical artifact path must stay relative: "
                f"{relative!r}"
            )
        path = (root / relative_path).resolve()
        try:
            path.relative_to(root)
        except ValueError as error:
            raise CycleIdentityError(
                f"{registry}: historical artifact escapes repository: "
                f"{relative!r}"
            ) from error
        if not path.is_file():
            raise CycleIdentityError(
                f"{registry}: historical artifact does not exist: "
                f"{relative!r}"
            )
        if path in seen_paths:
            raise CycleIdentityError(
                f"{registry}: historical artifact paths must be unique"
            )
        seen_paths.add(path)
        resolved[key] = path
    return resolved


def historical_artifact_path(root: Path, key: str) -> Path:
    artifacts = historical_artifacts(root)
    try:
        return artifacts[key]
    except KeyError as error:
        raise CycleIdentityError(
            f"{root / HISTORICAL_REGISTRY}: unknown historical artifact "
            f"{key!r}"
        ) from error


def resolve_cycle(root: Path) -> CycleIdentity:
    root = root.resolve()
    contract = root / "AGENTS.md"
    try:
        lines = contract.read_text().splitlines()
    except OSError as error:
        raise CycleIdentityError(f"{contract}: {error}") from error

    matches = [
        (number, match.group(1))
        for number, line in enumerate(lines, 1)
        if (match := ACTIVE_CYCLE_RE.fullmatch(line)) is not None
    ]
    if len(matches) != 1:
        raise CycleIdentityError(
            f"{contract}: expected exactly one line matching "
            "'**Active cycle:** v<major>.<minor>'; "
            f"found {len(matches)}"
        )

    _, name = matches[0]
    return CycleIdentity(
        name=name,
        declaration=contract,
        runbook=root / f"TASKS-{name}-EXECUTION.md",
        progress=root / f"PROGRESS-{name}.md",
    )


def main() -> int:
    if len(sys.argv) != 3 or sys.argv[1] != "historical-artifact":
        print(
            "usage: python3 tools/cycle_identity.py "
            "historical-artifact <semantic-key>",
            file=sys.stderr,
        )
        return 2
    root = Path(__file__).resolve().parents[1]
    try:
        path = historical_artifact_path(root, sys.argv[2])
    except CycleIdentityError as error:
        print(f"cycle-identity: ERROR: {error}", file=sys.stderr)
        return 1
    print(path.relative_to(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
