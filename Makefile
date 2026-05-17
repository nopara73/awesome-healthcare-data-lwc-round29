PYTHON ?= python3
PYTHON_RUN = PYTHONDONTWRITEBYTECODE=1 $(PYTHON)

.PHONY: validate build links freshness site

validate:
	$(PYTHON_RUN) scripts/validate.py

build:
	$(PYTHON_RUN) scripts/build_readme.py
	$(PYTHON_RUN) scripts/build_docs.py
	$(PYTHON_RUN) scripts/build_csv.py
	$(PYTHON_RUN) scripts/build_search_index.py

links:
	$(PYTHON_RUN) scripts/check_links.py

freshness:
	$(PYTHON_RUN) scripts/check_freshness.py

site:
	mkdocs build --strict
