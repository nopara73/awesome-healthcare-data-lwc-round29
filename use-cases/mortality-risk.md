# Mortality risk

Use this page as a dataset acquisition and feature-source shortlist. Start with open and synthetic resources for pipeline development, then graduate to DUA/IRB assets once the cohort, target, validation plan, and security posture are stable.

| Dataset | Tier | Why it matters | OMOP/CDM status | PHI posture |
|---|---:|---|---|---|
| [MIMIC-IV](https://physionet.org/content/mimiciv/) | `registration` | person, admission, ICU stay, procedure, diagnosis, lab, medication, chart-event, and note/module records depending access | well-supported | deidentified-credentialed |
| [MIMIC-III](https://physionet.org/content/mimiciii/) | `registration` | participant, encounter, stay, event, waveform, image, or study record | supported-for-some-sources | credentialed-deidentified-or-controlled |
| [eICU-CRD](https://physionet.org/content/eicu-crd/2.0/) | `registration` | ICU patient/unit-stay/event tables across multiple hospitals | custom-critical-care-etl | deidentified-credentialed |
| [NHANES](https://www.cdc.gov/nchs/nhanes/index.htm) | `open` | person-level component files keyed by SEQN across two-year survey cycles | custom-survey-etl | public-use-deidentified-or-aggregate |
| [NVSS](https://www.cdc.gov/nchs/nvss/index.htm) | `open` | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | public-use-deidentified-or-aggregate |
| [SEER](https://seer.cancer.gov/data/) | `registration` | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | public-use-deidentified-or-aggregate |
| [SEER-Medicare](https://healthcaredelivery.cancer.gov/seermedicare/obtain/) | `dua` | tumor/case registry records linked to beneficiary enrollment and Medicare claims | custom-registry-plus-claims-etl | restricted-linked-registry-claims |
| [ADNI](https://adni.loni.usc.edu/data-samples/) | `registration` | image, study, series, DICOM object, report, participant, or collection | custom-imaging-extension | deidentified-or-governed |


## Starter modeling notes

- Define the cohort, time-zero, prediction window, and outcome before selecting predictors.
- Preserve source-code era, geography vintage, and release version in every feature table.
- Keep leakage checks close to the use case: future claims, post-outcome labs, and target-derived facility measures are common healthcare ML traps.
- Validate on at least one source with a different population, site, payer, or geography when feasible.
