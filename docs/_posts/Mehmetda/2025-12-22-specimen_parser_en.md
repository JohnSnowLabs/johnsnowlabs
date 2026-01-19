---
layout: model
title: Specimen Contextual Parser Model
author: John Snow Labs
name: specimen_parser
date: 2025-12-22
tags: [en, contextualparser, licensed, clinical, specimen]
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

This model, extracts specimen entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/specimen_parser_en_6.2.2_3.4_1766431439076.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/specimen_parser_en_6.2.2_3.4_1766431439076.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

specimen_contextual_parser = ContextualParserModel.pretrained("specimen_parser","en","clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("chunk_zip")

chunk_converter = ChunkConverter()\
    .setInputCols(["chunk_zip"])\
    .setOutputCol("ner_chunk")

parserPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        specimen_contextual_parser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """Specimen ID: AB123-456789 was collected from the patient. The laboratory processed Specimen Number CD987654 yesterday. Use Specimen Code: XYZ12-3456 for tracking purposes. Sample was labeled as Specimen#EF34-789. Specimen No. GH56-123456 was sent to the pathology department."""

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

specimen_contextual_parser = medical.ContextualParserModel.pretrained("specimen_parser","en","clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("chunk_zip")

chunk_converter = medical.ChunkConverter()\
    .setInputCols(["chunk_zip"])\
    .setOutputCol("ner_chunk")

parserPipeline = nlp.Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        specimen_contextual_parser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """Specimen ID: AB123-456789 was collected from the patient. The laboratory processed Specimen Number CD987654 yesterday. Use Specimen Code: XYZ12-3456 for tracking purposes. Sample was labeled as Specimen#EF34-789. Specimen No. GH56-123456 was sent to the pathology department."""

result = model.transform(spark.createDataFrame([[sample_text]]).toDF("text"))



```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val specimen_contextual_parser = ContextualParserModel.pretrained("specimen_parser","en","clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("chunk_zip")

val chunk_converter = new ChunkConverter()
    .setInputCols(Array("chunk_zip"))
    .setOutputCol("ner_chunk")

val parserPipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        tokenizer,
        specimen_contextual_parser,
        chunk_converter
        ))

val model = parserPipeline.fit(Seq(Array("")).toDS.toDF("text"))

val sample_text = """Specimen ID: AB123-456789 was collected from the patient. The laboratory processed Specimen Number CD987654 yesterday. Use Specimen Code: XYZ12-3456 for tracking purposes. Sample was labeled as Specimen#EF34-789. Specimen No. GH56-123456 was sent to the pathology department."""

val result = model.transform(Seq(Array(sample_text)).toDS.toDF("text"))

```
</div>

## Results

```bash


| specimen_id   |   begin |   end | label    |
|:--------------|--------:|------:|:---------|
| AB123         |      13 |    18 | SPECIMEN |
| CD987654      |      99 |   107 | SPECIMEN |
| XYZ12-3456    |     138 |   148 | SPECIMEN |
| EF34-789      |     203 |   211 | SPECIMEN |
| GH56-123456   |     226 |   237 | SPECIMEN |



```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|specimen_parser|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token_doc]|
|Output Labels:|[entity_specimen]|
|Language:|en|
|Size:|4.4 KB|
|Case sensitive:|false|