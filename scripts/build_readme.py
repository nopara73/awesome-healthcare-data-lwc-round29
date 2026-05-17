from __future__ import annotations

from common import (
    CATEGORY_TITLES,
    ROOT,
    TIER_DETAILS,
    catalog_stats,
    category_description,
    category_icon,
    category_title,
    group_by_category,
    load_all_datasets,
    tier_label,
)


def esc(value):
    if value is None:
        return ""
    return str(value).replace("|", "\\|").replace("\n", " ")


def shields_value(value):
    return str(value).replace("-", "--").replace("_", "__").replace(" ", "%20")


def badge(label, message, color="0b7285"):
    label = shields_value(label)
    message = shields_value(message)
    return f"https://img.shields.io/badge/{label}-{message}-{color}.svg?style=for-the-badge"


def dataset_table(cat_entries, yaml_prefix=""):
    lines = [
        "| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |\n",
        "|---|---:|---|---|---|---|---|\n",
    ]
    for entry in cat_entries:
        official = entry["resources"]["official_page"]
        dataset_link = f"[{esc(entry['short_name'])}]({official})"
        yaml_link = f"{yaml_prefix}datasets/{entry['category']}/{entry['id']}.yaml"
        lines.append(
            f"| {dataset_link}<br><sub>[yaml]({yaml_link})</sub> | "
            f"`{esc(entry['access']['tier'])}` | {esc(entry['phi']['classification'])} | "
            f"{esc(entry['grain'])} | {esc(entry['omop_mapping']['status'])} | "
            f"{esc(entry['curation']['level'])} | {esc(entry['freshness']['last_validated'])} |\n"
        )
    return lines


entries = [data for _, data in load_all_datasets()]
by_cat = group_by_category(entries)
stats = catalog_stats(entries)

lines = []
lines.append(
    '<p align="center"><img src="docs/assets/awesome-health-data-banner.png" '
    'alt="Abstract healthcare data network banner" width="100%"></p>\n\n'
)
lines.append('<h1 align="center">Awesome Health Data</h1>\n\n')
lines.append(
    '<p align="center"><strong>A machine-readable healthcare dataset catalog '
    "for ML, analytics, public health, policy, and life sciences teams.</strong></p>\n\n"
)
lines.append('<p align="center">\n')
lines.append(
    f'  <img alt="Datasets" src="{badge("datasets", stats["total"])}">\n'
    f'  <img alt="Categories" src="{badge("categories", stats["categories"], "1864ab")}">\n'
    f'  <img alt="Open sources" src="{badge("open", stats["open"], "2f9e44")}">\n'
    f'  <img alt="Generated from YAML" src="{badge("source", "YAML", "495057")}">\n'
    f'  <img alt="Awesome" src="{badge("awesome", "health data", "6741d9")}">\n'
)
lines.append("</p>\n\n")
lines.append(
    "> This README is generated from `datasets/**/*.yaml`. Do not hand-edit "
    "dataset tables; update YAML and rerun `make build`.\n\n"
)

lines.append("## At a Glance\n\n")
lines.append("<table>\n<tr>\n")
lines.append(f'<td align="center"><strong>{stats["total"]}</strong><br><sub>datasets</sub></td>\n')
lines.append(
    f'<td align="center"><strong>{stats["categories"]}</strong><br><sub>categories</sub></td>\n'
)
lines.append(f'<td align="center"><strong>{stats["open"]}</strong><br><sub>open sources</sub></td>\n')
lines.append(
    f'<td align="center"><strong>{stats["governed"]}</strong><br><sub>DUA, IRB, or purchase</sub></td>\n'
)
lines.append(
    f'<td align="center"><strong>{stats["curation_counts"].get("reference", 0)}</strong>'
    "<br><sub>reference entries</sub></td>\n"
)
lines.append("</tr>\n</table>\n\n")

lines.append("## Start Here\n\n")
lines.append("| Need | Go to |\n")
lines.append("|---|---|\n")
lines.append("| Find a source by domain | [Category map](#category-map) |\n")
lines.append("| Compare access restrictions | [Access tiers](#access-tiers) |\n")
lines.append("| Browse every dataset | [Dataset index](#dataset-index) |\n")
lines.append("| Build a governed-data workflow | [PHI guide](docs/phi-guide.md) and [playbooks](playbooks/) |\n")
lines.append("| Prototype ML examples | [notebooks](notebooks/) and [sample data](examples/sample_data/) |\n")
lines.append("| Consume machine-readable exports | [CSV/JSON exports](exports/) |\n\n")

lines.append("## Category Map\n\n")
lines.append("| Category | Count | What it covers |\n")
lines.append("|---|---:|---|\n")
for category in CATEGORY_TITLES:
    count = stats["category_counts"].get(category, 0)
    if not count:
        continue
    lines.append(
        f"| {category_icon(category)} [{category_title(category)}](#{category}) | "
        f"{count} | {category_description(category)} |\n"
    )
lines.append("\n")

lines.append("## Access Tiers\n\n")
lines.append("| Tier | Count | Meaning |\n")
lines.append("|---|---:|---|\n")
for tier, details in TIER_DETAILS.items():
    count = stats["tier_counts"].get(tier, 0)
    lines.append(
        f"| `{tier}` {tier_label(tier)} | {count} | {details['description']} |\n"
    )
lines.append("\n")

lines.append("## What These Data Sources Can Help With\n\n")
lines.append(
    "This catalog brings together data sources that help healthcare, life sciences, "
    "public health, policy, and analytics teams answer practical business questions: "
    "where care is delivered, what it costs, which populations are at risk, how "
    "communities differ, how drugs and devices perform, and how clinical evidence "
    "can be reused responsibly.\n\n"
)
for category in CATEGORY_TITLES:
    cat_entries = by_cat.get(category, [])
    if not cat_entries:
        continue
    lines.append(
        f'<details>\n<summary><strong>{category_icon(category)} '
        f'{category_title(category)}</strong> '
        f'<sub>{len(cat_entries)} datasets</sub></summary>\n\n'
    )
    lines.append(f"{category_description(category)}\n\n")
    for entry in cat_entries:
        official = entry["resources"]["official_page"]
        lines.append(
            f"- **[{esc(entry['short_name'])}]({official})**: "
            f"{esc(entry['business_summary'])}\n"
        )
    lines.append("\n</details>\n\n")

lines.append("## What Makes This Maintainable\n\n")
lines.append("- **Machine-readable entries**: every dataset is YAML validated against `schemas/dataset.schema.json`.\n")
lines.append("- **Use-case-first navigation**: `use-cases/` pages shortlist datasets for real ML workflows.\n")
lines.append("- **Access-tier + PHI filters**: prototype-now sources are separated from DUA/IRB assets.\n")
lines.append("- **OMOP/PCORnet mapping status**: each entry records CDM fit and ETL notes.\n")
lines.append("- **Crosswalks and notebooks**: vocabulary/geography joins and starter analyses are first-class content.\n")
lines.append("- **Freshness signals**: scripts can flag stale `last_validated` dates and broken links.\n\n")

lines.append("## Dataset Index\n\n")
lines.append(f"Total entries: **{stats['total']}**.\n\n")
for category in CATEGORY_TITLES:
    cat_entries = by_cat.get(category, [])
    if not cat_entries:
        continue
    lines.append(f'<a id="{category}"></a>\n\n')
    lines.append(
        f'<details>\n<summary><strong>{category_icon(category)} '
        f'{category_title(category)}</strong> '
        f'<sub>{len(cat_entries)} datasets</sub></summary>\n\n'
    )
    lines.extend(dataset_table(cat_entries))
    lines.append("\n</details>\n\n")

lines.append("## Contributing\n\n")
lines.append(
    "Open a PR with a schema-valid YAML file under the right "
    "`datasets/<category>/` directory. See [CONTRIBUTING.md](CONTRIBUTING.md).\n\n"
)
lines.append("## License\n\n")
lines.append(
    "Repository metadata/docs are intended to be CC-BY-4.0; code is intended to be MIT. "
    "This repository does **not** grant rights to redistribute third-party data files.\n"
)

(ROOT / "README.md").write_text("".join(lines), encoding="utf-8")
print(f"Wrote README.md with {len(entries)} entries")
