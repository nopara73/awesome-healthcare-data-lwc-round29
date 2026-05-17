# OMOP Vocabulary Coverage

Track whether each dataset is:

- `canonical-target`: the CDM/vocabulary layer itself.
- `native-omop-oriented`: source platform already exposes OMOP-shaped structures.
- `well-supported`: community ETL or common production mapping exists.
- `custom-claims-etl` / `custom-encounter-etl`: source data can be mapped, but project-specific ETL is expected.
- `geospatial-context-enrichment`: better used as contextual enrichment than direct OMOP fact tables.
- `not-primary-omop-source`: source is mainly an indicator, survey, or policy-data layer.

Always preserve source fields. OMOP standardization accelerates feature reuse, but source nuance is often essential for audit and model interpretation.
