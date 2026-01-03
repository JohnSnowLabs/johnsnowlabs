---
layout: model
title: Procedure Named Entity Recognition Italian (Base, ONNX)
author: John Snow Labs
name: bert_procedure_ner_it_onnx
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

Bert-based token classification model for extracting procedure mentions from text using BIO labels (B-PROCEDURE, I-PROCEDURE, O). Intended for dense procedure recognition in clinical and biomedical narratives.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_procedure_ner_it_onnx_it_6.2.0_3.4_1767404150447.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_procedure_ner_it_onnx_it_6.2.0_3.4_1767404150447.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .pretrained("bert_procedure_ner_it_onnx", "en", "clinical/models") \
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
    ["Valutazione iniziale: esami ematici, diagnostica per immagini (RX, TC, RM) e screening cardiopolmonare (ECG, stress test, angiografia, test funzionalità polmonare)."],
    ["Ricovero: intubazione, ventilazione meccanica, accessi vascolari (CVC/arteriosi), procedure invasive (rachicentesi, toracentesi) e dialisi (CRRT)."],
    ["Interventi chirurgici: appendicectomia, laparotomia, resezione intestinale e colostomia. Inclusi debridement, trasfusioni e percorso di riabilitazione fisica."]
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
    .pretrained("bert_procedure_ner_it_onnx", "en", "clinical/models") \
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
    ["Valutazione iniziale: esami ematici, diagnostica per immagini (RX, TC, RM) e screening cardiopolmonare (ECG, stress test, angiografia, test funzionalità polmonare)."],
    ["Ricovero: intubazione, ventilazione meccanica, accessi vascolari (CVC/arteriosi), procedure invasive (rachicentesi, toracentesi) e dialisi (CRRT)."],
    ["Interventi chirurgici: appendicectomia, laparotomia, resezione intestinale e colostomia. Inclusi debridement, trasfusioni e percorso di riabilitazione fisica."]
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
  .pretrained("bert_procedure_ner_it_onnx", "en", "clinical/models")
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
  "Valutazione iniziale: esami ematici, diagnostica per immagini (RX, TC, RM) e screening cardiopolmonare (ECG, stress test, angiografia, test funzionalità polmonare).",
  "Ricovero: intubazione, ventilazione meccanica, accessi vascolari (CVC/arteriosi), procedure invasive (rachicentesi, toracentesi) e dialisi (CRRT).",
  "Interventi chirurgici: appendicectomia, laparotomia, resezione intestinale e colostomia. Inclusi debridement, trasfusioni e percorso di riabilitazione fisica."
).toDF("text")

val result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk")
  .selectExpr("chunk.result as text", "chunk.metadata['entity'] as entity")
  .show(false)
```
</div>

## Results

```bash

+---------------------------+---------+
|text                       |entity   |
+---------------------------+---------+
|esami                      |PROCEDURE|
|diagnostica per immagini   |PROCEDURE|
|RX                         |PROCEDURE|
|TC                         |PROCEDURE|
|RM                         |PROCEDURE|
|screening cardiopolmonare  |PROCEDURE|
|ECG                        |PROCEDURE|
|stress test                |PROCEDURE|
|angiografia                |PROCEDURE|
|test funzionalità polmonare|PROCEDURE|
|intubazione                |PROCEDURE|
|ventilazione meccanica     |PROCEDURE|
|accessi vascolari          |PROCEDURE|
|CVC/arteriosi              |PROCEDURE|
|rachicentesi               |PROCEDURE|
|toracentesi                |PROCEDURE|
|dialisi                    |PROCEDURE|
|CRRT                       |PROCEDURE|
|appendicectomia            |PROCEDURE|
|laparotomia                |PROCEDURE|
+---------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_procedure_ner_it_onnx|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token, sentence]|
|Output Labels:|[ner]|
|Language:|it|
|Size:|409.2 MB|
|Case sensitive:|true|
|Max sentence length:|128|