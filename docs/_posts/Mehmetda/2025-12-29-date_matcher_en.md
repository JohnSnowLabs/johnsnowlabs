---
layout: model
title: Date Contextual Parser Model
author: John Snow Labs
name: date_matcher
date: 2025-12-29
tags: [en, contextualparser, licensed, date]
task: Contextual Parser
language: en
edition: Healthcare NLP 6.2.2
spark_version: 3.4
supported: true
annotator: RegexMatcherInternalModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model, extracts dates entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/date_matcher_en_6.2.2_3.4_1767002826514.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/date_matcher_en_6.2.2_3.4_1767002826514.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

token_doc = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token_doc")

date_matcher = RegexMatcherInternalModel.pretrained("date_matcher","en","clinical/models")\
    .setInputCols(["document", "token_doc"])\
    .setOutputCol("entity_country")\
    .setCaseSensitive(False)

parserPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        token_doc,
        date_matcher
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """Record date : 2081-01-04
DB : 11.04.1962
DT : 12-03-1978
DOD : 10.25.23

SOCIAL HISTORY:
She was born on Nov 04, 1962 in London and got married on 04/05/1979. When she got pregnant on 15 May 1079, the doctor wanted to verify her DOB was November 4, 1962. Her date of birth was confirmed to be 11-04-1962, the patient is 45 years old on 25 Sep 2007.

PROCEDURES:
Patient was evaluated on 1988-03-15 for allergies. She was seen by the endocrinology service and she was discharged on 9/23/1988.

MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on August 14, 2007, and her INR was 2.3."""
result = model.transform(spark.createDataFrame([[sample_text]]).toDF("text"))


```

{:.jsl-block}
```python


document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

token_doc = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token_doc")

date_matcher = medical.RegexMatcherInternalModel.pretrained("date_matcher","en","clinical/models")\
    .setInputCols(["document", "token_doc"])\
    .setOutputCol("entity_country")\
    .setCaseSensitive(False)

parserPipeline = nlp.Pipeline(stages=[
        document_assembler,
        sentence_detector,
        token_doc,
        date_matcher
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """Record date : 2081-01-04
DB : 11.04.1962
DT : 12-03-1978
DOD : 10.25.23

SOCIAL HISTORY:
She was born on Nov 04, 1962 in London and got married on 04/05/1979. When she got pregnant on 15 May 1079, the doctor wanted to verify her DOB was November 4, 1962. Her date of birth was confirmed to be 11-04-1962, the patient is 45 years old on 25 Sep 2007.

PROCEDURES:
Patient was evaluated on 1988-03-15 for allergies. She was seen by the endocrinology service and she was discharged on 9/23/1988.

MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on August 14, 2007, and her INR was 2.3."""
result = model.transform(spark.createDataFrame([[sample_text]]).toDF("text"))


```
```scala

val documentAssembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
	.setInputCols(Array("document"))
	.setOutputCol("sentence")

val tokenDoc = new Tokenizer()
	.setInputCols(Array("document"))
	.setOutputCol("token_doc")

val dateMatcher = RegexMatcherInternalModel.pretrained("date_matcher","en","clinical/models")
	.setInputCols(Array("document", "token_doc"))
	.setOutputCol("entity_country")
	.setCaseSensitive(false)

val parserPipeline = new Pipeline().setStages(Array(
		documentAssembler,
		sentenceDetector,
		tokenDoc,
		dateMatcher
		))

val model = parserPipeline.fit(Seq("").toDF("text"))

val sampleText = """Record date : 2081-01-04
DB : 11.04.1962
DT : 12-03-1978
DOD : 10.25.23

SOCIAL HISTORY:
She was born on Nov 04, 1962 in London and got married on 04/05/1979. When she got pregnant on 15 May 1079, the doctor wanted to verify her DOB was November 4, 1962. Her date of birth was confirmed to be 11-04-1962, the patient is 45 years old on 25 Sep 2007.

PROCEDURES:
Patient was evaluated on 1988-03-15 for allergies. She was seen by the endocrinology service and she was discharged on 9/23/1988.

MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on August 14, 2007, and her INR was 2.3."""

val result = model.transform(Seq(sampleText).toDF("text"))

```
</div>

## Results

```bash


| chunk            |   begin |   end | label   |
|------------------|---------|-------|---------|
| 2081-01-04       |      15 |    24 | DATE    |
| 11.04.1962       |      31 |    40 | DATE    |
| 12-03-1978       |      47 |    56 | DATE    |
| 10.25.23         |      64 |    71 | DATE    |
| Nov 04, 1962     |     106 |   117 | DATE    |
| 04/05/1979       |     148 |   157 | DATE    |
| 15 May           |     185 |   190 | DATE    |
| November 4, 1962 |     238 |   253 | DATE    |
| 11-04-1962       |     294 |   303 | DATE    |
| 25 Sep 2007      |     337 |   347 | DATE    |
| 1988-03-15       |     388 |   397 | DATE    |
| 9/23/1988        |     482 |   490 | DATE    |
| August 14, 2007  |     546 |   560 | DATE    |




```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|date_matcher|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[entity_date]|
|Language:|en|
|Size:|2.5 KB|