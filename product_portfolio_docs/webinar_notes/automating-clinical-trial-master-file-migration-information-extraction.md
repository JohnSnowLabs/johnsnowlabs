# Automating Clinical Trial Master File Migration & Information Extraction
Automating Clinical Trial Master File Migration & Information Extraction

https://www.johnsnowlabs.com/watch-webinar-automating-clinical-trial-master-file-migration-information-extraction/

<https://www.youtube.com/watch?v=IchcgkDDdtw>

<img src="/media/image.jpg" title="Video titled: [Webinar] Automating Clinical Trial Master File Migration &amp; Information Extraction" style="width:6.3125in;height:3.65625in" />

The provided source is an excerpt from the transcript of a webinar titled, "\[Webinar\] Automating Clinical Trial Master File Migration & Information Extraction" by John Snow Labs. The speaker outlines the motivation for Trial Master File (TMF) migration, details the AI-driven solution developed by John Snow Labs, and reviews a specific case study conducted for Novartis.

### **I. Motivation for Trial Master File (TMF) Migration**

The webinar begins by noting that a Trial Master File must always exist within a company conducting clinical trials. However, there is no exact standardization of TMF content. While attempts have been made, such as the Drug Information Association's regular review and publishing of the TMF reference model, this model can be adjusted to fit the particular needs of different companies.

**Reasons for Migration:** Migration of a TMF from one IT system to another becomes necessary when **acquiring a new company or drug, or setting up a new ID system**.

**Challenges of Manual Migration:** TMF migration is a **complex project** because there is **no one-to-one mapping of standards** between systems, and additional information, such as metadata, needs to be extracted. When migrating tens or hundreds of thousands of documents, doing so manually is difficult.

The core challenges involve:

- **Labor-Intensive Process:** The process is challenging for the organization and the people migrating the documents.

- **Document Format Issues:** Documents are often scanned, requiring Optical Character Recognition (OCR). They frequently contain **handwritten text**, which is difficult to process.

- **Unstructured Data:** The text is unstructured, making it difficult or impossible to use standard Robotic Process Automation (RPA).

- **Bespoke Rules:** The process is governed by **bespoke, non-straightforward rules** that are usually not recorded anywhere.

The speaker provides specific examples of documents requiring complex metadata extraction, such as signature pages where specific metadata (version, principal investigator's last name, protocol date) must be extracted, even when two different dates are present in the document. Curriculum Vitae (CVs) require extraction of names and dates, sometimes handwritten.

### **II. The John Snow Labs TMF Migration Solution**

John Snow Labs developed a trial documentation migration system based on **Natural Language Processing (NLP)** and **Artificial Intelligence (AI)** methods. This technology allows the extraction of information and classification of documents even if the governing rules are not explicit.

**Key Features and Capabilities:**

- **OCR Capabilities:** Includes OCR and specific **handwritten detection and recognition**. Spark OCR can partially extract handwritten text and perform classification based on the visual image of the document.

- **Language Handling:** Supports language detection and can work with **multiple languages**.

- **Operational Modes:** Can operate in batch mode or instant mode.

- **Time and Labor Savings:** Offers significant time and labor savings, allowing migration to be done faster with a smaller team.

- **Custom Rules and Data Augmentation:** The system incorporates specific rules defined by a Subject Matter Expert (SME). It can **augment names or roles** using data from third-party databases, such as a database of people involved in a clinical trial.

**Quality Assurance and Technology:** The system is designed to ensure correctness of extracted information.

- **False Positives Detector:** A machine learning model is included to classify if the extracted information is correct or potentially incorrect. If potentially incorrect, it is flagged for **auditory exception handling**.

  - This detector uses signals such as whether the extracted data matches existing metadata, if the information is handwritten, the confidence level, and the location on the page (top, bottom, first page).

- **Validation:** Because clinical trials can negatively impact patient health, the system needs to be **21 CFR Part 11 validated**.

- **Architecture:** It runs **on-premise** without requiring internet access. It is based on **Apache Spark technology**, making it scalable to large computer clusters.

- **Underlying Components:** The solution utilizes **Spark NLP for Healthcare**, **Spark OCR**, and the **Annotation Lab**.

### **III. The Implementation Process and Team**

The migration project is typically an **end-to-end project** delivered over approximately six months, depending on complexity.

**Phases of the Project:**

1.  **Definition:** Define each **artifact** (document class), how information is extracted, post-processing rules, and Quality Assurance (QA) checks.

2.  **Development:** Code custom training models, develop post-processing components and the false positive classifier, and **verify accuracy**.

3.  **Verification:** Check performance metrics and adjust software pipelines.

4.  **Production Run:** Run the OCR, extraction, document classifier, and all post-processing steps.

5.  **Review and Finalization:** Review output quality, handle exceptions, and migrate documents.

The beginning of the project focuses heavily on setting up the **annotation guidelines and rules**, while the later part focuses on the true document migration and quality control.

**Key Components Developed for Each Project:** Due to the differences between TMFs, project-specific components are always developed:

- Annotation guidelines.

- Custom trained classification and entity extraction models.

- Post-processing pipelines.

- Validation documentation.

**Team Requirements:** John Snow Labs provides a multi-disciplinary team, including around two data scientists, one lead data annotator, annotators, a part-time TMF consultant, a computer validation specialist, and a part-time project manager. Customer resources are also necessary, including Subject Matter Experts (SMEs) on document management, TMF, IT security, quality, and validation, as well as **virtual machines** to perform the IT work, since the project runs on the customer side.

### **IV. Detailed Component Focus**

- **Annotation Guidelines:** These are written at the beginning of the project to describe how to classify a document, how to extract metadata, and define post-processing rules (e.g., what to do if two dates or multiple names are present).

- **Post-Processing Rules:** This is a critical step that can improve accuracy by **30-40 percent**. These rules codify procedures that would otherwise be informally discussed among human colleagues. Examples include handling mismatches between extracted names and existing metadata, dealing with names that appear in different locations within documents (e.g., top of a CV versus bottom of a signature page), and how to utilize third-party databases. These rules must be written down in guidelines and then coded.

### **V. Case Study: Novartis**

John Snow Labs completed a migration project for Novartis, which was presented at the 2021 NLP Summit.

**Solution Architecture for Novartis:** The solution involved two pipelines: a **development/training pipeline** and a **production pipeline**.

1.  **Training Pipeline:** Training data is entered, extracted via OCR, annotated in the Annotation Lab, enriched with post-processing, and used to prepare the machine learning/NLP model.

2.  **Production Pipeline:** Documents undergo OCR, the developed models (classification, NER extraction, handwritten recognition) are run, post-processing rules are applied, and the output goes through quality control and exception handling. A feedback loop allows adjusting models and rules based on quality control results.

**Project Scope and Setup:**

- The project lasted one year.

- The team selected **48 TMF artifacts** (e.g., site staff qualification supporting information).

- The system extracted **29 attributes**.

- **Technical Environment:** The solution ran entirely **on-premise without internet access** on three production and three development servers provided by Novartis, each with 64GB RAM, running Red Linux.

- **Team Composition:** The JSL team included two data scientists, 1.5 data annotators, and a part-time project manager. Novartis provided subject matter experts, annotators, ID support, and validation support.

**Novartis Post-Processing Rule Examples:** Rules were dictated or suggested by SMEs to handle specific data conflicts:

- Selecting which date to use when multiple dates existed in a document, across multiple pages, or when dates conflicted with existing metadata.

- Handling instances where names and roles did not match existing metadata.

- Addressing document type mismatches.

- Specifying regions within documents where data should be extracted (e.g., name on top for a CV, but on the bottom for a signature page).

The project achieved very **high accuracy** for both artifact and attribute extraction.