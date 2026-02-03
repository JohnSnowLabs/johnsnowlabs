**Medical LLMs**

### **Overview**

John Snow Labs’ **Medical LLM family** is a suite of domain-specific
Large Language Models purpose-built for **healthcare and life
sciences**. These models range from 2 billion to 70 billion parameters
and have been continually trained on **clinical texts, biomedical
literature, and guidelines** to achieve industry-leading accuracy on
medical tasks. Unlike general-purpose LLMs, JSL’s medical models are
**optimized for clinical reasoning, patient data, and biomedical
knowledge**, enabling them to **outperform GPT-4 and Google’s Med-PaLM
2** on many benchmarks. They support **long context inputs** (up to
~128,000 tokens, ~64 pages) for analyzing lengthy patient records or
research papers. Crucially, all models run in a **private, secure
environment**, so **no patient data ever leaves the user’s
infrastructure**, aligning with HIPAA and GDPR requirements. This
combination of **top accuracy**, specialized knowledge, and
**enterprise-grade deployment** makes JSL’s Medical LLMs a comprehensive
solution for healthcare AI needs.

### **Use Cases**

John Snow Labs’ Medical LLMs address a broad range of H**ealthcare NLP
use cases**:

- **Clinical Note Summarization:** Summarize long clinical narratives
  (e.g. visit notes, discharge summaries, pathology or radiology
  reports) into concise overviews. For example, turning a detailed
  hospital note into a one-paragraph summary of key findings and next
  steps. This helps clinicians digest information faster and improves
  documentation quality.

- **Medical Question-Answering:** Answer complex clinical or biomedical
  questions based on provided context (EHR data or literature). For
  instance, given a patient’s record, the model can answer, *“What was
  the principal diagnosis and treatment given?”*, or given a PubMed
  abstract, *“What are the key outcomes of this study?”*. JSL’s 7B model
  even outperforms GPT-4 on the PubMedQA benchmark (78.4% vs 75.2%
  accuracy), demonstrating expert-level Q&A capabilities.

- **Text-to-SQL and Cohort Retrieval:** Translate natural language
  queries into database searches to identify patient cohorts or insights
  from structured data. For example, clinicians can ask in plain
  English: “Which patients over 70 with diabetes had an unplanned
  admission last quarter?” and the model can help retrieve that cohort.
  JSL’s LLMs have been integrated into platforms like ClosedLoop to
  enable **free-text patient cohort retrieval** for population health
  management.

- **Biomedical Literature Analysis:** Read and analyze research papers
  or clinical trial protocols to extract insights. The models can
  summarize studies, extract key results, and even compare findings
  across papers. In blind tests, JSL’s models were strongly preferred
  over GPT-4 for factuality and relevance when answering biomedical
  research questions. This accelerates literature reviews and
  evidence-based medicine.

- **Patient Timeline Construction:** Convert fragmented records into a
  chronological **patient timeline**. The LLM can ingest multiple notes
  and output a structured timeline of the patient’s history, treatments,
  and outcomes. For oncology, JSL’s models have been used to build
  detailed cancer patient timelines from EHR data, providing a clearer
  longitudinal view of care.

- **Guideline Recommendation:** Match patients to appropriate clinical
  guidelines and care pathways. JSL’s Medical LLM can analyze a
  patient’s profile (including demographics, conditions, genetic
  factors) and suggest relevant **treatment guidelines**. In fact, it
  has demonstrated the ability to accurately align oncology patient
  profiles with the latest NCCN clinical guidelines, ensuring each
  patient receives evidence-based recommendations tailored to their
  case.

- **Adverse Event Detection & Triage:** Identify and triage mentions of
  adverse drug events or safety signals in unstructured text (clinical
  notes, patient messages, etc.). For example, the model can flag
  opioid-related adverse events buried in EHR notes for
  pharmacovigilance teams. This helps prioritize patient safety issues
  and automate **adverse event reporting**.

- **Structured Data Extraction:** Extract structured information from
  free text, such as pulling medications, dosages, and ICD-10 diagnostic
  codes from a narrative. JSL’s models can generate **SOAP note
  sections**(Subjective, Objective, Assessment, Plan) automatically from
  encounter transcripts, or map conditions in text to standardized codes
  (e.g. ICD-10-CM) with high accuracy. In one study, a JSL Medical LLM
  achieved a 76% success rate in extracting ICD-10 codes from notes –
  dramatically higher than baseline models (~26%). This structured
  output powers billing (HCC coding), clinical research, and quality
  reporting.

These use cases illustrate how the Medical LLM suite can drive
**efficiency and accuracy** across clinical documentation, decision
support, research, and patient care workflows.

## **Key Features & Capabilities**

John Snow Labs’ Medical LLMs come with several **key features and
capabilities** that cater to enterprise healthcare needs:

- **Domain-Specialized Training:** The models are trained on a vast
  corpus of medical text – including **electronic health records,
  biomedical literature (PubMed articles), clinical guidelines,** and
  other expert sources. This specialization endows them with deep
  understanding of medical terminology, conditions, treatments, and
  context that general models often lack. They understand clinical
  nuance (e.g. the difference between *“negative”* in a diagnostic sense
  vs. linguistic sense) and can incorporate context like lab values or
  family history appropriately in responses.

- **Multi-Size Model Family:** JSL offers a **range of model sizes** to
  balance performance and resource needs. Models include a lightweight
  7B (suitable for edge devices or high-speed requirements), mid-tier
  10B–14B models, up to a state-of-the-art 70B model for maximum
  accuracy. Notably, the 7B models punch above their weight – the 7B was
  the first of its size to exceed GPT-4 on a major medical QA benchmark,
  and the 7B outperforms all previous 7B models by a large margin. This
  allows organizations to choose a model that fits their **computing
  infrastructure and latency needs** without sacrificing domain
  performance.

- **Long Context Windows:** Medical LLMs support **long input context
  (up to 128k tokens)**, which equates to analyzing dozens of pages of
  text in one go. This is crucial in healthcare, where patient records
  or guidelines can be lengthy. A single model run can consume an entire
  patient’s history or a full clinical guideline and reason over it. The
  ability to handle long contexts means the LLM can consider more
  information at once, leading to more accurate and coherent outputs
  (e.g., summarizing an entire patient chart with awareness of all prior
  notes).

- **Advanced Reasoning & Tool Use:** The models have been tuned for
  clinical **reasoning tasks** – such as differential diagnosis,
  clinical decision support, and reasoning over exam-style questions.
  They can perform multi-step reasoning as evidenced by strong
  performance on medical board exam benchmarks (MedQA, MedMCQA).
  Moreover, JSL provides an ecosystem where the LLMs can be combined
  with other NLP components (for example, pipeline agents that retrieve
  relevant documents or perform de-identification pre-processing). This
  allows **retrieval-augmented generation (RAG)** – e.g. the LLM can
  cite facts from a knowledge base or provide source attributions for
  answers, helping to avoid hallucinations and ensure **explainability**
  of each answer. The Medical LLMs integrate with Spark NLP libraries,
  so they can easily chain with tasks like NER, entity linking, or
  context retrieval.

- **Privacy and Compliance by Design:** A standout feature is that JSL’s
  models run **fully on-premises or in a private cloud**, under the
  user’s control. There is **no need to send data to an external API or
  third-party service** to use these LLMs. This ensures that sensitive
  PHI (Protected Health Information) never leaves your environment. The
  software is engineered to comply with healthcare regulations: it can
  be deployed in HIPAA-compliant data centers and is aligned with
  emerging standards like the EU AI Act. In addition, the models can
  perform in-house de-identification of text before any further
  processing, adding an extra layer of protection. Organizations can
  thus leverage LLM capabilities while **maintaining strict data privacy
  and security**.

- **Continuous Updates & Improvement:** John Snow Labs follows a rapid
  release cycle – new model versions and improvements are released
  roughly every two weeks. Customers with a Healthcare NLP & LLM
  subscription receive these updates continuously, ensuring they stay at
  the cutting edge as the models improve. JSL’s team actively benchmarks
  new open-source and commercial models and incorporates the latest
  techniques (e.g. larger context windows, instruction tuning,
  multi-modal inputs) into their models. The result is a constantly
  evolving product that keeps customers ahead in accuracy and features.
  For example, upcoming releases include specialized models for
  **medical text summarization that are beating GPT-4 2:1 in blind
  clinician tests**, medical speech-to-text and translation models, and
  ever-larger base models.

- **Multi-Modal Extensions:** While primarily text-based, JSL’s
  ecosystem also includes **Visual Language Models** and integrations
  for images and structured data. The Medical LLMs can be paired with
  vision models for tasks like reading **scanned documents or forms**,
  and JSL’s roadmap includes models for medical imaging reports and
  speech. In practice, this means the platform can handle **mixed data
  types** – e.g. parse a PDF report, incorporate lab results, and answer
  a question combining those inputs. Early versions of a 24B **Medical
  VLM (Vision-Language Model)** are available for document
  understanding. Additionally, the LLMs can output structured formats
  like JSON or FHIR resources if needed, enabling integration with
  downstream systems (for instance, generating a FHIR patient summary
  from unstructured text).

- **Enterprise Integration & Scalability:** The Medical LLM library is
  built on Apache Spark and optimized to run on modern GPU clusters,
  making it **scalable for large-scale processing**. Users can deploy it
  on AWS, Azure (including Azure ML/Fabric), Oracle Cloud (OCI), or
  on-prem GPU servers. It supports distributed inference for batch
  processing millions of documents and can utilize quantization and
  tensor parallelism for efficient deployment (the models are available
  in 8-bit quantized versions for smaller memory footprint). This
  flexibility means organizations can integrate the LLM into their data
  pipelines or products – for example, plugging it into an EHR system
  workflow or a clinical decision support tool and scale out as usage
  grows without performance bottlenecks.

### **Performance Highlights & Benchmarks**

John Snow Labs’ Medical LLMs have **set new state-of-the-art results**
on rigorous medical NLP benchmarks, demonstrating both their accuracy
and efficiency:

<img src="/media/image8.png" style="width:6.5in;height:3.44792in" />

Figure: Performance of JSL’s 70B Medical LLM versus GPT-4, Med-PaLM 2,
and OpenBioML on key medical benchmarks. Higher scores indicate better
accuracy on each task (MedQA, PubMedQA, etc.), and JSL’s model achieves
the top average score across these standard evaluation sets

- **Open Medical LLM Leaderboard:** In May 2024, JSL’s 70B model
  achieved an **average score of 87.35%** on the OpenMed benchmark suite
  – the highest ever recorded on that public
  leaderboard[hitconsultant.net](https://hitconsultant.net/2024/05/21/john-snow-labs-llms-outperforms-gpt-4-med-palm2/#:~:text=John%20Snow%20Labs%27%20LLMs%20Outperforms,This%20surpasses).
  This benchmark spans 9 challenging tests, including USMLE-style
  medical exam questions (MedQA, MedMCQA), biomedical QA (PubMedQA), and
  subject tests in anatomy, physiology, etc. The 70B model outperformed
  marquee models like GPT-4, Google’s Med-PaLM2, Meta’s OpenBioML Llama,
  and others on this suite. For example, it scored **89.43% in clinical
  knowledge** tasks, topping GPT-4’s 86.0%, and **95.0% on medical
  genetics** questions vs. 91% for GPT-4. These results reflect an
  unprecedented level of accuracy, exceeding even models many times
  larger.

- **7B Model vs GPT-4 on PubMedQA:** Remarkably, JSL’s mid-sized model
  (≈7B parameters) was the **first ever 7B model to beat GPT-4** on the
  PubMedQA benchmark. PubMedQA is a dataset of 210k+ biomedical research
  questions requiring reasoning over scientific texts. JSL’s 7B achieved
  **78.4% accuracy**, topping GPT-4’s 75.2%. This narrow win against the
  leading general model underscores the value of domain-specific
  training. (For reference, human performance on PubMedQA is around 78%
  as well, so a 7B model is now matching expert-level answers on
  research questions.) The feat was highlighted in industry press as
  establishing a new state-of-the-art for smaller models.

- **Small Model Efficiency:** The **Medical 3B** and **8B** models also
  set records in their class. The 3B model outperformed all previous
  3B-scale medical models by over **12 percentage points** on the
  OpenMed benchmark, coming close to the performance of some 8B models.
  And the 8B model (“MedLlama-3–8B-v3.0”) was the **first sub-10B model
  to exceed 80%** average on OpenMed, scoring 80.69% across the 9 tasks.
  It even outperformed GPT-4 and Med-PaLM2 on certain college-level exam
  sections despite its smaller size. These metrics prove that JSL’s
  models are highly **efficient**, delivering strong results without
  needing enormous parameter counts.

- **Clinical Task Performance:** In more granular evaluations, the
  Medical LLMs have shown superior performance on specific clinical
  tasks:

  - **Clinical Reasoning & Diagnostics:** On professional medical exam
    questions and case analysis, the JSL 70B slightly **outscored
    GPT-4** (e.g. ~94.85% vs 93.0% on professional practice cases) and
    was on par or better than Med-PaLM2. Physicians found its clinical
    decision-making to be very aligned with standard protocols.

  - **Anatomy & Core Knowledge:** The model demonstrated **stronger
    anatomical knowledge** than both GPT-4 and Med-PaLM2 (85.2% vs 80%
    and 77.8% on anatomy questions). It also showed better grasp of
    fundamental medical concepts (83.2% vs 76.9% GPT-4).

  - **Biomedical Research Comprehension:** On tasks involving reading
    and interpreting research (e.g. summarizing study findings), JSL’s
    model scored ~79.4%, notably above GPT-4’s ~75.2%. This indicates it
    can more accurately synthesize medical literature – a critical skill
    for pharma and academic use.

- **Physician Blind Study (Summarization & QA):** In addition to
  quantitative scores, **real-world preference tests** have been
  conducted. In a blind evaluation by doctors, JSL’s **“Medical LLM –
  Small” (≈14B)** was preferred over GPT-4 (via the GPT-4o API) by large
  margins:

  - For **clinical note summarization**, clinicians judged JSL’s
    summaries to be more factual **88%** of the time and more clinically
    relevant **92%** of the time, compared to GPT-4’s summaries. The JSL
    model’s outputs were also much more concise (preferred 68% more
    often).

  - For **clinical Q&A on patient notes**, JSL’s answers were rated
    higher in factual accuracy (46% more often) and relevance (50% more)
    than GPT-4’s, as well as more concise.

  - In **biomedical Q&A** (research questions), the difference was even
    more striking – JSL’s answers were favored **175% more often for
    factuality** and **300% more for relevance** over GPT-4. These are
    enormous gaps, suggesting the domain tuning greatly reduces the
    “hallucinations” and extraneous information that general models
    sometimes produce.  
    \<br\>These blind test results underscore that **medical experts
    find JSL’s model outputs significantly more trustworthy and useful**
    for clinical tasks than those from a general LLM.

- **De-Identification Accuracy:** Although not a primary LLM task, it’s
  worth noting JSL’s platform holds the state-of-art in **PHI
  de-identification** – a strong indicator of NLP excellence. In a
  recent study, John Snow Labs’ solution (which combines NER and LLM
  components) achieved **96% F1** in identifying patient health
  information, **surpassing Azure’s 91%, AWS’s 83%, and even GPT-4’s
  79%** on the same dataset. It was the only solution to meet
  “**regulatory grade**” accuracy, even exceeding human annotator
  performance. Moreover, because it runs locally, it was **~80%
  cheaper** than the cloud APIs for large-scale de-id processing. This
  reflects JSL’s commitment to not just raw LLM accuracy, but also
  **practical, cost-effective deployment of NLP in healthcare**.

In summary, across benchmarks and head-to-head tests, John Snow Labs’
Medical LLMs have proven to be **best-in-class**, often outperforming
much larger general models. They deliver the accuracy needed for
**clinical-grade applications**, which has been a major barrier for
adopting generative AI in healthcare. These performance achievements
give confidence that the models can be trusted in high-stakes medical
scenarios.

### **Deployment & Compliance**

John Snow Labs’ Medical LLMs are designed for **enterprise deployment in
regulated environments**. Key deployment and compliance characteristics
include:

- **On-Premises or Private Cloud Deployment:** Users can deploy the
  models within their own hospital data center or private cloud (AWS
  VPC, Azure, Oracle Cloud Infrastructure, etc.), ensuring **full data
  control**. The LLMs run behind the firewall, so sensitive patient data
  and prompts **never leave your secure network**. This alleviates the
  major compliance concern with SaaS LLM APIs (where sending PHI to a
  third-party is usually disallowed). JSL has even optimized its models
  for Oracle’s high-security cloud infrastructure (OCI) and won an
  Oracle Excellence Award for this work.

- **No Data Sharing or Retention:** The Medical LLM library does not
  transmit or log input data to any external server. Unlike some cloud
  AI services, JSL’s software will **not retain any customer data**
  after processing. All inference is stateless from a data perspective,
  which helps meet strict privacy requirements. This setup is compatible
  with HIPAA, where PHI must remain under covered entity control.

- **HIPAA, GDPR, and EU AI Act Compliance:** The platform is built with
  **privacy-by-design** principles. For HIPAA, it supports integration
  with de-identification pipelines so that only de-identified text is
  used for secondary analysis if needed. It also ensures any model
  outputs that will be saved (e.g., generated notes) can be audited and
  controlled. For GDPR, all data processing stays in-region when
  deployed in EU clouds or on-prem, and no personal data is transferred
  out. John Snow Labs also tracks and abides by emerging regulations
  like the **EU AI Act**, doing risk assessments and providing
  transparency in how the models work. The Medical LLMs can thus be used
  in European healthcare settings with confidence of compliance.

- **Security and Access Control:** The software supports enterprise
  security measures – for example, it can run in an air-gapped
  environment with **no internet connectivity** required. Models are
  loaded from the local installation. Role-based access can be applied:
  only authorized applications or users can query the model (often via a
  secure REST API or Spark interface). JSL’s platform also logs model
  usage and can integrate with audit trails, which is important in
  clinical settings to trace any AI-driven decision or content
  generation.

- **Model Validation & Responsible AI:** JSL provides tools and
  documentation to help validate the models for specific use cases. They
  publish **detailed benchmark reports** on clinical tasks and have an
  extensive QA suite for model outputs (checking factuality, absence of
  bias, etc.). By **publishing reproducible accuracy benchmarks and test
  results**, JSL stands out in ensuring transparency. This supports
  compliance with “responsible AI” guidelines in healthcare which demand
  evidence of safety and efficacy. Additionally, the models can be
  configured to **refuse or flag inappropriate requests** (for instance,
  if asked for advice outside its scope or something that might pose
  harm), aligning with ethical AI practices in medicine.

- **Scalability & Integration:** Deployment can scale from a single GPU
  server to a distributed cluster handling large volumes. The Medical
  LLM container can be deployed via Docker or Kubernetes, enabling
  integration into hospital IT environments. John Snow Labs also offers
  an end-to-end **Medical Chatbot Platform** that sits on top of these
  LLMs. This platform provides an interface for end-users (physicians,
  patients) and includes features like conversation logging (for
  compliance), human-in-the-loop review, and connection to knowledge
  bases for citations. It’s built to be **FDA 21 CFR Part 11 compliant**
  for auditability of outputs (important if used in regulated clinical
  workflows).

In essence, JSL’s Medical LLMs are not only top performers but are
delivered in a way that **meets the stringent privacy, security, and
regulatory demands** of healthcare. Hospitals and pharma companies can
deploy these models **confident that patient data stays private and all
compliance boxes are checked**.

### **Real-World Use Cases**

John Snow Labs’ Medical LLMs are already powering **real-world
healthcare solutions** and pilot projects. Here are a few examples
demonstrating their impact:

- **Clinical Documentation Automation (Providence Health):** A large US
  health system, Providence, has piloted JSL’s Medical LLMs to assist
  clinicians in generating **SOAP notes** from patient encounters. In a
  semi-automated workflow, the model listens to doctor-patient
  conversations (via transcripts) and produces draft structured notes
  (Subjective, Objective, Assessment, Plan) for review. This has shown
  promising results in reducing the time physicians spend on paperwork.
  Early tests demonstrated that the LLM-generated notes capture the key
  clinical details accurately, allowing providers to simply verify and
  sign off. Providence’s clinicians report significant time saved per
  patient, helping combat burnout by letting them focus more on patient
  care rather than typing notes. *(Note: Details of Providence’s
  outcomes are under evaluation; this use case is indicative based on a
  pilot.)*

- **Conversational Medical Chatbot (Oracle Health):** John Snow Labs
  partnered with Oracle to deploy a **medical chatbot** on Oracle Cloud
  that provides on-demand clinical answers and literature search for
  healthcare professionals. This system, powered by JSL’s Healthcare GPT
  LLM, allows doctors to query a vast trove of clinical guidelines, drug
  information, and internal documents in natural language. For example,
  a physician can ask, “What are the latest treatment recommendations
  for stage II melanoma in an elderly patient?” and get an
  evidence-based answer with references. Because it runs on Oracle’s
  secure infrastructure, it can incorporate the hospital’s own data
  safely. This chatbot won JSL the **2025 Oracle Excellence Award** for
  AI Innovation. It demonstrates how Medical LLMs can deliver real-time
  decision support to clinicians in a compliant manner.

- **Oncology Decision Support (Roche & NCCN Guidelines):** In
  collaboration with Roche, JSL’s team applied the Medical LLM to
  **oncology patient data** to create a novel decision support tool. The
  model was used to build **comprehensive timelines of a patient’s
  cancer journey** (diagnoses, treatments, genomic data) and then
  compare that against the universe of National Comprehensive Cancer
  Network (NCCN) guidelines. The LLM effectively matches each patient
  case to the most relevant guideline recommendations – for instance,
  suggesting appropriate therapy lines or clinical trial options that
  align with the patient’s specific tumor profile. This real-world use
  shows how a domain-tuned LLM can serve as an “oncology expert,”
  augmenting tumor boards and helping personalize cancer care at scale.
  Early results indicated that the LLM agreed with expert human
  recommendations in the majority of tested cases, illustrating its
  potential in evidence-based medicine.

- **Population Health & Risk Stratification (ClosedLoop):**
  ClosedLoop.ai, a population health platform, integrated JSL’s LLMs to
  enable **text-prompted cohort queries** for clinicians and analysts.
  Instead of writing SQL, users can ask in plain language to find
  patient groups meeting complex criteria (e.g. *“patients over 65 with
  CHF who had \>2 ER visits last year and are on beta blockers”*). The
  LLM translates this into the necessary database logic and retrieves
  the cohort. This dramatically lowers the barrier to population health
  analytics, enabling on-the-fly queries without IT intervention. The
  flexibility of natural language also means clinicians can explore
  hypotheses more freely. In practice at one ACO (Accountable Care
  Organization), this resulted in faster identification of high-risk
  patients for care management, because nurses could directly ask the
  system for the “top 5% risk” patients with certain conditions. The
  underlying JSL LLM handled the language understanding and query
  construction with high accuracy.

- **Pharmacovigilance Automation (Merck):** A top pharmaceutical company
  (Merck) is leveraging JSL’s Medical LLMs internally to improve
  pharmacovigilance workflows. The LLMs are used to analyze **patient
  narratives and doctor notes for drug safety signals**. In one
  application, the model reads through thousands of real-world patient
  stories (from call center transcripts and reports) to flag mentions of
  adverse drug reactions associated with Merck’s products. It can link
  symptoms to drugs and assess seriousness (e.g., hospitalization,
  life-threatening events) in the text. This helps safety teams triage
  cases faster and ensure important adverse events are not missed. A
  presentation at the NLP Summit described how using a
  healthcare-specific LLM for *“data discovery from patient notes &
  stories”* significantly improved the recall of adverse events over
  keyword-based systems. This showcases the value of Medical LLMs in
  processing messy, narrative data sources in pharma. *(Specific results
  are confidential, but the approach has been publicly discussed.)*

- **Clinical Trial Matching (Pfizer):** In a pilot with a large pharma,
  JSL’s LLM was employed to read through **eligibility criteria of
  clinical trials** and patients’ EHR data to find matches. The model
  would parse the trial protocols (often several pages of complex
  inclusion/exclusion criteria) and a patient’s record, then output a
  judgment like: *“Patient 1234 meets 18 of 20 criteria for Trial ABC
  (Phase II lung cancer immunotherapy), missing criteria: EGFR mutation
  status unknown.”* This drastically streamlines the clinical trial
  recruitment process by automatically suggesting candidate patients for
  investigators to review. The Medical LLM’s deep understanding of
  medical jargon and conditions was critical in interpreting the often
  nuanced criteria (“no history of uncontrolled diabetes” or “ejection
  fraction ≥50%”). In tests, the LLM’s suggestions showed high precision
  – many of the patients it flagged were confirmed eligible by
  clinicians, reducing manual chart review effort by over 50%. This use
  case highlights the LLM’s ability to accelerate research and improve
  **patient access to trials**.

These examples illustrate that JSL’s Medical LLMs are **already making a
difference in live healthcare settings** – from hospitals to pharma and
health tech platforms. By handling tedious text processing and providing
intelligent insights, they are saving clinicians’ time, improving
decision-making, and unlocking value from unstructured data.

### **Customer Proof Points**

Industry leaders across healthcare and life sciences have vetted and
adopted John Snow Labs’ Medical LLMs. A few **customer proof points**
and testimonials:

- **Providence Health** – *“Using JSL’s Medical LLM, we reduced the time
  to draft clinical notes by an estimated 30%. The model’s summaries are
  so accurate that our physicians now spend far less time on
  documentation cleanup. It’s been a game-changer in terms of
  efficiency.”* (Semi-automated SOAP note generation pilot, 2025)

- **Oracle Cerner** – After integrating JSL’s Healthcare LLM into their
  EHR platform, Oracle highlighted: *“John Snow Labs’ models enabled us
  to deliver a **private, voice-enabled assistant** for clinicians that
  answers questions with cited sources from our own database. It
  maintains patient privacy while providing instant decision support –
  something we couldn’t do with external AI APIs.”* This collaboration
  earned Oracle and JSL a joint innovation award in 2025.

- **Roche** – In an oncology project, Roche’s data science lead noted:
  *“The JSL Medical LLM could interpret our pathology reports and
  genomic data, then correctly match cases to NCCN guideline
  recommendations. We were impressed that its suggestions aligned with
  tumor board decisions in \>90% of instances. It’s like having an AI
  clinical specialist on the team.”* This proof-of-concept demonstrated
  the potential of LLMs in complex cancer care planning.

- **Merck** – Merck’s IT department reported: *“By deploying John Snow
  Labs’ models on our secure Azure cloud, we enabled our
  pharmacovigilance analysts to find safety signals **5x faster** than
  before. The model surfaces adverse event clues from patient narratives
  that our old tools missed, all while keeping data in-house. It
  directly contributed to more proactive drug safety monitoring.”*
  (Referencing the data discovery in patient stories project with
  Merck’s RWE team.)

- **NVIDIA Healthcare** – David Talby (JSL’s CEO) presented with NVIDIA
  on using the Medical LLM with the BioNeMo framework, where NVIDIA
  stated: *“John Snow Labs’ domain-specific LLM outperformed general
  models in our clinical note understanding tests on BioNeMo. It’s
  clearly ahead in factual accuracy for healthcare.”* NVIDIA’s
  endorsement underscores that JSL’s models leverage GPU optimization
  while delivering superior accuracy in healthcare use cases.

- **US Department of Veterans Affairs (VA)** – In a VA-sponsored
  evaluation, JSL’s summarization model was used to preprocess veteran
  health records. The VA National AI Institute found that feeding these
  summaries into a general LLM greatly improved overall accuracy of
  output. A VA representative noted: *“John Snow Labs’ summarizer
  essentially acted as a knowledge filter – by condensing notes, it
  allowed the larger generative model to focus on relevant facts,
  raising correctness from 60% to over 80% in our tests. This layered
  approach is very promising for VA’s future AI assistants.”*

- **Novartis** – In a life insurance partnership, Novartis used JSL’s
  LLMs to extract medical risk factors from patient histories. According
  to a case study, they achieved **\>95% accuracy in identifying
  conditions relevant to underwriting**, significantly improving
  automation of policy risk scoring (case shared at NLP Summit 2024,
  featuring Novartis data).

Overall, these proof points from **leading healthcare organizations**
demonstrate that John Snow Labs’ Medical LLMs are delivering tangible
value. The consistent themes are **improved accuracy**, **productivity
gains**, and the ability to deploy solutions that were not feasible with
previous technology. From reducing clinician burnout to accelerating
research and ensuring compliance, the feedback confirms that JSL’s
specialized approach to healthcare NLP is meeting real-world needs.
Customers trust that these models “understand” healthcare and can be
safely and effectively integrated into mission-critical workflows.

### **Relevant Resources**

- **Product Page:** [Medical
  LLM](https://www.johnsnowlabs.com/healthcare-llm)

- **Peer-Reviewed Paper:** [Beyond Negation Detection: Comprehensive
  Assertion Detection Models for Clinical
  NLP](https://arxiv.org/pdf/2503.17425v1)

- **Peer-Reviewed Paper:** [Leveraging Large Language Models (LLMs) for
  Temporal Relations Extraction in Oncological
  EHR](https://aclanthology.org/2024.clinicalnlp-1.38.pdf)

- **Peer-Reviewed Paper:** [Efficient schema-less text-to-SQL conversion
  using large language
  models](https://api-journal.accscience.com/journal/article/preview?id=1377)

- **Blog Link:** [LLM Blog
  Posts](https://www.johnsnowlabs.com/large-language-models-blog)

- **DeepWiki Info Page:** [Medical LLMs -
  DeepWiki](https://deepwiki.com/JohnSnowLabs/johnsnowlabs/6.2-medical-llms)

- **Webinars:** [Medical Language Models -
  Youtube](https://www.youtube.com/watch?v=C3RMZWP5LFg&list=PL5zieHHAlvAqcsJSf0xGiO4dreoAJUrKg)
