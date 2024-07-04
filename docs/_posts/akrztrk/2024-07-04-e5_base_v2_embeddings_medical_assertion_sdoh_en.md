---
layout: model
title: Medical Assertion E5 Embedding ( SDOH )
author: John Snow Labs
name: e5_base_v2_embeddings_medical_assertion_sdoh
date: 2024-07-04
tags: [embeddings, en, licensed, clinical, e5, medical, sdoh, onnx]
task: Embeddings
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
engine: onnx
annotator: E5Embeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model has been trained on a curated list of clinical and biomedical datasets. It has been fine-tuned for Few-Shot Assertion but can also be utilized for other purposes, such as Classification and Retrieval-Augmented Generation (RAG).

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/e5_base_v2_embeddings_medical_assertion_sdoh_en_5.3.3_3.0_1720084681662.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/e5_base_v2_embeddings_medical_assertion_sdoh_en_5.3.3_3.0_1720084681662.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_sdoh", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("e5_embeddings")

pipeline = Pipeline().setStages([document_assembler, e5_embeddings])

text = [
    ["I feel a bit drowsy after taking an insulin."],
    ["Peter Parker is a nice guy and lives in New York"]
]

data = spark.createDataFrame(text).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_sdoh", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("e5_embeddings")

val pipeline = new Pipeline().setStages(Array(document_assembler, e5_embeddings))

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                              embeddings|
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[{sentence_embeddings, 0, 43, I feel a bit drowsy after taking an insulin., {sentence -> 0}, [0.016282124, 0.03343147, 0.06332478, -0.018355524, 0.07614877, -0.05762618, -0.027328357, 8.692102E-4, ...|
|[{sentence_embeddings, 0, 47, Peter Parker is a nice guy and lives in New York, {sentence -> 0}, [0.119976304, 0.04998236, 0.038619783, 0.04968784, -0.01774702, -0.009462719, 0.012399124, 0.0409855...|
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|e5_base_v2_embeddings_medical_assertion_sdoh|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[embeddings]|
|Language:|en|
|Size:|393.0 MB|
|Case sensitive:|false|