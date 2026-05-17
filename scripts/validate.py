from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "dataset.schema.json"
DATASET_DIR = ROOT / "datasets"

schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
validator = Draft202012Validator(schema, format_checker=FormatChecker())
errors = []
seen_ids: dict[str, Path] = {}

for path in sorted(DATASET_DIR.glob("**/*.y*ml")):
    rel = path.relative_to(ROOT)
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{rel}: YAML parse error: {exc}")
        continue

    for err in sorted(validator.iter_errors(data), key=lambda e: e.path):
        loc = ".".join(str(p) for p in err.path) or "<root>"
        errors.append(f"{rel}: schema error at {loc}: {err.message}")

    dataset_id = data.get("id")
    if dataset_id in seen_ids:
        errors.append(f"{rel}: duplicate id {dataset_id!r}; already in {seen_ids[dataset_id].relative_to(ROOT)}")
    else:
        seen_ids[dataset_id] = path

    expected_category = path.parent.name
    if data.get("category") != expected_category:
        errors.append(f"{rel}: category {data.get('category')!r} does not match directory {expected_category!r}")

    if path.stem != dataset_id:
        errors.append(f"{rel}: filename should be {dataset_id}.yaml")

    try:
        date.fromisoformat(data["freshness"]["last_validated"])
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{rel}: invalid freshness.last_validated: {exc}")

if errors:
    print("Validation failed:\n" + "\n".join(f"- {e}" for e in errors), file=sys.stderr)
    sys.exit(1)

print(f"Validated {len(seen_ids)} dataset entries.")
