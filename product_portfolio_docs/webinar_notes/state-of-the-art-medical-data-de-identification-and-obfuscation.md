# State-Of-The-Art Medical Data De-identification and Obfuscation
State-Of-The-Art Medical Data De-identification and Obfuscation

<https://www.johnsnowlabs.com/watch-state-of-the-art-medical-data-de-identification-and-obfuscation/>

<https://youtu.be/SuzqI3CM8ik>

<img src="/media/image.jpg" title="Video titled: State-Of-The-Art Medical Data De-identification and Obfuscation Webinar" style="width:6.3125in;height:3.65625in" />

This detailed summary extracts and synthesizes the key information from the "State-Of-The-Art Medical Data De-identification and Obfuscation Webinar" transcript, covering the motivation, regulatory landscape, John Snow Labs' (JSL) solutions, technical approach, and project implementation methods.

### **I. Introduction and John Snow Labs (JSL) Overview**

The webinar focuses on state-of-the-art medical data de-identification and obfuscation. The agenda covers the background of John Snow Labs, the motivation for de-identification, benchmarks, and the typical process for running a de-identification project.

**John Snow Labs Background:**

- JSL is the organization behind **Spark NLP**, which is described as the most widely used library in the industry.

- JSL has developed commercial extensions, including Healthcare NLP, Finance NLP, and Legal NLP.

- They focus on accuracy, holding 20 top positions in benchmark papers, and speed, partnering with Nvidia and Intel to ensure fast execution, even on a single processor.

- The solution is built on the Spark platform, ensuring scalability for Big Data and large clusters, making it suitable for the Enterprise.

- JSL has experience handling Protected Health Information (PHI) data and utilizes internal annotation teams to build proprietary models.

- JSL has customers among the largest Pharma companies, including case studies involving **Providence** (de-identification of 700 million notes) and **IQVIA** (de-identification of doctor notes in general language).

### **II. Motivation and Regulatory Framework**

The need for de-identification is driven by three main factors: increasing privacy concerns, exponential data growth, and improving NLP capabilities.

**Privacy Regulations:**

- Key regulations include the **HIPAA Privacy Rule** (introduced early 21st century) and **GDPR** (younger than HIPAA).

- **GDPR** imposes strict penalties for non-compliance, such as 10 million Euros or 2% of global revenues.

- **HIPAA** carries potential criminal or civil penalties. Other regulations exist globally (e.g., Canada and Australia).

- The **HIPAA Privacy Rule** generally prohibits the use or disclosure of Protected Health Information (PHI) except for specific reasons (e.g., curing people, billing, or running a healthcare business).

- However, if the data is de-identified-meaning PHI is removed-it is **no longer covered by the regulations**.

**Methods for PHI Removal (HIPAA):** HIPAA outlines two methods for removing PHI:

1.  **Expert Determination:** Requires using generally accepted statistical methods and documenting the process of removing the health information.

2.  **Safe Harbor:** Requires the removal of **18 listed identifiers**. Both methods mandate that there must be no information remaining that can identify an individual, and no reasonable basis to believe the remaining information can be used to identify a human.

**GDPR (Europe):** The GDPR situation is similar, although it is "more fuzzy" and lacks a specific Safe Harbor rule. Compliance requires determining if the data is sufficient to identify a person, either directly or indirectly, taking into account the time, cost, and available technology required for identification. If data is rendered anonymous and the subject is not identifiable, it is not covered by GDPR.

### **III. Accuracy and De-identification Benchmarks**

The quality of NLP is increasing, which supports automatic de-identification.

**Human vs. NLP Accuracy:**

- Manual de-identification has shown limitations: a benchmark indicated one person achieved 81% recall (ability to find PHI), and quality assurance checks only achieved 94% accuracy.

- Natural Language Processing (NLP) has surpassed manual limits, achieving a benchmark of **98.2% accuracy** in JSL's solution.

- Accuracy measurement differs: 98% is measured at the **token level** (counting PHI successfully removed). If measured at the **sentence level** (ensuring no PHI leakage in a sentence), the figure is much higher, exceeding 99%.

**JSL Benchmarks and Augmentation:**

- JSL supports seven languages and multiple entity levels. De-identification involves more than just Named Entity Recognition (NER); the end-to-end pipeline includes **regex rules** and **contextual parsers**.

- Augmenting the base NER models with regex and contextual parsers provides significant boosts, such as a 5% average accuracy boost in English.

- When using the entity-agnostic metric (PHI detection regardless of entity type), the accuracy is 95%.

- Overall, JSL currently detects Phi entities with an average accuracy **above 98%**, meaning less than two sensitive entities are missed out of 100.

- JSL's augmented solution is reported to be **3% better** than the latest state-of-the-art academic benchmarks.

- JSL aims for language agnostic performance, showing consistent accuracy across various languages (e.g., name entities around 94%, dates over 98%, IDs over 93% in every language).

**Comparison to Commercial Providers:**

- Commercial cloud providers (AWS, Google, Azure) offer pay-as-you-go identification solutions.

- Spark NLP outperforms these major providers on almost every major entity. JSL's licensing model allows users to process millions of records after a single license purchase.

### **IV. John Snow Labs De-identification Capabilities**

JSL's software handles a variety of input formats and offers different methods for PHI removal.

**Input Formats and Languages:**

- Input formats include PDF (scanned or searchable), unstructured text documents, Microsoft Office formats, CSV, JSON, and **dicom images** (on the pixel level and embedded metadata).

- The system supports English and various European languages, with the capability to train more models if demand arises.

**De-identification Methods:**

1.  **Masking:** Replacing PHI with a constant string (e.g., "name" or "date") or replacing the original token with a fixed or preserved number of stars (e.g., "John" replaced by three stars).

2.  **Obfuscation and Faking:** Replacing sensitive information (names, dates, locations, hospital names) with random numbers or entries selected from a dictionary. Dates can be replaced with a random date or shifted by a constant time shift.

3.  **Image Masking:** PHI in images (like diagrams or PDFs) can be replaced with black rectangles.

### **V. Technical Pipeline and Consistency**

The JSL solution can be run in high-compliance, air-gap environments, with no need for an internet connection.

**Technical Pipeline Stages (Spark NLP):** The process utilizes a pipeline concept where each stage uses the output of the previous stage.

1.  **Document Assembler:** The entry point to the pipeline.

2.  **Sentence Detection & Tokenization:** Processes the document into sentences and tokens.

3.  **Embeddings:** Uses clinical embeddings (or others, depending on context) to create a meaningful representation of each token, essential for the NER architecture.

4.  **NER Models:** Token classification algorithms (e.g., BiLSTM-CNN-Char architecture or Transformer-based) are used to detect and label entities (e.g., John is a "B-Patient").

5.  **Contextual Parsers and Regex Matchers:** Rule-based systems augment the deep learning models, leveraging domain knowledge to detect entities that the machine learning models might miss.

6.  **Chunk Merger:** Merges the output from the various detection models (DL, contextual, regex) to ensure each token receives a single label.

7.  **De-identification Annotator:** The final stage that performs the actual masking or obfuscation. It includes hard-coded rules for common structured data like SSN, passport, and credit card numbers.

**Obfuscation Consistency Rules:** When obfuscating data, JSL applies consistency measures to ensure the integrity of the document:

- **Name Consistency:** The replacement name for a patient must be consistent throughout all references within a single document and across all clinical notes belonging to that patient.

- **Gender Consistency:** A gender classifier is integrated to ensure female names are replaced with female names, and male names with male names.

- **Age Consistency:** Ages are replaced only with others from the same defined age group (e.g., adult replaced by adult age).

- **Clinical Consistency:** Replacement names must align with gender-specific clinical diseases (e.g., breast cancer or prostate cancer) that might indicate the patient's gender.

- **Date Shift Consistency:** Dates can be normalized (using a date normalizer) and then shifted by a specific range or a consistent patient-wise shift (e.g., Patient 1 always shifted by +3 days).

- **Length Consistency:** Sometimes required by infrastructure, the length of the replaced tokens or the resulting document is preserved.

### **VI. Project Implementation and Deployment**

JSL offers multiple paths for implementing a de-identification solution.

**Project Options:**

1.  **End-to-End De-identification Service:** JSL manages the entire process. This comprehensive solution includes:

    1.  **Legal Requirements Analysis:** Addressing regulations beyond HIPAA/GDPR.

    2.  **Risk Analysis:** Determining potential PHI leakage and who works with the documents.

    3.  **Quality Assurance (QA) Strategy:** Setting up processes for checking quality, monitoring results, and addressing data distribution shift ("drift").

    4.  **Programming and Operation:** Running the de-identification pipelines and handling operation, including emergency unblinding or response to audit requests.

2.  **Proof of Concept (POC):** A focused project, typically lasting one month or slightly over, designed to determine feasibility, accuracy, and expected results. A team of clinical data scientists and annotators is assigned. Complex projects may take two to three months.

3.  **Self-Serving Cloud:** A product currently under development that will be available through the AWS Marketplace, though with fewer capabilities than the full iterative pipelines.

**Data Location and Deployment:** The solution is designed to run **on-prem** with no internet connection. This deployment model allows customers to ship the pipeline within their own environment, connect to their sensitive data sources, and maintain full control without sending data externally. The license allows the customer to run the library while JSL provides support.