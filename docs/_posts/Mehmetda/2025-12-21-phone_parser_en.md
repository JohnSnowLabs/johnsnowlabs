---
layout: model
title: This model, extracts phone entities from clinical texts.
author: John Snow Labs
name: phone_parser
date: 2025-12-21
tags: [en, contextualparser, licensed, clinical, phone]
task: Contextual Parser
language: en
edition: Healthcare NLP 6.2.2
spark_version: 3.4
supported: true
annotator: ContextualParserModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model, extracts license number entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/phone_parser_en_6.2.2_3.0_1766345919330.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/phone_parser_en_6.2.2_3.0_1766345919330.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

phone_contextual_parser = ContextualParserModel.pretrained("phone_parser","en","clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("chunk_phone")

chunk_converter = ChunkConverter()\
    .setInputCols(["chunk_phone"])\
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
Email: medunites@firsthospital.com
Emergency contact phone: (555) 123-4567.
Additional phone number: (310) 987-6543."""

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

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

phone_contextual_parser = medical.ContextualParserModel.pretrained("phone_parser","en","clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("chunk_phone")

chunk_converter = medical.ChunkConverter()\
    .setInputCols(["chunk_phone"])\
    .setOutputCol("ner_chunk")

parserPipeline = nlp.Pipeline(stages=[
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
Email: medunites@firsthospital.com
Emergency contact phone: (555) 123-4567.
Additional phone number: (310) 987-6543."""

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
Email: medunites@firsthospital.com
Emergency contact phone: (555) 123-4567.
Additional phone number: (310) 987-6543."""

val data = Seq(sample_text).toDF("text")

val results = parserPipeline.fit(data).transform(data)


```
</div>

## Results

```bash


| chunk          |   begin |   end | label   |
|:---------------|--------:|------:|:--------|
| (818) 342-7353 |     292 |   305 | PHONE   |
| (818) 342-7354 |     316 |   329 | PHONE   |
| (818) 342-7353 |     386 |   399 | PHONE   |
| (555) 123-4567 |     462 |   475 | PHONE   |
| (310) 987-6543 |     503 |   516 | PHONE   |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|phone_parser|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token_doc]|
|Output Labels:|[entity_phone]|
|Language:|en|
|Size:|4.6 KB|
|Case sensitive:|false|
