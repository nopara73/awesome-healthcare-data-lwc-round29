from __future__ import annotations

import csv
import json
from common import ROOT, load_all_datasets

EXPORTS = ROOT / "exports"
EXPORTS.mkdir(exist_ok=True)

rows = []
for _, e in load_all_datasets():
    rows.append({
        "id": e["id"],
        "name": e["name"],
        "short_name": e["short_name"],
        "category": e["category"],
        "business_summary": e["business_summary"],
        "tier": e["access"]["tier"],
        "official_page": e["resources"]["official_page"],
        "download_url": e["resources"]["download_url"],
        "grain": e["grain"],
        "unit_of_observation": e["unit_of_observation"],
        "phi_classification": e["phi"]["classification"],
        "reid_risk": e["phi"]["reid_risk"],
        "omop_status": e["omop_mapping"]["status"],
        "curation_level": e["curation"]["level"],
        "use_cases": ";".join(e["common_use_cases"]),
        "vocabularies": ";".join(e.get("vocabularies", [])),
        "last_validated": e["freshness"]["last_validated"],
    })

fieldnames = list(rows[0].keys())
with (EXPORTS / "all-datasets.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

(EXPORTS / "all-datasets.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")

try:
    import pandas as pd
    pd.DataFrame(rows).to_parquet(EXPORTS / "all-datasets.parquet", index=False)
except Exception as exc:  # noqa: BLE001
    print(f"Parquet export skipped: {exc}")

print(f"Wrote {len(rows)} rows to exports/")
