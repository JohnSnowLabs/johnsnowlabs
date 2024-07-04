---
layout: model
title: Phone Regex Matcher
author: John Snow Labs
name: phone_matcher
date: 2024-06-19
tags: [en, licensed, clinical, phone, regexmatcher]
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

This model extracts phone entities in clinical notes using rule-based RegexMatcherInternal annotator.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/phone_matcher_en_5.3.3_3.0_1718771598418.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/phone_matcher_en_5.3.3_3.0_1718771598418.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

regex_matcher = RegexMatcherInternalModel.pretrained("phone_matcher","en","clinical/models") \
    .setInputCols(["sentence"])\
    .setOutputCol("phone_entity")\

regex_pipeline = Pipeline().setStages([
    documentAssembler,
    sentenceDetector,
    tokenizer,
    regex_matcher])

data = spark.createDataFrame([["""Record date :2093-01-13,  David Hale, M.D. IP 203.120.223.13.
ID: 1231511863, The driver's license no:A334455B and e-mail: hale@gmail.com .
PCP : Oliveira, 25 years-old, Jake 5 year old, Record date : 2079-11-09.
Cocke County Baptist Hospital , 0295 Keats Street, 12345, TX 55555-4444. Phone: (818) 342-7353 Fax No.: (818) 342-7354, SSN# 332255677, The other is ssN: 333-44-6666."""]]).toDF("text")

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

val regex_matcher = RegexMatcherInternalModel.pretrained("phone_matcher","en","clinical/models")
	.setInputCols(Array("sentence"))
	.setOutputCol("phone_entity")
	.setMergeOverlapping(true)

val regex_pipeline = new Pipeline().setStages(Array(
		documentAssembler,
		sentenceDetector,
		tokenizer,
		regex_matcher))

val data = Seq("""Record date :2093-01-13,  David Hale, M.D. IP 203.120.223.13.
ID: 1231511863, The driver's license no:A334455B and e-mail: hale@gmail.com .
PCP : Oliveira, 25 years-old, Jake 5 year old, Record date : 2079-11-09.
Cocke County Baptist Hospital , 0295 Keats Street, 12345, TX 55555-4444. Phone: (818) 342-7353 Fax No.: (818) 342-7354, SSN# 332255677, The other is ssN: 333-44-6666.""").toDF("text")

val result = regex_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------+-----+---+-----+
|         chunk|begin|end|label|
+--------------+-----+---+-----+
|(818) 342-7353|  293|306|PHONE|
|(818) 342-7354|  317|330|PHONE|
+--------------+-----+---+-----+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|phone_matcher|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence]|
|Output Labels:|[entity_phone]|
|Language:|en|
|Size:|6.9 KB|
