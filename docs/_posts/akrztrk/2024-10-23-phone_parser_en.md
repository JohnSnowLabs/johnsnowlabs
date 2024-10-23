---
layout: model
title: Phone Contextual Parser Model
author: John Snow Labs
name: phone_parser
date: 2024-10-23
tags: [en, licensed, clinical, contextualparser, phone]
task: Contextual Parser
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.0
supported: true
annotator: ContextualParserModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model, extracts phone entities from clinical texts.

## Predicted Entities

`PHONE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/phone_parser_en_5.5.0_3.0_1729685040235.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/phone_parser_en_5.5.0_3.0_1729685040235.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

phone_contextual_parser = ContextualParserModel.pretrained("phone_parser","en","clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("chunk_phone")

chunk_converter = ChunkConverter() \
    .setInputCols(["chunk_phone"]) \
    .setOutputCol("ner_chunk")

parserPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        phone_contextual_parser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """Record date :2093-01-13, David Hale, M.D. IP 203.120.223.13.
ID: 1231511863, The driver's license no:A334455B and e-mail: hale@gmail.com .
PCP : Oliveira, 25 years-old, Jake 5 year old, Record date : 2079-11-09.
Cocke County Baptist Hospital , 0295 Keats Street, 12345, TX 55555-4444. Phone: (818) 342-7353 Fax No.: (818) 342-7354, SSN# 332255677, The other is ssN: 333-44-6666.
Phone: (818) 342-7353.
Email: medunites@firsthospital.com"""

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

val phone_contextual_parser = ContextualParserModel.pretrained("phone_parser","en","clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("chunk_phone")

val chunk_converter = new ChunkConverter()
    .setInputCols("chunk_phone")
    .setOutputCol("ner_chunk")

val parserPipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        tokenizer,
        phone_contextual_parser,
        chunk_converter
))


val sample_text = """Record date :2093-01-13, David Hale, M.D. IP 203.120.223.13.
ID: 1231511863, The driver's license no:A334455B and e-mail: hale@gmail.com .
PCP : Oliveira, 25 years-old, Jake 5 year old, Record date : 2079-11-09.
Cocke County Baptist Hospital , 0295 Keats Street, 12345, TX 55555-4444. Phone: (818) 342-7353 Fax No.: (818) 342-7354, SSN# 332255677, The other is ssN: 333-44-6666.
Phone: (818) 342-7353.
Email: medunites@firsthospital.com"""

val data = Seq(sample_text).toDF("text")

val results = parserPipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+--------------+-----+---+-----+
|         chunk|begin|end|label|
+--------------+-----+---+-----+
|(818) 342-7353|  292|305|PHONE|
|(818) 342-7354|  316|329|PHONE|
|(818) 342-7353|  386|399|PHONE|
+--------------+-----+---+-----+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|phone_parser|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[entity_phone]|
|Language:|en|
|Size:|9.4 KB|
|Case sensitive:|false|