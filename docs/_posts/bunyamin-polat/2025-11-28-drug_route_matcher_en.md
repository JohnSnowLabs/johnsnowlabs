---
layout: model
title: Drug Route Text Matcher
author: John Snow Labs
name: drug_route_matcher
date: 2025-11-28
tags: [matcher, drug_route, en, licensed, clinical]
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

This is a TextMatcher model that can identify drug route entities in clinical text. It recognizes various administration routes including oral, intravenous, subcutaneous, intramuscular, topical, sublingual, rectal, transdermal, intranasal, inhaled, and many more drug delivery routes.

## Predicted Entities

`DRUG_ROUTE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/drug_route_matcher_en_6.2.0_3.2_1764374292789.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/drug_route_matcher_en_6.2.0_3.2_1764374292789.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

drug_route_matcher = TextMatcherInternalModel.pretrained("drug_route_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_drug_route")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    drug_route_matcher
])

text = """Patient was prescribed aspirin 500mg tablet orally twice daily. Administer the medication intravenously for rapid effect. The injection should be given subcutaneously."""

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

drug_route_matcher = medical.TextMatcherModel.pretrained("drug_route_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_drug_route")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    drug_route_matcher
])

text = """Patient was prescribed aspirin 500mg tablet orally twice daily. Administer the medication intravenously for rapid effect. The injection should be given subcutaneously."""

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

val drugRouteMatcher = TextMatcherInternalModel.pretrained("drug_route_matcher", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("matched_drug_route")
    .setMergeOverlapping(true)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    drugRouteMatcher
))

val data = Seq("""Patient was prescribed aspirin 500mg tablet orally twice daily. Administer the medication intravenously for rapid effect. The injection should be given subcutaneously.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+---------------+-----+---+----------+
|chunk          |begin|end|label     |
+---------------+-----+---+----------+
|orally         |44   |49 |DRUG_ROUTE|
|intravenously  |96   |108|DRUG_ROUTE|
|subcutaneously |168  |181|DRUG_ROUTE|
+---------------+-----+---+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|drug_route_matcher|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[matched_drug_route]|
|Language:|en|
|Size:|939.6 KB|
|Case sensitive:|false|
