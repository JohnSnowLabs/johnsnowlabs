---
layout: model
title: Country Text Matcher
author: John Snow Labs
name: country_matcher
date: 2024-10-23
tags: [en, licensed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.0
supported: true
annotator: TextMatcherInternalModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts countries in clinical notes using rule-based TextMatcherInternal annotator.

## Predicted Entities

`COUNTRY`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/country_matcher_en_5.5.0_3.0_1729683043606.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/country_matcher_en_5.5.0_3.0_1729683043606.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

text_matcher = TextMatcherInternalModel.pretrained("country_matcher","en","clinical/models") \
    .setInputCols(["document", "token"])\
    .setOutputCol("country")\
    .setMergeOverlapping(True)

mathcer_pipeline = Pipeline().setStages([
    documentAssembler,
    tokenizer,
    text_matcher])

data = spark.createDataFrame([["""Côte d’Ivoire
São Tomé & Príncipe
Åland Islands
This is Bahamas and the USAID in the USA here
Name: Johnson, Alice, Record date: 2093-03-22, MR: 846275.
Dr. Emily Brown, IP 192.168.1.1.
She is a 55-year-old female who was admitted to the Global Hospital for hip replacement on 03/22/93.
Patient's VIN: 2HGFA165X8H123456, SSN: 444-55-8888, Driver's license no: C789012D.
Phone: (212) 555-7890, 4321 Oak Street, New York, USA, E-MAIL: alice.johnson@example.com.
Patient has traveled to Japan, France, and Australia in the past year."""]]).toDF("text")

result = mathcer_pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")


val tokenizer = new Tokenizer()
	.setInputCols(Array("document"))
	.setOutputCol("token")

val text_matcher = TextMatcherInternalModel.pretrained("country_matcher","en","clinical/models")
	.setInputCols(Array("document","token"))
	.setOutputCol("country")
	.setMergeOverlapping(true)

val matcher_pipeline = new Pipeline().setStages(Array(
		documentAssembler,
		tokenizer,
		text_matcher))

val data = Seq("""Côte d’Ivoire
São Tomé & Príncipe
Åland Islands
This is Bahamas and the USAID in the USA here
Name: Johnson, Alice, Record date: 2093-03-22, MR: 846275.
Dr. Emily Brown, IP 192.168.1.1.
She is a 55-year-old female who was admitted to the Global Hospital for hip replacement on 03/22/93.
Patient's VIN: 2HGFA165X8H123456, SSN: 444-55-8888, Driver's license no: C789012D.
Phone: (212) 555-7890, 4321 Oak Street, New York, USA, E-MAIL: alice.johnson@example.com.
Patient has traveled to Japan, France, and Australia in the past year.""").toDF("text")

val result = matcher_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------------+-----+---+-------+
|chunk              |begin|end|label  |
+-------------------+-----+---+-------+
|Côte d’Ivoire      |0    |12 |Country|
|São Tomé & Príncipe|14   |32 |Country|
|Åland Islands      |34   |46 |Country|
|Bahamas            |56   |62 |Country|
|USA                |85   |87 |Country|
|USA                |420  |422|Country|
|Japan              |484  |488|Country|
|France             |491  |496|Country|
|Australia          |503  |511|Country|
+-------------------+-----+---+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|country_matcher|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[country]|
|Language:|en|
|Size:|10.4 KB|
|Case sensitive:|false|
