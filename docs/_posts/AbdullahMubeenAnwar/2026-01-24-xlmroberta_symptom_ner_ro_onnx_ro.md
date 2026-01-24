---
layout: model
title: Symptom Named Entity Recognition Romanian (Base, ONNX)
author: John Snow Labs
name: xlmroberta_symptom_ner_ro_onnx
date: 2026-01-24
tags: [medical, clinical, xlmroberta, ner, ro, licensed, onnx]
task: Named Entity Recognition
language: ro
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
engine: onnx
annotator: XlmRoBertaForTokenClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is an XLM-RoBERTa-based NER model for Romanian medical text. It identifies symptom mentions in clinical sentences and labels them using B-SYMPTOM, I-SYMPTOM, or O. The model is intended for extracting symptom names from notes, reports, and clinical records, and is provided in ONNX format for efficient inference.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/xlmroberta_symptom_ner_ro_onnx_ro_6.2.0_3.4_1769254510754.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/xlmroberta_symptom_ner_ro_onnx_ro_6.2.0_3.4_1769254510754.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

tokenClassifier = XlmRoBertaForTokenClassification \
    .pretrained("xlmroberta_symptom_ner_ro_onnx", "ro", "clinical/models") \
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
    ["Pacientul acuză dureri de cap severe și amețeli persistente, asociate cu greață și vărsături."],
    ["Femeia prezintă dispnee la efort, tuse cronică și oboseală accentuată de câteva săptămâni."],
    ["Bărbatul se plânge de dureri abdominale, febră mare și frisoane nocturne."]
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

tokenClassifier = nlp.XlmRoBertaForTokenClassification \
    .pretrained("xlmroberta_symptom_ner_ro_onnx", "ro", "clinical/models") \
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
    ["Pacientul acuză dureri de cap severe și amețeli persistente, asociate cu greață și vărsături."],
    ["Femeia prezintă dispnee la efort, tuse cronică și oboseală accentuată de câteva săptămâni."],
    ["Bărbatul se plânge de dureri abdominale, febră mare și frisoane nocturne."]
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
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols(Array("document"))
  .setOutputCol("token")

val tokenClassifier = XlmRoBertaForTokenClassification
  .pretrained("xlmroberta_symptom_ner_ro_onnx", "ro", "clinical/models")
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

val data = spark.createDataFrame(Seq(
  "Pacientul acuză dureri de cap severe și amețeli persistente, asociate cu greață și vărsături.",
  "Femeia prezintă dispnee la efort, tuse cronică și oboseală accentuată de câteva săptămâni.",
  "Bărbatul se plânge de dureri abdominale, febră mare și frisoane nocturne."
)).toDF("text")

val result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk")
  .selectExpr("chunk.result as text", "chunk.metadata['entity'] as entity")
  .show(false)
```
</div>

## Results

```bash

+------+-------+
|text  |entity |
+------+-------+
|greață|SYMPTOM|
|tuse  |SYMPTOM|
+------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|xlmroberta_symptom_ner_ro_onnx|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token, sentence]|
|Language:|ro|
|Size:|1.0 GB|