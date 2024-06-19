---
layout: model
title: State Regex Matcher
author: John Snow Labs
name: state_matcher
date: 2024-06-19
tags: [en, clinical, licensed, state, regexmatcher]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
annotator: RegexMatcherInternalModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts states in clinical notes using rule-based RegexMatcherInternal annotator.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/state_matcher_en_5.3.3_3.0_1718773178136.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/state_matcher_en_5.3.3_3.0_1718773178136.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

regex_matcher = RegexMatcherInternalModel.pretrained("state_matcher","en","clinical/models") \
    .setInputCols(["sentence"])\
    .setOutputCol("state_entity")\

regex_pipeline = Pipeline().setStages([
    documentAssembler,
    sentenceDetector,
    tokenizer,
    regex_matcher])

data = spark.createDataFrame([["""California is known for its beautiful beaches and vibrant entertainment industry centered.
The Grand Canyon in Arizona is one of the most stunning natural landmarks in the world."""]]).toDF("text")

result = regex_pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
	.setInputCols(Array("document"))
	.setOutputCol("sentence")

val tokenizer = new Tokenizer()
	.setInputCols(Array("sentence"))
	.setOutputCol("token")

val regex_matcher = RegexMatcherInternalModel.pretrained("state_matcher","en","clinical/models")
	.setInputCols(Array("sentence"))
	.setOutputCol("state_entity")
	.setMergeOverlapping(true)

val regex_pipeline = new Pipeline().setStages(Array(
		documentAssembler,
		sentenceDetector,
		tokenizer,
		regex_matcher))

val data = Seq(""""California is known for its beautiful beaches and vibrant entertainment industry centered.
The Grand Canyon in Arizona is one of the most stunning natural landmarks in the world.""").toDF("text")

val result = regex_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------+-----+---+-----+
|     chunk|begin|end|label|
+----------+-----+---+-----+
|California|    0|  9|STATE|
|   Arizona|  124|130|STATE|
+----------+-----+---+-----+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|state_matcher|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[regex_matches]|
|Language:|en|
|Size:|4.5 KB|