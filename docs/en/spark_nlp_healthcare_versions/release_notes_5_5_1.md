---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP v5.5.1 Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_5_5_1
key: docs-licensed-release-notes
modify_date: 2024-12-02
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.5.1

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release comes with brand new `PretrainedZeroShotNER`, `ContextualEntityRuler`, and `StructuredJsonConverter` annotators, 39 new and updated clinical pretrained models, and pipelines**.

+ Introducing a brand new `PretrainedZeroShotNER` annotator to extract named entities with no annotation or additional training, for any arbitrary label (coming with 12 zero shot models that are already finetuned on in-house annotations)
+ New `ContextualEntityRuler` annotator customizing named entities based on contextual rules (modifying chunks via inclusion and exclusion criteria)
+ New `StructuredJsonConverter` annotator for prettified annotation results and enhanced data processing (returning structured JSON outputs from Spark NLP pipelines)
+ Majority voting for overlapping annotations in `AssertionMerger` (picking the optimal assertion status coming from multiple models)
+ New rule-based contextual parser and entity matcher models to customize De-Identification pipelines
+ Introducing 5 new named entity recognition (NER) models and pipelines to detect German PHI data for deidentification with minimal customization
+ Introducing 2 new RxNorm resolution models for mapping the medication entities to RxNorm terminology, using SOTA `MedEmbed` sentence embeddings
+ Optimizing Spark Driver memory allocation to utilize all the available resources by default
+ `Databricks` support for `MedicalLLM` and `LLMLoader` to load/ run finetuned medical LLMs 
+ New blog posts on various topics
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
	- The `AnnotationLab` supports the `ssl_verification` parameter, allowing users to disable SSL certificate verification
	- Fixed entity filtering issue in `PipelineTracer` and it supports `PretrainedZeroShotNER` and `MedicalBertForTokenClassification`
  	- Fixed hanging issue when setting `setSelectMostDifferent(True)` in the `ChunkKeyPhraseExtraction` annotator by updating the algorithm at the behind
	- Updated faker output generation algorithm in `Deidentification` annotator by making it more sensitive for the "names"
	- `Deidentification` supports new faker labels such as "location_other" and "company" entities
	- Added new `setKeepMonth` parameter to `Deidentification` to allow month data keep intacted
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
    - New [Deidentification_Custom_Pretrained_Pipelines](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.7.Deidentification_Custom_Pretrained_Pipelines.ipynb)  Notebook
    - New [Contextual_Entity_Ruler](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/47.Contextual_Entity_Ruler.ipynb) Notebook
	- Updated [Contextual_Parser_Rule_Based_NER](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.2.Contextual_Parser_Rule_Based_NER.ipynb) Notebook
    - Updated [ZeroShot_Clinical_NER](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.6.ZeroShot_Clinical_NER.ipynb) Notebook
    - Updated [Rule_Based_Entity_Matchers](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.Rule_Based_Entity_Matchers.ipynb) Notebook
    - Updated [PipelineTracer_and_PipelineOutputParser](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.4.PipelineTracer_and_PipelineOutputParser.ipynb) Notebook
    - New [NER_GENE_PHENOTYPES](https://demo.johnsnowlabs.com/healthcare/NER_GENE_PHENOTYPES/) Demo
	- New [NER_VACCANIES](https://demo.johnsnowlabs.com/healthcare/NER_VACCANIES/) Demo
	- Updated [HCC_RISK_SCORE](https://demo.johnsnowlabs.com/healthcare/HCC_RISK_SCORE/) Demo
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.

</div><div class="h3-box" markdown="1">


#### `PretrainedZeroShotNER` Annotator to Extract Named Entities with No Annotation or Additional Training, for any Arbitrary Label.

Pretrained-Zero-Shot Named Entity Recognition (NER) enables the identification of entities in text with minimal effort. By leveraging pre-trained language models and contextual understanding, zero-shot NER extends entity recognition capabilities to new domains and languages.
While the model card includes default labels as examples, it is important to highlight that users are not limited to these labels. The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. For best results, it is recommended to use labels that are conceptually similar to the provided defaults.

{:.table-model-big}
| Model Name                                                            |      Description            |      Predicted Entites      |
|-----------------------------------------------------------------------|-----------------------------|-----------------------------|
| [`zeroshot_ner_generic_large`](https://nlp.johnsnowlabs.com/2024/11/28/zeroshot_ner_generic_large_en.html) | This model extracts generic entities | `AGE`, `DATE`, `DISEASE`, `DISORDER`, `DRUG`, `LOCATION`, `NAME`, `PHONE`, `RESULT`, `SYMPTOM`, `SYNDROME`, `TEST`, `TREATMENT` |
| [`zeroshot_ner_generic_medium`](https://nlp.johnsnowlabs.com/2024/11/28/zeroshot_ner_generic_medium_en.html)|This model extracts generic entities | `AGE`, `DATE`, `DISEASE`, `DISORDER`, `DRUG`, `LOCATION`, `NAME`, `PHONE`, `RESULT`, `SYMPTOM`, `SYNDROME`, `TEST`, `TREATMENT` |
| [`zeroshot_ner_clinical_large`](https://nlp.johnsnowlabs.com/2024/11/27/zeroshot_ner_clinical_large_en.html) | This model extracts clinical entities  | `PROBLEM`, `TREATMENT`, `TEST` |
| [`zeroshot_ner_clinical_medium`](https://nlp.johnsnowlabs.com/2024/11/27/zeroshot_ner_clinical_medium_en.html)|This model extracts clinical entities  | `PROBLEM`, `TREATMENT`, `TEST` |
| [`zeroshot_ner_deid_generic_docwise_large`](https://nlp.johnsnowlabs.com/2024/11/28/zeroshot_ner_deid_generic_docwise_large_en.html) | This model extracts demographic entities | `AGE`, `CONTACT`, `DATE`, `ID`, `LOCATION`, `NAME`, `PROFESSION` |
| [`zeroshot_ner_deid_generic_docwise_medium`](https://nlp.johnsnowlabs.com/2024/11/28/zeroshot_ner_deid_generic_docwise_medium_en.html)|This model extracts demographic entities | `AGE`, `CONTACT`, `DATE`, `ID`, `LOCATION`, `NAME`, `PROFESSION` |
| [`zeroshot_ner_oncology_large`](https://nlp.johnsnowlabs.com/2024/11/28/zeroshot_ner_oncology_large_en.html) | This model extracts oncological entities | `Adenopathy`, `Age`, `Biomarker`, `Biomarker_Result`, `Body_Part`, `Cancer_Dx`, `Cancer_Surgery`, `Cycle_Count`, `Cycle_Day`, `Date`, `Death_Entit`, `Directio`, `Dosage`, `Duration`, `Frequency`, `Gender`, `Grade`, `Histological_Type`, `Imaging_Test`, `Invasion`, `Metastasis`, `Oncogene`, `Pathology_Test`, `Race_Ethnicity`, `Radiation_Dose`, `Relative_Date`, `Response_To_Treatment`, `Route`, `Smoking_Status`, `Staging`, `Therapy`, `Tumor_Finding`, `Tumor_Size` |
| [`zeroshot_ner_oncology_medium`](https://nlp.johnsnowlabs.com/2024/11/27/zeroshot_ner_oncology_medium_en.html)|This model extracts oncological entities  | `Adenopathy`, `Age`, `Biomarker`, `Biomarker_Result`, `Body_Part`, `Cancer_Dx`, `Cancer_Surgery`, `Cycle_Count`, `Cycle_Day`, `Date`, `Death_Entit`, `Directio`, `Dosage`, `Duration`, `Frequency`, `Gender`, `Grade`, `Histological_Type`, `Imaging_Test`, `Invasion`, `Metastasis`, `Oncogene`, `Pathology_Test`, `Race_Ethnicity`, `Radiation_Dose`, `Relative_Date`, `Response_To_Treatment`, `Route`, `Smoking_Status`, `Staging`, `Therapy`, `Tumor_Finding`, `Tumor_Size` |
| [`zeroshot_ner_vop_medium`](https://nlp.johnsnowlabs.com/2024/11/29/zeroshot_ner_vop_medium_en.html)|This model extracts Voice of the Patients (VOP) entities  |`AdmissionDischarge`, `Age`, `Allergen`, `BodyPart`, `ClinicalDept`, `DateTime`, `Disease`, `Dosage`, `Drug`, `Duration`, `Employment`, `Form`, `Frequency`, `Gender`, `Laterality`, `MedicalDevice`,`Modifier`, `Procedure`, `PsychologicalCondition`, `RaceEthnicity`, `Substance`, `Symptom`, `Test`, `Treatment`, `Vaccine`|
| [`zeroshot_ner_vop_large`](https://nlp.johnsnowlabs.com/2024/11/30/zeroshot_ner_vop_large_en.html)|This model extracts Voice of the Patients (VOP) entities  |`AdmissionDischarge`, `Age`, `Allergen`, `BodyPart`, `ClinicalDept`, `DateTime`, `Disease`, `Dosage`, `Drug`, `Duration`, `Employment`, `Form`, `Frequency`, `Gender`, `Laterality`, `MedicalDevice`,`Modifier`, `Procedure`, `PsychologicalCondition`, `RaceEthnicity`, `Substance`, `Symptom`, `Test`, `Treatment`, `Vaccine`|

*Example*:

```python
# You can change the labels
labels = ['DOCTOR', 'PATIENT', 'AGE', 'DATE', 'HOSPITAL', 'CITY', 'STREET', 'STATE', 'COUNTRY', 'PHONE', 'IDNUM', 'EMAIL', 'ZIP', 'ORGANIZATION', 'PROFESSION', 'USERNAME']

pretrained_zero_shot_ner = sparknlp_jsl.annotator.PretrainedZeroShotNER()\
    .pretrained("zeroshot_ner_deid_subentity_merged_medium", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("ner")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)

text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890. The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 .
Dr. John Taylor, ID: 982345, a cardiologist at St. Mary's Hospital in Boston, was contacted on 05/10/2023 regarding a 45-year-old.
"""
```

*Result*:

{:.table-model-big}
|chunk               |begin|end|ner_label |
|--------------------|-----|---|----------|
|John Lee            |4    |11 |DOCTOR    |
|Royal Medical Clinic|19   |38 |HOSPITAL  |
|Chicago             |43   |49 |CITY      |
|11/05/2024          |80   |89 |DATE      |
|56467890            |131  |138|IDNUM     |
|Emma Wilson         |154  |164|PATIENT   |
|50                  |170  |171|AGE       |
|444-456-7890        |205  |216|PHONE     |
|John Taylor         |224  |234|DOCTOR    |
|982345              |241  |246|IDNUM     |
|cardiologist        |251  |262|PROFESSION|
|St. Mary's Hospital |267  |285|HOSPITAL  |
|Boston              |290  |295|CITY      |
|05/10/2023          |315  |324|DATE      |
|45-year-old         |338  |348|AGE       |



*Example for Changing the Labels*:

```python
# You can change the labels. If we can group them such as DOCTOR -> NAME, PATIENT -> NAME ...
labels = ['NAME', 'AGE', 'DATE', 'LOCATION', 'IDNUM',' ORGANIZATION', 'PROFESSION']

pretrained_zero_shot_ner = sparknlp_jsl.annotator.PretrainedZeroShotNER()\
    .pretrained("zeroshot_ner_deid_subentity_merged_medium", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("ner")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)
```

*Result*:

{:.table-model-big}
|chunk               |begin|end|ner_label   |
|--------------------|-----|---|------------|
|John Lee            |4    |11 |NAME        |
|Royal Medical Clinic|19   |38 |ORGANIZATION|
|Chicago             |43   |49 |LOCATION    |
|11/05/2024          |80   |89 |DATE        |
|56467890            |131  |138|IDNUM       |
|Emma Wilson         |154  |164|NAME        |
|50                  |170  |171|AGE         |
|444-456-7890        |205  |216|IDNUM       |
|John Taylor         |224  |234|NAME        |
|982345              |241  |246|IDNUM       |
|cardiologist        |251  |262|PROFESSION  |
|St. Mary's Hospital |267  |285|ORGANIZATION|
|Boston              |290  |295|LOCATION    |
|05/10/2023          |315  |324|DATE        |
|45-year-old         |338  |348|AGE         |

Please check the [ZeroShot Clinical NER](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.6.ZeroShot_Clinical_NER.ipynb) Notebook for more information


</div><div class="h3-box" markdown="1">

#### `ContextualEntityRuler` Annotator Customizing Named Entities Based on Contextual Rules (Modifying Chunks via Inclusion and Exclusion Criteria).

`ContextualEntityRuler` is an annotator that updates chunks based on contextual rules. These rules are defined in the form of dictionaries and can include prefixes, suffixes, and the context within a specified scope window around the chunk.

This annotator modifies detected chunks by replacing content based on matching patterns and rules. It is particularly useful for refining entity recognition results in domain-specific text processing.

*Example*:

```python
rules = [
	{
		"entity" : "Age",
		"scopeWindow" : [15,15],
		"scopeWindowLevel"  : "char",
		"suffixPatterns" : ["years old", "year old", "months",],
		"replaceEntity" : "Modified_Age",
		"mode" : "exclude"
	},
	{
		"entity" : "Diabetes",
		"scopeWindow" : [3,3],
		"scopeWindowLevel"  : "token",
		"suffixPatterns" : ["with complications"],
		"replaceEntity" : "Modified_Diabetes",
		"mode" : "include"
	},
	{
		"entity" : "Date",
		"suffixRegexes" : ["\\d{4}"],
		"replaceEntity" : "Modified_Date",
		"mode" : "include"
	},
	{
		"entity" : "Name",
		"scopeWindow" : [3,3],
		"scopeWindowLevel"  : "token",
		"prefixPatterns" : ["MD","M.D"],
		"replaceEntity" : "Modified_Name",
		"mode" : "include"
	}   
]

contextual_entity_ruler = ContextualEntityRuler() \
    .setInputCols("sentence", "token", "ner_chunks") \
    .setOutputCol("ruled_ner_chunks") \
    .setRules(rules) \
    .setCaseSensitive(False)\
    .setDropEmptyChunks(True)\
    .setAllowPunctuationInBetween(True)

text = """ M.D John Snow assessed the 36 years old who has a history of the diabetes mellitus with complications in May, 2006"""
data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```

*NER Result*:

{:.table-model-big}

| entity      | begin | end  | ruled_ner_chunks_result  |
|-------------|-------|------|--------------------------|
| Name        | 5     | 13   | John Snow                |
| Age         | 28    | 39   | 36 years old             |
| Diabetes    | 66    | 82   | diabetes mellitus        |
| Date        | 106   | 108  | May                      |
| Date        | 111   | 114  | 2006                     |



*Result for after ContextualEntityRuler*:

{:.table-model-big}
| entity            | begin | end  | ruled_ner_chunks_result                 |  description   |
|-------------------|-------|------|-----------------------------------------|---------------------|
| Modified_Name     | 1     | 13   | M.D John Snow                           | `M.D` included	      |
| Modified_Age      | 28    | 29   | 36                                      |  `years old` excluded  |
| Modified_Diabetes | 66    | 101  | diabetes mellitus with complications    |`with complications` included |
| Modified_Date     | 106   | 114  | May, 2006                               | `2006` included |

Please check the [Contextual_Entity_Ruler](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/47.Contextual_Entity_Ruler.ipynb) Notebook for more information


</div><div class="h3-box" markdown="1">

#### `StructuredJsonConverter` Annotator for Prettified Annotation Results and Enhanced Data Processing (Returning Structured JSON Outputs from Spark NLP Pipelines)

This annotator integrates seamlessly with existing frameworks to process outputs from pretrained pipelines, delivering structured, easy-to-read results in a dictionary format. Optimized for API integration and user-friendly outputs, it supports streamlined data analysis workflows by converting raw annotations into a prettified, structured JSON format. With configurable schema mappings, it accommodates diverse outputs, including entities, assertions, resolutions, relations, summaries, deidentifications, and classifications. It uses column_maps to define output columns and align them with pipeline requirements. It handles diverse annotation types, including entities, assertions, resolutions, relations, summaries, deidentifications, and classifications. It produces well-structured, easy-to-read results ideal for API consumption and streamlined workflows.


*Example*:

```python
biomarker_pipeline = PretrainedPipeline("explain_clinical_doc_biomarker", "en", "clinical/models")

text = """In the bone- marrow (BM) aspiration, blasts accounted for 88.1% of ANCs, which were positive for CD9 and CD10 on flow cytometry.
      Measurements of serum tumor markers showed elevated level of Cyfra21-1: 4.77 ng/mL, NSE: 19.60 ng/mL, and SCCA: 2.58 ng/mL.
      Immunohistochemical staining showed positive staining for CK5/6, P40, and negative staining for TTF-1 and weakly positive staining for ALK
"""

data = spark.createDataFrame([text], T.StringType()).toDF("text")

result_df = biomarker_pipeline.transform(data)

column_maps = {
    'document_identifier': '',
    'document_text': 'document',
    'entities': ['merged_chunk'],
    'assertions': [],
    'resolutions': [],
    'relations': ['re_oncology_biomarker_result_wip'],
    'summaries': [],
    'deidentifications': [],
    'classifications': [{
        'classification_column_name': 'prediction',
        'sentence_column_name': 'sentence'
      }]
}

output_converter = StructuredJsonConverter()\
            .setOutputCol("result")\
            .setConverterSchema(column_maps)\
            .setCleanAnnotations(False)\
            .setReturnRelationEntities(True)

json_output = output_converter.transform(result_df).select("result")
json_output.show(truncate=200)
```

*Result*:

```bash
{
    "document_identifier": "529c4f43-ea61-4e81-a0b1-3cdb87627cc2",
    "document_text": ['In the bone- marrow (BM) aspiration, blasts accounted for 88.1% of ANCs, which were positive for CD9 and CD10 on flow cytometry. \n      Measurements of serum tumor markers showed elevated level of Cyfra21-1: 4.77 ng/mL, NSE: 19.60 ng/mL, and SCCA: 2.58 ng/mL. \n      Immunohistochemical staining showed positive staining for CK5/6, P40, and negative staining for TTF-1 and weakly positive staining for ALK.'
    ],
    "entities": [
        {'ner_label': 'Biomarker_Result', 'sentence': '0', 'chunk': 'positive', 'end': '91', 'ner_source': 'ner_oncology_chunk', 'ner_confidence': '0.9672', 'begin': '84', 'chunk_id': 'bc15add6'},
        {'ner_label': 'Biomarker', 'sentence': '0', 'chunk': 'CD9', 'end': '99', 'ner_source': 'ner_oncology_chunk', 'ner_confidence': '0.992', 'begin': '97', 'chunk_id': 'b473fd80'},
        {'ner_label': 'Biomarker', 'sentence': '0', 'chunk': 'CD10', 'end': '108', 'ner_source': 'ner_oncology_chunk', 'ner_confidence': '0.9987', 'begin': '105', 'chunk_id': '0252d08a'},
        {'ner_label': 'Biomarker', 'sentence': '1', 'chunk': 'tumor markers', 'end': '170', 'ner_source': 'ner_oncology_chunk', 'ner_confidence': '0.48290002', 'begin': '158', 'chunk_id': 'ddab7cc4'},
        {'ner_label': 'Biomarker_Result', 'sentence': '1', 'chunk': 'elevated level', 'end': '192', 'ner_source': 'ner_oncology_chunk', 'ner_confidence': '0.90779996', 'begin': '179', 'chunk_id': 'a9c78d75'},
        ...
    ],
    "assertions": [],
    "resolutions": [],
    "relations": [
        {'entity1_begin': '84', 'chunk1': 'positive', 'chunk2': 'CD9', 'entity2_begin': '97', 'confidence': '0.9944541', 'entity2_end': '99', 'chunk1_id': 'bc15add6', 'chunk2_id': 'b473fd80', 'relation': 'is_finding_of', 'entity1': 'Biomarker_Result', 'entity2': 'Biomarker', 'entity1_end': '91', 'direction': 'both'},
        {'entity1_begin': '84', 'chunk1': 'positive', 'chunk2': 'CD10', 'entity2_begin': '105', 'confidence': '0.9989317', 'entity2_end': '108', 'chunk1_id': 'bc15add6', 'chunk2_id': '0252d08a', 'relation': 'is_finding_of', 'entity1': 'Biomarker_Result', 'entity2': 'Biomarker', 'entity1_end': '91', 'direction': 'both'},
        {'entity1_begin': '158', 'chunk1': 'tumor markers', 'chunk2': 'elevated level', 'entity2_begin': '179', 'confidence': '0.8983218', 'entity2_end': '192', 'chunk1_id': 'ddab7cc4', 'chunk2_id': 'a9c78d75', 'relation': 'is_finding_of', 'entity1': 'Biomarker', 'entity2': 'Biomarker_Result', 'entity1_end': '170', 'direction': 'both'},
        ...
    ],
    "summaries": [],
    "deidentifications": [],
    "classifications": [
        {'classification': '1', 'sentence': 'In the bone- marrow (BM) aspiration, blasts accounted for 88.1% of ANCs, which were positive for CD9 and CD10 on flow cytometry.', 'sentence_id': '0'},
        {'classification': '1', 'sentence': 'Measurements of serum tumor markers showed elevated level of Cyfra21-1: 4.77 ng/mL, NSE: 19.60 ng/mL, and SCCA: 2.58 ng/mL.', 'sentence_id': '1'},
        {'classification': '1', 'sentence': 'Immunohistochemical staining showed positive staining for CK5/6, P40, and negative staining for TTF-1 and weakly positive staining for ALK.', 'sentence_id': '2'}
    ]
}
```

Please check the [PipelineTracer and PipelineOutputParser](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.4.PipelineTracer_and_PipelineOutputParser.ipynb) Notebook for more information



</div><div class="h3-box" markdown="1">

#### Majority Voting for Overlapping Annotations in `AssertionMerger` (Picking the Optimal Assertion Status Coming from Multiple Models)

When there are multiple annotations in the same overlapping group, **majority voting** is used to resolve conflicts. This method helps determine the final selected annotation based on the most frequent or strongest assertion.

- If **confidence** is specified as an ordering feature, then the **sum of confidence scores** for each assertion type is used for majority voting. The assertion type with the highest total confidence score is selected.

*Example-1*:

In a pipeline consisting of `AssertionDL`, `FewShotAssertion`, and `ContextualAssertion` models:

{:.table-model-big}
| Model                  | Assertion Type | Confidence Score |
|------------------------|----------------|------------------|
| FewShotAssertion       | `possible`     | 0.90             |
| AssertionDL            | `present`      | 0.85             |
| ContextualAssertion    | `present`      | 0.80             |

- Here, **confidence** is used as an ordering feature.
- Total confidence score for `present` = `0.85 + 0.80 = 1.65`.
- Total confidence score for `possible` = `0.90`.
- Since the total confidence score for `present` is higher, the selected annotation is **`present`**.

*Example-2*:

{:.table-model-big}
| Model                  | Assertion Type | Confidence Score |
|------------------------|----------------|------------------|
| FewShotAssertion       | `possible`     | 0.90             |
| AssertionDL            | `present`      | 0.30             |
| ContextualAssertion    | `present`      | 0.50             |

- Total confidence score for `present` = `0.30 + 0.50 = 0.80`.
- Total confidence score for `possible` = `0.90`.
- Since the total confidence score for `possible` is higher, the selected annotation is **`possible`**.

*Example*:

```python
assertion_merger = AssertionMerger() \
    .setInputCols(["assertion_dl","assertion_jsl", "assertion_fewshot"]) \
    .setOutputCol("assertion_merger")\
    .setMergeOverlapping(True)\
    .setMajorityVoting(True)\
    .setOrderingFeatures(["confidence"])

text ="""Intramuscular as well as intravenous Haldol were ordered p.r.n. for emergency use should he become acutely agitated."""
```

*assertion_dl Result*:

{:.table-model-big}
|ner_chunk        |begin|end|ner_label|assertion_dl|confidence_assertion_dl|
|-----------------|-----|---|---------|------------|-----------------------|
|he               |402  |403|Gender   |Hypothetical|0.947                  |
|acutely agitated |412  |427|PROBLEM  |Hypothetical|0.974                  |

*assertion_jsl Result*:

{:.table-model-big}
|ner_chunk        |begin|end|ner_label|assertion_jsl|confidence_assertion_jsl|
|-----------------|-----|---|---------|-------------|------------------------|
|he               |402  |403|Gender   |Family       |1.0                     |
|acutely agitated |412  |427|PROBLEM  |Family       |1.0                     |

*assertion_fewshot Result*:

{:.table-model-big}
|ner_chunk        |begin|end|ner_label|assertion_fewshot|confidence_assertion_fewshot|
|-----------------|-----|---|---------|-----------------|----------------------------|
|he               |402  |403|Gender   |Family           |0.887                  |
|acutely agitated |412  |427|PROBLEM  |Hypothetical     |0.887                  |

*Merged Result*:

{:.table-model-big}
|ner_chunk        |begin|end|ner_label|assertion   |assertion_source |merge_confidence|
|-----------------|-----|---|---------|------------|-----------------|----------------|
|he               |402  |403|Gender   |Family      |assertion_jsl    |1.0             |
|acutely agitated |412  |427|PROBLEM  |Hypothetical|assertion_dl     |0.974           |



</div><div class="h3-box" markdown="1">

####  New Rule-Based Contextual Parser and Entity Matcher Models to Customise De-IDentification Pipelines

We introduce a suite of text, contextual parser models, and entity matchers, specifically designed to enhance the deidentification and clinical document understanding process with rule-based methods.

{:.table-model-big}
| Model Name                               |      Description            |
|------------------------------------------|-----------------------------|
| [`account_parser`](https://nlp.johnsnowlabs.com/2024/10/23/account_parser_en.html) | This model extracts account number entities in clinical notes using a rule-based `ContextualParserModel` annotator. |
| [`age_parser`](https://nlp.johnsnowlabs.com/2024/10/23/age_parser_en.html) | This model extracts age entities in clinical notes using a rule-based `ContextualParserModel` annotator. |
| [`country_matcher`](https://nlp.johnsnowlabs.com/2024/10/23/country_matcher_en.html) | This model extracts countries in clinical notes using rule-based `TextMatcherInternal` annotator. |
| [`date_matcher`](https://nlp.johnsnowlabs.com/2024/10/23/date_matcher_en.html) | This model extracts date entities in clinical notes using a rule-based `RegexMatcherInternal` annotator. |
| [`dln_parser`](https://nlp.johnsnowlabs.com/2024/10/23/dln_parser_en.html) | This model extracts drive license number entities in clinical notes using a rule-based `ContextualParserModel` annotator. |
| [`license_parser`](https://nlp.johnsnowlabs.com/2024/10/23/license_parser_en.html) | This model extracts license number entities in clinical notes using a rule-based `ContextualParserModel` annotator. |
| [`medical_record_parser`](https://nlp.johnsnowlabs.com/2024/10/23/medical_record_parser_en.html) | This model extracts medical record entities in clinical notes using a rule-based `ContextualParserModel` annotator. |
| [`phone_parser`](https://nlp.johnsnowlabs.com/2024/10/23/phone_parser_en.html) | This model extracts phone entities in clinical notes using a rule-based `ContextualParserModel` annotator. |
| [`plate_parser`](https://nlp.johnsnowlabs.com/2024/10/23/plate_parser_en.html) | This model extracts plate number entities in clinical notes using a rule-based `ContextualParserModel` annotator. |
| [`ssn_parser`](https://nlp.johnsnowlabs.com/2024/10/23/ssn_parser_en.html) | This model extracts SSN number entities in clinical notes using a rule-based `ContextualParserModel` annotator. |
| [`vin_parser`](https://nlp.johnsnowlabs.com/2024/10/23/vin_parser_en.html) | This model extracts vehicle identifier number entities in clinical notes using a rule-based `ContextualParserModel` annotator. |


*Example*:

```python
account_contextual_parser = ContextualParserModel.pretrained("account_parser","en","clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("chunk_account")

chunk_converter = ChunkConverter() \
    .setInputCols(["chunk_account"]) \
    .setOutputCol("ner_chunk")

sample_text = """Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13. account: 1234567890120 route number: 123567
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""
```

*Result*:

{:.table-model-big}
|        chunk|begin|end|  label|
|-------------|-----|---|-------|
|1234567890120|  120|132|ACCOUNT|
|       123567|  148|153|ACCOUNT|


Please check the [Rule Based Entity Matchers](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.Rule_Based_Entity_Matchers.ipynb) Notebook for more information


</div><div class="h3-box" markdown="1">

#### Introducing 5 New Named Entity Recognition (NER) Models and Pipeline to Detect German PHI Data for Deidentification with Minimal Customization

Introducing 5 New Named Entity Recognition (NER) Models: `ner_deid_generic_docwise`, `ner_deid_subentity_langtest`, `zeroshot_ner_deid_generic_docwise_large`,  `clinical_deidentification_docwise_wip`, and `clinical_deidentification_docwise_large_wip`. These models work at the document level and are particularly useful for detecting Protected Health Information (PHI) for de-identification in German.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`ner_deid_generic_docwise_de`](https://nlp.johnsnowlabs.com/2024/10/24/ner_deid_generic_docwise_de.html) | This document-level model detects PHI entities for de-identification. (Generic) |
| [`zeroshot_ner_deid_generic_docwise_large_de`](https://nlp.johnsnowlabs.com/2024/11/28/zeroshot_ner_deid_generic_docwise_large_de.html) | This document-level zero-shot NER model detects PHI entities for de-identification. (Generic) |
| [`ner_deid_subentity_langtest_de`](https://nlp.johnsnowlabs.com/2024/10/24/ner_deid_subentity_langtest_de.html) | This langtest model detects PHI entities for de-identification. (Subentity - Langtest) |
| [`clinical_deidentification_docwise_wip_de`](https://nlp.johnsnowlabs.com/2024/11/29/clinical_deidentification_docwise_wip_de.html) | This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. The pipeline can mask and obfuscate: `LOCATION`, `DATE`, `NAME`, `ID`, `AGE`, `PROFESSION`, `CONTACT`, `ORGANIZATION`, `DOCTOR`, `CITY`, `COUNTRY`, `STREET`, `PATIENT`, `PHONE`, `HOSPITAL`, `STATE`, `DLN`, `SSN`, `ZIP`, `ACCOUNT`, `LICENSE`, `PLATE`, `VIN`, `MEDICALRECORD`, `EXCLUDED`, `EMAIL`, `URL` entities. |
| [`clinical_deidentification_docwise_large_wip_de`](https://nlp.johnsnowlabs.com/2024/11/29/clinical_deidentification_docwise_large_wip_de.html) | This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. The pipeline can mask and obfuscate: `LOCATION`, `DATE`, `NAME`, `ID`, `AGE`, `PROFESSION`, `CONTACT`, `ORGANIZATION`, `DOCTOR`, `CITY`, `COUNTRY`, `STREET`, `PATIENT`, `PHONE`, `HOSPITAL`, `STATE`, `DLN`, `SSN`, `ZIP`, `ACCOUNT`, `LICENSE`, `PLATE`, `VIN`, `MEDICALRECORD`, `EXCLUDED`, `EMAIL`, `URL` entities. |

*Example*:

```python
deid_ner = MedicalNerModel.pretrained("ner_deid_generic_docwise", "de", "clinical/models")\
    .setInputCols(["document", "token", "embeddings"])\
    .setOutputCol("ner")

data = spark.createDataFrame([["""Michael Berger wird am Morgen des 12 Dezember 2018 ins St. Elisabeth-Krankenhaus
in Bad Kissingen eingeliefert. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen."""]]).toDF("text")
```

*Result*:

{:.table-model-big}
|chunk                    |begin|end|ner_label|
|-------------------------|-----|---|---------|
|Michael Berger           |0    |13 |NAME     |
|12 Dezember 2018         |34   |49 |DATE     |
|St. Elisabeth-Krankenhaus|55   |79 |LOCATION |
|Bad Kissingen            |84   |96 |LOCATION |
|Herr Berger              |112  |122|NAME     |
|76                       |128  |129|AGE      |



</div><div class="h3-box" markdown="1">

#### Introducing 2 new RxNorm Resolution Models for Mapping the Medication Entities to RxNorm Terminology, Using SOTA `MedEmbed` Sentence Embeddings

The latest lineup of 3 cutting-edge resolver models are designed to enhance clinical entity mapping and coding accuracy. These models leverage advanced natural language processing to seamlessly map medical entities and concepts to standardized codes, facilitating streamlined data analysis and healthcare decision-making.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`medembed_base_rxnorm_augmented`](https://nlp.johnsnowlabs.com/2024/11/19/medembed_base_rxnorm_augmented_en.html) | This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes|
| [`medmebed_large_rxnorm_augmented`](https://nlp.johnsnowlabs.com/2024/11/19/medmebed_large_rxnorm_augmented_en.html) | This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes |
| [`biolordresolve_loinc_augmented`](https://nlp.johnsnowlabs.com/2024/10/08/biolordresolve_loinc_augmented_en.html) | This model maps medical entities to Logical Observation Identifiers Names and Codes(LOINC) codes using `mpnet_embeddings_biolord_2023_c` embeddings. |


*Example*:

```python
rxnorm_resolver = SentenceEntityResolverModel.pretrained("medmebed_large_rxnorm_augmented", "en", "clinical/models")\
    .setInputCols(["embeddings"])\
    .setOutputCol("rxnorm_code")\
    .setDistanceFunction("EUCLIDEAN")

text = "The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. He was seen by the endocrinology service and she was discharged on Coumadin 5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily"
```

*Result*:

{:.table-model-big}

| ner_chunk         | entity | rxnorm_code | all_k_resolutions                                                                         |
|-------------------|--------|-------------|-------------------------------------------------------------------------------------------|
| aspirin           | DRUG   | 1191        | aspirin[aspirin]:::Empirin[Empirin]:::aluminum aspirin[aluminum aspirin]:::...            |
| Albuterol inhaler | DRUG   | 1649559     | albuterol Dry Powder Inhaler[albuterol Dry Powder Inhaler]:::albuterol[albuterol]:::...   |
| Coumadin 5 mg     | DRUG   | 855333      | warfarin sodium 5 MG [Coumadin]:::warfarin sodium 7.5 MG [Coumadin]:::...                 |
| metformin 1000 mg | DRUG   | 316255      | metformin 1000 MG[metformin 1000 MG]:::metformin hydrochloride 1000 MG[metformin...]      |
| Lisinopril 10 mg  | DRUG   | 316151      | lisinopril 10 MG[lisinopril 10 MG]:::lisinopril 10 MG Oral Tablet:::...                   |


</div><div class="h3-box" markdown="1">

#### `Databricks` Support for `MedicalLLM` and `LLMLoader` to Load/Run Finetuned Medical LLMs 

Enables seamless support for MedicalLLM and LLMLoader on Databricks, facilitating the deployment and management of medical-focused large language models. This integration streamlines data preprocessing, model training, and inference workflows, providing an efficient platform for developing advanced medical AI solutions. PS: Some models may not be supported yet.


</div><div class="h3-box" markdown="1">

#### Optimizing Spark Driver Memory Allocation to Utilize all the Available Resources by Default.

The Spark driver is optimized to utilize 100% of available system memory for `spark.driver.memory` by default. If this allocation isn't viable due to system constraints, Spark automatically reverts to a default memory allocation of 32GB, ensuring stability and adaptability in resource-limited environments.

</div><div class="h3-box" markdown="1">


#### New Blog Posts On Various Topics

Explore the latest developments in healthcare NLP through our new blog posts, where we take a deep dive into the innovative technologies and methodologies transforming the medical field. These posts offer insights into the transformative impact of NLP technologies in healthcare, showcasing how they streamline processes, improve patient outcomes, and pave the way for future innovations in medical research and practice.

- [From Data Overload to Precision: How Medical Language Models Enhance Clinical Trials](https://gursev-pirge.medium.com/46efda119aab): This blog post explores how John Snow Labs’ Healthcare NLP & LLM library is transforming clinical trials by using advanced NER models to efficiently filter through large datasets of patient records. By automatically extracting cancer-related information from unstructured clinical notes, the solution enables researchers to quickly identify patients with specific cancer indications, accelerating trial enrollment and ensuring more accurate patient selection.
- [The Power of Small LLMs in Healthcare: A RAG Framework Alternative to Large Language Models](https://www.johnsnowlabs.com/the-power-of-small-llms-in-healthcare-a-rag-framework-alternative-to-large-language-models/) This blog post explores the potential of smaller, fine-tuned language models like JSL’s Retrieval-Augmented Generation (RAG) models (e.g., jsl_med_rag_v1) to deliver performance comparable to larger LLMs in specialized clinical tasks such as question answering and medical summarization. This blog post provides an in-depth look at these efficient models, demonstrating their high relevance and effectiveness in a RAG framework while challenging the dominance of larger general-purpose models like GPT-4.
- [From Data Overload to Precision: How Medical Language Models Enhance Clinical Trials](https://medium.com/john-snow-labs/from-data-overload-to-precision-how-medical-language-models-enhance-clinical-trials-46efda119aab): This blog post explores how John Snow Labs’ Healthcare NLP & LLM library is transforming clinical trials by using advanced NER models to efficiently filter through large datasets of patient records. By automatically extracting cancer-related information from unstructured clinical notes, the solution enables researchers to quickly identify patients with specific cancer indications, accelerating trial enrollment and ensuring more accurate patient selection.

</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, and Reliability of Spark NLP for Healthcare

- The `AnnotationLab` supports the `ssl_verification` parameter, allowing users to disable SSL certificate verification
- Fixed entity filtering issue in `PipelineTracer` and it supports `PretrainedZeroShotNER` and `MedicalBertForTokenClassification`
- Fixed hanging issue when setting `setSelectMostDifferent(True)` in the `ChunkKeyPhraseExtraction` annotator by updating the algorithm at the behind
- `Deidentification` changed the faker generation algorithm and it is more sensitive for the "names"
- `Deidentification` supports new faker labels such as "location_other" and "company"
- Added new `keepMonth` parameter to `Deidentification`
- Added new end-to-end `RelationalDBDeidentification` into utils


</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [Deidentification_Custom_Pretrained_Pipelines](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.7.Deidentification_Custom_Pretrained_Pipelines.ipynb)  Notebook
- New [Contextual_Entity_Ruler](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/47.Contextual_Entity_Ruler.ipynb) Notebook
- Updated [Contextual_Parser_Rule_Based_NER](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.2.Contextual_Parser_Rule_Based_NER.ipynb) Notebook
- Updated [ZeroShot_Clinical_NER](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.6.ZeroShot_Clinical_NER.ipynb) Notebook
- Updated [Rule_Based_Entity_Matchers](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.Rule_Based_Entity_Matchers.ipynb) Notebook
- Updated [PipelineTracer_and_PipelineOutputParser](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.4.PipelineTracer_and_PipelineOutputParser.ipynb) Notebook
- New [NER_GENE_PHENOTYPES](https://demo.johnsnowlabs.com/healthcare/NER_GENE_PHENOTYPES/) Demo
- New [NER_VACCANIES](https://demo.johnsnowlabs.com/healthcare/NER_VACCANIES/) Demo
- Updated [HCC_RISK_SCORE](https://demo.johnsnowlabs.com/healthcare/HCC_RISK_SCORE/) Demo


</div><div class="h3-box" markdown="1">

#### We have added and updated a substantial number of new clinical models and pipelines, further solidifying our offering in the healthcare domain.


+ `zeroshot_ner_generic_large`
+ `zeroshot_ner_generic_medium`
+ `zeroshot_ner_clinical_large`
+ `zeroshot_ner_clinical_medium`
+ `zeroshot_ner_oncology_large`
+ `zeroshot_ner_oncology_medium`
+ `zeroshot_ner_deid_generic_docwise_large`
+ `zeroshot_ner_deid_generic_docwise_medium`
+ `zeroshot_ner_deid_subentity_docwise_large`
+ `zeroshot_ner_deid_subentity_docwise_medium`
+ `zeroshot_ner_vop_medium`
+ `zeroshot_ner_vop_large`
+ `sbiobertresolve_loinc_numeric_augmented`            
+ `loinc_numeric_resolver_pipeline`             
+ `loinc_resolver_pipeline`  
+ `biolordresolve_loinc_augmented`
+ `account_parser`
+ `age_parser`
+ `country_matcher`
+ `date_matcher`
+ `dln_parser`
+ `license_parser`
+ `medical_record_parser`
+ `phone_parser`
+ `plate_parser`
+ `ssn_parser`
+ `vin_parser`
+ `clinical_deidentification_docwise_wip`
+ `clinical_deidentification_docwise_wip_v2`
+ `clinical_deidentification_v2_wip`
+ `ner_deid_generic_docwise` -> `de`
+ `zeroshot_ner_deid_generic_docwise_large` -> `de`
+ `clinical_deidentification_docwise_large_wip` -> `de`
+ `clinical_deidentification_docwise_wip` -> `de`
+ `ner_deid_subentity_langtest` -> `de`
+ `drug_action_treatment_mapper`
+ `medembed_base_rxnorm_augmented`
+ `medmebed_large_rxnorm_augmented`
+ `snomed_term_resolver_pipeline`

</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">




## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
