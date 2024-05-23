---
layout: model
title: Medical Assertion MPNet Embedding ( oncology )
author: John Snow Labs
name: mpnet_embeddings_medical_assertion_oncology
date: 2024-05-23
tags: [embeddings, en, licensed, clinical, mpnet, onnx]
task: Embeddings
language: en
edition: Healthcare NLP 5.3.2
spark_version: 3.0
supported: true
engine: onnx
annotator: MPNetEmbeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is trained on a list of clinical and biomedical datasets curated in-house

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/mpnet_embeddings_medical_assertion_oncology_en_5.3.2_3.0_1716485127779.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/mpnet_embeddings_medical_assertion_oncology_en_5.3.2_3.0_1716485127779.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

mpnet_embedding = MPNetEmbeddings.pretrained("mpnet_embeddings_medical_assertion_oncology", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("mpnet_embeddings")

pipeline = Pipeline().setStages([document_assembler, mpnet_embedding])

text = [
    ["I feel a bit drowsy after taking an insulin."],
    ["Peter Parker is a nice lad and lives in New York"]
]

data = spark.createDataFrame(text).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val mpnet_embedding = MPNetEmbeddings.pretrained("mpnet_embeddings_medical_assertion_oncology", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("mpnet_embeddings")

val pipeline = new Pipeline().setStages(Array(document_assembler, mpnet_embedding))

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                     assertion_embedding|
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[{sentence_embeddings, 0, 43, I feel a bit drowsy after taking an insulin., {sentence -> 0}, [-0.030117756, -0.06916913, 0.01004766, 0.0070122266, -0.009609902, -0.07718129, -0.069940895, 0.1486813...|
|[{sentence_embeddings, 0, 47, Peter Parker is a nice lad and lives in New York, {sentence -> 0}, [-0.010607893, -0.06711012, 0.0058346647, 0.010627323, -4.902818E-4, -0.07712458, -0.036254555, 0.12...|
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|mpnet_embeddings_medical_assertion_oncology|
|Compatibility:|Healthcare NLP 5.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[assertion_embedding]|
|Language:|en|
|Size:|406.9 MB|
|Case sensitive:|false|
