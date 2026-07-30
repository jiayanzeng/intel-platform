#!/usr/bin/env python3
"""Verify that a Repomix review export contains every required source path."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.cycle_identity import (
    CycleIdentityError,
    execution_runbooks,
    progress_for_runbook,
    resolve_cycle,
)

SOURCE_ROOTS = ("crates", "apps", "tools", "shell")
REQUIRED_PATHS = (
    ".github/workflows/ci.yml",
    "AGENTS.md",
    "Cargo.lock",
    "Cargo.toml",
    "config/protected-artifacts.json",
    "run",
    "rust-toolchain.toml",
)
FILE_PATH_RE = re.compile(r'^<file path="([^"]+)">\r?$', re.MULTILINE)
CYCLE_DOCUMENT_RE = re.compile(
    r"^docs/cycles/(?:TASKS|PROGRESS)-"
    r"v[0-9]+(?:\.[0-9]+)*(?:-EXECUTION)?\.md$"
)
MAX_EXPORT_BYTES = 3_000_000
CYCLE_RETENTION_DEPTH = 3
EXCLUDED_EXPORT_FILENAMES = ("sec-edgar-usgaap.rss.xml",)
EXCLUDED_EXPORT_PREFIXES = ("docs/state-archive/",)


class ExportCheckError(RuntimeError):
    """The export or its repository source set could not be inspected."""


def tracked_source_paths(root: Path) -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", *SOURCE_ROOTS],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        detail = result.stderr.decode(errors="replace").strip()
        raise ExportCheckError(
            f"git ls-files failed with exit {result.returncode}"
            f"{f': {detail}' if detail else ''}"
        )
    return {
        raw.decode(errors="strict")
        for raw in result.stdout.split(b"\0")
        if raw
    }


def exported_paths(export_path: Path) -> set[str]:
    try:
        text = export_path.read_text()
    except OSError as error:
        raise ExportCheckError(f"cannot read export {export_path}: {error}") from error
    paths = set(FILE_PATH_RE.findall(text))
    if not paths:
        raise ExportCheckError(
            f"{export_path}: no Repomix <file path=\"...\"> entries found"
        )
    return paths


def cycle_name_version(name: str) -> tuple[int, ...]:
    match = re.fullmatch(r"v([0-9]+(?:\.[0-9]+)*)", name)
    if match is None:
        raise ExportCheckError(f"invalid cycle name {name!r}")
    return tuple(int(part) for part in match.group(1).split("."))


def expected_retained_cycle_paths(root: Path) -> set[str]:
    root = root.resolve()
    try:
        identity = resolve_cycle(root)
    except CycleIdentityError as error:
        raise ExportCheckError(str(error)) from error
    active_version = cycle_name_version(identity.name)
    candidates = sorted(
        (
            version,
            path,
        )
        for path in execution_runbooks(root)
        if (
            (version := cycle_name_version(
                path.name.removeprefix("TASKS-").removesuffix(
                    "-EXECUTION.md"
                )
            ))
            <= active_version
        )
    )
    if (
        len(candidates) < CYCLE_RETENTION_DEPTH
        or candidates[-1][1].resolve() != identity.runbook.resolve()
    ):
        raise ExportCheckError(
            f"cannot derive {CYCLE_RETENTION_DEPTH}-cycle retention set "
            f"ending at {identity.name}"
        )
    expected: set[str] = set()
    for _, runbook in candidates[-CYCLE_RETENTION_DEPTH:]:
        progress = progress_for_runbook(root, runbook)
        if progress is None:
            raise ExportCheckError(
                f"no progress record resolves for {runbook.relative_to(root)}"
            )
        expected.add(runbook.relative_to(root).as_posix())
        expected.add(progress.relative_to(root).as_posix())
    return expected


def excluded_export_paths(root: Path) -> set[str]:
    excluded: set[str] = set()
    observations = root.resolve() / "observations"
    for filename in EXCLUDED_EXPORT_FILENAMES:
        matches = sorted(observations.glob(f"**/{filename}"))
        if len(matches) != 1:
            raise ExportCheckError(
                f"expected exactly one observations/**/{filename}, "
                f"found {len(matches)}"
            )
        excluded.add(matches[0].relative_to(root.resolve()).as_posix())
    return excluded


def check_export(
    root: Path,
    export_path: Path,
) -> tuple[set[str], set[str], list[str]]:
    root = root.resolve()
    export_path = export_path.resolve()
    sources = tracked_source_paths(root)
    actual = exported_paths(export_path)
    expected_cycles = expected_retained_cycle_paths(root)
    excluded_paths = excluded_export_paths(root)
    actual_cycles = {
        path for path in actual if CYCLE_DOCUMENT_RE.fullmatch(path) is not None
    }
    errors = [
        f"missing derived source path: {path}"
        for path in sorted(sources - actual)
    ]
    errors.extend(
        f"missing required path: {path}"
        for path in REQUIRED_PATHS
        if path not in actual
    )
    export_bytes = export_path.stat().st_size
    if export_bytes > MAX_EXPORT_BYTES:
        errors.append(
            f"export size {export_bytes} exceeds ceiling {MAX_EXPORT_BYTES}"
        )
    errors.extend(
        f"missing retained cycle document: {path}"
        for path in sorted(expected_cycles - actual_cycles)
    )
    errors.extend(
        f"unexpected cycle document outside retention depth "
        f"{CYCLE_RETENTION_DEPTH}: {path}"
        for path in sorted(actual_cycles - expected_cycles)
    )
    errors.extend(
        f"excluded export path is present: {path}"
        for path in sorted(excluded_paths)
        if path in actual
    )
    errors.extend(
        f"excluded export prefix is present: {prefix}"
        for prefix in EXCLUDED_EXPORT_PREFIXES
        if any(path.startswith(prefix) for path in actual)
    )
    return sources, actual, errors


def run(root: Path, export_path: Path) -> int:
    try:
        sources, actual, errors = check_export(root, export_path)
    except ExportCheckError as error:
        print(f"export-check: ERROR: {error}", file=sys.stderr)
        print("export-check: FAIL (inspection unavailable)", file=sys.stderr)
        return 2
    for error in errors:
        print(f"export-check: ERROR: {error}", file=sys.stderr)
    if errors:
        print(
            f"export-check: FAIL ({len(errors)} defect(s); "
            f"derived_sources={len(sources)}, exported={len(actual)})",
            file=sys.stderr,
        )
        return 1
    print(
        "export-check: PASS "
        f"(derived_sources={len(sources)}, required={len(REQUIRED_PATHS)}, "
        f"exported={len(actual)}, bytes={export_path.stat().st_size}, "
        f"retained_cycles={CYCLE_RETENTION_DEPTH})"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check a freshly written Repomix export against Git paths."
    )
    parser.add_argument("export", type=Path)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root used for git ls-files (default: this checkout)",
    )
    args = parser.parse_args()
    return run(args.root.resolve(), args.export.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
