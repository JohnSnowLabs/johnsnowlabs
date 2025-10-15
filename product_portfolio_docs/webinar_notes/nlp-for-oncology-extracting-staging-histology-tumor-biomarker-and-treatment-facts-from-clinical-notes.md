# NLP for Oncology Extracting Staging, Histology, Tumor, Biomarker, and Treatment Facts from Clinical Notes
NLP for Oncology Extracting Staging, Histology, Tumor, Biomarker, and Treatment Facts from Clinical Notes

<https://www.johnsnowlabs.com/nlp-for-oncology-extracting-staging-histology-tumor-biomarker-and-treatment-facts-from-clinical-notes/>

<https://youtu.be/7YYdpBidyDc?si=xwuCUa0gVlQ6Y3Fo>

<img src="/media/image.jpg" title="Video titled: NLP for Oncology: Extracting Staging, Histology, Tumor, Biomarker, and Treatment Facts" style="width:6.3125in;height:3.65625in" />

The content provided is an excerpt from the transcript of a YouTube webinar titled "NLP for Oncology: Extracting Staging, Histology, Tumor, Biomarker, and Treatment Facts".

The following is a detailed summary of the speech form extracted from the source:

### **I. Introduction and Context**

The webinar begins with an introduction by the host, welcoming attendees and requesting that questions be asked in the chat, where the speaker will answer them live. The speaker is **Maro Universal Fidani**, a medical doctor and data scientist at **John Snow Labs**, located in Argentina.

The main topics covered include:

1.  Different types of oncology models (including usage and selection).

2.  Pre-trained pipelines and how to use them.

3.  A sample use case demonstrating how to apply the learned concepts.

The models discussed were trained using data annotated and reviewed by John Snow Labs' **in-house team of medical doctors/annotators**, who also developed the annotation guidelines. The annotation process utilized the **Annotation Lab** tool.

### **II. Core Types of Oncology NLP Models**

The speaker covers four primary types of oncology models available in Spark NLP for Healthcare:

#### **1. Entity Recognition (NER)**

NER models are used to **extract and classify parts of the text**. Examples of extracted entities include age, gender, cancer diagnosis, surgery, and staging.

- **Granularity and Selection:** Different NER models offer varying levels of **granularity** (number of layers in the taxonomy). The most comprehensive model is **ner_oncology**, which extracts data for all entity groups at a high granularity, covering around **50 entities**. Other NER models are specific to certain areas like treatments or tests.

- **Recommendation for Selection:** When building an NLP pipeline, it is recommended to **include more than one NER model** and check which one fits the use case best. Users can also employ **Ner Overwrite** to combine extractions from multiple NER models.

- **Key Entity Groups in ner_oncology**:

  - **Anatomical Entities:** Includes locations and directions (e.g., left, right, bone, breast).

  - **Demographic Entities:** Age, gender, race, ethnicity, smoking status, and a **Death entity** (for words like "died").

  - **Diagnosis Related Entities:** Includes Cancer Diagnosis (e.g., breast cancer, which includes the anatomical site), adenopathies, metastasis, performance status (Karnofsky/ECOG), and staging (TNM and other systems like "Advanced").

  - **Pathology Entities:** Specific oncology concepts like cycle day and cycle number, along with unspecific ones like duration and frequency.

  - **Response to Treatment:** Entities like line of therapy (e.g., first line) and mentions of recurrence or good/bad response.

  - **Test Entities:** Tests, biomarkers, and their results.

  - **Treatment Entities:** Chemotherapy and cancer surgery.

- **Specific NER Examples:** ner_oncology_tnm extracts information related to the TNM stage, including tumor description, lymph nodes, and metastases. ner_oncology_biomarker specifically extracts biomarkers and their results.

#### **2. Entity Resolution (ER)**

ER models are used to **map NER extractions to normalized terms**. An example shown is mapping cancer diagnoses (e.g., "breast carcinoma") to standardized **ICDO codes**.

- **Filtering:** It is generally recommended to **filter NER extractions** before using an entity resolver, especially if the goal is to get specific codes (like ICDO codes). Entities such as dates or gender usually do not require codes, so a **Chunk Merger with a blacklist** can be used to filter them out.

#### **3. Relation Extraction (RE)**

RE models are used to **link NER chunks that are related to one another**. For instance, linking a tumor finding (mass) with its size (e.g., 2 centimeters).

- **Types:** Relation models vary in their granularity, extracting relations such as test findings, locations, dates, and sizes. Specific models exist for biomarkers/results, locations/entities, and sizes/tumors/metastasis/lymph nodes.

- **Fine-Tuning:** The speaker recommends using **relation pairs** as a crucial fine-tuning parameter. This ensures the model only attempts to extract relations between relevant entity combinations (e.g., excluding dates or treatments when looking for tumor sizes), thereby reducing noise.

#### **4. Assertion Status Models**

Assertion status models extract information about the **context** of NER extractions. They determine if an extraction is **absent, past, present, or hypothetical**. They can classify a cancer diagnosis as "medical history," "possible," or "family history," based on the surrounding text.

- **Complete Model:** The most complete model is **assertion_oncology_wip**, which extracts labels including *absent, family, hypothetical, past, possible,* and *present*.

- **Recommendation:** Similar to ER models, it is important to **filter entities** (using a Chunk Merger and a blacklist) before applying assertion models, as assertions may not make sense for entities like body parts.

### **III. Pre-trained Pipelines**

Pre-trained pipelines are a way to **summarize and simplify the use of NLP components**, often including many steps (e.g., over 20 steps in one example). They are the recommended starting point for new projects.

- **Benefit:** When using these pipelines, users do not need to worry about fine-tuning parameters like relation pairs or using Chunk Merger blacklists, as that is handled during pipeline creation.

- **Oncology-Specific Pipelines:** John Snow Labs offers four oncology-specific pipelines: a general oncology pipeline, one for **diagnosis entities** (including NER, Assertion, RE, and the ICDO Entity Resolver), one for **biomarkers**, and one for **therapies**.

### **IV. Sample Use Case: Clinical Trial Recruitment**

A common real-world problem is recruiting patients for a clinical trial based on inclusion criteria (e.g., gender, age, specific diagnosis, or absence of previous treatments).

- **Strategy:** Approaching such problems requires **combining different model types**.

- **Examples of Model Combination**:

  - **Gender:** Use NER to extract gender, plus an **Assertion model** to ensure the mention refers to the patient, not someone else (e.g., family history).

  - **Cancer Diagnosis/Staging:** Use NER (e.g., ner_oncology or ner_oncology_tnm) combined with **Assertion** or **Entity Resolver** to filter results.

  - **Biomarker Results:** Use NER plus **Relation Extraction** to link the biomarker to its corresponding result value.

  - **Cancer Treatments:** Use NER plus **Assertion** to determine if a treatment is present, absent, or merely hypothetical.

### **V. Conclusion and Q&A Handling**

Maro concludes his presentation, hoping the audience found the information useful. The host informs attendees that due to technical issues, the live Q&A session could not proceed. Attendees are instructed to **forward all questions to John Snow Labs**. A copy of the webinar recording will be sent via email shortly after the session ends.