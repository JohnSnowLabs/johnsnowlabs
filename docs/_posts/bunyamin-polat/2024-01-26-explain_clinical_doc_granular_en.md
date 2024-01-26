---
layout: model
title: Explain Clinical Document - Granular
author: John Snow Labs
name: explain_clinical_doc_granular
date: 2024-01-26
tags: [licensed, en, entity_resolution, relation_extraction, assertion_status, clinical, pipeline, granular]
task: [Entity Resolution, Relation Extraction, Assertion Status, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to:

- extract clinical entities
- assign assertion status to the extracted entities
- establish relations between the extracted entities

from clinical texts. In this pipeline, [ner_jsl](https://nlp.johnsnowlabs.com/2022/10/19/ner_jsl_en.html) NER model, [assertion_jsl](https://nlp.johnsnowlabs.com/2021/07/24/assertion_jsl_en.html) assertion model, and [re_test_result_date](https://nlp.johnsnowlabs.com/2021/02/24/re_test_result_date_en.html) relation extraction model were used to achieve those tasks. Here are the NER, assertion, and relation extraction labels this pipeline can extract.

- Clinical Entity Labels: `Admission_Discharge`, `Age`, `Alcohol`, `Allergen`, `BMI`, `Birth_Entity`, `Blood_Pressure`, `Cerebrovascular_Disease`, `Clinical_Dept`, `Communicable_Disease`, `Date`, `Death_Entity`, `Diabetes`, `Diet`, `Direction`, `Disease_Syndrome_Disorder`, `Dosage`, `Drug_BrandName`, `Drug_Ingredient`, `Duration`, `EKG_Findings`, `Employment`, `External_body_part_or_region`, `Family_History_Header`, `Fetus_NewBorn`, `Form`, `Frequency`, `Gender`, `HDL`, `Heart_Disease`, `Height`, `Hyperlipidemia`, `Hypertension`, `ImagingFindings`, `Imaging_Technique`, `Injury_or_Poisoning`, `Internal_organ_or_component`, `Kidney_Disease`, `LDL`, `Labour_Delivery`, `Medical_Device`, `Medical_History_Header`, `Modifier`, `O2_Saturation`, `Obesity`, `Oncological`, `Overweight`, `Oxygen_Therapy`, `Pregnancy`, `Procedure`, `Psychological_Condition`, `Pulse`, `Race_Ethnicity`, `Relationship_Status`, `RelativeDate`, `RelativeTime`, `Respiration`, `Route`, `Section_Header`, `Sexually_Active_or_Sexual_Orientation`, `Smoking`, `Social_History_Header`, `Strength`, `Substance`, `Substance_Quantity`, `Symptom`, `Temperature`, `Test`, `Test_Result`, `Time`, `Total_Cholesterol`, `Treatment`, `Triglycerides`, `VS_Finding`, `Vaccine`, `Vaccine_Name`, `Vital_Signs_Header`, `Weight`

- Assertion Status Labels: `Hypothetical`, `Someoneelse`, `Past`, `Absent`, `Family`, `Planned`, `Possible`, `Present`

- Relation Extraction Labels: `is_finding_of`, `is_date_of`, `is_result_of`, `O`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_granular_en_5.2.1_3.0_1706288377782.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_granular_en_5.2.1_3.0_1706288377782.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_granular", "en", "clinical/models")

result = ner_pipeline.fullAnnotate("""The patient admitted for gastrointestinal pathology, under working treatment.
History of prior heart murmur with echocardiogram findings as above on March 1998.
According to the latest echocardiogram, basically revealed normal left ventricular function with left atrial enlargement .
Based on the above findings, we will treat her medically with ACE inhibitors and diuretics and see how she fares.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_granular", "en", "clinical/models")

val result = ner_pipeline.fullAnnotate("""The patient admitted for gastrointestinal pathology, under working treatment.
History of prior heart murmur with echocardiogram findings as above on March 1998.
According to the latest echocardiogram, basically revealed normal left ventricular function with left atrial enlargement .
Based on the above findings, we will treat her medically with ACE inhibitors and diuretics and see how she fares.""")

```
</div>

## Results

```bash
|    | chunks                     |   begin |   end | entities            |
|---:|:---------------------------|--------:|------:|:--------------------|
|  0 | admitted                   |      12 |    19 | Admission_Discharge |
|  1 | gastrointestinal pathology |      25 |    50 | Clinical_Dept       |
|  2 | heart murmur               |      95 |   106 | Heart_Disease       |
|  3 | echocardiogram             |     113 |   126 | Test                |
|  4 | March 1998                 |     149 |   158 | Date                |
|  5 | echocardiogram             |     185 |   198 | Test                |
|  6 | normal                     |     220 |   225 | Test_Result         |
|  7 | left ventricular function  |     227 |   251 | Test                |
|  8 | left atrial enlargement    |     258 |   280 | Heart_Disease       |
|  9 | her                        |     327 |   329 | Gender              |
| 10 | ACE inhibitors             |     346 |   359 | Drug_Ingredient     |
| 11 | diuretics                  |     365 |   373 | Drug_Ingredient     |
| 12 | she                        |     387 |   389 | Gender              |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_granular|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- NerConverterInternalModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel