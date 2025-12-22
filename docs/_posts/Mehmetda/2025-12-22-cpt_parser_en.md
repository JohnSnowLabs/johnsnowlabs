---
layout: model
title: CPT Contextual Parser Model
author: John Snow Labs
name: cpt_parser
date: 2025-12-22
tags: [en, contextualparser, licensed, clinical, cpt]
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

This model, extracts cpt entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/cpt_parser_en_6.2.2_3.4_1766433290399.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/cpt_parser_en_6.2.2_3.4_1766433290399.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

cpt_contextual_parser = ContextualParserModel.pretrained("cpt_contextual_parser","en","clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("chunk_zip")

chunk_converter = ChunkConverter()\
    .setInputCols(["chunk_zip"])\
    .setOutputCol("ner_chunk")

parserPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        cpt_contextual_parser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """The patient underwent procedure CPT 99213 for office visit. Laboratory tests were performed using CPT code 80053 for comprehensive metabolic panel. The radiology department billed CPT 93000 for electrocardiogram. Surgical procedure was coded as CPT 36415 for routine venipuncture. The final billing included CPT 85025 for complete blood count with differential."""

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

cpt_contextual_parser = medical.ContextualParserModel.pretrained("cpt_contextual_parser","en","clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("chunk_zip")

chunk_converter = medical.ChunkConverter()\
    .setInputCols(["chunk_zip"])\
    .setOutputCol("ner_chunk")

parserPipeline = nlp.Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        cpt_contextual_parser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """The patient underwent procedure CPT 99213 for office visit. Laboratory tests were performed using CPT code 80053 for comprehensive metabolic panel. The radiology department billed CPT 93000 for electrocardiogram. Surgical procedure was coded as CPT 36415 for routine venipuncture. The final billing included CPT 85025 for complete blood count with differential."""

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

val cpt_contextual_parser = ContextualParserModel.pretrained("cpt_contextual_parser","en","clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("chunk_zip")

val chunk_converter = new ChunkConverter()
    .setInputCols(Array("chunk_zip"))
    .setOutputCol("ner_chunk")

val parserPipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        tokenizer,
        cpt_contextual_parser,
        chunk_converter
        ))

val model = parserPipeline.fit(Seq(Array("")).toDS.toDF("text"))

val sample_text = """The patient underwent procedure CPT 99213 for office visit. Laboratory tests were performed using CPT code 80053 for comprehensive metabolic panel. The radiology department billed CPT 93000 for electrocardiogram. Surgical procedure was coded as CPT 36415 for routine venipuncture. The final billing included CPT 85025 for complete blood count with differential."""

val result = model.transform(Seq(Array(sample_text)).toDS.toDF("text"))

```
</div>

## Results

```bash


|   cpt_id |   begin |   end | label   |
|---------:|--------:|------:|:--------|
|    99213 |      36 |    41 | CPT     |
|    80053 |     107 |   112 | CPT     |
|    93000 |     184 |   189 | CPT     |
|    36415 |     249 |   254 | CPT     |
|    85025 |     312 |   317 | CPT     |




```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|cpt_parser|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token_doc]|
|Output Labels:|[entity_cpt]|
|Language:|en|
|Size:|4.4 KB|
|Case sensitive:|false|