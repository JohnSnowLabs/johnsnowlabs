---
layout: model
title: Age Contextual Parser Model
author: John Snow Labs
name: age_parser
date: 2024-10-18
tags: [en, licensed, clinical, contextualparser, age]
task: Contextual Parser
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.4
supported: true
annotator: ContextualParserModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model, extracts age entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/age_parser_en_5.5.0_3.4_1729219700932.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/age_parser_en_5.5.0_3.4_1729219700932.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

age_contextual_parser = ContextualParserModel.pretrained("age_parser","en","clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("chunk_age")

chunk_converter = ChunkConverter() \
    .setInputCols(["chunk_age"]) \
    .setOutputCol("ner_chunk")

parserPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        age_contextual_parser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, VIN 4Y1SL65848Z411439, VIN 1HGCM82633A123456 - VIN JH4KA7560MC012345 - VIN 5YJSA1E14HF123456
SSN #333-44-6666, Driver's license no: A334455B, plate 34NLP34. Lic: 12345As. Cert: 12345As
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com.

A 28 year old female with a history of gestational diabetes mellitus diagnosed 8 years ago.
3 years ago, he reported an episode of HTG-induced pancreatitis . 5 months old boy with repeated concussions."""

result = model.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val age_contextual_parser = ContextualParserModel.pretrained("age_parser","en","clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("chunk_age")

val chunk_converter = new ChunkConverter()
    .setInputCols("chunk_age")
    .setOutputCol("ner_chunk")

val parserPipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        tokenizer,
        age_contextual_parser,
        chunk_converter
))


val sample_text = """Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, VIN 4Y1SL65848Z411439, VIN 1HGCM82633A123456 - VIN JH4KA7560MC012345 - VIN 5YJSA1E14HF123456
SSN #333-44-6666, Driver's license no: A334455B, plate 34NLP34. Lic: 12345As. Cert: 12345As
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com.

A 28 year old female with a history of gestational diabetes mellitus diagnosed 8 years ago.
3 years ago, he reported an episode of HTG-induced pancreatitis . 5 months old boy with repeated concussions."""

val data = Seq(sample_text).toDF("text")

val results = parserPipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----+-----+---+-----+
|chunk|begin|end|label|
+-----+-----+---+-----+
|   60|  119|120|  AGE|
|   28|  501|502|  AGE|
|    5|  657|657|  AGE|
+-----+-----+---+-----+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|age_parser|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[entity_age]|
|Language:|en|
|Size:|9.4 KB|
|Case sensitive:|false|
