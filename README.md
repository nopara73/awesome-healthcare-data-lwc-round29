<p align="center"><img src="docs/assets/awesome-health-data-banner.png" alt="Abstract healthcare data network banner" width="100%"></p>

<h1 align="center">Awesome Healthcare Data</h1>

<p align="center"><strong>A machine-readable healthcare dataset catalog for ML, analytics, public health, policy, and life sciences teams.</strong></p>

<p align="center">
  <img alt="Datasets" src="https://img.shields.io/badge/datasets-108-0b7285.svg?style=for-the-badge">
  <img alt="Categories" src="https://img.shields.io/badge/categories-14-1864ab.svg?style=for-the-badge">
  <img alt="Open sources" src="https://img.shields.io/badge/open-69-2f9e44.svg?style=for-the-badge">
  <img alt="Generated from YAML" src="https://img.shields.io/badge/source-YAML-495057.svg?style=for-the-badge">
  <img alt="Awesome" src="https://img.shields.io/badge/awesome-health%20data-6741d9.svg?style=for-the-badge">
</p>

> This README is generated from `datasets/**/*.yaml`. Do not hand-edit dataset tables; update YAML and rerun `make build`.

## At a Glance

<table>
<tr>
<td align="center"><strong>108</strong><br><sub>datasets</sub></td>
<td align="center"><strong>14</strong><br><sub>categories</sub></td>
<td align="center"><strong>69</strong><br><sub>open sources</sub></td>
<td align="center"><strong>17</strong><br><sub>DUA, IRB, or purchase</sub></td>
<td align="center"><strong>20</strong><br><sub>reference entries</sub></td>
</tr>
</table>

## Start Here

| Need | Go to |
|---|---|
| Find a source by domain | [Category map](#category-map) |
| Compare access restrictions | [Access tiers](#access-tiers) |
| Browse every dataset | [Dataset index](#dataset-index) |
| Build a governed-data workflow | [PHI guide](docs/phi-guide.md) and [playbooks](playbooks/) |
| Prototype ML examples | [notebooks](notebooks/) and [sample data](examples/sample_data/) |
| Consume machine-readable exports | [CSV/JSON exports](exports/) |

## Category Map

| Category | Count | What it covers |
|---|---:|---|
| &#x1F524; [Terminologies & Vocabularies](#terminologies) | 16 | Code systems, vocabularies, and ontology sources for semantic normalization. |
| &#x1F3E5; [CMS / Medicare](#cms-medicare) | 11 | Medicare, quality, payment, enrollment, and federal provider datasets. |
| &#x1F91D; [Medicaid](#medicaid) | 1 | Medicaid and CHIP files for access, cost, eligibility, and utilization analysis. |
| &#x1F4CA; [CDC Surveillance & Public Health](#cdc-surveillance) | 16 | Public health surveillance, surveys, registries, and vital statistics. |
| &#x1F3E8; [HCUP](#hcup) | 4 | Encounter-level inpatient, emergency, and ambulatory surgery research assets. |
| &#x1F4B3; [Claims, Cost & Transparency](#claims-commercial) | 7 | Commercial claims, APCDs, price transparency, and state encounter files. |
| &#x1F9D1;&#x200D;&#x2695;&#xFE0F; [Provider Data](#provider) | 6 | Provider directories, taxonomy files, quality measures, and relationship data. |
| &#x1F3D8;&#xFE0F; [SDOH & Environment](#sdoh) | 13 | Social, economic, environmental, housing, workforce, and place-based context. |
| &#x1F5FA;&#xFE0F; [Census & Demographic](#census) | 5 | Population, insurance, poverty, commuting, and denominator datasets. |
| &#x1F52C; [Clinical / Research / ICU](#clinical-research) | 10 | Credentialed EHR, ICU, cohort, trial, and multimodal research datasets. |
| &#x1F48A; [Drug & Pharmacology](#drug-pharma) | 7 | Drug labels, approvals, adverse events, compounds, side effects, and safety data. |
| &#x1F5BC;&#xFE0F; [Imaging](#imaging) | 5 | Radiology, dermatology, cancer imaging, and benchmark medical image collections. |
| &#x1F9EC; [Genomics / Phenotype](#genomics) | 3 | Variant, phenotype, ontology, and association resources for genetics workflows. |
| &#x1F310; [International / Global Health](#international) | 4 | Global and country-comparable health indicators, burden, and system measures. |

## Access Tiers

| Tier | Count | Meaning |
|---|---:|---|
| `open` Open | 69 | Public download, API, or aggregate portal. |
| `registration` Registration | 13 | Free account, click-through terms, training, or attestation. |
| `dua` DUA | 8 | Data use agreement or project approval. |
| `irb` IRB | 2 | IRB, DAC, or human-subjects governed access. |
| `purchase` Purchase | 7 | Paid license or proprietary component. |
| `mixed` Mixed | 9 | Dataset family with multiple access paths. |

## What These Data Sources Can Help With

This catalog brings together data sources that help healthcare, life sciences, public health, policy, and analytics teams answer practical business questions: where care is delivered, what it costs, which populations are at risk, how communities differ, how drugs and devices perform, and how clinical evidence can be reused responsibly.

<details>
<summary><strong>&#x1F524; Terminologies & Vocabularies</strong> <sub>16 datasets</sub></summary>

Code systems, vocabularies, and ontology sources for semantic normalization.

- **[ATC/DDD](https://atcddd.fhi.no/)**: A global drug classification and dose-reference source that helps pharmacy, population health, and market access teams compare medication use across products, classes, regions, and time periods.
- **[CPT/HCPCS](https://www.cms.gov/medicare/coding/healthcare-common-procedure-system)**: The main U.S. procedure and service billing code sets, useful for understanding what care was delivered, pricing services, measuring utilization, and grouping outpatient or professional claims.
- **[NDC Directory](https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory)**: A public directory of U.S. drug product and package identifiers that helps teams normalize pharmacy claims, connect products to labels, and track medication portfolios.
- **[ICD-10-CM/PCS](https://www.cms.gov/medicare/coding-billing/icd-10-codes)**: The current U.S. diagnosis and inpatient procedure coding system, used to group diseases, procedures, utilization, quality measures, risk scores, and reimbursement analytics.
- **[ICD-11](https://icd.who.int/browse11)**: The WHO disease classification for global health reporting, useful for international comparisons, public health measurement, and planning analytics that need a modern worldwide disease framework.
- **[ICD-9-CM/GEMs](https://www.cms.gov/medicare/coding-billing/icd-10-codes/general-equivalence-mappings)**: Legacy diagnosis and procedure codes plus crosswalks that help teams interpret older claims, compare historical trends, and bridge pre-2015 data to newer coding systems.
- **[ICD-O-3](https://seer.cancer.gov/icd-o-3/)**: A cancer-specific coding standard for tumor site and histology that supports oncology registries, cancer outcomes research, tumor cohorting, and specialty analytics.
- **[LOINC](https://loinc.org/downloads/)**: A standard naming system for lab tests and clinical observations, useful for combining lab results across hospitals, vendors, and data feeds into comparable measures.
- **[MedDRA](https://www.meddra.org/)**: A global adverse-event terminology used in drug and device safety, helping safety, regulatory, and pharmacovigilance teams group symptoms and events consistently.
- **[MeSH](https://www.nlm.nih.gov/mesh/download_mesh.html)**: A biomedical topic vocabulary used for literature indexing, useful for evidence search, medical knowledge graphs, research discovery, and retrieval-augmented analytics.
- **[DRG groupers](https://www.cms.gov/medicare/payment/prospective-payment-systems/acute-inpatient-pps/ms-drg-classifications-and-software)**: Hospital episode grouping systems that summarize inpatient stays by clinical complexity and payment category, useful for reimbursement, case-mix, service-line, and capacity analysis.
- **[NCIt](https://evs.nci.nih.gov/ftp1/NCI_Thesaurus/)**: A cancer and biomedical ontology that helps oncology, genomics, and clinical research teams standardize diseases, drugs, anatomy, biomarkers, and trial concepts.
- **[OMOP/Athena](https://athena.ohdsi.org/)**: A common data model and vocabulary hub that helps organizations standardize claims, EHR, registry, and public data so analytics can be reused across sources.
- **[RxNorm](https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html)**: A normalized U.S. medication vocabulary that helps pharmacy, clinical, and claims teams reconcile drug names, ingredients, strengths, and dispense records.
- **[SNOMED CT](https://www.nlm.nih.gov/healthit/snomedct/)**: A broad clinical terminology for diagnoses, findings, procedures, and body structures, useful for harmonizing EHR data and building clinically meaningful cohorts.
- **[UMLS](https://www.nlm.nih.gov/research/umls/)**: A large biomedical terminology crosswalk that helps data and AI teams connect different medical vocabularies, synonyms, abbreviations, and text-mining outputs.

</details>

<details>
<summary><strong>&#x1F3E5; CMS / Medicare</strong> <sub>11 datasets</sub></summary>

Medicare, quality, payment, enrollment, and federal provider datasets.

- **[CMS Care Compare](https://data.cms.gov/provider-data/)**: Public CMS quality and performance data for hospitals, nursing homes, home health, hospice, and other providers, useful for provider selection, benchmarking, and network strategy.
- **[Open Payments](https://openpaymentsdata.cms.gov/)**: Public records of industry payments to physicians and teaching hospitals, useful for compliance reviews, conflict-of-interest checks, market mapping, and provider relationship analysis.
- **[POS File](https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/provider-of-services-file)**: A national file of Medicare-certified facilities and provider attributes, useful as a facility master list for market sizing, geographic access, and provider network analytics.
- **[HCAHPS](https://www.cms.gov/medicare/quality/initiatives/hospital-quality-initiative/hcahps-patients-perspectives-care-survey)**: Hospital patient-experience survey results that help business and quality teams compare communication, responsiveness, discharge experience, and overall satisfaction across facilities.
- **[MEPS](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files.jsp)**: A national survey of healthcare use, insurance, spending, and conditions, useful for estimating cost burden, affordability, utilization patterns, and population-level demand.
- **[MA enrollment/landscape](https://www.cms.gov/data-research/statistics-trends-and-reports/medicareadvantagepartdenrollment)**: Medicare Advantage plan and enrollment files that help payers, brokers, providers, and investors understand plan availability, market share, and county-level competition.
- **[MBSF](https://resdac.org/cms-data/files/mbsf-base)**: Medicare beneficiary demographics, enrollment, and chronic-condition context that helps define cohorts, adjust risk, and understand eligibility over time.
- **[DE-SynPUF](https://www.cms.gov/data-research/statistics-trends-and-reports/medicare-claims-synthetic-public-use-files)**: Synthetic Medicare-like claims data that lets engineering and analytics teams test pipelines, demos, and models without handling real patient information.
- **[HCRIS](https://www.cms.gov/data-research/statistics-trends-and-reports/cost-reports)**: Hospital and institutional cost-report data that helps finance, strategy, and operations teams study margins, costs, capacity, and provider financial performance.
- **[Medicare FFS Claims](https://resdac.org/cms-data/request/cms-data-request-center)**: Detailed Medicare fee-for-service claims used to follow patient care, cost, utilization, outcomes, and provider patterns over time for approved research and analytics.
- **[Medicare Provider Utilization](https://data.cms.gov/provider-summary-by-type-of-service)**: Public Medicare provider utilization and payment summaries that help teams benchmark services, procedure volumes, prescribing, payment levels, and provider market activity.

</details>

<details>
<summary><strong>&#x1F91D; Medicaid</strong> <sub>1 datasets</sub></summary>

Medicaid and CHIP files for access, cost, eligibility, and utilization analysis.

- **[TAF / T-MSIS](https://www.medicaid.gov/medicaid/data-systems/macbis/transformed-medicaid-statistical-information-system-t-msis/index.html)**: National Medicaid and CHIP eligibility, encounter, and claims-style files that help study access, cost, utilization, equity, and state program performance.

</details>

<details>
<summary><strong>&#x1F4CA; CDC Surveillance & Public Health</strong> <sub>16 datasets</sub></summary>

Public health surveillance, surveys, registries, and vital statistics.

- **[BRFSS](https://www.cdc.gov/brfss/data_documentation/index.htm)**: A large adult health behavior survey that helps public health and strategy teams understand smoking, obesity, prevention, chronic disease risks, and state-level population trends.
- **[WONDER](https://wonder.cdc.gov/)**: A public query system for mortality, births, disease, and other public health data, useful for quick population benchmarks, outcomes research, and local trend checks.
- **[FluView](https://www.cdc.gov/fluview/)**: CDC influenza surveillance and hospitalization data that helps teams monitor flu seasons, forecast respiratory demand, and plan staffing, outreach, and capacity.
- **[NHANES](https://www.cdc.gov/nchs/nhanes/index.htm)**: A national survey with interviews, exams, labs, and diet measures, useful for biomarker-rich population health, risk calibration, nutrition, and chronic disease analytics.
- **[NHIS](https://www.cdc.gov/nchs/nhis/documentation/index.html)**: A household health interview survey that helps teams understand insurance, access, disability, health status, and care use across the U.S. population.
- **[NHSN](https://www.cdc.gov/nhsn/)**: Healthcare-associated infection and facility safety surveillance data that helps quality, infection prevention, and reporting teams monitor safety outcomes and compliance.
- **[NNDSS](https://www.cdc.gov/nndss/)**: National notifiable disease surveillance outputs that help public health teams track infectious and reportable disease trends, outbreaks, and geographic risk patterns.
- **[NPCR](https://www.cdc.gov/national-program-cancer-registries/index.html)**: Cancer registry data that complements SEER and helps surveillance, policy, and oncology teams understand cancer incidence and outcomes across more of the U.S.
- **[NSDUH](https://www.samhsa.gov/data/data-we-collect/nsduh-national-survey-drug-use-and-health)**: A national survey on substance use and mental health that helps policy, behavioral health, and market teams estimate need, risk, and service demand.
- **[NVSS](https://www.cdc.gov/nchs/nvss/index.htm)**: Birth and death statistics that help analysts measure mortality, natality, life expectancy, cause-specific death trends, and community health outcomes.
- **[PLACES](https://www.cdc.gov/places/)**: Small-area CDC estimates of chronic disease, prevention, and health behaviors that help planners target interventions at county, city, tract, or ZIP-like levels.
- **[PRAMS](https://www.cdc.gov/prams/php/data-research/index.html)**: Maternal survey data linked to birth context that helps public health teams study pregnancy experiences, maternal risk factors, infant health, and perinatal programs.
- **[SEER](https://seer.cancer.gov/data/)**: Cancer incidence and survival registry data that helps oncology, public health, and life sciences teams study cancer burden, outcomes, and disparities.
- **[VAERS](https://vaers.hhs.gov/data.html)**: Spontaneous vaccine adverse event reports that help safety teams look for early warning signals while remembering reports do not prove causation.
- **[WISQARS](https://wisqars.cdc.gov/)**: CDC injury and violence statistics that help public health, safety, and policy teams measure injury burden, mortality, and prevention priorities.
- **[YRBSS](https://www.cdc.gov/yrbs/)**: Youth risk behavior survey data that helps schools, public health agencies, and policy teams understand adolescent behaviors, safety, mental health, and prevention needs.

</details>

<details>
<summary><strong>&#x1F3E8; HCUP</strong> <sub>4 datasets</sub></summary>

Encounter-level inpatient, emergency, and ambulatory surgery research assets.

- **[HCUP KID](https://hcup-us.ahrq.gov/kidoverview.jsp)**: A national pediatric inpatient sample that helps hospitals, researchers, and planners estimate children's hospital use, outcomes, charges, and service-line needs.
- **[HCUP NIS](https://hcup-us.ahrq.gov/nisoverview.jsp)**: A national inpatient hospital discharge sample that helps estimate U.S. hospitalization volume, outcomes, charges, diagnoses, procedures, and burden of disease.
- **[HCUP NEDS](https://hcup-us.ahrq.gov/nedsoverview.jsp)**: A national emergency department sample that helps teams understand ED demand, treat-and-release visits, admissions from the ED, charges, and utilization patterns.
- **[HCUP SID/SASD](https://hcup-us.ahrq.gov/db/state/siddbdocumentation.jsp)**: State inpatient and ambulatory surgery encounter data that helps analysts study local utilization, outcomes, access, and market patterns when state-level detail matters.

</details>

<details>
<summary><strong>&#x1F4B3; Claims, Cost & Transparency</strong> <sub>7 datasets</sub></summary>

Commercial claims, APCDs, price transparency, and state encounter files.

- **[CA HCAI](https://hcai.ca.gov/data/data-resources/)**: California healthcare facility, encounter, finance, workforce, and related data that helps teams study state-specific utilization, access, outcomes, capacity, and costs.
- **[HCCI](https://healthcostinstitute.org/data)**: Commercial claims data and benchmarks that help employers, payers, researchers, and policy teams understand spending, prices, utilization, and privately insured populations.
- **[Hospital Price Transparency](https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency)**: Hospital-posted machine-readable price files that help revenue, contracting, consumer, and market teams analyze charges, negotiated rates, and price variation.
- **[NY SPARCS](https://www.health.ny.gov/statistics/sparcs/access/)**: New York hospital, emergency department, and ambulatory surgery data that helps teams study state utilization, quality, charges, and local market dynamics.
- **[State APCDs](https://www.apcdcouncil.org/)**: State all-payer claims databases that help teams understand regional spending, utilization, payer mix, and access across commercial and public coverage where available.
- **[TX THCIC](https://www.dshs.texas.gov/center-health-statistics/texas-health-care-information-collection)**: Texas public use healthcare encounter files that help teams analyze hospital and outpatient utilization, charges, outcomes, and regional patterns across the state.
- **[TiC MRFs](https://www.cms.gov/priorities/healthplan-price-transparency)**: Payer-published negotiated-rate files that help price transparency, contracting, and market intelligence teams study commercial rates, provider networks, and reimbursement variation.

</details>

<details>
<summary><strong>&#x1F9D1;&#x200D;&#x2695;&#xFE0F; Provider Data</strong> <sub>6 datasets</sub></summary>

Provider directories, taxonomy files, quality measures, and relationship data.

- **[Doctors & Clinicians](https://data.cms.gov/provider-data/topics/doctors-clinicians)**: CMS clinician and group practice quality data that helps provider organizations, payers, and consumers compare clinicians, specialties, performance, and network options.
- **[Provider Data Catalog](https://data.cms.gov/provider-data/)**: The CMS provider data hub that helps teams find official facility, clinician, quality, and reporting datasets for provider benchmarking and market analysis.
- **[DocGraph](https://careset.com/docgraph-open-social-doctor-data/)**: Provider relationship and referral-pattern data that helps network, sales, and population health teams understand clinical communities and patient flow proxies.
- **[NPDB PUF](https://www.npdb.hrsa.gov/resources/publicData.jsp)**: Public malpractice and adverse action summaries that help credentialing, risk, workforce, and policy teams study provider safety and professional accountability trends.
- **[NPPES](https://download.cms.gov/nppes/NPI_Files.html)**: The national NPI registry for clinicians and organizations, useful as core provider master data for directories, claims, networks, and enrichment.
- **[NUCC Taxonomy](https://taxonomy.nucc.org/)**: Provider specialty and taxonomy codes that help teams classify clinicians and organizations consistently across directories, claims, credentialing, and network analytics.

</details>

<details>
<summary><strong>&#x1F3D8;&#xFE0F; SDOH & Environment</strong> <sub>13 datasets</sub></summary>

Social, economic, environmental, housing, workforce, and place-based context.

- **[AHRQ SDOH](https://www.ahrq.gov/sdoh/data-analytics/sdoh-data.html)**: A compiled set of county and ZIP-level social determinants that helps teams add community context to risk, access, equity, and outcomes analytics.
- **[ADI](https://www.neighborhoodatlas.medicine.wisc.edu/)**: A neighborhood disadvantage score that helps health systems, payers, and researchers account for socioeconomic context in risk adjustment and equity programs.
- **[AHRF](https://data.hrsa.gov/data/download)**: County-level health workforce, facility, population, and resource data that helps planners assess provider supply, access gaps, and community capacity.
- **[LAUS](https://www.bls.gov/lau/)**: Local unemployment and labor force measures that help teams connect economic conditions to health access, coverage, demand, and community risk.
- **[SVI](https://www.atsdr.cdc.gov/place-health/php/svi/)**: A social vulnerability index that helps emergency response, public health, and healthcare teams identify communities likely to need more support.
- **[CHR&R](https://www.countyhealthrankings.org/health-data)**: County health outcomes and factor rankings that help community health, policy, and strategy teams compare places and prioritize interventions.
- **[Dartmouth Atlas](https://data.dartmouthatlas.org/)**: Regional healthcare variation measures that help teams study differences in practice patterns, resource use, spending, and care intensity across markets.
- **[EPA AQS](https://www.epa.gov/aqs)**: Air quality monitor data that helps teams connect pollution and environmental exposure patterns to respiratory, cardiovascular, and community health risk.
- **[EJScreen](https://www.epa.gov/ejscreen)**: Environmental justice screening data that helps organizations identify communities facing combined environmental, demographic, and socioeconomic burdens.
- **[Walkability Index](https://www.epa.gov/smartgrowth/smart-location-mapping)**: Built-environment walkability scores that help planners and health teams study transportation access, activity-friendly communities, and neighborhood context.
- **[HUD PIT/HMIS](https://www.huduser.gov/portal/datasets/ahar.html)**: Homelessness counts and housing inventory summaries that help community health, policy, and social care teams understand housing instability and service needs.
- **[USDA Food Atlas](https://www.ers.usda.gov/data-products/food-access-research-atlas/)**: Food access and food environment measures that help teams study nutrition access, food deserts, retail context, and community health risks.
- **[RUCA](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/)**: Rural-urban commuting classifications that help teams segment markets, access patterns, provider supply, and outcomes by rurality and commuting context.

</details>

<details>
<summary><strong>&#x1F5FA;&#xFE0F; Census & Demographic</strong> <sub>5 datasets</sub></summary>

Population, insurance, poverty, commuting, and denominator datasets.

- **[ACS](https://www.census.gov/programs-surveys/acs/data.html)**: The default U.S. demographic and socioeconomic context source, useful for market sizing, equity analytics, community profiles, and denominator estimates.
- **[Decennial Census](https://www.census.gov/programs-surveys/decennial-census/data.html)**: The once-a-decade population and housing baseline that helps teams build small-area denominators, geography profiles, and long-term demographic comparisons.
- **[LEHD](https://lehd.ces.census.gov/data/)**: Employment and commuting flow data that helps analysts understand labor markets, daytime populations, access, mobility, and employer-area context.
- **[SAHIE](https://www.census.gov/programs-surveys/sahie.html)**: County and state health insurance coverage estimates that help teams study uninsured rates, coverage gaps, access strategy, and policy impact.
- **[SAIPE](https://www.census.gov/programs-surveys/saipe.html)**: Small-area poverty and income estimates that help public health, education, and policy teams target resources and understand economic need.

</details>

<details>
<summary><strong>&#x1F52C; Clinical / Research / ICU</strong> <sub>10 datasets</sub></summary>

Credentialed EHR, ICU, cohort, trial, and multimodal research datasets.

- **[All of Us](https://www.researchallofus.org/)**: A diverse U.S. research cohort with EHR, surveys, measurements, wearables, and genomics that helps study precision medicine and health equity.
- **[ClinicalTrials.gov](https://clinicaltrials.gov/data-api)**: A public registry of clinical studies and results that helps life sciences, research, and strategy teams monitor evidence, trial activity, and competitors.
- **[dbGaP](https://www.ncbi.nlm.nih.gov/gap/)**: Controlled-access genotype and phenotype studies that help approved researchers connect genetic variation to disease, traits, biomarkers, and outcomes.
- **[eICU-CRD](https://physionet.org/content/eicu-crd/2.0/)**: A multi-center ICU dataset that helps validate critical care models beyond one hospital and study practice variation, mortality, and resource use.
- **[MIMIC-CXR](https://physionet.org/content/mimic-cxr/)**: A large de-identified chest X-ray and report dataset that helps teams build and test medical imaging and vision-language models.
- **[MIMIC-III](https://physionet.org/content/mimiciii/)**: A classic ICU research dataset that helps teams benchmark critical care analytics, mortality prediction, length-of-stay modeling, and retrospective methods.
- **[MIMIC-IV](https://physionet.org/content/mimiciv/)**: A modern de-identified hospital and ICU dataset that helps teams prototype clinical prediction, operational analytics, and OMOP-style EHR pipelines.
- **[PhysioNet](https://physionet.org/)**: A catalog of clinical, waveform, imaging, and signal datasets that helps researchers find benchmark data for healthcare AI and physiology analytics.
- **[SEER-Medicare](https://healthcaredelivery.cancer.gov/seermedicare/obtain/)**: Linked cancer registry and Medicare claims data that helps oncology teams study treatment paths, outcomes, utilization, survivorship, and cost of cancer care.
- **[UK Biobank](https://www.ukbiobank.ac.uk/use-our-data/apply-for-access/)**: A large U.K. cohort with health, imaging, lifestyle, and genetic data that helps study long-term disease risk and multimodal prediction.

</details>

<details>
<summary><strong>&#x1F48A; Drug & Pharmacology</strong> <sub>7 datasets</sub></summary>

Drug labels, approvals, adverse events, compounds, side effects, and safety data.

- **[ChEMBL](https://www.ebi.ac.uk/chembl/downloads/)**: A public bioactivity and compound database that helps drug discovery teams study targets, assays, compounds, and mechanism-aware modeling.
- **[DailyMed](https://dailymed.nlm.nih.gov/dailymed/spl-resources-all-drug-labels.cfm)**: Structured FDA drug labels that help teams extract indications, warnings, contraindications, dosage, labeling history, and regulatory text features.
- **[DrugBank](https://go.drugbank.com/)**: A curated drug knowledge base that helps research, product, and AI teams connect drugs to targets, pathways, indications, interactions, and mechanisms.
- **[FAERS](https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers/fda-adverse-event-reporting-system-faers-public-dashboard)**: FDA adverse drug event reports that help safety teams detect potential signals, monitor product issues, and enrich pharmacovigilance workflows.
- **[Orange/Purple Book](https://www.fda.gov/drugs/drug-approvals-and-databases/approved-drug-products-therapeutic-equivalence-evaluations-orange-book)**: FDA approval, therapeutic equivalence, biologic, patent, and exclusivity information that helps market access, formulary, and product lifecycle teams.
- **[openFDA](https://open.fda.gov/)**: Open FDA APIs and downloads that help teams quickly access regulatory, recall, label, adverse event, and enforcement data for lightweight analytics.
- **[SIDER](http://sideeffects.embl.de/)**: A side-effect knowledge resource that helps teams prototype drug safety knowledge graphs, adverse event matching, and medication risk features.

</details>

<details>
<summary><strong>&#x1F5BC;&#xFE0F; Imaging</strong> <sub>5 datasets</sub></summary>

Radiology, dermatology, cancer imaging, and benchmark medical image collections.

- **[ADNI](https://adni.loni.usc.edu/data-samples/)**: Longitudinal Alzheimer's imaging, biomarker, clinical, and genetics data that helps teams study disease progression and multimodal prediction.
- **[CheXpert](https://aimi.stanford.edu/datasets/chexpert-chest-x-rays)**: A large chest radiograph dataset with labels that helps teams benchmark medical imaging classification, uncertainty handling, and radiology AI workflows.
- **[ISIC](https://www.isic-archive.com/)**: A public skin image archive that helps dermatology and AI teams build, test, and compare skin lesion classification models.
- **[ChestX-ray14](https://nihcc.app.box.com/v/ChestXray-NIHCC)**: A public chest X-ray benchmark that helps teams prototype computer vision models for thoracic disease detection and transfer learning.
- **[TCIA](https://www.cancerimagingarchive.net/collections/)**: Cancer imaging collections that help oncology, radiology, and AI teams study imaging biomarkers, segmentation, treatment response, and multimodal research.

</details>

<details>
<summary><strong>&#x1F9EC; Genomics / Phenotype</strong> <sub>3 datasets</sub></summary>

Variant, phenotype, ontology, and association resources for genetics workflows.

- **[ClinVar-OMIM-gnomAD](https://www.ncbi.nlm.nih.gov/clinvar/)**: Variant, disease, and population frequency resources that help genetics teams interpret variants, connect genes to phenotypes, and assess population context.
- **[HPO](https://hpo.jax.org/app/download/ontology)**: A standard vocabulary for clinical features that helps rare disease, genomics, and AI teams describe phenotypes consistently.
- **[GWAS Catalog](https://www.ebi.ac.uk/gwas/downloads)**: Curated genome-wide association results that help teams find trait-linked variants, build genetic evidence features, and explore polygenic risk signals.

</details>

<details>
<summary><strong>&#x1F310; International / Global Health</strong> <sub>4 datasets</sub></summary>

Global and country-comparable health indicators, burden, and system measures.

- **[Eurostat Health](https://ec.europa.eu/eurostat/web/health/database)**: European health indicator data that helps policy, market, and public health teams compare countries and regions across health status, care, and systems.
- **[GBD + DHS](https://www.healthdata.org/research-analysis/gbd)**: Global disease burden estimates and demographic health surveys that help teams compare risks, outcomes, coverage, and population health across countries.
- **[OECD Health Statistics](https://www.oecd.org/en/data/datasets/oecd-health-statistics.html)**: Comparable health system, spending, workforce, and outcome indicators that help strategy and policy teams benchmark OECD and partner countries.
- **[WHO GHO](https://www.who.int/data/gho)**: WHO country-level health indicators that help teams monitor global disease burden, risk factors, system capacity, and public health progress.

</details>

## What Makes This Maintainable

- **Machine-readable entries**: every dataset is YAML validated against `schemas/dataset.schema.json`.
- **Use-case-first navigation**: `use-cases/` pages shortlist datasets for real ML workflows.
- **Access-tier + PHI filters**: prototype-now sources are separated from DUA/IRB assets.
- **OMOP/PCORnet mapping status**: each entry records CDM fit and ETL notes.
- **Crosswalks and notebooks**: vocabulary/geography joins and starter analyses are first-class content.
- **Freshness signals**: scripts can flag stale `last_validated` dates and broken links.

## Dataset Index

Total entries: **108**.

<a id="terminologies"></a>

<details>
<summary><strong>&#x1F524; Terminologies & Vocabularies</strong> <sub>16 datasets</sub></summary>

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

</details>

<a id="cms-medicare"></a>

<details>
<summary><strong>&#x1F3E5; CMS / Medicare</strong> <sub>11 datasets</sub></summary>

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

</details>

<a id="medicaid"></a>

<details>
<summary><strong>&#x1F91D; Medicaid</strong> <sub>1 datasets</sub></summary>

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [TAF / T-MSIS](https://www.medicaid.gov/medicaid/data-systems/macbis/transformed-medicaid-statistical-information-system-t-msis/index.html)<br><sub>[yaml](datasets/medicaid/tmsis-analytic-files.yaml)</sub> | `dua` | restricted | beneficiary eligibility, enrollment, claim, encounter, and service-line files | custom-claims-etl | reference | 2026-05-17 |

</details>

<a id="cdc-surveillance"></a>

<details>
<summary><strong>&#x1F4CA; CDC Surveillance & Public Health</strong> <sub>16 datasets</sub></summary>

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

</details>

<a id="hcup"></a>

<details>
<summary><strong>&#x1F3E8; HCUP</strong> <sub>4 datasets</sub></summary>

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [HCUP KID](https://hcup-us.ahrq.gov/kidoverview.jsp)<br><sub>[yaml](datasets/hcup/hcup-kid.yaml)</sub> | `purchase` | deidentified-governed | weighted hospital discharge or encounter record | custom-encounter-etl | seed | 2026-05-17 |
| [HCUP NIS](https://hcup-us.ahrq.gov/nisoverview.jsp)<br><sub>[yaml](datasets/hcup/hcup-nis.yaml)</sub> | `purchase` | deidentified-governed | discharge-level inpatient record with survey design variables and weights | custom-discharge-etl | reference | 2026-05-17 |
| [HCUP NEDS](https://hcup-us.ahrq.gov/nedsoverview.jsp)<br><sub>[yaml](datasets/hcup/hcup-neds.yaml)</sub> | `purchase` | deidentified-governed | weighted hospital discharge or encounter record | custom-encounter-etl | seed | 2026-05-17 |
| [HCUP SID/SASD](https://hcup-us.ahrq.gov/db/state/siddbdocumentation.jsp)<br><sub>[yaml](datasets/hcup/hcup-sid-sasd.yaml)</sub> | `purchase` | deidentified-governed | weighted hospital discharge or encounter record | custom-encounter-etl | seed | 2026-05-17 |

</details>

<a id="claims-commercial"></a>

<details>
<summary><strong>&#x1F4B3; Claims, Cost & Transparency</strong> <sub>7 datasets</sub></summary>

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [CA HCAI](https://hcai.ca.gov/data/data-resources/)<br><sub>[yaml](datasets/claims-commercial/ca-hcai.yaml)</sub> | `mixed` | none-to-restricted | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | seed | 2026-05-17 |
| [HCCI](https://healthcostinstitute.org/data)<br><sub>[yaml](datasets/claims-commercial/hcci-commercial-claims.yaml)</sub> | `dua` | none-to-restricted | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | seed | 2026-05-17 |
| [Hospital Price Transparency](https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency)<br><sub>[yaml](datasets/claims-commercial/hospital-price-transparency-mrfs.yaml)</sub> | `open` | none-to-restricted | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | seed | 2026-05-17 |
| [NY SPARCS](https://www.health.ny.gov/statistics/sparcs/access/)<br><sub>[yaml](datasets/claims-commercial/ny-sparcs.yaml)</sub> | `mixed` | none-to-restricted | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | seed | 2026-05-17 |
| [State APCDs](https://www.apcdcouncil.org/)<br><sub>[yaml](datasets/claims-commercial/state-apcds.yaml)</sub> | `mixed` | mixed-public-aggregate-to-restricted-microdata | member, enrollment month, claim, claim-line, provider, or aggregate depending state and access tier | custom-state-claims-etl | reference | 2026-05-17 |
| [TX THCIC](https://www.dshs.texas.gov/center-health-statistics/texas-health-care-information-collection)<br><sub>[yaml](datasets/claims-commercial/tx-thcic.yaml)</sub> | `mixed` | none-to-restricted | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | seed | 2026-05-17 |
| [TiC MRFs](https://www.cms.gov/priorities/healthplan-price-transparency)<br><sub>[yaml](datasets/claims-commercial/transparency-in-coverage-mrfs.yaml)</sub> | `open` | none-to-restricted | claim-line, negotiated-rate, encounter, plan, provider, or aggregate depending product | custom-claims-etl | seed | 2026-05-17 |

</details>

<a id="provider"></a>

<details>
<summary><strong>&#x1F9D1;&#x200D;&#x2695;&#xFE0F; Provider Data</strong> <sub>6 datasets</sub></summary>

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [Doctors & Clinicians](https://data.cms.gov/provider-data/topics/doctors-clinicians)<br><sub>[yaml](datasets/provider/cms-doctors-clinicians.yaml)</sub> | `open` | none-provider-public | provider, facility, taxonomy, or provider-pair edge | provider-dimension-enrichment | seed | 2026-05-17 |
| [Provider Data Catalog](https://data.cms.gov/provider-data/)<br><sub>[yaml](datasets/provider/cms-provider-data-catalog.yaml)</sub> | `open` | none-provider-public | provider, facility, taxonomy, or provider-pair edge | provider-dimension-enrichment | seed | 2026-05-17 |
| [DocGraph](https://careset.com/docgraph-open-social-doctor-data/)<br><sub>[yaml](datasets/provider/docgraph-referral-graph.yaml)</sub> | `open` | none-provider-public | provider, facility, taxonomy, or provider-pair edge | provider-dimension-enrichment | seed | 2026-05-17 |
| [NPDB PUF](https://www.npdb.hrsa.gov/resources/publicData.jsp)<br><sub>[yaml](datasets/provider/npdb-public-use-file.yaml)</sub> | `open` | none-provider-public | provider, facility, taxonomy, or provider-pair edge | provider-dimension-enrichment | seed | 2026-05-17 |
| [NPPES](https://download.cms.gov/nppes/NPI_Files.html)<br><sub>[yaml](datasets/provider/nppes-npi-registry.yaml)</sub> | `open` | none-provider-public | one record per NPI plus taxonomy, address, endpoint, and status fields | provider-dimension-enrichment | reference | 2026-05-17 |
| [NUCC Taxonomy](https://taxonomy.nucc.org/)<br><sub>[yaml](datasets/provider/nucc-provider-taxonomy.yaml)</sub> | `open` | none-provider-public | provider, facility, taxonomy, or provider-pair edge | provider-dimension-enrichment | seed | 2026-05-17 |

</details>

<a id="sdoh"></a>

<details>
<summary><strong>&#x1F3D8;&#xFE0F; SDOH & Environment</strong> <sub>13 datasets</sub></summary>

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

</details>

<a id="census"></a>

<details>
<summary><strong>&#x1F5FA;&#xFE0F; Census & Demographic</strong> <sub>5 datasets</sub></summary>

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [ACS](https://www.census.gov/programs-surveys/acs/data.html)<br><sub>[yaml](datasets/census/acs-1yr-5yr.yaml)</sub> | `open` | none-aggregate-geography | geography-indicator-year estimate | geospatial-context-enrichment | seed | 2026-05-17 |
| [Decennial Census](https://www.census.gov/programs-surveys/decennial-census/data.html)<br><sub>[yaml](datasets/census/decennial-census.yaml)</sub> | `open` | none-aggregate-geography | geography-indicator-year estimate | geospatial-context-enrichment | seed | 2026-05-17 |
| [LEHD](https://lehd.ces.census.gov/data/)<br><sub>[yaml](datasets/census/lehd-onthemap.yaml)</sub> | `open` | none-aggregate-geography | geography-indicator-year estimate | geospatial-context-enrichment | seed | 2026-05-17 |
| [SAHIE](https://www.census.gov/programs-surveys/sahie.html)<br><sub>[yaml](datasets/census/sahie.yaml)</sub> | `open` | none-aggregate-geography | geography-indicator-year estimate | geospatial-context-enrichment | seed | 2026-05-17 |
| [SAIPE](https://www.census.gov/programs-surveys/saipe.html)<br><sub>[yaml](datasets/census/saipe.yaml)</sub> | `open` | none-aggregate-geography | geography-indicator-year estimate | geospatial-context-enrichment | seed | 2026-05-17 |

</details>

<a id="clinical-research"></a>

<details>
<summary><strong>&#x1F52C; Clinical / Research / ICU</strong> <sub>10 datasets</sub></summary>

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

</details>

<a id="drug-pharma"></a>

<details>
<summary><strong>&#x1F48A; Drug & Pharmacology</strong> <sub>7 datasets</sub></summary>

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [ChEMBL](https://www.ebi.ac.uk/chembl/downloads/)<br><sub>[yaml](datasets/drug-pharma/chembl.yaml)</sub> | `open` | none-public-regulatory-or-knowledgebase | drug product, label, adverse-event report, compound, target, or safety concept | drug-vocabulary-or-knowledge-enrichment | seed | 2026-05-17 |
| [DailyMed](https://dailymed.nlm.nih.gov/dailymed/spl-resources-all-drug-labels.cfm)<br><sub>[yaml](datasets/drug-pharma/dailymed.yaml)</sub> | `open` | none-public-regulatory-or-knowledgebase | drug product, label, adverse-event report, compound, target, or safety concept | drug-vocabulary-or-knowledge-enrichment | seed | 2026-05-17 |
| [DrugBank](https://go.drugbank.com/)<br><sub>[yaml](datasets/drug-pharma/drugbank.yaml)</sub> | `purchase` | none-public-regulatory-or-knowledgebase | drug product, label, adverse-event report, compound, target, or safety concept | drug-vocabulary-or-knowledge-enrichment | seed | 2026-05-17 |
| [FAERS](https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers/fda-adverse-event-reporting-system-faers-public-dashboard)<br><sub>[yaml](datasets/drug-pharma/faers.yaml)</sub> | `open` | none-public-regulatory-or-knowledgebase | case/report tables across demographic, drug, reaction, indication, outcome, and therapy components | custom-pharmacovigilance-etl | reference | 2026-05-17 |
| [Orange/Purple Book](https://www.fda.gov/drugs/drug-approvals-and-databases/approved-drug-products-therapeutic-equivalence-evaluations-orange-book)<br><sub>[yaml](datasets/drug-pharma/orange-purple-book.yaml)</sub> | `open` | none-public-regulatory-or-knowledgebase | drug product, label, adverse-event report, compound, target, or safety concept | drug-vocabulary-or-knowledge-enrichment | seed | 2026-05-17 |
| [openFDA](https://open.fda.gov/)<br><sub>[yaml](datasets/drug-pharma/openfda.yaml)</sub> | `open` | none-public-regulatory-or-knowledgebase | endpoint-specific JSON record or bulk download document | knowledge-enrichment | reference | 2026-05-17 |
| [SIDER](http://sideeffects.embl.de/)<br><sub>[yaml](datasets/drug-pharma/sider.yaml)</sub> | `open` | none-public-regulatory-or-knowledgebase | drug product, label, adverse-event report, compound, target, or safety concept | drug-vocabulary-or-knowledge-enrichment | seed | 2026-05-17 |

</details>

<a id="imaging"></a>

<details>
<summary><strong>&#x1F5BC;&#xFE0F; Imaging</strong> <sub>5 datasets</sub></summary>

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [ADNI](https://adni.loni.usc.edu/data-samples/)<br><sub>[yaml](datasets/imaging/adni.yaml)</sub> | `registration` | deidentified-or-governed | image, study, series, DICOM object, report, participant, or collection | custom-imaging-extension | seed | 2026-05-17 |
| [CheXpert](https://aimi.stanford.edu/datasets/chexpert-chest-x-rays)<br><sub>[yaml](datasets/imaging/chexpert.yaml)</sub> | `registration` | deidentified-or-governed | image, study, series, DICOM object, report, participant, or collection | custom-imaging-extension | seed | 2026-05-17 |
| [ISIC](https://www.isic-archive.com/)<br><sub>[yaml](datasets/imaging/isic-archive.yaml)</sub> | `open` | deidentified-or-governed | image, study, series, DICOM object, report, participant, or collection | custom-imaging-extension | seed | 2026-05-17 |
| [ChestX-ray14](https://nihcc.app.box.com/v/ChestXray-NIHCC)<br><sub>[yaml](datasets/imaging/nih-chestxray14.yaml)</sub> | `open` | deidentified-or-governed | image, study, series, DICOM object, report, participant, or collection | custom-imaging-extension | seed | 2026-05-17 |
| [TCIA](https://www.cancerimagingarchive.net/collections/)<br><sub>[yaml](datasets/imaging/tcia.yaml)</sub> | `open` | deidentified-or-governed | image, study, series, DICOM object, report, participant, or collection | custom-imaging-extension | seed | 2026-05-17 |

</details>

<a id="genomics"></a>

<details>
<summary><strong>&#x1F9EC; Genomics / Phenotype</strong> <sub>3 datasets</sub></summary>

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [ClinVar-OMIM-gnomAD](https://www.ncbi.nlm.nih.gov/clinvar/)<br><sub>[yaml](datasets/genomics/clinvar-omim-gnomad.yaml)</sub> | `mixed` | none-public-aggregate-or-controlled-if-individual-level | variant, gene, phenotype, association, or ontology concept | custom-genomics-extension | seed | 2026-05-17 |
| [HPO](https://hpo.jax.org/app/download/ontology)<br><sub>[yaml](datasets/genomics/human-phenotype-ontology.yaml)</sub> | `open` | none-public-aggregate-or-controlled-if-individual-level | variant, gene, phenotype, association, or ontology concept | custom-genomics-extension | seed | 2026-05-17 |
| [GWAS Catalog](https://www.ebi.ac.uk/gwas/downloads)<br><sub>[yaml](datasets/genomics/gwas-catalog.yaml)</sub> | `open` | none-public-aggregate-or-controlled-if-individual-level | variant, gene, phenotype, association, or ontology concept | custom-genomics-extension | seed | 2026-05-17 |

</details>

<a id="international"></a>

<details>
<summary><strong>&#x1F310; International / Global Health</strong> <sub>4 datasets</sub></summary>

| Dataset | Tier | PHI posture | Grain | OMOP/CDM status | Curation | Last validated |
|---|---:|---|---|---|---|---|
| [Eurostat Health](https://ec.europa.eu/eurostat/web/health/database)<br><sub>[yaml](datasets/international/eurostat-health.yaml)</sub> | `open` | none-aggregate-or-deidentified-survey | country, region, indicator, survey respondent, household, or modeled estimate | not-primary-omop-source | seed | 2026-05-17 |
| [GBD + DHS](https://www.healthdata.org/research-analysis/gbd)<br><sub>[yaml](datasets/international/ihme-gbd-dhs.yaml)</sub> | `mixed` | none-aggregate-or-deidentified-survey | country, region, indicator, survey respondent, household, or modeled estimate | not-primary-omop-source | seed | 2026-05-17 |
| [OECD Health Statistics](https://www.oecd.org/en/data/datasets/oecd-health-statistics.html)<br><sub>[yaml](datasets/international/oecd-health-statistics.yaml)</sub> | `open` | none-aggregate-or-deidentified-survey | country, region, indicator, survey respondent, household, or modeled estimate | not-primary-omop-source | seed | 2026-05-17 |
| [WHO GHO](https://www.who.int/data/gho)<br><sub>[yaml](datasets/international/who-global-health-observatory.yaml)</sub> | `open` | none-aggregate-or-deidentified-survey | country, region, indicator, survey respondent, household, or modeled estimate | not-primary-omop-source | seed | 2026-05-17 |

</details>

## Contributing

Open a PR with a schema-valid YAML file under the right `datasets/<category>/` directory. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Repository metadata/docs are intended to be CC-BY-4.0; code is intended to be MIT. This repository does **not** grant rights to redistribute third-party data files.
