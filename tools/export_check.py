#!/usr/bin/env python3
"""Verify that a Repomix review export contains every required source path."""

from __future__ import annotations

import argparse
import json
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

FILE_PATH_RE = re.compile(r'^<file path="([^"]+)">\r?$', re.MULTILINE)
CYCLE_DOCUMENT_RE = re.compile(
    r"^docs/cycles/(?:TASKS|PROGRESS)-"
    r"v[0-9]+(?:\.[0-9]+)*(?:-EXECUTION)?\.md$"
)
EXECUTION_RUNBOOK_PATH_RE = re.compile(
    r"^docs/cycles/TASKS-(v[0-9]+(?:\.[0-9]+)*)-EXECUTION\.md$"
)
MAX_EXPORT_BYTES = 3_000_000
CYCLE_RETENTION_DEPTH = 2
GLOB_META = frozenset("*?[]{}")


class ExportCheckError(RuntimeError):
    """The export or its repository source set could not be inspected."""


def tracked_repository_paths(root: Path) -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--"],
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


def derived_required_paths(root: Path) -> set[str]:
    """Derive review-critical paths without a hand-maintained path list."""
    tracked = tracked_repository_paths(root)
    retained_cycles = expected_retained_cycle_paths(root)
    excluded_cycles = tracked_cycle_paths(root) - retained_cycles
    excluded_raw_wire = derived_raw_wire_paths(root)
    excluded_prefixes = (
        derived_bulk_evidence_prefixes(root)
        | derived_structural_archive_prefixes(root)
    )
    excluded_by_prefix = {
        path
        for path in tracked
        if any(path.startswith(prefix) for prefix in excluded_prefixes)
    }
    return tracked - excluded_cycles - excluded_raw_wire - excluded_by_prefix


def tracked_cycle_paths(root: Path) -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", "docs/cycles"],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        detail = result.stderr.decode(errors="replace").strip()
        raise ExportCheckError(
            f"git ls-files for cycle documents failed with exit "
            f"{result.returncode}{f': {detail}' if detail else ''}"
        )
    return {
        path
        for raw in result.stdout.split(b"\0")
        if raw
        if (path := raw.decode(errors="strict"))
        if CYCLE_DOCUMENT_RE.fullmatch(path) is not None
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
    tracked_cycles = tracked_cycle_paths(root)
    candidates = sorted(
        (
            version,
            root / raw_path,
        )
        for raw_path in tracked_cycles
        if EXECUTION_RUNBOOK_PATH_RE.fullmatch(raw_path) is not None
        if (
            (version := cycle_name_version(
                EXECUTION_RUNBOOK_PATH_RE.fullmatch(raw_path).group(1)
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
        runbook_path = runbook.relative_to(root).as_posix()
        progress_path = progress.relative_to(root).as_posix()
        if progress_path not in tracked_cycles:
            raise ExportCheckError(
                f"retained progress record is not tracked: {progress_path}"
            )
        expected.add(runbook_path)
        expected.add(progress_path)
    return expected


def repomix_custom_patterns(root: Path) -> tuple[str, ...]:
    root = root.resolve()
    config_path = root / "repomix.config.json"
    try:
        config = json.loads(config_path.read_text())
        patterns = config["ignore"]["customPatterns"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        raise ExportCheckError(
            f"cannot read Repomix exclusions from {config_path}: {error}"
        ) from error
    if not isinstance(patterns, list) or not all(
        isinstance(pattern, str) for pattern in patterns
    ):
        raise ExportCheckError("Repomix customPatterns must be a string list")
    return tuple(patterns)


def pinned_file_records(root: Path) -> tuple[dict[str, object], ...]:
    manifest_path = root / "config/protected-artifacts.json"
    try:
        raw = json.loads(manifest_path.read_text())
        records = raw["pinned_files"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        raise ExportCheckError(
            f"cannot read pinned-file records from {manifest_path}: {error}"
        ) from error
    if not isinstance(records, list) or not all(
        isinstance(record, dict) for record in records
    ):
        raise ExportCheckError("protected pinned_files must be an object list")
    return tuple(records)


def derived_raw_wire_paths(root: Path) -> set[str]:
    """Derive pinned raw publisher bodies from their byte-preservation marks."""
    root = root.resolve()
    candidates = sorted(
        path
        for record in pinned_file_records(root)
        if record.get("grade") == "observation"
        if isinstance(path := record.get("path"), str)
        if path.startswith("observations/")
    )
    if not candidates:
        return set()
    result = subprocess.run(
        ["git", "check-attr", "-z", "binary", "--", *candidates],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        detail = result.stderr.decode(errors="replace").strip()
        raise ExportCheckError(
            f"git check-attr failed with exit {result.returncode}"
            f"{f': {detail}' if detail else ''}"
        )
    fields = result.stdout.split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()
    if len(fields) % 3 != 0:
        raise ExportCheckError("git check-attr returned malformed binary records")
    derived: set[str] = set()
    for index in range(0, len(fields), 3):
        path, attribute, value = (
            field.decode(errors="strict") for field in fields[index : index + 3]
        )
        if attribute != "binary":
            raise ExportCheckError(
                f"git check-attr returned unexpected attribute {attribute!r}"
            )
        if value == "set":
            derived.add(path)
    return derived


def configured_raw_wire_exclusions(root: Path) -> set[str]:
    configured: set[str] = set()
    for raw_path in repomix_custom_patterns(root):
        if not raw_path.startswith("observations/"):
            continue
        if any(character in raw_path for character in GLOB_META):
            continue
        if not (root / raw_path).is_file():
            raise ExportCheckError(
                f"invalid exact Repomix observation exclusion: {raw_path}"
            )
        configured.add(raw_path)
    return configured


def raw_wire_exclusion_errors(
    derived: set[str],
    configured: set[str],
) -> list[str]:
    errors: list[str] = []
    # Invariant R12 control site: derived raw-wire exclusion population.
    if not derived:
        errors.append("derived raw-wire exclusion class is empty")
    # Invariant R12 control site: every derived raw-wire body is excluded.
    errors.extend(
        f"derived raw-wire body lacks an exact Repomix exclusion: {path}"
        for path in sorted(derived - configured)
    )
    # Invariant R12 control site: every exact observation exclusion is raw wire.
    errors.extend(
        f"exact Repomix observation exclusion is not derived raw wire: {path}"
        for path in sorted(configured - derived)
    )
    return errors


def excluded_export_paths(root: Path) -> set[str]:
    derived = derived_raw_wire_paths(root)
    configured = configured_raw_wire_exclusions(root)
    errors = raw_wire_exclusion_errors(derived, configured)
    if errors:
        raise ExportCheckError("; ".join(errors))
    return derived


def derived_structural_archive_prefixes(root: Path) -> set[str]:
    return {
        f"{Path(path).parent.as_posix()}/"
        for record in pinned_file_records(root)
        if record.get("grade") == "structural"
        if isinstance(path := record.get("path"), str)
        if not path.startswith("evidence/")
    }


def derived_bulk_evidence_prefixes(root: Path) -> set[str]:
    patterns = set(repomix_custom_patterns(root))
    prefixes: set[str] = set()
    for record in pinned_file_records(root):
        path = record.get("path")
        if not isinstance(path, str) or "/" not in path:
            continue
        prefix = f"{path.split('/', 1)[0]}/"
        if f"{prefix}**" in patterns:
            prefixes.add(prefix)
    return prefixes


def configured_structural_archive_prefixes(root: Path) -> set[str]:
    patterns = set(repomix_custom_patterns(root))
    expected = derived_structural_archive_prefixes(root)
    configured = {
        prefix
        for prefix in expected
        if f"{prefix}**" in patterns
    }
    if configured != expected:
        missing = ", ".join(sorted(expected - configured))
        raise ExportCheckError(
            f"missing derived structural-archive Repomix exclusion: {missing}"
        )
    return configured


def untracked_export_errors(
    tracked: set[str],
    actual: set[str],
) -> list[str]:
    # Invariant R12 control site: review export contains only Git-tracked bytes.
    return [
        f"export contains untracked path: {path}"
        for path in sorted(actual - tracked)
    ]


def check_export(
    root: Path,
    export_path: Path,
) -> tuple[set[str], set[str], list[str]]:
    root = root.resolve()
    export_path = export_path.resolve()
    tracked = tracked_repository_paths(root)
    sources = derived_required_paths(root)
    actual = exported_paths(export_path)
    expected_cycles = expected_retained_cycle_paths(root)
    excluded_paths = excluded_export_paths(root)
    actual_cycles = {
        path for path in actual if CYCLE_DOCUMENT_RE.fullmatch(path) is not None
    }
    errors = [
        f"missing derived required path: {path}"
        for path in sorted(sources - actual)
    ]
    errors.extend(untracked_export_errors(tracked, actual))
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
    archive_prefixes = configured_structural_archive_prefixes(root)
    errors.extend(
        f"excluded export prefix is present: {prefix}"
        for prefix in archive_prefixes
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
            f"derived_required={len(sources)}, exported={len(actual)})",
            file=sys.stderr,
        )
        return 1
    print(
        "export-check: PASS "
        f"(derived_required={len(sources)}, "
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
