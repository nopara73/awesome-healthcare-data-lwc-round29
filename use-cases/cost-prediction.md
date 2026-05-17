# Cost prediction

Use this page as a dataset acquisition and feature-source shortlist. Start with open and synthetic resources for pipeline development, then graduate to DUA/IRB assets once the cohort, target, validation plan, and security posture are stable.

| Dataset | Tier | Why it matters | OMOP/CDM status | PHI posture |
|---|---:|---|---|---|
| [Medicare FFS Claims](https://resdac.org/cms-data/request/cms-data-request-center) | `dua` | beneficiary, claim, claim-line, enrollment-month, and provider/facility records | well-supported | research-identifiable-or-limited-data-set |
| [MEPS](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files.jsp) | `open` | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | public-aggregate-or-restricted-microdata |
| [HCCI](https://healthcostinstitute.org/data) | `dua` | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | none-to-restricted |
| [State APCDs](https://www.apcdcouncil.org/) | `mixed` | member, enrollment month, claim, claim-line, provider, or aggregate depending state and access tier | custom-state-claims-etl | mixed-public-aggregate-to-restricted-microdata |
| [Hospital Price Transparency](https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency) | `open` | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | none-to-restricted |
| [TiC MRFs](https://www.cms.gov/priorities/healthplan-price-transparency) | `open` | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | none-to-restricted |
| [HCRIS](https://www.cms.gov/data-research/statistics-trends-and-reports/cost-reports) | `open` | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | public-aggregate-or-restricted-microdata |


## Starter modeling notes

- Define the cohort, time-zero, prediction window, and outcome before selecting predictors.
- Preserve source-code era, geography vintage, and release version in every feature table.
- Keep leakage checks close to the use case: future claims, post-outcome labs, and target-derived facility measures are common healthcare ML traps.
- Validate on at least one source with a different population, site, payer, or geography when feasible.
