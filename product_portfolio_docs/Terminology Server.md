**Terminology Server**

### **Overview**

John Snow Labs’ **Terminology Server** is an enterprise-grade platform
for managing, searching, and distributing clinical terminologies, value
sets, and code mappings at scale. It functions as a centralized
**healthcare terminology service** that bridges disparate systems by
providing a versioned, always up-to-date suite of medical coding
standards and custom vocabularies.

**Designed for healthcare** data extraction and interoperability use
cases, it allows seamless integration into electronic health records
(EHRs), clinical data warehouses, and analytics platforms, ensuring that
all applications “speak the same language” using consistent codes and
mappings. Crucially, the platform can be deployed privately **behind
your firewall** or in your cloud, enabling healthcare organizations to
maintain full control over sensitive data and comply with strict privacy
regulations (e.g. HIPAA) while leveraging **standards-based
terminology** services.

**Supported Standards & Vocabularies:** **SNOMED CT**, **ICD-10-CM**,
**LOINC**, **RxNorm**, **CPT4**, **UMLS** (Unified Medical Language
System), **MeSH**, **MedDRA**, **ICDO, NDC, ATC, CPT4, CVX, HCPCS, HGNC,
HPO** and OMOP **Common Data Model** conventions. The Terminology Server
comes pre-loaded with the most widely used clinical coding systems and
can incorporate additional standards (e.g., CDISC terminologies for
clinical trials) as needed.

In summary, John Snow Labs’ Terminology Server provides healthcare and
life sciences teams with a **unified, high-performance terminology
infrastructure**. It enables **fast, accurate code lookup and
normalization** of clinical text, **context-aware mapping between coding
systems**, and easy management of custom code sets – all within a
secure, compliant environment. The result is significantly improved
interoperability across systems and datasets, reducing manual coding
effort and errors while powering downstream applications like clinical
decision support, population health analytics, and AI-driven insights.

### **Key Features & Capabilities**

**Comprehensive Vocabulary Library –** The Terminology Server comes
**pre-loaded with millions of medical concepts** from the latest
versions of standard coding systems, including **SNOMED CT**,
**ICD-10-CM**, **LOINC**, **RxNorm**, **CPT4**, **UMLS** (Unified
Medical Language System), **MeSH**, **MedDRA**, **ICDO, NDC, ATC, CPT4,
CVX, HCPCS, HGNC, HPO** and more. Updates to terminologies are provided
regularly, ensuring the platform stays current with evolving medical
knowledge and coding guidelines. Users can also **ingest and version
custom code systems** (e.g. internal catalogs or specialty-specific
codes) and manage them alongside standard vocabularies. Each terminology
is stored with its full hierarchy and metadata, enabling rich functions
like ancestor/descendant hierarchy views and concept details on click.

**Advanced Search & Concept Discovery –** A hallmark capability of JSL’s
Terminology Server is its **context-aware, intelligent search** for
medical concepts. It leverages a combination of **advanced string
matching, NLP embedding models, and ontological knowledge** to find the
most relevant codes for a given input.

**Flexible Search**

**Code Search (Code to Code mapping)** – Enables users to locate a
specific medical code within the Terminology Server’s curated set of
medical coding systems.  
<img src="/media/image2.png" style="width:6.5in;height:2.73958in" />

**Concept Search (Semantic & Exact match search) -** Enables users to
search for medical terms or concepts using a combination of exact text
matching and semantic search techniques to return similar or related
concepts, as described in the section below:

- **Semantic Search**: Go beyond exact keyword matches – the server
  understands clinical language nuances and can retrieve concepts by
  synonyms, acronyms, layperson terms, and even common misspellings. For
  example, a search for “heart attack” will return the SNOMED CT concept
  for myocardial infarction (along with related terms), even if the
  exact phrase doesn’t match. This LLM-powered search capability
  identifies concepts when no exact string match exists by applying
  synonym expansion and hierarchical reasoning.  
  <img src="/media/image3.png" style="width:6.25in;height:2.94792in" />

- **Boolean Search**: Used in the context of exact match search, Boolean
  search can be applied using AND or OR operators.

- **Context-Based Ranking**: The search algorithm takes into account the
  clinical context (if provided) to rank results. This means it can
  weight results differently if the user context is a diagnosis vs. a
  medication vs. a lab. It will find the most relevant concept given the
  clinical context, which is invaluable for picking the correct code
  among many. For instance, given “iron” in a lab context, it will
  prioritize an iron lab test LOINC code, whereas in a medication
  context, it might prioritize an iron supplement RxNorm code.  
    
  <img src="/media/image4.png" style="width:6.25in;height:2.97917in" />

**Spelling Correction**: The server automatically detects and corrects
spelling errors or abbreviations in user queries. A misspelled term like
“diabetes mallitus” will still yield the proper Diabetes Mellitus codes.
Users can choose to see results for the original string or the corrected
term, ensuring robustness to typos and variations in input.  
<img src="/media/image5.png" style="width:6.5in;height:1.875in" />

**ValueSet management.** A custom Value Set in the context of medical
terminology is a user-defined collection of medical codes and terms
selected from one or more standard coding systems (such as SNOMED CT,
ICD-10, LOINC, RxNorm, etc.), created to meet a specific need, use case,
or organizational requirement  
John Snow Labs’ Terminology Server supports the use of custom Value
Sets, offering the following capabilities:

- Upload custom Value Sets created externally in Excel or CSV format
  using the built-in Upload feature.

- View, create new versions, delete

- Filter search results based on the codes included in a selected Value
  Set.

<img src="/media/image6.png" style="width:6.16667in;height:2.92521in" />

**Filters and Facets**: Users can interactively filter search results by
various attributes – for example, restricting to a particular code
system (only SNOMED CT), a clinical domain (only diagnoses, or only
medications), or OMOP standard concepts only. There are options to hide
inactive/deprecated codes (ensure “Valid Concepts Only”), and even
filter by a specific Value Set to see if a term falls within a defined
subset. These controls make it easy to narrow down results in a large
terminology.  
<img src="/media/image7.png" style="width:6.5in;height:1.84375in" />  
<img src="/media/image8.png" style="width:6.5in;height:3.0625in" />  
  
Optimize search precision based on context and confidence levels by
using **Term Weight** and **Scope**:

- Use higher term weights when you're confident in your terminology

- Use lower term weights when context is critical for disambiguation

- Adjust scope based on how much surrounding context affects meaning

- Combine with vocabulary filters for more precise results

<img src="/media/image.jpg" style="width:6.5in;height:1.96875in"
alt="A screenshot of a medical survey AI-generated content may be incorrect." />

**Batch & Bulk Queries**: The API supports batch queries for
high-throughput use cases – for instance, validating or mapping a list
of codes in one call. This batch transaction support enables efficient
processing of large datasets with minimal network overhead. It is
designed to handle millions of lookups (e.g., normalizing an entire
warehouse of clinical notes) with horizontal scalability and robust
performance.

**Concept Mapping & Cross-Code Set Links**

In addition to search, the Terminology Server can function as a
**mapping engine**, translating codes from one coding scheme to another.
It incorporates an extensive repository of **concept mappings and
relationships** – including official mappings (e.g., SNOMED CT to ICD-10
crosswalks, LOINC to SNOMED mappings) and augmented links via the UMLS
and OMOP vocabulary. This allows it to answer queries like “*map code X
from source terminology A to target terminology B*” via API or UI. For
example, the server knows how ICD-10 code **E11** (Type 2 Diabetes) maps
to the equivalent UMLS concept **C0011847** and to the corresponding
MedDRA term **10067585**. It can thus return all related codes across
vocabularies for a given concept, enabling **data translation across
systems**.

Furthermore, domain experts can **manage custom Concept Maps** –
defining organization-specific mappings or extensions – through the
Terminology Server’s interface. All mappings are version-controlled, and
the server can validate whether a mapping is up-to-date or if a target
code has been retired. This capability is critical for projects like
migrating legacy codes to modern standards, or integrating datasets that
use different code systems.

**Integration with Spark NLP & Healthcare AI Pipelines –** John Snow
Labs has tightly integrated the Terminology Server with its NLP and AI
ecosystem. The server’s APIs and data can be used directly within Spark
NLP’s pipelines for entity resolution and concept normalization tasks.
For instance, after named entity recognition identifies a medical
concept in text (e.g., a condition or drug mention), a Resolver model
can call the Terminology Server to link that mention to a standard code
(like a UMLS CUI or SNOMED CT ID). This integration powers use cases
such as mapping free-text to OMOP CDM concept IDs as part of an NLP
pipeline, or auto-annotating text with standard codes in the Generative
AI Lab annotation tool. The Terminology Server provides the “backbone”
terminology data (synonym lists, code embeddings, etc.) that these AI
models leverage for high-accuracy linking. Additionally, the server’s
results can be fed into downstream analytics or machine learning models,
ensuring that all data is normalized to the proper codes before analysis
(this greatly improves machine learning feature consistency and model
performance). In summary, the Terminology Server is not an isolated tool
– it’s built to plug into enterprise data science workflows, from data
ingestion and cleaning to model deployment

**User Interface & API Access**

While the Terminology Server offers rich APIs, it also includes a
user-friendly web interface for interactive use by analysts, clinicians,
and terminologists. The UI provides **advanced search** with real-time
filtering, a **hierarchical browser** to explore parent/child
relationships of codes, and dashboards for managing terminology
assets.  
Users can upload Value Sets through the UI , versioning it and
publishing it. They can be used later on to filter search results by
ValueSets.  
For example, a clinical informatics team can update a “Critical Lab
Tests” value set on their own when guidelines change, and the new
version is immediately available via the server’s API to all integrated
systems. Role-based access controls and audit logs are available to meet
governance requirements in large organizations.

In summary, the Terminology Server’s feature set is **comprehensive and
purpose-built for healthcare**: it combines a deep well of content
(standard and custom terminologies) with intelligent search and mapping
capabilities and seamless integration into both human workflows and
automated pipelines. This enables organizations to confidently rely on
it as the central hub for terminology management and concept
normalization.

### **Performance & Interoperability**

John Snow Labs’ Terminology Server is engineered for **high performance
and scalability**, capable of serving low-latency responses even under
heavy workloads and with extremely large vocabulary. The server has been
tested with **millions of concept entries** (the combined size of loaded
terminologies) and is optimized for sub-second query times in typical
deployments. Its architecture allows **horizontal scaling** to handle
high concurrency. For example, in an enterprise environment, the
Terminology Server can handle real-time code lookups or validations for
dozens of simultaneous EHR transactions without noticeable delay. Batch
operations (like normalizing an entire dataset) are performed
efficiently by leveraging distributed processing when available.
Additionally, the **embedding-based search** is accelerated with vector
indexing techniques, ensuring that semantic searches remain fast even as
new terms and embeddings are added.

**Interoperability** is at the core of the Terminology Server’s design.
It acts as a **translator between coding languages**, ensuring that
disparate systems – whether legacy or modern – can understand each
other’s data.

Terminology Server supports OMOP CDM conventions, which is crucial for
research networks harmonizing data in OMOP format. For example, it can
flag which codes in a result set are OMOP “Standard” concepts and ensure
that only standard concept IDs are used for analytics (a vital step in
OMOP-based pipelines). It can also be integrated with standards from HL7
v2 and CDA where relevant (e.g., providing mappings for HL7 v2 code
tables), and can host terminologies needed for CDISC clinical trial
submissions (such as those from NCI Thesaurus for study data).

Since a Terminology Server is used for mapping between terminologies or
linking entities to their corresponding terminology codes, if the
outputs of HL7 or FHIR datasets are reduced to the entity level, the
Terminology Server can be integrated at the output points of these
systems. The output of the Terminology Server can then be provided as
input to other subsystems, enabling faster and more detailed analyses,
supporting pattern detection, and serving purposes such as billing
systems.

From a compliance perspective, the Terminology Server ensures that all
terminology content is used in accordance with licensing and regulatory
requirements. John Snow Labs handles the updating and distribution of
standard code sets (e.g., annual ICD-10 updates, monthly RxNorm
releases), so customers are relieved from the burden of manually
updating codes. The platform logs terminology versions and can expose a
**Terminology Capabilities** statement that advertises exactly what
functions and code systems it supports, which aids integration testing
and documentation.

Lastly, **performance metrics** of the Terminology Server have been
benchmarked against alternative solutions and approaches. The server’s
**deterministic approach** (using curated datasets and algorithms)
yields consistent, **reproducible results** for code mapping queries,
unlike generative AI models, which can vary in output. This consistency
is critical for interoperability and auditing – the same input will
always return the same standardized code, enabling reliable data
exchange. In internal evaluations, JSL’s terminology mapping technology
delivered *superior accuracy and speed* compared to both cloud NLP
services and general-purpose LLMs. For instance, in a medication coding
benchmark, the Terminology Server (via Healthcare NLP) correctly mapped
medications to RxNorm codes with **82.7%** top-3 accuracy, versus
**55.8%** for Amazon Comprehend Medical and only **8.9%** for GPT-4,
while also being about **5× more cost-effective** than the next best
solution. These results highlight that the Terminology Server not only
integrates well – it brings **state-of-the-art performance** in
accuracy, reliability, and efficiency for enterprise healthcare
scenarios.

### **Deployment & Compliance**

John Snow Labs’ Terminology Server is designed for flexible deployment
in **enterprise environments with strict compliance requirements**. It
can be deployed on-premises or in a private cloud, ensuring that
**sensitive health data and PHI never leave your controlled
environment**. The software is provided as a containerized application
and is cloud-agnostic – many customers run it on AWS or Azure (John Snow
Labs offers pre-configured Amazon Machine Images on AWS Marketplace as
well as Azure templates), or on their own Kubernetes clusters or VMs in
hospital data centers. This deployment flexibility means organizations
can meet data residency requirements and integrate with existing
security infrastructures (VPCs, corporate firewalls, etc.).

From a compliance standpoint, the Terminology Server supports the **full
healthcare security stack**: encryption in transit and at rest,
role-based access control for administrative functions, audit logging of
terminology updates and user access, and compatibility with single
sign-on (SAML/OAuth) if integrated via the UI. The platform has been
used in environments that require HIPAA compliance and has the necessary
safeguards to qualify as a HIPAA-compliant component (e.g., no
persistent PHI storage—only codes and metadata are stored; any transient
query data can be purged or anonymized as needed). **No patient
identifiers or clinical notes are stored** in the server – only the
standard terminologies and user-defined mappings – which further
simplifies compliance, as the server deals purely with reference data
and mapping logic.

**Privacy and Data Governance**

When the Terminology Server is deployed on-prem or in a private cloud,
all queries to it (e.g., a phrase to code search) stay within the
organization’s secure network. Unlike some cloud-based terminology or
NLP services, there is **no need to send potentially sensitive text or
codes over the public internet** for processing. This is a critical
consideration for healthcare CIOs and compliance officers. The server
can also be configured to purge query logs or not log query content at
all, ensuring that no trace of PHI is kept. Customers maintain full
ownership of any custom code systems or value sets they load into the
system, and these can be exported at any time – avoiding vendor lock-in.

**Maintenance and Support**

John Snow Labs provides commercial support for the Terminology Server,
including regular updates of content (e.g., new code releases) and
software patches. Dedicated support ensures that as new versions of
terminologies (ICD, SNOMED, etc.) are released, the server’s content
library can be updated seamlessly without downtime. Versioning is
handled in a way that users can choose to keep older versions available
for historical data while adopting new versions for future data, which
is important for long-term clinical record-keeping and research
reproducibility. The system also supports **multiple environments**
(dev, test, prod) so organizations can validate new terminology updates
in a sandbox before rolling them into production use.

In summary, the Terminology Server can be deployed in a manner that
meets the **highest levels of data protection and compliance**, while
its ongoing maintenance is streamlined through vendor support. This
ensures **enterprise IT teams and architects** can adopt it without
compliance headaches and integrate it within their existing governance
frameworks.

### **Use Cases**

Tailored for healthcare, the Medical Terminology Server uses John Snow
Labs proprietary models and knowledge bases that understands the nuances
of clinical language and medical terminologies, ensuring that the
information it generates is accurate and highly relevant.

The platform comes pre-loaded with a large number of standard medical
terminologies; and offers a robust API and user interface that enable
advanced concept search, mapping, and normalization.

The Medical Terminology Server addresses challenges often faced by
traditional terminology servers in healthcare: identifying concepts
without exact matches by correcting spelling errors and using synonyms;
finding the most relevant concept based on clinical context for accurate
coding of diagnoses, drugs, treatments, or adverse events; identifying
semantically close concepts for terms that may vary in expression.

**Clinical Coders & Medical Billing Specialists**

- **Accurate Code Assignment from Clinical Notes**: Coders can input
  free-text from clinical documentation (e.g., “high blood pressure”,
  “sugar disease”) into Terminology Server’s User Interface to retrieve
  the most relevant codes from systems like ICD-10 or SNOMED CT. The
  server interprets synonyms, common misspellings, and colloquialisms
  using advanced search techniques. This reduces manual lookup time and
  reliance on clinical intuition, minimizes errors by handling spelling
  variations and informal terms and ensures coding accuracy for billing,
  documentation, and compliance.

- **Cross-Mapping Diagnoses Across Code Systems**: Coders working across
  international or multi-payer environments often need to convert codes
  between SNOMED CT, ICD-10, or OMOP Standard concepts. Terminology
  Server simplifies this with direct mapping support and concept
  relationships. This ensures consistency and traceability across code
  systems, ereduces duplicate effort in translating codes manually and
  supports diverse documentation and billing requirements in global
  settings.

**Researchers & Pharmacovigilance Professionals**

- **Concept Expansion for Adverse Event Detection**: Researchers
  analyzing narrative data (e.g., clinical notes, social media, or
  patient feedback) can input vague or colloquial descriptions of
  symptoms (e.g., “woozy,” “fainting”) and retrieve corresponding
  standardized adverse event codes. The system supports enhanced
  detection of underreported or informally described events and improved
  sensitivity and completeness in pharmacovigilance analyses. As such it
  facilitates the expansion of search coverage across structured and
  unstructured sources.

- **Search & Linkage Across Clinical Contexts**: Studies that aim to
  identify all variations of “hypertension” across SNOMED, ICD-10, and
  patient language can use the Terminology Server’s semantic search and
  mappings to connect equivalent and closely related concepts. This
  facilitates comprehensive and flexible cohort discovery, supports
  broader clinical research by capturing related expressions and
  enhances study accuracy and reproducibility across vocabularies.

  In addition to the above, John Snow Labs’ Terminology Server is
  engineered to address a broad range of real-world healthcare and
  biomedical use cases where consistent coding and interoperability are
  critical:

<!-- -->

- **Clinical Decision Support**  
  Ensuring that point-of-care applications and alert systems use
  standardized codes (e.g. SNOMED CT or LOINC) for diagnoses, labs, and
  medications. The Terminology Server can translate free-text or local
  codes into standard codes in real time, enabling accurate triggers for
  clinical guidelines and drug safety alerts in EHRs and physician order
  entry systems. This supports safer, evidence-based care by aligning
  data with decision support rules.

- **Automated Medical Coding & Billing**  
  Assisting clinical coders and billing specialists in mapping clinical
  notes and diagnoses to billing codes (ICD-10-CM, CPT, HCC categories).
  For example, coders can input a phrase like “high blood sugar” or
  “sugar disease” and retrieve the correct ICD-10-CM code for diabetes.
  By recognizing synonyms and colloquial terms, the server reduces
  manual lookup time and improves coding accuracy for reimbursement and
  reporting.

- **Data Normalization & Integration**  
  Normalizing diverse clinical text and data into a common vocabulary
  for unified analysis. The Terminology Server can map equivalent
  concepts across coding systems – for instance, linking an EHR’s
  internal codes or an old ICD-9 code to a modern standard like SNOMED
  CT. This canonical mapping simplifies aggregating data from multiple
  sources and ensures that analytics and AI models work on consistent,
  comparable data. It is especially useful in ETL pipelines for data
  lakes and in creating longitudinal patient records from multi-modal
  data

- **Pharmacovigilance & Real-World Evidence (RWE)**  
  In pharmaceutical research and post-market safety, the Terminology
  Server can map drug names and adverse event descriptions to standard
  vocabularies like RxNorm and MedDRA. For instance, researchers
  analyzing patient feedback or clinician notes can input colloquial
  symptom descriptions (“feeling woozy”) and obtain the corresponding
  MedDRA adverse event code or SNOMED CT concept. This enables detection
  of under-reported events and aggregation of real-world data across
  sources for safety signals and outcomes research.

- **Population Health & Analytics**  
  Public health agencies and analytics teams can leverage the
  Terminology Server to unify diagnosis and procedure codes from
  different providers for cohort discovery and outcomes analysis. The
  server supports value set definitions (e.g. a list of codes for
  “diabetes and its complications”) that can be used to query data
  warehouses. By expanding value sets and validating codes, it helps
  ensure that counts and measures (like prevalence, readmission rates)
  are calculated on the correct, complete set of codes. This is crucial
  for quality reporting, epidemiology studies, and population health
  management initiatives.  
    
  In all these scenarios, the Terminology Server acts as the **“single
  source of truth” for terminology** – whether the goal is to
  auto-normalize streaming data, assist human coders with suggestions,
  or enable applications to consistently interpret clinical data. The
  result is **higher data quality, reduced administrative burden, and
  enhanced interoperability** across the healthcare ecosystem.

###  **Relevant Resources**

For more information on John Snow Labs’ Terminology Server, the
following resources are available:

- **Product Page:**
  <https://nlp.johnsnowlabs.com/docs/en/terminology_server/term_server>

- **Webinar**:
  [An-llm-enabled-medical-terminology-server](https://www.johnsnowlabs.com/an-llm-enabled-medical-terminology-server)

- **Blog Link:** [Comparing OpenAI LLMs and John Snow Labs’ Medical
  Terminology Server (TS) for Medical Terminology
  Mapping](https://www.johnsnowlabs.com/comparing-openai-llms-and-john-snow-labs-medical-terminology-server-ts-for-medical-terminology-mapping)
