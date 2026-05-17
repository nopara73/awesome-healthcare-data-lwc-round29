from __future__ import annotations

import json
from common import ROOT, load_all_datasets

index = []
for _, e in load_all_datasets():
    index.append({
        "id": e["id"],
        "title": e["name"],
        "category": e["category"],
        "tier": e["access"]["tier"],
        "phi": e["phi"]["classification"],
        "reid_risk": e["phi"]["reid_risk"],
        "omop": e["omop_mapping"]["status"],
        "curation": e["curation"]["level"],
        "use_cases": e["common_use_cases"],
        "vocabularies": e.get("vocabularies", []),
        "url": e["resources"]["official_page"],
        "text": " ".join([e["name"], e["description"], e["grain"], e["etl"]["canonical_path"], " ".join(e["quality_gotchas"])]),
    })

out = ROOT / "docs" / "assets" / "search-index.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(index, indent=2), encoding="utf-8")
print(f"Wrote {out.relative_to(ROOT)}")
