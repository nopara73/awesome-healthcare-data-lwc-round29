#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON:-python3}"
export PYTHONDONTWRITEBYTECODE=1

"$PYTHON_BIN" -m pip install -r requirements.txt
"$PYTHON_BIN" scripts/validate.py
"$PYTHON_BIN" scripts/build_readme.py
"$PYTHON_BIN" scripts/build_docs.py
"$PYTHON_BIN" scripts/build_csv.py
"$PYTHON_BIN" scripts/build_search_index.py
