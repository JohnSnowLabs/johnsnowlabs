---
layout: model
title: State Text Matcher
author: John Snow Labs
name: state_matcher
date: 2024-09-11
tags: [en, licensed, clinical, state, textmatcher]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.0
supported: true
annotator: TextMatcherInternalModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts US state entities in clinical notes using a rule-based TextMatcherInternal annotator.

## Predicted Entities

`STATE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/state_matcher_en_5.4.1_3.0_1726051642401.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/state_matcher_en_5.4.1_3.0_1726051642401.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

text_matcher = TextMatcherInternalModel.pretrained("state_matcher","en","clinical/models") \
    .setInputCols(["sentence", "token"])\
    .setOutputCol("state_name")\
    .setMergeOverlapping(True)

mathcer_pipeline = Pipeline().setStages([
    documentAssembler,
    sentenceDetector,
    tokenizer,
    text_matcher])

data = spark.createDataFrame([["""Dr. Sarah Mitchell, a renowned oncologist from California, treated a patient diagnosed with lung cancer. The patient, originally from Texas, had traveled across several states seeking specialized care. After consulting with various doctors in Nevada and Arizona, the decision was made to transfer the patient to California for advanced treatment options. During a conference in New York, Dr. Mitchell presented the case to her colleagues from Florida and Illinois, discussing the innovative techniques used in the surgery. The patient’s recovery has been closely monitored, with follow-up appointments scheduled in both  California and Texas to ensure continued care and support."""]]).toDF("text")

result = mathcer_pipeline.fit(data).transform(data)
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

val text_matcher = TextMatcherInternalModel.pretrained("state_matcher","en","clinical/models")
	.setInputCols(Array("sentence","token"))
	.setOutputCol("state_name")
	.setMergeOverlapping(true)

val mathcer_pipeline = new Pipeline().setStages(Array(
		documentAssembler,
		sentenceDetector,
		tokenizer,
		text_matcher))

val data = Seq("""Dr. Sarah Mitchell, a renowned oncologist from California, treated a patient diagnosed with lung cancer. The patient, originally from Texas, had traveled across several states seeking specialized care. After consulting with various doctors in Nevada and Arizona, the decision was made to transfer the patient to California for advanced treatment options. During a conference in New York, Dr. Mitchell presented the case to her colleagues from Florida and Illinois, discussing the innovative techniques used in the surgery. The patient’s recovery has been closely monitored, with follow-up appointments scheduled in both  California and Texas to ensure continued care and support.""").toDF("text")

val result = mathcer_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------+-----+---+-----+
|chunk     |begin|end|label|
+----------+-----+---+-----+
|California|47   |56 |STATE|
|Texas     |134  |138|STATE|
|Nevada    |243  |248|STATE|
|Arizona   |254  |260|STATE|
|California|312  |321|STATE|
|New York  |378  |385|STATE|
|Florida   |443  |449|STATE|
|Illinois  |455  |462|STATE|
|California|621  |630|STATE|
|Texas     |636  |640|STATE|
+----------+-----+---+-----+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|state_matcher|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[entity_state]|
|Language:|en|
|Size:|6.3 KB|
|Case sensitive:|true|
