---
layout: model
title: Drug Form Text Matcher
author: John Snow Labs
name: drug_form_matcher
date: 2025-11-28
tags: [matcher, drug_form, en, licensed, clinical]
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

This is a TextMatcher model that can identify drug form entities in clinical text.It recognizes various pharmaceutical forms including tablet, capsule, injection, cream, solution,
spray, patch, drops, suppository, nebulizer, and many more drug delivery forms.

## Predicted Entities

`DRUG_FORM`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/drug_form_matcher_en_6.2.0_3.2_1764373917954.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/drug_form_matcher_en_6.2.0_3.2_1764373917954.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

drug_form_matcher = TextMatcherInternalModel.pretrained("drug_form_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_drug_form")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    drug_form_matcher
])

text = """Patient was prescribed aspirin 500mg tablet orally twice daily.
Also given ibuprofen capsule for pain relief.
The doctor recommended insulin injection subcutaneously."""


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

drug_form_matcher = medical.TextMatcherModel.pretrained("drug_form_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_drug_form")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    drug_form_matcher
])

text = """Patient was prescribed aspirin 500mg tablet orally twice daily.
Also given ibuprofen capsule for pain relief.
The doctor recommended insulin injection subcutaneously."""

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

val drugFormMatcher = TextMatcherInternalModel.pretrained("drug_form_matcher", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("matched_drug_form")
    .setMergeOverlapping(true)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    drugFormMatcher
))

val data = Seq("""Patient was prescribed aspirin 500mg tablet orally twice daily.
Also given ibuprofen capsule for pain relief.
The doctor recommended insulin injection subcutaneously.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------------+-----+---+---------+
|            chunk|begin|end|    label|
+-----------------+-----+---+---------+
|           tablet|   37| 42|DRUG_FORM|
|          capsule|   85| 91|DRUG_FORM|
|        injection|  141|149|DRUG_FORM|
|            cream|  181|185|DRUG_FORM|
|    oral solution|  214|226|DRUG_FORM|
|      Suppository|  296|306|DRUG_FORM|
|      Nasal spray|  387|397|DRUG_FORM|
|Transdermal patch|  415|431|DRUG_FORM|
+-----------------+-----+---+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|drug_form_matcher|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[matched_drug_form]|
|Language:|en|
|Size:|934.4 KB|
|Case sensitive:|false|