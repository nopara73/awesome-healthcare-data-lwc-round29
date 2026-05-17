#!/usr/bin/env bash
set -euo pipefail
python -m pip install -r requirements.txt
python scripts/validate.py
python scripts/build_readme.py
python scripts/build_csv.py
python scripts/build_search_index.py
cp README.md docs/datasets.md
