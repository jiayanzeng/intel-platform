#!/usr/bin/env python3
"""Derive and check the release-baselined public response-domain manifest."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SHELL = ROOT / "shell"
BASELINE = SHELL / "intel_shell" / "public_response_domains_v0.17.4.json"
EXPECTED_ROUTES = {
    "GET /v1/ask",
    "GET /v1/brief",
    "GET /v1/search",
    "GET /v1/signals",
    "POST /v1/billing/stripe",
    "POST /v1/billing/webhook",
}


class ManifestError(ValueError):
    """The derived or recorded manifest is incomplete or malformed."""


@dataclass(frozen=True)
class Difference:
    kind: str
    path: str
    before: object
    after: object


def _json_key(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _resolve_pointer(document: dict[str, Any], pointer: str) -> Any:
    if not pointer.startswith("#/"):
        raise ManifestError(f"unsupported non-local schema reference {pointer!r}")
    current: Any = document
    for raw in pointer[2:].split("/"):
        key = raw.replace("~1", "/").replace("~0", "~")
        if not isinstance(current, dict) or key not in current:
            raise ManifestError(f"unresolved schema reference {pointer!r}")
        current = current[key]
    return current


def _domain(
    schema: dict[str, Any],
    document: dict[str, Any],
    resolving: tuple[str, ...] = (),
) -> dict[str, Any]:
    if "$ref" in schema:
        reference = schema["$ref"]
        if not isinstance(reference, str):
            raise ManifestError("schema $ref must be a string")
        if reference in resolving:
            raise ManifestError(f"recursive response schema is unsupported: {reference}")
        target = _resolve_pointer(document, reference)
        if not isinstance(target, dict):
            raise ManifestError(f"schema reference {reference!r} is not an object")
        return _domain(target, document, (*resolving, reference))

    for keyword, label in (
        ("anyOf", "union"),
        ("oneOf", "union"),
        ("allOf", "intersection"),
    ):
        if keyword in schema:
            raw_options = schema[keyword]
            if not isinstance(raw_options, list) or not raw_options:
                raise ManifestError(f"schema {keyword} must be a non-empty list")
            options = []
            for option in raw_options:
                if not isinstance(option, dict):
                    raise ManifestError(f"schema {keyword} member must be an object")
                options.append(_domain(option, document, resolving))
            return {
                "kind": label,
                "options": sorted(options, key=_json_key),
            }

    raw_type = schema.get("type")
    if raw_type == "object" or "properties" in schema:
        properties = schema.get("properties", {})
        required = schema.get("required", [])
        if not isinstance(properties, dict) or not isinstance(required, list):
            raise ManifestError("object schema properties/required shape is invalid")
        if not all(isinstance(item, str) for item in required):
            raise ManifestError("object schema required entries must be strings")
        unknown_required = set(required) - set(properties)
        if unknown_required:
            raise ManifestError(
                f"object schema requires absent fields {sorted(unknown_required)}"
            )
        fields: dict[str, Any] = {}
        for name in sorted(properties):
            field_schema = properties[name]
            if not isinstance(field_schema, dict):
                raise ManifestError(f"field {name!r} schema must be an object")
            fields[name] = {
                "domain": _domain(field_schema, document, resolving),
                "required": name in required,
            }
        additional = schema.get("additionalProperties", True)
        if isinstance(additional, dict):
            additional_domain: bool | dict[str, Any] = _domain(
                additional, document, resolving
            )
        elif isinstance(additional, bool):
            additional_domain = additional
        else:
            raise ManifestError("additionalProperties must be boolean or schema")
        return {
            "additional_properties": additional_domain,
            "fields": fields,
            "kind": "object",
        }

    if raw_type == "array":
        items = schema.get("items")
        if not isinstance(items, dict):
            raise ManifestError("array response schema requires an items schema")
        return {"items": _domain(items, document, resolving), "kind": "array"}

    if raw_type is None and not (
        set(schema) - {"default", "description", "examples", "title"}
    ):
        return {"kind": "any"}
    if raw_type not in {"string", "integer", "number", "boolean", "null"}:
        raise ManifestError(f"unsupported response schema type {raw_type!r}")
    result: dict[str, Any] = {"kind": raw_type}
    if "const" in schema:
        result["values"] = [schema["const"]]
    elif "enum" in schema:
        values = schema["enum"]
        if not isinstance(values, list) or not values:
            raise ManifestError("schema enum must be a non-empty list")
        result["values"] = sorted(values, key=_json_key)
    for keyword in ("format", "maximum", "minimum", "maxLength", "minLength"):
        if keyword in schema:
            result[keyword] = schema[keyword]
    return result


def derive_manifest(release: str) -> dict[str, Any]:
    if not release.startswith("v"):
        raise ManifestError("release must use vX.Y.Z form")
    sys.path.insert(0, str(SHELL))
    try:
        from intel_shell.app import app
    finally:
        sys.path.pop(0)

    response_models = {
        f"{method.upper()} {route.path}": route.response_model
        for route in app.routes
        if route.path.startswith("/v1/")
        for method in route.methods
    }
    if set(response_models) != EXPECTED_ROUTES:
        raise ManifestError(
            "public route set differs: "
            f"expected={sorted(EXPECTED_ROUTES)} actual={sorted(response_models)}"
        )
    missing_models = sorted(
        route for route, model in response_models.items() if model is None
    )
    if missing_models:
        raise ManifestError(f"public routes lack response models: {missing_models}")

    openapi = app.openapi()
    routes: dict[str, Any] = {}
    for route_key in sorted(EXPECTED_ROUTES):
        method, path = route_key.split(" ", 1)
        operation = openapi["paths"][path][method.lower()]
        responses = operation.get("responses")
        if not isinstance(responses, dict) or not responses:
            raise ManifestError(f"{route_key} has no declared responses")
        variants: dict[str, Any] = {}
        for status in sorted(responses, key=str):
            response = responses[status]
            if not isinstance(response, dict):
                raise ManifestError(f"{route_key} response {status} is not an object")
            content = response.get("content")
            if not isinstance(content, dict) or not content:
                raise ManifestError(f"{route_key} response {status} has no content schema")
            for media_type in sorted(content):
                media = content[media_type]
                schema = media.get("schema") if isinstance(media, dict) else None
                if not isinstance(schema, dict):
                    raise ManifestError(
                        f"{route_key} response {status} {media_type} has no schema"
                    )
                variants[f"{status} {media_type}"] = _domain(schema, openapi)
        routes[route_key] = {"responses": variants}
    return {"release": release, "routes": routes, "schema_version": 1}


def _difference_kind(path: str, removed: bool = False) -> str:
    if ".fields" in path:
        return "field-removed" if removed else "field-added"
    return "surface-removed" if removed else "surface-added"


def compare(before: object, after: object, path: str = "manifest") -> list[Difference]:
    differences: list[Difference] = []
    if isinstance(before, dict) and isinstance(after, dict):
        for key in sorted(before.keys() - after.keys()):
            differences.append(
                Difference(
                    _difference_kind(path, removed=True),
                    f"{path}.{key}",
                    before[key],
                    None,
                )
            )
        for key in sorted(after.keys() - before.keys()):
            differences.append(
                Difference(_difference_kind(path), f"{path}.{key}", None, after[key])
            )
        for key in sorted(before.keys() & after.keys()):
            differences.extend(compare(before[key], after[key], f"{path}.{key}"))
        return differences
    if isinstance(before, list) and isinstance(after, list):
        before_keys = {_json_key(item): item for item in before}
        after_keys = {_json_key(item): item for item in after}
        kind_prefix = "value" if path.endswith(".values") else "member"
        for key in sorted(before_keys.keys() - after_keys.keys()):
            differences.append(
                Difference(f"{kind_prefix}-removed", path, before_keys[key], None)
            )
        for key in sorted(after_keys.keys() - before_keys.keys()):
            differences.append(
                Difference(f"{kind_prefix}-added", path, None, after_keys[key])
            )
        return differences
    if before != after:
        kind = "type-changed" if path.endswith(".kind") else "domain-redefined"
        differences.append(Difference(kind, path, before, after))
    return differences


def read_baseline(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise ManifestError(f"{path}: {error}") from error
    if not isinstance(value, dict) or set(value) != {
        "release",
        "routes",
        "schema_version",
    }:
        raise ManifestError(f"{path}: baseline root shape is invalid")
    if value["schema_version"] != 1 or not isinstance(value["release"], str):
        raise ManifestError(f"{path}: baseline version/release is invalid")
    if not isinstance(value["routes"], dict):
        raise ManifestError(f"{path}: baseline routes must be an object")
    return value


def _field_count(domain: object) -> int:
    if not isinstance(domain, dict):
        return 0
    fields = domain.get("fields", {})
    count = len(fields) if isinstance(fields, dict) else 0
    return count + sum(_field_count(value) for value in domain.values())


def check(path: Path) -> tuple[dict[str, Any], list[Difference]]:
    baseline = read_baseline(path)
    derived = derive_manifest(baseline["release"])
    return baseline, compare(baseline, derived)


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    write_parser = subparsers.add_parser("write")
    write_parser.add_argument("--release", required=True)
    write_parser.add_argument("--output", type=Path, default=BASELINE)
    check_parser = subparsers.add_parser("check")
    check_parser.add_argument("--baseline", type=Path, default=BASELINE)
    args = parser.parse_args(argv)

    try:
        if args.command == "write":
            manifest = derive_manifest(args.release)
            args.output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
            print(
                "domain-manifest: WROTE "
                f"{args.output} (release={args.release}, routes={len(manifest['routes'])}, "
                f"fields={_field_count(manifest)})"
            )
            return 0

        baseline, differences = check(args.baseline)
        if differences:
            for difference in differences:
                print(
                    "domain-manifest: ERROR: "
                    f"{difference.kind} at {difference.path}: "
                    f"before={_json_key(difference.before)} "
                    f"after={_json_key(difference.after)}"
                )
            print(f"domain-manifest: FAIL ({len(differences)} difference(s))")
            return 1
        print(
            "domain-manifest: PASS "
            f"(release={baseline['release']}, routes={len(baseline['routes'])}, "
            f"fields={_field_count(baseline)})"
        )
        return 0
    except ManifestError as error:
        print(f"domain-manifest: CONFIG FAIL: {error}")
        return 2


if __name__ == "__main__":
    raise SystemExit(run())
