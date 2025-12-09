# Zero Shot Learning for Semantic Relation Extraction from Unstructured Text
Zero Shot Learning for Semantic Relation Extraction from Unstructured Text

https://www.johnsnowlabs.com/watch-webinar-zero-shot-learning-for-semantic-relation-extraction-from-unstructured-text/

<https://www.youtube.com/watch?v=re5Aw6D7RNo>

<img src="/media/image.jpg" title="Video titled: Zero Shot Learning for Semantic Relation Extraction from Unstructured Text" style="width:6.3125in;height:3.65625in" />

The following is a detailed summary of the speech provided in the YouTube transcript excerpts, focusing on the core concepts of Spark NLP, relation extraction, and zero-shot learning.

### **Introduction and Agenda**

The webinar focuses on **zero-shot learning for semantic relation extraction from unstructured text** and its benefits for the **healthcare industry**. The speaker, Muhammad Santos, a data scientist in the healthcare team at John Snow Labs, outlined the agenda:

1.  Introduction to the **Spark NLP** library.

2.  **Spark NLP for Healthcare** and its components.

3.  Clinical relation extraction.

4.  **Zero-shot learning** for relation extraction.

5.  A live demonstration.

### **Spark NLP: The Foundation**

**Spark NLP** is an **open-source library** released in 2017. Its primary goal was to create an NLP library that requires **no dependencies other than Spark itself** and is capable of working on Spark clusters. It implements transfer learning and the latest state-of-the-art algorithms.

- **Adoption and Scope:** Spark NLP is highly popular, with 65K daily and 1.7 million monthly downloads, totaling 27 million downloads so far. It is updated every two weeks, accumulating more than 85 total releases. It supports Python, R, Java, and Scala.

- **Capabilities:** It is designed as a unified library for all NLU and NLP tasks, handling tasks like NER, text classification, question answering, and summarization. It uniquely includes features such as date matcher, spell checker, language detector, and keyword extraction.

- **Models:** It supports over 200 languages using the same NER architecture and includes more than four thousand pre-trained pipelines and models utilizing embeddings like GloVe, BERT, or ALBERT.

### **Spark NLP for Healthcare**

**Spark NLP for Healthcare** is a specialized, licensed library dedicated to healthcare tasks. (The related Spark OCR library handles preprocessing clinical images, but it was not the focus of the presentation).

- **Models and Tasks:** The healthcare module contains **more than 600 pre-trained pipelines and models** for tasks including entity recognition, entity linking, assertion status, relation extraction, de-identification, and clinical entity recognition.

- **Clinical Entity Recognition (NER):** This stage is critical; everything else is built upon it. The library offers over 100 clinical entity recognition models trained on clinical data sets like I2B2, NCBI, or PubMed, or datasets annotated by internal experts.

- **Entity Application:** Extracted entities (e.g., disease or problem entities) can be used to assign **ICD-10 codes** or **RxNorm codes** for drugs. Other applications include using the assertion status model (to check if a disease relates to the patient or someone else) and de-identification components to obfuscate sensitive information.

- **Ultimate Goal:** The combined use of these components allows users to detect various entities (like age, drug, and frequency) and find the **relations between them**, helping achieve results like calculating patient risk adjustment scores.

### **Clinical Relation Extraction (RE)**

**Clinical relation extraction** is one of the most important tasks in the healthcare domain, focusing on **predicting the semantic relationships between detected entities**.

- **Use Cases:** RE is vital for NLP applications such as question answering, summarization, and building clinical knowledge graphs. It can be used to detect temporal events, check **drug-drug interactions**, or determine which frequency is related to which drug or which treatment is used for which problem.

- **Adverse Drug Event (ADE) Example:** If a sentence contains multiple drug and ADE entities, relation extraction is necessary to determine which drug is responsible for which ADE entity.

- **Training Approaches:** Spark NLP uses two different approaches for training RE models for scalability:

  - **Fully Connected Neural Network (FCNN) based model:** This is lighter than BERT.

  - **BERT-based model:** This approach generally yields better results. The BERT-based model operates like sequence classification.

### **Challenges in Supervised Clinical RE**

Training supervised clinical RE models faces significant challenges:

- **Data Scarcity:** Finding clinical data is difficult because it contains **sensitive information (PHI)** that cannot be shared with third parties.

- **Expert Dependence:** Processing and annotating clinical data requires specific domain knowledge and trained domain experts.

- **Resource Constraints:** Training deep learning models commonly involves resource problems.

- **Label Limitation:** If these challenges are overcome, the resulting supervised model is trained only on a **fixed set of labels** and cannot detect relations without those specific labels.

### **Zero-Shot Learning (ZSL)**

**Zero-Shot Learning (ZSL)** overcomes the limitations of supervised learning by training a classifier on one set of labels and evaluating it on a different set of labels that the classifier has never encountered before. ZSL works by providing adequate auxiliary information (like appearance, properties, or functionalities) about the object to be recognized.

- **ZSL in NLP:** In NLP, ZSL commonly means enabling a model to perform a task it was not originally trained to do.

- **Common ZSL Approaches in NLP:**

  - **Prompt-based:** (e.g., GPT-3).

  - **Q&A based:** Based on asking questions and checking the answers.

  - **NLI (Natural Language Inference) based:** This is the method used in Spark NLP.

### **NLI-Based Zero-Shot Relation Extraction**

Spark NLP uses the **NLI-based approach** for zero-shot clinical relation extraction.

- **NLI Mechanism:** NLI models identify the relationship between two sequences: a **Premise** (the input text) and a **Hypothesis** (the desired relation description).

- **Classification:** The model classifies the relationship:

  - **Entailment:** The premise and hypothesis are compatible.

  - **Contradiction:** They are incompatible.

  - **Natural:** They are irrelevant.

- **RE Implementation:** To check for a relation (e.g., Adverse Drug Event), a user creates a meaningful hypothesis, such as "Drug causes problem". The clinical text is the premise. If the NLI model returns **entailment**, the relation extraction model confirms the adversarial designation between the entities.

### **Live Demonstration Overview**

The demonstration utilized a pipeline setup requiring a license and libraries like Spark NLP GSL and Spark NLP Display.

- **Pipeline Flow:** The pipeline included components like Document Assembler, Sentence Tokenizer, Tokenizer, Word Embeddings (clinical model), multiple NER models (clinical and ner_posology for drugs), and a ChunkMergeApproach.

- **RE Specific Components:** Perceptual model and Dependency Parser model were used to prepare the data for the **zero-shot relation extraction model (re_zero_shot_bert_model)**.

- **Zero-Shot Labels:** The model was tested on labels it had not seen before, such as "ADE," "improve," or "reveal". Users defined custom hypotheses (e.g., "Paracetamol improves sickness").

- **Results:** The zero-shot model successfully identified relations based on entailment:

  - Example 1: The hypothesis "Paracetamol improves sickness" resulted in an **entailment** prediction, assigning the relation label **"improved"**.

  - Example 2: The hypothesis "An mri test reveals cancer" resulted in an **entailment** prediction, assigning the relation label **"revealed"**.

- **Visualization:** Using the relation extraction visualizer, the relationships were displayed, showing linkages between detected entities like *Paracetamol* (Drug) and *headache/sickness* (Problem). A second example showed *Jupyter* (Drug) linked to *fatigue* and *anxiety* (Problem) with an **"adverse event"** relation.