# Disease surveillance

Use this page as a dataset acquisition and feature-source shortlist. Start with open and synthetic resources for pipeline development, then graduate to DUA/IRB assets once the cohort, target, validation plan, and security posture are stable.

| Dataset | Tier | Why it matters | OMOP/CDM status | PHI posture |
|---|---:|---|---|---|
| [NNDSS](https://www.cdc.gov/nndss/) | `open` | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | public-use-deidentified-or-aggregate |
| [WONDER](https://wonder.cdc.gov/) | `open` | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | public-use-deidentified-or-aggregate |
| [FluView](https://www.cdc.gov/fluview/) | `open` | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | public-use-deidentified-or-aggregate |
| [BRFSS](https://www.cdc.gov/brfss/data_documentation/index.htm) | `open` | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | public-use-deidentified-or-aggregate |
| [NHIS](https://www.cdc.gov/nchs/nhis/documentation/index.html) | `open` | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | public-use-deidentified-or-aggregate |
| [PLACES](https://www.cdc.gov/places/) | `open` | county, place, census tract, and ZCTA-level modeled indicator estimate | geospatial-context-enrichment | public-use-deidentified-or-aggregate |
| [WISQARS](https://wisqars.cdc.gov/) | `open` | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | public-use-deidentified-or-aggregate |


## Starter modeling notes

- Define the cohort, time-zero, prediction window, and outcome before selecting predictors.
- Preserve source-code era, geography vintage, and release version in every feature table.
- Keep leakage checks close to the use case: future claims, post-outcome labs, and target-derived facility measures are common healthcare ML traps.
- Validate on at least one source with a different population, site, payer, or geography when feasible.
