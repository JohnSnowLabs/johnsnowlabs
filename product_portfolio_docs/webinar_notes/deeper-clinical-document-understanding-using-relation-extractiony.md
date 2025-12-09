# Deeper Clinical Document Understanding Using Relation Extractiony
Deeper Clinical Document Understanding Using Relation Extractiony

<https://www.johnsnowlabs.com/watch-the-webinar-deeper-clinical-document-understanding-using-relation-extraction/>

<https://www.youtube.com/watch?v=ETyEZE1T6hA>

<img src="/media/image.jpg" title="Video titled: [Webinar] Deeper Clinical Document Understanding Using Relation Extraction" style="width:6.3125in;height:3.65625in" />

The following is a detailed summary of the speech form the YouTube source, which discusses deeper clinical document understanding using Relation Extraction (RE).

The speaker, Hashem Alik, a data scientist at John Snow Labs, presents the work on relation extraction models, noting that the content is an extension of a paper published in AAAI '22.

### **The Motivation: Limitations of Named Entity Recognition (NER)**

The core problem addressed by RE is the limitation of traditional NER models. While NER successfully feeds in raw text and extracts entities (such as drugs or adverse events), these entities are often **disjoint and separate from each other**. For instance, in an Adverse Drug Event (ADE) example, NER might identify multiple drugs and multiple reactions, but the model does not indicate **which specific drug is responsible for which specific reaction**.

### **The Solution: Relation Extraction (RE)**

Relation Extraction is utilized as a layer placed on top of the NER model. Its primary function is to **semantically relate entities**, determining how entities are connected or which entity is responsible for another.

In a binary relationship example, the model determines whether a drug is responsible for a reaction or not. The presented results showed that while Lipitor was linked to reactions like fatigue, cramps, anxiety, and sadness, **Zocor was not responsible for any adverse reactions**. This type of relationship linking allows for a more granular understanding of the text. Relationships can also be of multiple types, such as **temporal relations**, where one event is determined to have happened after another.

### **Technical Approaches and State-of-the-Art Performance**

John Snow Labs has developed two main approaches for relation extraction, optimized for scalability:

1.  **Custom Feature-Engineered Fully Connected Neural Network:** This is considered the **lighter model** and is used for simpler problems, such as binary classification (like ADE, which involves only two classes). It is tuned for **maximum speed**. This model uses bespoke features, including the **dependency tree of the sentence**, token spans between two entities, and embeddings (both Glove and BERT-based).

2.  **BERT-based Model:** This approach is an extension of previous research. The sequence length is limited to 128 tokens. This BERT-based model is the **best performing one** and has been benchmarked on several datasets.

The BioBERT model developed by John Snow Labs is currently **state-of-the-art (SOTA)**. It has been tested on seven benchmark datasets, including Temporal, Clinical, Drug-Drug Interaction (DDI), ADE, Gene Relations, and Pathology relations. In some cases, the BioBERT model outperforms existing SOTA models by a great margin.

### **Real-World Applications of Relation Extraction**

By introducing relations, the models achieve more granularity and allow for structured output:

- **Parsing Prescriptions and Discharge Summaries:** RE links dosage and drugs to their frequencies and forms (e.g., oral). For example, the model can specify that one type of insulin has a dosage of 40 units, while another has 12 units with the frequency "with meals," and Metformin is taken two times a day. This provides more **precise chunks** of information linked together.

- **Generating Patient Timelines:** RE allows the extraction of dates and the linking of these dates to lab results or procedures. This is crucial for putting the **entire timeline of a patient on a chart**, tracking how test results (e.g., calcium scores) change across different reports and dates, allowing for the deduction of improvement or necessary action.

- **Knowledge Graph Generation (KGs):** Relations are described as playing the **most pivotal role** in generating knowledge graphs. The example of a radiology report demonstrates how RE integrates dates, procedures (CT scan), technique (multi-slice), body parts (chest, lung, kidney), findings (pleural effusion, cyst), measurements (9.8), and laterality (left lobe). The model identifies the type of relationship (e.g., finding and body part). This process converts a large, unstructured piece of text into **completely structured data with a hierarchy** (e.g., JSON output).

- **Precise Medical Coding:** Relating entities helps in achieving more **precise medical codes** (CPT or ICD codes). Instead of resolving "cyst" to an "unspecified" code, relating "cyst" to its body part "kidney" provides an enriched chunk that feeds into the resolver model, yielding better, more precise results.

### **Implementation in Spark NLP**

John Snow Labs offers multiple pre-trained models for RE within Spark NLP, each designed for specific conditions and entity pairs. The use of lighter models and the division of entities based on overlap are strategies used to avoid confusion. Examples of specific models mentioned include:

- re_ade (Adverse Drug Event, linking reaction and drug).

- bodypart_procedure_test (linking procedure/test like CT to body parts like chest).

- test_result_date.

- bodypart_problem (linking lung and pleural effusion).

- re_clinical: A multi-classification model with roughly seven classes that can determine not just if entities are related, but whether a drug cured a symptom or aggravated it.

The models are designed for ease of use. Pre-trained pipelines (such as explain_doc_ade) are available, containing NER, assertion, and relation extraction models in a single unit. To create custom pipelines, users can run a basic NER model and then use the **dependency structure of the document to filter out candidate relation pairs**. This dependency structure helps reduce computation cost by only classifying eligible pairs.