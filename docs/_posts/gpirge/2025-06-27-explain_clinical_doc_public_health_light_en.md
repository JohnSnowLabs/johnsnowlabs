---
layout: model
title: Explain Clinical Document Public Health - Light
author: John Snow Labs
name: explain_clinical_doc_public_health_light
date: 2025-06-27
tags: [licensed, en, clinical, pipeline, ner, public_health]
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

This pipeline is designed to extract public health related clinical/medical entities from text. In this pipeline, 3 NER models and a text matcher are used to extract the clinical entity labels.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_public_health_light_en_6.0.2_3.4_1751041663258.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_public_health_light_en_6.0.2_3.4_1751041663258.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_public_health_light", "en", "clinical/models")

result = ner_pipeline.annotate("""A recent community health survey conducted in South Oakwood revealed high rates of hypertension, diabetes, and obesity, particularly among low-income residents and minority populations. 
Limited access to healthy food options and safe recreational spaces has contributed to poor diet and low physical activity levels.
Many respondents reported unemployment or unstable jobs, lack of health insurance, and difficulties accessing primary care facilities. 
Substance use, including alcohol, marijuana and tobacco, was notably prevalent among young adults, while older adults reported feelings of isolation and untreated mental health issues.
The report also highlighted increasing rates of communicable diseases such as Hepatitis C among individuals with a history of intravenous drug use. 
Domestic violence and housing insecurity were frequently mentioned, especially among single mothers.
Public health officials are planning targeted interventions to improve access to care, expand social support programs, and address racial disparities in health outcomes.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_public_health_light", "en", "clinical/models")

val result = ner_pipeline.annotate("""A recent community health survey conducted in South Oakwood revealed high rates of hypertension, diabetes, and obesity, particularly among low-income residents and minority populations. 
Limited access to healthy food options and safe recreational spaces has contributed to poor diet and low physical activity levels.
Many respondents reported unemployment or unstable jobs, lack of health insurance, and difficulties accessing primary care facilities. 
Substance use, including alcohol, marijuana and tobacco, was notably prevalent among young adults, while older adults reported feelings of isolation and untreated mental health issues.
The report also highlighted increasing rates of communicable diseases such as Hepatitis C among individuals with a history of intravenous drug use. 
Domestic violence and housing insecurity were frequently mentioned, especially among single mothers.
Public health officials are planning targeted interventions to improve access to care, expand social support programs, and address racial disparities in health outcomes.
""")

```
</div>

## Results

```bash
|    | chunks                       |   begin |   end | entities                  |
|---:|:-----------------------------|--------:|------:|:--------------------------|
|  0 | hypertension                 |      83 |    94 | Disease_Syndrome_Disorder |
|  1 | diabetes                     |      97 |   104 | Disease_Syndrome_Disorder |
|  2 | obesity                      |     111 |   117 | Obesity                   |
|  3 | low-income residents         |     139 |   158 | Employment                |
|  4 | minority populations         |     164 |   183 | Spiritual_Beliefs         |
|  5 | healthy food                 |     205 |   216 | Food_Insecurity           |
|  6 | safe recreational spaces     |     230 |   253 | Environmental_Condition   |
|  7 | poor diet                    |     274 |   282 | Diet                      |
|  8 | low physical activity levels |     288 |   315 | Environmental_Condition   |
|  9 | unemployment                 |     344 |   355 | Employment                |
| 10 | unstable jobs                |     360 |   372 | Employment                |
| 11 | health insurance             |     383 |   398 | Insurance_Status          |
| 12 | primary care facilities      |     428 |   450 | Access_To_Care            |
| 13 | Substance                    |     454 |   462 | Substance                 |
| 14 | alcohol                      |     479 |   485 | Alcohol                   |
| 15 | marijuana                    |     488 |   496 | Substance                 |
| 16 | tobacco                      |     502 |   508 | Smoking                   |
| 17 | isolation                    |     593 |   601 | Social_Exclusion          |
| 18 | mental health issues         |     617 |   636 | Mental_Health             |
| 19 | communicable diseases        |     687 |   707 | Disease_Syndrome_Disorder |
| 20 | Hepatitis C                  |     717 |   727 | Disease_Syndrome_Disorder |
| 21 | intravenous drug             |     765 |   780 | Substance                 |
| 22 | Domestic violence            |     788 |   804 | Violence_Or_Abuse         |
| 23 | housing insecurity           |     810 |   827 | Housing                   |
| 24 | single                       |     873 |   878 | Relationship_Status       |
| 25 | Public health officials      |     889 |   911 | Employment                |
| 26 | access to care               |     960 |   973 | Access_To_Care            |
| 27 | social support               |     983 |   996 | Social_Support            |
| 28 | racial disparities           |    1020 |  1037 | Community_Safety          |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_public_health_light|
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
- NerConverterInternalModel
- TextMatcherInternalModel
- ChunkMergeModel