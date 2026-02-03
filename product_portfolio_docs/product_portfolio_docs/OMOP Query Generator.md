**OMOP Query Generator**

**Overview**

John Snow Labs’ **OMOP Query Generator** is an intelligent natural language
interface that translates clinical questions and cohort criteria into
**executable SQL queries for OMOP Common Data Model (CDM)** databases. It
enables healthcare informatics and real-world evidence (RWE) teams to query
multimodal patient data using plain English, without manual SQL coding. The
platform leverages healthcare-tuned NLP and **medical LLMs** to ensure that
complex inclusion/exclusion criteria and temporal logic are accurately
converted into **OMOP-compliant SQL** , yielding governed and explainable
results. Built for enterprise needs, the OMOP Query Generator operates
securely within a organization’s environment and provides a compliance-first
solution for patient cohort discovery and data exploration. It bridges the gap
between clinical intent and database queries – empowering analysts and
clinicians to retrieve insights from EHR and claims data **with precision,
auditability, and speed**.

**Use Cases**

  * **Clinical Trial Cohort Definition:** Automatically convert protocol inclusion/exclusion criteria into SQL filters to find eligible patients for clinical trials. For example, a user can ask for “patients who had a heart attack in the last 6 months and are not on beta blockers” and retrieve the corresponding cohort from an OMOP CDM warehouse. This streamlines trial feasibility analysis by quickly identifying candidates who meet complex, multi-condition criteria.
  * **Real-World Evidence & Outcomes Research:** Enable epidemiologists and outcomes researchers to pose questions about large patient populations in natural language. Queries like “What drugs are prescribed after an atrial fibrillation diagnosis?” can be answered by mapping the question to standard concepts and executing optimized SQL on observational data. The tool handles **temporal queries** (e.g. drug exposure after diagnosis within a time window) and yields reproducible results for RWE studies.
  * **Population Health and Quality Improvement:** Allow care management teams to segment high-risk or non-compliant patients using free-text prompts. For instance, population health managers can ask, “Which diabetic patients over age 65 have not had an annual eye exam?” and get a cohort list without writing code. This supports proactive care gap analysis and quality measure reporting by making **dashboard-ready cohort queries** accessible to non-technical users.
  * **Integrated Unstructured Data Queries:** Combine structured and unstructured data in cohort building. The OMOP Query Generator works with John Snow Labs’ NLP stack to incorporate findings from clinical notes, pathology reports, or radiology text. Users can query conditions or events that are documented only in text (e.g. “patients with **smoking history** mentioned in their notes and a diagnosis of COPD”), because the system can **extract and normalize those facts** into OMOP concepts before generating the query. This facilitates comprehensive patient queries spanning EHR tables and narrative clinical documentation.

**Key Features & Capabilities**

  * **Natural Language to OMOP SQL Conversion:** Translates plain-language questions and eligibility criteria into **valid SQL** targeting the OMOP schema. The system understands clinical phrasing and maps it to the proper tables, joins, and filters in the OMOP CDM (e.g., conditions, procedures, drug exposures). By parsing complex sentence structures and medical context, it produces **production-ready SQL** so users don’t need to know table names or syntax.
  * **Complex Temporal Logic & Nested Queries:** Supports advanced cohort definitions with **time-based conditions and nested logic**. For example, it can handle queries like “find patients who had Diagnosis A **within 90 days after** Procedure B and **before** Medication C was started,” which require subqueries and date comparisons. The Query Generator intelligently constructs these temporal constraints and nested WHERE clauses, ensuring the logic is correctly represented in SQL. This capability allows sophisticated patient timeline queries that traditionally demand specialized SQL skills.
  * **Terminology Integration & Concept Mapping:** The tool is tightly integrated with John Snow Labs’ **Medical Terminology Server** to map clinical terms and colloquialisms to standard codes. Free-text inputs like _“heart attack”_ or _“high blood sugar”_ are automatically resolved to standardized concepts (e.g., SNOMED CT or OMOP concept IDs for myocardial infarction or diabetes). The Terminology Server uses string matching and embeddings to find the relevant SNOMED, RxNorm, LOINC, ICD, or OMOP codes – even handling synonyms and common misspellings. This ensures the generated SQL is semantically precise, using **OMOP Standard Concepts** (and checking concept validity) for compliance with data standards.
  * **Governed, Validated Query Generation:** The OMOP Query Generator emphasizes **governance and accuracy** in query creation. It uses a library of validated SQL query templates and an agent-like approach to plan complex queries. Rather than free-form code generation, the system selects and assembles SQL patterns that are known to be correct for the given intent. This yields **traceable, consistent queries** that can be trusted to produce the right results. Every generated query can be reviewed by data engineers or analysts, and a **human-in-the-loop workflow** is supported for validation: users can inspect the suggested SQL, see which medical concepts were chosen, and adjust any criteria if needed before execution. This approach provides transparency and keeps humans in control of critical cohort definitions.
  * **Explainability & Auditability:** The platform provides robust explainability for each query and its results. It not only generates SQL but also **explains the reasoning** – for instance, highlighting that _“heart attack”_ was mapped to SNOMED code 22298006 (Myocardial Infarction) and that _“last 6 months”_ was interpreted as a date range in the condition occurrence date field. Each answer or cohort output includes **provenance and a rationale** , so users see which data sources and logic contributed to the result. The system can provide a chain-of-thought or rule trace for how it constructed the query, enhancing trust and auditability. This means analysts can audit the criteria and regulators can get a clear record of how a cohort was defined – a critical need in clinical research compliance.
  * **Integration with Clinical NLP & LLMs:** The OMOP Query Generator is part of John Snow Labs’ broader healthcare AI stack, integrating **Spark NLP for Healthcare** and domain-specific LLMs. Prior to query generation, unstructured text can be processed to extract over **400 types of medical entities** (e.g., problems, medications, lab results, procedures). These extracted facts are normalized (e.g., linking “high blood sugar” in a note to a glucose lab concept) and stored in structured form, often in the OMOP CDM itself or an associated knowledge graph. The Query Generator’s LLM component is **fine-tuned on clinical data** and works in concert with these pipelines – it understands clinical language nuances and uses the context of extracted information. For example, an embedded reasoning model can deduplicate and infer patient facts (resolving that “MI” means myocardial infarction) before formulating the SQL query. This integration allows the tool to handle **rich clinical narratives** and complex questions by combining NLP-derived insights with the structured OMOP data.
  * **GenAI Lab & Workflow Integration:** As part of John Snow Labs’ ecosystem, the Query Generator integrates with the **Generative AI Lab** , a no-code platform for designing and deploying AI workflows. Users can interact with the OMOP Query Generator through a conversational UI or a visual interface in GenAI Lab – for example, typing a cohort query in natural language and reviewing the generated SQL and results in the Lab’s dashboard. This provides a user-friendly, governed environment to experiment with queries and perform human-in-the-loop corrections. Additionally, the tool’s outputs can feed directly into **BI and analytics tools** : the SQL produced is compatible with any OMOP-compliant data warehouse, so it can be used to power dashboards or reports in tools like Tableau, PowerBI, or Databricks SQL. By integrating with existing data workflows, the Query Generator delivers **dashboard-ready outputs** , accelerating the path from question to insight.

**Performance & Benchmarks**

John Snow Labs’ OMOP Query Generator has demonstrated **state-of-the-art
performance** on both accuracy and efficiency metrics, outshining general-
purpose solutions in this domain. In a 2024 peer-reviewed study, the
underlying text-to-SQL model achieved **85% logical form accuracy** on a
challenging clinical SQL dataset (MIMICSQL) – **significantly outperforming**
prior models and even GPT-3.5 and GPT-4 on the same task. This high accuracy
reflects the benefit of domain-specific fine-tuning and the system’s use of
validated query patterns. In blind evaluations with clinicians, the Query
Generator’s answers to medical questions were more accurate and consistent
than those from a general AI assistant, highlighting its **domain tuning and
reliability**. Importantly, the system maintains consistency across repeated
runs – the same query will yield the same results every time, a critical
requirement in clinical analytics (where reproducibility is a must).

Performance at scale is another key strength. The Query Generator is
**optimized for large healthcare datasets** , capable of querying **millions
of patient records and billions of clinical events with sub-second response
times**. It achieves this through a combination of **SQL optimization and
intelligent caching** : frequently used query patterns (e.g. common cohort
definitions) can be cached or materialized, and the system’s agent breaks down
complex questions into efficient sub-queries. Unlike naive text-to-SQL
approaches that might generate slow, ad-hoc SQL, John Snow Labs’ solution uses
**pre-built query templates and schema-specific optimizations** to avoid
performance pitfalls. For instance, it can automatically include indexes or
use table partition filters in the generated SQL to speed up execution on
large OMOP tables. The result is enterprise-grade query performance – even
intricate temporal queries run quickly, enabling interactive data exploration
over huge electronic health record datasets.

In benchmarks against open-source alternatives and general AI coders, the OMOP
Query Generator stands out for its **traceability and clinical accuracy**.
General code assistants often miss context or produce syntactically correct
but semantically wrong SQL, especially on healthcare data. In contrast, John
Snow Labs’ tool is **purpose-built for healthcare** : it was _“significantly
better than GPT-4”_ in complex medical question answering and information
extraction tasks in testing, thanks to its specialized training. It also
provides explanations for each query step, which means errors can be caught
and corrected more easily – a big advantage over black-box AI solutions. This
focus on **accuracy, speed, and accountability** gives healthcare
organizations confidence to use the Query Generator in mission-critical
scenarios, knowing it can handle the scale and complexity of real-world
clinical data.

**Deployment & Compliance**

The OMOP Query Generator is designed for **flexible deployment in high-
compliance environments**. It can be deployed on-premises or in a private
cloud, ensuring that **sensitive patient data never leaves the organization’s
secure perimeter**. All NLP and LLM processing runs locally – there are _no
external API calls_ to third-party services – which allows the solution to
meet stringent privacy requirements (HIPAA, GDPR and other data protection
laws). For cloud deployments, it supports major platforms and configurations:
for example, it can run on **AWS, Azure, or GCP** in the customer’s VPC, and
it’s compatible with platforms like Databricks, Snowflake, Oracle, and other
infrastructures where OMOP data may reside. This broad support means the Query
Generator can be integrated into existing data ecosystems without requiring a
specific database technology – it works with any OMOP CDM SQL database
(PostgreSQL, SQL Server, etc.) or via Spark for big data setups.

Enterprise IT teams can deploy the solution as a set of **containerized
microservices** , orchestrated via Kubernetes for scalability and high
availability. Each component (NLP extraction, terminology service, LLM query
planner, etc.) can scale independently and be assigned GPU or CPU resources as
needed. This modular architecture not only aids performance, but also
simplifies validation and updates – for instance, the medical LLM models and
terminology databases are updated regularly (with bi-weekly model releases)
and can be upgraded without disrupting other components. John Snow Labs offers
a **universal license model** that unlocks all these components (Healthcare
NLP library, Medical LLMs, Reasoning models, Terminology Server) under one
agreement, simplifying procurement and compliance review.

From a compliance perspective, the OMOP Query Generator was built with
**governance and auditability in mind**. Every query executed can be logged
and traced, creating an audit trail of who queried what criteria – crucial for
research oversight and data governance. The system’s use of standard
terminologies and concept validity checks ensures that only proper, up-to-date
medical codes are used in queries, reducing the risk of errors due to outdated
or local codes. Additionally, the **human-in-the-loop validation** capability
means organizations can enforce review of queries that meet certain risk
criteria (for example, a privacy officer could review queries that involve
sensitive cohorts). The platform also supports role-based access control: only
authorized users can run queries or see certain data fields, aligning with the
principle of least privilege.

By aligning with the OMOP CDM (a widely adopted data standard) and integrating
with terminology services, the Query Generator inherently promotes
**interoperability and consistency**. Cohort definitions created on one OMOP
dataset can be ported to another, since the SQL uses standard schemas and
vocabularies. This is valuable for multi-site studies or federated research
networks. In summary, the deployment model and compliance features of JSL’s
OMOP Query Generator make it suitable for regulated healthcare settings – it’s
**enterprise-ready, secure, and compliant by design**.

**Real-World Use Cases**

John Snow Labs’ OMOP Query Generator is already being used in real-world
healthcare projects to accelerate data analysis and cohort building:

  * **Large Health System (VA Pilot):** In collaboration with the U.S. Department of Veterans Affairs, John Snow Labs deployed a pilot system to enable natural language questions on a massive EHR dataset (9+ million veterans). This system integrated document understanding, reasoning LLMs, and the OMOP Query interface. Clinicians could ask questions like “Has this patient ever been on an SSRI before?” and get an immediate, explainable answer drawn from structured and unstructured records. The pilot demonstrated that out-of-the-box LLMs were not accurate enough on clinical notes, but with JSL’s domain-specific models and preprocessing (summarization of notes, terminology mapping), the accuracy improved significantly. This real-world example shows the Query Generator’s ability to handle **noisy, longitudinal patient data** at scale, turning disparate VA records into a unified timeline and Q&A system for clinicians.
  * **Oncology Research & Patient Journeys:** A global oncology center used the Query Generator as part of building **longitudinal patient timelines** for cancer patients. The solution extracted facts from pathology reports, radiology notes, and clinical narratives (e.g. tumor mutations, staging, treatments) and loaded them into an OMOP CDM. Researchers then used natural language queries to find cohorts – for example, asking “patients with HER2-positive breast cancer who progressed after Trastuzumab therapy” would automatically translate to the appropriate criteria on diagnoses, genomic results, and drug exposures. This enabled complex cohort discovery across multi-year, multi-encounter oncology data in minutes instead of weeks. The system’s explainability was crucial: oncologists could see exactly which criteria were applied and adjust them (ensuring, for instance, that **“progression”** was defined consistently). This use case highlights how the tool supports **real-world clinical research** by unifying structured and unstructured data into queryable form.
  * **Population Health Platform (ClosedLoop Integration):** John Snow Labs’ generative AI capabilities have been integrated into the ClosedLoop platform (a healthcare AI company) to power **text-prompted cohort retrieval**. Population health analysts can type free-text queries – e.g. “Which patients are in the top 5% risk for hospitalization and have uncontrolled Stage 3+ chronic kidney disease?” – and the system returns the list of patients matching those conditions. Under the hood, the Query Generator interprets the clinical terms (finding the CKD stage, identifying “risk for hospitalization” from predictive models, etc.) and produces the SQL that fetches those patients from the OMOP data. This deployment has **enabled non-technical clinicians to directly interact with data** and get risk-based cohorts, improving how care managers target interventions. It’s a strong validation of the tool’s usability outside of JSL: an existing healthcare platform was able to plug in the Query Generator to deliver new functionality to its users.
  * **Pharmaceutical RWE & Clinical Data Readiness:** Several leading pharmaceutical companies and contract research organizations are leveraging the OMOP Query Generator to expedite real-world evidence studies and clinical trial data preparation. For example, in a drug safety study, a team used the tool to identify all patients across a network of hospitals who had a certain drug exposure followed by a specific adverse event diagnosis within one year. What previously required crafting a complex SQL by hand (and iterative tweaking) was accomplished by a single English query and a few validation checks. The result was a validated cohort of patients for analysis, produced in a fraction of the time. Because the system provides **traceable output** , the researchers could include the exact query logic in their study documentation for regulatory submission, with confidence that it was generated using standard definitions. This **traceability and speed** improve real-world data pipelines – from data ingestion to final analysis, the Query Generator helps ensure reproducibility and clarity in how study cohorts are defined.

**Customer Proof Points**

John Snow Labs’ OMOP Query Generator has garnered positive validation from
industry use and evaluations:

  * **Outperforming General AI Solutions:** In internal evaluations, John Snow Labs’ healthcare-specific query agent showed **significant accuracy gains over general LLMs like GPT-4**. In fact, blind assessments by practicing physicians found that the Query Generator’s answers and SQL outputs for medical questions were more accurate and consistent than those produced by GPT-4 or other general models. This domain-focused approach provides tangible value to customers – one hospital CIO noted that having an **explainable, specialist AI** for clinical queries increased their clinicians’ trust compared to using a generic AI assistant.
  * **Peer-Reviewed Accuracy Leadership:** The methodology behind the Query Generator is published in the _Journal of Artificial Intelligence in Health_ (2024), where it achieved state-of-the-art results on medical text-to-SQL tasks. The paper reports the model **“achieves logical form accuracy of 0.85 on the MIMICSQL dataset, significantly outperforming”** models like Defog-SQL, Codex (GPT-3.5), and even GPT-4. This independent validation gives enterprise customers confidence that the solution is not only novel but rigorously benchmarked. It set a new standard for healthcare SQL generation, showing that JSL’s smaller specialized models can beat larger general models when properly tuned to the clinical domain.
  * **Industry Demonstrations and Adoption:** The OMOP Query Generator’s capabilities have been showcased at major industry forums. At **HIMSS 2025** , John Snow Labs (with partners Databricks and AWS) demonstrated how the system _“excels in complex queries”_ on multimodal clinical data and is _“ideal for organizations seeking OMOP data enrichment.”_ This drew significant interest from healthcare IT leaders, and since then over a dozen healthcare organizations – including top pharmaceutical companies, academic medical centers, and digital health platforms – have begun piloting or deploying the solution. Early adopters report that the tool has **dramatically reduced the time** to define patient cohorts (from weeks to hours) and improved collaboration between clinical experts and data teams. The fact that the Query Generator produces explainable, standardized queries was cited as a key advantage, as it allowed stakeholders (clinicians, data engineers, compliance officers) to all review and agree on cohort definitions in a transparent way. Customers also appreciate that the solution operates _within their secure environment_ and supports regulatory compliance, which has been a hurdle for using other AI coding tools in healthcare.

By combining cutting-edge NLP technology with a deep understanding of
healthcare data standards, John Snow Labs’ OMOP Query Generator has proven its
value in real-world settings. It provides an accurate, efficient, and
**clinically-aligned** solution for turning natural language questions into
the actionable SQL queries needed for patient cohort discovery and data
analysis, all while maintaining the governance and trust that enterprise
healthcare demands.

**Relevant Resources**

  * **Presentation:**[OMOP CDM - Patient Journey JSL- April 2025.pptx](https://johnsnowlabs-my.sharepoint.com/:p:/p/david/EWbtqDmZXRFMv7xyXugUJS8B-7aqoAKsAcS6d-hfcRR0yw?e=sRjlbl)
  * **Product Page:**
  * **Peer-Reviewed Paper:**
  * **Blog Link:**
  * **Webinar:**[Answering-patient-level-questions-from-raw-clinical-data](https://www.nlpsummit.org/answering-patient-level-questions-from-raw-clinical-data)

