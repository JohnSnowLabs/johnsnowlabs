---
layout: model
title: Pipeline to Social Determinants of Health (LangTest)
author: John Snow Labs
name: ner_sdoh_langtest_pipeline
date: 2023-09-09
tags: [licensed, en, sdoh, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_sdoh_langtest](https://nlp.johnsnowlabs.com/2023/07/31/ner_sdoh_langtest_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_langtest_pipeline_en_5.1.0_3.0_1694278273068.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_langtest_pipeline_en_5.1.0_3.0_1694278273068.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_sdoh_langtest_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She speaks Spanish and Portuguese. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI in April and was due to court this week.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_sdoh_langtest_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She speaks Spanish and Portuguese. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI in April and was due to court this week.""")

```
</div>

## Results

```bash
|    | chunks                  |   begin |   end | entities            |
|---:|:------------------------|--------:|------:|:--------------------|
|  0 | 55 years old            |       9 |    20 | Age                 |
|  1 | New York                |      33 |    40 | Geographic_Entity   |
|  2 | divorced                |      45 |    52 | Marital_Status      |
|  3 | Mexcian American        |      54 |    69 | Race_Ethnicity      |
|  4 | woman                   |      71 |    75 | Gender              |
|  5 | financial problems      |      82 |    99 | Financial_Status    |
|  6 | She                     |     102 |   104 | Gender              |
|  7 | Spanish                 |     113 |   119 | Language            |
|  8 | Portuguese              |     125 |   134 | Language            |
|  9 | She                     |     137 |   139 | Gender              |
| 10 | apartment               |     153 |   161 | Housing             |
| 11 | She                     |     164 |   166 | Gender              |
| 12 | diabetes                |     193 |   200 | Other_Disease       |
| 13 | hospitalizations        |     268 |   283 | Other_SDoH_Keywords |
| 14 | cleaning assistant      |     342 |   359 | Employment          |
| 15 | access health insurance |     372 |   394 | Insurance_Status    |
| 16 | She                     |     416 |   418 | Gender              |
| 17 | son                     |     426 |   428 | Family_Member       |
| 18 | student                 |     433 |   439 | Education           |
| 19 | college                 |     444 |   450 | Education           |
| 20 | depression              |     482 |   491 | Mental_Health       |
| 21 | She                     |     494 |   496 | Gender              |
| 22 | she                     |     507 |   509 | Gender              |
| 23 | rehab                   |     517 |   521 | Access_To_Care      |
| 24 | her                     |     542 |   544 | Gender              |
| 25 | catholic faith          |     546 |   559 | Spiritual_Beliefs   |
| 26 | support                 |     575 |   581 | Social_Support      |
| 27 | She                     |     593 |   595 | Gender              |
| 28 | etoh abuse              |     619 |   628 | Alcohol             |
| 29 | her                     |     644 |   646 | Gender              |
| 30 | teens                   |     648 |   652 | Age                 |
| 31 | She                     |     655 |   657 | Gender              |
| 32 | she                     |     667 |   669 | Gender              |
| 33 | daily                   |     682 |   686 | Substance_Frequency |
| 34 | drinker                 |     688 |   694 | Alcohol             |
| 35 | 30 years                |     700 |   707 | Substance_Duration  |
| 36 | drinking                |     724 |   731 | Alcohol             |
| 37 | beer                    |     733 |   736 | Alcohol             |
| 38 | daily                   |     738 |   742 | Substance_Frequency |
| 39 | She                     |     745 |   747 | Gender              |
| 40 | smokes                  |     749 |   754 | Smoking             |
| 41 | a pack                  |     756 |   761 | Substance_Quantity  |
| 42 | cigarettes              |     766 |   775 | Smoking             |
| 43 | a day                   |     777 |   781 | Substance_Frequency |
| 44 | She                     |     784 |   786 | Gender              |
| 45 | DUI                     |     792 |   794 | Legal_Issues        |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_sdoh_langtest_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.1.0+|
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