---
layout: model
title: Plate Number Contextual Parser Model
author: John Snow Labs
name: plate_parser
date: 2024-10-23
tags: [clinical, contextualparser, plate, en, licensed]
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

This model, extracts plate number entities from clinical texts.

## Predicted Entities

`PLATE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/plate_parser_en_5.5.0_3.0_1729687324417.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/plate_parser_en_5.5.0_3.0_1729687324417.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

plate_contextual_parser = ContextualParserModel.pretrained("plate_parser","en","clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("chunk_plate")

chunk_converter = ChunkConverter() \
    .setInputCols(["chunk_plate"]) \
    .setOutputCol("ner_chunk")

parserPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        plate_contextual_parser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B, plates 34NLP34. LPN# 25ASD25
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

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

val plate_contextual_parser = ContextualParserModel.pretrained("plate_parser","en","clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("chunk_plate")

val chunk_converter = new ChunkConverter()
    .setInputCols("chunk_plate")
    .setOutputCol("ner_chunk")

val parserPipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        tokenizer,
        plate_contextual_parser,
        chunk_converter
))


val sample_text = """Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B, plates 34NLP34. LPN# 25ASD25
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

val data = Seq(sample_text).toDF("text")

val results = parserPipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-------+-----+---+-----+
|  chunk|begin|end|label|
+-------+-----+---+-----+
|34NLP34|  287|293|PLATE|
|25ASD25|  301|307|PLATE|
+-------+-----+---+-----+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|plate_parser|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[entity_plate]|
|Language:|en|
|Size:|9.3 KB|
|Case sensitive:|false|
