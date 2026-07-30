---
layout: model
title: Zeroshot Ner Jsl Medium- Pipeline
author: John Snow Labs
name: zeroshot_ner_jsl_medium_pipeline
date: 2026-04-22
tags: [en, clinical, licensed, ner, pipeline]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline performs clinical Zero-shot Named Entity Recognition (NER) using a pretrained language model with contextual understanding, enabling entity extraction without task-specific fine-tuning.

To ensure consistent and production-stable outputs, the pipeline uses a fixed, predefined label schema. Predictions are restricted to the supported labels provided to the model (e.g., AGE, GENDER, SYMPTOM, TEST, TEST_RESULT, TREATMENT, BLOOD_PRESSURE, TEMPERATURE, O2_SATURATION, and other clinical categories in the configured label list).

The pipeline also supports long medical notes by splitting documents into overlapping 512-character chunks before tokenization and inference, then converts token-level predictions into consolidated entity spans with character offsets and confidence scores.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_jsl_medium_pipeline_en_6.4.0_3.4_1776847162358.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_jsl_medium_pipeline_en_6.4.0_3.4_1776847162358.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("zeroshot_ner_jsl_medium_pipeline", "en", "clinical/models")

sample_text = """ The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("zeroshot_ner_jsl_medium_pipeline", "en", "clinical/models")

sample_text = """ The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("zeroshot_ner_jsl_medium_pipeline", "en", "clinical/models")

val sample_text = """ The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""

val result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
</div>

## Results

```bash

+----------------------+-----+---+--------------------+----------+
|chunk                 |begin|end|ner_label           |confidence|
+----------------------+-----+---+--------------------+----------+
|21-day-old            |17   |26 |AGE                 |0.99695885|
|Caucasian             |28   |36 |RACE_ETHNICITY      |0.97338253|
|male                  |38   |41 |GENDER              |0.99688834|
|congestion            |62   |71 |COMMUNICABLE_DISEASE|0.7530978 |
|mom                   |75   |77 |GENDER              |0.99827564|
|yellow discharge      |99   |114|SYMPTOM             |0.60354805|
|she                   |147  |149|GENDER              |0.9835264 |
|his                   |187  |189|GENDER              |0.8737911 |
|retractions           |258  |268|SYMPTOM             |0.81836635|
|mom                   |357  |359|GENDER              |0.9957776 |
|decreased p.o. intake |449  |469|SYMPTOM             |0.6698668 |
|His                   |472  |474|GENDER              |0.9965887 |
|His                   |472  |474|GENDER              |0.9945926 |
|his                   |560  |562|GENDER              |0.98096585|
|respiratory congestion|564  |585|KIDNEY_DISEASE      |0.6405383 |
|He                    |588  |589|GENDER              |0.9884072 |
|tired                 |622  |626|SYMPTOM             |0.7520301 |
|fussy                 |641  |645|SYMPTOM             |0.8103654 |
|His                   |747  |749|GENDER              |0.97294575|
|decreased             |773  |781|SYMPTOM             |0.6032274 |
+----------------------+-----+---+--------------------+----------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_jsl_medium_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|789.8 MB|

## Included Models

- DocumentAssembler
- InternalDocumentSplitter
- TokenizerModel
- PretrainedZeroShotNER
- NerConverterInternalModel