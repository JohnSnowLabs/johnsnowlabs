---
layout: model
title: Explain Clinical Document - Voice Of Patient (VOP)
author: John Snow Labs
name: explain_clinical_doc_vop_small
date: 2024-09-09
tags: [licensed, en, vop, ner, assertion, relation_extraction, pipeline]
task: [Pipeline Healthcare, Named Entity Recognition, Assertion Status, Relation Extraction]
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to

- extract all clinical/medical entities from voice of patient notes,

- assign assertion status to the extracted entities,

- establish relations between the extracted entities.

One ner model, one assertion model and one relation extraction model were used in order to achieve those tasks.

Clinical Entity Labels:

`InjuryOrPoisoning`, `Substance`, `Form`, `Frequency`, `Employment`, `Drug`, `Route`, `Disease`, `Gender`, `Dosage`, `Employment`, `Procedure`, `RelationshipStatus`, `ClinicalDept`, `Symptom`, `VitalTest`, `Laterality`, `PsychologicalCondition`,`Modifier`, `Age`, `Vaccine`, `TestResult`, `HealthStatus`, `AdmissionDischarge`, `Allergen`, `DateTime`, `MedicalDevice`, `SubstanceQuantity`, `Treatment`, `BodyPart`, `Test`, `Duration`


Assertion Status Labels:

`Present_Or_Past`, `Hypothetical_Or_Absent`, `SomeoneElse`


Relation Extraction Labels:

`DateTime-Symptom`, `DateTime-Disease`, `DateTime-PsychologicalCondition`, `DateTime-InjuryOrPoisoning`, `DateTime-Drug`, `DateTime-Substance`, `DateTime-Procedure`, `DateTime-Treatment`, `DateTime-Test`, `DateTime-TestResult`, `DateTime-Vaccine`, `DateTime-AdmissionDischarge`, `TestResult-Test`, `TestResult-VitalTest`, `PsychologicalCondition-Drug`, `PsychologicalCondition-Procedure`, `PsychologicalCondition-Treatment`, `Disease-Drug`, `Disease-Procedure`, `Disease-Treatment`, `Disease-Allergen`, `Disease-Vaccine`, `Treatment-Drug`, `Treatment-Procedure`, `Drug-Procedure`, `Symptom-Disease`, `Symptom-InjuryOrPoisoning`, `Symptom-PsychologicalCondition`, `BodyPart-Disease`, `BodyPart-Symptom`, `BodyPart-InjuryOrPoisoning`, `BodyPart-Test`, `BodyPart-Procedure`, `Drug-Dosage`, `Drug-Frequency`, `Drug-Form`, `Disease-Test`

## Predicted Entities

`InjuryOrPoisoning`, `Substance`, `Form`, `Frequency`, `Employment`, `Drug`, `Route`, `Disease`, `Gender`, `Dosage`, `Employment`, `Procedure`, `RelationshipStatus`, `ClinicalDept`, `Symptom`, `VitalTest`, `Laterality`, `PsychologicalCondition`,`Modifier`, `Age`, `Vaccine`, `TestResult`, `HealthStatus`, `AdmissionDischarge`, `Allergen`, `DateTime`, `MedicalDevice`, `SubstanceQuantity`, `Treatment`, `BodyPart`, `Test`, `Duration`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_vop_small_en_5.4.1_3.4_1725903018000.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_vop_small_en_5.4.1_3.4_1725903018000.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_vop_small", "en", "clinical/models")

result = ner_pipeline.annotate("""
It seems like my health troubles started a few years ago. I had been feeling really tired all the time and was losing weight without even trying. My doctor did some blood work and said my sugar levels were high - he diagnosed me with something called type 2 diabetes.
He put me on two medications - I take a pill called metformin 500 mg twice a day, and another one called glipizide 5 mg before breakfast and dinner. Those are supposed to help lower my blood sugar. I also have to watch what I eat and try to exercise more even though it's hard with my energy levels.
A couple years after the diabetes, I started having really bad heartburn all the time. I saw a specialist called a gastroenterologist who did an endoscopy procedure where they stick a camera down your throat. That test showed I have chronic acid reflux disease or GERD. Now I take a daily pill called omeprazole 20 mg to control the heartburn symptoms.
Most recently, I've had a lot of joint pain in my shoulders and knees. My primary doctor ran some blood tests that showed something called rheumatoid arthritis. He referred me to a rheumatologist who started me on a weekly medication called methotrexate. I have to remember to take folic acid with that to help minimize side effects. It seems to be helping the joint pain so far.
""")

```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_vop_small", "en", "clinical/models")

val result = ner_pipeline.annotate("""
It seems like my health troubles started a few years ago. I had been feeling really tired all the time and was losing weight without even trying. My doctor did some blood work and said my sugar levels were high - he diagnosed me with something called type 2 diabetes.
He put me on two medications - I take a pill called metformin 500 mg twice a day, and another one called glipizide 5 mg before breakfast and dinner. Those are supposed to help lower my blood sugar. I also have to watch what I eat and try to exercise more even though it's hard with my energy levels.
A couple years after the diabetes, I started having really bad heartburn all the time. I saw a specialist called a gastroenterologist who did an endoscopy procedure where they stick a camera down your throat. That test showed I have chronic acid reflux disease or GERD. Now I take a daily pill called omeprazole 20 mg to control the heartburn symptoms.
Most recently, I've had a lot of joint pain in my shoulders and knees. My primary doctor ran some blood tests that showed something called rheumatoid arthritis. He referred me to a rheumatologist who started me on a weekly medication called methotrexate. I have to remember to take folic acid with that to help minimize side effects. It seems to be helping the joint pain so far.
""")

```
</div>

## Results

```bash

#NER

|    | chunks                      |   begin |   end |   sentence_id | entities      |   confidence |
|---:|:----------------------------|--------:|------:|--------------:|:--------------|-------------:|
|  0 | few years ago               |      44 |    56 |             0 | DateTime      |     0.620833 |
|  1 | really                      |      78 |    83 |             1 | Modifier      |     0.5723   |
|  2 | tired                       |      85 |    89 |             1 | Symptom       |     0.9959   |
|  3 | all the time                |      91 |   102 |             1 | Duration      |     0.5925   |
|  4 | losing weight               |     112 |   124 |             1 | Symptom       |     0.81445  |
|  5 | doctor                      |     150 |   155 |             2 | Employment    |     0.9895   |
|  6 | blood work                  |     166 |   175 |             2 | Test          |     0.8835   |
|  7 | sugar levels                |     189 |   200 |             2 | Test          |     0.8277   |
|  8 | high                        |     207 |   210 |             2 | TestResult    |     0.9095   |
|  9 | he                          |     214 |   215 |             2 | Gender        |     1        |
| 10 | type 2 diabetes             |     252 |   266 |             2 | Disease       |     0.379367 |
| 11 | He                          |     269 |   270 |             3 | Gender        |     1        |
| 12 | pill                        |     309 |   312 |             3 | Form          |     0.9979   |
| 13 | metformin                   |     321 |   329 |             3 | Drug          |     0.997    |
| 14 | 500 mg                      |     331 |   336 |             3 | Dosage        |     0.9785   |
| 15 | twice a day                 |     338 |   348 |             3 | Frequency     |     0.889967 |
| 16 | glipizide                   |     374 |   382 |             3 | Drug          |     0.9953   |
| 17 | 5 mg                        |     384 |   387 |             3 | Dosage        |     0.96535  |
| 18 | blood sugar                 |     454 |   464 |             4 | Test          |     0.6415   |
| 19 | couple years after          |     571 |   588 |             6 | DateTime      |     0.5461   |
| 20 | diabetes                    |     594 |   601 |             6 | Disease       |     0.9901   |
| 21 | heartburn                   |     632 |   640 |             6 | Symptom       |     0.988    |
| 22 | all the time                |     642 |   653 |             6 | Duration      |     0.624767 |
| 23 | specialist                  |     664 |   673 |             7 | Employment    |     0.9878   |
| 24 | gastroenterologist          |     684 |   701 |             7 | Employment    |     0.9866   |
| 25 | endoscopy procedure         |     714 |   732 |             7 | Procedure     |     0.75475  |
| 26 | camera                      |     753 |   758 |             7 | MedicalDevice |     0.9362   |
| 27 | throat                      |     770 |   775 |             7 | BodyPart      |     0.8006   |
| 28 | chronic acid reflux disease |     802 |   828 |             8 | Disease       |     0.7071   |
| 29 | GERD                        |     833 |   836 |             8 | Disease       |     0.9476   |
| 30 | Now                         |     839 |   841 |             9 | DateTime      |     0.9938   |
| 31 | daily                       |     852 |   856 |             9 | Frequency     |     0.9183   |
| 32 | pill                        |     858 |   861 |             9 | Form          |     0.9925   |
| 33 | omeprazole                  |     870 |   879 |             9 | Drug          |     0.9987   |
| 34 | 20 mg                       |     881 |   885 |             9 | Dosage        |     0.9704   |
| 35 | heartburn                   |     902 |   910 |             9 | Symptom       |     0.9849   |
| 36 | recently                    |     927 |   934 |            10 | DateTime      |     0.9637   |
| 37 | a lot                       |     946 |   950 |            10 | Modifier      |     0.6227   |
| 38 | joint                       |     955 |   959 |            10 | BodyPart      |     0.8617   |
| 39 | pain                        |     961 |   964 |            10 | Symptom       |     0.9923   |
| 40 | shoulders                   |     972 |   980 |            10 | BodyPart      |     0.9362   |
| 41 | knees                       |     986 |   990 |            10 | BodyPart      |     0.8989   |
| 42 | primary doctor              |     996 |  1009 |            11 | Employment    |     0.75345  |
| 43 | blood tests                 |    1020 |  1030 |            11 | Test          |     0.93715  |
| 44 | rheumatoid arthritis        |    1061 |  1080 |            11 | Disease       |     0.74685  |
| 45 | He                          |    1083 |  1084 |            12 | Gender        |     1        |
| 46 | rheumatologist              |    1103 |  1116 |            12 | Employment    |     0.9913   |
| 47 | weekly                      |    1138 |  1143 |            12 | Frequency     |     0.8902   |
| 48 | methotrexate                |    1163 |  1174 |            12 | Drug          |     0.9995   |
| 49 | folic acid                  |    1204 |  1213 |            13 | Drug          |     0.7913   |
| 50 | joint                       |    1283 |  1287 |            14 | BodyPart      |     0.874    |
| 51 | pain                        |    1289 |  1292 |            14 | Symptom       |     0.9837   |

# Assertion Status

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

# Relation Extraction

|    |   sentence |   entity1_begin |   entity1_end | chunk1              | entity1   |   entity2_begin |   entity2_end | chunk2       | entity2    | relation           |   confidence |
|---:|-----------:|----------------:|--------------:|:--------------------|:----------|----------------:|--------------:|:-------------|:-----------|:-------------------|-------------:|
|  0 |          2 |             166 |           175 | blood work          | Test      |             207 |           210 | high         | TestResult | Test-TestResult    |            1 |
|  1 |          3 |             309 |           312 | pill                | Form      |             321 |           329 | metformin    | Drug       | Form-Drug          |            1 |
|  2 |          3 |             321 |           329 | metformin           | Drug      |             331 |           336 | 500 mg       | Dosage     | Drug-Dosage        |            1 |
|  3 |          3 |             321 |           329 | metformin           | Drug      |             338 |           348 | twice a day  | Frequency  | Drug-Frequency     |            1 |
|  4 |          3 |             374 |           382 | glipizide           | Drug      |             384 |           387 | 5 mg         | Dosage     | Drug-Dosage        |            1 |
|  5 |          6 |             571 |           588 | couple years after  | DateTime  |             594 |           601 | diabetes     | Disease    | DateTime-Disease   |            1 |
|  6 |          6 |             594 |           601 | diabetes            | Disease   |             632 |           640 | heartburn    | Symptom    | Disease-Symptom    |            1 |
|  7 |          7 |             714 |           732 | endoscopy procedure | Procedure |             770 |           775 | throat       | BodyPart   | Procedure-BodyPart |            1 |
|  8 |          9 |             852 |           856 | daily               | Frequency |             870 |           879 | omeprazole   | Drug       | Frequency-Drug     |            1 |
|  9 |          9 |             858 |           861 | pill                | Form      |             870 |           879 | omeprazole   | Drug       | Form-Drug          |            1 |
| 10 |          9 |             870 |           879 | omeprazole          | Drug      |             881 |           885 | 20 mg        | Dosage     | Drug-Dosage        |            1 |
| 11 |         10 |             927 |           934 | recently            | DateTime  |             961 |           964 | pain         | Symptom    | DateTime-Symptom   |            1 |
| 12 |         10 |             955 |           959 | joint               | BodyPart  |             961 |           964 | pain         | Symptom    | BodyPart-Symptom   |            1 |
| 13 |         10 |             961 |           964 | pain                | Symptom   |             972 |           980 | shoulders    | BodyPart   | Symptom-BodyPart   |            1 |
| 14 |         10 |             961 |           964 | pain                | Symptom   |             986 |           990 | knees        | BodyPart   | Symptom-BodyPart   |            1 |
| 15 |         12 |            1138 |          1143 | weekly              | Frequency |            1163 |          1174 | methotrexate | Drug       | Frequency-Drug     |            1 |
| 16 |         14 |            1283 |          1287 | joint               | BodyPart  |            1289 |          1292 | pain         | Symptom    | BodyPart-Symptom   |            1 |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_vop_small|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.4.1+|
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
- GenericREModel
