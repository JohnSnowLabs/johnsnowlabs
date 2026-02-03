# Zero-Shot Learning of Healthcare NLP Models
Zero-Shot Learning of Healthcare NLP Models

<https://www.johnsnowlabs.com/zero-shot-learning-of-healthcare-nlp-models/>

<https://www.youtube.com/watch?v=8RZwqvhfti8>

<img src="/media/image.jpg" title="Video titled: Zero Shot Learning of Healthcare NLP Models" style="width:6.3125in;height:3.65625in" />

The following is a detailed summary extracted from the speech presented by Asham Muhak from Johnson Labs regarding zero-shot learning applications in healthcare Natural Language Processing (NLP) within the Spark NLP ecosystem.

### **Overview of Spark NLP and Spark NLP for Healthcare**

**Spark NLP** is the foundational NLP library developed by John Snow Labs. It offers a full suite of NLP capabilities, including text normalization, cleaning, advanced functions like summarization, entity recognition, translation, and support for Automatic Speech Recognition (ASR). It includes over **11,000 pre-trained pipelines and models** and supports more than 250 languages. It is designed to run within the user's environment, including air-gapped settings, and is optimized with GPU integration (Nvidia) while also functioning on standard CPUs.

**Spark NLP for Healthcare** builds upon this foundation, offering a library specifically fine-tuned for healthcare use cases. This involves two main expansions: **bespoke models** and additional capabilities.

- **Bespoke Models:** The library contains over 800 pre-trained models in total. For Named Entity Recognition (NER) alone, there are more than 100 models covering specific biomedical domains such as internal medicine, pathology, oncology, nephrology, biomarkers, and social determinants of health (SDOH). These models are trained on curated datasets.

- **Additional Capabilities for Healthcare:**

  - **Deidentification:** A module that uses entity recognition to mask, obfuscate, or offiscate text, replacing PHI information (e.g., names, dates, locations, SSN) with random data.

  - **Clinical Entity Linking (Resolvers):** Models used to map extracted entities to standardized codes like ICD, CPT, SNOMED, RxNorm, UMLS, and MeSH.

  - **Assertion Status:** Distinguishes the context of a problem, such as whether it relates to the subject, occurred in the past, or is part of a family history.

  - **Relation Extraction (RE):** Links entities semantically to create a hierarchical structure.

The core foundation of medical NLP is the extraction of named entities (chunks). Errors made at the NER layer (the first layer) naturally propagate to downstream tasks like entity linking and relation extraction. RE's basic job is to link independent entities (like a drug, its duration, and its dosage) to create a hierarchy and establish attributes.

### **Transition to Zero-Shot Learning**

Historically, models for NER and RE were trained using the **supervised approach**, which requires large amounts of labeled data (token classification schemes like BIO or BIOES) to train architectures like Bi-LSTM or BERT.

**Limitations of the Supervised Approach:**

- **Lack of Bespoke Data:** It is difficult to find specific datasets for niche use cases, hindering quick experiments.

- **Laborious Data Generation:** Annotating data for NER and RE is time-consuming and complex, as it involves highlighting chunks and linking them.

- **Limited Generalization:** Supervised models trained on one dataset perform poorly or incur more errors when applied to new, unseen data, especially if the new data distribution is different (e.g., classifying "CA" as Calcium instead of California).

- **Fixed Entity Types:** If looking for a very specific type of entity (like biomarkers) and no model exists, annotation must be started from scratch.

The goal of the **Zero-Shot (ZS) approach** is to reduce or eliminate manual annotation and provide models with better generalization capabilities.

### **Zero-Shot Named Entity Recognition (NER)**

ZS NER leverages large, pre-trained language models (like BERT or RoBERTa, trained in an unsupervised manner on large corpora like PubMed) to utilize the model's learned semantic knowledge.

**How it Works (Question Answering):** The problem is reformulated as a **Question Answering (QA) problem**. The base language model is fine-tuned on a QA dataset (like SQuAD). Users provide the input text and ask generic questions (e.g., "When was the patient admitted?"). The model predicts spans or finds the answers to these questions within the text. The output is dynamic; if the NER model does not find an answer, it will not return any spans.

**Implementation in Spark NLP:** Spark NLP streamlines this process by including a **Medical Question Generator module**. This module can automate the generation of questions using templates for static concepts (like age or temporal aspects). The **Contextual Parser** (a proprietary, rule-based component) runs first to identify subjects and actions in the text (e.g., patient is the subject, admission is the action), which the Question Generator then uses to formulate questions (e.g., "When was the patient admitted?").

If multiple questions result in overlapping or conflicting spans, the module resolves this by assigning the entity type based on the span with the **highest confidence** or by selecting a larger span that encapsulates a shorter one. If the problem is complex, users can skip the parser/generator stages and manually define their own prompts (questions) to gain better control over the results.

### **Zero-Shot Relation Extraction (RE)**

The concept is similar to ZS NER, but it simplifies the task to a **classification problem**.

**How it Works (Classification):** The ZS RE model takes entities (spans) predicted by the NER model. It is tuned on **NLI (Natural Language Inference) datasets**. Given two entities, the model classifies the relationship between them into three main classes: **Entailment** (supports the premise), **Contradiction** (negates the premise), or **Neutral** (no relation). If the model finds no relationship, the "neutral" class is the most probable answer.

**Prompt Generation for RE:** To determine the relation, the user defines a question (prompt) designed to link the entities. For example, to link "Norvasc" (drug) and "chest pain" (problem), the prompt might be: "Norvasc treats chest pain". The model then classifies whether this statement contradicts, entails, or is neutral relative to the original document. By controlling the prompt, the three NLI outputs can be mapped onto various specific relation classes (e.g., drug caused a problem, drug improves a problem, test reveals a problem), enabling multiclass classification. RE tasks are primarily done on entity pairs, though complex relations (e.g., involving three entities) can be broken down into multiple pairs.

**Performance and Control:** While supervised models trained on a specific dataset (like I2B2) might achieve higher F1 scores (e.g., 72-81% range for ZS versus higher for supervised) on that same data, the zero-shot model's primary strength is its consistent performance on **unseen data**. The quality of the **prompt generation** has a major impact on how well the ZS model performs.

### **The Spark NLP Pipeline for Zero-Shot**

Spark NLP utilizes a modular pipeline:

1.  **Preprocessing:** Document Assembler, Sentence Detector (important for breaking up text so it fits the 512-token limit of BERT models and avoids clipping).

2.  **Zero-Shot NER:** Contextual Parser \$\rightarrow\$ Question Generator \$\rightarrow\$ Zero Shot NER.

3.  **Efficiency Step:** **NE Chunk Filterer**. This module filters the entities extracted by the NER model, instructing the RE model to only look for relations between specific entity pairs (e.g., only Patient and Date, filtering out other entity types). This reduces the number of questions the RE model must answer, significantly improving inference efficiency.

4.  **Zero-Shot RE:** Zero Shot RE model, using custom questions to establish relationship hierarchies.

This process results in a final output that includes both entities and the hierarchical relationships between them, all achieved without needing to label data. The core model running underneath must be appropriate for the domain (e.g., BioBERT for healthcare) to achieve the best results. The models are robust enough to handle typos and misspellings because the underlying BERT model was trained on noisy data.