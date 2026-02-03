# Integrating Multi-Modal Medical Data Into Unified Patient Journeys
Integrating Multi-Modal Medical Data Into Unified Patient Journeys

<https://www.johnsnowlabs.com/watch-webinar-integrating-multi-modal-medical-data-into-unified-patient-journeys/>

<https://youtu.be/VKuW6n25VdM>

This summary details the speech presented in the source, which introduces the John Snow Labs (JSL) platform for integrating multimodal medical data into unified patient journeys using specialized Large Language Models (LLMs) and the OMOP Common Data Model. The presentation was led by David Albby, CTO at John Snow Labs.

I. Platform Goals and Vision

The primary goal of the platform is to transition from analyzing single documents (like a pathology or radiology report) to looking at a patient's entire history (over five to ten years), including multiple hospital visits, claims, prescriptions, and lab reports.

Key Capabilities Expected:

• Natural Language Question Answering: The system must be able to load all documents about a patient (via upload or API) and answer questions in natural language. Questions range from simple (e.g., "what is the age of the patient?") to complex (e.g., "does the patient fit clinical trial inclusion criteria?").

• Accuracy and Explanations: Answers must be accurate and include references to specific documents and roles in the patient story. Users must be able to link back and check where an answer came from within a long document.

• Medical Reasoning: The system must possess common sense reasoning and basic medical reasoning. For instance, it should be able to infer age from a birthday or understand that a specific drug maps to an antibiotic class using NDC or RxNorm codes.

• Handling Real-World Data Complexity: The system is designed to handle "garbage in"-raw, dirty, unstructured data that is often not normalized, inconsistent, uncertain, and sometimes conflicting (e.g., conflicting lab results or contradictory drug records).

II\. Enterprise-Grade Requirements and Architecture

The platform is designed as an Enterprise-grade system for real-world deployment, handling millions of patients and billions of documents.

Enterprise Requirements:

• Privacy and Security (PHI/Air-Gap): The platform is designed to work with Protected Health Information (PHI) within an air-gap environment. It is deployed on the organization's infrastructure, within the security perimeter, and does not send data to JSL, cloud providers, or any external LLM APIs.

• Scalability: It must work at scale, handling organizations that serve 10 to 30 million patients per year, resulting in potentially billions of data points or pages. The use of long-context LLMs alone is considered "completely meaningless" at this scale.

• Consistency and Accuracy: Results must be consistent (asking the same question twice yields the same answer) and exhibit high accuracy, leveraging JSL's specialized Healthcare-specific LLMs.

• Open Standard: JSL chose to adopt the OMOP Common Data Model for the final data store. This is a relational data model supported by an open ecosystem of tools, allowing users to run SQL queries, use dashboards (Tableau, PowerBI), or build predictive models in Python. JSL extended the OMOP model to include necessary features like traceability and confidence levels.

III\. Processing Multimodal and Dirty Data

Real patient journeys are "very messy" due to multiple providers, non-standard interactions (like patients reporting past symptoms in text), and the sheer volume of data (a typical cancer patient generates over a thousand pages of text per year).

Supported Modalities:

The system unifies data from four key modalities:

1\. Structured Data (EHR): Three hospitalizations might appear as three rows in the EHR.

2\. Unstructured Notes: Discharge notes, progress notes, and Radiology reports provide much richer information, often containing details missing from structured data (e.g., pain levels, family history, social determinants, unrecorded medications taken before admission, diet, smoking, and alcohol use).

3\. Semi-Structured Data (FHIR): Used to capture events outside the primary EHR, such as an out-of-state hospitalization captured via a Health Information Exchange (HIE) integration.

4\. Risk Scores: Once unified, the data is used to calculate various patient risk scores and prospective risk scores (e.g., readmission risk) on an ongoing, hourly or daily basis.

The Data Processing Pipeline (Junk In, OMOP Out):

The incoming "junk data" is processed through several specialized LLM components:

1\. Information Extraction: The first set of medical LLMs extracts entities from free text in PDFs, FHIR messages, or free text fields within tabular data. JSL models extract more than 400 types of entities (e.g., medications, anatomical parts, negated diagnoses). This includes Assertion Status (determining if an entity is present, negated, or related to a family member) and Relation Extraction (e.g., distinguishing between a patient's breast cancer and a family history of breast cancer).

2\. Terminology Resolution: Terms extracted from unstructured data, or codes from FHIR/tabular data, are resolved to standard codes like SNOMED and 12 other terminologies, ensuring consistency across different code sets (e.g., Flow codes, RxNorm, NDC).

3\. Date Normalization: Temporal aspects are crucial. The system normalizes relative dates (e.g., "last year") into exact dates (e.g., July 1st, 2023, if the note is from July 1st, 2024), enabling precise timeline queries for clinical matching (e.g., finding patients diagnosed within the last 18 months).

4\. Data Merge and Deduplication: After extraction, the data is often "a whole lot of junk" due to repetition (e.g., 30-40 progress notes for a 3-day stay). JSL applies Healthcare-specific logic to deduplicate, merge data (e.g., keeping the most specific diagnosis, or averaging multiple blood pressure measurements), and carry uncertainty forward.

5\. OMOP Knowledge Graph: The merged, normalized, and validated data is stored in a relational database based on the OMOP Common Data Model, forming a patient knowledge graph.

IV\. Natural Language Querying and Accuracy

The platform enables advanced querying for individual patients and cohort building, providing answers that are significantly more accurate due to the combined data modalities.

LLM Benchmarks (Clinical Text Summarization)

JSL conducted a blind, randomized evaluation by practicing medical doctors comparing JSL Medical LLMs against the latest GPT-4 model on three tasks (summarization, information extraction, and medical Q&A).

• On clinical text summarization, JSL models "significantly outperform GPT-4", winning almost at a 2 to 1 ratio on dimensions like factuality (not hallucinating) and clinical relevancy (summarizing the most critical results).

Text-to-SQL Agent

Querying the large OMOP relational database is complex. JSL uses an AI agent instead of simple text-to-SQL models, addressing critical issues:

1\. Accuracy: Traditional models struggle with the complex, multi-page SQL statements required for healthcare queries (e.g., joining diagnosis, clinical events, and terminology tables).

2\. Consistency: JSL ensures consistent responses, which is vital for credibility in a clinical setting.

3\. Speed/Optimization: The agent is trained to use optimized queries leveraging indices and materialized views, preventing system crashes when users ask broad questions (e.g., SELECT \* from a 300 million-row table).

The agent follows a multi-step process:

• Tool 1 (RAG): Maps the user query to pre-built, optimized queries JSL knows how to run efficiently.

• Tool 2 (Terminology Service): Maps clinical terms (e.g., hypertension, antibiotics) to specific codes (SNOMED, NDC) required for the query.

• Tool 3 (Schema Adjustment): Adjusts the schema and SQL based on the user's slightly different query.

• Final Execution: Runs the adjusted query and post-processes results.

Explainability and Business Logic

A crucial feature is explaining the business logic behind the results. When building patient cohorts (e.g., "Find patients with hypertension and diabetes"), different people within an organization (billing, clinical, research) may have vastly different definitions of what counts as "diabetes" (e.g., having an ICD-10 code vs. taking insulin vs. having two abnormal H1C tests).

The system must show the user the SQL and the business logic (what criteria were counted as defining the condition). This interaction allows users to change their definitions, acknowledging that in healthcare, "the details matter".

V. Deployment and Licensing

The JSL system is available across various platforms (on-premise, AWS, Azure, Databricks, Snowflake, Oracle). Licensing is usually by server, not by user, patient, or modality, encouraging organizations to open access to all data types and users. The implementation includes a 12-week project to install the system within the user's infrastructure, integrate data sources (S3 folders, Epic/Clarity, DICOM images, FHIR API), and customize terminology mappings and query optimization.