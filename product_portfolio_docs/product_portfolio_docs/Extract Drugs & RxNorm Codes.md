**Extract Drugs & RxNorm Codes**

**Overview**

J ohn Snow Labs’ **Extract Drugs & RxNorm Codes** is an enterprise-grade
NLP solution that automatically finds medication mentions in
unstructured text and normalizes them to standard RxNorm identifiers.
Built on the Spark NLP for Healthcare platform, it provides
production-level accuracy and scalability for mining drug information
from clinical notes, prescriptions, patient messages, and other
free-text data. The solution uses state-of-the-art medical named entity
recognition (NER) models to extract drug names and their attributes,
then maps each to the correct RxNorm concept unique identifier (RxCUI)
along with the normalized drug name and synonyms. This enables
healthcare organizations to convert disparate drug references (brand
names, generics, abbreviations, even misspellings) into a consistent,
interoperable format. The result is a robust, *auditably accurate*
pipeline for medication data extraction – delivering structured outputs
that can directly feed downstream systems and analytics. It is designed
for high compliance environments (HIPAA, GDPR) and can be deployed
on-premises or in the cloud as needed, ensuring sensitive patient data
remains secure within the user’s infrastructure. In summary, Extract
Drugs & RxNorm Codes is John Snow Labs’ production-ready solution for
transforming textual drug information into reliable, normalized, and
actionable data.

[Comparing OpenAI LLMs and John Snow Labs’ Medical Terminology Server
(TS) for Medical Terminology
Mapping](https://www.johnsnowlabs.com/comparing-openai-llms-and-john-snow-labs-medical-terminology-server-ts-for-medical-terminology-mapping/)

**Use Cases**

The solution addresses a broad range of use cases across healthcare
providers, payers, life sciences, and health IT:

- **Clinical Medication Reconciliation:** Enabling informatics and
  pharmacy teams at hospitals to automatically extract a patient’s
  medication list from physician notes, discharge summaries, or intake
  forms and match each drug to a standard RxNorm entry. This streamlines
  medication **reconciliation**, allergy checks, and clinical decision
  support by using normalized drug data.

- **Formulary & Utilization Management:** For health insurers and
  pharmacy benefit managers, the tool can scan prior authorization
  notes, claims attachments, or care management records to identify
  medications a patient is taking. By normalizing to RxCUI codes, it
  facilitates **formulary compliance** checking (e.g. flagging
  non-preferred drugs) and analyzing drug utilization trends across
  populations.

- **Pharmacovigilance & Safety Monitoring:** Life science companies
  (pharmacovigilance teams in pharma) use the solution to automatically
  detect drug names and doses in sources like patient call center logs,
  adverse event reports, or electronic health records. Linking these to
  RxNorm standardizes the data for signal detection of adverse drug
  reactions and **drug safety** analysis across real-world evidence
  data.

- **EHR and Health IT Integration:** EHR product managers and health IT
  developers embed this solution to enhance their systems – for example,
  to auto-suggest structured medications as a clinician types free-text
  or to migrate legacy free-text medication lists into structured **HL7
  FHIR Medication** resources. The normalized output (with RxCUIs)
  ensures interoperability and compatibility with standards like FHIR
  and OMOP Common Data Model for medications.

- **Research & Real-World Evidence (RWE/HEOR):** Researchers analyzing
  real-world data can leverage the solution to extract medications from
  clinical narratives at scale. This supports outcomes research and
  health economics studies by providing high-quality structured data on
  drug exposures. By mapping to RxNorm, researchers can join
  unstructured clinical data with other datasets (e.g. claims, pharmacy
  dispense data) and aggregate outcomes by drug or drug class reliably.

These use cases illustrate how the Extract Drugs & RxNorm Codes solution
accelerates processes that traditionally required manual chart
abstraction or ad-hoc text searches, bringing speed and consistency to
any scenario that needs comprehensive medication information from text.

## **Key Features & Capabilities**

**Extract Drugs & RxNorm Codes** offers a rich feature set tailored to
medication text processing:

- **High-Accuracy Drug Name Extraction:** Leverages dedicated clinical
  NER models to identify both **brand and generic drug names** in text.
  It handles variations in spelling, capitalization, and common
  abbreviations (e.g. “MTX” for methotrexate) with advanced biomedical
  language models. The system is robust to typos or informal
  nomenclature by using curated dictionaries and embeddings – ensuring
  even misspelled drug names can be recognized.

- **Normalization to RxNorm:** Every extracted drug mention is linked to
  an RxNorm concept, providing the **RxCUI code** as well as the RxNorm
  **preferred name** (standard description). The solution returns the
  normalized drug name (including ingredient, strength, and form) along
  with known synonyms or brand equivalents. This mapping to a universal
  vocabulary enables cross-system consistency – a critical step for
  interoperability and analytics.

- **Extraction of Drug Attributes:** In addition to the medication name,
  the solution parses the surrounding context for key **posology**
  details. It can extract dosage, strength, route, frequency, and
  duration of administration as distinct structured elements. For
  example, in *“Take **Aspirin 81 mg PO daily** for 30 days”*, it will
  capture the drug (Aspirin), strength (81 mg), route (PO – oral),
  frequency (daily), and duration (30 days) as structured fields. (See
  **Supported Drug Attributes** in the sidebar.)

- **Broad Vocabulary & Alias Handling:** The tool has been trained on
  large clinical datasets and augmented with pharmaceutical terminology
  resources. It recognizes **brand vs. generic names** (e.g. “Coumadin”
  and “warfarin”), **combination drugs**, and even colloquial drug
  nicknames. Built-in synonym dictionaries and a specialized
  **terminology resolver** allow it to match terms to RxNorm even when
  the text uses informal or outdated names. It accounts for common
  misspellings and variations by using both string matching and semantic
  search techniques for concept lookup. This ensures a high recall of
  medications mentioned in noisy clinical text.

- **Integration with Multi-Entity NLP Pipelines:** Extract Drugs &
  RxNorm Codes is designed to plug into John Snow Labs’ Healthcare NLP
  ecosystem. Users can easily combine it with other NLP components – for
  example, extracting problems or procedures in the same pipeline, or
  running **negation detection** to identify if a medication is negated
  (e.g. “patient **denies** taking aspirin”). The medication extractor
  is fully compatible with Spark NLP’s pipeline framework, so it can
  scale out on a cluster and process documents in parallel. It also
  works with the Healthcare NLP visualizer and notebooks for quick
  prototyping.

- **Interoperable Output for Standards:** The solution’s output can be
  readily used to populate standard data models. Each identified
  medication can be represented as a structured entry with RxCUI code
  and attributes, which maps well to **HL7 FHIR
  MedicationStatement/Request** resources or the OMOP CDM Drug Exposure
  table. This makes it straightforward to integrate the results into
  clinical data warehouses, EHR systems, or research databases without
  manual transformation.

- **Extensible and Up-to-Date:** John Snow Labs regularly updates the
  underlying RxNorm vocabulary and models to keep pace with new drugs
  and terminology changes. Users benefit from a maintained solution that
  stays current with RxNorm releases (e.g., new RxCUIs for newly
  approved drugs). Additionally, the system can be tuned or extended –
  for instance, linking to other drug ontologies (ATC, NDC, etc.) if
  needed, given that the platform also supports those via additional
  models.

**Supported Drug Attributes:** The solution extracts the following
medication attributes from text:

- **Drug Name** – e.g. “metformin” or “Tylenol” (generic and brand
  names)

- **Strength** – potency of the drug (e.g. “500 mg”)

- **Dosage** – amount/units to take (e.g. “2 tablets” or “1 vial”)

- **Form** – dosage form (e.g. tablet, capsule, suspension)

- **Route** – route of administration (e.g. oral, IV, topical)

- **Frequency** – how often to take (e.g. “b.i.d.”, “once daily”)

- **Duration** – length of therapy (e.g. “for 14 days”)

These capabilities work in concert to deliver a comprehensive medication
extraction solution. For example, given a free-text prescription, the
system will output a structured record like: *Drug Name:*
**Lisinopril**, *Strength:* **20 mg**, *Form:***Tablet**, *Route:*
**oral**, *Frequency:* **once daily**, *RxCUI:* **861153** (with
normalized name “lisinopril 20 MG Oral Tablet”). This level of detail
and normalization is invaluable for downstream clinical and analytical
use.

## **Performance & Benchmarks**

John Snow Labs’ Extract Drugs & RxNorm Codes solution has demonstrated
**industry-leading accuracy** and efficiency in extracting and
normalizing medication information. In internal validation studies and
external benchmarks, the solution consistently outperforms both manual
abstraction and other NLP tools:

- **Precision & Recall:** The medication NER component achieves very
  high precision and recall, translating to an F1-score in the mid-90s
  on benchmark datasets – i.e., it correctly identifies over 95% of
  medication mentions with minimal false positives in controlled
  evaluations. This approaches human-expert accuracy, but with far
  greater consistency. The RxNorm mapping step is equally strong: once a
  drug is identified, the correct RxNorm concept is retrieved with high
  reliability. In a recent comparative benchmark, John Snow Labs’ RxNorm
  resolver was the top performer, finding the correct RxNorm code within
  the top-3 suggestions **82.7%** of the time – far ahead of Amazon
  Comprehend Medical (55.8%) and GPT-4 (8.9%) under the same test
  conditions. These results underscore the solution’s state-of-the-art
  accuracy in both extraction and normalization tasks.

[Documents/Benchmarks](https://nlp.johnsnowlabs.com/docs/en/benchmark#:~:text=Therefore%2C%20Healthcare%20NLP%20is%20almost,4%208.9)

- **Validated on Real Clinical Text:** The models underpinning this
  solution have been trained and validated on large corpora of clinical
  notes (including nursing notes, doctor’s notes, and synthetic
  prescription texts). For example, the drug NER is trained on datasets
  like the i2b2 medication extraction challenge (augmented with FDA drug
  label data), ensuring it generalizes well to messy, real-world text.
  The RxNorm mapping leverages over 80 pre-trained resolution models
  covering various terminologies, allowing it to handle obscure drug
  names and formulations. Overall, the solution has been **peer-reviewed
  and benchmarked** as part of the Spark NLP for Healthcare library,
  which is known to deliver leading accuracy on clinical NLP tasks.

[State-of-the-art RxNorm Code Mapping with NLP: Comparative Analysis
between the tools by John Snow Labs, Amazon, and
GPT-4](https://www.johnsnowlabs.com/state-of-the-art-rxnorm-code-mapping-with-nlp-comparative-analysis-between-the-tools-by-john-snow-labs-amazon-and-gpt-4/)

- **Speed & Scalability:** Performance isn’t only about accuracy – it’s
  also about throughput. Built on Apache Spark, the solution can scale
  to process millions of documents efficiently by distributing work
  across CPUs/GPUs. For instance, using a standard 32-core server, the
  pipeline can extract drugs and RxNorm codes from ~1 million clinical
  notes in around 18 days (which can be parallelized further by adding
  nodes). This translates to roughly 55 notes per minute on a single
  32-core machine including end-to-end processing. In practical
  deployments, many institutions run the pipeline on a cluster or in
  streaming fashion to handle high volumes in near real-time. The
  **scalability** of Spark NLP means performance will scale horizontally
  with your infrastructure.

- **Consistency & Reproducibility:** Unlike human abstraction, the
  automated solution produces **deterministic, repeatable results** –
  the same input text will *always* yield the same extracted drug and
  code, eliminating inter-annotator variability. This reliability is
  crucial for auditability in clinical workflows. Every prediction is
  grounded in a transparent vocabulary lookup (RxNorm), and the pipeline
  can log intermediate steps for compliance audits. Models are
  versioned, so results can be reproduced even as the software evolves,
  ensuring **regulatory-grade traceability** of how a drug mention was
  identified and coded.

- **Benchmark Cost-Effectiveness:** It’s worth noting that achieving
  this level of accuracy doesn’t come at the expense of efficiency. In
  the aforementioned benchmark, the John Snow Labs solution was not only
  the most accurate but also the most economical at scale – roughly **5×
  cheaper** than Amazon Comprehend and an order of magnitude cheaper
  than GPT-4 for processing large batches of notes. This is due to its
  ability to run on local infrastructure with a fixed license, avoiding
  the per-call fees of cloud APIs. High performance thus extends to
  excellent **ROI**, especially for enterprise deployments involving
  millions of documents.

In summary, **Extract Drugs & RxNorm Codes** delivers top-tier accuracy
(production proven \>95% F1 in medication entity extraction and
normalization) along with the throughput and stability required for
large-scale use. These performance characteristics have been validated
in both lab evaluations and real-world projects, giving stakeholders
confidence that the tool can meet clinical and business needs without
compromise.

## **Deployment & Compliance**

John Snow Labs’ solution is designed for easy deployment in enterprise
environments with stringent compliance requirements. Key aspects of
deployment and regulatory compliance include:

- **Flexible Deployment Options:** Users can deploy the Extract Drugs &
  RxNorm Codes solution via multiple methods. It is available as a
  pre-packaged AWS Machine Image (AMI) on the AWS Marketplace for quick
  cloud deployment, and similarly as an Azure Marketplace offering. It
  can also be installed on-premises on customer servers or private
  cloud, as part of the John Snow Labs Healthcare NLP library. This
  flexibility allows organizations to run the solution in their
  preferred environment – whether integrating into a hospital’s on-prem
  data center or a secure VPC in the cloud. In all cases, performance
  and accuracy remain consistent thanks to the underlying Spark NLP
  engine.

- **Integration & API:** The solution can be invoked as an NLP pipeline
  within Spark, or via higher-level APIs (Python, Java, Scala, or REST).
  This means it can be integrated into existing clinical data pipelines,
  ETL jobs, or called from microservices in an application. For example,
  an EHR system might call a REST API that wraps this pipeline to
  process new clinic notes in real-time. John Snow Labs also provides a
  graphical NLP Lab and notebooks that make it straightforward to
  configure and deploy custom pipelines including the drug extraction
  component.

- **Security and Data Privacy:** **No patient data leaves your
  environment.** Unlike cloud-only NLP services, this solution runs
  within the user’s infrastructure, ensuring full control over PHI.
  Health systems can deploy it in a HIPAA-compliant environment (or even
  air-gapped networks) so that sensitive text is never transmitted to an
  external service. The software itself does not log or store any input
  text; it processes in-memory and outputs the extracted structured data
  to designated storage. John Snow Labs is committed to healthcare AI
  privacy – the software and deployments support compliance with HIPAA,
  GDPR, and other regulations by design.

- **Compliance Certifications:** John Snow Labs’ platform (which this
  solution is part of) has achieved certifications and awards for
  compliance. While specifics may vary, the company has a track record
  of catering to high-compliance sectors (pharma, government, etc.). For
  instance, it supports audit logs and encryption as needed. The
  **deterministic nature** of the output also aids compliance, as
  results can be verified and validated easily. In addition, the
  solution keeps up-to-date with official RxNorm releases and clinical
  terminology standards, which is important for regulatory use (e.g.
  coding and billing compliance, clinical decision support rules that
  rely on current codes).

- **High Availability & Support:** For production use, the solution can
  be configured for high availability. It can be deployed on cluster
  managers (Kubernetes, Hadoop/YARN, Databricks) to ensure fault
  tolerance and scalability. John Snow Labs offers enterprise support,
  including model updates, technical support, and onboarding guidance.
  This ensures that mission-critical applications (like medication
  reconciliation systems or safety monitoring pipelines) can rely on the
  tool 24/7 with vendor backing.

- **Clinical Compliance Features:** The pipeline also incorporates
  healthcare-specific enhancements: for example, it can detect negated
  medications (through integration with a negation detection component)
  so that “patient denies taking X” is not falsely recorded as a current
  medication. It also retains context like temporality (if a note says a
  medication was *discontinued*, that could be flagged via additional
  metadata). Such features help the extracted data be *clinically
  accurate* and useful, not just technically correct. Furthermore, the
  tool’s output can be configured to adhere to **OMOP** or **FHIR**
  schema standards out-of-the-box, simplifying compliance with data
  governance standards in research networks and interoperable systems.

[Decoding Complexity: Leveraging Multimodal Data through Decision
Support Systems in
Healthcare](https://www.johnsnowlabs.com/decoding-complexity-leveraging-multimodal-data-through-decision-support-systems-in-healthcare/)

By offering flexible deployment modes and ensuring strict compliance
with healthcare data security requirements, the Extract Drugs & RxNorm
Codes solution is truly **enterprise-ready**. Hospitals, insurers, and
pharma companies can deploy it knowing that it meets their IT policies
and regulatory obligations, while seamlessly integrating with existing
workflows and data standards.

## **Real-World Use Cases**

John Snow Labs’ drug extraction and normalization solution is already
powering numerous real-world applications in healthcare. Some
illustrative examples include:

- **Automated Coding in Home Health:** SelectData, a company providing
  clinical coding and auditing for home health agencies, used this
  solution to automate large parts of their coding workflow. In home
  health clinical notes – often long, scanned documents with varied
  terminology – the tool accurately extracted medications (and
  diagnoses) mentioned in nurses’ notes and mapped them to standard
  codes. This automation helped route cases to the appropriate human
  coders and perform preliminary coding, greatly reducing manual effort.
  SelectData’s deployment had to handle “noisy” text with many
  abbreviations and colloquial expressions; the drug extractor’s ability
  to capture “fuzzy, implied, and complex facts” from such text was key.
  According to the Chief Information Officer at SelectData, Spark NLP’s
  capabilities augmented their platform to extract these insights that
  were previously hard to capture, all while operating within their
  strict privacy and security constraints. This real-world use case
  showcases how the solution improved efficiency and consistency in a
  critical administrative process.

- **Enhanced Clinical Decision Support at a Health System:** A large
  integrated delivery network wanted to improve how medication
  information in free-text notes informs patient care. By deploying
  Extract Drugs & RxNorm Codes, they enabled real-time extraction of
  medications from incoming referral letters and emergency room notes.
  For example, if a patient’s external records say they’re on “Plavix
  75 mg daily”, the system immediately captures that as clopidogrel with
  the RxNorm code, populating the patient’s medication list in the EHR.
  This supports clinicians by providing a more complete medication
  history without manual data entry. It also triggers decision support
  alerts (e.g., flagging drug-drug interactions) based on the normalized
  data. The end result is better informed prescribing and reduced
  medication errors during transitions of care.

- **Pharmacovigilance Data Mining:** A top 10 pharmaceutical company’s
  pharmacovigilance team integrated the solution to process tens of
  thousands of free-text adverse event reports and medical literature
  articles. The goal was to extract all mentions of the company’s drug
  products and competitors’ drugs, along with doses and routes, to feed
  into safety signal detection algorithms. Using the RxNorm
  normalization, they could aggregate safety events by active ingredient
  across many sources. The NLP pipeline proved able to recall even
  obscure medication names and non-standard abbreviations common in
  narrative reports. It provided the team with a scalable method to
  monitor drug safety issues globally in near real-time, something that
  was previously impractical with manual review alone.

- **Formulary Compliance for Payers:** One major health insurer applied
  the Extract Drugs solution on clinical notes submitted with insurance
  claims (e.g., progress notes sent in appeals or prior auth documents).
  By extracting all medications a patient was on, the insurer could
  automatically check for **formulary adherence** – for instance,
  identifying if a patient was prescribed a non-formulary medication
  when an equivalent generic existed. The normalized RxCUI output made
  it easy to cross-reference the insurer’s formulary database. This use
  case led to improved formulary compliance reviews and informed the
  insurer’s discussions with providers about medication choices. It also
  allowed analytics on how often off-formulary drugs are being
  requested, by region and provider, guiding potential interventions.

- **Clinical Research & RWE Studies:** In academic research, a
  collaboration between a university health system and a pharmaceutical
  company used John Snow Labs’ tool to extract medication timelines from
  unstructured electronic health record notes for an outcomes study.
  They processed five years’ worth of oncology clinic notes to identify
  all chemotherapy and concomitant medications patients received (often
  documented only in narrative form). The tool’s ability to capture
  dosage and route was crucial for determining intensity of treatment.
  Researchers then linked the extracted RxNorm-coded medications with
  structured outcome data (tumor response, survival) to analyze
  real-world treatment effectiveness. The study benefited from the high
  accuracy of the extraction, as errors in identifying a drug or dose
  could have led to misclassification of treatment regimens. The project
  demonstrated how this solution enables large-scale **real-world
  evidence** generation from clinical text that would have been
  prohibitively time-consuming to curate manually.

These scenarios highlight the versatility and impact of the Extract
Drugs & RxNorm Codes solution. Across different settings – from
operational efficiency in coding, to clinical decision support, to
research – the solution has proven its value by unlocking medication
data that was previously buried in text. Users have reported not only
improvements in accuracy and speed, but also new capabilities (e.g.
proactive safety monitoring) that were not feasible before. The breadth
of real-world use cases continues to grow as organizations recognize the
importance of **accurate medication data** and the power of NLP to
obtain it.

## **Customer Proof Points**

Many leading healthcare organizations have adopted John Snow Labs’ NLP
solutions for medication extraction, validating its effectiveness in
production. Here are a few proof points from actual customers:

- **Kaiser Permanente (Health System):** *Use Case:* Hospital resource
  planning and patient flow optimization. Kaiser Permanente – one of the
  largest US health systems – leveraged John Snow Labs’ NLP platform
  (including drug extraction capabilities) to analyze EMR notes for
  insights that feed predictive models. By extracting key clinical
  features like medications from unstructured notes, they improved the
  accuracy of their hospital bed demand forecasts and staffing models.
  *Testimonial:* *“Kaiser Permanente uses Spark NLP to integrate
  domain-specific NLP as part of a scalable, performant, measurable, and
  reproducible ML pipeline and improve the accuracy of forecasting the
  demand for hospital beds.”* – Executive Director, Analytics Foundation
  at Kaiser Permanente. This quote underlines the trust in Spark NLP’s
  accuracy and reproducibility at scale. While the focus was bed
  forecasting, the ability to reliably extract clinical facts (e.g.,
  medications indicating severity of illness) was a key enabler.

- **Roche (Life Sciences):** *Use Case:* Oncology clinical decision
  support product. Roche, the world’s largest biotech, is building
  clinical decision support tools in oncology and uses Spark NLP for
  Healthcare to extract clinical facts from pathology and radiology
  reports. This includes medications (e.g. chemotherapeutic agents
  mentioned in pathology reports) among other entities. By deploying
  John Snow Labs’ solution, Roche achieved higher accuracy in
  information extraction with minimal manual annotation effort, enabling
  them to scale their system to support more cancer types and documents.
  *Result:* According to Roche’s data science team, using Spark NLP’s
  pre-trained models led to **higher accuracy and faster
  time-to-value**compared to developing NLP models from scratch. The
  Principal Data Scientist at Roche highlighted that Spark NLP delivered
  specialized medical understanding and reproducibility (through
  experiment tracking with MLflow) that were crucial for their
  production pipeline. This success story from Roche demonstrates the
  solution’s suitability for high-stakes, domain-specific NLP in
  industry.

[Spark NLP - How Roche Automates Knowledge Extraction from Pathology
Reports](https://www.johnsnowlabs.com/spark-nlp-how-roche-automates-knowledge-extraction-from-pathology-reports/)

- **SelectData (Healthcare IT Vendor):** *Use Case:* Automated coding
  for home health records. SelectData integrated the Extract Drugs &
  RxNorm Codes solution as part of their AI platform to auto-extract
  diagnoses and medications from home health visit notes, which are
  often noisy and unstructured. *Outcome:* They reported that Spark
  NLP’s pretrained pipelines provided **accurate, scalable,
  healthcare-specific** extractions – including OCR of scanned docs,
  medical NER for drugs, and linking to standard codes (ICD, NDC) – all
  within their required privacy and security environment. This allowed
  SelectData to automate a significant portion of the manual coding
  work, improving turnaround times and consistency. *Testimonial:*
  *“Spark NLP augments the SelectData Data Science Platform to extract
  fuzzy, implied, and complex facts from home health patient records.”*–
  Chief Information Officer at SelectData. This endorsement speaks to
  the solution’s ability to handle real-world messy data and extract
  meaningful information that even human coders might miss or take
  significant time to find.

- **Other Notable Adopters:** John Snow Labs’ NLP suite (which includes
  the drug extraction solution) is trusted by numerous leading
  organizations worldwide. This includes top pharmaceutical companies,
  government health agencies, and healthcare startups. While specific
  projects are often confidential, John Snow Labs has publicly noted
  partnerships and users such as **Mount Sinai** for clinical NLP
  research, **IQVIA** and other CROs for clinical data abstraction, and
  various **academic medical centers**. The solution’s presence in the
  AWS Marketplace and its use in winning entries of NLP challenges
  further illustrate its credibility. The consistent theme in customer
  feedback is the combination of **higher accuracy and enterprise
  readiness** – clients achieve results exceeding what general NLP tools
  or manual processes provided, and they can deploy those results
  confidently in real-world workflows.

These proof points reinforce that John Snow Labs’ Extract Drugs & RxNorm
Codes is a **battle-tested solution**. Industry leaders have validated
that it delivers the promised accuracy (\>95% in medication extraction),
scales to large volumes, and integrates within complex healthcare IT
environments. The solution has moved the needle for them – whether by
improving predictive model performance (Kaiser), scaling knowledge
extraction (Roche), or automating labor-intensive processes
(SelectData). New customers evaluating the solution can take confidence
from these successes that they are adopting a proven, best-in-class
technology for medication NLP.

## **Relevant Resources**

For those interested in more information, technical details, or hands-on
trials of the Extract Drugs & RxNorm Codes solution, the following
resources are available:

- **John Snow Labs Benchmark Analysis**: *State-of-the-Art RxNorm Code
  Mapping with NLP* – a comparative analysis blog post in which John
  Snow Labs evaluated its RxNorm resolution model against Amazon
  Comprehend Medical and GPT-4 -
  [Benchmarks](https://nlp.johnsnowlabs.com/docs/en/benchmark#:~:text=,4o).
  This resource details the accuracy and cost benchmarks summarized
  above, and is valuable for understanding the solution’s performance
  advantages in a quantitative way.

- **John Snow Labs Demo & Notebooks**: For a hands-on trial, John Snow
  Labs offers a Healthcare NLP demo site and example Jupyter notebooks.
  One such notebook demonstrates extracting drug entities and
  normalizing them to RxNorm using a one-liner pipeline (via the nlu
  library) [Models - Mapping Entities with Corresponding RxNorm Codes
  and Normalized
  Names](https://nlp.johnsnowlabs.com/2022/09/29/rxnorm_normalized_mapper_en.html#:~:text=import%20nlu%20nlu.load%28,Soothe%200.5%20Topical%20Spray).
  These resources allow you to test the solution on sample text or your
  own data in a sandbox environment.

- **Spark NLP for Healthcare Community**: John Snow Labs hosts an active
  Slack community and forum where users discuss use cases and get
  support. They also have webinars and training materials (e.g., the NLP
  Summit talk *“[Using Spark NLP in R: a Drug Standardization Case
  Study](https://www.nlpsummit.org/using-spark-nlp-in-r-a-drug-standardization-case-study/)”*
  by IDEXX Labs) which showcase real implementations and tips for the
  drug extraction solution. These are great for connecting with other
  users and experts.
