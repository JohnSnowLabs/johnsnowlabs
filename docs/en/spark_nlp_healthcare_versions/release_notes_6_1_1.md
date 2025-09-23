---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP v6.1.1 Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_6_1_1
key: docs-licensed-release-notes
modify_date: 2025-09-22
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.1.1

#### Highlights


We are delighted to announce **significant new features and major enhancements** in the latest release of Healthcare NLP.
This release introduces brand-new **Medical Vision language models (VLMs)**, new capabilities such as the new **Annotation2Training** module for converting annotations from GenAI Lab into trainable dataframes, the **MedicalNerDLGraphChecker** for well-informed NER training, domain-specific **LLM pipelines**, and **faster ONNX models**—a total of **78 new LLMs, pipelines, and ONNX models** available out of the box.

- Medical Vision LLM Models extend clinical AI with multimodal text and image understanding
- Pretrained Clinical Pipelines for LLMs deliver ready-to-use Q&A, NER, summarization, RAG, and chat
- Introducing `MedicalNerDLGraphChecker` improves graph management during medical NER training
- `Annotation2Training` converts GenAI Lab annotations into NER-ready training datasets
- Lightweight Text-to-SQL Model based on small LLMs enables seamless natural language queries on healthcare data
- Human phenotype ontology (HPO) Mapping Models and Pipeline standardize phenotype recognition and linking via returning exact, related, and broad synonyms for each term at once
- ONNX-Optimized MedicalBERT Models provide faster inference on CPU and GPU for certain tasks (NER, assertion)
- Cross-Framework Benchmarking compares TensorFlow, ONNX, and OpenVINO, with ONNX leading on GPU
- Additional De-Identification Enhancements strengthen HIPAA compliance and customization
- Structured JSON Converter with Mappers streamlines integration of structured data
- Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
  - Simplified Spark Session initialization
  - `ner_source` metadata key in IOBTagger
  - Consistent results with `genderAwareness=True` in DeIdentification
- Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
    - New [MedicalVisionLLM](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/MedicalVisionLLM.ipynb) MOOC Notebook
    - New [AssertionMerger](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/AssertionMerger.ipynb) MOOC Notebook
    - New [End2End Preannotation and Training Pipeline](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.14.End2End_Preannotation_and_Training_Pipeline.ipynb) Notebook
    - New [GenAI Lab to Ner Training](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.7.Generative_AI_to_Ner_Training.ipynb) Notebook
    - New [NER ASSERTIONS RULE BASED](https://demo.johnsnowlabs.com/healthcare/NER_ASSERTIONS_RULE_BASED/) Demo
    - Updated [MEDICAL LLM](https://demo.johnsnowlabs.com/healthcare/MEDICAL_LLM/) Demo
    - Updated [ENTITY RESOLUTION CODE MAPPING](https://demo.johnsnowlabs.com/healthcare/ER_CODE_MAPPING/) Demo
    - Updated [NER GENE PHENOTYPES](https://demo.johnsnowlabs.com/healthcare/NER_GENE_PHENOTYPES/) Demo

+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

</div><div class="h3-box" markdown="1">

#### Medical Vision LLM Models Extend Clinical AI with Multimodal Text and Image Understanding

In this release, we are expanding our Medical Vision LLM (VLM) family with additional models specifically finetuned for medical tasks. These models extend large language model capabilities with integrated visual language understanding, enabling multimodal clinical analysis by combining textual and image inputs.

The new VLMs provide strong performance for tasks such as diagnostic image interpretation, image-to-text summarization, and integrated documentation analysis — continuing our mission to advance clinical AI with robust, domain-specific multimodal solutions.


{:.table-model-big}
| **Model Name**             | **Quantization Options**   |
| -------------------------- | -------------------------- |
| jsl_meds_ner_vlm_8b_v1     | [q4](https://nlp.johnsnowlabs.com/2025/08/27/jsl_meds_ner_vlm_8b_q4_v1_en.html), [q8](https://nlp.johnsnowlabs.com/2025/08/27/jsl_meds_ner_vlm_8b_q8_v1_en.html), [q16](https://nlp.johnsnowlabs.com/2025/08/27/jsl_meds_ner_vlm_8b_q16_v1_en.html) |
| jsl_meds_ner_vlm_7b_v1     | [q4](https://nlp.johnsnowlabs.com/2025/09/16/jsl_meds_ner_vlm_7b_q4_v1_en.html), [q8](https://nlp.johnsnowlabs.com/2025/09/16/jsl_meds_ner_vlm_7b_q8_v1_en.html), [q16](https://nlp.johnsnowlabs.com/2025/09/16/jsl_meds_ner_vlm_7b_q16_v1_en.html) |


*Example*:

```python
prompt = """
# Template:
{
  "Patient Name": "string",
  "Patient Age": "integer",
  "Patient Gender": "string",
  "Hospital Number": "string",
  "Episode Number": "string",
  "Episode Date": "date-time"
}
# Context:
<image>
"""

input_df = nlp.vision_llm_preprocessor(
    spark=spark,
    images_path="images",
    prompt=prompt,
    output_col_name="prompt"
)

document_assembler = (
    nlp.DocumentAssembler()
    .setInputCol("prompt")
    .setOutputCol("caption_document")
)

image_assembler = (
    nlp.ImageAssembler()
    .setInputCol("image")
    .setOutputCol("image_assembler")
)

medicalVisionLLM = (
    medical.AutoGGUFVisionModel.pretrained("jsl_meds_ner_vlm_8b_q16_v1", "en", "clinical/models")
    .setInputCols(["caption_document", "image_assembler"])
    .setOutputCol("completions")
)

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    image_assembler,
    medicalVisionLLM
])

model = pipeline.fit(input_df)
result = model.transform(input_df)
```

*Result*:

```bash
{
    "Patient Name": "Ms RUKHSANA SHAHEEN",
    "Patient Age": 56,
    "Patient Gender": "Female",
    "Hospital Number": "MH005990453",
    "Episode Number": "030000528270",
    "Episode Date": "2021-07-02T08:31:00"
}
```




</div><div class="h3-box" markdown="1">

####  Pretrained Clinical Pipelines for LLMs Deliver ready-to-use Q&A, NER, summarization, RAG, and chat

This release introduces a new collection of pretrained clinical LLM pipelines, designed to streamline clinical document analysis. Each pipeline is built on top of state-of-the-art small-sized Medical LLMs finetuned by us, providing ready-to-use solutions for Q&A, NER, Summarization, Retrieval-Augmented Generation (RAG), and Chat.

The main advantage of these pipelines is the elimination of manual model chaining. Instead of building and testing complex workflows, users can instantly deploy one-liner pipelines that are efficient, accurate, and purpose-built for clinical tasks — reducing setup time while maintaining high performance.


{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`jsl_meds_4b_q16_v4_pipeline`](https://nlp.johnsnowlabs.com/2025/08/16/jsl_meds_4b_q16_v4_pipeline_en.html) |  Q&A, NER, Summarization, RAG, and Chat. |
| [`jsl_meds_8b_q8_v4_pipeline`](https://nlp.johnsnowlabs.com/2025/08/16/jsl_meds_8b_q8_v4_pipeline_en.html) |  Q&A, NER, Summarization, RAG, and Chat. |
| [`jsl_meds_ner_2b_q16_v2_pipeline`](https://nlp.johnsnowlabs.com/2025/08/16/jsl_meds_ner_2b_q16_v2_pipeline_en.html) |  Q&A, NER, Summarization, RAG, and Chat. |
| [`jsl_meds_ner_q16_v4_pipeline`](https://nlp.johnsnowlabs.com/2025/08/16/jsl_meds_ner_q16_v4_pipeline_en.html) |  Q&A, NER |
| [`jsl_meds_ner_vlm_2b_q16_v2_pipeline`](https://nlp.johnsnowlabs.com/2025/08/16/jsl_meds_ner_vlm_2b_q16_v2_pipeline_en.html) |  Q&A, NER |


*Example*:

```python
from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("jsl_meds_ner_2b_q16_v2_pipeline", "en", "clinical/models")

text = """
# Template:
{
  "Patient Name": "string",
  "Patient Age": "integer",
  "Patient Gender": "string",
  "Hospital Number": "string",
  "Episode Number": "string",
  "Episode Date": "date-time"
}
# Context:
The patient, Johnathan Miller, is a 54-year-old male admitted under hospital number HN382914. 
His most recent episode number is EP2024-1178, recorded on 2025-08-10. 
The patient presented with chronic knee pain and swelling. 
Past medical history includes hypertension and type 2 diabetes.
"""
```

*Result*:

```bash
{
    "Patient Name": "Johnathan Miller",
    "Patient Age": 54,
    "Patient Gender": "male",
    "Hospital Number": "HN382914",
    "Episode Number": "EP2024-1178",
    "Episode Date": "2025-08-10"
}
```

Please check [Loading Medical and Open Source LLMs]([https://nlp.johnsnowlabs.com/docs/en/benchmark#deidentification-benchmarks](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/36.0.Loading_Medical_and_Open_Source_LLMs.ipynb)) notebook for more detail



</div><div class="h3-box" markdown="1">

#### Introducing `MedicalNerDLGraphChecker` Improves Graph Management During Medical NER Training

This release introduces a new annotator, `MedicalNerDLGraphChecker`, designed to verify whether a suitable MedicalNerApproach TensorFlow graph is available for a given training dataset before computation begins. This prevents runtime errors and ensures that the correct graph is used for custom training workflows.

Along with the new annotator, we have added ~80 new graph files to support a wider range of configurations.

The `MedicalNerDLGraphChecker` must be placed before embeddings or MedicalNerApproach annotators in the pipeline. It processes the dataset to extract required graph parameters (tokens, labels, embedding dimensions) and raises an exception if the appropriate graph is missing in the JAR. This makes it especially useful for custom datasets and specialized NER training cases.


*Example*:

```python
nerDLGraphChecker = (MedicalNerDLGraphChecker()
            .setInputCols(["sentence", "token"])
            .setLabelColumn("label")
            .setEmbeddingsModel(embeddings))
            
nerDLGraphChecker.fit(train_df)
```

> **Note**: The `MedicalNerDLGraphChecker` automatically validates whether a suitable TensorFlow graph is bundled inside the JAR for the specified embeddings and labels.
>
> - If a required graph is **not found**, it will raise a detailed error message, guiding you on what configuration is missing.
> - If a suitable graph **is found**, it runs silently, confirming that the embedded graph is compatible, and you can proceed with training without manually creating graph files.


</div><div class="h3-box" markdown="1">

#### `Annotation2Training` Converts GenAI Lab Annotations into NER-ready Training Datasets

We’re introducing `Annotation2Training`, a utility that converts annotation outputs (from JSON or CSV) into a Spark DataFrame ready for NER training. It expects inputs structured like John Snow Labs’ Generative AI annotation tool exports and produces token-level labels aligned with sentences and documents.

🚀 **_Features & Highlights_**
- **Converts GenAI Exports to NER Training DataFrames**
  - `convertJson2NerDF`
  - `convertCsv2NerDF`
- **Practical & Easy-to-Use**: Convert JSON or CSV files directly into Spark DataFrames with a single function call.
- **Fast & Scalable**: Optimized partitioning ensures high performance, leveraging system CPU cores for parallel processing.
- **Base Pipeline Compatibility**: Works with your base pipeline (e.g., `DocumentAssembler`, `SentenceDetector`, `InternalDocumentSplitter`, and `Tokenizer`).
- **NER Training Ready**: Use this to streamline data prep for `MedicalNerApproach` and other NER trainers—no manual wrangling, consistent columns, and validated alignment out of the box.
- **Modern Alternative**: Eliminates the complexity of traditional **CoNLL-based approach**, providing a more efficient and reliable workflow.

*Example*:

```python
JSON_PATH = "/content/result.json"

from sparknlp_jsl.training import Annotation2Training
annotation2training = Annotation2Training(spark)
training_df_json = annotation2training.convertJson2NerDF(
    json_path = JSON_PATH,                   # Path to the input JSON file.
    pipeline_model = base_pipeline_model,    # A pre-trained Spark NLP PipelineModel that includes at least a DocumentAssembler, and Tokenizer.
    repartition = (os.cpu_count() * 4),      # Number of partitions to use when creating the DataFrame (default is 32).
    token_output_col = "token",              # The name of the column containing token annotations (default is "token").
    ner_label_col = "label")                 # The name of the output column for NER labels (default is "label").
```

Please check the [1.7.GenAI Lab_to_Ner_Training.ipynb](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.7.Generative_AI_to_Ner_Training.ipynb) Notebook


</div><div class="h3-box" markdown="1">

#### Lightweight Text-to-SQL Model Enables Seamless Natural Language Queries on Healthcare Data

We are releasing a new Text-to-SQL model fine-tuned by John Snow Labs for the healthcare domain based on small LLMs. The `jsl_meds_text2sql_1b_q16_v1` model is lightweight and optimized for transforming natural language queries into SQL, enabling seamless interaction with structured medical and healthcare datasets.

*Example*:

```python
medical_llm = MedicalLLM.pretrained("jsl_meds_text2sql_1b_q16_v1", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(100)\
    .setUseChatTemplate(True)\
    .setTemperature(0)

medm_prompt = """### Instruction:
### Instruction:
Table: CancerPatients
- patient_id (INT)
- name (VARCHAR)
- age (INT)
- gender (VARCHAR)
- cancer_type (VARCHAR)
- diagnosis_date (DATE)
List the names of patients diagnosed with breast cancer.
### Response:
"""
```

*Results*:

```bash
SELECT name FROM CancerPatients WHERE cancer_type = 'breast cancer'
```


</div><div class="h3-box" markdown="1">

#### HPO Mapping Models and Pipeline Standardize Phenotype Recognition and Linking

We are introducing new resources for phenotype extraction and ontology mapping. Together, the `hpo_synonym_mapper` model and the `hpo_mapper_pipeline_v4` pipeline enable comprehensive recognition and standardization of phenotypic concepts in clinical and biomedical text.

- The `pretrained model` maps Human Phenotype Ontology (HPO) terms to their exact, related, and broad synonyms, ensuring consistent representation of phenotypic concepts.
- The `pretrained pipeline` extracts phenotype-related entities, maps them to HPO codes, determines assertion status (present, absent, suspected), and enriches the results by linking to UMLS CUIs, genes, and associated diseases.

These tools provide a powerful way to achieve deeper phenotypic and genomic insights directly from unstructured text, supporting downstream clinical and biomedical applications.


{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`hpo_synonym_mapper`](https://nlp.johnsnowlabs.com/2025/09/04/hpo_synonym_mapper_en.html) |  Maps HPO terms to their exact, related, and broad synonyms |
| [`hpo_mapper_pipeline_v4`](https://nlp.johnsnowlabs.com/2025/09/04/hpo_mapper_pipeline_v4_en.html) |  Designed to extract phenotype-related entities from clinical or biomedical text, map them to their corresponding Human Phenotype Ontology (HPO) codes, and determine their assertion status |


*Example*:

```python
mapperModel = ChunkMapperModel.pretrained("hpo_synonym_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["synonym"])

result = model.transform(spark.createDataFrame([["""The patient, a 62-year-old male, presented with a neoplasm in the lung. He also reported progressive fatigue over the past three months and episodes of shortness of breath. On examination, hepatomegaly was noted, and laboratory results confirmed anemia."""]]).toDF("text"))
```


*Results*:

{:.table-model-big}
|term               |synonym                                                                                                                                                                                                                 |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|shortness of breath|{'exact_synonym': ['dyspnea', 'abnormal breathing', 'breathing difficulty', 'difficult to breathe', 'difficulty breathing', 'dyspnoea', 'trouble breathing'], 'related_synonym': ['panting'], 'broad_synonym': []}      |
|fatigue            |{'exact_synonym': ['fatigue', 'tired', 'tiredness'], 'related_synonym': [], 'broad_synonym': []}                                                                                                                        |
|neoplasm           |{'exact_synonym': ['neoplasia', 'oncological abnormality', 'tumor', 'tumour'], 'related_synonym': ['cancer', 'oncology'], 'broad_synonym': ['abnormal tissue mass']}                                                    |
|anemia             |{'exact_synonym': ['anaemia', 'low number of red blood cells or haemoglobin', 'low number of red blood cells or hemoglobin'], 'related_synonym': ['decreased haemoglobin', 'decreased hemoglobin'], 'broad_synonym': []}|
|progressive        |{'exact_synonym': ['worsens with time'], 'related_synonym': ['progressive disorder'], 'broad_synonym': []}                                                                                                              |
|hepatomegaly       |{'exact_synonym': ['enlarged liver'], 'related_synonym': [], 'broad_synonym': []}                                                                                                                                       |


</div><div class="h3-box" markdown="1">

#### ONNX-Optimized MedicalBERT Models Provide Faster Inference on CPU and GPU

We have converted multiple `MedicalBertForSequenceClassification` and `MedicalBertForTokenClassifier` models into ONNX format, enabling significant speed improvements when running on CPU and especially GPU.
This conversion allows users to leverage the efficiency of ONNX Runtime, resulting in faster inference times. The new models ends with `_onnx` in their names to easily identify them.


*Example*:

```python
sequence_classification = (
    MedicalBertForSequenceClassification.pretrained(
        "bert_sequence_classifier_ade_augmented_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "sentence"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

data = spark.createDataFrame(["So glad I am off effexor, so sad it ruined my teeth. tip Please be carefull taking antideppresiva and read about it 1st",
                              "Religare Capital Ranbaxy has been accepting approval for Diovan since 2012"], StringType()).toDF("text")
```



*Results*:

{:.table-model-big}
|text                                                                                                                   |result |
|-----------------------------------------------------------------------------------------------------------------------|-------|
|So glad I am off effexor, so sad it ruined my teeth. tip Please be carefull taking antideppresiva and read about it 1st|[ADE]  |
|Religare Capital Ranbaxy has been accepting approval for Diovan since 2012                                             |[noADE]|



</div><div class="h3-box" markdown="1">

#### Cross-Framework Benchmarking compares TensorFlow, ONNX, and OpenVINO, with ONNX leading on GPU

This benchmark evaluates the performance of Spark NLP for Healthcare models across three different architectures (TensorFlow, ONNX, OpenVINO) on both CPU and GPU hardware.
Key findings show ONNX consistently delivers superior performance on GPU environments.

- **Datasets:**
  - **MTSamples Dataset:** 1,000 clinical texts, ~500 tokens per text
    - *Usage:* General NER and embedding benchmarks
  - **Assertion Test Dataset:** 7,570 labeled rows
    - *Usage:* BertForAssertionClassification evaluation
- **Versions:**
  - **spark-nlp Version:** v6.1.1
  - **spark-nlp-jsl Version :** v6.1.0
  - **Spark Version :** v3.5.1
- **Instance Types:**
  - **CPU Machine:** Colab V6e-1, 173.0 GB RAM, 44 vCPUs
  - **GPU Machine:** Colab A100, 83.5 GB RAM, 40.0 GB GPU VRAM, 12 vCPUs
- **Models Tested:**
  - **BertSentenceEmbeddings** → `sbiobert_base_cased_mli`
  - **MedicalBertForSequenceClassification** → `bert_sequence_classifier_ade`
  - **BertForAssertionClassification** → `assertion_bert_classification_oncology`
  - **MedicalBertForTokenClassifier** → `bert_token_classifier_ner_clinical`
  - **PretrainedZeroShotNER** → `zeroshot_ner_deid_subentity_merged_medium`
  - **WordEmbeddings + MedicalNerModel** → `embeddings_clinical` + `ner_deid_subentity_augmented`
  - **WordEmbeddings + 2 MedicalNerModel** → `embeddings_clinical` + `ner_deid_subentity_augmented` + `ner_deid_generic_docwise`

- **NOTES:**
  - This benchmark compares Transformer architectures and ML models across CPU and GPU environments
  - **Hardware Context:** CPU and GPU machines differ in cores and memory; comparisons should consider these hardware variations
  - **Preprocessing:** DocumentAssembler, SentenceDetector, and Tokenizer stages were pre-processed; reported times reflect pure model execution
  - **Configuration:** All models executed with default settings
  - **Timing Methodology:**
    ```python
    %%timeit -n 3 -r 1
    model.write.mode("overwrite").format("noop").save()
    ```
  - **Results:** Numbers represent average execution times across runs
- **Base Pipeline Configuration:**
  ```python
  basePipeline = Pipeline(
      stages=[
          documentAssembler,
          sentenceDetector,
          tokenizer
      ])
  ```

##### CPU Benchmarking

{:.table-model-big}
| Model                                |TensorFlow         | ONNX             | OpenVINO         |
|:-------------------------------------|------------------:|-----------------:|-----------------:|
| BertSentenceEmbeddings               |      8 min 37 sec |     4 min 46 sec |     3 min 31 sec |
| MedicalBertForSequenceClassification |      3 min 30 sec |     2 min 47 sec |              N/A |
| BertForAssertionClassification       |            57 sec |           33 sec |              N/A |
| MedicalBertForTokenClassifier        |      3 min 29 sec |     2 min 46 sec |              N/A |
| PretrainedZeroShotNER                |               N/A |    38 min 10 sec |              N/A |
| WordEmbeddings + MedicalNerModel     |            25 sec |              N/A |              N/A |
| WordEmbeddings + 2 MedicalNerModel   |            38 sec |              N/A |              N/A |


##### GPU Benchmarking

{:.table-model-big}
| Model                                |TensorFlow         | ONNX             | OpenVINO         |
|:-------------------------------------|------------------:|-----------------:|-----------------:|
| BertSentenceEmbeddings               |     28 min 50 sec |           12 sec |    18 min 49 sec |
| MedicalBertForSequenceClassification |     11 min 45 sec |           28 sec |              N/A |
| BertForAssertionClassification       |      3 min 24 sec |            8 sec |              N/A |
| MedicalBertForTokenClassifier        |     11 min 47 sec |           26 sec |              N/A |
| PretrainedZeroShotNER                |               N/A |      1 min 1 sec |              N/A |
| WordEmbeddings + MedicalNerModel     |      2 min 24 sec |              N/A |              N/A |
| WordEmbeddings + 2 MedicalNerModel   |       4 min 8 sec |              N/A |              N/A |




</div><div class="h3-box" markdown="1">

#### De-Identification Enhancements strengthen HIPAA compliance and customization

This release introduces new parameters that give users more flexibility and control over how sensitive information is obfuscated, while also ensuring alignment with HIPAA Safe Harbor requirements.

- **ZIP Code Obfuscation (HIPAA Safe Harbor)**  
  A new parameter `obfuscateZipByHipaa` allows users to enforce HIPAA-compliant ZIP code handling.  
  When enabled, ZIP and ZIP+4 codes are automatically masked according to HIPAA Safe Harbor rules: restricted prefixes are fully suppressed, and all others are generalized to protect patient privacy.  
  When disabled, the system falls back to default/custom ZIP obfuscation rules, offering freedom for alternative strategies.

```python
data = [
    ("Patient lives at 123 Main St, ZIP 12345-6789, with mild asthma.",),
    ("The clinic in ZIP 03690 treated the patient for diabetes.",),
    ("Follow-up scheduled at ZIP 90210 for hypertension check.",)
]
df = spark.createDataFrame(data, ["text"])

deidentification = LightDeIdentification()\
    .setInputCols(["document", "chunk"])\
    .setOutputCol("deid")\
    .setMode("obfuscate")\
    .setObfuscateZipByHipaa(True)    
```
*Results*:

```bash
+---------------------------------------------------------------+
|deid                                                           |
+---------------------------------------------------------------+
|Patient lives at 123 Main St, ZIP 123**-****, with mild asthma.|
|The clinic in ZIP 000** treated the patient for diabetes.      |
|Follow-up scheduled at ZIP 902** for hypertension check.       |
+---------------------------------------------------------------+
```

- **Date Obfuscation Flexibility**  

The `maxRandomDisplacementDays` parameter provides fine-grained control over the extent to which date values can be randomly shifted when randomization is enabled. This ensures a balanced trade-off between data utility and privacy.
When an ID column (e.g., patient identifier) is provided, all dates linked to the same ID will be displaced by the *same amount*. This preserves the relative temporal relationships within a patient’s timeline, while still protecting sensitive information.

*Example:*
```python
data = [
    ("PAT-0001", "Patient was admitted on 11/11/2020."),
    ("PAT-0001", "Follow-up scheduled for 13/11/2020."),
    ("PAT-0002", "Discharge planned on 15/11/2020."),
    ("PAT-0002", "Next appointment set for 17/11/2020.")
]
df = spark.createDataFrame(data, ["ID", "text"])
```

*Define DeIdentification and Pipeline*

```python
documentAssembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document") \
    .setIdCol("ID")

dateMatcher = RegexMatcherInternalModel.pretrained("date_matcher", "en") \
    .setInputCols(["document"]) \
    .setOutputCol("date")

deIdentification = LightDeIdentification() \
    .setInputCols(["date", "document"]) \
    .setOutputCol("dei") \
    .setMode("obfuscate") \
    .setObfuscateDate(True) \
    .setMaxRandomDisplacementDays(60) \
    .setIsRandomDateDisplacement(True) \
    .setSeed(1000)

pipeline = Pipeline(stages=[
    documentAssembler,
    dateMatcher,
    deIdentification
])

result = pipeline.fit(df).transform(df)
result.select("ID", "text", "dei.result").show(truncate=False)
```
*Results*:

```bash
+--------+------------------------------------+--------------------------------------+
|ID      |text                                |result                                |
+--------+------------------------------------+--------------------------------------+
|PAT-0001|Patient was admitted on 11/11/2020. |[Patient was admitted on 16/11/2020.] |
|PAT-0001|Follow-up scheduled for 13/11/2020. |[Follow-up scheduled for 18/11/2020.] |
|PAT-0002|Discharge planned on 15/11/2020.    |[Discharge planned on 06/12/2020.]    |
|PAT-0002|Next appointment set for 17/11/2020.|[Next appointment set for 08/12/2020.]|
+--------+------------------------------------+--------------------------------------+
```

These improvements empower users to adopt stricter compliance when required, while also maintaining flexibility for research, testing, or custom obfuscation needs.


</div><div class="h3-box" markdown="1">

#### `StructuredJsonConverter` with Mappers streamlines integration of structured data

We have added support for mappers in StructuredJsonConverter, making it easier to transform and normalize extracted entity outputs into custom schemas. This enhancement allows developers to map model outputs (e.g., synonyms, IDs, or ontology codes) directly into a structured JSON format that aligns with their downstream applications.

*Example*:

```python
ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

hpo_mapper = ChunkMapperModel().pretrained("hpo_mapper", "en", "clinical/models") \
    .setInputCols(["ner_chunk"]) \
    .setOutputCol("hpo_code") \
    .setLowerCase(False)

from sparknlp_jsl.pipeline_tracer import PipelineTracer
tracer = PipelineTracer(base_model)
columns_schema = tracer.createParserDictionary()
columns_schema
```
*Schema of the StructuredJsonConverter*:
```bash
{'document_identifier': '',
 'document_text': 'document',
 'entities': ['ner_chunk'],
 'assertions': [],
 'resolutions': [],
 'relations': [],
 'summaries': [],
 'deidentifications': [],
 'classifications': [],
 'mappers': ['hpo_code']}
```

*Define StructuredJsonConverter And Transform*

```python
converter = StructuredJsonConverter() \
.setOutputCol("json") \
.setConverterSchema(columns_schema) \
.setOutputAsStr(False) \
.setCleanAnnotations(True)

json_df = converter.transform(base_df)
mappers_json_output = json_df.select("json.mappers").collect()[0][0]
mappers_json_output
```
*Result*:
```bash
[{'sentence': '0',
  'resolved_text': 'HP:0001249',
  'distance': '0.0',
  'all_relations': '',
  'chunk': 'intellectual disability',
  'ner_source': 'ner_chunk',
  'ner_confidence': '0.99325',
  'chunk_id': '30e08780',
  'relation': 'hpo_code',
  'ner_label': 'HP',
  'all_k_distances': '0.0:::0.0',
  'all_k_resolutions': 'HP:0001249',
  'end': '49',
  'begin': '27'}]
```

</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, and Reliability of Spark NLP for Healthcare

- Simplified Spark Session initialization

Starting a Spark NLP for Healthcare session is now easier and more flexible.  
Previously, a `secret` had to be explicitly passed to the `start()` function:
```python
spark = sparknlp_jsl.start(secret = "YOUR_SECRET_HERE")
```
With this release, the library can automatically read the secret from the environment variable `SECRET`, so you can simply run:
```python
spark = sparknlp_jsl.start()
```
This improvement makes session startup simpler, more user-friendly, and adaptable across different environments.

- Disabled llama.cpp logs in LLM annotators

LLM annotators in Spark NLP for Healthcare now run with **llama.cpp logs disabled** by default.  
  This change provides a **cleaner and less verbose output**, making it easier to focus on the actual results.

- `ner_source` metadata key in IOBTagger

The `IOBTagger` annotator now enriches its metadata with a new field: **`ner_source`**.  
This field indicates the originating chunk for each created token. This enhancement provides:
  - **Better monitoring** of token generation
  - **Improved traceability** between chunks and their derived tokens

With this addition, users gain **deeper insights** into the tokenization process and can more easily debug or analyze entity extraction workflows.

- Consistent Results with `genderAwareness=True` in DeIdentification
Fixed an issue in **DeIdentification** where enabling `genderAwareness=True` produced inconsistent results for names with three parts (`[first_name, middle_name, last_name]`).  
Now, both two-part and three-part names are handled consistently.



</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For Making Spark NLP For Healthcare Easier To Navigate And Understand

- New [MedicalVisionLLM](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/MedicalVisionLLM.ipynb) MOOC Notebook
- New [AssertionMerger](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/AssertionMerger.ipynb) MOOC Notebook
- New [End2End Preannotation and Training Pipeline](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.14.End2End_Preannotation_and_Training_Pipeline.ipynb) Notebook
- New [Generative AI to Ner Training](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.7.Generative_AI_to_Ner_Training.ipynb) Notebook
- New [NER ASSERTIONS RULE BASED](https://demo.johnsnowlabs.com/healthcare/NER_ASSERTIONS_RULE_BASED/) Demo
- Updated [MEDICAL LLM](https://demo.johnsnowlabs.com/healthcare/MEDICAL_LLM/) Demo
- Updated [ENTITY RESOLUTION CODE MAPPING](https://demo.johnsnowlabs.com/healthcare/ER_CODE_MAPPING/) Demo
- Updated [NER GENE PHENOTYPES](https://demo.johnsnowlabs.com/healthcare/NER_GENE_PHENOTYPES/) Demo


</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.


+ `jsl_meds_4b_q16_v4_pipeline`            
+ `jsl_meds_8b_q8_v4_pipeline`
+ `jsl_meds_ner_2b_q16_v2_pipeline`
+ `jsl_meds_ner_q16_v4_pipeline`
+ `jsl_meds_ner_vlm_2b_q16_v2_pipeline`
+ `jsl_meds_ner_vlm_8b_q16_v1`
+ `jsl_meds_ner_vlm_8b_q8_v1`
+ `jsl_meds_ner_vlm_8b_q4_v1`
+ `jsl_meds_ner_vlm_7b_q4_v1`
+ `jsl_meds_ner_vlm_7b_q8_v1`
+ `jsl_meds_ner_vlm_7b_q16_v1`
+ `hpo_synonym_mapper`
+ `hpo_mapper_pipeline_v4`
+ `jsl_meds_text2sql_1b_q16_v1`
+ `bert_sequence_classifier_ade_augmented_onnx`
+ `bert_sequence_classifier_ade_augmented_v2_onnx`
+ `bert_sequence_classifier_age_group_onnx`
+ `bert_sequence_classifier_binary_rct_biobert_onnx`
+ `bert_sequence_classifier_biomarker_onnx`
+ `bert_sequence_classifier_clinical_sections_headless_onnx`
+ `bert_sequence_classifier_covid_sentiment_onnx`
+ `bert_sequence_classifier_drug_reviews_webmd_onnx`
+ `bert_sequence_classifier_exact_age_reddit_onnx`
+ `bert_sequence_classifier_gender_biobert_onnx`
+ `bert_sequence_classifier_health_mandates_premise_tweet_onnx`
+ `bert_sequence_classifier_health_mandates_stance_tweet_onnx`
+ `bert_sequence_classifier_health_mentions_bert_onnx`
+ `bert_sequence_classifier_health_mentions_medbert_onnx`
+ `bert_sequence_classifier_metastasis_onnx`
+ `bert_sequence_classifier_patient_complaint_onnx`
+ `bert_sequence_classifier_patient_urgency_onnx`
+ `bert_sequence_classifier_pico_biobert_onnx`
+ `bert_sequence_classifier_rct_biobert_onnx`
+ `bert_sequence_classifier_response_to_treatment_onnx`
+ `bert_sequence_classifier_sdoh_community_absent_status_onnx`
+ `bert_sequence_classifier_sdoh_community_present_status_onnx`
+ `bert_sequence_classifier_sdoh_environment_status_onnx`
+ `bert_sequence_classifier_sdoh_frailty_onnx`
+ `bert_sequence_classifier_sdoh_frailty_vulnerability_onnx`
+ `bert_sequence_classifier_sdoh_mental_health_onnx`
+ `bert_sequence_classifier_sdoh_violence_abuse_onnx`
+ `bert_sequence_classifier_self_reported_age_tweet_onnx`
+ `bert_sequence_classifier_self_reported_partner_violence_tweet_onnx`
+ `bert_sequence_classifier_self_reported_stress_tweet_onnx`
+ `bert_sequence_classifier_self_reported_symptoms_tweet_onnx`
+ `bert_sequence_classifier_self_reported_vaccine_status_tweet_onnx`
+ `bert_sequence_classifier_stressor_onnx`
+ `bert_sequence_classifier_treatment_changes_sentiment_tweet_onnx`
+ `bert_sequence_classifier_vaccine_sentiment_onnx`
+ `bert_sequence_classifier_vop_adverse_event_onnx`
+ `bert_sequence_classifier_vop_drug_side_effect_onnx`
+ `bert_sequence_classifier_vop_hcp_consult_onnx`
+ `bert_sequence_classifier_vop_self_report_onnx`
+ `bert_sequence_classifier_vop_side_effect_onnx`
+ `bert_sequence_classifier_vop_sound_medical_onnx`
+ `bert_token_classifier_ade_tweet_binary_onnx`
+ `bert_token_classifier_drug_development_trials_onnx`
+ `bert_token_classifier_ner_ade_binary_onnx`
+ `bert_token_classifier_ner_ade_onnx`
+ `bert_token_classifier_ner_anatem_onnx`
+ `bert_token_classifier_ner_anatomy_onnx`
+ `bert_token_classifier_ner_bacteria_onnx`
+ `bert_token_classifier_ner_bc2gm_gene_onnx`
+ `bert_token_classifier_ner_bc4chemd_chemicals_onnx`
+ `bert_token_classifier_ner_bc5cdr_chemicals_onnx`
+ `bert_token_classifier_ner_bc5cdr_disease_onnx`
+ `bert_token_classifier_ner_bionlp_onnx`
+ `bert_token_classifier_ner_cellular_onnx`
+ `bert_token_classifier_ner_chemicals_onnx`
+ `bert_token_classifier_ner_chemprot_onnx`
+ `bert_token_classifier_ner_clinical_onnx`
+ `bert_token_classifier_ner_clinical_trials_abstracts_onnx`
+ `bert_token_classifier_ner_deid_onnx`
+ `bert_token_classifier_ner_drugs_onnx`
+ `bert_token_classifier_ner_jnlpba_cellular_onnx`
+ `bert_token_classifier_ner_jsl_onnx`
+ `bert_token_classifier_ner_jsl_slim_onnx`
+ `bert_token_classifier_ner_linnaeus_species_onnx`
+ `bert_token_classifier_ner_living_species_onnx`
+ `bert_token_classifier_ner_ncbi_disease_onnx`
+ `bert_token_classifier_ner_pathogen_onnx`
+ `bert_token_classifier_ner_species_onnx`



</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">

## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
