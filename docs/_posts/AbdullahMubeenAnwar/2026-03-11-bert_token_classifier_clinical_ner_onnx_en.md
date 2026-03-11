---
layout: model
title: Detect Clinical Entities (BertForTokenClassifier - ONNX)
author: John Snow Labs
name: bert_token_classifier_clinical_ner_onnx
date: 2026-03-11
tags: [medical, clinical, ner, en, licensed, onnx]
task: Named Entity Recognition
language: en
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

A BERT-based token classification model exported to ONNX for efficient inference. It performs clinical named entity recognition (NER) by identifying and labeling medical entities.

## Predicted Entities

`I-AGE`, `I-LAB_VALUE`, `I-LAB_NAME`, `B-BMI_VALUE`, `B-SUBSTANCE`, `B-PERF_STATUS`, `I-SMOKING`, `I-PREGNANCY`, `B-LAB_VALUE`, `I-ALLERGY`, `I-PROCEDURE`, `B-AGE`, `I-CONDITION`, `I-GENDER`, `I-PERF_STATUS`, `I-SUBSTANCE`, `B-LAB_NAME`, `B-GENDER`, `B-CONDITION`, `B-SMOKING`, `B-PROCEDURE`, `B-MEDICATION`, `I-BMI_VALUE`, `I-MEDICATION`, `B-ALLERGY`, `O`, `B-PREGNANCY`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_clinical_ner_onnx_en_6.2.0_3.4_1773244366482.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_clinical_ner_onnx_en_6.2.0_3.4_1773244366482.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import *
from sparknlp_jsl.annotator import *
from pyspark.ml import Pipeline

document_assembler = DocumentAssembler() \
    .setInputCol('text') \
    .setOutputCol('document')

tokenizer = Tokenizer() \
    .setInputCols(['document']) \
    .setOutputCol('token')

bert_loaded = MedicalBertForTokenClassifier.pretrained("bert_token_classifier_clinical_ner_onnx", "en", "clinical/models") \
    .setInputCols(['document', 'token']) \
    .setOutputCol('ner')

ner_converter = NerConverterInternal() \
    .setInputCols(['document', 'token', 'ner']) \
    .setOutputCol('entities')

pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    bert_loaded,
    ner_converter,
])

texts = [
    'Exclude patients with type 1 diabetes and pregnant or breastfeeding women.',
    'Patients must have a serum creatinine level below 1.5 mg/dL.',
    'Subjects receiving metformin 500mg twice daily for at least 3 months.',
]

df = spark.createDataFrame([[t] for t in texts], ['text'])

model = pipeline.fit(df)
predictions = model.transform(df)

predictions.select('text', 'entities.result').show(truncate=60)
predictions.selectExpr("explode(entities) as chunk").selectExpr(
    "chunk.result as text",
    "chunk.metadata['entity'] as entity",
    "chunk.metadata['confidence'] as score"
).show(truncate=False)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler() \
    .setInputCol('text') \
    .setOutputCol('document')

tokenizer = nlp.Tokenizer() \
    .setInputCols(['document']) \
    .setOutputCol('token')

bert_loaded = medical.MedicalBertForTokenClassifier.pretrained("bert_token_classifier_clinical_ner_onnx", "en", "clinical/models") \
    .setInputCols(['document', 'token']) \
    .setOutputCol('ner')

ner_converter = nlp.NerConverterInternal() \
    .setInputCols(['document', 'token', 'ner']) \
    .setOutputCol('entities')

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    bert_loaded,
    ner_converter,
])

texts = [
    'Exclude patients with type 1 diabetes and pregnant or breastfeeding women.',
    'Patients must have a serum creatinine level below 1.5 mg/dL.',
    'Subjects receiving metformin 500mg twice daily for at least 3 months.',
]

df = spark.createDataFrame([[t] for t in texts], ['text'])

model = pipeline.fit(df)
predictions = model.transform(df)

predictions.select('text', 'entities.result').show(truncate=60)
predictions.selectExpr("explode(entities) as chunk").selectExpr(
    "chunk.result as text",
    "chunk.metadata['entity'] as entity",
    "chunk.metadata['confidence'] as score"
).show(truncate=False)
```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp._
import org.apache.spark.ml.Pipeline
import spark.implicits._

val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols(Array("document"))
  .setOutputCol("token")

val bert_loaded = MedicalBertForTokenClassifier
  .pretrained("bert_token_classifier_clinical_ner_onnx", "en", "clinical/models")
  .setInputCols(Array("document", "token"))
  .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
  .setInputCols(Array("document", "token", "ner"))
  .setOutputCol("entities")

val pipeline = new Pipeline().setStages(Array(
  document_assembler,
  tokenizer,
  bert_loaded,
  ner_converter
))

val texts = Seq(
  "Exclude patients with type 1 diabetes and pregnant or breastfeeding women.",
  "Patients must have a serum creatinine level below 1.5 mg/dL.",
  "Subjects receiving metformin 500mg twice daily for at least 3 months."
)

val df = texts.toDF("text")

val model = pipeline.fit(df)
val predictions = model.transform(df)

predictions.select("text", "entities.result").show(60, truncate = false)

import org.apache.spark.sql.functions._

predictions
  .select(explode($"entities").alias("chunk"))
  .select(
    $"chunk.result".alias("text"),
    $"chunk.metadata".getItem("entity").alias("entity"),
    $"chunk.metadata".getItem("confidence").alias("score")
  )
  .show(false)
```
</div>

## Results

```bash

+------------------------------------------------------------+------------------------------------------+
|                                                        text|                                    result|
+------------------------------------------------------------+------------------------------------------+
|Exclude patients with type 1 diabetes and pregnant or bre...|[type 1 diabetes, pregnant, breastfeeding]|
|Patients must have a serum creatinine level below 1.5 mg/dL.|             [serum creatinine, 1.5 mg/dL]|
|Subjects receiving metformin 500mg twice daily for at lea...|                               [metformin]|
+------------------------------------------------------------+------------------------------------------+

+----------------+----------+----------+
|text            |entity    |score     |
+----------------+----------+----------+
|type 1 diabetes |CONDITION |0.99994826|
|pregnant        |PREGNANCY |0.9960041 |
|breastfeeding   |PREGNANCY |0.99455976|
|serum creatinine|LAB_NAME  |0.9964936 |
|1.5 mg/dL       |LAB_VALUE |0.99515235|
|metformin       |MEDICATION|0.99995756|
+----------------+----------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_clinical_ner_onnx|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|439.8 MB|
|Case sensitive:|false|
|Max sentence length:|512|