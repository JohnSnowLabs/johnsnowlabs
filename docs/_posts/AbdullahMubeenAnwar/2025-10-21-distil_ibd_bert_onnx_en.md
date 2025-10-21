---
layout: model
title: Distil_IBD_BERT (ONNX)
author: John Snow Labs
name: distil_ibd_bert_onnx
date: 2025-10-21
tags: [medical, clinical, en, embeddings, licensed, onnx]
task: Embeddings
language: en
edition: Healthcare NLP 6.1.0
spark_version: 3.0
supported: true
engine: onnx
annotator: DistilBertEmbeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The model classifies documents as either IBD or Not IBD. It is designed to distinguish between documents that are likely related to patients with inflammatory bowel disease (IBD) and those that are not suggestive of IBD.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/distil_ibd_bert_onnx_en_6.1.0_3.0_1761056671570.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/distil_ibd_bert_onnx_en_6.1.0_3.0_1761056671570.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import Tokenizer, DistilBertEmbeddings
from pyspark.ml import Pipeline

document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

distilbert_loaded = DistilBertEmbeddings.pretrained("distil_ibd_bert_onnx") \
    .setInputCols(['document', 'token']) \
    .setOutputCol("distilbert")

pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    distilbert_loaded
])

data = spark.createDataFrame([
    ["The patient reports intermittent abdominal pain and loose stools over the past three months."]
]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

result.select("distilbert.embeddings").show()

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

distilbert_loaded = nlp.DistilBertEmbeddings.pretrained("distil_ibd_bert_onnx") \
    .setInputCols(['document', 'token']) \
    .setOutputCol("distilbert")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    distilbert_loaded
])

data = spark.createDataFrame([
    ["The patient reports intermittent abdominal pain and loose stools over the past three months."]
]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

result.select("distilbert.embeddings").show()

```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import org.apache.spark.ml.Pipeline
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols(Array("document"))
  .setOutputCol("token")

val distilBert = DistilBertEmbeddings.pretrained("distil_ibd_bert_onnx")
  .setInputCols(Array("document", "token"))
  .setOutputCol("distilbert")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  tokenizer,
  distilBert
))

val data = Seq(
  "The patient reports intermittent abdominal pain and loose stools over the past three months."
).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)

result.select("distilbert.embeddings").show(false)

```
</div>

## Results

```bash

+--------------------+
|          embeddings|
+--------------------+
|[[0.23429918, 0.3...|
+--------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|distil_ibd_bert_onnx|
|Compatibility:|Healthcare NLP 6.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[distilbert]|
|Language:|en|
|Size:|247.2 MB|
|Case sensitive:|true|