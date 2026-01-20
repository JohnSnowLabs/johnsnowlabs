---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2025-12-09
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.2.2

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. This release introduces a new zero-shot NER chunking annotator, **PretrainedZeroShotNERChunker**, and advanced ZIP obfuscation controls for **Deidentification**, **StructuredDeidentification**, and **LightDeidentification** workflows.

+ Introducing a new zero-shot NER chunking annotator, `PretrainedZeroShotNERChunker`, enabling direct span-level entity extraction without token alignment
+ Advanced ZIP obfuscation controls with the new `setObfuscateZipKeepDigits` parameter, now supported across Deidentification, StructuredDeidentification, and LightDeidentification workflows
+ 7 new TextMatcher and parser models for enhanced clinical entity recognition, including specialized matchers for drug forms, medical devices, and other clinical concepts
+ A new clinical classification model for identifying sentences containing quantitative measurements
+ 4 new entity resolver models using `bge_base_en_v1_5_onnx` embeddings and 4 new mapper models for improved accuracy in medical code mapping
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain
+ Various core improvements, bug fixes, enhanced overall robustness, and reliability of Spark NLP for Healthcare
    - In pipelines that use the splitter component, `NerConverterInternal` could, in rare cases, miss tokens when overlapping spans occurred. This issue has been fixed, resulting in more robust handling of overlaps and improved consistency in entity conversion.


These enhancements will elevate your experience with Healthcare NLP, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">

#### New Zero-Shot NER Chunking Annotator: `PretrainedZeroShotNERChunker`

A new zero-shot NER annotator, `PretrainedZeroShotNERChunker`, has been introduced to simplify entity extraction workflows by producing **direct span-level entity chunks** from raw text. Unlike `PretrainedZeroShotNER`, this annotator does not require token alignment and enables fast, lightweight zero-shot entity extraction without any task-specific training data.

Key capabilities:

- Direct chunk-level entity extraction from `DOCUMENT` input
- No token alignment required, reducing pipeline complexity
- Fully zero-shot architecture—no annotated data needed
- Ideal for rapid prototyping, weak supervision, and exploratory NER workflows

*Example*:

PretrainedZeroShot NER (token-aligned, requires NerConverter)
```python
from johnsnowlabs import nlp, medical

text = """
Dr. Eleanor Vance, a neurologist at MountSinaiHospital,NewYorkCity recently consulted with patient JohnDoe.
Mr.Doe,55yearsold, has an appointment scheduled for October262025, regarding his condition.
"""

labels = ['DOCTOR', 'PATIENT', 'AGE', 'DATE', 'HOSPITAL', 'CITY', 'STREET', 'STATE', 'COUNTRY', 'PHONE', 'IDNUM', 'EMAIL','ZIP', 'ORGANIZATION', 'PROFESSION', 'USERNAME']

zeroshot_ner = medical.PretrainedZeroShotNER() \
    .pretrained("zeroshot_ner_deid_subentity_merged_medium", "en", "clinical/models") \
    .setInputCols("document", "token") \
    .setOutputCol("ner_zero_shot") \
    .setPredictionThreshold(0.5) \
    .setLabels(labels)

ner_converter = medical.NerConverter() \
    .setInputCols("document", "token", "ner_zero_shot") \
    .setOutputCol("ner_chunk_zero_shot")

```
*Results*

| begin | end | chunk          | entity  | confidence |
|-------|-----|----------------|---------|------------|
| 4     | 16  | Eleanor Vance  | DOCTOR  | 1.0        |
| 99    | 105 | JohnDoe        | PATIENT | 1.0        |
| 160   | 172 | October262025  | DATE    | 1.0        |
 

PretrainedZeroShotNERChunker (direct chunks)

```python
labels = ['DOCTOR', 'PATIENT', 'AGE', 'DATE', 'HOSPITAL', 'CITY', 'STREET', 'STATE', 'COUNTRY', 'PHONE', 'IDNUM', 'EMAIL','ZIP', 'ORGANIZATION', 'PROFESSION', 'USERNAME']

zeroshot_chunker = medical.PretrainedZeroShotNERChunker() \
    .pretrained("zeroshot_ner_deid_subentity_merged_medium", "en", "clinical/models") \
    .setInputCols("document") \
    .setOutputCol("ner_chunk_zero_shot") \
    .setPredictionThreshold(0.5) \
    .setLabels(labels)

```
*Results*

| begin | end | chunk              | entity   | confidence |
|-------|-----|--------------------|----------|------------|
| 4     | 16  | Eleanor Vance      | DOCTOR   | 0.99998724 |
| 36    | 53  | MountSinaiHospital | HOSPITAL | 0.99986887 |
| 55    | 65  | NewYorkCity        | CITY     | 0.99928530 |
| 99    | 105 | JohnDoe            | PATIENT  | 0.99999845 |
| 111   | 113 | Doe                | PATIENT  | 0.99999870 |
| 115   | 124 | 55yearsold         | AGE      | 0.99999976 |
| 160   | 172 | October262025      | DATE     | 1.0        |



**Why does `PretrainedZeroShotNERChunker` find more entities?**

- Works **directly at the span level**, not token-by-token  
- Not limited by tokenization (e.g., "55yearsold", "NewYorkCity", "MountSinaiHospital")  
- Detects **nested** or **overlapping** mentions (e.g., "JohnDoe" + "Doe")  
- Avoids IOB conversion issues caused by Spark NLP Tokenizer
- Produces more complete chunks because it evaluates the **full text span** rather than individual tokens



</div><div class="h3-box" markdown="1">

#### Advanced ZIP Code Obfuscation Controls Across All Deidentification Workflows

A new parameter, `setObfuscateZipKeepDigits`, has been added to provide finer control over ZIP code masking when applying HIPAA-compliant geographic de-identification. This enhancement allows users to customize how many leading ZIP digits are preserved before the remaining digits are masked.  
The parameter is now supported across **Deidentification**, **StructuredDeidentification**, and **LightDeidentification** workflows, ensuring consistent behavior in all de-identification pipelines.

Key capabilities:

- Preserves the first *N* digits of a ZIP code while masking the remainder
- Masks all trailing digits—including ZIP+4 extensions—with `*`
- Accepts values from **0 to 5** (default: **3**)
- Overrides the default HIPAA Safe Harbor ZIP generalization pattern
- Enables customizable expert-determination–aligned obfuscation strategies

**Examples**

| Input ZIP        | Keep = 3 (default) | Keep = 2 |
|------------------|--------------------|----------|
| `12345`          | `123**`            | `12***`  |

This new parameter provides significantly more flexibility for organizations seeking to balance privacy protection with analytical utility in their de-identification workflows.


</div><div class="h3-box" markdown="1">

#### 7 New TextMatcher and Parser Models for Enhanced Clinical Entity Recognition, Including Specialized Matchers for Drug Forms, Medical Devices, and Other Clinical Concepts

We have added 7 new `TextMatcher` and `ContextualParser` models that expand our clinical entity recognition capabilities with specialized dictionaries for various healthcare domains. These lightweight, dictionary-based models enable fast and accurate identification of domain-specific entities in clinical text.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`drug_form_matcher`](https://nlp.johnsnowlabs.com/2025/11/30/drug_form_matcher_en.html) | Identify drug form entities in clinical text |
| [`drug_route_matcher`](https://nlp.johnsnowlabs.com/2025/11/30/drug_route_matcher_en.html) | Identifies drug administration route entities in clinical text |
| [`drug_strength_parser`](https://nlp.johnsnowlabs.com/2025/11/30/drug_strength_parser_en.html) | Identifies drug strength entities in clinical text |
| [`medical_device_matcher`](https://nlp.johnsnowlabs.com/2025/11/30/medical_device_matcher_en.html) | Identifies medical device entities in clinical text |
| [`procedure_matcher`](https://nlp.johnsnowlabs.com/2025/11/30/procedure_matcher_en.html) | Identifies medical procedure entities in clinical text |
| [`symptom_matcher`](https://nlp.johnsnowlabs.com/2025/11/30/symptom_matcher_en.html) | Identify symptom entities in clinical text |
| [`test_result_parser`](https://nlp.johnsnowlabs.com/2025/11/30/test_result_parser_en.html) | Identifies test result entities in clinical text |


*Example:*

```python
drug_form_matcher = TextMatcherInternalModel.pretrained("drug_form_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_drug_form")


text = """The patient was started on Metformin 500mg tablet twice daily with meals. For pain, Oxycodone 5mg capsule every 6 hours PRN was prescribed. Insulin glargine injection 20 units subcutaneously at bedtime. Apply Hydrocortisone 1% cream to affected areas twice daily. Fentanyl 25mcg/hr transdermal patch applied every 72 hours. Albuterol solution via nebulizer every 4 hours PRN."""

data = spark.createDataFrame([[text]]).toDF("text")
result = pipeline.fit(data).transform(data)
```


*Result*:

{:.table-model-big}
|chunk            |begin|end|label    |
|-----------------|-----|---|---------|
|tablet           |44   |49 |DRUG_FORM|
|capsule          |97   |103|DRUG_FORM|
|injection        |149  |157|DRUG_FORM|
|cream            |220  |224|DRUG_FORM|
|transdermal patch|270  |286|DRUG_FORM|
|solution         |330  |337|DRUG_FORM|
|nebulizer        |343  |351|DRUG_FORM|




</div><div class="h3-box" markdown="1">

#### A New Clinical Classification Model for Identifying Sentences Containing Quantitative Measurements

A new binary classification model, `generic_classifier_measurement`, has been introduced to identify clinical sentences containing quantitative measurement information. This classifier streamlines the extraction and filtering of measurement-related content from clinical documentation, making it easier to isolate vital signs, lab results, and other numerical health data.

**Classes:**

- `MEASUREMENT`: Contains numerical health measurements, vital signs, lab results, or test values
- `OTHER`: Doesn't contain quantitative measurement information

*Example:*

```python
generic_classifier = GenericClassifierModel.pretrained("generic_classifier_measurement", "en", "clinical/models")\
    .setInputCols(["features"])\
    .setOutputCol("prediction")


sample_texts = [
    ["This is a 58-year-old male who started out having a toothache in the left lower side of the mouth that is now radiating into his jaw and towards his left ear."],
    ["The database was available at this point of time. WBC count is elevated at 19,000 with the left shift, hemoglobin of 17.7, and hematocrit of 55.8 consistent with severe dehydration."],
    ["Temperature max is 99, heart rate was 133 to 177, blood pressure is 114/43 (while moving), respiratory rate was 28 to 56 with O2 saturations 97 to 100% on room air."],
    ["I will see her back in followup in 3 months, at which time she will be recovering from a shoulder surgery."]
]

data = spark.createDataFrame(sample_texts).toDF("text")
result = clf_pipeline.fit(data).transform(data)
```

*Result:*

{:.table-model-big}
|text|prediction|
|----|----------|
|This is a 58-year-old male who started out having a toothache...|OTHER|
|The database was available at this point of time. WBC count is elevated at 19,000...|MEASUREMENT|
|Temperature max is 99, heart rate was 133 to 177, blood pressure is 114/43...|MEASUREMENT|
|I will see her back in followup in 3 months...|OTHER|




</div><div class="h3-box" markdown="1">

#### 3 New Entity Resolvers and 1 Mapper Using by `bge_base_en_v1_5_onnx` Embeddings for Improved Accuracy in Medical Code Mapping

We are introducing 3 new entity resolvers and 1 mapper built on the state-of-the-art `bge_base_en_v1_5_onnx` embeddings. These models leverage BGE (BAAI General Embeddings) for superior semantic understanding, resulting in more accurate medical code resolution and entity mapping across various healthcare terminologies.


{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`bgeresolve_icd10cm`](https://nlp.johnsnowlabs.com/2025/12/03/bgeresolve_icd10cm_en.html) | Maps clinical entities to ICD-10-CM codes using `bge_base_en_v1_5_onnx` embeddings |
| [`bgeresolve_rxnorm`](https://nlp.johnsnowlabs.com/2025/12/03/bgeresolve_rxnorm_en.html) | Maps drug entities to RxNorm codes using `bge_base_en_v1_5_onnx` embeddings |
| [`bgeresolve_snomed`](https://nlp.johnsnowlabs.com/2025/12/03/bgeresolve_snomed_en.html) | Maps clinical entities to SNOMED codes using `bge_base_en_v1_5_onnx` embeddings |
| [`bgeresolve_cpt`](https://nlp.johnsnowlabs.com/2025/12/04/bgeresolve_cpt_en.html) | Maps clinical entities to CPT codes using `bge_base_en_v1_5_onnx` embeddings |
| [`rxnorm_mapper`](https://nlp.johnsnowlabs.com/2025/12/04/rxnorm_mapper_en.html) | Maps drug entities to their corresponding RxNorm codes |
| [`snomed_mapper`](https://nlp.johnsnowlabs.com/2025/12/04/snomed_mapper_en.html) | Maps clinical entities to their corresponding SNOMED codes |
| [`icd10cm_mapper`](https://nlp.johnsnowlabs.com/2025/12/04/icd10cm_mapper_en.html) | Maps clinical entities to their corresponding ICD10CM codes |
| [`cpt_mapper`](https://nlp.johnsnowlabs.com/2025/12/04/cpt_mapper_en.html) | Maps clinical entities to their corresponding CPT codes |


*Example:*

```python
bge_embeddings = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")

icd10cm_resolver = SentenceEntityResolverModel.pretrained("bgeresolve_icd10cm", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("icd10cm_code")\
    .setDistanceFunction("EUCLIDEAN")

text = """A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis and obesity, presented with a one-week history of polyuria, polydipsia, and vomiting."""

data = spark.createDataFrame([[text]]).toDF("text")
result = pipeline.fit(data).transform(data)
```

*Result:*

{:.table-model-big}
|sent_id|ner_chunk                             |entity |icd10cm_code|resolutions                  |all_codes                                      |all_resolutions                                |
|-------|--------------------------------------|-------|------------|-----------------------------|-----------------------------------------------|-----------------------------------------------|
|0      |gestational diabetes mellitus         |PROBLEM|O24.4       |gestational diabetes mellitus|[O24.4, O24.41, O24.43, O24.42, O24.414, ...]  |[gestational diabetes mellitus, gestational di...]|
|0      |subsequent type two diabetes mellitus |PROBLEM|E11         |type 2 diabetes mellitus     |[E11, E11.69, E11.6, E11.64, E13, E11.65, ...] |[type 2 diabetes mellitus, type 2 diabetes mel...]|
|0      |T2DM                                  |PROBLEM|E11         |type 2 diabetes mellitus     |[E11, E11.65, E11.64, E11.9, E11.44, E11.5, ...]|[type 2 diabetes mellitus, type 2 diabetes mel...]|
|0      |HTG-induced pancreatitis              |PROBLEM|K85.3       |drug induced acute pancreatitis|[K85.3, K86.0, K85.2, K85.31, K85.21, ...]    |[drug induced acute pancreatitis, alcohol-indu...]|
|0      |acute hepatitis                       |PROBLEM|B15         |acute hepatitis a            |[B15, B16, B17.1, B17, B17.2, B17.9, ...]      |[acute hepatitis a, acute hepatitis b, acute h...]|
|0      |obesity                               |PROBLEM|E66         |overweight and obesity       |[E66, E66.9, E66.0, E66.8, E66.3, O99.21, ...] |[overweight and obesity, obesity, unspecified,...]|
|0      |polyuria                              |PROBLEM|R35         |polyuria                     |[R35, R35.89, R35.8, R35.81, R80, R80.8, ...]  |[polyuria, other polyuria, other polyuria, noc...]|
|0      |polydipsia                            |PROBLEM|R63.1       |polydipsia                   |[R63.1, O40, R35, R35.89, R35.8, R63.2, ...]   |[polydipsia, polyhydramnios, polyuria, other p...]|
|0      |vomiting                              |PROBLEM|R11.1       |vomiting                     |[R11.1, R11, R11.12, R11.10, R11.11, R11.13, ...]|[vomiting, nausea and vomiting, projectile vom...]|




</div><div class="h3-box" markdown="1">


#### New blog post ?



</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Healthcare NLP Easier To Navigate And Understand ?



</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `drug_form_matcher`
+ `drug_route_matcher`
+ `drug_strength_parser`
+ `medical_device_matcher`
+ `procedure_matcher`
+ `symptom_matcher`
+ `test_result_parser`
+ `generic_classifier_measurement`
+ `bgeresolve_icd10cm`
+ `bgeresolve_rxnorm`
+ `bgeresolve_snomed`
+ `bgeresolve_cpt`
+ `rxnorm_mapper`
+ `snomed_mapper`
+ `icd10cm_mapper`
+ `cpt_mapper`           



</div><div class="h3-box" markdown="1">

For all Healthcare NLP models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">


## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
