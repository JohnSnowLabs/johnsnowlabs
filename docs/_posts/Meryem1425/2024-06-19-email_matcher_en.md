---
layout: model
title: Email Regex Matcher
author: John Snow Labs
name: email_matcher
date: 2024-06-19
tags: [en, clinical, licensed, regexmatcher]
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

This model extracts emails in clinical notes using rule-based RegexMatcherInternal annotator.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/email_matcher_en_5.3.3_3.0_1718772843289.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/email_matcher_en_5.3.3_3.0_1718772843289.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

regex_matcher = RegexMatcherInternalModel.pretrained("email_matcher","en","clinical/models") \
    .setInputCols(["sentence"])\
    .setOutputCol("email_entity")\

regex_pipeline = Pipeline().setStages([
    documentAssembler,
    sentenceDetector,
    tokenizer,
    regex_matcher])

data = spark.createDataFrame([["""ID: 1231511863, The driver's license no:A334455B, the SSN:324598674 and jadjada_adald19@msku.edu.tr, mail: afakfl_lakf19@yahoo.com, e-mail: hale@gmail.com .
EMAIL: afakfl_lakf19@yahoo.com, E-mail: hale@gmail.com ."""]]).toDF("text")

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

val regex_matcher = RegexMatcherInternalModel.pretrained("email_matcher","en","clinical/models")
	.setInputCols(Array("sentence"))
	.setOutputCol("email_entity")
	.setMergeOverlapping(true)

val regex_pipeline = new Pipeline().setStages(Array(
		documentAssembler,
		sentenceDetector,
		tokenizer,
		regex_matcher))

val data = Seq(""""ID: 1231511863, The driver's license no:A334455B, the SSN:324598674 and jadjada_adald19@msku.edu.tr, mail: afakfl_lakf19@yahoo.com, e-mail: hale@gmail.com .
EMAIL: afakfl_lakf19@yahoo.com, E-mail: hale@gmail.com .""").toDF("text")

val result = regex_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------------------------+-----+---+-----+
|                      chunk|begin|end|label|
+---------------------------+-----+---+-----+
|jadjada_adald19@msku.edu.tr|   72| 98|EMAIL|
|    afakfl_lakf19@yahoo.com|  107|129|EMAIL|
|             hale@gmail.com|  140|153|EMAIL|
|    afakfl_lakf19@yahoo.com|  164|186|EMAIL|
|             hale@gmail.com|  197|210|EMAIL|
+---------------------------+-----+---+-----+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|email_matcher|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence]|
|Output Labels:|[email]|
|Language:|en|
|Size:|6.6 KB|
