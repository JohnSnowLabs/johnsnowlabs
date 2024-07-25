---
layout: model
title: Medical Assertion MPNet Embedding ( i2b2 )
author: John Snow Labs
name: mpnet_embeddings_medical_assertion
date: 2024-07-25
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

This model is trained on a list of clinical and biomedical datasets curated in-house.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/mpnet_embeddings_medical_assertion_en_5.3.2_3.0_1721895142581.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/mpnet_embeddings_medical_assertion_en_5.3.2_3.0_1721895142581.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
    
mpnet_embedding = MPNetEmbeddings.pretrained("mpnet_embeddings_medical_assertion", "en", "clinical/models")\
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
    
val mpnet_embedding = MPNetEmbeddings.pretrained("mpnet_embeddings_medical_assertion", "en", "clinical/models")
    .setInputCols(Array("document")) 
    .setOutputCol("mpnet_embeddings") 

val pipeline = new Pipeline().setStages(Array(document_assembler, mpnet_embedding))

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
|    | assertion_embedding            |
|---:|:-------------------------------|
|  0 | [Row(annotatorType='sentence_embeddings', begin=0, end=43, result='I feel a bit drowsy after taking an insulin.', metadata={'sentence': '0'}, embeddings=[-0.02157330885529518, -0.05100712180137634, 0.043191660195589066, 0.035359036177396774, -0.04416131228208542, 0.036355987191200256, -0...])] |
|  1 | [Row(annotatorType='sentence_embeddings', begin=0, end=47, result='Peter Parker is a nice lad and lives in New York', metadata={'sentence': '0'}, embeddings=[-0.07660277187824249, -0.01287313923239708, 0.015349301509559155, 0.008208038285374641, 0.015206931158900261, -0.0321115218102932,...])] |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|mpnet_embeddings_medical_assertion|
|Compatibility:|Healthcare NLP 5.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[assertion_embedding]|
|Language:|en|
|Size:|407.0 MB|
|Case sensitive:|false|