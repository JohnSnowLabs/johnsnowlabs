---
layout: model
title: Medical Assertion MPNet Embedding ( base )
author: John Snow Labs
name: e5_base_v2_embeddings_medical_assertion_base
date: 2024-07-03
tags: [embeddings, en, licensed, clinical, e5, onnx, medical, assertion, base]
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

This model is trained on a list of clinical and biomedical datasets curated in-house

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/e5_base_v2_embeddings_medical_assertion_base_en_5.3.3_3.0_1720001190877.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/e5_base_v2_embeddings_medical_assertion_base_en_5.3.3_3.0_1720001190877.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_base", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("mpnet_embeddings")

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

val e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_base", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("embeddings")

val pipeline = new Pipeline().setStages(Array(document_assembler, mpnet_embedding))

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                              embeddings|
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[{sentence_embeddings, 0, 43, I feel a bit drowsy after taking an insulin., {sentence -> 0}, [-0.010884863, 0.007896974, 0.03736705, -0.057596024, 0.028397387, -9.937644E-4, -0.06973768, -0.0125734...|
|[{sentence_embeddings, 0, 47, Peter Parker is a nice guy and lives in New York, {sentence -> 0}, [0.108221725, 0.050705638, 0.025993714, 0.04520446, -0.018801026, -0.01583123, 0.020007214, 0.036804...|
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|e5_base_v2_embeddings_medical_assertion_base|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[embeddings]|
|Language:|en|
|Size:|393.0 MB|
|Case sensitive:|false|
