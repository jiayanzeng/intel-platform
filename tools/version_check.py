#!/usr/bin/env python3
"""Fail when intel-platform's hand-maintained release versions diverge."""

from __future__ import annotations

import ast
import re
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CARGO_TOML = ROOT / "apps/cored/Cargo.toml"
PYTHON_INIT = ROOT / "shell/intel_shell/__init__.py"
FASTAPI_APP = ROOT / "shell/intel_shell/app.py"
STATE = ROOT / "STATE.md"


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


def main() -> int:
    try:
        cargo_data = tomllib.loads(CARGO_TOML.read_text())
        versions = {
            relative(CARGO_TOML): cargo_data["package"]["version"],
            relative(PYTHON_INIT): python_package_version(),
            relative(FASTAPI_APP): fastapi_version(),
            relative(STATE): state_version(),
        }
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

    print(f"version-check: PASS ({canonical_version})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
