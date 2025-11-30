---
layout: model
title: Test Result Contextual Parser
author: John Snow Labs
name: test_result_parser
date: 2025-11-30
tags: [parser, test_result, en, licensed, clinical, contextual_parser]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.2
supported: true
annotator: ContextualParserModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a ContextualParser model that identifies test result entities in clinical text. It recognizes result descriptors including positive, negative, normal, abnormal, elevated, low, high, decreased, increased, and more.

## Predicted Entities

`TEST_RESULT`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/test_result_parser_en_6.2.0_3.2_1764469126580.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/test_result_parser_en_6.2.0_3.2_1764469126580.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

test_result_parser = ContextualParserModel.pretrained("test_result_parser", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("parsed_test_result")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    test_result_parser
])

text = """Laboratory findings showed hemoglobin was low and white blood cell count was elevated. The COVID-19 test came back positive. Liver function tests were normal, but the glucose level was abnormal."""

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

test_result_parser = medical.ContextualParserModel.pretrained("test_result_parser", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("parsed_test_result")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    test_result_parser
])

text = """Laboratory findings showed hemoglobin was low and white blood cell count was elevated. The COVID-19 test came back positive. Liver function tests were normal, but the glucose level was abnormal."""

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

val testResultParser = ContextualParserModel.pretrained("test_result_parser", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("parsed_test_result")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    testResultParser
))

val data = Seq("""Laboratory findings showed hemoglobin was low and white blood cell count was elevated. The COVID-19 test came back positive. Liver function tests were normal, but the glucose level was abnormal.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+--------+-----+---+-----------+
|chunk   |begin|end|label      |
+--------+-----+---+-----------+
|low     |42   |44 |TEST_RESULT|
|elevated|77   |84 |TEST_RESULT|
|positive|115  |122|TEST_RESULT|
|normal  |151  |156|TEST_RESULT|
|abnormal|185  |192|TEST_RESULT|
+--------+-----+---+-----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|test_result_parser|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[chunk_test_result]|
|Language:|en|
|Size:|18.9 KB|
|Case sensitive:|false|
