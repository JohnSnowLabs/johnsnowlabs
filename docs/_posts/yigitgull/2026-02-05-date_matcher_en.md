---
layout: model
title: Date Regex Matcher
author: John Snow Labs
name: date_matcher
date: 2026-02-05
tags: [en, licensed, clinical, regexmatcher, date]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.3.0
spark_version: 3.4
supported: true
annotator: RegexMatcherInternalModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model, extracts date entities from clinical texts.

## Predicted Entities

`DATE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/date_matcher_en_6.3.0_3.4_1770292211176.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/date_matcher_en_6.3.0_3.4_1770292211176.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

date_regex_matcher = RegexMatcherInternalModel.pretrained("date_matcher","en","clinical/models") \
    .setInputCols(["sentence"]) \
    .setOutputCol("date_matcher")

matcherPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        date_regex_matcher
        ])


sample_text = """Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, VIN 4Y1SL65848Z411439, VIN 1HGCM82633A123456 - VIN JH4KA7560MC012345 - VIN 5YJSA1E14HF123456
SSN #333-44-6666, Driver's license no: A334455B, plate 34NLP34. Lic: 12345As. Cert: 12345As
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com"""

data = spark.createDataFrame([[sample_text]]).toDF("text")

result = matcherPipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val date_regex_matcher = RegexMatcherInternalModel.pretrained("date_matcher","en","clinical/models")
    .setInputCols("sentence")
    .setOutputCol("date_parser")

val matcherPipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        date_regex_matcher
))


val sample_text = """Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, VIN 4Y1SL65848Z411439, VIN 1HGCM82633A123456 - VIN JH4KA7560MC012345 - VIN 5YJSA1E14HF123456
SSN #333-44-6666, Driver's license no: A334455B, plate 34NLP34. Lic: 12345As. Cert: 12345As
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com"""

val data = Seq(sample_text).toDF("text")

val results = matcherPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
| chunk            |   begin |   end | label   |
|:-----------------|--------:|------:|:--------|
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
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[entity_date]|
|Language:|en|
|Size:|2.5 KB|