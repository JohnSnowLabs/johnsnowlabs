---
layout: model
title: Veterinary Clinical Diagnosis Embeddings (ONNX)
author: John Snow Labs
name: vetclinical_bert_dx_onnx
date: 2025-12-29
tags: [bert, embeddings, medical, clinical, en, licensed, onnx]
task: Embeddings
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
engine: onnx
annotator: BertEmbeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is trained on large scale real world veterinary medical records to capture the terminology, structure, and diagnostic patterns found in animal health notes, enabling accurate downstream tasks such as disease syndrome classification, information extraction, and clinical text analysis.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/vetclinical_bert_dx_onnx_en_6.2.0_3.4_1767010179009.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/vetclinical_bert_dx_onnx_en_6.2.0_3.4_1767010179009.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = BertEmbeddings.pretrained("vetclinical_bert_dx_onnx", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("embeddings")

pipeline = Pipeline(stages=[
    documentAssembler, 
    tokenizer, 
    embeddings
])

data = spark.createDataFrame([[
    "Dog presented with vomiting, lethargy, and decreased appetite for three days."
]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

result.select("embeddings.embeddings").show()
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

embeddings = medical.BertEmbeddings.pretrained("vetclinical_bert_dx_onnx", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("embeddings")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, 
    tokenizer, 
    embeddings
])

data = spark.createDataFrame([[
    "Dog presented with vomiting, lethargy, and decreased appetite for three days."
]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

result.select("embeddings.embeddings").show()
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

val embeddings = BertEmbeddings.pretrained("vetclinical_bert_dx_onnx", "en", "clinical/models")
  .setInputCols(Array("document", "token"))
  .setOutputCol("embeddings")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  tokenizer,
  embeddings
))

val data = spark.createDataFrame(Seq(
  "Dog presented with vomiting, lethargy, and decreased appetite for three days."
).map(Tuple1(_))).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)

result.select("embeddings.embeddings").show(false)
```
</div>

## Results

```bash

+--------------------+
|          embeddings|
+--------------------+
|[[-0.12431372, -0...|
+--------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|vetclinical_bert_dx_onnx|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[embeddings]|
|Language:|en|
|Size:|402.8 MB|
|Case sensitive:|false|
|Max sentence length:|512|