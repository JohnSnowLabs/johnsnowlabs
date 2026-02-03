## Turning Straw into Gold: Building Patient Journeys from Raw Medical Data

> An end-to-end approach to transform messy multimodal healthcare data into a unified, queryable patient journey using healthcare-specific LLMs and the OMOP data model.

### Overview
This document summarizes a talk on applying generative AI to healthcare data integration. The goal is to convert raw, unnormalized, and uncertain multimodal medical data into a consistent, trustworthy, and scalable representation of each patient over time, enabling natural-language queries for both individual patients and large cohorts.

### Core Goals
- **Unified patient journey**: Build a longitudinal view over months and years, integrating structured, semi-structured, and unstructured data.
- **Natural-language queries**: Ask questions about single patients or cohorts; receive answers with **citations to sources**.
- **Consistency and trust**: The same query returns the same result, with traceable provenance.
- **Production-grade system**: Secure, accurate, scalable, and operable on commodity infrastructure.
- **Open standards**: Map all data to the **OMOP** relational data model for interoperability with dashboards, notebooks, and ML workloads.

### Data Ingestion (The “Straw”)
- **Accept raw data as-is**: No pre-processing required; data may be incomplete, uncertain, or inconsistent.
- **Multimodal sources**: EHR/claims (structured), FHIR/HL7/CSVs (semi-structured), PDFs/text/discharge notes/radiology reports (unstructured).
- **Continuously updating**: System must accommodate ongoing changes and additions to records.

### End-to-End Automated Pipeline
1. **Information extraction (IE)**
   - Extract entities, context (e.g., negation, family history), and relations (e.g., temporal ordering, dosage, laterality).
2. **Semantic modeling & terminology mapping**
   - Normalize clinical concepts to standard codes; handle **relative time** (e.g., “two weeks ago” in June → normalized date for a September query).
3. **Data modeling (OMOP)**
   - Represent the patient journey in a relational model (OMOP) for scalability and operational simplicity.
4. **Deduplication & merging (reasoning)**
   - Resolve conflicts and duplicates with effect-specific logic:
     - Prefer more specific concepts (e.g., “knee pain” over “pain”).
     - Aggregate numeric measurements (e.g., average multiple weights on the same day).
     - Prefer dispensed pharmacy claims over prescribed drug when they differ.
5. **Clinical inference generation**
   - Compute scores and measures (e.g., readmission risk, sepsis risk, kidney disease progression, population health metrics) to enrich the record.

### Why OMOP (Relational) over a Knowledge Graph?
- **Scale**: Efficient indexing, views, sharding, and backups at the scale of tens of millions of patients and billions of facts.
- **Operations**: Familiar to enterprise DevOps/SecOps; easier to run consistently in production.
- **Ecosystem**: Rich open-source tooling and a global community.

### Multimodal Integration Adds Clinical Value
- **Richer timelines**: Unstructured notes and radiology add years of history beyond EHR-only data; FHIR messages may reveal care at external sites.
- **More complete diagnoses**: Text-derived NLP often surfaces additional conditions (e.g., arthritis, dyspnea) missing from structured data.
- **Preventive care visibility**: Screenings and preventative actions often appear only in free text or FHIR labs, not in structured EHR fields.

### Cohort Queries and Terminology Groupings
- **Natural-language cohorts**: Example—“patients diagnosed with back pain who had spinal fusion.”
- **Terminology expansion**: Abstract intents (e.g., “back pain,” “spinal fusion”) translate to sets of codes across vocabularies.
- **Temporal constraints**: Support queries constrained to before/after events (e.g., drugs prescribed after AF diagnosis).

### Why General-Purpose LLMs Fall Short for Healthcare SQL
- **Accuracy**: Generated SQL can be complex and wrong or incomplete, leading to incorrect results.
- **Consistency**: Non-deterministic answers erode clinician trust.
- **Performance**: Queries must leverage indices/materialized views to return in seconds at enterprise scale.

### Healthcare-Specific LLMs
Purpose-built models are used for:
- **Semantic IE** over clinical text
- **Terminology mapping** and code normalization
- **Conflict resolution** and **reasoning** over multimodal facts
- **Text-to-query** optimized for the OMOP schema and database tuning
- **Clinical inference** generation (scores, risk, conditions)

### Example Patient Journey (Illustrative)
- EHR-only data shows three hospitalizations (2015, 2017, 2019).
- Adding discharge notes and radiology extends visibility back to 2011 with richer details.
- Adding FHIR reveals an additional hospitalization at an external site.
- The unified journey enables comprehensive summaries, preventative care reviews, and risk assessments.

### Production Requirements
- **Security/PHI**: Air-gapped, no random external API calls; designed to process PHI safely.
- **Operability**: Commodity infrastructure; standard monitoring, backups, patching, updates.
- **Consistency & traceability**: Deterministic results with sources cited.
- **Scale**: Millions of patients, billions of documents/facts.

### Key Takeaways
- **Integrate all modalities** to avoid blind spots in clinical decision-making.
- **Automate the pipeline** from raw data to a unified, normalized patient journey.
- **Use OMOP** as the open, scalable backbone for data access and analytics.
- **Rely on healthcare-specific LLMs** for accuracy, consistency, and performance.

### Call to Action
Interested in the approach or have experience tackling similar problems? Share feedback, compare solutions, and explore how to apply this pipeline to your data and use cases.


