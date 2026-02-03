---
layout: model
title: Disease Named Entity Recognition Italian (Base, ONNX)
author: John Snow Labs
name: bert_token_classifier_disease_ner_it_onnx
date: 2026-01-20
tags: [medical, clinical, bert, ner, it, licensed, onnx]
task: Named Entity Recognition
language: it
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
engine: onnx
annotator: MedicalBertForTokenClassifier
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a BERT-based NER model for Italian medical text. It identifies disease mentions in clinical sentences and labels them using B-DISEASE, I-DISEASE, or O. The model is intended for extracting disease names from notes, reports, and diagnoses, and is provided in ONNX format for efficient inference.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_disease_ner_it_onnx_it_6.2.0_3.4_1768900384936.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_disease_ner_it_onnx_it_6.2.0_3.4_1768900384936.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import *
from sparknlp_jsl.annotator import *
from pyspark.ml import Pipeline

documentAssembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")

tokenClassifier = MedicalBertForTokenClassifier \
    .pretrained("bert_token_classifier_disease_ner_it_onnx", "it", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("ner")

converter = NerConverterInternal() \
    .setInputCols(["document", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    documentAssembler,
    tokenizer,
    tokenClassifier,
    converter
])

data = spark.createDataFrame([["Il paziente è stato diagnosticato con diabete e ipertensione."]]).toDF("text")
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

tokenClassifier = medical.MedicalBertForTokenClassifier \
    .pretrained("bert_token_classifier_disease_ner_it_onnx", "it", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("ner")

converter = nlp.NerConverterInternal() \
    .setInputCols(["document", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    tokenizer,
    tokenClassifier,
    converter
])

data = spark.createDataFrame([["Il paziente è stato diagnosticato con diabete e ipertensione."]]).toDF("text")
result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk").selectExpr(
    "chunk.result as text",
    "chunk.metadata['entity'] as entity"
).show(truncate=False)
```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols(Array("document"))
  .setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier
  .pretrained("bert_token_classifier_disease_ner_it_onnx", "it", "clinical/models")
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

val data = Seq("Il paziente è stato diagnosticato con diabete e ipertensione.").toDF("text")
val result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk")
  .selectExpr("chunk.result as text", "chunk.metadata['entity'] as entity")
  .show(false)
```
</div>

## Results

```bash

+------------+-------+
|text        |entity |
+------------+-------+
|diabete     |DISEASE|
|ipertensione|DISEASE|
+------------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_disease_ner_it_onnx|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token, sentence]|
|Output Labels:|[ner]|
|Language:|it|
|Size:|441.5 MB|
|Case sensitive:|true|
|Max sentence length:|128|