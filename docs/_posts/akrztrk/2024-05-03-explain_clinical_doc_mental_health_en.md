---
layout: model
title: Explain Clinical Document - Mental Health
author: John Snow Labs
name: explain_clinical_doc_mental_health
date: 2024-05-03
tags: [licensed, en, relation_extraction, clinical, pipeline, mental_health, ner, assertion]
task: [Pipeline Healthcare, Named Entity Recognition, Relation Extraction, Assertion Status]
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to

- extract all mental health-related entities from text,

- assign assertion status to the extracted entities,

- establish relations between the extracted entities.

5 NER models, one assertion model and one relation extraction model were used in order to achieve those tasks.

Clinical Entity Labels:

`Mental_Health`, `Opioid_Drug`, `Substance_Use`, `Substance_Quantity`, `Injury_or_Poisoning`, `Symptom`, `Drug`, `Drug_Dosage`, `Drug_Duration`, `Drug_Route`, `Drug_Form`, `Frequency`, `Drug_Strength`, `Procedure`, `Treatment`, `Test`, `Test_Result`, `Gender`, `Age`, `Disease_Syndrome_Disorder`, `Smoking`, `Alcohol`, `Social_Exclusion`, `Family_Member`, `Childhood_Event`, `Disability`, `Eating_Disorder`, `Violence_Or_Abuse`

Assertion Status Labels:

`Present`, `Absent`, `Possible`, `Planned`, `Past`, `Family`, `Hypotetical`, `SomeoneElse`

Relation Extraction Labels:

`Drug- Drug_Dosage`, `Drug-Frequency`, `Drug-Duration`, `Drug-Drug_Strength`, `Drug-Drug`, `Test-Test_Result`, `Disease_Syndrome_Disorder-Symptom`, `Disease_Syndrome_Disorder-Drug`, `Symptom-Drug`, `Treatment_Drug`, `Symptom-Treatment`, `Disease_Syndrome_Disorder-Treatment`, `Treatment-Drug`, `Disease_Syndrome_Disorder-Procedure`, `Procedure-Drug`, `Mental_Health-Opioid_Drug`,  `Mental_Health-Substance_Use`,  `Mental_Health-Injury_or_Poisoning`, `Mental_Health-Symptom`, `Mental_Health-Drug`, `Mental_Health-Procedure`, `Mental_Health-Treatment`, `Mental_Health-Test`, `Mental_Health-Gender`, `Mental_Health-Age`, `Mental_Health-Disease_Syndrome_Disorder`, `Mental_Health-Smoking`, `Mental_Health-Alcohol`, `Mental_Health-Social_Exclusion`, `Mental_Health-Childhood_Event`, `Mental_Health-Disability`, `Mental_Health-Eating_Disorder`, `Mental_Health- Violence_Or_Abuse`,  `Opioid_Drug-Symptom`, `Opioid_Drug-Procedure`, `Opioid_Drug-Treatment`, `Opioid_Drug-Disease_Syndrome_Disorder`, `Opioid_Drug-Smoking`, `Opioid_Drug-Alcohol`, `Opioid_Drug-Childhood_Event`, `Opioid_Drug-Disability`, `Opioid_Drug-Eating_Disorder`, `Opioid_Drug-Violence_Or_Abuse`, `Opioid_Drug-Social_Exclusion`, `Substance_Use-Symptom`, `Substance_Use-Disease_Syndrome_Disorder`, `Substance_Use-Smoking`, `Substance_Use-Alcohol`, `Substance_Use-Childhood_Event`, `Substance_Use-Disability`, `Substance_Use-Eating_Disorder`, `Substance_Use-Violence_Or_Abuse`, `Substance_Use-Social_Exclusion`, `Substance_Use-Substance_Quantity`, `Injury_or_Poisoning-Symptom`, `Injury_or_Poisoning-Procedure`, `Injury_or_Poisoning-Test`, `Injury_or_Poisoning-Childhood_Event`, `Injury_or_Poisoning-Disability`, `Symptom-Procedure`, `Symptom-Test`, `Symptom-Eating_Disorder`, `Procedure-Disability`, `Opioid_Drug-Gender`, `Substance_Use-Gender`, `Opioid_Drug-Age`, `Substance_Use-Age`, `Violence_Or_Abuse-Gender`, `Violence_Or_Abuse-Age`, `Childhood_Event-Gender`, `Childhood_Event-Age`, `Alcohol-Gender`, `Alcohol-Age`, `Smoking-Gender`, `Smoking-Age`, `Social_Exclusion-Gender`, `Eating_Disorder-Disease_Syndrome_Disorder`, `Eating_Disorder-Treatment`, `Eating_Disorder-Alcohol`, `Eating_Disorder-Smoking`, `Disease_Syndrome_Disorder-Test`, `Disease_Syndrome_Disorder-Smoking`, `Disease_Syndrome_Disorder-Alcohol`, `Disease_Syndrome_Disorder-Social_Exclusion`, `Disease_Syndrome_Disorder-Childhood_Event`, `Disease_Syndrome_Disorder-Violence_Or_Abuse`, `Social_Exclusion-Alcohol`, `Social_Exclusion-Smoking`, `Social_Exclusion-Childhood_Event`, `Social_Exclusion-Disability`, `Social_Exclusion-Violence_Or_Abuse`, `Family_Member-Mental_Health`, `Childhood_Event-Disability`, `Childhood_Event-Eating_Disorder`, `Childhood_Event-Violence_Or_Abuse`

## Predicted Entities

`Age`, `Alcohol`, `Childhood_Event`, `Disability`, `Disease_Syndrome_Disorder`, `Dosage`, `Drug`, `Drug_Dosage`, `Drug_Duration`, `Drug_Form`, `Drug_Route`, `Drug_Strength`, `Eating_Disorder`, `Family_Member`, `Frequency`, `Gender`, `Injury_or_Poisoning`, `Mental_Health`, `Opioid_Drug`, `Procedure`, `Smoking`, `Social_Exclusion`, `SubstanceQuantity`, `Substance_Quantity`, `Substance_Use`, `Symptom`, `Test`, `Test_Result`, `Treatment`, `Violence_Or_Abuse`


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_mental_health_en_5.3.1_3.0_1714757124362.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_mental_health_en_5.3.1_3.0_1714757124362.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_mental_health", "en", "clinical/models")

result = ner_pipeline.annotate("""
The patient is a 38-year-old male presenting with complaints of anxiety and depression over the past 2 months. 
He has a history of hypertension, generalized anxiety disorder, major depressive disorder. 
The patient disclosed a history of childhood trauma, violence and abuse within his household. Those are the contributing factors to his smoking, alcohol use, and concurrent use of cocaine and marijuana. 
His anxiety has escalated with increased restlessness, irritability, muscle tension, and difficulties with concentration. He denies any suicidal ideation. Sleep has been poor and appetite decreased. 
Current medications include sertraline 100 mg daily, propranolol 20 mg twice daily, and lisinopril 20 mg daily.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_mental_health", "en", "clinical/models")

val result = ner_pipeline.annotate("""
The patient is a 38-year-old male presenting with complaints of anxiety and depression over the past 2 months. 
He has a history of hypertension, generalized anxiety disorder, major depressive disorder. 
The patient disclosed a history of childhood trauma, violence and abuse within his household. Those are the contributing factors to his smoking, alcohol use, and concurrent use of cocaine and marijuana. 
His anxiety has escalated with increased restlessness, irritability, muscle tension, and difficulties with concentration. He denies any suicidal ideation. Sleep has been poor and appetite decreased. 
Current medications include sertraline 100 mg daily, propranolol 20 mg twice daily, and lisinopril 20 mg daily.
""")

```
</div>

## Results

```bash

# NER
|    | chunks                          | begin | end |          entities         |
|---:|---------------------------------|:-----:|:---:|:-------------------------:|
|  0 | 38-year-old                     |   18  |  28 |            Age            |
|  1 | male                            |   30  |  33 |           Gender          |
|  2 | anxiety                         |   65  |  71 |       Mental_Health       |
|  3 | depression                      |   77  |  86 |       Mental_Health       |
|  4 | He                              |  113  | 114 |           Gender          |
|  5 | hypertension                    |  133  | 144 | Disease_Syndrome_Disorder |
|  6 | generalized anxiety disorder    |  147  | 174 |       Mental_Health       |
|  7 | major depressive disorder       |  177  | 201 |       Mental_Health       |
|  8 | childhood trauma                |  240  | 255 |      Childhood_Event      |
|  9 | violence                        |  258  | 265 |     Violence_Or_Abuse     |
| 10 | abuse                           |  271  | 275 |     Violence_Or_Abuse     |
| 11 | his                             |  284  | 286 |           Gender          |
| 12 | his                             |  337  | 339 |           Gender          |
| 13 | smoking                         |  341  | 347 |          Smoking          |
| 14 | alcohol                         |  350  | 356 |          Alcohol          |
| 15 | cocaine                         |  385  | 391 |       Substance_Use       |
| 16 | marijuana                       |  397  | 405 |       Substance_Use       |
| 17 | His                             |  409  | 411 |           Gender          |
| 18 | anxiety                         |  413  | 419 |       Mental_Health       |
| 19 | restlessness                    |  450  | 461 |          Symptom          |
| 20 | irritability                    |  464  | 475 |          Symptom          |
| 21 | muscle tension                  |  478  | 491 |          Symptom          |
| 22 | difficulties with concentration |  498  | 528 |          Symptom          |
| 23 | He                              |  531  | 532 |           Gender          |
| 24 | suicidal ideation               |  545  | 561 |       Mental_Health       |
| 25 | Sleep has been poor             |  564  | 582 |          Symptom          |
| 26 | appetite decreased              |  588  | 605 |          Symptom          |
| 27 | sertraline                      |  637  | 646 |            Drug           |
| 28 | 100 mg                          |  648  | 653 |       Drug_Strength       |
| 29 | daily                           |  655  | 659 |         Frequency         |
| 30 | propranolol                     |  662  | 672 |            Drug           |
| 31 | 20 mg                           |  674  | 678 |       Drug_Strength       |
| 32 | twice daily                     |  680  | 690 |         Frequency         |
| 33 | lisinopril                      |  697  | 706 |            Drug           |
| 34 | 20 mg                           |  708  | 712 |       Drug_Strength       |
| 35 | daily                           |  714  | 718 |         Frequency         |

# Assertion Status
|    | chunks                          |          entities         |   assertion  |
|---:|---------------------------------|:-------------------------:|:------------:|
|  0 | anxiety                         |       Mental_Health       |    Present   |
|  1 | depression                      |       Mental_Health       |    Present   |
|  2 | hypertension                    | Disease_Syndrome_Disorder |    Present   |
|  3 | generalized anxiety disorder    |       Mental_Health       |    Present   |
|  4 | major depressive disorder       |       Mental_Health       |    Present   |
|  5 | childhood trauma                |      Childhood_Event      |     Past     |
|  6 | violence                        |     Violence_Or_Abuse     |     Past     |
|  7 | abuse                           |     Violence_Or_Abuse     |     Past     |
|  8 | smoking                         |          Smoking          | Hypothetical |
|  9 | alcohol                         |          Alcohol          | Hypothetical |
| 10 | cocaine                         |       Substance_Use       | Hypothetical |
| 11 | marijuana                       |       Substance_Use       | Hypothetical |
| 12 | anxiety                         |       Mental_Health       |    Present   |
| 13 | restlessness                    |          Symptom          |    Present   |
| 14 | irritability                    |          Symptom          |    Present   |
| 15 | muscle tension                  |          Symptom          |    Present   |
| 16 | difficulties with concentration |          Symptom          |    Present   |
| 17 | suicidal ideation               |       Mental_Health       |    Absent    |
| 18 | Sleep has been poor             |          Symptom          |    Present   |
| 19 | appetite decreased              |          Symptom          |    Present   |

# Relation Extraction
|    | sentence | entity1_begin | entity1_end |      chunk1      |          entity1          | entity2_begin | entity2_end |            chunk2            |      entity2      |                 relation                | confidence |
|---:|---------:|--------------:|------------:|:----------------:|:-------------------------:|:-------------:|:-----------:|:----------------------------:|:-----------------:|:---------------------------------------:|:----------:|
|  0 |     0    |       18      |      28     |    38-year-old   |            Age            |       65      |      71     |            anxiety           |   Mental_Health   |            Age-Mental_Health            |     1.0    |
|  1 |     0    |       18      |      28     |    38-year-old   |            Age            |       77      |      86     |          depression          |   Mental_Health   |            Age-Mental_Health            |     1.0    |
|  2 |     0    |       30      |      33     |       male       |           Gender          |       65      |      71     |            anxiety           |   Mental_Health   |           Gender-Mental_Health          |     1.0    |
|  3 |     0    |       30      |      33     |       male       |           Gender          |       77      |      86     |          depression          |   Mental_Health   |           Gender-Mental_Health          |     1.0    |
|  4 |     1    |      113      |     114     |        He        |           Gender          |      147      |     174     | generalized anxiety disorder |   Mental_Health   |           Gender-Mental_Health          |     1.0    |
|  5 |     1    |      113      |     114     |        He        |           Gender          |      177      |     201     |   major depressive disorder  |   Mental_Health   |           Gender-Mental_Health          |     1.0    |
|  6 |     1    |      133      |     144     |   hypertension   | Disease_Syndrome_Disorder |      147      |     174     | generalized anxiety disorder |   Mental_Health   | Disease_Syndrome_Disorder-Mental_Health |     1.0    |
|  7 |     1    |      133      |     144     |   hypertension   | Disease_Syndrome_Disorder |      177      |     201     |   major depressive disorder  |   Mental_Health   | Disease_Syndrome_Disorder-Mental_Health |     1.0    |
|  8 |     2    |      240      |     255     | childhood trauma |      Childhood_Event      |      258      |     265     |           violence           | Violence_Or_Abuse |    Childhood_Event-Violence_Or_Abuse    |     1.0    |
|  9 |     2    |      240      |     255     | childhood trauma |      Childhood_Event      |      271      |     275     |             abuse            | Violence_Or_Abuse |    Childhood_Event-Violence_Or_Abuse    |     1.0    |
| 10 |     2    |      240      |     255     | childhood trauma |      Childhood_Event      |      284      |     286     |              his             |       Gender      |          Childhood_Event-Gender         |     1.0    |
| 11 |     2    |      258      |     265     |     violence     |     Violence_Or_Abuse     |      284      |     286     |              his             |       Gender      |         Violence_Or_Abuse-Gender        |     1.0    |
| 12 |     2    |      271      |     275     |       abuse      |     Violence_Or_Abuse     |      284      |     286     |              his             |       Gender      |         Violence_Or_Abuse-Gender        |     1.0    |
| 13 |     3    |      337      |     339     |        his       |           Gender          |      341      |     347     |            smoking           |      Smoking      |              Gender-Smoking             |     1.0    |
| 14 |     3    |      337      |     339     |        his       |           Gender          |      350      |     356     |            alcohol           |      Alcohol      |              Gender-Alcohol             |     1.0    |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_mental_health|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.1+|
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
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- GenericREModel
