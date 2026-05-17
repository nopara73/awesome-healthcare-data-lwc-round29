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

REPO_BLOB_BASE = "https://github.com/adnanmasood/awesome-health-data/blob/main"


def esc(value):
    if value is None:
        return ""
    return str(value).replace("|", "\\|").replace("\n", " ")


def stat_card(value, label):
    return (
        '<div class="stat-card">'
        f'<span class="stat-card__value">{value}</span>'
        f'<span class="stat-card__label">{label}</span>'
        "</div>\n"
    )


def dataset_table(cat_entries):
    lines = [
        "| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |\n",
        "|---|---:|---|---|---|---|---|\n",
    ]
    for entry in cat_entries:
        official = entry["resources"]["official_page"]
        dataset_link = f"[{esc(entry['short_name'])}]({official})"
        yaml_link = f"{REPO_BLOB_BASE}/datasets/{entry['category']}/{entry['id']}.yaml"
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
docs_dir = ROOT / "docs"

index_lines = []
index_lines.append("# Awesome Healthcare Data\n\n")
index_lines.append('<section class="catalog-hero" aria-label="Abstract healthcare data network banner">\n')
index_lines.append('  <div class="catalog-hero__content">\n')
index_lines.append('    <p class="catalog-hero__kicker">Healthcare data catalog</p>\n')
index_lines.append("    <h1>Find the right healthcare dataset faster.</h1>\n")
index_lines.append(
    "    <p>Curated healthcare data sources<br>"
    "for governed access, research,<br>"
    "imaging, genomics, drug safety,<br>"
    "global health, ML, and analytics.</p>\n"
)
index_lines.append('    <div class="catalog-hero__actions">\n')
index_lines.append('      <a class="catalog-button catalog-button--primary" href="datasets.md">Browse datasets</a>\n')
index_lines.append('      <a class="catalog-button" href="getting-started.md">Get started</a>\n')
index_lines.append("    </div>\n")
index_lines.append("  </div>\n")
index_lines.append("</section>\n\n")

index_lines.append('<section class="stat-grid" aria-label="Catalog statistics">\n')
index_lines.append(stat_card(stats["total"], "datasets"))
index_lines.append(stat_card(stats["categories"], "categories"))
index_lines.append(stat_card(stats["open"], "open sources"))
index_lines.append(stat_card(stats["governed"], "DUA, IRB, or purchase"))
index_lines.append(stat_card(stats["curation_counts"].get("reference", 0), "reference entries"))
index_lines.append("</section>\n\n")

index_lines.append("## Explore by Domain\n\n")
index_lines.append('<section class="category-grid">\n')
for category in CATEGORY_TITLES:
    count = stats["category_counts"].get(category, 0)
    if not count:
        continue
    index_lines.append(f'  <a class="category-card" href="datasets.md#{category}">\n')
    index_lines.append(f'    <span class="category-card__icon">{category_icon(category)}</span>\n')
    index_lines.append("    <span>\n")
    index_lines.append(f'      <strong>{category_title(category)}</strong>\n')
    index_lines.append(f'      <small>{count} datasets - {category_description(category)}</small>\n')
    index_lines.append("    </span>\n")
    index_lines.append("  </a>\n")
index_lines.append("</section>\n\n")

index_lines.append("## Start With the Workflow\n\n")
index_lines.append("| Need | Open |\n")
index_lines.append("|---|---|\n")
index_lines.append("| Pick a source by domain and access tier | [Dataset index](datasets.md) |\n")
index_lines.append("| Understand governed access | [Access tiers](access-tiers.md) and [PHI guide](phi-guide.md) |\n")
index_lines.append("| Plan a research-grade workflow | [Research method](research-method.md) |\n")
index_lines.append("| Run the project locally | [Getting started](getting-started.md) |\n\n")

index_lines.append("## Access Mix\n\n")
index_lines.append('<section class="tier-grid">\n')
for tier, details in TIER_DETAILS.items():
    count = stats["tier_counts"].get(tier, 0)
    index_lines.append(f'  <div class="tier-card tier-card--{tier}">\n')
    index_lines.append(f"    <strong>{tier_label(tier)}</strong>\n")
    index_lines.append(f"    <span>{count} datasets</span>\n")
    index_lines.append(f"    <small>{details['description']}</small>\n")
    index_lines.append("  </div>\n")
index_lines.append("</section>\n")

datasets_lines = []
datasets_lines.append("# Dataset Index\n\n")
datasets_lines.append(
    "Generated from schema-valid YAML entries. Use this page for browsing; use the "
    "[CSV and JSON exports](https://github.com/adnanmasood/awesome-health-data/tree/main/exports) "
    "for machine-readable ingestion.\n\n"
)
datasets_lines.append('<section class="stat-grid stat-grid--compact" aria-label="Catalog statistics">\n')
datasets_lines.append(stat_card(stats["total"], "datasets"))
datasets_lines.append(stat_card(stats["categories"], "categories"))
datasets_lines.append(stat_card(stats["open"], "open sources"))
datasets_lines.append(stat_card(stats["governed"], "DUA, IRB, or purchase"))
datasets_lines.append("</section>\n\n")

datasets_lines.append("## Category Map\n\n")
datasets_lines.append("| Category | Count | What it covers |\n")
datasets_lines.append("|---|---:|---|\n")
for category in CATEGORY_TITLES:
    count = stats["category_counts"].get(category, 0)
    if not count:
        continue
    datasets_lines.append(
        f"| {category_icon(category)} [{category_title(category)}](#{category}) | "
        f"{count} | {category_description(category)} |\n"
    )
datasets_lines.append("\n")

datasets_lines.append("## Access Tiers\n\n")
datasets_lines.append("| Tier | Count | Meaning |\n")
datasets_lines.append("|---|---:|---|\n")
for tier, details in TIER_DETAILS.items():
    count = stats["tier_counts"].get(tier, 0)
    datasets_lines.append(
        f"| `{tier}` {tier_label(tier)} | {count} | {details['description']} |\n"
    )
datasets_lines.append("\n")

datasets_lines.append("## Sources by Category\n\n")
for category in CATEGORY_TITLES:
    cat_entries = by_cat.get(category, [])
    if not cat_entries:
        continue
    datasets_lines.append(f'<a id="{category}"></a>\n\n')
    datasets_lines.append(
        f"### {category_icon(category)} {category_title(category)} "
        f"<small>{len(cat_entries)} datasets</small>\n\n"
    )
    datasets_lines.append(f"{category_description(category)}\n\n")
    datasets_lines.extend(dataset_table(cat_entries))
    datasets_lines.append("\n")

(docs_dir / "index.md").write_text("".join(index_lines), encoding="utf-8")
(docs_dir / "datasets.md").write_text("".join(datasets_lines), encoding="utf-8")
print("Wrote docs/index.md and docs/datasets.md")
