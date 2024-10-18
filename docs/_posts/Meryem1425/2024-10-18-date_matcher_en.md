---
layout: model
title: Date Regex Matcher
author: John Snow Labs
name: date_matcher
date: 2024-10-18
tags: [en, licensed, clinical, regexmatcher, date]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.4
supported: true
annotator: RegexMatcherInternalModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model, extracts date entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/date_matcher_en_5.5.0_3.4_1729220800505.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/date_matcher_en_5.5.0_3.4_1729220800505.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setOutputCol("date_parser")

parserPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        date_regex_matcher
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, VIN 4Y1SL65848Z411439, VIN 1HGCM82633A123456 - VIN JH4KA7560MC012345 - VIN 5YJSA1E14HF123456
SSN #333-44-6666, Driver's license no: A334455B, plate 34NLP34. Lic: 12345As. Cert: 12345As
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com"""

result = model.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

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

val parserPipeline = new Pipeline().setStages(Array(
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

val results = parserPipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+----------+-----+---+-----+
|     chunk|begin|end|label|
+----------+-----+---+-----+
|2093-01-13|   38| 47| DATE|
|  01/13/93|  187|194| DATE|
|33-44-6666|  331|340| DATE|
+----------+-----+---+-----+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|date_matcher|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence]|
|Output Labels:|[entity_date]|
|Language:|en|
|Size:|5.2 KB|