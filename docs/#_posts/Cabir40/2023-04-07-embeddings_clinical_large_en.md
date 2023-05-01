---
layout: model
title: Embeddings Clinical (Large)
author: John Snow Labs
name: embeddings_clinical_large
date: 2023-04-07
tags: [licensed, en, clinical, embeddings]
task: Embeddings
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.0
supported: true
annotator: WordEmbeddingsModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is trained on a list of clinical and biomedical datasets curated in-house, using the word2vec algorithm. The dataset curation cut-off date is March 2023 and the model is expected to have a better generalization on recent content. The size of the model is around 2 GB and has 200 dimensions. Our benchmark tests indicate that our legacy clinical embeddings (embeddings _clinical) can be replaced with this one.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/embeddings_clinical_large_en_4.3.2_3.0_1680905541704.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/embeddings_clinical_large_en_4.3.2_3.0_1680905541704.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_large","en","clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("word_embeddings")

```
```scala

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_large","en","clinical/models")
    .setInputCols(Array("document","token"))
    .setOutputCol("word_embeddings")

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|embeddings_clinical_large|
|Type:|embeddings|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[word_embeddings]|
|Language:|en|
|Size:|2.0 GB|
|Case sensitive:|true|
|Dimension:|200|