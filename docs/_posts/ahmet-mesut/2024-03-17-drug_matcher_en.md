---
layout: model
title: Drug Text Matcher
author: John Snow Labs
name: drug_matcher
date: 2024-03-17
tags: [en, licensed, drug, textmatcher, clinical]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.0
supported: true
annotator: TextMatcherInternalModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts medication entities in clinical notes using rule-based `TextMatcherInternal` annotator.

## Predicted Entities

`DRUG`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/drug_matcher_en_5.3.0_3.0_1710705381198.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/drug_matcher_en_5.3.0_3.0_1710705381198.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
	
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

text_matcher = TextMatcherInternalModel.pretrained("drug_matcher","en","clinical/models") \
    .setInputCols(["document", "token"])\
    .setOutputCol("matched_text")\

mathcer_pipeline = Pipeline().setStages([
    documentAssembler,
    tokenizer,
    text_matcher])

data = spark.createDataFrame([["John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD on 2023-12-01."]]).toDF("text")

matcher_model = mathcer_pipeline.fit(data)
result = matcher_model.transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols(Array("document"))
    .setOutputCol("token")

val text_matcher = TextMatcherInternalModel.pretrained("drug_matcher","en","clinical/models")
    .setInputCols(Array("document","token"))
    .setOutputCol("matched_text")

val mathcer_pipeline = new Pipeline()
    .setStages(Array(
    documentAssembler,
    tokenizer,
    text_matcher))

val data = Seq("John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD on 2023-12-01.") .toDF("text")

val matcher_model = mathcer_pipeline.fit(data)
val result = matcher_model.transform(data)
```
</div>

## Results

```bash
+------------+-----+---+-----+
|       chunk|begin|end|label|
+------------+-----+---+-----+
|     aspirin|   25| 31| DRUG|
| paracetamol|   69| 79| DRUG|
| amoxicillin|  109|119| DRUG|
|lansoprazole|  144|155| DRUG|
+------------+-----+---+-----+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|drug_matcher|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[matched_text]|
|Language:|en|
|Size:|3.6 MB|
|Case sensitive:|false|
