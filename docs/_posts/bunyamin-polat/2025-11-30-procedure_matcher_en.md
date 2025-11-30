---
layout: model
title: Procedure Text Matcher
author: John Snow Labs
name: procedure_matcher
date: 2025-11-30
tags: [matcher, procedure, en, licensed, clinical, text_matcher]
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

This is a TextMatcher model that identifies medical procedure entities in clinical text. It recognizes procedures including colonoscopy, biopsy, MRI, CT scan, echocardiogram, endoscopy, blood transfusion, and more.

## Predicted Entities

`PROCEDURE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/procedure_matcher_en_6.2.0_3.2_1764466584376.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/procedure_matcher_en_6.2.0_3.2_1764466584376.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

procedure_matcher = TextMatcherInternalModel.pretrained("procedure_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_procedure")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    procedure_matcher
])

text = """The patient presented with gastrointestinal symptoms. A colonoscopy was performed which revealed a suspicious lesion, and a biopsy was obtained for pathological examination."""

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

procedure_matcher = medical.TextMatcherModel.pretrained("procedure_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_procedure")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    procedure_matcher
])

text = """The patient presented with gastrointestinal symptoms. A colonoscopy was performed which revealed a suspicious lesion, and a biopsy was obtained for pathological examination."""

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

val procedureMatcher = TextMatcherInternalModel.pretrained("procedure_matcher", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("matched_procedure")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    procedureMatcher
))

val data = Seq("""The patient presented with gastrointestinal symptoms. A colonoscopy was performed which revealed a suspicious lesion, and a biopsy was obtained for pathological examination.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------+-----+---+---------+
|chunk      |begin|end|label    |
+-----------+-----+---+---------+
|colonoscopy|54   |64 |PROCEDURE|
|biopsy     |113  |118|PROCEDURE|
+-----------+-----+---+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|procedure_matcher|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[matched_procedure]|
|Language:|en|
|Size:|972.9 KB|
|Case sensitive:|false|