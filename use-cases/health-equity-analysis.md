# Health equity analysis

Use this page as a dataset acquisition and feature-source shortlist. Start with open and synthetic resources for pipeline development, then graduate to DUA/IRB assets once the cohort, target, validation plan, and security posture are stable.

| Dataset | Tier | Why it matters | OMOP/CDM status | PHI posture |
|---|---:|---|---|---|
| [AHRQ SDOH](https://www.ahrq.gov/sdoh/data-analytics/sdoh-data.html) | `open` | county- and ZIP-level SDOH variables by year/vintage | geospatial-context-enrichment | none-aggregate-geography |
| [SVI](https://www.atsdr.cdc.gov/place-health/php/svi/) | `open` | county, tract, block-group, ZIP, ZCTA, or geography-time indicator | geospatial-context-enrichment | none-aggregate-geography |
| [ADI](https://www.neighborhoodatlas.medicine.wisc.edu/) | `registration` | census block-group or ZIP/neighborhood deprivation score depending product | geospatial-context-enrichment | none-aggregate-geography |
| [ACS](https://www.census.gov/programs-surveys/acs/data.html) | `open` | geography-indicator-year estimate | geospatial-context-enrichment | none-aggregate-geography |
| [RUCA](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/) | `open` | county, tract, block-group, ZIP, ZCTA, or geography-time indicator | geospatial-context-enrichment | none-aggregate-geography |
| [PLACES](https://www.cdc.gov/places/) | `open` | county, place, census tract, and ZCTA-level modeled indicator estimate | geospatial-context-enrichment | public-use-deidentified-or-aggregate |
| [SEER](https://seer.cancer.gov/data/) | `registration` | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | public-use-deidentified-or-aggregate |
| [MEPS](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files.jsp) | `open` | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | public-aggregate-or-restricted-microdata |
| [All of Us](https://www.researchallofus.org/) | `registration` | participant-level OMOP tables, surveys, measurements, biospecimens, wearables, and genomics by access tier | native-omop-oriented | controlled-access-deidentified |


## Starter modeling notes

- Define the cohort, time-zero, prediction window, and outcome before selecting predictors.
- Preserve source-code era, geography vintage, and release version in every feature table.
- Keep leakage checks close to the use case: future claims, post-outcome labs, and target-derived facility measures are common healthcare ML traps.
- Validate on at least one source with a different population, site, payer, or geography when feasible.
