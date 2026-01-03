---
layout: model
title: Medication Named Entity Recognition Italian (Base, ONNX)
author: John Snow Labs
name: bert_medical_ner_it_onnx
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

Bert-based token classification model trained to identify medication mentions in clinical and biomedical text using the BIO tagging scheme. The model labels medication entities with B-MEDICATION and I-MEDICATION tags while assigning O to non-medication tokens. It is designed for dense medication extraction in free-text clinical notes, discharge summaries, prescriptions, and biomedical narratives.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_medical_ner_it_onnx_it_6.2.0_3.4_1767398956870.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_medical_ner_it_onnx_it_6.2.0_3.4_1767398956870.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .pretrained("bert_medical_ner_it_onnx", "en", "clinical/models") \
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
    ["Il paziente è stato trattato con metformina, insuline e sitagliptin, associati ad antiaggreganti e anticoagulanti, antibiotici multipli, e dimesso con statine, antipertensivi ed ezetimibe."],
    ["Durante il ricovero ha ricevuto antibiotici ad ampio spettro e antifungini, analgesici per il dolore, antiemetici per la nausea e farmaci per la protezione gastrica."],
    ["In oncologia ha ricevuto chemioterapia combinata con terapia di supporto, quindi è passato a terapia ormonale per il trattamento a lungo termine."]
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
    .pretrained("bert_medical_ner_it_onnx", "en", "clinical/models") \
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
    ["Il paziente è stato trattato con metformina, insuline e sitagliptin, associati ad antiaggreganti e anticoagulanti, antibiotici multipli, e dimesso con statine, antipertensivi ed ezetimibe."],
    ["Durante il ricovero ha ricevuto antibiotici ad ampio spettro e antifungini, analgesici per il dolore, antiemetici per la nausea e farmaci per la protezione gastrica."],
    ["In oncologia ha ricevuto chemioterapia combinata con terapia di supporto, quindi è passato a terapia ormonale per il trattamento a lungo termine."]
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
  .pretrained("bert_medical_ner_it_onnx", "en", "clinical/models")
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
  "Il paziente è stato trattato con metformina, insuline e sitagliptin, associati ad antiaggreganti e anticoagulanti, antibiotici multipli, e dimesso con statine, antipertensivi ed ezetimibe.",
  "Durante il ricovero ha ricevuto antibiotici ad ampio spettro e antifungini, analgesici per il dolore, antiemetici per la nausea e farmaci per la protezione gastrica.",
  "In oncologia ha ricevuto chemioterapia combinata con terapia di supporto, quindi è passato a terapia ormonale per il trattamento a lungo termine."
).toDF("text")

val result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk")
  .selectExpr("chunk.result as text", "chunk.metadata['entity'] as entity")
  .show(false)
```
</div>

## Results

```bash

+-----------+----------+
|text       |entity    |
+-----------+----------+
|metformina |MEDICATION|
|insuline   |MEDICATION|
|sitagliptin|MEDICATION|
|statine    |MEDICATION|
|ezetimibe  |MEDICATION|
+-----------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_medical_ner_it_onnx|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token, sentence]|
|Output Labels:|[ner]|
|Language:|it|
|Size:|409.2 MB|
|Case sensitive:|true|
|Max sentence length:|128|