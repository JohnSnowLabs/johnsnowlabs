---
layout: model
title: Disease Named Entity Recognition Italian (Base, ONNX)
author: John Snow Labs
name: bert_disease_ner_it_onnx
date: 2026-01-03
tags: [medical, clinical, bert, ner, it, licensed, onnx]
task: Named Entity Recognition
language: it
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
engine: onnx
annotator: BertForTokenClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Bert-based token classification model for identifying disease mentions in text using the BIO tagging scheme (B-DISEASE, I-DISEASE, O). Designed for dense disease extraction in clinical and biomedical narratives.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_disease_ner_it_onnx_it_6.2.0_3.4_1767402589007.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_disease_ner_it_onnx_it_6.2.0_3.4_1767402589007.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import *
from sparknlp.annotator import *
from pyspark.ml import Pipeline

documentAssembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")

tokenClassifier = BertForTokenClassification \
    .pretrained("bert_disease_ner_it_onnx", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("ner")

converter = NerConverter() \
    .setInputCols(["document", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    documentAssembler,
    tokenizer,
    tokenClassifier,
    converter
])

data = spark.createDataFrame([
    ["Paziente con diabete tipo 2, ipertensione, IRC, scompenso cardiaco e BPCO; complicazioni da retinopatia, neuropatia e osteoartrite, con gestione di iperlipidemia e anemia."],
    ["Paziente con polmonite, sepsi, ARDS e cirrosi; coesistono colite ulcerosa, Crohn e lupus. Necessari interventi per aritmia, squilibri elettrolitici e insufficienza cardiaca."],
    ["Paziente oncologico (seno, ovaie, pancreas, leucemia) con neutropenia, cachessia e infezioni (CMV, herpes). Presenti anche osteoporosi, diabete e dolore cronico."]
]).toDF("text")

result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk").selectExpr(
    "chunk.result as text",
    "chunk.metadata['entity'] as entity"
).show(truncate=False)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")

tokenClassifier = medical.BertForTokenClassification \
    .pretrained("bert_disease_ner_it_onnx", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("ner")

converter = nlp.NerConverter() \
    .setInputCols(["document", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    tokenizer,
    tokenClassifier,
    converter
])

data = spark.createDataFrame([
    ["Paziente con diabete tipo 2, ipertensione, IRC, scompenso cardiaco e BPCO; complicazioni da retinopatia, neuropatia e osteoartrite, con gestione di iperlipidemia e anemia."],
    ["Paziente con polmonite, sepsi, ARDS e cirrosi; coesistono colite ulcerosa, Crohn e lupus. Necessari interventi per aritmia, squilibri elettrolitici e insufficienza cardiaca."],
    ["Paziente oncologico (seno, ovaie, pancreas, leucemia) con neutropenia, cachessia e infezioni (CMV, herpes). Presenti anche osteoporosi, diabete e dolore cronico."]
]).toDF("text")

result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk").selectExpr(
    "chunk.result as text",
    "chunk.metadata['entity'] as entity"
).show(truncate=False)
```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import org.apache.spark.sql.functions._
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols(Array("document"))
  .setOutputCol("token")

val tokenClassifier = BertForTokenClassification
  .pretrained("bert_disease_ner_it_onnx", "en", "clinical/models")
  .setInputCols(Array("document", "token"))
  .setOutputCol("ner")

val converter = new NerConverter()
  .setInputCols(Array("document", "token", "ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  tokenizer,
  tokenClassifier,
  converter
))

val data = Seq(
  "Paziente con diabete tipo 2, ipertensione, IRC, scompenso cardiaco e BPCO; complicazioni da retinopatia, neuropatia e osteoartrite, con gestione di iperlipidemia e anemia.",
  "Paziente con polmonite, sepsi, ARDS e cirrosi; coesistono colite ulcerosa, Crohn e lupus. Necessari interventi per aritmia, squilibri elettrolitici e insufficienza cardiaca.",
  "Paziente oncologico (seno, ovaie, pancreas, leucemia) con neutropenia, cachessia e infezioni (CMV, herpes). Presenti anche osteoporosi, diabete e dolore cronico."
).toDF("text")

val result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk")
  .selectExpr("chunk.result as text", "chunk.metadata['entity'] as entity")
  .show(false)
```
</div>

## Results

```bash

+-----------------------+-------+
|text                   |entity |
+-----------------------+-------+
|diabete tipo           |DISEASE|
|ipertensione           |DISEASE|
|IRC                    |DISEASE|
|scompenso cardiaco     |DISEASE|
|BPCO                   |DISEASE|
|retinopatia            |DISEASE|
|neuropatia             |DISEASE|
|osteoartrite           |DISEASE|
|iperlipidemia          |DISEASE|
|anemia                 |DISEASE|
|polmonite              |DISEASE|
|sepsi                  |DISEASE|
|ARDS                   |DISEASE|
|cirrosi                |DISEASE|
|colite ulcerosa        |DISEASE|
|Crohn                  |DISEASE|
|lupus                  |DISEASE|
|aritmia                |DISEASE|
|squilibri elettrolitici|DISEASE|
|insufficienza cardiaca |DISEASE|
+-----------------------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_disease_ner_it_onnx|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token, sentence]|
|Output Labels:|[ner]|
|Language:|it|
|Size:|409.2 MB|
|Case sensitive:|true|
|Max sentence length:|128|