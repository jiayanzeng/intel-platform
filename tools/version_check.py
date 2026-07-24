#!/usr/bin/env python3
"""Fail when intel-platform's release files or an exact release tag diverge."""

from __future__ import annotations

import ast
import re
import subprocess
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CARGO_TOML = ROOT / "apps/cored/Cargo.toml"
PYTHON_INIT = ROOT / "shell/intel_shell/__init__.py"
FASTAPI_APP = ROOT / "shell/intel_shell/app.py"
STATE = ROOT / "STATE.md"
CHANGELOG = ROOT / "CHANGELOG.md"
TAG_SOURCE = "git describe --tags --abbrev=0"


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def literal_string(node: ast.AST, path: Path, label: str) -> str:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    raise ValueError(f"{relative(path)}: {label} must be a string literal")


def python_package_version() -> str:
    tree = ast.parse(PYTHON_INIT.read_text(), filename=str(PYTHON_INIT))
    values = [
        literal_string(node.value, PYTHON_INIT, "__version__")
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "__version__"
            for target in node.targets
        )
    ]
    if len(values) != 1:
        raise ValueError(
            f"{relative(PYTHON_INIT)}: expected exactly one __version__, "
            f"found {len(values)}"
        )
    return values[0]


def fastapi_version() -> str:
    tree = ast.parse(FASTAPI_APP.read_text(), filename=str(FASTAPI_APP))
    values: list[str] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if not isinstance(node.func, ast.Name) or node.func.id != "FastAPI":
            continue
        for keyword in node.keywords:
            if keyword.arg == "version":
                values.append(
                    literal_string(keyword.value, FASTAPI_APP, "FastAPI version=")
                )
    if len(values) != 1:
        raise ValueError(
            f"{relative(FASTAPI_APP)}: expected exactly one FastAPI version=, "
            f"found {len(values)}"
        )
    return values[0]


def state_version() -> str:
    matches = re.findall(
        r"^\*\*As of:\*\* [^\n]*? · \*\*Version:\*\* v([0-9]+\.[0-9]+\.[0-9]+) "
        r"\(core-shell\)",
        STATE.read_text(),
        flags=re.MULTILINE,
    )
    if len(matches) != 1:
        raise ValueError(
            f"{relative(STATE)}: expected exactly one versioned As-of header, "
            f"found {len(matches)}"
        )
    return matches[0]


def changelog_version() -> str:
    matches = re.findall(
        r"^## v([0-9]+\.[0-9]+\.[0-9]+)(?:\s|$)",
        CHANGELOG.read_text(),
        flags=re.MULTILINE,
    )
    if not matches:
        raise ValueError(
            f"{relative(CHANGELOG)}: expected at least one ## vX.Y.Z heading"
        )
    return matches[0]


def git_output(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def nearest_tag() -> tuple[str, bool] | None:
    described = git_output("describe", "--tags", "--abbrev=0")
    if described.returncode != 0:
        detail = described.stderr.strip() or "no reachable tag"
        print(f"version-check: WARNING: {TAG_SOURCE} unavailable: {detail}")
        return None

    tag = described.stdout.strip()
    match = re.fullmatch(r"v([0-9]+\.[0-9]+\.[0-9]+)", tag)
    if match is None:
        raise ValueError(f"{TAG_SOURCE}: expected vX.Y.Z, found {tag!r}")

    exact = git_output("describe", "--tags", "--exact-match", "HEAD")
    return match.group(1), exact.returncode == 0 and exact.stdout.strip() == tag


def main() -> int:
    try:
        cargo_data = tomllib.loads(CARGO_TOML.read_text())
        versions = {
            relative(CARGO_TOML): cargo_data["package"]["version"],
            relative(PYTHON_INIT): python_package_version(),
            relative(FASTAPI_APP): fastapi_version(),
            relative(STATE): state_version(),
            relative(CHANGELOG): changelog_version(),
        }
        tag = nearest_tag()
    except (KeyError, OSError, SyntaxError, tomllib.TOMLDecodeError, ValueError) as error:
        print(f"version-check: ERROR: {error}", file=sys.stderr)
        return 1

    for path, version in versions.items():
        print(f"{path}: {version}")

    canonical_path = relative(CARGO_TOML)
    canonical_version = versions[canonical_path]
    mismatches = [
        (path, version)
        for path, version in versions.items()
        if version != canonical_version
    ]
    if mismatches:
        print(
            f"version-check: ERROR: expected {canonical_version} "
            f"from {canonical_path}; disagreeing file(s):",
            file=sys.stderr,
        )
        for path, version in mismatches:
            print(f"  {path}: {version}", file=sys.stderr)
        return 1

    if tag is not None:
        tag_version, exact = tag
        state = "exact HEAD tag" if exact else "nearest ancestor; HEAD is ahead"
        print(f"{TAG_SOURCE}: {tag_version} ({state})")
        if exact and tag_version != canonical_version:
            print(
                f"version-check: ERROR: exact HEAD tag is {tag_version}, "
                f"but {canonical_path} is {canonical_version}",
                file=sys.stderr,
            )
            return 1
        if not exact:
            if tag_version == canonical_version:
                detail = f"version remains {canonical_version}"
            else:
                detail = (
                    f"tag is {tag_version}; working tree version is "
                    f"{canonical_version}"
                )
            print(f"version-check: WARNING: HEAD is ahead of its tag; {detail}")

    print(f"version-check: PASS ({canonical_version})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
