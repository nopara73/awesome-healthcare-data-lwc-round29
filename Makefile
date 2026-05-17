.PHONY: validate build links freshness site

validate:
	python scripts/validate.py

build:
	python scripts/build_readme.py
	python scripts/build_csv.py
	python scripts/build_search_index.py
	cp README.md docs/datasets.md

links:
	python scripts/check_links.py

freshness:
	python scripts/check_freshness.py

site:
	mkdocs build --strict
