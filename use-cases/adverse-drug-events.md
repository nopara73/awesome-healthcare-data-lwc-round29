# Adverse drug events

Use this page as a dataset acquisition and feature-source shortlist. Start with open and synthetic resources for pipeline development, then graduate to DUA/IRB assets once the cohort, target, validation plan, and security posture are stable.

| Dataset | Tier | Why it matters | OMOP/CDM status | PHI posture |
|---|---:|---|---|---|
| [FAERS](https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers/fda-adverse-event-reporting-system-faers-public-dashboard) | `open` | case/report tables across demographic, drug, reaction, indication, outcome, and therapy components | custom-pharmacovigilance-etl | none-public-regulatory-or-knowledgebase |
| [openFDA](https://open.fda.gov/) | `open` | endpoint-specific JSON record or bulk download document | knowledge-enrichment | none-public-regulatory-or-knowledgebase |
| [VAERS](https://vaers.hhs.gov/data.html) | `open` | respondent, report, certificate, facility, or aggregate public-health record | not-primary-omop-source | public-use-deidentified-or-aggregate |
| [DailyMed](https://dailymed.nlm.nih.gov/dailymed/spl-resources-all-drug-labels.cfm) | `open` | drug product, label, adverse-event report, compound, target, or safety concept | drug-vocabulary-or-knowledge-enrichment | none-public-regulatory-or-knowledgebase |
| [MedDRA](https://www.meddra.org/) | `purchase` | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | none |
| [RxNorm](https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html) | `open` | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | none |
| [NDC Directory](https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory) | `open` | concept-code, terminology relationship, or ontology release table | source-or-standard-vocabulary | none |


## Starter modeling notes

- Define the cohort, time-zero, prediction window, and outcome before selecting predictors.
- Preserve source-code era, geography vintage, and release version in every feature table.
- Keep leakage checks close to the use case: future claims, post-outcome labs, and target-derived facility measures are common healthcare ML traps.
- Validate on at least one source with a different population, site, payer, or geography when feasible.
