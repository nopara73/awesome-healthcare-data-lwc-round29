# Awesome Health Data

A machine-readable catalog of healthcare, public health, SDOH, claims, research, imaging, genomics, drug, and global-health datasets for ML and analytics.

> This README is generated from `datasets/**/*.yaml`. Do not hand-edit dataset tables; update YAML and rerun `make build`.

## What makes this maintainable

- **Machine-readable entries**: every dataset is YAML validated against `schemas/dataset.schema.json`.
- **Use-case-first navigation**: `use-cases/` pages shortlist datasets for real ML workflows.
- **Access-tier + PHI filters**: prototype-now sources are separated from DUA/IRB assets.
- **OMOP/PCORnet mapping status**: each entry records CDM fit and ETL notes.
- **Crosswalks and notebooks**: vocabulary/geography joins and starter analyses are first-class content.
- **Freshness signals**: CI can flag stale `last_validated` dates and broken links.

## Start here

- [Getting started](docs/getting-started.md)
- [Access tiers](docs/access-tiers.md)
- [PHI guide](docs/phi-guide.md)
- [Use cases](use-cases/)
- [Crosswalks](crosswalks/)
- [Playbooks](playbooks/)
- [Generated exports](exports/)

## Dataset index

Total entries: **108**.

### Terminologies & Vocabularies

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [ATC/DDD](https://atcddd.fhi.no/)<br><sub>[yaml](datasets/terminologies/atc-ddd.yaml)</sub> | `open` | none | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | seed | 2026-05-17 |
| [CPT/HCPCS](https://www.cms.gov/medicare/coding/healthcare-common-procedure-system)<br><sub>[yaml](datasets/terminologies/cpt-hcpcs-level-ii.yaml)</sub> | `purchase` | none | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | seed | 2026-05-17 |
| [NDC Directory](https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory)<br><sub>[yaml](datasets/terminologies/fda-ndc-directory.yaml)</sub> | `open` | none | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | seed | 2026-05-17 |
| [ICD-10-CM/PCS](https://www.cms.gov/medicare/coding-billing/icd-10-codes)<br><sub>[yaml](datasets/terminologies/icd-10-cm-pcs.yaml)</sub> | `open` | none | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | seed | 2026-05-17 |
| [ICD-11](https://icd.who.int/browse11)<br><sub>[yaml](datasets/terminologies/icd-11.yaml)</sub> | `open` | none | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | seed | 2026-05-17 |
| [ICD-9-CM/GEMs](https://www.cms.gov/medicare/coding-billing/icd-10-codes/general-equivalence-mappings)<br><sub>[yaml](datasets/terminologies/icd-9-cm-gems.yaml)</sub> | `open` | none | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | seed | 2026-05-17 |
| [ICD-O-3](https://seer.cancer.gov/icd-o-3/)<br><sub>[yaml](datasets/terminologies/icd-o-3.yaml)</sub> | `open` | none | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | seed | 2026-05-17 |
| [LOINC](https://loinc.org/downloads/)<br><sub>[yaml](datasets/terminologies/loinc.yaml)</sub> | `registration` | none | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | seed | 2026-05-17 |
| [MedDRA](https://www.meddra.org/)<br><sub>[yaml](datasets/terminologies/meddra.yaml)</sub> | `purchase` | none | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | seed | 2026-05-17 |
| [MeSH](https://www.nlm.nih.gov/mesh/download_mesh.html)<br><sub>[yaml](datasets/terminologies/mesh.yaml)</sub> | `open` | none | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | seed | 2026-05-17 |
| [DRG groupers](https://www.cms.gov/medicare/payment/prospective-payment-systems/acute-inpatient-pps/ms-drg-classifications-and-software)<br><sub>[yaml](datasets/terminologies/ms-drg-apr-drg.yaml)</sub> | `mixed` | none | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | seed | 2026-05-17 |
| [NCIt](https://evs.nci.nih.gov/ftp1/NCI_Thesaurus/)<br><sub>[yaml](datasets/terminologies/nci-thesaurus.yaml)</sub> | `open` | none | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | seed | 2026-05-17 |
| [OMOP/Athena](https://athena.ohdsi.org/)<br><sub>[yaml](datasets/terminologies/omop-cdm-athena.yaml)</sub> | `registration` | depends-on-source-data | OMOP CDM tables and standardized vocabulary tables | canonical-target | reference | 2026-05-17 |
| [RxNorm](https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html)<br><sub>[yaml](datasets/terminologies/rxnorm.yaml)</sub> | `open` | none | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | seed | 2026-05-17 |
| [SNOMED CT](https://www.nlm.nih.gov/healthit/snomedct/)<br><sub>[yaml](datasets/terminologies/snomed-ct.yaml)</sub> | `registration` | none | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | seed | 2026-05-17 |
| [UMLS](https://www.nlm.nih.gov/research/umls/)<br><sub>[yaml](datasets/terminologies/umls-metathesaurus.yaml)</sub> | `registration` | none | CUI, atom, string, semantic type, and relationship tables in Rich Release Format | terminology-reconciliation | reference | 2026-05-17 |

### CMS / Medicare

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [CMS Care Compare](https://data.cms.gov/provider-data/)<br><sub>[yaml](datasets/cms-medicare/cms-care-compare-family.yaml)</sub> | `open` | public-aggregate-or-restricted-microdata | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | seed | 2026-05-17 |
| [Open Payments](https://openpaymentsdata.cms.gov/)<br><sub>[yaml](datasets/cms-medicare/cms-open-payments.yaml)</sub> | `open` | public-aggregate-or-restricted-microdata | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | seed | 2026-05-17 |
| [POS File](https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/provider-of-services-file)<br><sub>[yaml](datasets/cms-medicare/cms-provider-of-services-file.yaml)</sub> | `open` | public-aggregate-or-restricted-microdata | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | seed | 2026-05-17 |
| [HCAHPS](https://www.cms.gov/medicare/quality/initiatives/hospital-quality-initiative/hcahps-patients-perspectives-care-survey)<br><sub>[yaml](datasets/cms-medicare/hcahps.yaml)</sub> | `open` | public-aggregate-or-restricted-microdata | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | seed | 2026-05-17 |
| [MEPS](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files.jsp)<br><sub>[yaml](datasets/cms-medicare/meps.yaml)</sub> | `open` | public-aggregate-or-restricted-microdata | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | seed | 2026-05-17 |
| [MA enrollment/landscape](https://www.cms.gov/data-research/statistics-trends-and-reports/medicareadvantagepartdenrollment)<br><sub>[yaml](datasets/cms-medicare/medicare-advantage-enrollment-landscape.yaml)</sub> | `open` | public-aggregate-or-restricted-microdata | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | seed | 2026-05-17 |
| [MBSF](https://resdac.org/cms-data/files/mbsf-base)<br><sub>[yaml](datasets/cms-medicare/medicare-beneficiary-summary-file.yaml)</sub> | `dua` | public-aggregate-or-restricted-microdata | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | seed | 2026-05-17 |
| [DE-SynPUF](https://www.cms.gov/data-research/statistics-trends-and-reports/medicare-claims-synthetic-public-use-files)<br><sub>[yaml](datasets/cms-medicare/medicare-synpuf.yaml)</sub> | `open` | synthetic | synthetic beneficiary, claim, claim-line, and prescription event records | well-supported | reference | 2026-05-17 |
| [HCRIS](https://www.cms.gov/data-research/statistics-trends-and-reports/cost-reports)<br><sub>[yaml](datasets/cms-medicare/medicare-cost-reports-hcris.yaml)</sub> | `open` | public-aggregate-or-restricted-microdata | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | seed | 2026-05-17 |
| [Medicare FFS Claims](https://resdac.org/cms-data/request/cms-data-request-center)<br><sub>[yaml](datasets/cms-medicare/medicare-ffs-claims-rif.yaml)</sub> | `dua` | research-identifiable-or-limited-data-set | beneficiary, claim, claim-line, enrollment-month, and provider/facility records | well-supported | reference | 2026-05-17 |
| [Medicare Provider Utilization](https://data.cms.gov/provider-summary-by-type-of-service)<br><sub>[yaml](datasets/cms-medicare/medicare-provider-utilization-payment.yaml)</sub> | `open` | public-aggregate-or-restricted-microdata | provider, beneficiary, claim, claim-line, plan, or facility-measure record depending on file | supported-or-custom-claims-etl | seed | 2026-05-17 |

### Medicaid

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [TAF / T-MSIS](https://www.medicaid.gov/medicaid/data-systems/macbis/transformed-medicaid-statistical-information-system-t-msis/index.html)<br><sub>[yaml](datasets/medicaid/tmsis-analytic-files.yaml)</sub> | `dua` | restricted | beneficiary eligibility, enrollment, claim, encounter, and service-line files | custom-claims-etl | reference | 2026-05-17 |

### CDC Surveillance & Public Health

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [BRFSS](https://www.cdc.gov/brfss/data_documentation/index.htm)<br><sub>[yaml](datasets/cdc-surveillance/brfss.yaml)</sub> | `open` | public-use-deidentified-or-aggregate | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | seed | 2026-05-17 |
| [WONDER](https://wonder.cdc.gov/)<br><sub>[yaml](datasets/cdc-surveillance/cdc-wonder.yaml)</sub> | `open` | public-use-deidentified-or-aggregate | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | seed | 2026-05-17 |
| [FluView](https://www.cdc.gov/fluview/)<br><sub>[yaml](datasets/cdc-surveillance/fluview-flusurvnet.yaml)</sub> | `open` | public-use-deidentified-or-aggregate | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | seed | 2026-05-17 |
| [NHANES](https://www.cdc.gov/nchs/nhanes/index.htm)<br><sub>[yaml](datasets/cdc-surveillance/nhanes.yaml)</sub> | `open` | public-use-deidentified-or-aggregate | person-level component files keyed by SEQN across two-year survey cycles | custom-survey-etl | reference | 2026-05-17 |
| [NHIS](https://www.cdc.gov/nchs/nhis/documentation/index.html)<br><sub>[yaml](datasets/cdc-surveillance/nhis.yaml)</sub> | `open` | public-use-deidentified-or-aggregate | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | seed | 2026-05-17 |
| [NHSN](https://www.cdc.gov/nhsn/)<br><sub>[yaml](datasets/cdc-surveillance/nhsn.yaml)</sub> | `dua` | public-use-deidentified-or-aggregate | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | seed | 2026-05-17 |
| [NNDSS](https://www.cdc.gov/nndss/)<br><sub>[yaml](datasets/cdc-surveillance/nndss.yaml)</sub> | `open` | public-use-deidentified-or-aggregate | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | seed | 2026-05-17 |
| [NPCR](https://www.cdc.gov/national-program-cancer-registries/index.html)<br><sub>[yaml](datasets/cdc-surveillance/npcr.yaml)</sub> | `dua` | public-use-deidentified-or-aggregate | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | seed | 2026-05-17 |
| [NSDUH](https://www.samhsa.gov/data/data-we-collect/nsduh-national-survey-drug-use-and-health)<br><sub>[yaml](datasets/cdc-surveillance/nsduh.yaml)</sub> | `open` | public-use-deidentified-or-aggregate | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | seed | 2026-05-17 |
| [NVSS](https://www.cdc.gov/nchs/nvss/index.htm)<br><sub>[yaml](datasets/cdc-surveillance/nvss.yaml)</sub> | `open` | public-use-deidentified-or-aggregate | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | seed | 2026-05-17 |
| [PLACES](https://www.cdc.gov/places/)<br><sub>[yaml](datasets/cdc-surveillance/places-500-cities.yaml)</sub> | `open` | public-use-deidentified-or-aggregate | county, place, census tract, and ZCTA-level modeled indicator estimate | geospatial-context-enrichment | reference | 2026-05-17 |
| [PRAMS](https://www.cdc.gov/prams/php/data-research/index.html)<br><sub>[yaml](datasets/cdc-surveillance/prams.yaml)</sub> | `dua` | public-use-deidentified-or-aggregate | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | seed | 2026-05-17 |
| [SEER](https://seer.cancer.gov/data/)<br><sub>[yaml](datasets/cdc-surveillance/seer.yaml)</sub> | `registration` | public-use-deidentified-or-aggregate | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | seed | 2026-05-17 |
| [VAERS](https://vaers.hhs.gov/data.html)<br><sub>[yaml](datasets/cdc-surveillance/vaers.yaml)</sub> | `open` | public-use-deidentified-or-aggregate | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | seed | 2026-05-17 |
| [WISQARS](https://wisqars.cdc.gov/)<br><sub>[yaml](datasets/cdc-surveillance/wisqars.yaml)</sub> | `open` | public-use-deidentified-or-aggregate | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | seed | 2026-05-17 |
| [YRBSS](https://www.cdc.gov/yrbs/)<br><sub>[yaml](datasets/cdc-surveillance/yrbss.yaml)</sub> | `open` | public-use-deidentified-or-aggregate | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | seed | 2026-05-17 |

### HCUP

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [HCUP KID](https://hcup-us.ahrq.gov/kidoverview.jsp)<br><sub>[yaml](datasets/hcup/hcup-kid.yaml)</sub> | `purchase` | deidentified-governed | weighted hospital discharge or encounter record | custom-encounter-etl | seed | 2026-05-17 |
| [HCUP NIS](https://hcup-us.ahrq.gov/nisoverview.jsp)<br><sub>[yaml](datasets/hcup/hcup-nis.yaml)</sub> | `purchase` | deidentified-governed | discharge-level inpatient record with survey design variables and weights | custom-discharge-etl | reference | 2026-05-17 |
| [HCUP NEDS](https://hcup-us.ahrq.gov/nedsoverview.jsp)<br><sub>[yaml](datasets/hcup/hcup-neds.yaml)</sub> | `purchase` | deidentified-governed | weighted hospital discharge or encounter record | custom-encounter-etl | seed | 2026-05-17 |
| [HCUP SID/SASD](https://hcup-us.ahrq.gov/db/state/siddbdocumentation.jsp)<br><sub>[yaml](datasets/hcup/hcup-sid-sasd.yaml)</sub> | `purchase` | deidentified-governed | weighted hospital discharge or encounter record | custom-encounter-etl | seed | 2026-05-17 |

### Claims, Cost & Transparency

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [CA HCAI](https://hcai.ca.gov/data/data-resources/)<br><sub>[yaml](datasets/claims-commercial/ca-hcai.yaml)</sub> | `mixed` | none-to-restricted | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | seed | 2026-05-17 |
| [HCCI](https://healthcostinstitute.org/data)<br><sub>[yaml](datasets/claims-commercial/hcci-commercial-claims.yaml)</sub> | `dua` | none-to-restricted | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | seed | 2026-05-17 |
| [Hospital Price Transparency](https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency)<br><sub>[yaml](datasets/claims-commercial/hospital-price-transparency-mrfs.yaml)</sub> | `open` | none-to-restricted | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | seed | 2026-05-17 |
| [NY SPARCS](https://www.health.ny.gov/statistics/sparcs/access/)<br><sub>[yaml](datasets/claims-commercial/ny-sparcs.yaml)</sub> | `mixed` | none-to-restricted | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | seed | 2026-05-17 |
| [State APCDs](https://www.apcdcouncil.org/)<br><sub>[yaml](datasets/claims-commercial/state-apcds.yaml)</sub> | `mixed` | mixed-public-aggregate-to-restricted-microdata | member, enrollment month, claim, claim-line, provider, or aggregate depending state and access tier | custom-state-claims-etl | reference | 2026-05-17 |
| [TX THCIC](https://www.dshs.texas.gov/center-health-statistics/texas-health-care-information-collection)<br><sub>[yaml](datasets/claims-commercial/tx-thcic.yaml)</sub> | `mixed` | none-to-restricted | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | seed | 2026-05-17 |
| [TiC MRFs](https://www.cms.gov/priorities/healthplan-price-transparency)<br><sub>[yaml](datasets/claims-commercial/transparency-in-coverage-mrfs.yaml)</sub> | `open` | none-to-restricted | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | seed | 2026-05-17 |

### Provider Data

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [Doctors & Clinicians](https://data.cms.gov/provider-data/topics/doctors-clinicians)<br><sub>[yaml](datasets/provider/cms-doctors-clinicians.yaml)</sub> | `open` | none-provider-public | provider, facility, taxonomy, or provider-pair edge | provider-dimension-enrichment | seed | 2026-05-17 |
| [Provider Data Catalog](https://data.cms.gov/provider-data/)<br><sub>[yaml](datasets/provider/cms-provider-data-catalog.yaml)</sub> | `open` | none-provider-public | provider, facility, taxonomy, or provider-pair edge | provider-dimension-enrichment | seed | 2026-05-17 |
| [DocGraph](https://careset.com/docgraph-open-social-doctor-data/)<br><sub>[yaml](datasets/provider/docgraph-referral-graph.yaml)</sub> | `open` | none-provider-public | provider, facility, taxonomy, or provider-pair edge | provider-dimension-enrichment | seed | 2026-05-17 |
| [NPDB PUF](https://www.npdb.hrsa.gov/resources/publicData.jsp)<br><sub>[yaml](datasets/provider/npdb-public-use-file.yaml)</sub> | `open` | none-provider-public | provider, facility, taxonomy, or provider-pair edge | provider-dimension-enrichment | seed | 2026-05-17 |
| [NPPES](https://download.cms.gov/nppes/NPI_Files.html)<br><sub>[yaml](datasets/provider/nppes-npi-registry.yaml)</sub> | `open` | none-provider-public | one record per NPI plus taxonomy, address, endpoint, and status fields | provider-dimension-enrichment | reference | 2026-05-17 |
| [NUCC Taxonomy](https://taxonomy.nucc.org/)<br><sub>[yaml](datasets/provider/nucc-provider-taxonomy.yaml)</sub> | `open` | none-provider-public | provider, facility, taxonomy, or provider-pair edge | provider-dimension-enrichment | seed | 2026-05-17 |

### SDOH & Environment

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [AHRQ SDOH](https://www.ahrq.gov/sdoh/data-analytics/sdoh-data.html)<br><sub>[yaml](datasets/sdoh/ahrq-sdoh-database.yaml)</sub> | `open` | none-aggregate-geography | county- and ZIP-level SDOH variables by year/vintage | geospatial-context-enrichment | reference | 2026-05-17 |
| [ADI](https://www.neighborhoodatlas.medicine.wisc.edu/)<br><sub>[yaml](datasets/sdoh/area-deprivation-index.yaml)</sub> | `registration` | none-aggregate-geography | census block-group or ZIP/neighborhood deprivation score depending product | geospatial-context-enrichment | reference | 2026-05-17 |
| [AHRF](https://data.hrsa.gov/data/download)<br><sub>[yaml](datasets/sdoh/hrsa-ahrf.yaml)</sub> | `open` | none-aggregate-geography | county, tract, block-group, ZIP, ZCTA, or geography-time indicator | geospatial-context-enrichment | seed | 2026-05-17 |
| [LAUS](https://www.bls.gov/lau/)<br><sub>[yaml](datasets/sdoh/bls-laus.yaml)</sub> | `open` | none-aggregate-geography | county, tract, block-group, ZIP, ZCTA, or geography-time indicator | geospatial-context-enrichment | seed | 2026-05-17 |
| [SVI](https://www.atsdr.cdc.gov/place-health/php/svi/)<br><sub>[yaml](datasets/sdoh/cdc-atsdr-svi.yaml)</sub> | `open` | none-aggregate-geography | county, tract, block-group, ZIP, ZCTA, or geography-time indicator | geospatial-context-enrichment | seed | 2026-05-17 |
| [CHR&R](https://www.countyhealthrankings.org/health-data)<br><sub>[yaml](datasets/sdoh/county-health-rankings.yaml)</sub> | `open` | none-aggregate-geography | county/state measure and rank records | geospatial-context-enrichment | reference | 2026-05-17 |
| [Dartmouth Atlas](https://data.dartmouthatlas.org/)<br><sub>[yaml](datasets/sdoh/dartmouth-atlas.yaml)</sub> | `open` | none-aggregate-geography | Hospital Referral Region, Hospital Service Area, provider, or geographic measure depending extract | geospatial-and-provider-context-enrichment | reference | 2026-05-17 |
| [EPA AQS](https://www.epa.gov/aqs)<br><sub>[yaml](datasets/sdoh/epa-aqs.yaml)</sub> | `open` | none-aggregate-geography | county, tract, block-group, ZIP, ZCTA, or geography-time indicator | geospatial-context-enrichment | seed | 2026-05-17 |
| [EJScreen](https://www.epa.gov/ejscreen)<br><sub>[yaml](datasets/sdoh/epa-ejscreen.yaml)</sub> | `open` | none-aggregate-geography | county, tract, block-group, ZIP, ZCTA, or geography-time indicator | geospatial-context-enrichment | seed | 2026-05-17 |
| [Walkability Index](https://www.epa.gov/smartgrowth/smart-location-mapping)<br><sub>[yaml](datasets/sdoh/epa-walkability-index.yaml)</sub> | `open` | none-aggregate-geography | county, tract, block-group, ZIP, ZCTA, or geography-time indicator | geospatial-context-enrichment | seed | 2026-05-17 |
| [HUD PIT/HMIS](https://www.huduser.gov/portal/datasets/ahar.html)<br><sub>[yaml](datasets/sdoh/hud-hmis-pit.yaml)</sub> | `mixed` | none-aggregate-geography | county, tract, block-group, ZIP, ZCTA, or geography-time indicator | geospatial-context-enrichment | seed | 2026-05-17 |
| [USDA Food Atlas](https://www.ers.usda.gov/data-products/food-access-research-atlas/)<br><sub>[yaml](datasets/sdoh/usda-food-access-environment.yaml)</sub> | `open` | none-aggregate-geography | county, tract, block-group, ZIP, ZCTA, or geography-time indicator | geospatial-context-enrichment | seed | 2026-05-17 |
| [RUCA](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/)<br><sub>[yaml](datasets/sdoh/ruca-codes.yaml)</sub> | `open` | none-aggregate-geography | county, tract, block-group, ZIP, ZCTA, or geography-time indicator | geospatial-context-enrichment | seed | 2026-05-17 |

### Census & Demographic

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [ACS](https://www.census.gov/programs-surveys/acs/data.html)<br><sub>[yaml](datasets/census/acs-1yr-5yr.yaml)</sub> | `open` | none-aggregate-geography | geography-indicator-year estimate | geospatial-context-enrichment | seed | 2026-05-17 |
| [Decennial Census](https://www.census.gov/programs-surveys/decennial-census/data.html)<br><sub>[yaml](datasets/census/decennial-census.yaml)</sub> | `open` | none-aggregate-geography | geography-indicator-year estimate | geospatial-context-enrichment | seed | 2026-05-17 |
| [LEHD](https://lehd.ces.census.gov/data/)<br><sub>[yaml](datasets/census/lehd-onthemap.yaml)</sub> | `open` | none-aggregate-geography | geography-indicator-year estimate | geospatial-context-enrichment | seed | 2026-05-17 |
| [SAHIE](https://www.census.gov/programs-surveys/sahie.html)<br><sub>[yaml](datasets/census/sahie.yaml)</sub> | `open` | none-aggregate-geography | geography-indicator-year estimate | geospatial-context-enrichment | seed | 2026-05-17 |
| [SAIPE](https://www.census.gov/programs-surveys/saipe.html)<br><sub>[yaml](datasets/census/saipe.yaml)</sub> | `open` | none-aggregate-geography | geography-indicator-year estimate | geospatial-context-enrichment | seed | 2026-05-17 |

### Clinical / Research / ICU

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [All of Us](https://www.researchallofus.org/)<br><sub>[yaml](datasets/clinical-research/all-of-us.yaml)</sub> | `registration` | controlled-access-deidentified | participant-level OMOP tables, surveys, measurements, biospecimens, wearables, and genomics by access tier | native-omop-oriented | reference | 2026-05-17 |
| [ClinicalTrials.gov](https://clinicaltrials.gov/data-api)<br><sub>[yaml](datasets/clinical-research/clinicaltrials-gov.yaml)</sub> | `open` | credentialed-deidentified-or-controlled | participant, encounter, stay, event, waveform, image, or study record | supported-for-some-sources | seed | 2026-05-17 |
| [dbGaP](https://www.ncbi.nlm.nih.gov/gap/)<br><sub>[yaml](datasets/clinical-research/dbgap.yaml)</sub> | `irb` | credentialed-deidentified-or-controlled | participant, encounter, stay, event, waveform, image, or study record | supported-for-some-sources | seed | 2026-05-17 |
| [eICU-CRD](https://physionet.org/content/eicu-crd/2.0/)<br><sub>[yaml](datasets/clinical-research/eicu-crd.yaml)</sub> | `registration` | deidentified-credentialed | ICU patient/unit-stay/event tables across multiple hospitals | custom-critical-care-etl | reference | 2026-05-17 |
| [MIMIC-CXR](https://physionet.org/content/mimic-cxr/)<br><sub>[yaml](datasets/clinical-research/mimic-cxr.yaml)</sub> | `registration` | credentialed-deidentified-or-controlled | participant, encounter, stay, event, waveform, image, or study record | supported-for-some-sources | seed | 2026-05-17 |
| [MIMIC-III](https://physionet.org/content/mimiciii/)<br><sub>[yaml](datasets/clinical-research/mimic-iii.yaml)</sub> | `registration` | credentialed-deidentified-or-controlled | participant, encounter, stay, event, waveform, image, or study record | supported-for-some-sources | seed | 2026-05-17 |
| [MIMIC-IV](https://physionet.org/content/mimiciv/)<br><sub>[yaml](datasets/clinical-research/mimic-iv.yaml)</sub> | `registration` | deidentified-credentialed | person, admission, ICU stay, procedure, diagnosis, lab, medication, chart-event, and note/module records depending access | well-supported | reference | 2026-05-17 |
| [PhysioNet](https://physionet.org/)<br><sub>[yaml](datasets/clinical-research/physionet.yaml)</sub> | `mixed` | credentialed-deidentified-or-controlled | participant, encounter, stay, event, waveform, image, or study record | supported-for-some-sources | seed | 2026-05-17 |
| [SEER-Medicare](https://healthcaredelivery.cancer.gov/seermedicare/obtain/)<br><sub>[yaml](datasets/clinical-research/seer-medicare.yaml)</sub> | `dua` | restricted-linked-registry-claims | tumor/case registry records linked to beneficiary enrollment and Medicare claims | custom-registry-plus-claims-etl | reference | 2026-05-17 |
| [UK Biobank](https://www.ukbiobank.ac.uk/use-our-data/apply-for-access/)<br><sub>[yaml](datasets/clinical-research/uk-biobank.yaml)</sub> | `irb` | credentialed-deidentified-or-controlled | participant, encounter, stay, event, waveform, image, or study record | supported-for-some-sources | seed | 2026-05-17 |

### Drug & Pharmacology

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [ChEMBL](https://www.ebi.ac.uk/chembl/downloads/)<br><sub>[yaml](datasets/drug-pharma/chembl.yaml)</sub> | `open` | none-public-regulatory-or-knowledgebase | drug product, label, adverse-event report, compound, target, or safety concept | drug-vocabulary-or-knowledge-enrichment | seed | 2026-05-17 |
| [DailyMed](https://dailymed.nlm.nih.gov/dailymed/spl-resources-all-drug-labels.cfm)<br><sub>[yaml](datasets/drug-pharma/dailymed.yaml)</sub> | `open` | none-public-regulatory-or-knowledgebase | drug product, label, adverse-event report, compound, target, or safety concept | drug-vocabulary-or-knowledge-enrichment | seed | 2026-05-17 |
| [DrugBank](https://go.drugbank.com/)<br><sub>[yaml](datasets/drug-pharma/drugbank.yaml)</sub> | `purchase` | none-public-regulatory-or-knowledgebase | drug product, label, adverse-event report, compound, target, or safety concept | drug-vocabulary-or-knowledge-enrichment | seed | 2026-05-17 |
| [FAERS](https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers/fda-adverse-event-reporting-system-faers-public-dashboard)<br><sub>[yaml](datasets/drug-pharma/faers.yaml)</sub> | `open` | none-public-regulatory-or-knowledgebase | case/report tables across demographic, drug, reaction, indication, outcome, and therapy components | custom-pharmacovigilance-etl | reference | 2026-05-17 |
| [Orange/Purple Book](https://www.fda.gov/drugs/drug-approvals-and-databases/approved-drug-products-therapeutic-equivalence-evaluations-orange-book)<br><sub>[yaml](datasets/drug-pharma/orange-purple-book.yaml)</sub> | `open` | none-public-regulatory-or-knowledgebase | drug product, label, adverse-event report, compound, target, or safety concept | drug-vocabulary-or-knowledge-enrichment | seed | 2026-05-17 |
| [openFDA](https://open.fda.gov/)<br><sub>[yaml](datasets/drug-pharma/openfda.yaml)</sub> | `open` | none-public-regulatory-or-knowledgebase | endpoint-specific JSON record or bulk download document | knowledge-enrichment | reference | 2026-05-17 |
| [SIDER](http://sideeffects.embl.de/)<br><sub>[yaml](datasets/drug-pharma/sider.yaml)</sub> | `open` | none-public-regulatory-or-knowledgebase | drug product, label, adverse-event report, compound, target, or safety concept | drug-vocabulary-or-knowledge-enrichment | seed | 2026-05-17 |

### Imaging

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [ADNI](https://adni.loni.usc.edu/data-samples/)<br><sub>[yaml](datasets/imaging/adni.yaml)</sub> | `registration` | deidentified-or-governed | image, study, series, DICOM object, report, participant, or collection | custom-imaging-extension | seed | 2026-05-17 |
| [CheXpert](https://aimi.stanford.edu/datasets/chexpert-chest-x-rays)<br><sub>[yaml](datasets/imaging/chexpert.yaml)</sub> | `registration` | deidentified-or-governed | image, study, series, DICOM object, report, participant, or collection | custom-imaging-extension | seed | 2026-05-17 |
| [ISIC](https://www.isic-archive.com/)<br><sub>[yaml](datasets/imaging/isic-archive.yaml)</sub> | `open` | deidentified-or-governed | image, study, series, DICOM object, report, participant, or collection | custom-imaging-extension | seed | 2026-05-17 |
| [ChestX-ray14](https://nihcc.app.box.com/v/ChestXray-NIHCC)<br><sub>[yaml](datasets/imaging/nih-chestxray14.yaml)</sub> | `open` | deidentified-or-governed | image, study, series, DICOM object, report, participant, or collection | custom-imaging-extension | seed | 2026-05-17 |
| [TCIA](https://www.cancerimagingarchive.net/collections/)<br><sub>[yaml](datasets/imaging/tcia.yaml)</sub> | `open` | deidentified-or-governed | image, study, series, DICOM object, report, participant, or collection | custom-imaging-extension | seed | 2026-05-17 |

### Genomics / Phenotype

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [ClinVar-OMIM-gnomAD](https://www.ncbi.nlm.nih.gov/clinvar/)<br><sub>[yaml](datasets/genomics/clinvar-omim-gnomad.yaml)</sub> | `mixed` | none-public-aggregate-or-controlled-if-individual-level | variant, gene, phenotype, association, or ontology concept | custom-genomics-extension | seed | 2026-05-17 |
| [HPO](https://hpo.jax.org/app/download/ontology)<br><sub>[yaml](datasets/genomics/human-phenotype-ontology.yaml)</sub> | `open` | none-public-aggregate-or-controlled-if-individual-level | variant, gene, phenotype, association, or ontology concept | custom-genomics-extension | seed | 2026-05-17 |
| [GWAS Catalog](https://www.ebi.ac.uk/gwas/downloads)<br><sub>[yaml](datasets/genomics/gwas-catalog.yaml)</sub> | `open` | none-public-aggregate-or-controlled-if-individual-level | variant, gene, phenotype, association, or ontology concept | custom-genomics-extension | seed | 2026-05-17 |

### International / Global Health

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [Eurostat Health](https://ec.europa.eu/eurostat/web/health/database)<br><sub>[yaml](datasets/international/eurostat-health.yaml)</sub> | `open` | none-aggregate-or-deidentified-survey | country, region, indicator, survey respondent, household, or modeled estimate | not-primary-omop-source | seed | 2026-05-17 |
| [GBD + DHS](https://www.healthdata.org/research-analysis/gbd)<br><sub>[yaml](datasets/international/ihme-gbd-dhs.yaml)</sub> | `mixed` | none-aggregate-or-deidentified-survey | country, region, indicator, survey respondent, household, or modeled estimate | not-primary-omop-source | seed | 2026-05-17 |
| [OECD Health Statistics](https://www.oecd.org/en/data/datasets/oecd-health-statistics.html)<br><sub>[yaml](datasets/international/oecd-health-statistics.yaml)</sub> | `open` | none-aggregate-or-deidentified-survey | country, region, indicator, survey respondent, household, or modeled estimate | not-primary-omop-source | seed | 2026-05-17 |
| [WHO GHO](https://www.who.int/data/gho)<br><sub>[yaml](datasets/international/who-global-health-observatory.yaml)</sub> | `open` | none-aggregate-or-deidentified-survey | country, region, indicator, survey respondent, household, or modeled estimate | not-primary-omop-source | seed | 2026-05-17 |

## Contributing

Open a PR with a schema-valid YAML file under the right `datasets/<category>/` directory. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Repository metadata/docs are intended to be CC-BY-4.0; code is intended to be MIT. This repository does **not** grant rights to redistribute third-party data files.
