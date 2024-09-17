---
layout: model
title: Oncology Pipeline for Biomarkers
author: John Snow Labs
name: oncology_biomarker_pipeline
date: 2024-09-17
tags: [licensed, en, oncolgy, biomarker, pipeline, clinical]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This specialized oncology pipeline can;

- extract oncology biomarker type entities,

- assign assertion status to the extracted entities,

- establish relations between the extracted entities from the clinical documents.

In this pipeline, [ner_oncology](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_en.html), [ner_oncology_test](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_test_en.html), [ner_oncology_biomarker](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_biomarker_en.html), [ner_biomarker](https://nlp.johnsnowlabs.com/2021/11/26/ner_biomarker_en.html) and [cancer_diagnosis_matcher](https://nlp.johnsnowlabs.com/2024/06/17/cancer_diagnosis_matcher_en.html) NER models, 
[assertion_oncology](https://nlp.johnsnowlabs.com/2024/07/03/assertion_oncology_en.html) and [assertion_oncology_test_binary](https://nlp.johnsnowlabs.com/2024/07/03/assertion_oncology_test_binary_en.html) assertion models and [re_oncology_granular](https://nlp.johnsnowlabs.com/2024/07/03/re_oncology_granular_en.html)
and [re_oncology_biomarker_result](https://nlp.johnsnowlabs.com/2024/07/03/re_oncology_biomarker_result_en.html)  relation extraction models were used to achieve those tasks.

- Clinical Entity Labels: `Histological_Type`, `Direction`, `Staging`, `Cancer_Score`, `Imaging_Test`, `Cycle_Number`, `Tumor_Finding`, `Site_Lymph_Node`, `Invasion`, `Response_To_Treatment`, `Smoking_Status`, `Tumor_Size`, `Cycle_Count`, `Adenopathy`, `Age`, `Biomarker_Result`, `Unspecific_Therapy`, `Site_Breast`, `Chemotherapy`, `Targeted_Therapy`, `Radiotherapy`, `Performance_Status`, `Pathology_Test`, `Site_Other_Body_Part`, `Cancer_Surgery`, `Line_Of_Therapy`, `Pathology_Result`, `Hormonal_Therapy`, `Site_Bone`, `Biomarker`, `Immunotherapy`, `Cycle_Day`, `Frequency`, `Route`, `Duration`, `Death_Entity`, `Metastasis`, `Site_Liver`, `Cancer_Dx`, `Grade`, `Date`, `Site_Lung`, `Site_Brain`, `Relative_Date`, `Race_Ethnicity`, `Gender`, `Oncogene`, `Dosage`, `Radiation_Dose`, `Drug`, `CancerModifier`, `Radiological_Test_Result`, `Biomarker_Measurement`, `Radiological_Test`, `Test`, `Test_Result`, `Prognostic_Biomarkers`, `Predictive_Biomarkers`

- Assertion Status Labels: `Past`, `Family`, `Absent`, `Hypothetical`, `Possible`, `Present`, `Hypothetical_Or_Absent`, `Medical_History`

- Relation Extraction Labels: `is_related_to`, `is_size_of`, `is_date_of`, `is_location_of`, `is_finding_of`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/oncology_biomarker_pipeline_en_5.4.1_3.0_1726589469070.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/oncology_biomarker_pipeline_en_5.4.1_3.0_1726589469070.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("oncology_biomarker_pipeline", "en", "clinical/models")

result = pipeline.fullAnnotate("""Immunohistochemistry was negative for thyroid transcription factor-1 and napsin A. The test was positive for ER and PR,
and negative for HER2.""")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("oncology_biomarker_pipeline", "en", "clinical/models")

val result = pipeline.fullAnnotate("""Immunohistochemistry was negative for thyroid transcription factor-1 and napsin A. The test was positive for ER and PR,
and negative for HER2.""")
```
</div>

## Results

```bash
******************** ner_biomarker results ********************

| chunk                          |   begin |   end | ner_label             |   confidence |
|:-------------------------------|--------:|------:|:----------------------|-------------:|
| Immunohistochemistry           |       0 |    19 | Test                  |     0.9561   |
| negative                       |      25 |    32 | Biomarker_Measurement |     0.968    |
| thyroid transcription factor-1 |      38 |    67 | Biomarker             |     0.610925 |
| napsin A                       |      73 |    80 | Biomarker             |     0.8696   |
| positive                       |      96 |   103 | Biomarker_Measurement |     0.9228   |
| ER                             |     109 |   110 | Biomarker             |     0.9978   |
| PR                             |     116 |   117 | Biomarker             |     0.9932   |
| negative                       |     124 |   131 | Biomarker_Measurement |     0.9781   |
| HER2                           |     137 |   140 | Biomarker             |     0.7243   |


******************** assertion results ********************

| chunk                          | ner_label        | assertion   | assertion_source   |
|:-------------------------------|:-----------------|:------------|:-------------------|
| Immunohistochemistry           | Pathology_Test   | Past        | assertion_oncology |
| negative                       | Biomarker_Result | Past        | assertion_oncology |
| thyroid transcription factor-1 | Biomarker        | Present     | assertion_oncology |
| napsin A                       | Biomarker        | Present     | assertion_oncology |
| positive                       | Biomarker_Result | Present     | assertion_oncology |
| ER                             | Biomarker        | Present     | assertion_oncology |
| PR                             | Biomarker        | Present     | assertion_oncology |
| negative                       | Biomarker_Result | Present     | assertion_oncology |
| HER2                           | Oncogene         | Present     | assertion_oncology |


******************** re results ********************

| chunk1               | entity1          | chunk2                         | entity2          | relation      |
|:---------------------|:-----------------|:-------------------------------|:-----------------|:--------------|
| Immunohistochemistry | Pathology_Test   | negative                       | Biomarker_Result | O             |
| negative             | Biomarker_Result | thyroid transcription factor-1 | Biomarker        | is_related_to |
| negative             | Biomarker_Result | napsin A                       | Biomarker        | is_related_to |
| positive             | Biomarker_Result | ER                             | Biomarker        | is_related_to |
| positive             | Biomarker_Result | PR                             | Biomarker        | is_related_to |
| positive             | Biomarker_Result | HER2                           | Oncogene         | O             |
| ER                   | Biomarker        | negative                       | Biomarker_Result | O             |
| PR                   | Biomarker        | negative                       | Biomarker_Result | O             |
| negative             | Biomarker_Result | HER2                           | Oncogene         | is_related_to |
| Immunohistochemistry | Pathology_Test   | negative                       | Biomarker_Result | O             |
| negative             | Biomarker_Result | thyroid transcription factor-1 | Biomarker        | is_finding_of |
| negative             | Biomarker_Result | napsin A                       | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | ER                             | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | PR                             | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | HER2                           | Oncogene         | is_finding_of |
| ER                   | Biomarker        | negative                       | Biomarker_Result | O             |
| PR                   | Biomarker        | negative                       | Biomarker_Result | O             |
| negative             | Biomarker_Result | HER2                           | Oncogene         | is_finding_of |
| negative             | Biomarker_Result | thyroid transcription factor-1 | Biomarker        | is_finding_of |
| negative             | Biomarker_Result | napsin A                       | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | ER                             | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | PR                             | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | HER2                           | Oncogene         | O             |
| ER                   | Biomarker        | negative                       | Biomarker_Result | O             |
| PR                   | Biomarker        | negative                       | Biomarker_Result | O             |
| negative             | Biomarker_Result | HER2                           | Oncogene         | is_finding_of |



```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|oncology_biomarker_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- TextMatcherInternalModel
- ChunkMergeModel
- ChunkMergeModel
- AssertionDLModel
- ChunkFilterer
- AssertionDLModel
- AssertionMerger
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
- RelationExtractionModel
- AnnotationMerger