---
layout: model
title: BioClinicalBERT_IBD (ONNX)
author: John Snow Labs
name: bioclinicalbert_ibd_onnx
date: 2025-10-21
tags: [medical, clinical, en, classification, licensed, onnx]
task: Text Classification
language: en
edition: Healthcare NLP 6.1.0
spark_version: 3.0
supported: true
engine: onnx
annotator: BertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The model classifies documents as either IBD or Not IBD. It is designed to distinguish between documents that are likely related to patients with inflammatory bowel disease (IBD) and those that are not suggestive of IBD.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bioclinicalbert_ibd_onnx_en_6.1.0_3.0_1761065465537.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bioclinicalbert_ibd_onnx_en_6.1.0_3.0_1761065465537.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import Tokenizer, BertForSequenceClassification
from pyspark.ml import Pipeline

document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

bfsc_loaded = BertForSequenceClassification.pretrained("bioclinicalbert_ibd_onnx") \
    .setInputCols(['document', 'token']) \
    .setOutputCol("label")

pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    bfsc_loaded
])

data = spark.createDataFrame([
    ["Patient with inflammatory bowel disease and colon inflammation."],
    ["Normal colonoscopy findings, no evidence of inflammation."],
]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

result.select("text", "label.result").show(truncate=False)

```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

bfsc_loaded = nlp.BertForSequenceClassification.pretrained("bioclinicalbert_ibd_onnx") \
    .setInputCols(['document', 'token']) \
    .setOutputCol("label")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    bfsc_loaded
])

data = spark.createDataFrame([
    ["Patient with inflammatory bowel disease and colon inflammation."],
    ["Normal colonoscopy findings, no evidence of inflammation."],
]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

result.select("text", "label.result").show(truncate=False)

```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotator._
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols(Array("document"))
  .setOutputCol("token")

val bfscLoaded = BertForSequenceClassification.pretrained("bioclinicalbert_ibd_onnx")
  .setInputCols(Array("document", "token"))
  .setOutputCol("label")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  tokenizer,
  bfscLoaded
))

val data = Seq(
  ("Patient with inflammatory bowel disease and colon inflammation."),
  ("Normal colonoscopy findings, no evidence of inflammation.")
).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)

result.select("text", "label.result").show(false)

```
</div>

## Results

```bash

+---------------------------------------------------------------+---------+
|text                                                           |result   |
+---------------------------------------------------------------+---------+
|Patient with inflammatory bowel disease and colon inflammation.|[IBD]    |
|Normal colonoscopy findings, no evidence of inflammation.      |[Not IBD]|
+---------------------------------------------------------------+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bioclinicalbert_ibd_onnx|
|Compatibility:|Healthcare NLP 6.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|405.5 MB|