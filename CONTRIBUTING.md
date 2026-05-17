# Contributing

Dataset entries live under `datasets/<category>/<id>.yaml` and must validate against `schemas/dataset.schema.json`.

## Add or update a dataset

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/build_readme.py
python scripts/build_csv.py
python scripts/build_search_index.py
```

## Quality bar

Every entry should document:

1. Access tier and licensing.
2. Grain, schema, and identifiers.
3. Coverage, size, and representativeness.
4. PHI/re-identification posture.
5. Known quality gotchas.
6. Canonical ETL / OMOP or PCORnet mapping status.

Use official source URLs whenever possible. Do not link to unofficial mirrors unless the official source points there.
