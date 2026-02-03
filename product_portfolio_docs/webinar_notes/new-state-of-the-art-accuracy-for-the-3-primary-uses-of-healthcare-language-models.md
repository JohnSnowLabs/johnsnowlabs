# New State-of-the-art Accuracy for the 3 Primary Uses of Healthcare Language Models
New State-of-the-art Accuracy for the 3 Primary Uses of Healthcare Language Models

<https://www.johnsnowlabs.com/watch-webinar-new-state-of-the-art-accuracy-for-the-3-primary-uses-of-healthcare-language-models/>

<https://youtu.be/xR_SF6HOo2E>

<img src="/media/image.jpg" title="Video titled: New State-of-the-art Accuracy for the 3 Primary Uses of Healthcare Language Models" style="width:6.3125in;height:3.65625in" />

The speech extracted from the YouTube transcript details the current state-of-the-art (SOTA) accuracy metrics and critical learnings regarding three primary use cases for medical Large Language Models (LLMs). The speaker, David Alby (CTO at John Snow Labs), emphasizes the practical implications of these benchmarks for projects.

The three use cases discussed move from the least commonly seen in production to the most prevalent use case currently enabled by LLMs:

## **1. Answering Medical Questions (Medical QA)**

This use case often serves as the **primary benchmark** for evaluating medical LLMs. John Snow Labs (Johns) recently achieved a new state-of-the-art on the **Open Medical LLM Leaderboard** (a resource they are not affiliated with). This leaderboard looks at the average performance across nine benchmark datasets and includes over 100 models, positioning Johns' model as the best overall, outperforming competitors like GPT-4, Med-PaLM 2, Llama 3 variants, and various healthcare-specific models.

### **Key Benchmarks and Milestones**

The nine benchmarks are intended to show different types of medical question answering and reasoning. Examples discussed include:

- **MedQA:** A classic question-answering dataset based on the US medical licensing exam. These questions present a patient story combining natural language (like patient slang) with technical details (vital signs, lab results). The model must provide a multiple-choice answer, usually related to diagnosis or the next test/drug, and explain the evidence behind its choice.

- **MMLU:** Contains a large set of tests for college-level question answering, including five datasets related to healthcare (Clinical, Genomic, Biology, Medicine, and Professional Medicine). These also require understanding medical terminology, context, and temporal order.

- **MedMCQ:** Questions drawn from medical licensing exams, often broken down by specialties (over 20 categories like pharmacology and surgery). The model must select a multiple-choice answer and provide evidence, such as explaining why a patient requires Vitamin B12.

- **PubMedQA:** A biomedical research dataset (not clinical) where questions are often derived from the titles or abstracts of academic papers. The model receives the question and context (the academic paper) and must produce a short answer (e.g., yes/no) and a long answer detailing the study's findings.

**Important Milestones:**

- Johns announced the first **8-billion parameter LLM** that beats both GPT-4 and Med-PaLM 2 on the average of these nine benchmarks.

- A 7-billion parameter model achieved 78.4% accuracy on PubMedQA, surpassing the **single human performance** baseline of 78% for biomedical researchers answering these questions.

### **Learnings from Medical QA**

1.  **Domain Specificity:** **Healthcare-specific models** generally outperform large, general-purpose models (like GPT-4). Tuning a model on domain-specific data yields more accurate results.

2.  **Overfitting:** Practitioners must beware of **overfitting**, especially with smaller models. A model can score extremely high on a specific benchmark (e.g., 90% on PubMedQA) but fail on general medical or basic non-medical questions. It is recommended to test medical models on general LLM benchmarks to assess their ability to generalize.

3.  **Efficiency:** Smaller, task-specific models are far **more efficient and economical** to run in production. An 8-billion parameter model can run on a laptop or a server costing less than \$1 per hour, contrasting sharply with LLM API endpoints that can cost \$15 to \$35 per compute hour or higher per token.

4.  **Real-World Use:** Benchmarks **do not reflect real-world use cases** (e.g., answering medical licensing questions is not a common customer requirement).

## **2. Understanding Clinical Documents (Information Extraction)**

This use case, information extraction from clinical documents, is seen much more frequently in production settings.

### **Core Tasks and Performance Gap**

The core need is to read and understand unstructured medical text. A case study with the FDA regarding Adverse Events (AEs) due to opioids highlights the importance, as Adverse Events are estimated to be over 90% underreported.

Classic medical information extraction tasks include:

- **Text Classification:** Determining if a sentence describes an Adverse Drug Event (ADE).

- **Entity Recognition:** Identifying specific entities like drugs (e.g., insulin) and symptoms (e.g., drowsiness, blurred vision).

- **Relation Detection:** Identifying the semantic relationship between entities (e.g., knowing that cramps relate only to the drug "flatin" and not "lipitor" in a single sentence).

**LLM Performance:** Current GPT models perform **quite poorly** on these medical information extraction tasks. While they can be used, traditional deep learning/transfer learning models tuned for the specific task provide much higher accuracy out of the box.

### **Specific Extraction Challenges**

1.  **Social Determinants of Health (SDoH):** For extracting SDoH (aspects like housing, education, or finances that impact health) from unstructured text, **GPT-4 made three times more mistakes** than John Snow Labs' current model.

2.  **Normalization:** There is an even bigger gap when normalizing recognized entities to standard codes (e.g., mapping a diagnosis to an ICD-10 CM code or a procedure to a CPT code). LLMs are not designed to do this effectively.

3.  **De-identification (PHI):** The task of identifying and masking or obfuscating sensitive entities (names, dates, addresses, etc.) in medical text.

    1.  State-of-the-art task-specific models consistently achieve **98-99% accuracy**, which is above the human baseline (a single human achieves around 93% accuracy; three humans achieve 98%).

    2.  GPT-4 currently lags significantly (a reported 33% gap was shown in a recent paper), meaning it cannot be reliably used for automated de-identification from a regulatory perspective.

    3.  Using specialized models for de-identification at scale was calculated to be two orders of magnitude cheaper than using GPT-4.

## **3. Patient-Level Reasoning (End-to-End Systems)**

This is the big new upcoming use case, moving beyond document analysis to reasoning about the **patient as a whole**.

### **The Need for Patient-Level Context**

A collaborative project focused on identifying neuropsychiatric events in children taking Montelukast (an asthma medication) illustrates this need. Much of the required mental health information (e.g., trouble sleeping, agitation, bad dreams, sleepwalking) appears only in unstructured clinical notes, as these symptoms rarely receive a formal diagnosis code in structured billing data.

LLMs enable patient-level questioning, where researchers or doctors can ask questions about the patient's entire history (structured and unstructured data) without manually clicking through EHR systems.

### **Key Requirements for Patient-Level QA**

The system must go beyond simple extraction and perform informed deduction:

- **Inferred Age Example:** If a patient's age is not explicitly mentioned, the system should infer it based on context (e.g., "born prematurely," "observed for apnea of prematurity") and conclude that the patient is likely a premature infant aged 28-35 weeks.

- **Critical References:** The system must provide **references** for all conclusions, allowing the user to click and verify the exact paragraph, even within 200 or 300-page documents.

### **End-to-End Architecture**

Solving this use case requires a carefully constructed pipeline, combining different specialized models and skills:

1.  **Ingestion:** Loading all available data (structured, notes, images, audio).

2.  **Information Extraction:** Applying highly accurate, **state-of-the-art task-specific models** to extract entities and information from *each document* (e.g., radiology entities from a radiology report).

3.  **Patient-Level Reasoning:** Using small LLMs to synthesize the extracted facts and answer questions about the patient's overall history or condition. Small LLMs are preferred for this stage due to the efficiency needed to process updates at scale.

4.  **Data Fusion/Modeling:** Organizing the extracted facts into a standard patient data model, such as a relational database using **OMOP** (a standardized data model for patients) or a **Knowledge Graph** (for querying relationships between diseases and events).

5.  **Serving/Chatbot:** Utilizing a chat LLM that works in tandem with a **healthcare-specific agent or tool**. This agent is critical because it converts the natural language question (e.g., "What is this patient allergic to?") into a structured query (Text-to-SQL or Cypher for a Knowledge Graph) against the data model to retrieve the precise answer.

John Snow Labs has a healthcare-specific **Text-to-SQL model** (accepted February 2024) that achieves SOTA accuracy (0.85) on the MIMIC-SQL database, outperforming GPT-4, and can be used as this agent tool.

### **General Conclusions on LLM Development**

- **Pipeline Necessity:** This medical reasoning requires a combination of different models and skills; trying to put all the data into a Retrieval Augmented Generation (RAG) database or giving everything to one LLM in a huge context window is generally found not to work at scale or in production.

- **Accuracy Volatility:** Any statement regarding LLM accuracy is a "point in time statement". Accuracy is improving on a weekly basis, sometimes multiple times a week.

- **Design for Change:** Organizations should **not get attached to specific LLMs**. System designs must encapsulate the LLM so that models and underlying architectures can be upgraded frequently to take advantage of continuous accuracy improvements.