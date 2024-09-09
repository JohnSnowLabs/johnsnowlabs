---
layout: model
title: State Text Matcher
author: John Snow Labs
name: state_matcher
date: 2024-09-09
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



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/state_matcher_en_5.4.1_3.0_1725886378937.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/state_matcher_en_5.4.1_3.0_1725886378937.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

data = spark.createDataFrame([["""California is known for its beautiful beaches and vibrant entertainment industry centered.
The Grand Canyon in Arizona is one of the most stunning natural landmarks in the world.
AL 123456!, TX 54321-4444, AL :55555-4444, JHBJHBJHB 12345-4444, MK 11111, TX 12345
'MD Connect Call 11:59pm 2/16/69 from Dr . Hale at Senior Care Clinic Queen Creek , SD regarding Terri Bird .',
 'Arroyo Grande , KS , 19741-6273',
 'Oroville , AL 89389 48423663',
 'Red Springs , WA 77286',
 'Lake Pocotopaug , ME 15424',
 'Queen Creek , SD 89544',
 'Goins is a 27 yo male with history of type I DM formally without regular medical care who was visiting family in Maryland and had sudden witnessed seizure activity in late August .',
 'Whitewater , NC 13662 10776605'"""]]).toDF("text")

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

val data = Seq("""California is known for its beautiful beaches and vibrant entertainment industry centered.
The Grand Canyon in Arizona is one of the most stunning natural landmarks in the world.
AL 123456!, TX 54321-4444, AL :55555-4444, JHBJHBJHB 12345-4444, MK 11111, TX 12345
'MD Connect Call 11:59pm 2/16/69 from Dr . Hale at Senior Care Clinic Queen Creek , SD regarding Terri Bird .',
 'Arroyo Grande , KS , 19741-6273',
 'Oroville , AL 89389 48423663',
 'Red Springs , WA 77286',
 'Lake Pocotopaug , ME 15424',
 'Queen Creek , SD 89544',
 'Goins is a 27 yo male with history of type I DM formally without regular medical care who was visiting family in Maryland and had sudden witnessed seizure activity in late August .',
 'Whitewater , NC 13662 10776605'""").toDF("text")

val result = mathcer_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------+-----+---+-----+
|chunk     |begin|end|label|
+----------+-----+---+-----+
|California|0    |9  |STATE|
|Arizona   |111  |117|STATE|
|AL        |179  |180|STATE|
|TX        |191  |192|STATE|
|AL        |206  |207|STATE|
|TX        |254  |255|STATE|
|SD        |347  |348|STATE|
|KS        |393  |394|STATE|
|AL        |424  |425|STATE|
|WA        |460  |461|STATE|
|ME        |491  |492|STATE|
|SD        |518  |519|STATE|
|Maryland  |644  |651|STATE|
|NC        |729  |730|STATE|
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
|Size:|6.9 KB|
|Case sensitive:|true|