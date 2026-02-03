**Visual NLP**

**Overview of Visual NLP Capabilities**

John Snow Labs’ **Visual NLP** platform is a comprehensive solution for
**visual document understanding**. It extends Natural Language
Processing to images and scanned documents, combining computer vision
(CV) and NLP in unified pipelines. Key capabilities of the Visual NLP
platform include:

- **Optical Character Recognition (OCR) & Layout Analysis:**
  High-accuracy text detection and extraction from images, PDFs, and
  DICOM files. The OCR engine supports multiple languages (English,
  German, French, Spanish, Russian, Vietnamese, Arabic) and handles
  complex layouts (columns, tables, forms). Advanced image
  pre-processing (denoising, skew correction) and layout analysis
  improve recognition results.

- **Visual Named Entity Recognition (NER):** Detection of entities
  (e.g., patient names, dates, medical terms) directly on scanned
  documents and forms. Layout-aware NER models consider the positioning
  of text in the document for context. This enables identifying and
  labeling key information in context (e.g., identifying PHI in a
  medical form or lab report image). Visual NLP has superior accuracy
  when compared to cloud providers\[[blogpost
  link](https://medium.com/p/75f6fbf1ae5f)\].

- **Image-based Document Classification:** Classify documents based on
  visual content and layout. For example, automatically distinguish
  between different document types like invoices or letters, using both
  textual and visual features. This helps route and process documents
  appropriately in workflows.

- **Visual Question Answering (VQA):** Answer questions about the
  content of an image or document. The platform can combine OCR and
  language models to enable queries like *“What is the patient’s name on
  this form?”* or *“What is the phone number present in the document?”*,
  returning answers derived from the visual text. Currently, only
  extractive VQA is supported, this means the answers are textually
  present in the document. For abstractive VQA check the VLM offerings.

- **Table and Form Structure Parsing:** Detect and extract structured
  data from tables and forms in scanned documents. Visual NLP can find
  table boundaries, identify rows/columns, and extract cell contents
  into structured formats. It similarly can detect form fields (like
  boxes, lines, or entry blanks) and associate recognized text with
  specific form labels. This enables automated parsing of lab result
  tables, admission forms, etc., into usable data.

- **Image & PDF De-Identification:** Automated **OCR-based
  de-identification** of sensitive data in images, scanned PDFs, and
  medical images (DICOM). The platform locates Protected Health
  Information (PHI) in both **text overlays** (e.g. burned-in patient
  name on an x-ray) and **image metadata**, then redacts or replaces
  that information. This process protects patient privacy in compliance
  with HIPAA while preserving the rest of the image for analysis.
  [De-identifying Whole Slide Images with Visual NLP – Part
  1](https://www.johnsnowlabs.com/what-to-know-before-de-identifying-whole-slide-images-wsi/#:~:text=Discover%20the%20low,focused%20healthcare%20AI%20workflows)
  \[I would put this link in the ‘pathology’ section\]

- **Multimodal Pipelines:** Support for **combined image and text
  processing pipelines**. Visual NLP seamlessly integrates with John
  Snow Labs’ text NLP libraries, allowing multi-step workflows (e.g.,
  classify a document image, OCR its text, then apply NLP models on the
  extracted text) all within one pipeline. It enables **computer
  vision + NLP** use cases, such as finding a signature in a form image
  and then running NER on the recognized text. This multimodal approach
  ensures that insights from both visual layout and textual content are
  leveraged together.

- **Obfuscation:** this feature extends de-identification by not only
  detecting PHI elements in documents, but also, creating forged
  versions of the original document with fake PHI elements. This means
  that, for example, patient names in the source record will be mapped
  to pseudonyms in the output record.

New documents are created considering,

<u>Coherence:</u> All this process is performed using coherent mappings,
for example, for ids, it means that existing relationships among the
original ids remain valid among the pseudonymized ids. This maintains
the possibility of researchers to establish relationships using these
ids while at the same time preserving confidentiality.

<u>Rendering Awareness:</u> The selection of the pseudonymized entities
is performed in a way that matches the style and aspect of the original
source document.

- **Pathology Image Deidentification:** this involves the
  de-identification of Whole Slide Images(WSI) both in the form of SVS
  and Dicom files. This feature deals with the de-identification of
  every image involved in WSI such as label, macro, and the different
  zoom levels involved, as well as the metadata tags which may contain
  PHI.

Pathology Images are typically high resolution, making it very hard for
ML models to be applied on them. Visual-NLP introduces specialized
techniques to enable ML pipelines run over these big images.

*(Visual NLP is built on Apache Spark, so all these capabilities scale
to large datasets and can be used in distributed pipelines. Each
component – OCR, detection, NER, etc. – is trainable and can be
customized for specific document types, as described later.)*

## **Key Differentiators and Platform Advantages**

John Snow Labs’ Visual NLP platform offers several **unique advantages**
over other OCR or NLP solutions. These differentiators help address
enterprise requirements around privacy, scale, accuracy, and
flexibility:

- **Privacy and On‑Premise Deployment:** All processing can be done
  **securely within the customer’s environment**, without sending data
  to external APIs. This is crucial for sensitive healthcare data.
  Visual NLP can run on-premises or in a private cloud, ensuring full
  control of PHI and compliance with privacy regulations. (John Snow
  Labs’ de-identification meets HIPAA Safe Harbor and GDPR anonymization
  standards, and the software does not require an internet connection
  for core functionality.) By contrast, many cloud OCR or NLP services
  require data to leave the hospital’s network. [John Snow Labs Blog,
  “Consistent Linking, Tokenization, and Obfuscation for
  Regulatory-Grade De-Identification”
  (2025)](https://www.johnsnowlabs.com/consistent-linking-tokenization-and-obfuscation-for-regulatory-grade-de-identification/#:~:text=gender%2C%20temporal%20accuracy%2C%20and%20semantic,Safe%20Harbor%20and%20GDPR%20anonymization)

- **Regulatory Compliance Built-In:** The platform is designed for
  **healthcare and life sciences** use cases, with out-of-the-box
  support for HIPAA and GDPR compliance. For example, its
  de-identification algorithms can remove all 18 HIPAA identifiers and
  produce audit logs or annotated outputs demonstrating compliance. This
  “regulatory-grade” focus means organizations can trust the tool for
  patient data without needing additional custom validation.

- **Scalability and Performance:** Visual NLP is built on Apache Spark,
  enabling **distributed processing** of large image and document
  collections. It can scale out to clusters of machines and utilize GPUs
  for acceleration. This architecture has been proven in production
  (e.g., processing hundreds of thousands of documents per day). In one
  benchmark, the system de-identified 500,000 clinical notes in ~2.5
  hours on a 15-node
  cluster[nlpsummit.org](https://www.nlpsummit.org/lessons-learned-de-identifying-700-million-patient-notes-with-spark-nlp/#:~:text=and%20500K%20patient%20notes%20,GB%20memory%2C%201%20GPU%2C%205DBU)
  – illustrating the throughput possible for visual pipelines. The
  ability to handle big data volumes efficiently is a key advantage over
  single-machine or cloud API solutions. [NLP Summit - Lessons Learned
  De-Identifying 700 Million Patient Notes with Spark
  NLP](https://www.nlpsummit.org/lessons-learned-de-identifying-700-million-patient-notes-with-spark-nlp/#:~:text=and%20500K%20patient%20notes%20,GB%20memory%2C%201%20GPU%2C%205DBU)

- **State-of-the-Art Accuracy:** The Visual NLP platform leverages
  **pre-trained models and transfer learning** from John Snow Labs’
  Healthcare NLP library, yielding best-in-class accuracy on clinical
  document tasks. In a recent peer-reviewed benchmark, John Snow Labs’
  solution achieved **96% F1-score** in PHI identification,
  outperforming Azure (91% F1), AWS (83%), and OpenAI GPT-4-based
  methods (79%). This superior accuracy – exceeding even human
  annotators in some cases – ensures that sales reps can confidently
  tout the platform’s quality. High precision and recall mean fewer
  missed entities and false positives, a critical factor for healthcare
  clients.

- **Adaptability and Customization:** Unlike black-box cloud services,
  Visual NLP is **fully customizable**. Users can modify pipelines, add
  or remove processing stages, and fine-tune models to their specific
  documents. For example, a hospital can adjust the de-identification
  pipeline to preserve certain medically relevant terms or train a new
  Visual NER model for a specialized form. This adaptability is a
  crucial advantage – the platform can be tailored to each project’s
  needs, whereas many competitors offer one-size-fits-all APIs. The
  ability to train custom OCR models or NER models on proprietary data
  (using the included libraries and Annotation Lab) is a strong selling
  point for enterprise AI teams.

- **Multi-Language & Multi-Format Support:** Visual NLP isn’t limited to
  English or to a single document format. The OCR component supports
  dozens of languages out of the box, which is important for global
  organizations or documents in non-English languages (e.g., French
  clinical notes or Spanish intake forms). The platform also handles a
  variety of file formats – from standard images (JPEG, PNG) and scanned
  PDFs to TIFF slides and DICOM radiology files – all within one unified
  framework. Competing solutions may require separate tools or add-ons
  for different formats (for instance, specialized tools for DICOM).
  With Visual NLP, the same platform covers all, simplifying deployment.
  It’s important to highlight that most of the Visual NLP platform is
  Java based which is way superior in terms of dependency management
  compared to Python.

- **Deterministic Tokenization & Consistent Pseudonymization:** John
  Snow Labs provides **deterministic tokenization and linking**
  techniques to ensure consistency across data. This means that the same
  identifier (e.g., a patient ID or name) will be transformed the same
  way every time across documents and modalities. For example, if a
  patient’s name appears in a text report and on a DICOM scan, the
  de-identification pipeline can replace both with the *same* fictitious
  name or token, maintaining **referential integrity** across datasets.

Competitors typically lack this level of cross-modal consistency. This
feature is critical for longitudinal analysis – it lets researchers link
records without exposing true identities. It’s an advantage that
resonates with customers needing **longitudinal data de-identification**
and re-linking capabilities.

- **Hardware Optimization and Speed:** The Visual NLP library is
  optimized for modern hardware. It can leverage GPUs for deep learning
  OCR and image processing and is optimized with Apache Spark for
  parallel CPU use. This yields **fast inference** even on large images
  or multi-page PDFs. Internal benchmarks have shown that Visual NLP
  often processes documents faster than real-time (sub-second per page
  in many cases), especially when scaled out. Quick processing means
  lower latency in production workflows (e.g., scanning and parsing
  documents on the fly).

- **Fixed-Cost Licensing (No Token-Based Fees):** John Snow Labs uses a
  straightforward licensing model (e.g., annual or monthly subscription
  for unlimited use) rather than charging per document or per API call.
  This **fixed-cost model** is a significant differentiator for
  enterprise buyers. It provides **predictable budgeting** and often
  much lower total cost at scale. In contrast, cloud NLP APIs and
  LLM-based services charge by usage (tokens or number of images), which
  can become prohibitively expensive as volume grows. For example, an
  independent study estimated de-identifying 1 million medical documents
  would cost about **\$2,418 with John Snow Labs**(using a fixed license
  and on-prem hardware) versus **\$281,000+ with a GPT-4 API**.
  Similarly, John Snow Labs’ solution was shown to be \>80% cheaper than
  Azure’s or OpenAI’s on a per-document basis. This cost advantage,
  combined with no need to send data externally, is a compelling point
  for customers who need to process millions of pages or images.

- 

## **Benchmark Results**

To back up the above claims, here are some **benchmark results and case
study outcomes** that sales reps can cite:

- **Peer-Reviewed Benchmarks:** In a 2025 Text2Story workshop paper,
  John Snow Labs’ de-identification pipeline achieved **96.0% F1-score**
  on expert-annotated clinical notes, compared to 91.0% for Microsoft’s
  Azure Health Data Service and 83.0% for AWS Comprehend Medical. The
  JSL solution was the **only one to exceed human expert accuracy** and
  was deemed *“regulatory-grade”*. It also outperformed OpenAI’s
  GPT-4-based approach (79% F1) by a wide margin. These results
  demonstrate Visual NLP’s **industry-leading accuracy** in identifying
  PHI, with 5–13% higher F1 than competing methods. Such precise numbers
  give credibility when positioning Visual NLP as the best-in-class
  solution for healthcare NLP tasks.

[V. Kocaman et al., “Can Zero-Shot Commercial API’s Deliver
Regulatory-Grade Clinical Text De-Identification?”, Text2Story Workshop
at ECIR 2025.](https://arxiv.org/abs/2503.20794)

- **Providence Health Case Study:** Providence St. Joseph Health (a
  large U.S. hospital network) has employed John Snow Labs’ Visual NLP
  in production. In one project, they de-identified **~40,000 DICOM
  radiology images** using Visual NLP and achieved over **99% accuracy**
  in removing PHI from both the image pixels and metadata fields
  (*i.e.*, virtually no patient identifiers remained) . This real-world
  result underscores the platform’s ability to operate at scale (tens of
  thousands of images) with extremely high accuracy. It gives sales reps
  a powerful proof point: a respected healthcare system successfully
  used Visual NLP to process a large imaging dataset with *\>99%*
  precision. (Notably, Providence’s team also reported that the Visual
  NLP approach was **significantly faster** and more reliable than
  manual redaction or prior tools they tried – ensuring both compliance
  and efficiency.)
  <https://www./de-identification-of-medical-images-in-dicom-format/>

- **\[Other Benchmarks\]**

- **Visual NER: benchmarking against cloud providers.**

<img src="/media/image2.png" style="width:2.66714in;height:1.48471in" /><img src="/media/image3.png" style="width:2.72487in;height:1.51684in" />

Source:
<https://medium.com/john-snow-labs/visual-document-understanding-benchmark-comparative-analysis-of-in-house-and-cloud-based-form-75f6fbf1ae5f>

- **PDF Deidentification and Obfuscation repository:** this repo
  contains a dataset, notebooks, and metrics. Focus here is
  reproducibility -\> see for yourself, run a notebook, see results.

| **Difficulty Level** | **Precision** | **Recall** | **F1-Score** | **Total Files** |
|----------------------|---------------|------------|--------------|-----------------|
| 🟢 Easy              | 0.9851        | 0.9799     | 0.9825       | 30              |
| 🟡 Medium            | 0.9800        | 0.9575     | 0.9686       | 40              |
| 🟡 Zero Shot Medium  | 0.9861        | 1          | 0.993        | 10              |
| 🔴 Hard              | 0.9561        | 0.9290     | 0.9424       | 50              |

Github repo: <https://github.com/JohnSnowLabs/pdf-deid-dataset>

- Dicom Deidentification repo:

<table style="width:95%;">
<colgroup>
<col style="width: 60%" />
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">Model</th>
<th style="text-align: center;">Precision</th>
<th style="text-align: center;">Recall</th>
<th style="text-align: center;">F1-Score</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>🚀 ImageTextDetector - MemOpt (Scala) + ImageToTextV2 -</p>
<p>Base (Scala)</p></td>
<td>0.871</td>
<td>0.800</td>
<td>0.834</td>
</tr>
<tr>
<td>🚀 ImageTextDetector - MemOpt (Scala) + ImageToTextV2 - Large
(Scala)</td>
<td>0.892</td>
<td>0.822</td>
<td>0.856</td>
</tr>
<tr>
<td>🚀 ImageTextDetector - MemOpt (Scala) + ImageToTextV3 (Scala)</td>
<td>0.741</td>
<td>0.433</td>
<td>0.547</td>
</tr>
<tr>
<td>🐍 ImageToText (Python)</td>
<td>0.436</td>
<td>0.289</td>
<td>0.348</td>
</tr>
<tr>
<td>🔴 Presidio</td>
<td>0.07</td>
<td>0.128</td>
<td>0.091</td>
</tr>
</tbody>
</table>

More details in the repo:
<https://github.com/JohnSnowLabs/dicom-deid-dataset>

*In summary, both laboratory benchmarks and production deployments show
Visual NLP as a **leader in accuracy and scalability**. It consistently
**outperforms alternative solutions by 5–10%** across metrics while
maintaining throughput needed for enterprise workloads. Sales teams can
leverage these concrete results to reassure clients of the platform’s
proven performance.*

## **Deployment & Compliance**

Visual NLP was built with real-world healthcare requirements in mind,
including data privacy, regulatory compliance, flexible deployment, and
cost-effectiveness. Below are key points to address client questions
about **how and where** the platform can be used:

- **Regulatory Compliance:** The Visual NLP platform meets stringent
  healthcare data regulations. It supports full **HIPAA compliance** for
  PHI handling and can perform de-identification that adheres to the
  HIPAA Safe Harbor standard (removing or obfuscating all 18
  identifiers). It also aligns with **GDPR** requirements for
  anonymization in the EU. The tool’s obfuscation methods preserve data
  utility while ensuring no real patient info remains, as verified by
  audits. This regulatory-grade approach has been proven in settings
  like clinical research where de-identified data must be certified for
  use. Clients can be confident that using Visual NLP will not
  compromise their compliance posture – on the contrary, it can help
  them enforce it.

- **Data Security & Privacy:** **No patient data ever leaves your
  environment** when using John Snow Labs software. Visual NLP can be
  deployed in a hospital’s secure network or VPC, and all processing
  (OCR, model inference) occurs locally. This is a stark contrast to
  cloud AI services where documents are uploaded to third-party servers.
  For sensitive industries (healthcare, finance, government), this
  on-premise capability is often non-negotiable. Visual NLP supports
  installation in air-gapped environments and can run without internet
  access. It also integrates with authentication and access control
  (e.g., it can be containerized and managed under the customer’s
  security policies). Keeping PHI in-house minimizes risk of breaches
  and simplifies security reviews for adoption.

- **Flexible Deployment (Cloud or On-Premise):** The platform is
  infrastructure-agnostic. It can be deployed **on-premises**, on
  private or public **cloud clusters**, or in hybrid architectures –
  wherever Apache Spark can run. Official support and containers are
  available for AWS, Azure, GCP as well as Kubernetes, Hadoop clusters,
  and Databricks. This flexibility means clients can choose a deployment
  that fits their IT strategy and scale. Some smaller teams run Visual
  NLP on a single server or VM (for modest workloads), while others
  scale out to large clusters for high throughput. The Spark foundation
  ensures that adding more compute nodes linearly increases capacity.
  Visual NLP also supports GPU acceleration for both training and
  inference, which can be enabled if servers have NVIDIA GPUs. Whether
  the client’s environment is an on-prem Hadoop cluster or a managed
  Spark service, Visual NLP can be integrated smoothly. John Snow Labs
  provides installation scripts and support for all these setups. [DICOM
  de-identification at scale in Visual NLP
  (1/3)](https://www.johnsnowlabs.com/dicom-de-identification-at-scale-in-visual-nlp-1-3/#:~:text=Scalability%3A%20Visual%20NLP%20leverages%20the,with%20big%20data%20in%20healthcare)

- **Integration and APIs:** Visual NLP offers APIs in Python and Scala
  (and interoperability with Java), making it easy to integrate into
  existing data pipelines. It can ingest common file formats and output
  results as structured data (JSON, CSV, or Spark DataFrames). For
  example, after processing documents, the extracted text and entities
  can be passed to downstream systems like data warehouses or analytics
  dashboards. There’s also integration with John Snow Labs’ Annotation
  Lab for human review workflows, and with cluster orchestration tools.
  From a deployment perspective, the platform can run as a stand-alone
  application, be embedded into enterprise ETL jobs, or be exposed as a
  REST API microservice (some clients containerize the OCR pipeline
  behind an API to serve internal applications). This versatility in
  integration is an advantage when working with IT departments.

- **Licensing Model – Fixed Cost vs. Usage-Based:** As noted, John Snow
  Labs uses a **fixed-cost licensing model**. This is typically an
  annual license that grants unlimited use of the software (with fair
  usage terms) rather than charging per document or per API call. The
  advantage to customers is significant cost predictability and often a
  much lower cost at scale. There are no surprise fees for spikes in
  volume, and no counting of characters or images. This contrasts with
  **token-based models** from Generative AI APIs or usage-based pricing
  from cloud OCR services (which might charge, say, \$0.001 per image or
  per 1000 characters – costs that add up quickly). For example,
  OpenAI’s GPT-4 API effectively charges by the token (approximately
  0.03 USD per 1K tokens for processing), which becomes exorbitant for
  large datasets. John Snow Labs’ fixed pricing allows clients to budget
  a set amount and process as much data as needed within that license
  period. The case study mentioned earlier demonstrated a **\>100× cost
  difference** for large-scale de-identification (\$2.4K vs \$281K for
  1M documents). Moreover, because the software can run on commodity
  hardware or existing infrastructure, organizations avoid the high
  markups of cloud services. This pricing model is a compelling selling
  point for any customer worried about long-term ROI and scalability of
  NLP solutions.

*(Overall, Visual NLP gives organizations **full control**: control over
their data (for privacy), control over deployment (where and how it
runs), and control over costs (no metered fees). These points resonate
strongly with enterprise IT and procurement teams, turning potential
barriers (security reviews, budget approval) into strengths in our
favor.)*

## **Real-World Use Cases**

Visual NLP’s capabilities translate into a variety of **practical use
cases** across healthcare and related domains. Below are several
real-world scenarios that John Snow Labs sales reps can use to
illustrate how the platform adds value:

- **De-Identification of Radiology & Pathology Images:** Hospitals use
  Visual NLP to anonymize imaging data for research and collaboration.
  For example, a radiology department can automatically remove patient
  names, IDs, and dates from **DICOM** MRI scans or X-ray images before
  sharing them. The platform reads the text “burned-in” on the images
  (like labels in corners of an X-ray) as well as checks the DICOM
  metadata tags, and then **redacts or blurs any PHI**. Similarly, in
  digital pathology, Visual NLP can process Whole Slide Images (SVS or
  Dicom formats) to redact embedded patient info. This is critical for
  building teaching archives or AI datasets from medical images while
  protecting patient identities. One health network used this solution
  to de-identify tens of thousands of legacy radiology images (some ~40k
  scans) in preparation for a machine learning project – a task that
  would have been infeasible manually. The Visual NLP pipeline ran
  through the image archives, outputting clean images and audit logs of
  what was removed.

- **Automated Form Understanding in Intake & Claims:** Healthcare
  providers and insurers deal with millions of forms – patient intake
  forms, insurance claim forms, referral forms, etc. Visual NLP can
  significantly speed up **form processing** by extracting key
  information from scanned forms. For instance, a clinic can scan a
  patient registration form and let Visual NLP locate and extract fields
  like patient name, address, insurance number, and signed date. The
  system can be trained to recognize the specific format of the form
  (e.g., which boxes correspond to which field) – effectively doing
  **layout-aware OCR**. It can even detect **signatures** on the form
  and flag whether a signature is present or not. By converting form
  images into structured data automatically, hospitals can integrate
  that data into their EHR systems without manual data entry. Insurance
  companies are likewise using the platform to parse claim documents and
  invoices, classifying them and pulling out relevant entities (provider
  name, codes, amounts) for further processing. This use case emphasizes
  Visual NLP’s ability to handle **structured documents with complex
  layouts**, a task where generic OCR APIs often struggle.

- **Table Extraction and Analysis from Scanned Reports:** Many medical
  and scientific documents contain tables – for example, lab result
  reports, clinical trial PDFs, or even billing statements. Visual NLP’s
  table detection and extraction capability turns these from static
  images into useful data. A lab might use it to process faxed lab
  results: the system will find the table of test results within the
  scanned page, extract each cell (test name, value, unit, reference
  range), and produce a structured output (CSV or DataFrame) for those
  results. Moreover, the platform can run NER or other NLP on the
  extracted table text – essentially performing **NER inside tables**.
  For instance, if a pharmacovigilance team has tables of adverse events
  in reports, Visual NLP could extract the tables and then identify drug
  names and adverse event terms within them. This **table NER**
  capability (finding entities within a table’s cells) is fairly unique.
  It has been applied in real-world projects like extracting patient
  demographic info from census tables embedded in clinical study PDFs,
  and pulling medication names from dosing tables in trial protocols.
  The key benefit is **turning unstructured tables into queryable data**
  without manual retyping. This accelerates data analysis and
  integration, saving time and reducing errors.

### **Resources**

- **Product page:**
  [https://www./visual-nlp/](https://www.johnsnowlabs.com/visual-nlp/)

- **Benchmark Link:**

1.  [Comparing Spark NLP for Healthcare and ChatGPT in Extracting
    ICD10-CM Codes from Clinical
    Notes](https://www.johnsnowlabs.com/comparing-spark-nlp-for-healthcare-and-chatgpt-in-extracting-icd10-cm-codes-from-clinical-notes/?utm_source=chatgpt.com)

2.  [Benchmarks That Matter: Evaluating Medical Language Models for
    Real‑World
    Applications](https://docs.google.com/presentation/d/19eq6njspmJt4QaW6MZtvi2OvNIwmRaQZXFO7EZx5kQc/edit?usp=sharing)

- **DeepWiki Link:**
  <https://deepwiki.com/JohnSnowLabs/johnsnowlabs/3.2-visual-nlp-(spark-ocr)>

- **ModelPark Link:** <https://cancer-registry.johnsnowlabs.app>

- **Blog Links:**
  [Deep-learning-based-table-extraction-using-visual-nlp-1-2](https://www.johnsnowlabs.com/deep-learning-based-table-extraction-using-visual-nlp-1-2)

- [One-liner-magic-with-spark-nlp-deep-learning-for-table-extraction-2-2](https://ttps://www.johnsnowlabs.com/one-liner-magic-with-spark-nlp-deep-learning-for-table-extraction-2-2)

- [Built for Scale: The Deidentification Solution That Keeps Up with
  Your
  Needs](https://medium.com/john-snow-labs/built-for-scale-the-deidentification-solution-that-keeps-up-with-your-needs-103cbda35721)

- **Webinars:**

1.  [https://www./de-identification-of-medical-images-in-dicom-format/](https://www.johnsnowlabs.com/de-identification-of-medical-images-in-dicom-format/)

2.  [https://www./watch-webinar-next-gen-table-extraction-from-visual-documents-leveraging-multimodal-ai/](https://www.johnsnowlabs.com/watch-webinar-next-gen-table-extraction-from-visual-documents-leveraging-multimodal-ai/)

3.  [https://www./watch-zero-shot-visual-question-answering/](https://www.johnsnowlabs.com/watch-zero-shot-visual-question-answering/)

- **Example notebooks:**

1.  [PDF De-identification
    Pipeline](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/pp_pdf_deid/jupyter/SparkOcrPdfDeIdentificationPipelines.ipynb)

2.  [Pretrained Pipelines for PDF
    Deidentification](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/pp_pdf_deid/jupyter/SparkOcrPdfDeIdentificationPipelines.ipynb)
