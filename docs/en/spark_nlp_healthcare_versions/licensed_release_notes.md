---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2024-01-18
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.2.1

#### Highlights

We are delighted to announce a suite of remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release comes with a new Opioid NER model as well as 23 new clinical pretrained models and pipelines**.

+ Introducing a new named entity recognition (NER) model for extracting information regarding `Opioid` usage
+ Introducing a new multilingual NER model to extract `NAME` entities for Deidentification purposes
+ Clinical document analysis with state-of-the-art Pretrained Pipelines for specific clinical tasks and concepts
+ Returning text embeddings within sentence entity resolution models
+ Setting entity pairs for relation labels in `RelationExtractionDLModel` to reduce false positives
+ Cluster and CPU speed benchmarks for Chunk Mapper, Entity Resolver, and Deidentification pipelines
+ ONNX support for `ZeroShotNerModel`, `MedicalBertForSequenceClassification`, `MedicalBertForTokenClassification`, and `MedicalDistilBertForSequenceClassification`
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
  - The error caused by `splitChars` in `NerConverterInternal` has been resolved
  - Fixed loading from disk issue for `ChunkConverter`, `AnnotationMerger`, and `GenericRE` annotators
  - `ContextualParser` now supports unlimited document size
  - Updated settings in `sparknlp_jsl.start()` function for Spark configuration
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
  - New [Opioid Demo](https://demo.johnsnowlabs.com/healthcare/NER_OPIOID/)
  - New [Structured Streaming with Spark NLP for Healthcare Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/39.Structured_Streaming_with_SparkNLP_for_Healthcare.ipynb)
  - Updated [Clinical Relation Extraction Model Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/10.Clinical_Relation_Extraction.ipynb)
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

We believe that these enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">

#### Introducing A New Opioid Named Entity Recognition (NER) Model For Extracting Information Regarding `Opioid` Usage
This model is designed to detect and label opioid-related entities within text data. Opioids are a class of drugs that include the illegal drug heroin, synthetic opioids such as fentanyl, and pain relievers available legally by prescription. The model has been trained using advanced deep-learning techniques on a diverse range of text sources and can accurately recognize and classify a wide range of opioid-related entities.
The model’s accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results.

Please see the model card [ner_opioid_small_wip](https://nlp.johnsnowlabs.com/2024/01/11/ner_opioid_small_wip_en.html) for more information about the model

*Example*:

```python
ner_model = MedicalNerModel.pretrained("ner_opioid_small_wip", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

sample_texts = """20 year old male transferred from [**Hospital1 112**] for liver transplant evaluation after percocet overdose. On Sunday [**3-27**] had a stressful day and pt took approximately 20 percocet (5/325) throughout the day after a series of family arguments. Denies trying to hurt himself. Parents confirm to suicidal attempts in the past. Pt felt that he had a hangover on Monday secondary to "percocet withdrawal" and took an additional 5 percocet.  Pt was admitted to the SICU and followed by Liver, Transplant, Toxicology, and [**Month/Year (2) **].  He was started on NAC q4hr with gradual decline in LFT's and INR.  His recovery was c/b hypertension, for which he was started on clonidine.  Pt was  transferred to the floor on [**4-1**].

Past Medical History:
Bipolar D/o (s/p suicide attempts in the past)
ADHD
S/p head injury [**2160**]: s/p MVA with large L3 transverse process
fx, small right frontal epidural hemorrhage-- with
post-traumatic seizures (was previously on dilantin, now dc'd)

Social History:
Father is HCP, student in [**Name (NI) 108**], Biology major, parents and brother live in [**Name (NI) 86**], single without children, lived in a group home for 3 years as a teenager, drinks alcohol 1 night a week, denies illict drug use, pt in [**Location (un) 86**] for neuro eval
"""
```

*Result*:

|chunk            |begin|end |ner_label             |
|-----------------|-----|----|----------------------|
|percocet         |92   |99  |opioid_drug           |
|20               |178  |179 |drug_quantity         |
|percocet         |181  |188 |opioid_drug           |
|5/325            |191  |195 |drug_strength         |
|suicidal attempts|303  |319 |psychiatric_issue     |
|hangover         |356  |363 |general_symptoms      |
|percocet         |389  |396 |opioid_drug           |
|withdrawal       |398  |407 |general_symptoms      |
|5                |433  |433 |drug_quantity         |
|percocet         |435  |442 |opioid_drug           |
|NAC              |567  |569 |other_drug            |
|q4hr             |571  |574 |drug_frequency        |
|decline in LFT's |589  |604 |general_symptoms      |
|clonidine        |679  |687 |other_drug            |
|Bipolar          |761  |767 |psychiatric_issue     |
|suicide attempts |778  |793 |psychiatric_issue     |
|ADHD             |808  |811 |psychiatric_issue     |
|dilantin         |976  |983 |other_drug            |
|illict drug use  |1236 |1250|substance_use_disorder|

Please check the [Opioid Demo](https://demo.johnsnowlabs.com/healthcare/NER_OPIOID/)


</div><div class="h3-box" markdown="1">

#### Introducing A New Multilingual NER Model To Extract `NAME` Entities For Deidentification Purposes

Introducing our latest invention Multilingual Named Entity Recognition model which annotates English, German, French, Italian, Spanish, Portuguese, and Romanian text to find `NAME` entities that may need to be de-identified. It was trained with in-house annotated datasets and detects NAME entities. We plan to expand this multilingual NER model to other PHI entities in the upcoming releases.

*Example*:

```python
embeddings = XlmRoBertaEmbeddings.pretrained("xlm_roberta_base", "xx") \
    .setInputCols("sentence", "token") \
    .setOutputCol("embeddings")\
    .setMaxSentenceLength(512)\
    .setCaseSensitive(False)

ner = MedicalNerModel.pretrained("ner_deid_name_multilingual", "xx", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")


text = ["""Record date: 2093-01-13, David Hale, M.D., Name: Hendrickson, Ora MR. # 7194334 Date: 01/13/93 PCP: Oliveira, 25 years old, Record date: 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227. The patient's complaints first surfaced when he started working for Brothers Coal-Mine.""",
"""J'ai vu en consultation Michel Martinez (49 ans) adressé au Centre Hospitalier De Plaisir pour un diabète mal contrôlé avec des symptômes datant de Mars 2015.""",
"""Michael Berger wird am Morgen des 12 Dezember 2018 ins St. Elisabeth-Krankenhaus in Bad Kissingen eingeliefert. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen.""",
"""Ho visto Gastone Montanariello (49 anni) riferito all' Ospedale San Camillo per diabete mal controllato con sintomi risalenti a marzo 2015."""]
```

*Result*:

| doc_id |                chunks | begin | end | entities |
|-------:|----------------------:|------:|----:|----------|
|      0 |            David Hale |    26 |  35 |     NAME |
|      0 |      Hendrickson, Ora |    51 |  66 |     NAME |
|      0 |              Oliveira |   104 | 111 |     NAME |
|      1 |       Michel Martinez |    24 |  38 |     NAME |
|      2 |        Michael Berger |     0 |  13 |     NAME |
|      2 |                Berger |   117 | 122 |     NAME |
|      3 | Gastone Montanariello |     9 |  29 |     NAME |

Please see the model card [ner_deid_name_multilingual](https://nlp.johnsnowlabs.com/2024/01/17/ner_deid_name_multilingual_xx.html) for more information about the model

</div><div class="h3-box" markdown="1">



#### Clinical Document Analysis With State-Of-The-Art Pretrained Pipelines For Specific Clinical Tasks And Concepts

We introduce a suite of advanced, hybrid pretrained pipelines, specifically designed to streamline the process of analyzing clinical documents. These pipelines are built upon multiple state-of-the-art (SOTA) pretrained models, delivering a comprehensive solution for extracting vital information with unprecedented ease.

What sets this release apart is the elimination of complexities typically involved in building and chaining models. Users no longer need to navigate the intricacies of constructing intricate pipelines from scratch or the uncertainty of selecting the most effective model combinations. Our new pretrained pipelines simplify these processes, offering a seamless, user-friendly experience.


| Pipeline Name                                                            |      Description            |
|--------------------------------------------------------------------------|-------------------------------------------|
| [`explain_clinical_doc_generic`](https://nlp.johnsnowlabs.com/2024/01/16/explain_clinical_doc_generic_en.html) | This pipeline is designed to extract all clinical/medical entities, assign assertion status to the extracted entities, establish relations between the extracted entities from the clinical texts. |
| [`explain_clinical_doc_oncology`](https://nlp.johnsnowlabs.com/2024/01/16/explain_clinical_doc_oncology_en.html) | This specialized oncology pipeline can extract oncological entities, assign assertion status to the extracted entities, establish relations between the extracted entities from the clinical documents. |
| [`explain_clinical_doc_vop`](https://nlp.johnsnowlabs.com/2024/01/16/explain_clinical_doc_vop_en.html) | This pipeline is designed to extract healthcare-related terms entities, assign assertion status to the extracted entities, establish relations between the extracted entities from the documents transferred from the patient’s sentences. |
| [`ner_vop_pipeline`](https://nlp.johnsnowlabs.com/2024/01/10/ner_vop_pipeline_en.html) | This pipeline includes the full taxonomy Named-Entity Recognition model to extract information from health-related text in colloquial language. This pipeline extracts diagnoses, treatments, tests, anatomical references, and demographic entities.  |
| [`ner_oncology_pipeline`](https://nlp.johnsnowlabs.com/2024/01/08/ner_oncology_pipeline_en.html) | This pipeline extracts more than 40 oncology-related entities, including therapies, tests and staging |
| [`oncology_diagnosis_pipeline`](https://nlp.johnsnowlabs.com/2024/01/09/oncology_diagnosis_pipeline_en.html) | This pipeline includes Named-Entity Recognition, Assertion Status, Relation Extraction and Entity Resolution models to extract information from oncology texts. This pipeline focuses on entities related to oncological diagnosis |
| [`clinical_deidentification`](https://nlp.johnsnowlabs.com/2024/01/10/clinical_deidentification_en.html) | This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. |
| [`clinical_deidentification_langtest`](https://nlp.johnsnowlabs.com/2024/01/10/clinical_deidentification_langtest_en.html) | This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. |
| [`summarizer_clinical_laymen_onnx_pipeline`](https://nlp.johnsnowlabs.com/2024/01/09/summarizer_clinical_laymen_onnx_pipeline_en.html) | This model is a modified version of LLM based summarization model that is finetuned with custom dataset by John Snow Labs to avoid using clinical jargon on the summaries |
| [`clinical_notes_qa_base_onnx_pipeline`](https://nlp.johnsnowlabs.com/2024/01/10/clinical_notes_qa_base_onnx_pipeline_en.html) | This model is capable of open-book question answering on Medical Notes. |
| [`clinical_notes_qa_large_onnx_pipeline`](https://nlp.johnsnowlabs.com/2024/01/10/clinical_notes_qa_large_onnx_pipeline_en.html) | This model is capable of open-book question answering on Medical Notes. |
| [`medical_qa_biogpt_pipeline`](https://nlp.johnsnowlabs.com/2024/01/09/medical_qa_biogpt_pipeline_en.html) |  This pipeline is trained on Pubmed abstracts and then finetuned with PubmedQA dataset. |
| [`flan_t5_base_jsl_qa_pipeline`](https://nlp.johnsnowlabs.com/2024/01/10/flan_t5_base_jsl_qa_pipeline_en.html) | This pipeline provides a powerful and efficient solution for accurately answering medical questions and delivering insightful information in the medical domain. |
| [`atc_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/01/17/atc_resolver_pipeline_en.html) | This pipeline extracts `DRUG` entities from clinical texts and map these entities to their corresponding Anatomic Therapeutic Chemical (ATC) codes. |
| [`cpt_procedures_measurements_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/01/17/cpt_procedures_measurements_resolver_pipeline_en.html) | This pipeline extracts `Procedure` and `Measurement` entities and maps them to corresponding Current Procedural Terminology (CPT) codes. |
| [`hcc_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/01/17/hcc_resolver_pipeline_en.html) |This advanced pipeline extracts clinical conditions from clinical texts and maps these entities to their corresponding Hierarchical Condition Categories (HCC) codes. |
| [`hpo_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/01/17/hpo_resolver_pipeline_en.html) | This advanced pipeline extracts human phenotype entities from clinical texts and maps these entities to their corresponding HPO codes. |
| [`snomed_body_structure_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/01/17/snomed_body_structure_resolver_pipeline_en.html) | This pipeline extracts anatomical structure entities and maps them to their corresponding SNOMED (body structure version) codes. |
| [`snomed_findings_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/01/17/snomed_findings_resolver_pipeline_en.html) | This pipeline extracts clinical findings and maps them to their corresponding SNOMED (CT version) codes. |


</div><div class="h3-box" markdown="1">

####  Returning Text Embeddings Within Sentence Entity Resolution Models

The unique aspect highlighted in this implementation is the use of the `setReturnResolvedTextEmbeddings` parameter. By setting it to `True`, the code allows for the inclusion of embeddings for resolved text candidates, enabling a more comprehensive analysis and understanding of the resolved entities within the clinical text. This parameter provides flexibility by allowing users to either include or exclude embeddings based on their requirements, with the default setting being `False`.


*Example*:

```python
rxnorm_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("rxnorm_code")\
    .setDistanceFunction("EUCLIDEAN")\
    .setReturnResolvedTextEmbeddings(True)

text = 'metformin 100 mg'
```

*Result*:

|            text|                                                                                          embeddings|
|----------------|----------------------------------------------------------------------------------------------------|
|metformin 100 mg| -0.20578815, 0.25846115, -0.7783525, 0.80831814, 0.91270417, -0.43411028, 0.41243184, 0.2023627... |



</div><div class="h3-box" markdown="1">


#### Setting Entity Pairs For Relation Labels Feature In `RelationExtractionDLModel` to Reduce False Positives

`RelationExtractionDLModel` now includes the ability to set entity pairs for each relation label, giving you more control over your results and even greater accuracy.

In the following example, we utilize entity pair restrictions to limit the results of Relation Extraction labels solely to relations that exist between specified entities, thus improving the accuracy and relevance of the extracted data. If we don't set the `setRelationTypePerPair` parameter here, the REDL model may return different RE labels for these specified entities.

*Example*:

```python
clinical_re_Model = RelationExtractionDLModel().pretrained('redl_clinical_biobert', "en", "clinical/models")\
    .setInputCols(["re_ner_chunks", "sentence"]) \
    .setOutputCol("relations")\
    .setRelationPairsCaseSensitive(False)\
    .setRelationTypePerPair({"TrAP": ["PROBLEM-TREATMENT"],
                             "TrIP": ["TREATMENT-PROBLEM"],
                             "TrWP": ["TREATMENT-PROBLEM"],
                             "TrCP": ["TREATMENT-PROBLEM"],
                             "TrAP": ["TREATMENT-PROBLEM"],
                             "TrNAP":["TREATMENT-PROBLEM"],
                             "TeCP": ["PROBLEM-TEST"],
                             "TeRP": ["PROBLEM-TEST"],
                             "PIP":  ["PROBLEM-PROBLEM"]
                             })

text ="""She was treated with a five-day course of amoxicillin for a respiratory tract infection . She was on metformin , glipizide , and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG .
She had been on dapagliflozin for six months at the time of presentation. Physical examination on presentation was significant for dry oral mucosa ; significantly , her abdominal examination was benign with no tenderness , guarding , or rigidity .
Pertinent laboratory findings on admission were : serum glucose 111 mg/dl , bicarbonate 18 mmol/l , anion gap 20 , creatinine 0.4 mg/dL , triglycerides 508 mg/dL , total cholesterol 122 mg/dL , glycated hemoglobin ( HbA1c ) 10% , and venous pH 7.27 . Serum lipase was normal at 43 U/L .
Serum acetone levels could not be assessed as blood samples kept hemolyzing due to significant lipemia . The patient was initially admitted for starvation ketosis , as she reported poor oral intake for three days prior to admission .
However , serum chemistry obtained six hours after presentation revealed her glucose was 186 mg/dL , the anion gap was still elevated at 21 , serum bicarbonate was 16 mmol/L , triglyceride level peaked at 2050 mg/dL , and lipase was 52 U/L .
The β-hydroxybutyrate level was obtained and found to be elevated at 5.29 mmol/L - the original sample was centrifuged and the chylomicron layer removed prior to analysis due to interference from turbidity caused by lipemia again .
The patient was treated with an insulin drip for euDKA and HTG with a reduction in the anion gap to 13 and triglycerides to 1400 mg/dL , within 24 hours . Her euDKA was thought to be precipitated by her respiratory tract infection in the setting of SGLT2 inhibitor use .
The patient was seen by the endocrinology service and she was discharged on 40 units of insulin glargine at night , 12 units of insulin lispro with meals , and metformin 1000 mg two times a day . It was determined that all SGLT2 inhibitors should be discontinued indefinitely . She had close follow-up with endocrinology post discharge .
"""
```

*Result*:

|sentence | chunk1                      | entity1 | chunk2            | entity2 | relation |confidence |
|--------:|:----------------------------|:--------|:------------------|:--------|:---------|----------:|
|       3 | Physical examination        | TEST    | dry oral mucosa   | PROBLEM | TeRP     |  0.99 |
|       4 | her abdominal examination   | TEST    | tenderness        | PROBLEM | TeRP     |  0.99 |
|       4 | her abdominal examination   | TEST    | guarding          | PROBLEM | TeRP     |  0.99 |
|       4 | her abdominal examination   | TEST    | rigidity          | PROBLEM | TeRP     |  0.99 |
|       9 | her glucose                 | TEST    | still elevated    | PROBLEM | TeRP     |  0.97 |
|       9 | the anion gap               | TEST    | still elevated    | PROBLEM | TeRP     |  0.99 |
|       9 | still elevated              | PROBLEM | serum bicarbonate | TEST    | TeRP     |  0.97 |
|       9 | still elevated              | PROBLEM | lipase            | TEST    | TeRP     |  0.93 |
|       9 | still elevated              | PROBLEM | U/L               | TEST    | TeRP     |  0.94 |
|      10 | The β-hydroxybutyrate level | TEST    | elevated          | PROBLEM | TeRP     |  0.99 |


Please check the [Clinical Relation Extraction Model Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/10.Clinical_Relation_Extraction.ipynb) for more information.


</div><div class="h3-box" markdown="1">

#### Cluster and CPU Speed Benchmark for Chunk Mapper, Entity Resolver, and Deidentification Pipelines

Dive into the heart of healthcare data processing with our benchmark experiment meticulously designed for Mapper, Resolver, and Deidentification Pipelines. This benchmark provides crucial insights into the performance of these pipelines under varied configurations and dataset conditions.

Cluster configuration:
  - Driver Name: Standard_DS3_v2
  - Driver Memory: 14GB
  - Worker Name: Standard_DS3_v2
  - Worker Memory: 14GB
  - Worker Cores: 4
  - Action: write_parquet
  - Total Worker Numbers: 10
  - Total Cores: 40

These figures might differ based on the size of the mapper and resolver models. The larger the models, the higher the inference times. Depending on the success rate of mappers (any chunk coming in caught by the mapper successfully), the combined mapper and resolver timing would be less than resolver-only timing.

If the resolver-only timing is equal to or very close to the combined mapper and resolver timing, it means that the mapper is not capable of catching/ mapping any chunk. In that case, try playing with various parameters in the mapper or retrain/ augment the mapper.

- Mapper and Resolver Benchmark Experiment

**Dataset:** 100 Clinical Texts from MTSamples, approx. 705 tokens and 11 chunks per text.

| partition | mapper timing | resolver timing | mapper and resolver timing |
| --------: | -------------:| ---------------:| ----------------------:|
| 4         | 40.8 sec      | 4.55 mins       | 3.20 mins              |
| 8         | 30.1 sec      | 3.34 mins       | 1.59 mins              |
| 16        | 11.6 sec      | 1.57 mins       | 1.12 mins              |
| 32        | 7.84 sec      | 1.33 mins       | 55.9 sec               |
| 64        | 7.25 sec      | 1.18 mins       | 56.1 sec               |
| 100       | 7.45 sec      | 1.05 mins       | 47.5 sec               |
| 1000      | 8.87 sec      | 1.14 mins       | 47.9 sec               |

Explore the efficiency of our `clinical_deidentification` pipeline through a dedicated benchmark experiment. Unearth performance metrics and make informed decisions to enhance your healthcare data processing workflows.

- Deidentification Benchmark Experiment
  - DataBricks Config: 32 CPU Core, 128GiB RAM (8 worker)
  - AWS Config: 32 CPU Cores, 58GiB RAM (c6a.8xlarge)
  - Colab Config: 8 CPU Cores 52GiB RAM (Colab Pro - High RAM)

**Dataset:** 1000 Clinical Texts from MTSamples, approx. 503 tokens and 21 chunks per text.

| partition | AWS <br> result timing | DataBricks <br> result timing | Colab <br> result timing |
|----------:|-------------:|-------------:|-------------:|
| 1024      |  1 min 3 sec | 1 min 55 sec | 5 min 45 sec |
| 512       |       56 sec | 1 min 26 sec | 5 min 15 sec |
| 256       |       50 sec | 1 min 20 sec | 5 min  4 sec |
| 128       |       45 sec | 1 min 21 sec | 5 min 11 sec |
| 64        |       46 sec | 1 min 31 sec | 5 min 3 sec  |
| 32        |       46 sec | 1 min 26 sec | 5 min 0 sec  |
| 16        |       56 sec | 1 min 43 sec | 5 min 3 sec  |
| 8         | 1 min 21 sec | 2 min 33 sec | 5 min 3 sec  |
| 4         | 2 min 26 sec | 4 min 53 sec | 6 min 3 sec  |


Please check the [Cluster Speed Benchmarks](https://nlp.johnsnowlabs.com/docs/en/benchmark) page for more information.



</div><div class="h3-box" markdown="1">

#### ONNX Support for `ZeroShotNerModel`, `MedicalBertForSequenceClassification`, `MedicalBertForTokenClassification`, and `MedicalDistilBertForSequenceClassification`

We are thrilled to announce the integration of ONNX support for several critical annotators, enhancing the versatility of our healthcare models. The following models now benefit from ONNX compatibility:

- ZeroShotNerModel
- MedicalBertForSequenceClassification
- MedicalBertForTokenClassification
- MedicalDistilBertForSequenceClassification

This update opens doors to a wider range of deployment scenarios and interoperability with other systems that support the Open Neural Network Exchange (ONNX) format. Experience heightened efficiency and integration capabilities as you incorporate these models into your healthcare workflows. Stay at the forefront of healthcare AI with the latest in interoperable model support.

</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, And Reliability Of Spark NLP For Healthcare

- The error caused by `splitChars` in `NerConverterInternal` has been resolved
- Fixed loading issue for `ChunkConverter`, `AnnotationMerger`, and `GenericRE` annotators
- `ContextualParser` now supports unlimited document size
- Updated settings in `sparknlp_jsl.start()` function for Spark configuration

</div><div class="h3-box" markdown="1">


#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [Opioid Demo](https://demo.johnsnowlabs.com/healthcare/NER_OPIOID/)
- New [Structured Streaming with SparkNLP for Healthcare Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/39.Structured_Streaming_with_SparkNLP_for_Healthcare.ipynb)
- Updated [Clinical Relation Extraction Model Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/10.Clinical_Relation_Extraction.ipynb)

</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.



+ `ner_deid_name_multilingual`
+ `ner_opioid_small_wip`
+ `ner_oncology_pipeline`
+ `ner_vop_pipeline`
+ `oncology_diagnosis_pipeline`
+ `summarizer_clinical_laymen_onnx_pipeline`
+ `clinical_notes_qa_base_onnx_pipeline`
+ `clinical_notes_qa_large_onnx_pipeline`
+ `medical_qa_biogpt_pipeline`
+ `flan_t5_base_jsl_qa_pipeline`
+ `clinical_deidentification`
+ `clinical_deidentification_langtest`
+ `explain_clinical_doc_generic`
+ `explain_clinical_doc_vop`
+ `explain_clinical_doc_oncology`
+ `explain_clinical_doc_radiology`
+ `atc_resolver_pipeline`
+ `cpt_procedures_measurements_resolver_pipeline`
+ `hcc_resolver_pipeline`
+ `hpo_resolver_pipeline`
+ `snomed_findings_resolver_pipeline`
+ `snomed_body_structure_resolver_pipeline`
+ `sbiobertresolve_rxnorm_augmented`



</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">



## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
