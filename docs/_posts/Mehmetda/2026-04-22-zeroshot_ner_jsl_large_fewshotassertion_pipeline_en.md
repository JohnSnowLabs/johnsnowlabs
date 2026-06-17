---
layout: model
title: Zeroshot Ner Jsl Large With FewShotAssertion and ContextualAssertion - Pipeline
author: John Snow Labs
name: zeroshot_ner_jsl_large_fewshotassertion_pipeline
date: 2026-04-22
tags: [en, clinical, licensed, ner, assertion, pipeline]
task: [Named Entity Recognition, Assertion Status, Pipeline Healthcare]
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

This pipeline extracts clinical entities and their assertion status from medical text.

It first runs Zero-shot Named Entity Recognition (NER) with a pretrained clinical language model, restricted to a fixed, predefined label schema (e.g., AGE, GENDER, SYMPTOM, TEST, TEST_RESULT, TREATMENT, BLOOD_PRESSURE, TEMPERATURE, O2_SATURATION, and the other configured clinical labels). For long notes, it applies recursive document splitting into overlapping 512-character chunks (40-character overlap) to ensure stable inference at scale.

After entity extraction, the pipeline assigns assertion status using a hybrid approach:
- Few-shot assertion classification: converts each extracted entity into an assertion sentence, encodes it with medical E5 embeddings, and predicts assertion with a pretrained few-shot classifier (i2b2-based).
- Contextual rule-based assertion: applies contextual assertion models to detect scopes for absent, possible, conditional, and associated-with-someone-else mentions.

Finally, an AssertionMerger combines the few-shot and contextual outputs (majority voting + confidence-based ordering) to produce a single, consolidated assertion label per extracted entity.

Outputs include NER entity spans (with begin/end offsets and confidence) and merged assertion predictions (with confidence) aligned to each entity.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_jsl_large_fewshotassertion_pipeline_en_6.4.0_3.4_1776852974146.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_jsl_large_fewshotassertion_pipeline_en_6.4.0_3.4_1776852974146.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("zeroshot_ner_jsl_large_fewshotassertion_pipeline", "en", "clinical/models")

sample_text = """ The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("zeroshot_ner_jsl_large_fewshotassertion_pipeline", "en", "clinical/models")

sample_text = """ The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("zeroshot_ner_jsl_large_fewshotassertion_pipeline", "en", "clinical/models")

val sample_text = """ The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""

val result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
</div>

## Results

```bash

+---------------------+-----+---+--------------+----------------------------+--------------------+
|chunk                |begin|end|ner_label     |assertion                   |assertion_confidence|
+---------------------+-----+---+--------------+----------------------------+--------------------+
|21-day-old           |17   |26 |AGE           |present                     |0.75985414          |
|Caucasian            |28   |36 |RACE_ETHNICITY|present                     |0.926688            |
|male                 |38   |41 |GENDER        |present                     |0.79617095          |
|congestion           |62   |71 |SYMPTOM       |present                     |0.9525222           |
|mom                  |75   |77 |GENDER        |associated_with_someone_else|1.0                 |
|yellow discharge     |99   |114|SYMPTOM       |present                     |0.9546637           |
|she                  |147  |149|GENDER        |present                     |0.91394824          |
|mild                 |168  |171|MODIFIER      |present                     |0.952924            |
|his                  |187  |189|GENDER        |present                     |0.89463806          |
|breathing            |191  |199|RESPIRATION   |present                     |0.9494906           |
|negative             |220  |227|TEST_RESULT   |absent                      |1.0                 |
|retractions          |258  |268|SYMPTOM       |absent                      |0.9556229           |
|Influenza vaccine    |325  |341|VACCINE       |present                     |0.9537577           |
|mom                  |357  |359|GENDER        |associated_with_someone_else|1.0                 |
|Tylenol              |417  |423|VACCINE       |present                     |0.9479955           |
|Baby                 |426  |429|GENDER        |conditional                 |0.3395339           |
|decreased p.o. intake|449  |469|SYMPTOM       |present                     |0.95393014          |
|His                  |472  |474|GENDER        |present                     |0.9232172           |
|His                  |472  |474|GENDER        |present                     |0.9232172           |
|his                  |560  |562|GENDER        |present                     |0.9278281           |
+---------------------+-----+---+--------------+----------------------------+--------------------+



```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_jsl_large_fewshotassertion_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|

## Included Models

- DocumentAssembler
- InternalDocumentSplitter
- TokenizerModel
- PretrainedZeroShotNER
- NerConverterInternalModel
- FewShotAssertionSentenceConverter
- E5Embeddings
- FewShotAssertionClassifierModel
- ContextualAssertion
- ContextualAssertion
- ContextualAssertion
- ContextualAssertion
- AssertionMerger