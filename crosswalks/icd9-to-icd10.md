# ICD-9-CM ↔ ICD-10-CM/PCS

**Primary official source:** CMS General Equivalence Mappings (GEMs).

Use this crosswalk for era-spanning claims and EHR cohorts, but treat mappings as approximate. Many mappings are one-to-many, many-to-one, or context-dependent. For ML, keep the original source code, mapped concept, mapping direction, and mapping confidence as separate fields.

Recommended pipeline:

1. Preserve original source code, date of service, and coding system.
2. Apply the correct GEM version for the cohort period.
3. Flag approximate, combination, and no-map cases.
4. Map both source and target codes into OMOP/Athena concepts where available.
5. Sensitivity-test models with and without cross-era mapped features.
