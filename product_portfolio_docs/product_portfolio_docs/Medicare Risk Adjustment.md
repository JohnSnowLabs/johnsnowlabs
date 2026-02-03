**Medicare Risk Adjustment**

**Overview**

John Snow Labs’ Medicare Risk Adjustment platform is a **full-stack AI
solution** designed to optimize Risk Adjustment Factor (RAF) scores by
**automating Hierarchical Condition Category (HCC) coding** from both
structured and unstructured clinical data. Using only claims or problem
list data often leaves significant gaps – studies show that nearly **40%
of important diagnoses may only appear in free-text notes**. This
platform addresses that gap by leveraging **clinical NLP** to extract
undocumented conditions from physician notes, ensure **complete and
accurate HCC capture**, and maximize appropriate reimbursements. The
result is a seamless end-to-end system that identifies missed chronic
conditions, links them to proper HCC codes, and updates RAF calculations
in real time, all while maintaining transparency and compliance.

*(Sidebar – **Supported CMS-HCC Versions:** The platform supports the
latest CMS-HCC model versions **v24** and **v28** for Medicare
Advantage, as well as the HHS-HCC model for Affordable Care Act risk
adjustment.)*

**Use Cases**

John Snow Labs’ solution supports both **retrospective** and
**prospective** risk capture workflows in Medicare Advantage and ACA
plans:

- **Retrospective Risk Adjustment:** Automatically review past encounter
  notes and claims to find **previously undocumented HCC conditions**,
  ensuring no diagnosis that impacts RAF was overlooked in the prior
  year. This helps plans recapture missed risk by discovering conditions
  mentioned only in narrative notes (e.g. a physician documented COPD in
  a note but it wasn’t coded on a claim).

- **Prospective Risk Capture:** Before upcoming patient visits, identify
  patients with likely HCC conditions (e.g. diabetes with complications,
  CHF, CKD) that are not yet coded, and flag these “suspect” conditions
  for providers. The platform can update the EHR problem list or provide
  reports to **prepare clinicians** to address and document these
  conditions in the next encounter. This proactive approach ensures
  **accurate documentation upfront**, improving care and RAF
  concurrently.

- **HCC Suspect Validation:** In workflows for Accountable Care
  Organizations (ACOs) and payers, the system validates “suspect” HCCs
  by scanning the patient’s charts for **supporting evidence**. For
  example, if analytics suspect a patient has chronic kidney disease
  (CKD) due to lab trends, the NLP can confirm mentions of CKD in the
  clinical text and surface those notes as justification. This
  **evidence linking** helps coding teams confirm true positives and
  avoid chasing false leads.

- **Audit Preparation (RADV Readiness):** The platform provides an audit
  trail for every HCC code it identifies, including the exact
  documentation snippet and metadata (date, provider, etc.). This
  greatly streamlines preparation for **CMS Risk Adjustment Data
  Validation (RADV)** audits or OIG compliance checks, since each
  submitted HCC code is backed by verifiable documentation.
  Organizations can rapidly pull **exportable audit packets** with
  annotated note excerpts for each HCC – reducing the time and effort
  needed to compile audit evidence.

- **Real-Time RAF Monitoring:** By integrating into claims and EHR data
  pipelines, the solution can maintain an up-to-date **RAF score for
  each member in real time**. As new diagnoses are documented (either
  manually or by the NLP system), RAF scores are recalculated (for both
  CMS-HCC and HHS-HCC models) so that analysts can monitor risk scores
  continuously. Health plans and at-risk providers can set alerts or
  dashboards for significant RAF changes, ensuring **no lag in
  recognizing population risk** changes mid-year. This supports use
  cases like tracking ACO performance and identifying emerging high-risk
  patients sooner.

These use cases span payer workflows (e.g. insurer risk adjustment units
using the system to improve coding across their membership) and provider
use cases (e.g. integrated systems and risk-bearing provider groups
using it to improve documentation and care). By supporting
retrospective, concurrent, and prospective reviews, the platform helps
organizations achieve **complete and compliant risk capture** while
reducing manual effort.

## **Key Features & Capabilities**

**HCC Code Identification from Clinical Notes:** The solution
automatically extracts diagnosis mentions from unstructured text –
**discharge summaries, progress notes, specialist consults, etc.** – and
maps them to ICD-10-CM codes and HCC categories. It uses pre-trained
medical NLP models to recognize conditions and synonyms (e.g. “heart
failure” for CHF) with high accuracy. This ensures that conditions
documented only in free-text are **captured and coded into the
appropriate HCC** categories for RAF scoring.

**Evidence Linking & Justification:** Each extracted HCC code comes with
a **linked evidence snippet** showing where in the note the condition is
mentioned. The platform provides **contextual justification** (e.g.
“COPD – mentioned in Pulmonology note on 2025-07-10: ‘severe COPD
exacerbation last month’). Suspected HCC conditions are presented with
confidence scores and citation of the source text, so clinical coders or
physicians can **validate the findings easily**. This traceability
builds trust and aids compliance – every code has an audit trail back to
the original documentation.

**NLP-Driven Comorbidity Detection:** Beyond single diagnoses, the
system’s NLP is tuned to detect major **comorbidities and
complications** that impact risk scoring. For example, it will identify
combinations like **diabetes with chronic kidney disease**, or comorbid
**COPD and congestive heart failure**, which carry higher HCC weights.
It can also infer related conditions (e.g. finding evidence of **chronic
kidney disease (CKD)** in a diabetic patient’s notes). By parsing the
nuanced clinical language, the platform surfaces all relevant chronic
conditions for each patient, enabling a more accurate cumulative RAF
calculation. These domain-specific NLP models ensure that even subtle
mentions (like “stage 3 CKD” or “EF 35%” indicating heart failure) are
not missed.

**Real-Time RAF Score Calculator:** The platform includes a built-in
**RAF score calculator** supporting CMS-HCC versions **V24 and V28** for
Medicare Advantage, as well as the HHS-HCC model for ACA plans. As
conditions are identified and validated, the software automatically
**recomputes the patient’s RAF**. Users can see the contribution of each
condition to the overall score, and even simulate “before vs. after”
scenarios (e.g. how adding a newly discovered HCC (such as vascular
disease) raises the RAF). The calculator is updated to reflect the
latest model coefficients and disease interactions. This real-time
feedback loop allows prioritization – for instance, highlighting which
patients’ RAF would increase the most from additional coding review (so
resources can focus on charts with the highest potential ROI).

**Full Audit Trail & RADV-Ready Exports:** Every action and suggestion
in the system is logged. There is a **full audit trail** of what notes
were analyzed, which model or rule identified a condition, who validated
it, and when it was added to the problem list or submission. The system
can export detailed **audit reports** for RADV, including for each HCC:
the original documentation excerpt (with patient identifiers redacted if
needed), the coding path, and validation status. This means
organizations can respond to auditor requests promptly with **legally
defensible evidence** for each risk-adjusting code – a process that
traditionally took weeks of chart hunting can be done in seconds.

**Spark NLP Integration & Terminology Server:** Under the hood, the
solution is powered by John Snow Labs’ **Spark NLP for Healthcare**
library, ensuring **scalable performance** on big data (millions of
notes). It also integrates with a **Terminology Server** for up-to-date
medical vocabularies: ICD-10, SNOMED CT, RxNorm, HCC mappings, etc. This
ensures that the HCC mappings are always current (for example,
reflecting the changes in mappings from CMS-HCC v24 to v28) and that
extracted concepts are normalized to standard codes. The Terminology
Server also enables **custom dictionaries or client-specific code
mappings** to be plugged in easily. In short, the platform can
seamlessly tie into clinical coding standards and leverage **enterprise
terminology management**, which is critical in a complex and evolving
regulatory environment.

**Plug-and-Play with EHRs and Claims Pipelines:** The solution was built
with integration in mind. It provides **REST APIs and connectors** that
allow easy integration with electronic health record systems (for
example, pulling notes from an Epic or Cerner system, and writing back
suspected codes or queries to clinicians). It can also ingest data from
claims systems or data lakes (e.g. CSV extracts, HL7 feeds, FHIR
resources). Results can be delivered into workflow tools: for instance,
sending a query or task to a clinician in the EHR to review an
NLP-suggested condition, or updating a data warehouse table with new
codes. This plug-and-play design means organizations can **implement the
platform without overhauling their existing IT –** it slots into the
current workflows and starts adding value from day one.

## **Performance & Benchmarks**

John Snow Labs’ Medicare Risk Adjustment solution has been validated on
industry benchmarks and real-world tests, demonstrating **leading
accuracy and efficiency**:

- **High Clinical Extraction Accuracy:** Achieves an **F1 score of
  ~98.2%** for extracting clinical concepts and diagnoses from text in
  benchmark evaluations. This level of accuracy is on par with expert
  human coders, ensuring that critical conditions are not missed. (John
  Snow Labs’ NLP models have established new state-of-the-art results on
  multiple clinical information extraction challenges, reflecting the
  precision of its HCC extraction capabilities.)

[Delivering Regulatory-Grade, Automated, Multimodal Medical Data
De-Identification](https://www.johnsnowlabs.com/delivering-regulatory-grade-automated-multimodal-medical-data-de-identification)

- **Top Performance on Medical LLM Leaderboard:** The platform’s
  underlying medical language models scored **86.2% accuracy on the Open
  Medical LLM leaderboard’s test harness** – outperforming general
  models like GPT-4 and Google’s Med-PaLM 2 on clinical knowledge Q&A.
  This indicates the solution’s deep understanding of medical context
  and terminology. Such high accuracy on comprehensive medical
  benchmarks translates to more reliable identification of complex
  conditions in notes.

- **\>99% De-Identification Accuracy:** In collaboration with Providence
  Health, John Snow Labs’ de-identification technology (part of the
  platform’s compliance toolkit) was independently certified to
  de-identify clinical notes with over **99% accuracy**, enabling **over
  1 billion patient notes** to be processed without exposing PHI. This
  “regulatory-grade” accuracy in handling sensitive data underscores the
  platform’s enterprise readiness – it can mine patient records at scale
  while strictly protecting privacy.

- **80% Cost Savings vs. GPT-4 or Azure NLP:** The solution delivers NLP
  results with far greater cost-efficiency compared to generic
  large-language-model services. Case studies have shown a **\>80%
  reduction in operational cost** when using John Snow Labs’ solution
  in-house versus cloud NLP APIs like Azure Cognitive Services or
  GPT-4o. The optimized Spark NLP pipeline processes text on commodity
  hardware or existing clusters, avoiding the pay-per-use fees of big
  cloud models. This drastically lowers the total cost of ownership for
  enterprise-scale deployments.

- **Improved Coding Precision (20–32% Uplift in RAF capture):** In
  proof-of-concept trials and deployments, healthcare organizations
  observed a **20–32% increase in HCC coding precision** after
  implementing this solution. In other words, the platform helped
  capture roughly a quarter more valid HCC codes per patient on average,
  compared to baseline manual processes. This uplift directly translates
  to higher RAF scores (and reimbursements) *without up-coding*, simply
  by **finding and validating conditions that were previously
  overlooked**. For example, West Virginia University Medicine reported
  a notable jump in HCC coding accuracy and a significant drop in missed
  codes after using the NLP system. This benchmark underscores that the
  platform not only matches human performance but in practice leads to
  materially more complete coding.

[John Snow Labs Launches Martlet.ai, Setting New Standards for Risk
Adjustment with Healthcare Large Language
Models](https://www.johnsnowlabs.com/john-snow-labs-launches-martlet-ai-setting-new-standards-for-risk-adjustment-with-healthcare-large-language-models/)

**Table: Comparison of Approaches – JSL Platform vs. Manual Review vs.
Generic NLP**

| **Aspect** | **John Snow Labs Platform** | **Manual Review** | **Generic NLP Tools** |
|----|----|----|----|
| **HCC Identification Accuracy** | ~98% F1 (expert-level) in capturing diagnoses. Few false negatives; every code linked to evidence. | Variable; human coders may miss 20–25% of conditions (e.g. omissions in charts). Accuracy can suffer under time constraints. | Moderate (often 80–90% F1). General NLP models miss clinical nuances, yielding more false negatives/positives. |
| **Throughput & Scalability** | Scales to millions of notes – distributed Spark processing with no drop in accuracy. Near real-time updates. | Very limited – one coder can review perhaps 10–20 charts per day thoroughly. Not scalable without large staff. | Faster than humans for single tasks, but **rate-limited by API throughput** and high latency for long notes. Struggles with very large volumes and long documents. |
| **Consistency & Audit Trail** | Consistent, rule-based outputs with **full audit logs** and traceability for each code. Easy export for audits (RADV/OIG). | Prone to human inconsistency; different coders may code differently. Audit prep requires manual chart collection, prone to error. | LLM outputs can be inconsistent (nondeterministic). Typically **lack detailed audit trails**; difficult to justify each extracted code to auditors. |
| **Compliance & Privacy** | Runs on secure infrastructure with **no data leaving** the organization. Proven HIPAA-compliant with third-party certification. PHI is masked in outputs. | Generally compliant if done internally, but **risk of human error** in handling sensitive data (e.g. exporting notes). Harder to ensure uniform privacy safeguards. | Cloud NLP services may send data offsite, raising HIPAA/GDPR concerns. Some models (like GPT) risk **PHI leakage** since they are not purpose-built for healthcare compliance. |
| **Cost per 1,000 Charts** | Low, fixed infrastructure cost (80% less than cloud NLP). After initial setup, high volume processing is very cost-effective. | High – requires many coder hours (labor cost), plus overhead for training/QA. Does not benefit from scale (cost grows linearly with volume). | High and unpredictable – usage-based charges (e.g. tokens or characters processed). Complex clinical language often means higher costs and additional preprocessing. |

As shown above, the John Snow Labs solution offers the best of both
worlds: **human-level accuracy with machine-level scalability**, all
while maintaining rigorous compliance and lower costs.

## **Deployment & Compliance**

John Snow Labs’ Medicare Risk Adjustment solution is designed for
**flexible deployment** in high-compliance environments:

- **Multiple Deployment Options:** It can be deployed fully
  **on-premises (on local servers or private cloud)**, in a **customer’s
  virtual private cloud**, or even in **air-gapped networks** with no
  internet access. All NLP models and components can run behind the
  healthcare organization’s firewall. This ensures that **no patient
  data ever leaves the organization’s control**, alleviating concerns
  about data security or sharing with third parties. For clients who
  prefer cloud, a managed deployment in their cloud tenancy is possible
  – but either way, the solution **does not send PHI to any external
  service** by default.

- **Integration and API Access:** Deployment includes connectors to
  common data sources: for example, FHIR APIs or HL7 feeds from EHRs,
  flat file ingestions, and JDBC for data lakes/warehouses. The platform
  provides a web UI for clinical reviewers, but also a complete **API
  layer** so that all functionality (e.g. submitting a batch of notes
  for processing, retrieving identified HCC codes, running RAF
  calculations) can be integrated into existing workflows or enterprise
  applications. This API-centric design means the solution can be added
  to the tech stack with minimal disruption, whether in a **batch
  processing context or real-time streaming** context.

- **Compliance with CMS and HHS Models:** The software fully supports
  the official CMS risk adjustment models (v24 and the newer v28 for
  Medicare Advantage) as well as the HHS-HCC model used in ACA Exchange
  plans. Updates to model coefficients or HCC mappings released by CMS
  are **incorporated in timely updates**, so customers remain compliant
  with the latest risk scoring methodology. For example, as CMS updates
  diabetes HCC definitions or adds/subtracts HCCs in version changes,
  the platform’s terminology server and logic are updated accordingly.
  This ensures **continuous alignment with regulatory requirements** for
  risk adjustment.

- **Regulatory Standards (HIPAA, GDPR, EU AI Act):** The platform was
  built with **privacy-by-design**principles. All patient identifiers
  and PHI can be automatically masked or obfuscated in the analysis
  outputs (using JSL’s de-identification models that have **99%+
  accuracy**). It complies with **HIPAA** regulations for
  de-identification and privacy, supports **GDPR** requirements (with
  capabilities like data anonymization and purpose limitation), and is
  prepared for emerging regulations like the **EU AI Act** (with
  features for transparency and human oversight of AI decisions). For
  instance, all model decisions can be explained or traced (e.g.
  highlighting the text that led to a condition being identified). The
  software also includes governance features such as access control,
  audit logging, and bias testing results to help clients ensure fair
  and responsible AI use.

- **Evidence Traceability & Annotation Layers:** Every identified
  condition is stored with metadata including context (surrounding text,
  note type, timestamps). The platform supports **annotation layers** –
  meaning that human reviewers (coders or auditors) can add their own
  notes, validations or overrides which are tracked in the system.
  Original notes are left unaltered; annotations are layered on top,
  preserving legal medical record integrity. The traceability means that
  one can easily drill down from a RAF score all the way to the source
  evidence in a note, and see who verified it. **PHI masking** is
  applied whenever data is exported or presented externally, so that no
  sensitive info is exposed in reporting. These capabilities provide
  end-to-end **transparency and governance**, which is crucial for
  internal compliance and external audit defense.

In summary, the deployment is **IT-friendly and compliant**: it can run
securely within the organization’s environment, adapt to their data
flows, and meet the strict requirements of healthcare data protection
and regulatory conformance.

## **Real-World Use Cases**

Several organizations have leveraged this solution to achieve
significant improvements in risk adjustment accuracy and efficiency:

- **WVU Medicine (Academic Health System):** West Virginia University
  Medicine implemented the platform to enhance their Medicare Advantage
  coding. By using John Snow Labs’ **Medical NLP** to review clinical
  notes, WVU identified numerous HCC diagnoses that had been missed in
  routine coding. Newly discovered codes were fed directly into their
  EHR for clinician review. As presented in their case study, WVU saw a
  **notable increase in HCC coding accuracy** and a sharp reduction in
  manual chart review time. Physicians appreciated that the tool brought
  forth specific evidence from their own notes, making it easier to
  validate and add diagnoses. This translated to more complete risk
  capture for their patient population without adding burden on
  providers – the NLP did the heavy lifting of chart combing.

- **SelectData (Coding Services Vendor):** SelectData, a company
  specializing in home health coding and revenue cycle, integrated John
  Snow Labs’ OCR and NLP into their workflow to process millions of
  patient documents. This enabled them to automatically extract
  diagnoses and key clinical indicators from both typed and handwritten
  notes. As a result, **productivity increased by 10%** and
  recommendation accuracy reached 95% in their coding operations. In
  practical terms, SelectData’s coding team could handle more charts in
  less time, and with fewer errors, by relying on the AI to flag
  relevant conditions. This case underscores how even well-trained human
  teams benefit from AI assistance to boost throughput and consistency.

[Select Data interprets millions of patient stories with deep learned
OCR and
NLP](https://www.johnsnowlabs.com/selectdata-interprets-millions-of-patient-stories-with-deep-learned-ocr-and-nlp/)

- **Providence Health (51-hospital Health System):** Providence
  undertook one of the nation’s largest de-identification and data
  mining projects using John Snow Labs’ technology. They successfully
  **de-identified over 700 million clinical notes** across their network
  (historical records), enabling these notes to be analyzed for HCCs and
  other insights without privacy risk. The John Snow Labs solution
  provided the backbone for this effort – automating PHI removal and
  then extracting conditions for population health research. Providence
  implemented rigorous multi-level validation, including third-party
  certification of the de-identification accuracy and even an external
  red-team attempt to re-identify patients, which **found zero
  breaches**. With the data rendered safe, Providence could mine years
  of clinical documentation to identify high-risk patients and
  previously uncaptured HCCs. This real-world use highlights the
  platform’s ability to operate at **unprecedented scale (hundreds of
  millions of notes)** while maintaining compliance. The outcome for
  Providence was a richer clinical data repository to support both risk
  adjustment and research, all with legal peace of mind.

These examples demonstrate the solution’s versatility – from **academic
medical centers to coding vendors to large health systems**, the
platform has proven its value in improving HCC capture, streamlining
workflows, and enabling data-driven care initiatives. Each deployment
also validated the solution’s claims about accuracy, scalability, and
compliance in real operational settings.

## **Customer Proof Points**

- **“Used by 5 of the 8 largest global pharma companies.”** John Snow
  Labs’ AI technologies (including its NLP platform) are trusted at an
  elite level – its customer base includes **half of the world’s top-10
  pharmaceutical firms**, among other major healthcare organizations.
  This broad adoption by industry leaders attests to the platform’s
  reliability and industry-leading capabilities.

- **“Preferred by over 54% of GenAI projects in healthcare at large
  enterprises.”** In a recent industry survey, a majority of large
  healthcare enterprises indicated a preference for domain-specific
  language models – in fact, **54% of respondents from big companies
  favor healthcare-specific NLP like John Snow
  Labs**[multilingual.com](https://multilingual.com/john-snow-labs-achieves-new-state-of-the-art-medical-llm-accuracy-benchmarks-outperforming-gpt-4-med-palm2-and-hundreds-of-others/#:~:text=Recent%20research%20shows%20that%20lack,optimized%20for%20healthcare%20use%20cases).
  This reflects the platform’s reputation: it is often the top choice
  for healthcare NLP tasks, outranking general AI solutions in actual
  enterprise usage.

## **Relevant Resources**

- **Webinar**: [Medical Risk Adjustment Score Use
  Case](https://www.youtube.com/watch?v=aa6PmR6pnVQ)

- **Blog:** [Transforming Medicare Risk Adjustment with Generative AI
  Lab](https://www.johnsnowlabs.com/transforming-medicare-risk-adjustment-with-generative-ai-lab)
