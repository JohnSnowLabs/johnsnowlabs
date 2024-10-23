---
layout: model
title: Medical Record Contextual Parser Model
author: John Snow Labs
name: medical_record_parser
date: 2024-10-23
tags: [en, licensed, clinical, contextualparser, medical_record]
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

This model, extracts medical record entities from clinical texts.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/medical_record_parser_en_5.5.0_3.0_1729684624863.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/medical_record_parser_en_5.5.0_3.0_1729684624863.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

medical_record_contextual_parser = ContextualParserModel.pretrained("medical_record_parser","en","clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("chunk_medical_record")

chunk_converter = ChunkConverter() \
    .setInputCols(["chunk_medical_record"]) \
    .setOutputCol("ner_chunk")

parserPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        medical_record_contextual_parser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """Month DD, YYYY
XYZ
RE: ABC
MEDICAL RECORD#: 12332
MRN: 1233567
Dear Dr. XYZ:

I saw ABC back in Neuro-Oncology Clinic today."""

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

val medical_record_contextual_parser = ContextualParserModel.pretrained("medical_record_parser","en","clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("chunk_medical_record")

val chunk_converter = new ChunkConverter()
    .setInputCols("chunk_medical_record")
    .setOutputCol("ner_chunk")

val parserPipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        tokenizer,
        medical_record_contextual_parser,
        chunk_converter
))


val sample_text = """Month DD, YYYY
XYZ
RE: ABC
MEDICAL RECORD#: 12332
MRN: 1233567
Dear Dr. XYZ:

I saw ABC back in Neuro-Oncology Clinic today."""

val data = Seq(sample_text).toDF("text")

val results = parserPipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-------+-----+---+-------------+
|  chunk|begin|end|        label|
+-------+-----+---+-------------+
|  12332|   44| 48|MEDICALRECORD|
|1233567|   55| 61|MEDICALRECORD|
+-------+-----+---+-------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|medical_record_parser|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[med_code]|
|Language:|en|
|Size:|9.3 KB|
|Case sensitive:|false|