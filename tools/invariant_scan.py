#!/usr/bin/env python3
"""Execute registered static repository invariants.

The scanner reads source, config, and Git worktree text only. It never loads a
built binary, opens an archive, or touches the network.

R1 deliberately scans production Rust outside ``crates/store/src/sqlite.rs``.
The store implementation and its ``#[cfg(test)]`` module are out of scope:
boundary/differential tests may name alternate numeric distances, while no
production caller outside the store may call ``assign_canonical_ids`` at all.
Rust files under a ``tests`` directory and text after the conventional
``#[cfg(test)] mod tests`` boundary are classified as test-only.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
RULES_FILE = Path("config/invariant-rules.json")
STORE = Path("crates/store/src/sqlite.rs")
CORE_MAIN = Path("apps/cored/src/main.rs")
AUTHORITY_FILES = (
    Path("AGENTS.md"),
    Path("intel-platform-OPERATIONS.md"),
)
AUTHORITY_START = "<!-- MODEL_PROFILE_AUTHORITY:START -->"
AUTHORITY_END = "<!-- MODEL_PROFILE_AUTHORITY:END -->"
ASSIGN_CALL = re.compile(r"\bassign_canonical_ids\s*\(")
TEST_MODULE = re.compile(r"(?m)^#\[cfg\(test\)\]\s*\nmod\s+tests\s*\{")
TCP_BIND = re.compile(r"\b(?:tokio::net::)?TcpListener::bind\s*\(")
LLM_MARKERS = (
    (
        "LLM client import",
        re.compile(
            r"(?mi)^\s*use\s+[^\n;]*(?:openai|anthropic|llm)[^\n;]*;"
        ),
    ),
    (
        "LLM/provider base-URL constant",
        re.compile(
            r"(?mi)^\s*(?:pub(?:\([^)]*\))?\s+)?(?:const|static)\s+"
            r"[A-Z0-9_]*(?:LLM|OPENAI|ANTHROPIC)[A-Z0-9_]*"
        ),
    ),
    (
        "LLM provider call",
        re.compile(
            r"(?i)api\.openai\.com|/v1/(?:chat/)?completions|"
            r"/v1/responses|\.chat_completions\s*\(|\.responses\s*\("
        ),
    ),
)
THRESHOLD_DECL = re.compile(
    r"(?m)^\s*(?:pub(?:\([^)]*\))?\s+)?const\s+"
    r"([A-Z0-9_]*(?:DEDUP|CANONICAL)[A-Z0-9_]*"
    r"(?:DISTANCE|THRESHOLD)[A-Z0-9_]*)\s*:\s*u32\s*=\s*(\d+)"
)
NUMERIC_THRESHOLD_CALL = re.compile(
    r"\b(?:assign_canonical_ids(?:_tx)?|"
    r"rematerialize_canonical_ids_with_distance)\s*"
    r"\([^;]{0,300}?\b\d+(?:u32)?\b",
    re.DOTALL,
)
PRIVATE_KEY_HEADER = re.compile(
    r"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----"
)
PROVIDER_KEY = re.compile(
    r"\b(?:"
    r"sk-(?:proj-|ant-)?[A-Za-z0-9_-]{20,}|"
    r"AKIA[0-9A-Z]{16}|"
    r"gh[opsu]_[A-Za-z0-9]{20,}|"
    r"xox[baprs]-[A-Za-z0-9-]{10,}|"
    r"AIza[0-9A-Za-z_-]{35}"
    r")\b"
)
AUTHORIZATION_VALUE = re.compile(
    r"(?i)\bAuthorization[\"']?\s*[:=]\s*[\"']?\s*"
    r"Bearer\s+([A-Za-z0-9._~+/\-=]{24,})"
)
SECRET_ASSIGNMENT = re.compile(
    r"(?m)^\s*(?:export\s+)?"
    r"[A-Z][A-Z0-9_]*(?:API_KEY|TOKEN|SECRET|PASSWORD)"
    r"[ \t]*=[ \t]*([^\s#]+)"
)
RAW_SECRET_FIELD = re.compile(
    r"(?i)[\"'](?:api_key|access_token|refresh_token|client_secret|password)"
    r"[\"']\s*:\s*[\"']([^\"']{20,})[\"']"
)
SECRET_PLACEHOLDERS = {
    "...",
    "…",
    "change-me",
    "replace-me",
    "replace-with-your-key",
}


class ConfigError(ValueError):
    """The rule registry cannot support the claim it declares."""


@dataclass(frozen=True)
class Rule:
    id: str
    claim: str
    source: str
    scope: str
    fail_before: str


def production_text(path: Path, text: str) -> str:
    """Return the production portion covered by the Rust rules."""
    if "tests" in path.parts:
        return ""
    boundary = TEST_MODULE.search(text)
    return text if boundary is None else text[: boundary.start()]


def rust_files(root: Path, base: Path | None = None) -> list[Path]:
    search_root = root if base is None else root / base
    if not search_root.is_dir():
        return []
    return sorted(
        path
        for path in search_root.rglob("*.rs")
        if ".git" not in path.parts and "target" not in path.parts
    )


def location(root: Path, path: Path, text: str, offset: int) -> str:
    line = text.count("\n", 0, offset) + 1
    return f"{path.relative_to(root)}:{line}"


def tracked_texts(root: Path) -> list[tuple[Path, str]]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z"],
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        message = result.stderr.decode(errors="replace").strip()
        raise ConfigError(f"git ls-files failed for {root}: {message}")

    tracked: list[tuple[Path, str]] = []
    for raw_path in result.stdout.split(b"\0"):
        if not raw_path:
            continue
        relative = Path(raw_path.decode())
        path = root / relative
        try:
            payload = path.read_bytes()
        except OSError as error:
            raise ConfigError(f"{relative}: {error}") from error
        if b"\0" in payload:
            continue
        try:
            text = payload.decode()
        except UnicodeDecodeError:
            continue
        tracked.append((path, text))
    return tracked


def r1_findings(root: Path) -> list[str]:
    findings: list[str] = []
    store = (root / STORE).resolve()
    for path in rust_files(root):
        if path.resolve() == store:
            continue
        text = production_text(path.relative_to(root), path.read_text())
        for match in ASSIGN_CALL.finditer(text):
            findings.append(
                f"{location(root, path, text, match.start())}: "
                "production assign_canonical_ids call outside the store"
            )
    return findings


def r2_findings(root: Path) -> list[str]:
    findings: list[str] = []
    matches: list[tuple[Path, str, re.Match[str]]] = []
    for path in rust_files(root):
        text = production_text(path.relative_to(root), path.read_text())
        matches.extend((path, text, match) for match in TCP_BIND.finditer(text))

    expected = (root / CORE_MAIN).resolve()
    for path, text, match in matches:
        allowed = (
            path.resolve() == expected
            and text.startswith(
                "tokio::net::TcpListener::bind(&bind_addresses[..])",
                match.start(),
            )
        )
        if not allowed:
            findings.append(
                f"{location(root, path, text, match.start())}: "
                "TcpListener bind outside the validated bind_addresses path"
            )

    main = (root / CORE_MAIN).read_text()
    production = production_text(CORE_MAIN, main)
    expected_call = "tokio::net::TcpListener::bind(&bind_addresses[..])"
    validation = "loopback_only(&bind)"
    if production.count(expected_call) != 1:
        findings.append(
            f"{CORE_MAIN}: expected exactly one validated TcpListener bind"
        )
    if production.count(validation) != 1:
        findings.append(
            f"{CORE_MAIN}: expected exactly one loopback_only validation"
        )
    if (
        expected_call in production
        and validation in production
        and production.index(validation) > production.index(expected_call)
    ):
        findings.append(f"{CORE_MAIN}: loopback validation occurs after bind")
    if len(matches) != 1:
        findings.append(
            f"production Rust contains {len(matches)} TcpListener binds; expected 1"
        )
    return findings


def r3_findings(root: Path) -> list[str]:
    findings: list[str] = []
    for path in rust_files(root, Path("crates")):
        text = production_text(path.relative_to(root), path.read_text())
        for label, pattern in LLM_MARKERS:
            for match in pattern.finditer(text):
                findings.append(
                    f"{location(root, path, text, match.start())}: {label}"
                )
    return findings


def r4_findings(root: Path) -> list[str]:
    findings: list[str] = []
    for path, text in tracked_texts(root):
        relative = path.relative_to(root)
        name = relative.name
        if name == ".env" or (
            name.startswith(".env.") and name != ".env.example"
        ):
            findings.append(f"{relative}: tracked secret-bearing environment file")

        patterns = (
            ("private-key header", PRIVATE_KEY_HEADER),
            ("provider-key-shaped value", PROVIDER_KEY),
            ("concrete Authorization bearer value", AUTHORIZATION_VALUE),
            ("raw secret-bearing response field", RAW_SECRET_FIELD),
        )
        for label, pattern in patterns:
            for match in pattern.finditer(text):
                findings.append(
                    f"{location(root, path, text, match.start())}: {label}"
                )

        for match in SECRET_ASSIGNMENT.finditer(text):
            value = match.group(1).strip("\"'")
            if (
                not value
                or value in SECRET_PLACEHOLDERS
                or "…" in value
                or "..." in value
                or value.startswith(("$", "<", "os.environ"))
            ):
                continue
            findings.append(
                f"{location(root, path, text, match.start())}: "
                "non-placeholder secret assignment"
            )
    return findings


def r5_findings(root: Path) -> list[str]:
    findings: list[str] = []
    declarations: list[tuple[Path, str, re.Match[str]]] = []
    for path in rust_files(root):
        text = production_text(path.relative_to(root), path.read_text())
        declarations.extend(
            (path, text, match) for match in THRESHOLD_DECL.finditer(text)
        )
        for match in NUMERIC_THRESHOLD_CALL.finditer(text):
            findings.append(
                f"{location(root, path, text, match.start())}: "
                "numeric canonical-distance argument in production"
            )

    expected = [
        item
        for item in declarations
        if item[0].resolve() == (root / STORE).resolve()
        and item[2].group(1) == "DEDUP_MAX_DISTANCE"
        and item[2].group(2) == "16"
    ]
    if len(expected) != 1:
        findings.append(
            f"{STORE}: expected one private DEDUP_MAX_DISTANCE: u32 = 16"
        )
    for path, text, match in declarations:
        if (
            path.resolve() != (root / STORE).resolve()
            or match.group(1) != "DEDUP_MAX_DISTANCE"
            or match.group(2) != "16"
        ):
            findings.append(
                f"{location(root, path, text, match.start())}: second "
                f"canonical-distance constant {match.group(1)}={match.group(2)}"
            )
    if len(declarations) != 1:
        findings.append(
            "production Rust contains "
            f"{len(declarations)} DEDUP/CANONICAL distance constants; expected 1"
        )
    return findings


def _authority_block(root: Path, relative: Path) -> tuple[str | None, list[str]]:
    path = root / relative
    try:
        text = path.read_text()
    except OSError as error:
        return None, [f"{relative}: cannot read authorization block: {error}"]
    if text.count(AUTHORITY_START) != 1 or text.count(AUTHORITY_END) != 1:
        return None, [
            f"{relative}: expected exactly one model-profile authorization block"
        ]
    start = text.index(AUTHORITY_START)
    end = text.index(AUTHORITY_END, start) + len(AUTHORITY_END)
    return text[start:end], []


def r6_findings(root: Path) -> list[str]:
    findings: list[str] = []
    blocks: dict[Path, str] = {}
    for relative in AUTHORITY_FILES:
        block, errors = _authority_block(root, relative)
        findings.extend(errors)
        if block is not None:
            blocks[relative] = block
    if len(blocks) == len(AUTHORITY_FILES):
        reference = blocks[AUTHORITY_FILES[0]]
        for relative in AUTHORITY_FILES[1:]:
            if blocks[relative] != reference:
                findings.append(
                    f"{relative}: model-profile authorization block differs "
                    f"from {AUTHORITY_FILES[0]}"
                )
    return findings


CHECKS: dict[str, Callable[[Path], list[str]]] = {
    "R1": r1_findings,
    "R2": r2_findings,
    "R3": r3_findings,
    "R4": r4_findings,
    "R5": r5_findings,
    "R6": r6_findings,
}


def load_rules(path: Path) -> list[Rule]:
    try:
        raw = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise ConfigError(f"{path}: {error}") from error
    if not isinstance(raw, dict) or set(raw) != {"schema_version", "rules"}:
        raise ConfigError(
            f"{path}: root keys must be exactly schema_version and rules"
        )
    if raw["schema_version"] != 1:
        raise ConfigError(f"{path}: schema_version must be 1")
    if not isinstance(raw["rules"], list) or not raw["rules"]:
        raise ConfigError(f"{path}: rules must be a non-empty array")

    rules: list[Rule] = []
    seen: set[str] = set()
    fields = {"id", "claim", "source", "scope", "fail_before"}
    for index, item in enumerate(raw["rules"]):
        where = f"{path}:rules[{index}]"
        if not isinstance(item, dict) or set(item) != fields:
            raise ConfigError(f"{where}: keys must be exactly {sorted(fields)}")
        for field in fields:
            if not isinstance(item[field], str) or not item[field].strip():
                raise ConfigError(f"{where}.{field}: must be a non-empty string")
        if item["id"] in seen:
            raise ConfigError(f"{where}.id: duplicate rule {item['id']}")
        if item["id"] not in CHECKS:
            raise ConfigError(f"{where}.id: no implemented check for {item['id']}")
        seen.add(item["id"])
        rules.append(Rule(**item))
    return rules


def run(root: Path, rules_path: Path) -> int:
    try:
        rules = load_rules(rules_path)
    except ConfigError as error:
        print(f"invariant-scan: CONFIG FAIL: {error}")
        return 2

    failed = False
    for rule in rules:
        findings = CHECKS[rule.id](root.resolve())
        if findings:
            failed = True
            for finding in findings:
                print(f"invariant-scan: {rule.id} FAIL: {finding}")
        else:
            print(f"invariant-scan: {rule.id} PASS: {rule.claim}")
    if failed:
        return 1
    print(f"invariant-scan: PASS ({len(rules)}/{len(rules)} registered rules)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--rules", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    rules = (
        args.rules.resolve()
        if args.rules is not None
        else root / RULES_FILE
    )
    return run(root, rules)


if __name__ == "__main__":
    raise SystemExit(main())
