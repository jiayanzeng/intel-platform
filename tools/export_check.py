#!/usr/bin/env python3
"""Verify that a Repomix review export contains every required source path."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


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


def check_export(
    root: Path,
    export_path: Path,
) -> tuple[set[str], set[str], list[str]]:
    sources = tracked_source_paths(root)
    actual = exported_paths(export_path)
    errors = [
        f"missing derived source path: {path}"
        for path in sorted(sources - actual)
    ]
    errors.extend(
        f"missing required path: {path}"
        for path in REQUIRED_PATHS
        if path not in actual
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
            f"export-check: FAIL ({len(errors)} missing path(s); "
            f"derived_sources={len(sources)}, exported={len(actual)})",
            file=sys.stderr,
        )
        return 1
    print(
        "export-check: PASS "
        f"(derived_sources={len(sources)}, required={len(REQUIRED_PATHS)}, "
        f"exported={len(actual)})"
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
