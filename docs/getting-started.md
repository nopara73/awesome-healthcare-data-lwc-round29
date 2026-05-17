# Getting started

1. Pick a use case under `use-cases/`.
2. Filter datasets by access tier and PHI posture.
3. Prototype ETL on open/synthetic data.
4. Apply for governed data only after the cohort, target, validation plan, and security posture are clear.
5. Map vocabularies and fact tables into OMOP/PCORnet when reuse or multi-source validation matters.

Useful commands:

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/build_readme.py
python scripts/build_csv.py
python scripts/build_search_index.py
```
