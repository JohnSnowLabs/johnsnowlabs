---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes 5.3.1
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_5_3_1
key: docs-licensed-release-notes
modify_date: 2024-03-27
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.3.1

#### Highlights


We are delighted to announce remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release comes with MedDRA resolver, 2x faster optimized Deidentification pipelines,  Response to Treatment classifier for oncology, and 41 new clinical pretrained models and pipelines. It's as big as a major release!**

+ Welcoming MedDRA into the library. Releasing 8 new Entity Resolver and Mapper models to associate clinical entities with MedDRA LLT and PT codes. 
+ Enhancing assertion annotation workflow with `AssertionMerger` annotator to allow using multiple assertion models within the same pipeline.
+ Adding new clinical deidentification pipelines that are 2x faster. Now we have 15 pretrained deidentification pipelines of various sizes and capabilities.
+ Efficiency analysis and cost evaluation of deidentification pipelines on cloud platforms
+ Updated `Opioid` NER model and `Drug` text matcher model
+ New text classifier for `Response to Treatment` to detect response status/ outcome for the treatment applied for oncology patients.
+ 2 new Entity Resolver models for associating SNOMED clinical entities.
+ Clinical document analysis with one-liner pretrained pipelines for specific clinical tasks and concepts.
+ A new augmented NER model for multilingual `name` extraction by leveraging the capabilities of the LangTest library to boost its robustness significantly.
+ `DatasetInfo` parameter added to `SentenceEntityResolver` annotator to track the source datasets' versions.
+ Robust exception handling to allow skipping only the corrupted records processed via `GenericClassifier`, `BertSentenceChunkEmbeddings`, `AssertionFilterer`, `ChunkFilterer`, `ContextualParser`, `ChunkMerge` and `Deidentification` annotators.
+ Changed the license of CPT and MedDRA models in the ModelHub, and attempting to use them in Healthcare NLP now throws an error.
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
    - Fixed sentence positions in `MedicalBertForSequenceClassification`
    - Updated Deidentification Module according to the latest spark versions
    - Updated ALAB Module for assertion result according to tokenization flexibility
    - Deprecation of the `setRel` Method in `ChunkMapper`: Transitioning to the `setRels` parameter
    - Enhancements in SentenceEntityResolver: Bug Fix and Annotator Refactor
    - Added `assertion_source`, `ner_chunk`, and `ner_label` metadata fields to the `AssertionDL` and `AssertionLogReg` annotators
    - Implemented fixes and enhancements related to entity handling and resolution in Resolver and ChunkMapper, including incorporating an `entity` field in resolver metadata from embeddings, rectifying the entity field assignment in `ChunkMapper`, and resolving a bug with `all_k_resolutions` when using `setMultivaluesRelations(True)` in `ChunkMapper`
    - Updated init.py and the path of class for `BertSentenceChunkEmbedding`
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
    - New [Task Based Clinical Pretrained Pipelines Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.3.Task_Based_Clinical_Pretrained_Pipelines.ipynb)
    - Updated [Clinical Assertion Model Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.Clinical_Assertion_Model.ipynb)
    - Updated [Snomed Entity Resolver Model Training Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/13.Snomed_Entity_Resolver_Model_Training.ipynb)
    - New [Response to Treatment Classification Demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_RESPONSE_TO_TREATMENT/)
    - Updated [Opioid Demo](https://demo.johnsnowlabs.com/healthcare/OPIOID/) 
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">

#### Welcoming MedDRA into the Library. Releasing 10 New Entity Resolver, Mapper Models and Pretrained Pipelines to Associate Clinical Entities With Meddra Llt and Pt Codes


Introducing 2 new Sentence Entity Resolver Models  `sbiobertresolve_meddra_lowest_level_term` and `sbiobertresolve_meddra_preferred_term` help to map medical entities to MedDRA codes.

| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`sbiobertresolve_meddra_lowest_level_term`](https://nlp.johnsnowlabs.com/2024/03/24/sbiobertresolve_meddra_lowest_level_term_en.html) | This model maps clinical terms to their corresponding MedDRA LLT (Lowest Level Term) codes. |
| [`sbiobertresolve_meddra_preferred_term`](https://nlp.johnsnowlabs.com/2024/03/04/sbiobertresolve_meddra_preferred_term_en.html) | This model maps clinical terms to their corresponding MedDRA PT (Preferred Term) codes. |


*Example*:

```python
meddra_resolver = SentenceEntityResolverModel.load("sbiobertresolve_meddra_lowest_level_term") \
     .setInputCols(["sbert_embeddings"]) \
     .setOutputCol("meddra_llt_code")\
     .setDistanceFunction("EUCLIDEAN")

text= """This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, chronic obstructive pulmonary disease, gastritis, and transient ischemic attack. He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of the left main coronary artery stenosis, which was complicated by hypotension and bradycardia."""
```

*Result*:

|                     chunk|           label|meddra_llt_code|              resolution|           all_codes|            all_resolutions|
|--------------------------|----------------|---------------|------------------------|--------------------|---------------------------|
|                              tobacco|                  Smoking|       10067622|                  tobacco interaction|10067622,10086359...|tobacco interaction,tobaccoism,tobac...|
|                         hypertension|             Hypertension|       10020772|                         hypertension|10020772,10020790...|hypertension,hypertension secondary,...|
|          chronic renal insufficiency|           Kidney_Disease|       10050441|          chronic renal insufficiency|10050441,10009122...|chronic renal insufficiency,chronic ...|
|chronic obstructive pulmonary disease|Disease_Syndrome_Disorder|       10009033|chronic obstructive pulmonary disease|10009033,10009032...|chronic obstructive pulmonary diseas...|
|                            gastritis|Disease_Syndrome_Disorder|       10017853|                            gastritis|10017853,10060703...|gastritis,verrucous gastritis,antral...|
|            transient ischemic attack|  Cerebrovascular_Disease|       10072760|            transient ischemic attack|10072760,10044390...|transient ischemic attack,transient ...|
|              cardiac catheterization|                Procedure|       10048606|              cardiac catheterization|10048606,10007527...|cardiac catheterization,cardiac cath...|
|   left main coronary artery stenosis|            Heart_Disease|       10090240|   left main coronary artery stenosis|10090240,10072048...|left main coronary artery stenosis,l...|
|                          hypotension|               VS_Finding|       10021097|                          hypotension|10021097,10021107...|hypotension,hypotensive,arterial hyp...|
|                          bradycardia|               VS_Finding|       10006093|                          bradycardia|10006093,10040741...|bradycardia,sinus bradycardia,centra...|

- 6 ChunkMapper Models for Medical Code Mapping to Map Various Medical Terminologies Across Each Other

Introducing a suite of new ChunkMapper models designed to streamline medical code mapping tasks. These models include mappings between  RxNorm, ICD-10, MedDRA-LLT, and MedDRA-PT codes, offering a comprehensive solution for interoperability within medical systems.

| Model Name                                                            |      Description           |
|-----------------------------------------------------------------------|----------------------------|
|[`icd10_meddra_llt_mapper`](https://nlp.johnsnowlabs.com/2024/03/14/icd10_meddra_llt_mapper_en.html)| Maps ICD-10 codes to corresponding MedDRA LLT (Lowest Level Term) codes. |
|[`meddra_llt_icd10_mapper`](https://nlp.johnsnowlabs.com/2024/03/14/meddra_llt_icd10_mapper_en.html)| Maps MedDRA-LLT (Lowest Level Term) codes to corresponding ICD-10 codes. |
|[`icd10_meddra_pt_mapper`](https://nlp.johnsnowlabs.com/2024/03/15/icd10_meddra_pt_mapper_en.html)  | Maps ICD-10 codes to corresponding MedDRA-PT (Preferred Term) codes. |
|[`meddra_pt_icd10_mapper`](https://nlp.johnsnowlabs.com/2024/03/15/meddra_pt_icd10_mapper_en.html)  | Maps MedDRA-PT (Preferred Term) codes to corresponding ICD-10 codes.   |
|[`meddra_llt_pt_mapper`](https://nlp.johnsnowlabs.com/2024/03/18/meddra_llt_pt_mapper_en.html)      | Maps MedDRA-LLT (Lowest Level Term) codes to their corresponding MedDRA-PT (Preferred Term) codes. |
|[`meddra_pt_llt_mapper`](https://nlp.johnsnowlabs.com/2024/03/18/meddra_pt_llt_mapper_en.html)      | Maps MedDRA-PT (Preferred Term) codes to their corresponding MedDRA-LLT (Lowest Level Term) codes. |

*Example*:

```python
mapperModel = ChunkMapperModel.load('meddra_llt_pt_mapper')\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["icd10_code"])

text = ["10002442", "10000007", "10003696"]
```

*Result*:

|llt_code|pt_code                                 |
|--------|----------------------------------------|
|10002442|10002442:Angiogram pulmonary normal     |
|10000007|10000007:17 ketosteroids urine decreased|
|10003696|10001324:Adrenal atrophy                |

- Introducing 2 New Pretrained Meddra Resolver Pipelines Designed For Effortless Integration With Just A Single Line Of Code

These pipelines are capable of extracting clinical entities and linking them to their respective MedDRA LLT and PT codes, while also facilitating mapping of these codes to LLT/PT or ICD-10 codes.

| Pipeline Name                                                            |      Description            |
|--------------------------------------------------------------------------|-----------------------------|
| [`meddra_llt_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/03/26/meddra_llt_resolver_pipeline_en.html) | This dedicated pipeline extracts clinical terms and links them to their corresponding MedDRA LLT (Lowest Level Term) codes, map those codes to their MedDRA PT (Preferred Term) codes and ICD-10 codes.|
| [`meddra_pt_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/03/07/meddra_pt_resolver_pipeline_en.html) | This dedicated pipeline  extracts clinical terms and links them to their corresponding MedDRA PT (Preferred Term) codes, map those codes to their MedDRA LLT (Lowest Level Term) codes and ICD-10 codes. |

*Example*:

```python
from sparknlp.pretrained import PretrainedPipeline

meddra_llt_pipeline = PretrainedPipeline.from_disk("meddra_llt_resolver_pipeline")

result = meddra_llt_pipeline.fullAnnotate('This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, chronic obstructive pulmonary disease, gastritis, and transient ischemic attack.')
```

*Result*:


|chunk                                 |label                    |meddra_llt_code|resolution                           |icd10_mappings                                                                     |meddra_pt_mappings                             |
|--------------------------------------|-------------------------|---------------|-------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------|
|tobacco                               |Smoking                  |10067622       |tobacco interaction                  |NONE                                                                               |10067622:Tobacco interaction                   |
|hypertension                          |Hypertension             |10020772       |hypertension                         |O10:Pre-existing hypertension complicating pregnancy, childbirth and the puerperium|10020772:Hypertension                          |
|chronic renal insufficiency           |Kidney_Disease           |10050441       |chronic renal insufficiency          |NONE                                                                               |10064848:Chronic kidney disease                |
|chronic obstructive pulmonary disease |Disease_Syndrome_Disorder|10009033       |chronic obstructive pulmonary disease|J44:Other chronic obstructive pulmonary disease                                    |10009033:Chronic obstructive pulmonary disease |
|gastritis                             |Disease_Syndrome_Disorder|10017853       |gastritis                            |K29.6:Other gastritis                                                              |10017853:Gastritis                             |
|transient ischemic attack             |Cerebrovascular_Disease  |10072760       |transient ischemic attack            |NONE                                                                               |10044390:Transient ischaemic attack            |

**Important note**: To utilize these MedDRA models/pipelines, possession of a valid MedDRA license is requisite. When you want to use these models and pipelines, you will receive a warning like below.  If you possess a valid MedDRA license and wish to use this model, kindly contact us at support@johnsnowlabs.com.

```bash
IllegalArgumentException: 'meddra_llt_pt_mapper' model cannot be used as a pretrained model.
To load this model locally via .load(), possession of a valid MedDRA / CPT license is required.
If you possess one thru corresponding agencies and wish to use this model, contact us at support@johnsnowlabs.com.
```

</div><div class="h3-box" markdown="1">

#### Enhancing Assertion Annotation Workflow with AssertionMerger Annotator to Allow using Multiple Assertion Models within the Same Pipeline.

Introducing the latest addition to our annotation toolkit, the AssertionMerger Annotator, designed to streamline the merging process of assertion columns from various annotators like AssertionDL and AssertionLogReg. This powerful tool offers customizable parameters for filtering, prioritizing, and seamlessly combining assertion annotations. Learn how to leverage features like merging overlapping annotations, applying filters before or after merging, and prioritizing based on confidence levels and assertion sources. Optimize your annotation workflow with AssertionMerger Annotator, ensuring efficient and accurate consolidation of assertion data.


**Parameters:**

- `mergeOverlapping`: Whether to merge overlapping matched assertion annotations. Default: `True`
- `applyFilterBeforeMerge`: Whether to apply filtering before the merging process. If `True`, filtering will be applied before merging; if `False`, filtering will be applied after the merging process. Default: `False`.
- `blackList`: If defined, list of entities to ignore. The rest will be processed.
- `whiteList`: If defined, list of entities to process. The rest will be ignored. Do not include the IOB prefix on labels.
- `caseSensitive`: Determines whether the definitions of the white-listed and black-listed entities are case sensitive. Default: `True`.
- `assertionsConfidence`: Pairs (assertion, confidenceThreshold) to filter assertions that have confidence lower than the confidence threshold.
- `orderingFeatures`: Specifies the ordering features to use for overlapping entities. Possible values include: 'begin', 'end', 'length', 'source', and 'confidence'. Default: `['begin', 'length', 'source']`
- `selectionStrategy`: Determines the strategy for selecting annotations. Annotations can be selected either sequentially based on their order (Sequential) or using a more diverse strategy (DiverseLonger). Currently, only Sequential and DiverseLonger options are available. Default: `Sequential`.
- `defaultConfidence`:  When the confidence value is included in the orderingFeatures and a given annotation does not have any confidence, this parameter determines the value to be used. The default value is `0`.
- `assertionSourcePrecedence`: Specifies the assertion sources to use for prioritizing overlapping annotations when the 'source' ordering feature is utilized. This parameter contains a comma-separated list of assertion sources that drive the prioritization. Annotations will be prioritized based on the order of the given string.
- `sortByBegin`: Whether to sort the annotations by begin at the end of the merge and filter process. Default: `False`.


*Example*:

```python
# Assertion model trained on i2b2 (sampled from MIMIC) dataset
assertion_jsl = AssertionDLModel.pretrained("assertion_jsl_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_jsl_chunk", "embeddings"]) \
    .setOutputCol("assertion_jsl")\
    .setEntityAssertionCaseSensitive(False)

# Assertion model trained on radiology dataset
assertion_dl = AssertionDLModel.pretrained("assertion_dl", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_clinical_chunk", "embeddings"]) \
    .setOutputCol("assertion_dl")

assertion_merger = AssertionMerger() \
    .setInputCols("assertion_jsl", "assertion_dl") \
    .setOutputCol("assertion_merger") \
    .setMergeOverlapping(True) \
    .setSelectionStrategy("sequential") \
    .setAssertionSourcePrecedence("assertion_dl, assertion_jsl") \
    .setCaseSensitive(False) \
    .setAssertionsConfidence({"past": 0.70}) \
    .setOrderingFeatures(["length", "source", "confidence"]) \
    .setDefaultConfidence(0.50)


text = [
    """Patient had a headache for the last 2 weeks, and appears anxious when she walks fast. No alopecia noted. She denies pain. Her father is paralyzed and it is a stressor for her. She got antidepressant. We prescribed sleeping pills for her current insomnia."""
]
```

*Result*:

|idx|ner_chunk     |begin|end|ner_label|assertion|assertion_source|confidence|
|---|--------------|-----|---|---------|---------|----------------|----------|
|0  |headache      |14   |21 |Symptom  |Past     |assertion_jsl   |0.9999    |
|0  |anxious       |57   |63 |PROBLEM  |present  |assertion_dl    |0.9392    |
|0  |alopecia      |89   |96 |PROBLEM  |absent   |assertion_dl    |0.9992    |
|0  |pain          |116  |119|PROBLEM  |absent   |assertion_dl    |0.9884    |
|0  |paralyzed     |136  |144|Symptom  |Family   |assertion_jsl   |0.9995    |
|0  |stressor      |158  |165|Symptom  |Family   |assertion_jsl   |1.0       |
|0  |antidepressant|184  |197|TREATMENT|present  |assertion_dl    |0.9628    |
|0  |sleeping pills|214  |227|TREATMENT|present  |assertion_dl    |0.998     |
|0  |insomnia      |245  |252|Symptom  |Past     |assertion_jsl   |0.9862    |


Please check [Clinical Assertion Model Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.Clinical_Assertion_Model.ipynb) for more information

</div><div class="h3-box" markdown="1">

    
####  Adding New Clinical Deidentification Pipelines for Flexible Deployments

The Comprehensive Clinical Deidentification Pipeline offers a robust solution for anonymizing sensitive PHI (Protected Health Information) from medical texts. This versatile pipeline is equipped to mask and obfuscate a wide array of PHI entities including A`AGE`, `CONTACT`, `DATE`, `ID`, `LOCATION`, `NAME`, `PROFESSION`, `CITY`, `COUNTRY`, `DOCTOR`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `ORGANIZATION`, `PATIENT`, `PHONE`, `PROFESSION`, `STREET`, `USERNAME`, `ZIP`, `ACCOUNT`, `LICENSE`, `VIN`, `SSN`, `DLN`, `PLATE`, `IPADDR`, and more. With support for multiple languages including `Arabic`, `German`,  `French`, `English` `Spanish`, `Italian`, `Portuguese`, and `Romanian` this pipeline ensures compliance with privacy regulations across diverse healthcare settings. Choose from various models optimized for different use cases, such as obfuscation levels and subentity recognition, to tailor the deidentification process according to specific requirements.


|index|model|lang|
|-----:|:-----|----|
| 1| [clinical_deidentification](https://nlp.johnsnowlabs.com/2022/09/14/clinical_deidentification_en.html)  | ar, de, en, es, fr, it, pt, ro|
| 2| [clinical_deidentification_augmented](https://nlp.johnsnowlabs.com/2022/03/03/clinical_deidentification_augmented_es_2_4.html)  |es|
| 3| [clinical_deidentification_generic](https://nlp.johnsnowlabs.com/2024/02/21/clinical_deidentification_generic_en.html)  |en|
| 4| [clinical_deidentification_generic_optimized](https://nlp.johnsnowlabs.com/2024/03/14/clinical_deidentification_generic_optimized_en.html)  |en|
| 5| [clinical_deidentification_glove](https://nlp.johnsnowlabs.com/2022/03/04/clinical_deidentification_glove_en_3_0.html)  |en|
| 6| [clinical_deidentification_glove_augmented](https://nlp.johnsnowlabs.com/2022/09/16/clinical_deidentification_glove_augmented_en.html)  |en|
| 7| [clinical_deidentification_langtest](https://nlp.johnsnowlabs.com/2024/01/10/clinical_deidentification_langtest_en.html)  |en|
| 8| [clinical_deidentification_multi_mode_output](https://nlp.johnsnowlabs.com/2024/03/27/clinical_deidentification_multi_mode_output_en.html)  |en|
| 9| [clinical_deidentification_obfuscation_medium](https://nlp.johnsnowlabs.com/2024/02/09/clinical_deidentification_obfuscation_medium_en.html)  |en|
| 10| [clinical_deidentification_obfuscation_small](https://nlp.johnsnowlabs.com/2024/02/09/clinical_deidentification_obfuscation_small_en.html)  |en|
| 11| [clinical_deidentification_slim](https://nlp.johnsnowlabs.com/2023/06/17/clinical_deidentification_slim_en.html)  |en|
| 12| [clinical_deidentification_subentity](https://nlp.johnsnowlabs.com/2024/02/21/clinical_deidentification_subentity_en.html)  |en|
| 13| [clinical_deidentification_subentity_nameAugmented](https://nlp.johnsnowlabs.com/2024/03/14/clinical_deidentification_subentity_nameAugmented_en.html)  |en|
| 14| [clinical_deidentification_subentity_optimized](https://nlp.johnsnowlabs.com/2024/03/14/clinical_deidentification_subentity_optimized_en.html)  |en|
| 15| [clinical_deidentification_wip](https://nlp.johnsnowlabs.com/2023/06/17/clinical_deidentification_wip_en.html)  |en|

We will share a detailed table on our [wiki page](https://nlp.johnsnowlabs.com/docs/en/wiki) soon to explain the pros and cons of each model as well as tips and tricks to show how to use them effectively

</div><div class="h3-box" markdown="1">

#### Efficiency Analysis and Cost Evaluation of Deidentification Pipelines on Cloud Platforms

These results show speed benchmarks and cost evaluations for deidentification pipelines deployed across diverse cloud platforms, including AWS EMR and EC2. Additionally, forthcoming results from DataBricks promise to further enrich the analysis, offering deeper insights into de-identification pipeline performance. 


| Partition | EMR <br> Base Pipeline | EMR <br> Optimized Pipeline | EC2 Instance <br> Base Pipeline | EC2 Instance <br> Optimized Pipeline |
|-----------|--------------------|------------------------|----------------------------|---------------------------------|
| 1024      | 5 min 1 sec        | 2 min 45 sec           | 7 min 6 sec                | **3 min 26 sec**                |
| 512       | 4 min 52 sec       | 2 min 30 sec           | **6 min 56 sec**           | 3 min 41 sec                    |
| 256       | **4 min 50 sec**   | **2 min 30 sec**       | 9 min 10 sec               | 5 min 18 sec                    |
| 128       | 4 min 55 sec       | 2 min 30 sec           | 14 min 30 sec              | 7 min 51 sec                    |
| 64        | 6 min 24 sec       | 3 min 8 sec            | 18 min 59 sec              | 9 min 9 sec                     |
| 32        | 7 min 15 sec       | 3 min 43 sec           | 18 min 47.2 sec            | 9 min 18 sec                    |
| 16        | 11 min 6 sec       | 4 min 57 sec           | 12 min 47.5 sec            | 6 min 14 sec                    |
| 8         | 19 min 13 se       | 8 min 8 sec            | 16 min 52 sec              | 8 min 48 sec                    |

Estimated Minimum Costs:
- EMR Base Pipeline: partition number: 256, 10K cost:**$1.04**, 1M cost:**$104.41** 
- EMR Optimized Pipeline: partition number: 256, 10K cost:**$0.54**, 1M cost:**$54.04** 
- EC2 Instance Base Pipeline: partition number: 512, 10K cost:**$0.36**, 1M cost:**$35.70** 
- EC2 Instance Optimized Pipeline: partition number: 1024, 10K cost:**$0.18**, 1M cost:**$17.85** 
- DataBricks results will be published soon.


</div><div class="h3-box" markdown="1">

#### Updated Opioid-related Named Entity Recognition and Drug-related Text Matcher Models

- [ner_opioid](https://nlp.johnsnowlabs.com/2024/03/27/ner_opioid_en.html): This Updated Opioid-related Named Entity Recognition model has been enhanced with new annotated text data. Opioids are a class of drugs that include the illegal drug heroin, synthetic opioids such as fentanyl, and pain relievers available legally by prescription. The model is designed to detect and label opioid-related entities within text data. It has been retrained using advanced deep learning techniques on an expanded and diversified range of text sources, including newly annotated text specifically focused on opioid-related content.

*Example*:

```python
ner_model = MedicalNerModel.pretrained("ner_opioid", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

sample_texts = """History of Present Illness: A 20-year-old male was transferred from an outside hospital for evaluation for liver transplant following a Percocet overdose. On Sunday, March 27th, he experienced a stressful day and consumed approximately 20 Percocet (5/325) tablets throughout the day following a series of family arguments. He denies any intent to harm himself, although his parents confirm past suicidal attempts. On Monday, he felt he was experiencing a Percocet withdrawal "hangover" and took an additional 5 Percocet. He was admitted to the Surgical Intensive Care Unit (SICU) and received care from Liver, Transplant, Toxicology. Treatment included Naloxone every 4 hours, resulting in a gradual improvement in liver function tests (LFTs) and INR. During recovery, he developed hypertension and was initiated on clonidine."""
```


*Result*:

|chunk                      |begin|end |ner_label             |
|---------------------------|-----|----|----------------------|
|Percocet                   |136  |143 |opioid_drug           |
|overdose                   |145  |152 |other_disease         |
|20                         |236  |237 |drug_quantity         |
|Percocet                   |239  |246 |opioid_drug           |
|tablets                    |256  |262 |drug_form             |
|harm himself               |347  |358 |violence              |
|suicidal attempts          |395  |411 |psychiatric_issue     |
|Percocet                   |455  |462 |opioid_drug           |
|withdrawal                 |464  |473 |general_symptoms      |
|hangover                   |476  |483 |general_symptoms      |
|5                          |509  |509 |drug_quantity         |
|Percocet                   |511  |518 |opioid_drug           |
|Naloxone                   |653  |660 |antidote              |
|every 4 hours              |662  |674 |drug_frequency        |
|hypertension               |782  |793 |other_disease         |
|clonidine                  |816  |824 |other_drug            |

*Benchmark*:

```bash
                 label  precision    recall  f1-score   support
           alcohol_use       0.92      0.95      0.94       353
              antidote       1.00      0.99      0.99       141
  communicable_disease       0.76      0.88      0.82       224
         drug_duration       0.81      0.71      0.75       238
             drug_form       0.97      0.95      0.96       614
        drug_frequency       0.94      0.97      0.96      1527
         drug_quantity       0.96      0.94      0.95      2169
            drug_route       0.95      0.98      0.97       903
         drug_strength       0.84      0.95      0.89       388
            employment       0.79      0.63      0.70       306
      general_symptoms       0.90      0.84      0.87      4483
           legal_issue       0.73      0.52      0.61        84
        marital_status       0.95      0.95      0.95        57
           opioid_drug       0.98      0.96      0.97       725
         other_disease       0.91      0.90      0.90      4145
            other_drug       0.94      0.93      0.94      2617
     psychiatric_issue       0.88      0.85      0.86      1356
    sexual_orientation       1.00      0.78      0.88        23
substance_use_disorder       0.91      0.88      0.90       276
                  test       0.97      0.93      0.95       102
           test_result       1.00      0.93      0.97        30
              violence       0.81      0.71      0.76       542
             micro-avg       0.92      0.89      0.90     21303
             macro-avg       0.91      0.87      0.89     21303
          weighted-avg       0.91      0.89      0.90     21303
```

- [drug_matcher](https://nlp.johnsnowlabs.com/2024/03/19/drug_matcher_en.html): The latest iteration of the Drug-related Text Matcher Model has been enhanced significantly, boasting an expanded database with the inclusion of an additional 100 thousand drugs. Through meticulous curation, the model has undergone refinement by strategically eliminating words that may have previously led to false positives. 

*Example*:

```python
text_matcher = TextMatcherInternalModel.pretrained("drug_matcher","en","clinical/models") \
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_text")\

sample_texts = """John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD on 2023-12-01."""
```

*Result*:

|       chunk|begin|end|label|
|------------|-----|---|-----|
|     aspirin|   25| 31| DRUG|
| paracetamol|   69| 79| DRUG|
| amoxicillin|  109|119| DRUG|
|lansoprazole|  144|155| DRUG|




</div><div class="h3-box" markdown="1">

#### New Oncological Response to Treatment Classification Model

The Oncological Response to Treatment classifier was trained on a diverse dataset, this model provides accurate label assignments and confidence scores for its predictions. The primary goal of this model is to categorize text into two key labels: `Yes` and `No`.

*Example*:

```python
sequenceClassifier = MedicalBertForSequenceClassification\
    .pretrained("bert_sequence_classifier_response_to_treatment", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("prediction")


sample_texts = [
    "The breast ultrasound after neoadjuvant chemotherapy displayed a decrease in the primary lesion size from 3 cm to 1 cm, suggesting a favorable response to treatment. The skin infection is also well controlled with a multi-antibiotic approach. ",
    "MRI of the pelvis indicated no further progression of endometriosis after laparoscopic excision and six months of hormonal suppression therapy.",
    "A repeat endoscopy revealed healing gastric ulcers with new signs of malignancy or H. pylori infection. Will discuss the PPI continuum.",
    "Dynamic contrast-enhanced MRI of the liver revealed no significant reduction in the size and number of hepatic metastases following six months of targeted therapy with sorafenib."
]
```

*Result*:

|                                                                                               text |result|
|----------------------------------------------------------------------------------------------------|------|
|The breast ultrasound after neoadjuvant chemotherapy displayed a decrease in the primary lesion s...| Yes |
|MRI of the pelvis indicated no further progression of endometriosis after laparoscopic excision a...| Yes |
|A repeat endoscopy revealed healing gastric ulcers with new signs of malignancy or H. pylori infe...| No  |
|Dynamic contrast-enhanced MRI of the liver revealed no significant reduction in the size and numb...| No  |

*Benchmark*:

```bash
       label  precision    recall  f1-score   support
          No     0.9927    0.9875    0.9901      3031
         Yes     0.8430    0.9027    0.8718       226
    accuracy          -         -    0.9816      3257
   macro-avg     0.9178    0.9451    0.9309      3257
weighted-avg     0.9823    0.9816    0.9819      3257
```

</div><div class="h3-box" markdown="1">


#### 2 New Sentence Entity Resolver Models for Associating SNOMED Clinical Entities

Introducing 2 new Sentence Entity Resolver Models `sbiobertresolve_snomed_no_class` and `sbiobertresolve_snomed_conditions` help to map medical entities to SNOMED codes.


| Model Name                                                            |      Description            |
|--------------------------------------------------------------------------|-------------------------------------------|
| [`sbiobertresolve_snomed_no_class`](https://nlp.johnsnowlabs.com/2024/03/05/sbiobertresolve_snomed_no_class_en.html) | This model maps extracted medical entities (no concept class) to SNOMED codes. |
| [`sbiobertresolve_snomed_conditions`](https://nlp.johnsnowlabs.com/2024/03/04/sbiobertresolve_snomed_conditions_en.html) | This model maps clinical conditions to their corresponding SNOMED (domain: Conditions) codes. |



*Example*:

```python
resolver = SentenceEntityResolverModel\
    .pretrained("sbiobertresolve_snomed_conditions", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

text = """Medical professionals rushed in the bustling emergency room to attend to the patient with alarming symptoms.
The attending physician immediately noted signs of respiratory distress, including stridor, a high-pitched sound indicative of upper respiratory tract obstruction.
The patient, struggling to breathe, exhibited dyspnea. Concern heightened when they began experiencing syncope,
a sudden loss of consciousness likely stemming from inadequate oxygenation. Further examination revealed a respiratory tract hemorrhage."""

```

*Result*:

|                              chunk|                    label|snomed_code|                         resolution|             all_codes|                               all_resolutions|
|-----------------------------------|-------------------------|-----------|-----------------------------------|----------------------|----------------------------------------------|
|               respiratory distress|               VS_Finding|  271825005|               respiratory distress|271825005,418092006...|respiratory distress,respiratory tract cong...|
|                            stridor|                  Symptom|   70407001|                            stridor|70407001,301826004:...|stridor,intermittent stridor,inhalatory str...|
|                 high-pitched sound|                  Symptom|   51406002|                 high pitched voice|51406002,271661003:...|high pitched voice,heart sounds exaggerated...|
|upper respiratory tract obstruction|Disease_Syndrome_Disorder|   68372009|upper respiratory tract obstruction|68372009,79688008::...|upper respiratory tract obstruction,respira...|
|              struggling to breathe|                  Symptom|  289105003|   difficulty controlling breathing|289105003,230145002...|difficulty controlling breathing,difficulty...|
|                            dyspnea|                  Symptom|  267036007|                            dyspnea|267036007,60845006:...|dyspnea,exertional dyspnea,inspiratory dysp...|
|                            syncope|                  Symptom|  271594007|                            syncope|271594007,234167006...|syncope,situational syncope,tussive syncope...|
|              loss of consciousness|                  Symptom|  419045004|              loss of consciousness|419045004,44077006:...|loss of consciousness,loss of sensation,los...|
|             inadequate oxygenation|                  Symptom|  238161004|           impaired oxygen delivery|238161004,70944005:...|impaired oxygen delivery,impaired gas excha...|
|       respiratory tract hemorrhage|Disease_Syndrome_Disorder|   95431003|       respiratory tract hemorrhage|95431003,233783005:...|respiratory tract hemorrhage,tracheal hemor...|



</div><div class="h3-box" markdown="1">

#### Clinical Document Analysis with One-Liner Pretrained Pipelines for Specific Clinical Tasks and Concepts

We introduce a suite of advanced, hybrid pretrained pipelines, specifically designed to streamline the process of analyzing clinical documents. These pipelines are built upon multiple state-of-the-art (SOTA) pretrained models, delivering a comprehensive solution for extracting vital information with unprecedented ease.

What sets this release apart is the elimination of complexities typically involved in building and chaining models. Users no longer need to navigate the intricacies of constructing intricate pipelines from scratch or the uncertainty of selecting the most effective model combinations. Our new pretrained pipelines simplify these processes, offering a seamless, user-friendly experience.


| Pipeline Name                                                            |      Description            |
|--------------------------------------------------------------------------|-----------------------------|
| [`icd10cm_rxnorm_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/03/07/icd10cm_rxnorm_resolver_pipeline_en.html) | This pipeline can extract clinical conditions and medication entities, map the clinical conditions to their respective ICD-10-CM codes, and medication entities to RxNorm codes. |
| [`snomed_term_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/03/22/snomed_term_resolver_pipeline_en.html) | This pretrained resolver pipeline extracts SNOMED terms and maps them to their corresponding SNOMED codes. |
| [`snomed_findings_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/03/03/snomed_findings_resolver_pipeline_en.html) | This pipeline extracts clinical findings and maps them to their corresponding SNOMED (CT version) codes. |
| [`snomed_body_structure_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/03/05/snomed_body_structure_resolver_pipeline_en.html) | This pipeline extracts anatomical structure entities and maps them to their corresponding SNOMED (body structure version) codes. |
| [`snomed_auxConcepts_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/03/12/snomed_auxConcepts_resolver_pipeline_en.html) | This pipeline extracts `Morph Abnormality`, `Clinical Drug`, `Clinical Drug Form`, `Procedure`, `Substance`, `Physical Object`, and `Body Structure` concepts from clinical notes, then maps them to their corresponding SNOMED codes. |
| [`snomed_conditions_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/03/11/snomed_conditions_resolver_pipeline_en.html) | This advanced pipeline extracts clinical conditions from clinical texts and map these entities to their corresponding SNOMED codes. |
| [`snomed_drug_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/03/11/snomed_drug_resolver_pipeline_en.html) | This advanced pipeline extracts drug entities from clinical texts and maps these entities to their corresponding SNOMED codes. |
| [`snomed_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/03/11/snomed_resolver_pipeline_en.html) | This pipeline extracts `Clinical Findings `, `Morph Abnormality`, `Clinical Drug`, `Clinical Drug Form`, `Procedure`, `Substance`, `Physical Object`, and `Body Structure` concepts from clinical notes and maps them to their corresponding SNOMED codes. |
| [`clinical_deidentification_generic_optimized`](https://nlp.johnsnowlabs.com/2024/03/14/clinical_deidentification_generic_optimized_en.html) | This pipeline can be used to deidentify PHI information from medical texts. |
| [`clinical_deidentification_nameAugmented`](https://nlp.johnsnowlabs.com/2024/03/14/clinical_deidentification_subentity_nameAugmented_en.html) | This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. |
| [`clinical_deidentification_subentity_optimized`](https://nlp.johnsnowlabs.com/2024/03/14/clinical_deidentification_subentity_optimized_en.html) | This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be obfuscated in the resulting text and also masked with entity labels in the metadata. |
| [`explain_clinical_doc_public_health`](https://nlp.johnsnowlabs.com/2024/03/19/explain_clinical_doc_public_health_en.html) | This specialized public health pipeline can extract public health-related entities, assign assertion status to the extracted entities, establish relations between the extracted entities from the clinical documents. In this pipeline, five NER, one assertion, and one relation extraction model were used to achieve those tasks. |
| [`explain_clinical_doc_biomarker`](https://nlp.johnsnowlabs.com/2024/03/11/explain_clinical_doc_biomarker_en.html) | This specialized biomarker pipeline can extract biomarker entities, classify sentences whether they contain biomarker entities or not, establish relations between the extracted biomarker and biomarker results from the clinical documents. |
| [`explain_clinical_doc_risk_factors`](https://nlp.johnsnowlabs.com/2024/03/25/explain_clinical_doc_risk_factors_en.html) | This pipeline is designed to extract all clinical/medical entities, which may be considered as risk factors from text, assign assertion status to the extracted entities, establish relations between the extracted entities. |
| [`clinical_deidentification_multi_mode_output`](https://nlp.johnsnowlabs.com/2024/03/26/clinical_deidentification_multi_mode_output_en.html) | This pipeline simultaneously produces masked with entity labels, fixed-length char, same-length char and obfuscated version of the text. |


</div><div class="h3-box" markdown="1">

#### A New Augmented NER Model for Multilingual Name Extraction by Leveraging the Capabilities of the LangTest Library to Boost Their Robustness Significantly

The newly introduced augmented NER model namely ner_deid_name_multilingual_clinical_langtest is powered by the innovative LangTest library. This cutting-edge NLP toolkit is at the forefront of language processing advancements, incorporating state-of-the-art techniques and algorithms to enhance the capabilities of our models significantly.

*Example*:

```python
ner = MedicalNerModel.pretrained("ner_deid_name_multilingual_clinical_langtest", "xx", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")


text_list = [
    """Record date: 2093-01-13, David Hale, M.D., Name: Hendrickson, Ora MR. # 7194334 Date: 01/13/93 PCP: Oliveira, 25 years old, Record date: 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227. The patient's complaints first surfaced when he started working for Brothers Coal-Mine.""",     
    """J'ai vu en consultation Michel Martinez (49 ans) adressé au Centre Hospitalier De Plaisir pour un diabète mal contrôlé avec des symptômes datant de Mars 2015.""",   
    """Michael Berger wird am Morgen des 12 Dezember 2018 ins St. Elisabeth-Krankenhaus in Bad Kissingen eingeliefert. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen."""    ,
    """Ho visto Gastone Montanariello (49 anni) riferito all' Ospedale San Camillo per diabete mal controllato con sintomi risalenti a marzo 2015.""",
    """Antonio Miguel Martínez, un varón de 35 años de edad, de profesión auxiliar de enfermería y nacido en Cadiz, España. Aún no estaba vacunado, se infectó con Covid-19 el dia 14 de Marzo y tuvo que ir al Hospital. Fue tratado con anticuerpos monoclonales en la Clinica San Carlos.""",
    """Detalhes do paciente:
    Nome do paciente: Pedro Gonçalves NHC: 2569870 Endereço: Rua Das Flores 23. Cidade/ Província: Porto Código Postal: 21754-987 Dados de cuidados Data de nascimento: 10/10/1963 Idade: 53 anos Data de admissão: 17/06/2016 Doutora: Maria Santos""",
    """Spitalul Pentru Ochi de Deal, Drumul Oprea Nr. 972 Vaslui, 737405 România Tel: +40(235)413773 Data setului de analize: 25 May 2022 15:36:00 Nume&Prenume: BUREAN MARIA, Varsta: 77 CNP: 2450502264401"""
]
```

*Result*:

|              ner_chunk|begin|end|ner_label|
|-----------------------|-----|---|---------|
|             David Hale|   25| 34|     NAME|
|       Hendrickson, Ora|   49| 64|     NAME|
|     Brothers Coal-Mine|  291|308|     NAME|
|        Michel Martinez|   24| 38|     NAME|
|         Michael Berger|    0| 13|     NAME|
|                 Berger|  117|122|     NAME|
|  Gastone Montanariello|    9| 29|     NAME|
|Antonio Miguel Martínez|    0| 22|     NAME|
|        Pedro Gonçalves|   41| 55|     NAME|
|           Maria Santos|  251|262|     NAME|
|           BUREAN MARIA|  154|165|     NAME|

Please check: [ner_deid_name_multilingual_clinical_langtest](https://nlp.johnsnowlabs.com/2024/03/12/ner_deid_name_multilingual_clinical_langtest_xx.html)



</div><div class="h3-box" markdown="1">

#### `DatasetInfo` Parameter Added to `SentenceEntityResolver` Annotator to Track the Source Datasets' Versions.

Introduced a setDatasetInfo param to SentenceEntityResolverApproach annotator to let users add dataset information (version, year, etc.) to the "model metadata" not the output.

*Example:*

```python
bertExtractor = SentenceEntityResolverApproach()\
  .setNeighbours(25)\
  .setThreshold(1000)\
  .setInputCols("bert_embeddings")\
  .setNormalizedCol("concept_name")\
  .setLabelCol("conceptId")\
  .setOutputCol('snomed_code')\
  .setDistanceFunction("EUCLIDIAN")\
  .setCaseSensitive(False)\
  .setDatasetInfo("the model version:531")
```



</div><div class="h3-box" markdown="1">

#### Robust Exception Handling to Allow Skipping only the Corrupted Records Processed via `GenericClassifier`, `BertSentenceChunkEmbeddings`, `AssertionFilterer`, `ChunkFilterer`, `ContextualParser`, `ChunkMerge` and `Deidentification` Annotators

We added the `doExceptionHandling` parameter into `GenericClassifier`, `BertSentenceChunkEmbeddings`, `AssertionFilterer`, `ChunkFilterer`, `ContextualParser`, `ChunkMerge` and `Deidentification` annotators for a robust exception handling if the process is broken down due to corrupted inputs. Suppose it is set as `True`. In that case, the annotator tries to process as usual and if exception-causing data (e.g. corrupted record/ document) is passed to the annotator, an exception warning is emitted which has the exception message. **Processing continues with the next one** while the rest of the records within the same batch are parsed without interruption. The default behavior is `False` and will throw an exception and break the process to inform users.

*Example*:

```python
deidentification = DeIdentification() \
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("mask")\
    .setDoExceptionHandling(True)
```


</div><div class="h3-box" markdown="1">

#### Changed the license of  CPT and MedDRA Models in the ModelHub, and Attempting to Use Them in Healthcare NLP now Throws an Error

The CPT and MedDRA models have been removed from the S3 storage. As a result, when attempting to use these models in Spark NLP, a new error message is thrown. The new error message states that the specified model (e.g., 'aaa') cannot be used as a pre-trained model. It further explains that to load the model locally using the .load() method, possession of a valid MedDRA or CPT license is required. If the user has such a license obtained through the corresponding agencies, they are instructed to contact the support team at support@johnsnowlabs.com to inquire about using the model.



</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, And Reliability Of Spark NLP For Healthcare

- Fixed sentence positions in `MedicalBertForSequenceClassification`
- Updated Deidentification Module according to the latest spark versions
- Updated ALAB Module for assertion result according to tokenization flexibility
- Deprecation of the `setRel` Method in `ChunkMapper`: Transitioning to the `setRels` parameter
- Enhancements in SentenceEntityResolver: Bug Fix and Annotator Refactor
- Added `assertion_source`, `ner_chunk`, and `ner_label` metadata fields to the `AssertionDL` and `AssertionLogReg` annotators
- Implemented fixes and enhancements related to entity handling and resolution in Resolver and ChunkMapper, including incorporating an `entity` field in resolver metadata from embeddings, rectifying the entity field assignment in `ChunkMapper`, and resolving a bug with `all_k_resolutions` when using `setMultivaluesRelations(True)` in `ChunkMapper`
- Updated init.py and the path of class for `BertSentenceChunkEmbedding`



</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [Task Based Clinical Pretrained Pipelines Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.3.Task_Based_Clinical_Pretrained_Pipelines.ipynb)
- Updated [Clinical Assertion Model Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.Clinical_Assertion_Model.ipynb) with AssertionMerger example
- Updated [Snomed Entity Resolver Model Training Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/13.Snomed_Entity_Resolver_Model_Training.ipynb) with new parameter
- New [Response to Treatment Classification Demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_RESPONSE_TO_TREATMENT/)
- Updated [Opioid Demo](https://demo.johnsnowlabs.com/healthcare/OPIOID/) with GPT4 comparison

</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.
+ `sbiobertresolve_snomed_no_class`
+ `sbiobertresolve_snomed_conditions`
+ `sbiobertresolve_meddra_lowest_level_term`
+ `sbiobertresolve_meddra_preferred_term`
+ `sbiobertresolve_snomed_bodyStructure`
+ `sbiobertresolve_snomed_drug`
+ `sbiobertresolve_snomed_findings_aux_concepts`
+ `ner_deid_name_multilingual_clinical_langtest`
+ `explain_clinical_doc_ade`
+ `explain_clinical_doc_biomarker`
+ `explain_clinical_doc_public_health`
+ `explain_clinical_doc_risk_factors`
+ `meddra_llt_resolver_pipeline`
+ `meddra_pt_resolver_pipeline`
+ `medication_resolver_pipeline`
+ `medication_resolver_transform_pipeline`
+ `ner_medication_pipeline`
+ `icd10cm_rxnorm_resolver_pipeline`
+ `snomed_term_resolver_pipeline`
+ `snomed_findings_resolver_pipeline`
+ `snomed_body_structure_resolver_pipeline`
+ `snomed_auxConcepts_resolver_pipeline`
+ `snomed_conditions_resolver_pipeline`
+ `snomed_drug_resolver_pipeline`
+ `snomed_resolver_pipeline`
+ `clinical_deidentification_generic_optimized`
+ `clinical_deidentification_nameAugmented`
+ `clinical_deidentification_subentity_optimized`
+ `umls_rxnorm_mapper`
+ `icd10_meddra_llt_mapper`
+ `meddra_llt_icd10_mapper`
+ `icd10_meddra_pt_mapper`
+ `meddra_pt_icd10_mapper`
+ `meddra_llt_pt_mapper`
+ `meddra_pt_llt_mapper`
+ `rxnorm_umls_mapper`
+ `drug_matcher`
+ `ner_opioid`
+ `clinical_deidentification`
+ `clinical_deidentification_multi_mode_output`
+ `bert_sequence_classifier_response_to_treatment`


</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">


## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
