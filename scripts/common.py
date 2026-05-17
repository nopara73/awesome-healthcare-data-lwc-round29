from __future__ import annotations

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

def dataset_paths():
    return sorted(DATASET_DIR.glob("**/*.y*ml"))

def load_dataset(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_all_datasets():
    return [(p, load_dataset(p)) for p in dataset_paths()]

def category_title(slug: str) -> str:
    return CATEGORY_TITLES.get(slug, slug.replace("-", " ").title())
