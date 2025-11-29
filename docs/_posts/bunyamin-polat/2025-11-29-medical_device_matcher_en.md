---
layout: model
title: Medical Device Text Matcher
author: John Snow Labs
name: medical_device_matcher
date: 2025-11-29
tags: [matcher, medical_device, en, licensed, clinical]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.2
supported: true
annotator: TextMatcherInternalModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a TextMatcher model that can identify medical device entities in clinical text. It recognizes various medical devices including insulin pump, pacemaker, CPAP machine, glucometer, oxygen concentrator, hearing aid, catheter, nebulizer, stent, and many more medical devices.

## Predicted Entities

`MEDICAL_DEVICE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/medical_device_matcher_en_6.2.0_3.2_1764374647975.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/medical_device_matcher_en_6.2.0_3.2_1764374647975.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

medical_device_matcher = TextMatcherInternalModel.pretrained("medical_device_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_medical_device")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    medical_device_matcher
])

text = """Patient has an insulin pump for diabetes management.
The pacemaker was implanted last year.
Using a CPAP machine for sleep apnea."""

data = spark.createDataFrame([[text]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

medical_device_matcher = medical.TextMatcherModel.pretrained("medical_device_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_medical_device")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    medical_device_matcher
])

text = """Patient has an insulin pump for diabetes management.
The pacemaker was implanted last year.
Using a CPAP machine for sleep apnea."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val medicalDeviceMatcher = TextMatcherInternalModel.pretrained("medical_device_matcher", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("matched_medical_device")
    .setMergeOverlapping(true)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    medicalDeviceMatcher
))

val data = Seq("""Patient has an insulin pump for diabetes management.
The pacemaker was implanted last year.
Using a CPAP machine for sleep apnea.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-------------------+-----+---+--------------+
|chunk              |begin|end|label         |
+-------------------+-----+---+--------------+
|insulin pump       |15   |26 |MEDICAL_DEVICE|
|pacemaker          |56   |64 |MEDICAL_DEVICE|
|CPAP machine       |99   |110|MEDICAL_DEVICE|
+-------------------+-----+---+--------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|medical_device_matcher|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[matched_medical_device]|
|Language:|en|
|Size:|947.5 KB|
|Case sensitive:|false|