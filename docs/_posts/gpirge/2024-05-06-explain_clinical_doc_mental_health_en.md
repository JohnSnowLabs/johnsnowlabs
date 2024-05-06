---
layout: model
title: Explain Clinical Document - Mental Health
author: John Snow Labs
name: explain_clinical_doc_mental_health
date: 2024-05-06
tags: [licensed, en, relation_extraction, clinical, pipeline, mental_health, ner, assertion]
task: [Pipeline Healthcare, Named Entity Recognition, Relation Extraction, Assertion Status]
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.4
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

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_mental_health_en_5.3.1_3.4_1715007317314.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_mental_health_en_5.3.1_3.4_1715007317314.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
|    | chunks                          |   begin |   end | entities                  |
|---:|:--------------------------------|--------:|------:|:--------------------------|
|  0 | 38-year-old                     |      18 |    28 | Age                       |
|  1 | male                            |      30 |    33 | Gender                    |
|  2 | anxiety                         |      65 |    71 | Mental_Health             |
|  3 | depression                      |      77 |    86 | Mental_Health             |
|  4 | He                              |     112 |   113 | Gender                    |
|  5 | hypertension                    |     132 |   143 | Disease_Syndrome_Disorder |
|  6 | generalized anxiety disorder    |     146 |   173 | Mental_Health             |
|  7 | major depressive disorder       |     176 |   200 | Mental_Health             |
|  8 | childhood trauma                |     238 |   253 | Childhood_Event           |
|  9 | violence                        |     256 |   263 | Violence_Or_Abuse         |
| 10 | abuse                           |     269 |   273 | Violence_Or_Abuse         |
| 11 | his                             |     282 |   284 | Gender                    |
| 12 | his                             |     335 |   337 | Gender                    |
| 13 | smoking                         |     339 |   345 | Smoking                   |
| 14 | alcohol                         |     348 |   354 | Alcohol                   |
| 15 | cocaine                         |     383 |   389 | Substance_Use             |
| 16 | marijuana                       |     395 |   403 | Substance_Use             |
| 17 | His                             |     406 |   408 | Gender                    |
| 18 | anxiety                         |     410 |   416 | Mental_Health             |
| 19 | restlessness                    |     447 |   458 | Symptom                   |
| 20 | irritability                    |     461 |   472 | Symptom                   |
| 21 | muscle tension                  |     475 |   488 | Symptom                   |
| 22 | difficulties with concentration |     495 |   525 | Symptom                   |
| 23 | He                              |     528 |   529 | Gender                    |
| 24 | suicidal ideation               |     542 |   558 | Mental_Health             |
| 25 | Sleep has been poor             |     561 |   579 | Symptom                   |
| 26 | appetite decreased              |     585 |   602 | Symptom                   |
| 27 | sertraline                      |     633 |   642 | Drug                      |
| 28 | 100 mg                          |     644 |   649 | Drug_Strength             |
| 29 | daily                           |     651 |   655 | Frequency                 |
| 30 | propranolol                     |     658 |   668 | Drug                      |
| 31 | 20 mg                           |     670 |   674 | Drug_Strength             |
| 32 | twice daily                     |     676 |   686 | Frequency                 |
| 33 | lisinopril                      |     693 |   702 | Drug                      |
| 34 | 20 mg                           |     704 |   708 | Drug_Strength             |
| 35 | daily                           |     710 |   714 | Frequency                 |
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