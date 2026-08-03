#!/usr/bin/env python3
"""Derive and check the release-baselined public response-domain manifest."""

from __future__ import annotations

import argparse
import ast
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SHELL = ROOT / "shell"
BASELINE = SHELL / "intel_shell" / "public_response_domains_v0.17.4.json"
MODEL_SOURCE = SHELL / "intel_shell" / "api_models.py"
APP_SOURCE = SHELL / "intel_shell" / "app.py"
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


def derive_openapi_manifest(release: str) -> dict[str, Any]:
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


def _validation_error_domain() -> dict[str, Any]:
    """Pinned FastAPI/Pydantic 422 domain, cross-checked after install."""
    location = {
        "kind": "array",
        "items": {
            "kind": "union",
            "options": [{"kind": "integer"}, {"kind": "string"}],
        },
    }
    error = {
        "additional_properties": True,
        "fields": {
            "ctx": {
                "domain": {
                    "additional_properties": True,
                    "fields": {},
                    "kind": "object",
                },
                "required": False,
            },
            "input": {"domain": {"kind": "any"}, "required": False},
            "loc": {"domain": location, "required": True},
            "msg": {"domain": {"kind": "string"}, "required": True},
            "type": {"domain": {"kind": "string"}, "required": True},
        },
        "kind": "object",
    }
    return {
        "additional_properties": True,
        "fields": {
            "detail": {
                "domain": {"items": error, "kind": "array"},
                "required": False,
            }
        },
        "kind": "object",
    }


def _source_type_tables() -> tuple[
    dict[str, ast.expr], dict[str, list[ast.AnnAssign]]
]:
    tree = ast.parse(MODEL_SOURCE.read_text(), filename=str(MODEL_SOURCE))
    aliases: dict[str, ast.expr] = {}
    classes: dict[str, list[ast.AnnAssign]] = {}
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
        ):
            aliases[node.targets[0].id] = node.value
        elif isinstance(node, ast.ClassDef) and node.name != "PublicResponseModel":
            fields = [item for item in node.body if isinstance(item, ast.AnnAssign)]
            if fields:
                classes[node.name] = fields
    return aliases, classes


def _source_domain(
    annotation: ast.expr,
    aliases: dict[str, ast.expr],
    classes: dict[str, list[ast.AnnAssign]],
    resolving: tuple[str, ...] = (),
) -> dict[str, Any]:
    primitive_names = {
        "str": "string",
        "int": "integer",
        "float": "number",
        "bool": "boolean",
    }
    if isinstance(annotation, ast.Constant) and annotation.value is None:
        return {"kind": "null"}
    if isinstance(annotation, ast.Name):
        if annotation.id in primitive_names:
            return {"kind": primitive_names[annotation.id]}
        if annotation.id in resolving:
            raise ManifestError(f"recursive source response type {annotation.id!r}")
        if annotation.id in aliases:
            return _source_domain(
                aliases[annotation.id],
                aliases,
                classes,
                (*resolving, annotation.id),
            )
        if annotation.id in classes:
            fields: dict[str, Any] = {}
            for field in classes[annotation.id]:
                if not isinstance(field.target, ast.Name):
                    raise ManifestError(
                        f"{annotation.id}: response field target must be a name"
                    )
                fields[field.target.id] = {
                    "domain": _source_domain(
                        field.annotation,
                        aliases,
                        classes,
                        (*resolving, annotation.id),
                    ),
                    "required": field.value is None,
                }
            return {
                "additional_properties": False,
                "fields": {name: fields[name] for name in sorted(fields)},
                "kind": "object",
            }
        raise ManifestError(f"unsupported source response name {annotation.id!r}")
    if isinstance(annotation, ast.Subscript) and isinstance(
        annotation.value, ast.Name
    ):
        if annotation.value.id == "list":
            return {
                "items": _source_domain(
                    annotation.slice, aliases, classes, resolving
                ),
                "kind": "array",
            }
        if annotation.value.id == "Literal":
            members = (
                annotation.slice.elts
                if isinstance(annotation.slice, ast.Tuple)
                else [annotation.slice]
            )
            values = [ast.literal_eval(member) for member in members]
            kinds = {
                "boolean"
                if isinstance(value, bool)
                else "integer"
                if isinstance(value, int)
                else "number"
                if isinstance(value, float)
                else "string"
                if isinstance(value, str)
                else "null"
                if value is None
                else "unsupported"
                for value in values
            }
            if len(kinds) != 1 or "unsupported" in kinds:
                raise ManifestError("Literal response domain must have one value type")
            return {"kind": kinds.pop(), "values": sorted(values, key=_json_key)}
    if isinstance(annotation, ast.BinOp) and isinstance(annotation.op, ast.BitOr):
        options: list[dict[str, Any]] = []

        def collect(member: ast.expr) -> None:
            if isinstance(member, ast.BinOp) and isinstance(member.op, ast.BitOr):
                collect(member.left)
                collect(member.right)
            else:
                options.append(_source_domain(member, aliases, classes, resolving))

        collect(annotation)
        return {"kind": "union", "options": sorted(options, key=_json_key)}
    raise ManifestError(
        "unsupported source response annotation " + ast.dump(annotation)
    )


def derive_manifest(release: str) -> dict[str, Any]:
    """Derive the public contract without requiring third-party imports."""
    if not release.startswith("v"):
        raise ManifestError("release must use vX.Y.Z form")
    aliases, classes = _source_type_tables()
    error_domain = _source_domain(ast.Name(id="ErrorResponse"), aliases, classes)
    tree = ast.parse(APP_SOURCE.read_text(), filename=str(APP_SOURCE))
    routes: dict[str, Any] = {}
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for decorator in node.decorator_list:
            if not (
                isinstance(decorator, ast.Call)
                and isinstance(decorator.func, ast.Attribute)
                and isinstance(decorator.func.value, ast.Name)
                and decorator.func.value.id == "app"
                and decorator.func.attr in {"get", "post"}
                and decorator.args
                and isinstance(decorator.args[0], ast.Constant)
                and isinstance(decorator.args[0].value, str)
                and decorator.args[0].value.startswith("/v1/")
            ):
                continue
            route_key = (
                f"{decorator.func.attr.upper()} {decorator.args[0].value}"
            )
            keywords = {item.arg: item.value for item in decorator.keywords}
            response_model = keywords.get("response_model")
            if response_model is None:
                raise ManifestError(f"{route_key} lacks a response_model")
            media_type = (
                "text/plain"
                if isinstance(keywords.get("response_class"), ast.Name)
                and keywords["response_class"].id == "PlainTextResponse"
                else "application/json"
            )
            variants = {
                f"200 {media_type}": _source_domain(
                    response_model, aliases, classes
                ),
                "422 application/json": _validation_error_domain(),
            }
            response_call = keywords.get("responses")
            if not (
                isinstance(response_call, ast.Call)
                and isinstance(response_call.func, ast.Name)
                and response_call.func.id
                in {"_error_responses", "_json_error_responses"}
            ):
                raise ManifestError(f"{route_key} lacks declared error responses")
            for argument in response_call.args:
                status = ast.literal_eval(argument)
                if not isinstance(status, int):
                    raise ManifestError(f"{route_key} error status is not an integer")
                variants[f"{status} application/json"] = error_domain
            routes[route_key] = {
                "responses": {name: variants[name] for name in sorted(variants)}
            }
    if set(routes) != EXPECTED_ROUTES:
        raise ManifestError(
            "public route set differs: "
            f"expected={sorted(EXPECTED_ROUTES)} actual={sorted(routes)}"
        )
    return {
        "release": release,
        "routes": {name: routes[name] for name in sorted(routes)},
        "schema_version": 1,
    }


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
    runtime_parser = subparsers.add_parser("verify-runtime")
    runtime_parser.add_argument("--release", required=True)
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

        if args.command == "verify-runtime":
            source = derive_manifest(args.release)
            runtime = derive_openapi_manifest(args.release)
            differences = compare(source, runtime)
            if differences:
                for difference in differences:
                    print(
                        "domain-manifest: RUNTIME ERROR: "
                        f"{difference.kind} at {difference.path}: "
                        f"source={_json_key(difference.before)} "
                        f"runtime={_json_key(difference.after)}"
                    )
                print(
                    "domain-manifest: RUNTIME FAIL "
                    f"({len(differences)} difference(s))"
                )
                return 1
            print(
                "domain-manifest: RUNTIME PASS "
                f"(release={args.release}, routes={len(source['routes'])}, "
                f"fields={_field_count(source)})"
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
