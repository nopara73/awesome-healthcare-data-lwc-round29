# Provider benchmarking

Use this page as a dataset acquisition and feature-source shortlist. Start with open and synthetic resources for pipeline development, then graduate to DUA/IRB assets once the cohort, target, validation plan, and security posture are stable.

| Dataset | Tier | Why it matters | OMOP/CDM status | PHI posture |
|---|---:|---|---|---|
| [NPPES](https://download.cms.gov/nppes/NPI_Files.html) | `open` | one record per NPI plus taxonomy, address, endpoint, and status fields | provider-dimension-enrichment | none-provider-public |
| [Medicare Provider Utilization](https://data.cms.gov/provider-summary-by-type-of-service) | `open` | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | public-aggregate-or-restricted-microdata |
| [Open Payments](https://openpaymentsdata.cms.gov/) | `open` | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | public-aggregate-or-restricted-microdata |
| [HCAHPS](https://www.cms.gov/medicare/quality/initiatives/hospital-quality-initiative/hcahps-patients-perspectives-care-survey) | `open` | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | public-aggregate-or-restricted-microdata |
| [CMS Care Compare](https://data.cms.gov/provider-data/) | `open` | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | public-aggregate-or-restricted-microdata |
| [HCRIS](https://www.cms.gov/data-research/statistics-trends-and-reports/cost-reports) | `open` | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | public-aggregate-or-restricted-microdata |
| [DocGraph](https://careset.com/docgraph-open-social-doctor-data/) | `open` | provider, facility, taxonomy, or provider-pair edge | provider-dimension-enrichment | none-provider-public |


## Starter modeling notes

- Define the cohort, time-zero, prediction window, and outcome before selecting predictors.
- Preserve source-code era, geography vintage, and release version in every feature table.
- Keep leakage checks close to the use case: future claims, post-outcome labs, and target-derived facility measures are common healthcare ML traps.
- Validate on at least one source with a different population, site, payer, or geography when feasible.
