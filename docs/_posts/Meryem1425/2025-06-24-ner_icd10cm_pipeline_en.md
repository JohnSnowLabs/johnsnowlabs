---
layout: model
title: Pipeline for Extracting Clinical Entities Related to ICD-10-CM (General 3-character Codes)
author: John Snow Labs
name: ner_icd10cm_pipeline
date: 2025-06-24
tags: [licensed, en, clinical, pipeline, ner]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to extract all entities mappable to ICD-10CM codes.

2 NER models and a Text Matcher are used to achieve those tasks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_icd10cm_pipeline_en_6.0.2_3.4_1750775269394.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_icd10cm_pipeline_en_6.0.2_3.4_1750775269394.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_icd10cm_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
The patient is a 38-year-old male presenting with complaints of anxiety and depression over the past 2 months.
He has a history of hypertension, generalized anxiety disorder, major depressive disorder.
The patient disclosed a history of childhood trauma, violence and abuse within his household. Those are the contributing factors to his smoking, alcohol use, and concurrent use of cocaine and marijuana.
Anxiety level has escalated with increased restlessness, irritability, muscle tension, and difficulties with concentration. He denies any suicidal ideation. Sleep has been poor and appetite decreased.
The patient was recently diagnosed with squamous cell carcinoma following a biopsy of the suspicious lesion.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_icd10cm_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
The patient is a 38-year-old male presenting with complaints of anxiety and depression over the past 2 months.
He has a history of hypertension, generalized anxiety disorder, major depressive disorder.
The patient disclosed a history of childhood trauma, violence and abuse within his household. Those are the contributing factors to his smoking, alcohol use, and concurrent use of cocaine and marijuana.
Anxiety level has escalated with increased restlessness, irritability, muscle tension, and difficulties with concentration. He denies any suicidal ideation. Sleep has been poor and appetite decreased.
The patient was recently diagnosed with squamous cell carcinoma following a biopsy of the suspicious lesion.
""")

```
</div>

## Results

```bash
|    | chunks                          |   begin |   end | entities                |
|---:|:--------------------------------|--------:|------:|:------------------------|
|  0 | anxiety                         |      65 |    71 | PSYCHOLOGICAL_CONDITION |
|  1 | depression                      |      77 |    86 | PSYCHOLOGICAL_CONDITION |
|  2 | hypertension                    |     132 |   143 | HYPERTENSION            |
|  3 | generalized anxiety disorder    |     146 |   173 | PROBLEM                 |
|  4 | major depressive disorder       |     176 |   200 | PSYCHOLOGICAL_CONDITION |
|  5 | childhood trauma                |     238 |   253 | INJURY_OR_POISONING     |
|  6 | violence                        |     256 |   263 | INJURY_OR_POISONING     |
|  7 | Anxiety level                   |     406 |   418 | PROBLEM                 |
|  8 | increased restlessness          |     439 |   460 | PROBLEM                 |
|  9 | irritability                    |     463 |   474 | SYMPTOM                 |
| 10 | muscle tension                  |     477 |   490 | SYMPTOM                 |
| 11 | difficulties with concentration |     497 |   527 | SYMPTOM                 |
| 12 | any suicidal ideation           |     540 |   560 | PROBLEM                 |
| 13 | Sleep has been poor             |     563 |   581 | SYMPTOM                 |
| 14 | appetite decreased              |     587 |   604 | SYMPTOM                 |
| 15 | squamous cell carcinoma         |     647 |   669 | Cancer_dx               |
| 16 | the suspicious lesion           |     693 |   713 | PROBLEM                 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_icd10cm_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
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
- MedicalNerModel
- NerConverter
- TextMatcherInternalModel
- ChunkMergeModel