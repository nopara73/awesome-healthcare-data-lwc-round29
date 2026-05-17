from __future__ import annotations

from collections import defaultdict
from common import ROOT, CATEGORY_TITLES, category_title, load_all_datasets

def esc(value):
    if value is None:
        return ""
    return str(value).replace("|", "\\|").replace("\n", " ")

entries = [data for _, data in load_all_datasets()]
by_cat = defaultdict(list)
for e in entries:
    by_cat[e["category"]].append(e)

lines = []
lines.append("# Awesome Health Data\n\n")
lines.append("A machine-readable catalog of healthcare, public health, SDOH, claims, research, imaging, genomics, drug, and global-health datasets for ML and analytics.\n\n")
lines.append("> This README is generated from `datasets/**/*.yaml`. Do not hand-edit dataset tables; update YAML and rerun `make build`.\n\n")

lines.append("## What makes this maintainable\n\n")
lines.append("- **Machine-readable entries**: every dataset is YAML validated against `schemas/dataset.schema.json`.\n")
lines.append("- **Use-case-first navigation**: `use-cases/` pages shortlist datasets for real ML workflows.\n")
lines.append("- **Access-tier + PHI filters**: prototype-now sources are separated from DUA/IRB assets.\n")
lines.append("- **OMOP/PCORnet mapping status**: each entry records CDM fit and ETL notes.\n")
lines.append("- **Crosswalks and notebooks**: vocabulary/geography joins and starter analyses are first-class content.\n")
lines.append("- **Freshness signals**: CI can flag stale `last_validated` dates and broken links.\n\n")

lines.append("## Start here\n\n")
lines.append("- [Getting started](docs/getting-started.md)\n")
lines.append("- [Access tiers](docs/access-tiers.md)\n")
lines.append("- [PHI guide](docs/phi-guide.md)\n")
lines.append("- [Use cases](use-cases/)\n")
lines.append("- [Crosswalks](crosswalks/)\n")
lines.append("- [Playbooks](playbooks/)\n")
lines.append("- [Generated exports](exports/)\n\n")

lines.append("## Dataset index\n\n")
lines.append(f"Total entries: **{len(entries)}**.\n\n")

for cat in CATEGORY_TITLES:
    cat_entries = sorted(by_cat.get(cat, []), key=lambda x: x["name"].lower())
    if not cat_entries:
        continue
    lines.append(f"### {category_title(cat)}\n\n")
    lines.append("| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |\n")
    lines.append("|---|---:|---|---|---|---|---|\n")
    for e in cat_entries:
        official = e["resources"]["official_page"]
        dataset_link = f"[{esc(e['short_name'])}]({official})"
        yaml_link = f"datasets/{e['category']}/{e['id']}.yaml"
        lines.append(
            f"| {dataset_link}<br><sub>[yaml]({yaml_link})</sub> | "
            f"`{esc(e['access']['tier'])}` | {esc(e['phi']['classification'])} | "
            f"{esc(e['grain'])} | {esc(e['omop_mapping']['status'])} | "
            f"{esc(e['curation']['level'])} | {esc(e['freshness']['last_validated'])} |\n"
        )
    lines.append("\n")

lines.append("## Contributing\n\n")
lines.append("Open a PR with a schema-valid YAML file under the right `datasets/<category>/` directory. See [CONTRIBUTING.md](CONTRIBUTING.md).\n\n")
lines.append("## License\n\n")
lines.append("Repository metadata/docs are intended to be CC-BY-4.0; code is intended to be MIT. This repository does **not** grant rights to redistribute third-party data files.\n")

(ROOT / "README.md").write_text("".join(lines), encoding="utf-8")
print(f"Wrote README.md with {len(entries)} entries")
