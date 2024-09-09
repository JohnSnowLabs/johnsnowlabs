---
layout: model
title: Medical Assertion E5 Embedding ( Smoking )
author: John Snow Labs
name: e5_base_v2_embeddings_medical_assertion_smoking
date: 2024-07-03
tags: [embeddings, en, licensed, clinical, e5, medical, smoking, onnx]
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/e5_base_v2_embeddings_medical_assertion_smoking_en_5.3.3_3.0_1720020757802.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/e5_base_v2_embeddings_medical_assertion_smoking_en_5.3.3_3.0_1720020757802.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_smoking", "en", "clinical/models")\
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

val e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_smoking", "en", "clinical/models")
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
|[{sentence_embeddings, 0, 43, I feel a bit drowsy after taking an insulin., {sentence -> 0}, [0.10872599, 0.055253826, 0.020003157, 0.041003194, -0.010374628, -0.02620654, 0.01587664, 0.037322525, ...|
|[{sentence_embeddings, 0, 47, Peter Parker is a nice guy and lives in New York, {sentence -> 0}, [0.108851634, 0.052013967, 0.029346386, 0.043766238, -0.012921171, -0.01598542, 0.023271276, 0.03910...|
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|e5_base_v2_embeddings_medical_assertion_smoking|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[embeddings]|
|Language:|en|
|Size:|393.1 MB|
|Case sensitive:|false|
