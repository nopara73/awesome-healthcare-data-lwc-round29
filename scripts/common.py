from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATASET_DIR = ROOT / "datasets"

CATEGORY_TITLES = {
    "terminologies": "Terminologies & Vocabularies",
    "cms-medicare": "CMS / Medicare",
    "medicaid": "Medicaid",
    "cdc-surveillance": "CDC Surveillance & Public Health",
    "hcup": "HCUP",
    "claims-commercial": "Claims, Cost & Transparency",
    "provider": "Provider Data",
    "sdoh": "SDOH & Environment",
    "census": "Census & Demographic",
    "clinical-research": "Clinical / Research / ICU",
    "drug-pharma": "Drug & Pharmacology",
    "imaging": "Imaging",
    "genomics": "Genomics / Phenotype",
    "international": "International / Global Health",
}

CATEGORY_ICONS = {
    "terminologies": "&#x1F524;",
    "cms-medicare": "&#x1F3E5;",
    "medicaid": "&#x1F91D;",
    "cdc-surveillance": "&#x1F4CA;",
    "hcup": "&#x1F3E8;",
    "claims-commercial": "&#x1F4B3;",
    "provider": "&#x1F9D1;&#x200D;&#x2695;&#xFE0F;",
    "sdoh": "&#x1F3D8;&#xFE0F;",
    "census": "&#x1F5FA;&#xFE0F;",
    "clinical-research": "&#x1F52C;",
    "drug-pharma": "&#x1F48A;",
    "imaging": "&#x1F5BC;&#xFE0F;",
    "genomics": "&#x1F9EC;",
    "international": "&#x1F310;",
}

CATEGORY_DESCRIPTIONS = {
    "terminologies": "Code systems, vocabularies, and ontology sources for semantic normalization.",
    "cms-medicare": "Medicare, quality, payment, enrollment, and federal provider datasets.",
    "medicaid": "Medicaid and CHIP files for access, cost, eligibility, and utilization analysis.",
    "cdc-surveillance": "Public health surveillance, surveys, registries, and vital statistics.",
    "hcup": "Encounter-level inpatient, emergency, and ambulatory surgery research assets.",
    "claims-commercial": "Commercial claims, APCDs, price transparency, and state encounter files.",
    "provider": "Provider directories, taxonomy files, quality measures, and relationship data.",
    "sdoh": "Social, economic, environmental, housing, workforce, and place-based context.",
    "census": "Population, insurance, poverty, commuting, and denominator datasets.",
    "clinical-research": "Credentialed EHR, ICU, cohort, trial, and multimodal research datasets.",
    "drug-pharma": "Drug labels, approvals, adverse events, compounds, side effects, and safety data.",
    "imaging": "Radiology, dermatology, cancer imaging, and benchmark medical image collections.",
    "genomics": "Variant, phenotype, ontology, and association resources for genetics workflows.",
    "international": "Global and country-comparable health indicators, burden, and system measures.",
}

TIER_DETAILS = {
    "open": {
        "label": "Open",
        "color": "2f9e44",
        "description": "Public download, API, or aggregate portal.",
    },
    "registration": {
        "label": "Registration",
        "color": "1971c2",
        "description": "Free account, click-through terms, training, or attestation.",
    },
    "dua": {
        "label": "DUA",
        "color": "f08c00",
        "description": "Data use agreement or project approval.",
    },
    "irb": {
        "label": "IRB",
        "color": "c92a2a",
        "description": "IRB, DAC, or human-subjects governed access.",
    },
    "purchase": {
        "label": "Purchase",
        "color": "9c36b5",
        "description": "Paid license or proprietary component.",
    },
    "mixed": {
        "label": "Mixed",
        "color": "495057",
        "description": "Dataset family with multiple access paths.",
    },
}

def dataset_paths():
    return sorted(DATASET_DIR.glob("**/*.y*ml"))

def load_dataset(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_all_datasets():
    return [(p, load_dataset(p)) for p in dataset_paths()]

def category_title(slug: str) -> str:
    return CATEGORY_TITLES.get(slug, slug.replace("-", " ").title())


def category_icon(slug: str) -> str:
    return CATEGORY_ICONS.get(slug, "&#x1F4C1;")


def category_description(slug: str) -> str:
    return CATEGORY_DESCRIPTIONS.get(slug, "Healthcare data sources and related assets.")


def tier_label(slug: str) -> str:
    return TIER_DETAILS.get(slug, {"label": slug.title()})["label"]


def group_by_category(entries):
    by_cat = defaultdict(list)
    for entry in entries:
        by_cat[entry["category"]].append(entry)
    return {
        category: sorted(items, key=lambda item: item["name"].lower())
        for category, items in by_cat.items()
    }


def catalog_stats(entries):
    category_counts = Counter(entry["category"] for entry in entries)
    tier_counts = Counter(entry["access"]["tier"] for entry in entries)
    curation_counts = Counter(entry["curation"]["level"] for entry in entries)
    governed_count = sum(tier_counts.get(tier, 0) for tier in ("dua", "irb", "purchase"))
    return {
        "total": len(entries),
        "categories": len(category_counts),
        "open": tier_counts.get("open", 0),
        "governed": governed_count,
        "category_counts": category_counts,
        "tier_counts": tier_counts,
        "curation_counts": curation_counts,
    }
