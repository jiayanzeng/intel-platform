#!/usr/bin/env python3
"""Resolve the repository's active execution cycle from its operating contract."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ACTIVE_CYCLE_RE = re.compile(
    r"^\*\*Active cycle:\*\* (v[0-9]+(?:\.[0-9]+)*)$"
)


class CycleIdentityError(RuntimeError):
    """The active-cycle declaration is absent or ambiguous."""


@dataclass(frozen=True)
class CycleIdentity:
    name: str
    declaration: Path
    runbook: Path
    progress: Path


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
