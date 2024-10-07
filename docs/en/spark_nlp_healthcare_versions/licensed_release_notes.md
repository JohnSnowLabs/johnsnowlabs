---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2024-10-07
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.5.0

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of Healthcare NLP. **This release comes with a brand new LLM Loader module with GPU support, several other new modules (Contextual Entity Filterer, RE Chunk Merger, Replacer) for precise and improved information extraction as well as 71 new clinical pretrained models and pipelines**. 

+ Introducing a brand new LLM loader called `MedicalLLM` to load and run LLMs in gguf format that could scale within a Spark NLP pipeline. 
+ Explore 6 new specialized LLMs at various sizes and quantization levels for healthcare applications (medical note summarization, Q&A, RAG, and Chat)
+ Clinical document analysis with one-liner pretrained pipelines for specific clinical tasks and concepts
+ Introducing 8 new Named Entity Recognition (NER) Models and pipelines to Detect PHI for Deidentification with minimal customization required
+ Introducing a new mapper model designed to link `ICD-10-CM codes` with their corresponding chronicity indicators
+ Introducing a new Named Entity Recognition (NER) Model and a new binary classification model to detect adverse drug events
+ Introducing the `REChunkMerger` annotator to merge the entities in a relationship as a single entity.
+ Introducing a brand new `ContextualEntityFilter` annotator to filter entities with context-specific rules.
+ Enhanced new sentence detector model for healthcare text segmentation in a corrupted text.
+ Introducing new parameters to `Replacer` for data augmentation.
+ New speed benchmarks for multi-NER pipelines
+ New blog posts on various topics (AI for equity, detecting stigmatizing language from medical texts, subcohort analysis for oncology patients, using small LLMs to extract structured named entities, ...)
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
    - Using structured entity jsons from various sources (pipeline, NLP Lab, etc) within a new pipeline to merge/ consolidate named entities.
    - Introducing new `setReturnEntityMappings`, `setMappingsColumn`, `setStaticEntityMappings`, and `setStaticEntityMappingsFallback` parameters for Replacer
    - Added the `RegexMatcherInternalModel` trait to Scala to match the pretrained method available in Python.
    - Added a new parameter for the `Flattener` annotator to sets an array of column names that should be kept in the dataframe after the flattening process.
    - Added `resetSentenceIndices` parameter to `ChunkMerger`, `NerConverterInternal`, and `ChunkConverter` annotators for reset sentence indices to treat the entire output as if it originates from a single document.
    - Fixed Generative AI Lab API task deletion endpoint: Resolved an issue with the `tasks_delete` endpoint, enabling proper deletion of tasks via the API.
    - Added `chunk_validation_options` dictionary into the `dict_to_annotation_converter` module for converting dictionary data to Spark NLP annotations.
    - Added pretrained feature added to `InternalDocumentSplitter`.
    - Deprecated the `nlp_test` module in `spark-nlp-jsl`; future development is being managed by `LangTest`.
    - Added support for `ONNX` models in the `ChunkKeyPhraseExtraction` annotator, allowing for compatibility with ONNX-based models.
+ Updated notebooks and demonstrations for making Healthcare NLP easier to navigate and understand
    - New [REChunkMerger](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/REChunkMerger.ipynb) MOOC Notebook
    - New [ContextualEntityFilterer](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ContextualEntityFilterer.ipynb) MOOC Notebook
    - Updated [Replacer](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/Replacer.ipynb) MOOC Notebook
    - Updated [NerConverterInternal](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/NerConverterInternal.ipynb) MOOC Notebook
    - Updated [ChunkConverter](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ChunkConverter.ipynb) MOOC Notebook
    - Updated [ChunkMergeModel](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ChunkMergeModel.ipynb) MOOC Notebook
    - Updated [Rule Based Entity Matchers](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.Rule_Based_Entity_Matchers.ipynb) notebook
    - Updated [Clinical DeIdentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.Clinical_DeIdentification.ipynb) notebook
    - Updated [Prepare CoNLL from Annotations for NER](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.3.prepare_CoNLL_from_annotations_for_NER.ipynb) notebook
    - Updated [Contextual Parser Rule Based NER](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.2.Contextual_Parser_Rule_Based_NER.ipynb) notebook
    - Updated [Loading Medical and Open Souce LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) notebook
    - Updated [ONCOLOGY Demo](https://demo.johnsnowlabs.com/healthcare/ONCOLOGY/)
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.



</div><div class="h3-box" markdown="1">

####  Introducing a Brand New LLM Loader Called `MedicalLLM` to Load and Aun LLMs in GGUF Format that Could Scale within a Spark NLP Pipeline. 

`MedicalLLM` is a brand new annotator in Spark NLP, designed to load and run large language models (LLMs) in `GGUF` format with scalable performance. Ideal for clinical and healthcare applications, MedicalLLM supports tasks like medical entity extraction, summarization, Q&A, Retrieval Augmented Generation (RAG), and conversational AI. With simple integration into Spark NLP pipelines, it allows for customizable batch sizes, prediction settings, and chat templates. GPU optimization is also available, enhancing its capabilities for high-performance environments. MedicalLLM empowers users to link medical entities and perform complex NLP tasks with efficiency and precision.

{:.table-model-big}
| Model Name              | Description |
|-------------------------|-------------|
|[jsl_meds_ner_q4_v2](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb)   | Extract and link medical named entities  |
|[jsl_meds_ner_q8_v2](https://nlp.johnsnowlabs.com/2024/10/04/jsl_meds_ner_q8_v2_en.html)   | Extract and link medical named entities  |
|[jsl_meds_ner_q16_v2](https://nlp.johnsnowlabs.com/2024/10/04/jsl_meds_ner_q16_v2_en.html)  | Extract and link medical named entities  |
|[jsl_medm_q4_v1](https://nlp.johnsnowlabs.com/2024/10/04/jsl_medm_q4_v1_en.html)       | Summarization and Q&A |
|[jsl_medm_q8_v1](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb)       | Summarization and Q&A |
|[jsl_medm_q16_v1](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb)      | Summarization and Q&A |
|[jsl_medsner_zs_q4_v1](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) | Extract and link medical named entities |
|[jsl_medsner_zs_q8_v1](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) | Extract and link medical named entities |
|[jsl_medsner_zs_q16_v1](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb)| Extract and link medical named entities |
|[jsl_meds_q4_v1](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_q4_v1_en.html)       | Summarization and Q&A |
|[jsl_meds_q8_v1](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_q8_v1_en.html)       | Summarization and Q&A |
|[jsl_meds_q16_v1](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_q16_v1_en.html)      | Summarization and Q&A |
|[jsl_meds_rag_q4_v1](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_rag_q4_v1_en.html)   | LLM component of Retrieval Augmented Generation (RAG) |
|[jsl_meds_rag_q8_v1](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_rag_q8_v1_en.html)   | LLM component of Retrieval Augmented Generation (RAG) |
|[jsl_meds_rag_q16_v1](https://nlp.johnsnowlabs.com/2024/10/05/jsl_meds_rag_q16_v1_en.html)  | LLM component of Retrieval Augmented Generation (RAG) |


*Example*:

```python
medical_llm = MedicalLLM.pretrained("jsl_meds_q16_v1", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(100)\
    .setUseChatTemplate(True)\
    .setTemperature(0)\
     #.setNGpuLayers(100) # if you have GPU

med_ner_prompt = """
Based on the following text, what age group is most susceptible to breast cancer?

## Text:
The exact cause of breast cancer is unknown. However, several risk factors can increase your likelihood of developing breast cancer, such as:
- A personal or family history of breast cancer
- A genetic mutation, such as BRCA1 or BRCA2
- Exposure to radiation
- Age (most commonly occurring in women over 50)
- Early onset of menstruation or late menopause
- Obesity
- Hormonal factors, such as taking hormone replacement therapy
"""

data = spark.createDataFrame([[med_ner_prompt]]).toDF("text")
```

*Result*:

```bash
The age group most susceptible to breast cancer, as mentioned in the text, is women over the age of 50.
```

Please check the [Loading Medical and Open Souce LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) Notebook for more information


</div><div class="h3-box" markdown="1">
 
#### Explore 6 New Specialized LLMs at Various Sizes and Quantisation Levels for Healthcare Applications (Medical Note Summarization, Q&A, RAG, and Chat)

Discover 9 new LLMs designed to tackle various tasks in the healthcare domain. These models include capabilities for summarization, question answering, retrieval-augmented generation (RAG), chat functionalities, and medical named entity recognition (NER). Each model is optimized with different quantization levels (q16, q8, q4) to balance performance and efficiency, catering to specific needs in medical data processing and analysis. Whether you need detailed summaries, precise Q&A, or accurate entity extraction, these models offer advanced solutions for healthcare professionals and researchers.


{:.table-model-big}
| Model Name              | Description |
|-------------------------|-------------|
| [JSL_MedS_q16_v2](https://nlp.johnsnowlabs.com/2024/09/19/jsl_meds_q16_v2_en.html)    | Summarization, Q&A, RAG |
| [JSL_MedS_q8_v2](https://nlp.johnsnowlabs.com/2024/09/19/jsl_meds_q8_v2_en.html)      | Summarization, Q&A, RAG |
| [JSL_MedS_q4_v2](https://nlp.johnsnowlabs.com/2024/09/19/jsl_meds_q4_v2_en.html)      | Summarization, Q&A, RAG |
| [JSL_MedS_q16_v3](https://nlp.johnsnowlabs.com/2024/09/19/jsl_meds_q16_v3_en.html)    | Summarization, Q&A, RAG |
| [JSL_MedS_q8_v3](https://nlp.johnsnowlabs.com/2024/09/19/jsl_meds_q8_v3_en.html)      | Summarization, Q&A, RAG |
| [JSL_MedS_q4_v3](https://nlp.johnsnowlabs.com/2024/09/19/jsl_meds_q4_v3_en.html)      | Summarization, Q&A, RAG |


**Note**: Our current LLM loader implementation based on `llama.cpp` may lag behind when it comes to inference speed and output quality on certain use cases given your hardware. We have other means of serving these models outside of the Healthcare NLP library and users are advised to get in touch with us if there is such a need. We recommend using 8b quantized versions of the models in a GPU-poor environment as the qualitative performance difference between q16 and q8 versions is very negligible.

*Example*:

```python

from sparknlp_jsl.llm import LLMLoader

llm_loader_pretrained = LLMLoader(spark).pretrained("jsl_meds_q16_v2", "en", "clinical/models")

prompt = """
A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus.
Which of the following is the best treatment for this patient?
A: Ampicillin
B: Ceftriaxone
C: Ciprofloxacin
D: Doxycycline
E: Nitrofurantoin
"""

llm_loader_pretrained.generate(prompt)
```

*Result*:

```bash
The best treatment for this patient is E: Nitrofurantoin. This medication is considered safe during pregnancy and is effective for treating urinary tract infections (UTIs). The other options listed are not recommended during pregnancy due to potential risks to the fetus. Ampicillin (A) and Ceftriaxone (B) are generally safe but may not be the first-line treatment for UTIs. Ciprofloxacin (C) and Doxycycline (D) are contraindicated in pregnancy due to potential adverse effects on fetal development. Nitrofurantoin (E) is a commonly used antibiotic for UTIs during pregnancy and has a good safety profile.
```

Please check the [Loading Medical and Open Souce LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) Notebook for more information



</div><div class="h3-box" markdown="1">

####  Clinical Document Analysis with One-Liner Pretrained Pipelines for Specific Clinical Tasks and Concepts

We introduce a suite of advanced, hybrid pretrained pipelines, specifically designed to streamline the clinical document analysis process. These pipelines are built upon multiple state-of-the-art (SOTA) pretrained models, delivering a comprehensive solution for quickly extracting vital information.

What sets this release apart is the elimination of complexities typically involved in building and chaining models. Users no longer need to navigate the intricacies of constructing intricate pipelines from scratch or the uncertainty of selecting the most effective model combinations. Our new pretrained pipelines simplify these processes, offering a seamless, user-friendly experience.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`explain_clinical_doc_vop_small`](https://nlp.johnsnowlabs.com/2024/09/09/explain_clinical_doc_vop_small_en.html) | This pipeline is designed to extract all clinical/medical entities, assertion status, and relation informations which may be considered as Voice Of Patient (VOP) entities from text. |
| [`explain_clinical_doc_cancer_type`](https://nlp.johnsnowlabs.com/2024/09/16/explain_clinical_doc_cancer_type_en.html) | This pipeline is designed to extract all clinical/medical entities, assertion status, and relation informations which may be considered as extract oncological and cancer type entities from text. |
| [`explain_clinical_doc_sdoh_small`](https://nlp.johnsnowlabs.com/2024/09/27/explain_clinical_doc_sdoh_small_en.html) | This pipeline is designed to extract all social determinants of health (SDOH) entities from text, assign assertion status to the extracted entities, establish relations between the extracted entities. |


*Example*:

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline_sdoh = PretrainedPipeline("explain_clinical_doc_vop_small", "en", "clinical/models")

text = """It seems like my health troubles started a few years ago. I had been feeling really tired all the time and was losing weight without even trying. My doctor did some blood work and said my sugar levels were high - he diagnosed me with something called type 2 diabetes. He put me on two medications - I take a pill called metformin 500 mg twice a day, and another one called glipizide 5 mg before breakfast and dinner. Those are supposed to help lower my blood sugar. I also have to watch what I eat and try to exercise more even though it's hard with my energy levels. A couple years after the diabetes, I started having really bad heartburn all the time. I saw a specialist called a gastroenterologist who did an endoscopy procedure where they stick a camera down your throat. That test showed I have chronic acid reflux disease or GERD. Now I take a daily pill called omeprazole 20 mg to control the heartburn symptoms.Most recently, I've had a lot of joint pain in my shoulders and knees. My primary doctor ran some blood tests that showed something called rheumatoid arthritis. He referred me to a rheumatologist who started me on a weekly medication called methotrexate. I have to remember to take folic acid with that to help minimize side effects. It seems to be helping the joint pain so far."""

```

*NER and Assertion Result*:

{:.table-model-big}
|    | chunks                      |   begin |   end |   sentence | entities   | assertion              |   confidence |
|---:|:----------------------------|--------:|------:|-----------:|:-----------|:-----------------------|-------------:|
|  0 | tired                       |      85 |    89 |          1 | Symptom    | Present_Or_Past        |     0.9959   |
|  1 | losing weight               |     112 |   124 |          1 | Symptom    | Present_Or_Past        |     0.81445  |
|  2 | doctor                      |     150 |   155 |          2 | Employment | SomeoneElse            |     0.9895   |
|  3 | blood work                  |     166 |   175 |          2 | Test       | Present_Or_Past        |     0.8835   |
|  4 | sugar levels                |     189 |   200 |          2 | Test       | Present_Or_Past        |     0.8277   |
|  5 | high                        |     207 |   210 |          2 | TestResult | SomeoneElse            |     0.9095   |
|  6 | type 2 diabetes             |     252 |   266 |          2 | Disease    | Hypothetical_Or_Absent |     0.379367 |
|  7 | metformin                   |     321 |   329 |          3 | Drug       | Hypothetical_Or_Absent |     0.997    |
|  8 | glipizide                   |     374 |   382 |          3 | Drug       | Hypothetical_Or_Absent |     0.9953   |
|  9 | blood sugar                 |     454 |   464 |          4 | Test       | Present_Or_Past        |     0.6415   |
| 10 | diabetes                    |     594 |   601 |          6 | Disease    | Present_Or_Past        |     0.9901   |
| 11 | heartburn                   |     632 |   640 |          6 | Symptom    | Present_Or_Past        |     0.988    |
| 12 | specialist                  |     664 |   673 |          7 | Employment | SomeoneElse            |     0.9878   |
| 13 | gastroenterologist          |     684 |   701 |          7 | Employment | SomeoneElse            |     0.9866   |
| 14 | endoscopy procedure         |     714 |   732 |          7 | Procedure  | Hypothetical_Or_Absent |     0.75475  |
| 15 | chronic acid reflux disease |     802 |   828 |          8 | Disease    | Present_Or_Past        |     0.7071   |
| 16 | GERD                        |     833 |   836 |          8 | Disease    | Hypothetical_Or_Absent |     0.9476   |
| 17 | omeprazole                  |     870 |   879 |          9 | Drug       | Present_Or_Past        |     0.9987   |
| 18 | heartburn                   |     902 |   910 |          9 | Symptom    | Present_Or_Past        |     0.9849   |
| 19 | pain                        |     961 |   964 |         10 | Symptom    | Present_Or_Past        |     0.9923   |
| 20 | primary doctor              |     996 |  1009 |         11 | Employment | SomeoneElse            |     0.75345  |
| 21 | blood tests                 |    1020 |  1030 |         11 | Test       | Present_Or_Past        |     0.93715  |
| 22 | rheumatoid arthritis        |    1061 |  1080 |         11 | Disease    | Hypothetical_Or_Absent |     0.74685  |
| 23 | rheumatologist              |    1103 |  1116 |         12 | Employment | Present_Or_Past        |     0.9913   |
| 24 | methotrexate                |    1163 |  1174 |         12 | Drug       | Present_Or_Past        |     0.9995   |
| 25 | folic acid                  |    1204 |  1213 |         13 | Drug       | Present_Or_Past        |     0.7913   |
| 26 | pain                        |    1289 |  1292 |         14 | Symptom    | Present_Or_Past        |     0.9837   |


*Relation Extraction Result*:

{:.table-model-big}
|sentence |entity1_begin |entity1_end | chunk1              | entity1   |entity2_begin |entity2_end | chunk2       | entity2    | relation           |confidence |
|--------:|-------------:|-----------:|:--------------------|:----------|-------------:|-----------:|:-------------|:-----------|:-------------------|----------:|
|       2 |          166 |        175 | blood work          | Test      |          207 |        210 | high         | TestResult | Test-TestResult    |         1 |
|       3 |          309 |        312 | pill                | Form      |          321 |        329 | metformin    | Drug       | Form-Drug          |         1 |
|       3 |          321 |        329 | metformin           | Drug      |          331 |        336 | 500 mg       | Dosage     | Drug-Dosage        |         1 |
|       3 |          321 |        329 | metformin           | Drug      |          338 |        348 | twice a day  | Frequency  | Drug-Frequency     |         1 |
|       3 |          374 |        382 | glipizide           | Drug      |          384 |        387 | 5 mg         | Dosage     | Drug-Dosage        |         1 |
|       6 |          571 |        588 | couple years after  | DateTime  |          594 |        601 | diabetes     | Disease    | DateTime-Disease   |         1 |
|       6 |          594 |        601 | diabetes            | Disease   |          632 |        640 | heartburn    | Symptom    | Disease-Symptom    |         1 |
|       7 |          714 |        732 | endoscopy procedure | Procedure |          770 |        775 | throat       | BodyPart   | Procedure-BodyPart |         1 |
|       9 |          852 |        856 | daily               | Frequency |          870 |        879 | omeprazole   | Drug       | Frequency-Drug     |         1 |
|       9 |          858 |        861 | pill                | Form      |          870 |        879 | omeprazole   | Drug       | Form-Drug          |         1 |
|       9 |          870 |        879 | omeprazole          | Drug      |          881 |        885 | 20 mg        | Dosage     | Drug-Dosage        |         1 |
|      10 |          927 |        934 | recently            | DateTime  |          961 |        964 | pain         | Symptom    | DateTime-Symptom   |         1 |
|      10 |          955 |        959 | joint               | BodyPart  |          961 |        964 | pain         | Symptom    | BodyPart-Symptom   |         1 |
|      10 |          961 |        964 | pain                | Symptom   |          972 |        980 | shoulders    | BodyPart   | Symptom-BodyPart   |         1 |
|      10 |          961 |        964 | pain                | Symptom   |          986 |        990 | knees        | BodyPart   | Symptom-BodyPart   |         1 |
|      12 |         1138 |       1143 | weekly              | Frequency |         1163 |       1174 | methotrexate | Drug       | Frequency-Drug     |         1 |
|      14 |         1283 |       1287 | joint               | BodyPart  |         1289 |       1292 | pain         | Symptom    | BodyPart-Symptom   |         1 |


Please check the [Task Based Clinical Pretrained Pipelines](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.3.Task_Based_Clinical_Pretrained_Pipelines.ipynb) model for more information




</div><div class="h3-box" markdown="1">

#### Introducing 8 New Named Entity Recognition (NER) Models and Pipelines to Detect PHI for Deidentification with Minimal Customisation Required

Introducing 8 New Named Entity Recognition (NER) Models: `ner_deid_generic_docwise`, `ner_deid_subentity_docwise`, `ner_deid_subentity_augmented_docwise`, `ner_deid_aipii`, `ner_deid_subentity_augmented_v2`, `clinical_deidentification_docwise_wip`, `clinical_deidentification_nameAugmented_v2` and `clinical_deidentification_v2_wip`. These models work at the document level and are particularly useful for detecting Protected Health Information (PHI) for de-identification.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`ner_deid_generic_docwise`](https://nlp.johnsnowlabs.com/2024/09/06/ner_deid_generic_docwise_en.html) | This document-level model detects PHI entities for de-identification. (Generic) |
| [`ner_deid_subentity_augmented_docwise`](https://nlp.johnsnowlabs.com/2024/09/06/ner_deid_subentity_augmented_docwise_en.html) | This document-level model detects PHI entities for de-identification. (Subentity_Augmented) |
| [`ner_deid_subentity_docwise`](https://nlp.johnsnowlabs.com/2024/09/06/ner_deid_subentity_docwise_en.html) | This document-level model detects PHI entities for de-identification. (Subentity) |
| [`ner_deid_aipii`](https://nlp.johnsnowlabs.com/2024/09/25/ner_deid_aipii_en.html) | This model is particularly effective in identifying and labeling various entities, making it useful for detecting protected health information (PHI) that may need to be masked or de-identified. |
| [`ner_deid_subentity_augmented_v2`](https://nlp.johnsnowlabs.com/2024/09/20/ner_deid_subentity_augmented_v2_en.html) | This document-level model detects PHI entities for de-identification. (Subentity) |
| [`clinical_deidentification_docwise_wip`](https://nlp.johnsnowlabs.com/2024/10/03/clinical_deidentification_docwise_wip_en.html) | This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. |
| [`clinical_deidentification_nameAugmented_v2`](https://nlp.johnsnowlabs.com/2024/10/03/clinical_deidentification_nameAugmented_v2_en.html) | This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. |
| [`clinical_deidentification_v2_wip`](https://nlp.johnsnowlabs.com/2024/10/03/clinical_deidentification_v2_wip_en.html) | This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. |

*Example*:

```python
ner_deid_generic = MedicalNerModel.pretrained("ner_deid_generic_docwise", "en", "clinical/models")  \
      .setInputCols(["document", "token", "embeddings"]) \
      .setOutputCol("ner_deid_generic_docwise")

text= '''Dr. John Taylor, ID 982345, a cardiologist at St. Mary's Hospital in Boston, was contacted on 05/10/2023 regarding a 45-year-old male patient.'''
```


*Result*:

{:.table-model-big}
|chunk              |begin|end|ner_label |
|-------------------|-----|---|----------|
|John Taylor        |5    |15 |NAME      |
|982345             |21   |26 |CONTACT   |
|cardiologist       |31   |42 |PROFESSION|
|St. Mary's Hospital|47   |65 |LOCATION  |
|Boston             |70   |75 |LOCATION  |
|05/10/2023         |95   |104|DATE      |
|45-year-old        |118  |128|AGE       |


Please check the [Clinical Deidentification Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.0.Clinical_DeIdentification.ipynb) for more information


</div><div class="h3-box" markdown="1">

#### Introducing a New Mapper Model Designed to Link `ICD-10-CM codes` with Their Corresponding Chronicity Indicators

Introducing a suite of new ChunkMapper models designed to streamline medical code mapping tasks.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
|[`icd10cm_chronic_indicator_mapper`](https://nlp.johnsnowlabs.com/2024/10/02/icd10cm_chronic_indicator_mapper_en.html)  | This mapper model links ICD-10-CM codes to their corresponding chronicity indicators. The `chronic indicator` can have three different values; `0`: "not chronic", `1`: "chronic", `9`: "no determination" |

*Example*:

```python
mapperModel = ChunkMapperModel.pretrained("icd10cm_chronic_indicator_mapper","en", "clinical/models")\
    .setInputCols(["chunk"])\
    .setOutputCol("chronic_indicator_mapping")\
    .setRels(["chronic_indicator"])


data = spark.createDataFrame([["""A 42-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with besity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""]]).toDF("text")
```

*Result*:

{:.table-model-big}
|sentence_id|                               entity|begin|end|  label|icd10cm|                                                                                resolution|chronic_indicator|
|-----------|-------------------------------------|-----|---|-------|-------|------------------------------------------------------------------------------------------|-----------------|
|          0|        gestational diabetes mellitus|   39| 67|PROBLEM|  O24.4|                             gestational diabetes mellitus [gestational diabetes mellitus]|                0|
|          0|subsequent type two diabetes mellitus|  117|153|PROBLEM| O24.11|pre-existing type 2 diabetes mellitus [pre-existing type 2 diabetes mellitus, in pregna...|                1|
|          0|                              obesity|  172|178|PROBLEM|  E66.9|                                                            obesity [obesity, unspecified]|                1|
|          0|                    a body mass index|  185|201|PROBLEM| Z68.41|                       finding of body mass index [body mass index [bmi] 40.0-44.9, adult]|                9|
|          0|                             polyuria|  261|268|PROBLEM|    R35|                                                                       polyuria [polyuria]|                0|
|          0|                           polydipsia|  271|280|PROBLEM|  R63.1|                                                                   polydipsia [polydipsia]|                0|
|          0|                        poor appetite|  283|295|PROBLEM|  R63.0|                                                                  poor appetite [anorexia]|                0|
|          0|                             vomiting|  302|309|PROBLEM|  R11.1|                                                                       vomiting [vomiting]|                0|
|          1|        a respiratory tract infection|  403|431|PROBLEM|  J98.8|                       respiratory tract infection [other specified respiratory disorders]|                0|


</div><div class="h3-box" markdown="1">

#### Introducing a New Named Entity Recognition (NER) Model and a New Binary Classification Model to Detect Adverse Drug Events

- Named Entity Recognition (NER) Model: [ner_ade_clinical_v2](https://nlp.johnsnowlabs.com/2024/09/05/ner_ade_clinical_v2_en.html) to detect adverse reactions of drugs, and problem in reviews, tweets, and medical text using pretrained NER model.
- Binary Classification Model: [bert_sequence_classifier_ade_augmented_v2](https://nlp.johnsnowlabs.com/2024/09/05/bert_sequence_classifier_ade_augmented_v2_en.html) Classify texts/sentences in two categories: `True`: The sentence is talking about a possible ADE. `False`: The sentence doesn’t have any information about an ADE. 

*Example*:

```python
ner_model = MedicalNerModel.pretrained("ner_ade_clinical_v2", "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

data = spark.createDataFrame([["""I have an allergic reaction to vancomycin so I have itchy skin, sore throat/burning/itching, numbness of tongue and gums.
I would not recommend this drug to anyone, especially since I have never had such an adverse reaction to any other medication."""]]).toDF("sentence")
```

*Result*:

{:.table-model-big}
|chunk                      |begin|end|ner_label|
|---------------------------|-----|---|---------|
|allergic reaction          |10   |26 |ADE      |
|vancomycin                 |31   |40 |DRUG     |
|itchy skin                 |52   |61 |ADE      |
|sore throat/burning/itching|64   |90 |ADE      |
|numbness of tongue and gums|93   |119|ADE      |
|an adverse reaction        |204  |222|PROBLEM  |


</div><div class="h3-box" markdown="1">

#### Introducing the `REChunkMerger` Annotator to Merge the Entities in a Relationship as a Single Entity

The `REChunkMerger` annotator merge related chunks of data into a new, single chunk. It specifically merges entities that are identified as being in a relationship by using a separator, which by default is a whitespace (" "). This means when two related entities are found within a text, this annotator combines them into one chunk using the specified separator to see the relationship clear.

Key Parameters:

- `separator`: Separator to add between the relation chunks. (default is a whitespace: " ").

*Example*:

```python
re_chunk_merger = REChunkMerger() \
     .setInputCols(["re_chunk"]) \
     .setOutputCol("relation_chunks") \
     .setSeparator("  ")\

data = spark.createDataFrame([["""The patient was prescribed 1 unit of Advil for 5 days after meals. The patient was also
given 1 unit of Metformin daily.
He was seen by the endocrinology service and she was discharged on 40 units of insulin glargine at night ,
12 units of insulin lispro with meals , and metformin 1000 mg two times a day."""]]).toDF("sentence")
```

*Relation Result*:

{:.table-model-big}
| sentence | chunk1           | entity1 | chunk2           | entity2   | relation       | confidence |
|----------|------------------|---------|------------------|-----------|----------------|------------|
| 0        | 1 unit           | DOSAGE  | Advil            | DRUG      | DOSAGE-DRUG    | 1\.0       |
| 0        | Advil            | DRUG    | for 5 days       | DURATION  | DRUG-DURATION  | 1\.0       |
| 1        | 1 unit           | DOSAGE  | Metformin        | DRUG      | DOSAGE-DRUG    | 1\.0       |
| 1        | Metformin        | DRUG    | daily            | FREQUENCY | DRUG-FREQUENCY | 1\.0       |
| 2        | 40 units         | DOSAGE  | insulin glargine | DRUG      | DOSAGE-DRUG    | 1\.0       |
| 2        | insulin glargine | DRUG    | at night         | FREQUENCY | DRUG-FREQUENCY | 1\.0       |
| 2        | 12 units         | DOSAGE  | insulin lispro   | DRUG      | DOSAGE-DRUG    | 1\.0       |
| 2        | insulin lispro   | DRUG    | with meals       | FREQUENCY | DRUG-FREQUENCY | 1\.0       |
| 2        | metformin        | DRUG    | 1000 mg          | STRENGTH  | DRUG-STRENGTH  | 1\.0       |
| 2        | metformin        | DRUG    | two times a day  | FREQUENCY | DRUG-FREQUENCY | 1\.0       |


*REChunkMerger Result*:

{:.table-model-big}
|result                    |
|--------------------------|
|1 unit  Advil             |
|Advil  for 5 days         |
|1 unit  Metformin         |
|Metformin  daily          |
|40 units  insulin glargine|
|insulin glargine  at night|
|12 units  insulin lispro  |
|insulin lispro  with meals|
|metformin  1000 mg        |
|metformin  two times a day|


Please check the [REChunkMerger Mooc Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/REChunkMerger.ipynb) Notebook for more information


</div><div class="h3-box" markdown="1">

#### Introducing a Brand New `ContextualEntityFilter` Annotator to Filter Entities with Context-Specific Rules.

The `ContextualEntityFilterer` filters segments of text—identified by metadata as "CHUNK" annotations that contain specific types of entities. These entities are defined by identifiers or field types detailed in the metadata. 

Key Parameters:

- `ruleScope`: The ruleScope parameter to apply the filter. Options: sentence, document.
- `caseSensitive`: Whether to use case sensitive when matching words
- `rules`: The rules parameter to filter chunks based on contextual rules and it is a list of dictionaries. A dictionary should contain the following keys: \
           - `entity`: The entity field to filter. \
           - `scopeWindow`: The scope window around the entity, defined as a list of two integers [before, after], specifying how many chunks before and after should be considered.\
           - `whiteListEntities`: The white list of entities. If an entity from this list appears within the scope window, the chunk will be kept.\
           - `blackListEntities`: The black list of entities. If an entity from this list appears within the scope window, the chunk will be filtered out.\
           - `blackListWords`: The black list of words. If a word from this list appears within the scope window, the chunk will be filtered out.\
           - `whiteListWords`: The white list of words. If a word from this list appears within the scope window, the chunk will be kept.\
           - `confidenceThreshold`: The confidence threshold to filter the chunks. Filtering is only applied if the confidence of the chunk is below the threshold.\
           - `scopeWindowLevel`: The level to apply the scope window. Options: token, chunk.

*Example*:

```python
rules =[
    {
        "entity": "LOCATION",
        "scopeWindow": [2, 2],
        "whiteList": ["AGE", "DATE"],
        "blackList": ["ID", "NAME"],
        "scopeWindowLevel": "token"
    },
    {
        "entity": "DATE",
        "scopeWindow": [2, 2],
        "whiteList": ["AGE", "DATE"],
        "blackList": ["ID", "NAME"],
        "scopeWindowLevel": "chunk"
    }
]

contextual_entity_filterer = ContextualEntityFilterer() \
    .setInputCols("sentence", "token", "ner_chunks") \
    .setOutputCol("filtered_ner_chunks") \
    .setRules(rules)\
    .setRuleScope("sentence")


text = "California, known for its beautiful beaches,and he is 36 years. " \
        "The Grand Canyon in Arizona, where the age is 37, is a stunning natural landmark. " \
        "It was founded on September 9, 1850, and Arizona on February 14, 1912."
df = spark.createDataFrame([[text]]).toDF("text")
```


*Input DataFrame*:

{:.table-model-big}
|            chunk|begin|end|ner_label|
|-----------------|-----|---|---------|
|       California|    0|  9| LOCATION|
|               36|   54| 55|      AGE|
|     Grand Canyon|   68| 79| LOCATION|
|          Arizona|   84| 90| LOCATION|
|               37|  110|111|      AGE|
|September 9, 1850|  164|180|     DATE|
|February 14, 1912|  198|214|     DATE|



*Result after filtering*:

{:.table-model-big}
|            chunk|begin|end|ner_label|confidence|
|-----------------|-----|---|---------|----------|
|               36|   54| 55|      AGE|      0.96|
|               37|  110|111|      AGE|    0.9921|
|September 9, 1850|  164|180|     DATE|  0.964375|
|February 14, 1912|  198|214|     DATE|  0.952525|


Please check the [ContextualEntityFilter Mooc Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ContextualEntityFilter.ipynb) Notebook for more information


</div><div class="h3-box" markdown="1">


####  Enhanced New Sentence Detector Model for Healthcare Text Segmentation in Corrupted Text

The new Sentence Detector DL Model  `v2` significantly improves sentence segmentation accuracy compared to its predecessor. Optimized for clinical and healthcare domains, it ensures more precise detection of sentence boundaries, particularly in complex medical texts. The model delivers superior performance across various document formats and medical terminology. The new model offers enhanced support for edge cases, improved handling of abbreviations and punctuation, and better adaptability to diverse linguistic structures, ensuring more reliable results in medical NLP pipelines.

*Example*:

```python
sentence_detector_v1 = SentenceDetectorDLModel\
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence_v1")

sentence_detector_v2 = SentenceDetectorDLModel\
    .pretrained("sentence_detector_dl_healthcare_v2_wip", "en", "clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence_v2")

pipeline = Pipeline(
    stages=[
        document_assembler, 
        sentence_detector_v1,
        sentence_detector_v2])

```

*Sentence Detector v1 Result*:

|sent_id|sentence  |
|-------|----------|
|0      |He was given boluses of MS04 with some effect, he has since been placed on a PCA - \nhe take 80mg of oxycontin at home, his PCA dose is ~ 2 the morphine dose of the oxycontin, \nhe has also received ativan for anxiety.  |
|1      |Repleted with 20 meq kcl po, 30 mmol K-phos iv and 2 gms \nmag so4 iv. |
|2      |Size: Prostate gland measures 10x1.  |
|3      |1x4.9 cm (LS x AP x TS).      |
|4      |Estimated volume is 51.9 ml \nand is mildly enlarged in size.  |
|5      |Normal delineation pattern of the prostate gland is preserved.  |
|6      |ORs with 95% CI for family - based analyses were calculated in PLINK (http: / / pngu . mgh . \nharvard .    |
|7      |edu / purcell / plink /) [59].    |
|8      |Classification and regression based quantitative \nstructure - toxicity relationship (QSTR) as well as toxicophore models were developed for \nthe first time on basal cytotoxicity data (in vitro 3T3 neutral red uptake data) of a diverse \nseries of chemicals (including drugs and environmental pollutants) collected from the ACuteTox \ndatabase (http: / / www . acutetox . eu /).|
|9      |Here, we created a database, the Worm Developmental \nDynamics Database (http: / / so . qbic . riken . jp / wddd /), which stores a collection of \nquantitative information about cell division dynamics in early Caenorhabditis elegans embryos \nwith single genes silenced by RNA - mediated interference.                 |
|10     |Worldwide prevalence figures estimate \nthat there are 280 million diabetic patients in 2011 and more than 500 million in 2030 (http: / \n/ www . diabetesatlas .  |
|11     |org /).                                               |
|12     |ESTs with homologues / orthologues in C . elegans and other \nnematodes were also subjected to analysis employing the KEGG Orthology - Based Annotation System (KOBAS)      |
|13     |(www . kobas .                    |
|14     |cbi . pku . edu . cn), which predicts the biochemical pathways in which \nmolecules are involved.     |
|15     |We also included the TNF - 308G / A promoter SNP, together with nine \nfurther SNPs in the region of HLA - B and MICA obtained from the database, dbSNP (http: / / \nwww . ncbi . nlm . nih . gov / projects / SNP /).              |
|16     |Sequences were analyzed using DNASTAR 4 . 0    |
|17     |(http: / / www . dnastar .  |
|18     |com), GeneDoc, and GCC (University of Wisconsin). |
|19     |Peptides inferred \nfrom ESTs were classified functionally using Interproscan (available at http: / / www . ebi . \nac . uk / InterProScan /) employing the default search parameters. |


*Sentence Detector v2 Result*:

|sent_id|sentence    |
|-------|------------|
|0      |He was given boluses of MS04 with some effect, he has since been placed on a PCA - \nhe take 80mg of oxycontin at home, his PCA dose is ~ 2 the morphine dose of the oxycontin, \nhe has also received ativan for anxiety. |
|1      |Repleted with 20 meq kcl po, 30 mmol K-phos iv and 2 gms \nmag so4 iv. |
|2      |Size: Prostate gland measures 10x1.1x4.9 cm (LS x AP x TS). |
|3      |Estimated volume is 51.9 ml \nand is mildly enlarged in size.     |
|4      |Normal delineation pattern of the prostate gland is preserved.  |
|5      |ORs with 95% CI for family - based analyses were calculated in PLINK (http: / / pngu . mgh . \nharvard . edu / purcell / plink /) [59].                                |
|6      |Classification and regression based quantitative \nstructure - toxicity relationship (QSTR) as well as toxicophore models were developed for \nthe first time on basal cytotoxicity data (in vitro 3T3 neutral red uptake data) of a diverse \nseries of chemicals (including drugs and environmental pollutants) collected from the ACuteTox \ndatabase (http: / / www . acutetox . eu /).|
|7      |Here, we created a database, the Worm Developmental \nDynamics Database (http: / / so . qbic . riken . jp / wddd /), which stores a collection of \nquantitative information about cell division dynamics in early Caenorhabditis elegans embryos \nwith single genes silenced by RNA - mediated interference.                                                                             |
|8      |Worldwide prevalence figures estimate \nthat there are 280 million diabetic patients in 2011 and more than 500 million in 2030 (http: / \n/ www . diabetesatlas . org /).     |
|9      |ESTs with homologues / orthologues in C . elegans and other \nnematodes were also subjected to analysis employing the KEGG Orthology - Based Annotation System (KOBAS)       |
|10     |(www . kobas . cbi . pku . edu . cn), which predicts the biochemical pathways in which \nmolecules are involved.                                                       |
|11     |We also included the TNF - 308G / A promoter SNP, together with nine \nfurther SNPs in the region of HLA - B and MICA obtained from the database, dbSNP (http: / / \nwww . ncbi . nlm . nih . gov / projects / SNP /).                                |
|12     |Sequences were analyzed using DNASTAR 4 . 0 \n(http: / / www . dnastar . com), GeneDoc, and GCC (University of Wisconsin).   |
|13     |Peptides inferred \nfrom ESTs were classified functionally using Interproscan (available at http: / / www . ebi . \nac . uk / InterProScan /) employing the default search parameters.  |

</div><div class="h3-box" markdown="1">

#### Introducing New Parameters to `Replacer` for Data Augmentation

Added new parameters into `Replacer` to replace identified tokens or patterns with predefined alternatives. Moreover, Added new option to `noneValuesTo`: prioritize_static_entity. If a static entity mapping is available for the entity type, it will use this values for mapping. If not, it will act according to StaticEntityMappingsFallback option.

- `returnEntityMappings`: With this property you select if you want to return mapping column
- `mappingsColumn`: This column maps the annotations to their corresponding chunks before the entities are replaced.
- `staticEntityMappings`: A map of entity types to their replacement values
- `staticEntityMappingsFallback`: Fallback option for static entity mappings. Allowed values: 'entity', 'place_holder', 'skip', 'error', Default; error

*Example*:

```python
replacer = Replacer() \
      .setInputCols("chunk", "sentence")\
      .setOutputCol("doc")\
      .setUseReplacement(True)\
      .setNoneValuesTo("prioritize_static_entity") \
      .setPlaceHolder("******") \
      .setPlaceHolderDelimiters(["<", ">"]) \
      .setReturnEntityMappings(True) \
      .setMappingsColumn("mappings") \
      .setStaticEntityMappings({"TREATMENT": "MEDICATION", "TEST": "ACTIVITY"}) \
      .setStaticEntityMappingsFallback("entity")

sample_text = "A 32-year-old woman with a history of type 2 diabetes, previously managed for gestational diabetes. Her treatment regimen included metformin. At her check-up, she was found to be dehydrated, though without abdominal discomfort. Important lab results showed a glucose level of 130 mg/dL, triglycerides at 450 mg/dL, and venous pH of 7.30."

data = spark.createDataFrame([[sample_text]]).toDF("text")
```

*Result*:

```bash
A 32-year-old woman with a history of <PROBLEM>, previously managed for <PROBLEM>., MEDICATION included MEDICATION., At ACTIVITY, she was found to be <PROBLEM>, though without <PROBLEM>., Important lab results showed ACTIVITY of 130 mg/dL, ACTIVITY at 450 mg/dL, and ACTIVITY of 7.30.
```

Please check the [Replacer Mooc Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/Replacer.ipynb) Notebook for more information



</div><div class="h3-box" markdown="1">

#### New Speed Benchmarks for Multi-NER Pipelines

- 64 Cores:

Driver: Standard_D4s_v3, 4 core, 16 GB memory, \
Worker: Standard_D4s_v2, 8 core, 28 GB memory, \
total worker number: 8 \
input_data_rows:1000

{:.table-model-big}
| action          | partition |  NER<br>timing  | 2_NER<br>timing | 4_NER<br>timing | NER+RE<br>timing |
|-----------------| ---------:|----------------:|----------------:|----------------:|-----------------:|
| write_parquet   |     4     | 1 min 36 sec    | 3 min 1 sec     | 6 min 32 sec    |  3 min 12 sec    |
| write_deltalake |     4     | 1 min 38 sec    | 3 min 2 sec     | 6 min 30 sec    |  3 min 18 sec    |
| write_parquet   |     8     | 48 sec          | 1 min 32 sec    | 3 min 21 sec    |  1 min 38 sec    |
| write_deltalake |     8     | 51 sec          | 1 min 36 sec    | 3 min 26 sec    |  1 min 43 sec    |
| write_parquet   |     16    | 28 sec          | 1 min 16 sec    |  2 min 2 sec    |  56 sec          |
| write_deltalake |     16    | 31 sec          | 57 sec          |  2 min 2 sec    |  58 sec          |
| write_parquet   |     32    | 20 sec          | 39 sec          | 1 min 22 sec    |  50 sec          |
| write_deltalake |     32    | 22 sec          | 41 sec          | 1 min 45 sec    |  35 sec          |
| write_parquet   |     64    | 17 sec          | 31 sec          |  1 min 8 sec    |  27 sec          |
| write_deltalake |     64    | 17 sec          | 32 sec          | 1 min 11 sec    |  29 sec          |
| write_parquet   |    100    | 18 sec          | 33 sec          | 1 min 13 sec    |  30 sec          |
| write_deltalake |    100    | 20 sec          | 33 sec          | 1 min 32 sec    |  32 sec          |
| write_parquet   |    1000   | 22 sec          | 36 sec          | 1 min 12 sec    |  31 sec          |
| write_deltalake |    1000   | 23 sec          | 34 sec          | 1 min 33 sec    |  52 sec          |



Please check [NER (BiLSTM-CNN-Char Architecture) Benchmark Experiment](https://nlp.johnsnowlabs.com/docs/en/benchmark#ner-bilstm-cnn-char-architecture-benchmark-experiment) for more detail




</div><div class="h3-box" markdown="1">

#### New Blog Posts on Various Topics (AI for Equity, Detecting Stigmatizing Language from Medical Texts, Subcohort Analysis for Oncology Patients, Using Small LLMs to Extract Structured Named Entities, ...)

Explore the latest developments in healthcare NLP through our new blog posts, where we take a deep dive into the innovative technologies and methodologies transforming the medical field. These posts offer insights into how the latest tools are being used to analyze large amounts of unstructured data, identify critical medical assets, and extract meaningful patterns and correlations. Learn how these advances are not only improving our understanding of complex health issues but also contributing to more effective prevention, diagnosis, and treatment strategies.

- [AI for Equity: Extracting Stigmatizing Language from Medical Texts for Better Patient Care](https://medium.com/john-snow-labs/ai-for-equity-extracting-stigmatizing-language-from-medical-texts-for-better-patient-care-1fbf2a9abeb4) The primary aim of medicine is to help patients manage and improve their health, but the language used in medical settings can sometimes have unintended negative effects. Stigmatizing language in medical records can reduce patients to their conditions or pass judgment on their illnesses, leading to poorer care and worsening health disparities. This article discusses how such language can be recognized and addressed using a model developed by John Snow Labs.
  
- [Refining Entity Detection in Healthcare NLP: Precision Through Entity Filtering](https://medium.com/john-snow-labs/refining-entity-detection-in-healthcare-nlp-precision-through-entity-filtering-84a43afd8733) The blog post discusses the ChunkFilterer annotator in Healthcare NLP, emphasizing its role in refining Named Entity Recognition (NER) for precise healthcare applications. It highlights the annotator's capabilities to filter entities using whitelists, blacklists, regular expressions, and confidence scores, enabling users to focus on relevant information from unstructured clinical texts. By integrating ChunkFilterer into NLP pipelines, healthcare professionals can enhance data accuracy and efficiency, leading to improved patient diagnoses, treatment recommendations, and information retrieval from medical databases.

- [Accurate Extracting of Cancer Biomarkers from Free-Text Clinical Notes](https://medium.com/john-snow-labs/accurate-extracting-of-cancer-biomarkers-from-free-text-clinical-notes-6fcd2e8a5e9a) This blog post examines the role of biomarkers in enhancing cancer diagnosis through their extraction from unstructured clinical notes using advanced NLP techniques. It highlights the challenges posed by the inconsistent and complex nature of clinical documentation and how the Healthcare NLP library, developed by John Snow Labs, addresses these through specialized models for entity extraction, relation extraction, and sequence classification. By accurately identifying and analyzing biomarkers from clinical texts, the library supports personalized cancer treatment, improves diagnosis and prognosis, and accelerates cancer research, ultimately enhancing patient outcomes and advancing our understanding of cancer biology.

- [From Diagnosis to Prognosis: Understanding 6 Common Cancers in Medical Records](https://medium.com/john-snow-labs/from-diagnosis-to-prognosis-understanding-6-common-cancers-in-medical-records-df65ad5b3f87) This blog post details the application of John Snow Labs’ Healthcare NLP and LLM library in revolutionizing cancer care through enhanced analysis of medical records. Concentrating on six prevalent cancer types, it showcases how sophisticated natural language processing aids in refining diagnosis, prognosis, and personalized treatment plans by extracting and interpreting vital data from unstructured clinical texts. This technology is pivotal in tackling the rising global cancer rates and improving the overall efficiency and effectiveness of cancer treatments.

- [Harnessing Healthcare-Specific LLMs for Clinical Entity Extraction](https://medium.com/@cabircelik/harnessing-healthcare-specific-llms-for-clinical-entity-extraction-7e0bf63c9b0f) This blog post focuses on how JSL-MedS-NER models are optimized to extract clinical entities from unstructured medical text. These models identify critical information like drug names, diagnoses, side effects, and protected health information (PHI) using quantization options (q4, q8, q16) that balance speed and accuracy. It highlights the models' application in pharmacovigilance, oncology reporting, and clinical data processing. By enabling the identification of drugs, adverse events, and medical conditions, the models support clinical decision-making and data privacy compliance across healthcare systems.


</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, and Reliability of Spark NLP for Healthcare

- Added the `RegexMatcherInternalModel` trait to Scala to match the pretrained method available in Python.
- Added a new parameter for the `Flattener` annotator to sets an array of column names that should be kept in the dataframe after the flattening process.
- Added `resetSentenceIndices` parameter to `ChunkMerger`, `NerConverterInternal`, and `ChunkConverter` annotators for reset sentence indices to treat the entire output as if it originates from a single document.
- Fixed Generative AI Lab API task deletion endpoint: Resolved an issue with the `tasks_delete` endpoint, enabling proper deletion of tasks via the API.
- Added `chunk_validation_options` dictionary into the `dict_to_annotation_converter` module for converting dictionary data to Spark NLP annotations.
- Added pretrained feature added to `InternalDocumentSplitter`.
- Deprecated the `nlp_test` module in `spark-nlp-jsl`; future development will now be managed by `LangTest`. Streamlined the `spark-nlp-jsl` package for improved efficiency.
- Added support for `ONNX` models in the `ChunkKeyPhraseExtraction` annotator, allowing for compatibility with ONNX-based models.

</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [REChunkMerger](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/REChunkMerger.ipynb) MOOC Notebook for merging the entities in a relationship.
- New [ContextualEntityFilterer](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ContextualEntityFilterer.ipynb) MOOC Notebook to filter chunks.
- Updated [Replacer](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/Replacer.ipynb) MOOC Notebook with new `returnEntityMappings`, `mappingsColumn`, `staticEntityMappings`, and `staticEntityMappingsFallback` parameters.
- Updated [NerConverterInternal](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/NerConverterInternal.ipynb) MOOC Notebook with `resetSentenceIndices` parameter.
- Updated [ChunkConverter](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ChunkConverter.ipynb) MOOC Notebook with `resetSentenceIndices` parameter.
- Updated [ChunkMergeModel](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ChunkMergeModel.ipynb) MOOC Notebook with `resetSentenceIndices` parameter.
- Updated [Rule Based Entity Matchers](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.Rule_Based_Entity_Matchers.ipynb) notebook with `country_matcher` and `state_matcher` model.
- Updated [Clinical DeIdentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.Clinical_DeIdentification.ipynb) notebook with new models into model list.
- Updated [Prepare CoNLL from Annotations for NER](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.3.prepare_CoNLL_from_annotations_for_NER.ipynb) notebook with alternative method for creating conll file.
- Updated [Contextual Parser Rule Based NER](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.2.Contextual_Parser_Rule_Based_NER.ipynb) notebook with `zip_parser` model
- Updated [Loading Medical and Open Souce LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) notebook with new LLMs models
- Updated [ONCOLOGY Demo](https://demo.johnsnowlabs.com/healthcare/ONCOLOGY/) with classification models.

</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `biolordresolve_icd10cm_augmented_billable_hcc`            
+ `sbiobertresolve_hcc_augmented`             
+ `sbiobertresolve_meddra_lowest_level_term`            
+ `sbiobertresolve_meddra_preferred_term`   
+ `meddra_llt_pt_mapper`      
+ `meddra_pt_llt_mapper`  
+ `sbertresolve_icd10cm_augmented` 
+ `icd10_meddra_llt_mapper` 
+ `icd10_meddra_pt_mapper`      
+ `meddra_llt_icd10_mapper`  
+ `meddra_pt_icd10_mapper` 
+ `sbertresolve_hcc_augmented` 
+ `sbertresolve_icd10cm_augmented_billable_hcc` 
+ `meddra_hlt_pt_mapper` 
+ `meddra_llt_snomed_mapper` 
+ `meddra_pt_hlt_mapper` 
+ `sbiobertresolve_icd10cm_generalised_augmented` 
+ `snomed_meddra_llt_mapper`
+ `meddra_llt_resolver_pipeline` 
+ `meddra_pt_resolver_pipeline` 
+ `explain_clinical_doc_vop_small`
+ `explain_clinical_doc_cancer_type`
+ `sentence_detector_dl_healthcare_v2_wip`
+ `explain_clinical_doc_oncology`
+ `ndc_resolver_pipeline`
+ `explain_clinical_doc_cancer_type`
+ `sbiobertresolve_ndc`
+ `state_matcher`
+ `country_matcher`
+ `zip_parser`
+ `jsl_meds_q16_v2`
+ `jsl_meds_q8_v2`
+ `jsl_meds_q4_v2`
+ `jsl_meds_q16_v3`
+ `jsl_meds_q8_v3`
+ `jsl_meds_q4_v3`
+ `oncology_biomarker_pipeline`
+ `rxnorm_resolver_pipeline`
+ `icd10cm_rxnorm_resolver_pipeline`
+ `medication_resolver_pipeline`
+ `medication_resolver_transform_pipeline`
+ `ner_deid_subentity_augmented_v2` 
+ `ner_deid_generic_docwise`
+ `ner_deid_subentity_augmented_docwise`
+ `ner_deid_subentity_docwise`
+ `ner_deid_aipii`
+ `explain_clinical_doc_sdoh_small`
+ `icd10cm_chronic_indicator_mapper`
+ `jsl_meds_ner_q4_v2`
+ `jsl_meds_ner_q8_v2`
+ `jsl_meds_ner_q16_v2`
+ `jsl_medm_q4_v1`
+ `jsl_medm_q8_v1`
+ `jsl_medm_q16_v1`
+ `jsl_medsner_zs_q4_v1`
+ `jsl_medsner_zs_q8_v1`
+ `jsl_medsner_zs_q16_v1`
+ `jsl_meds_q4_v1`
+ `jsl_meds_q8_v1`
+ `jsl_meds_q16_v1`
+ `jsl_meds_rag_q4_v1`
+ `jsl_meds_rag_q8_v1`
+ `jsl_meds_rag_q16_v1`
+ `clinical_deidentification_docwise_wip`
+ `clinical_deidentification_v2_wip`
+ `clinical_deidentification_nameAugmented_v2`
+ `ner_ade_clinical_v2`
+ `bert_sequence_classifier_ade_augmented_v2`
+ `sbiobertresolve_loinc`
+ `sbiobertresolve_loinc_augmented`
+ `sbiobertresolve_loinc_numeric`


</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">



## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
