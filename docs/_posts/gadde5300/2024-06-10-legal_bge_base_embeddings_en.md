---
layout: model
title: Legal BGE Embeddings
author: John Snow Labs
name: legal_bge_base_embeddings
date: 2024-06-10
tags: [legal, licensed, embeddings, bge, en, onnx]
task: Embeddings
language: en
edition: Legal NLP 1.0.0
spark_version: 3.2
supported: true
recommended: true
engine: onnx
annotator: BGEEmbeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The BGE embedding model was trained on a mix of different datasets. We used public data and in-house annotated documents.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legal_bge_base_embeddings_en_1.0.0_3.2_1718032892975.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legal_bge_base_embeddings_en_1.0.0_3.2_1718032892975.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
embeddings =  nlp.BGEEmbeddings.pretrained("legal_bge_base_embeddings","en","legal/models")\
    .setInputCols("document")\ 
    .setOutputCol("embeddings")
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legal_bge_base_embeddings|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[sentence_embeddings]|
|Language:|en|
|Size:|394.4 MB|

## References

Public data and in-house annotated documents