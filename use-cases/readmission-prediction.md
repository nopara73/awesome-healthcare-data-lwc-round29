# Readmission prediction

Use this page as a dataset acquisition and feature-source shortlist. Start with open and synthetic resources for pipeline development, then graduate to DUA/IRB assets once the cohort, target, validation plan, and security posture are stable.

| Dataset | Tier | Why it matters | OMOP/CDM status | PHI posture |
|---|---:|---|---|---|
| [DE-SynPUF](https://www.cms.gov/data-research/statistics-trends-and-reports/medicare-claims-synthetic-public-use-files) | `open` | synthetic beneficiary, claim, claim-line, and prescription event records | well-supported | synthetic |
| [Medicare FFS Claims](https://resdac.org/cms-data/request/cms-data-request-center) | `dua` | beneficiary, claim, claim-line, enrollment-month, and provider/facility records | well-supported | research-identifiable-or-limited-data-set |
| [MBSF](https://resdac.org/cms-data/files/mbsf-base) | `dua` | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | public-aggregate-or-restricted-microdata |
| [HCUP NIS](https://hcup-us.ahrq.gov/nisoverview.jsp) | `purchase` | discharge-level inpatient record with survey design variables and weights | custom-discharge-etl | deidentified-governed |
| [MIMIC-IV](https://physionet.org/content/mimiciv/) | `registration` | person, admission, ICU stay, procedure, diagnosis, lab, medication, chart-event, and note/module records depending access | well-supported | deidentified-credentialed |
| [AHRQ SDOH](https://www.ahrq.gov/sdoh/data-analytics/sdoh-data.html) | `open` | county- and ZIP-level SDOH variables by year/vintage | geospatial-context-enrichment | none-aggregate-geography |
| [ADI](https://www.neighborhoodatlas.medicine.wisc.edu/) | `registration` | census block-group or ZIP/neighborhood deprivation score depending product | geospatial-context-enrichment | none-aggregate-geography |
| [PLACES](https://www.cdc.gov/places/) | `open` | county, place, census tract, and ZCTA-level modeled indicator estimate | geospatial-context-enrichment | public-use-deidentified-or-aggregate |
| [NPPES](https://download.cms.gov/nppes/NPI_Files.html) | `open` | one record per NPI plus taxonomy, address, endpoint, and status fields | provider-dimension-enrichment | none-provider-public |


## Starter modeling notes

- Define the cohort, time-zero, prediction window, and outcome before selecting predictors.
- Preserve source-code era, geography vintage, and release version in every feature table.
- Keep leakage checks close to the use case: future claims, post-outcome labs, and target-derived facility measures are common healthcare ML traps.
- Validate on at least one source with a different population, site, payer, or geography when feasible.
