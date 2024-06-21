---
layout: model
title: Finance Word Embeddings
author: John Snow Labs
name: finance_word_embeddings
date: 2024-05-21
tags: [en, finance, licensed, word_embeddings]
task: Embeddings
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
annotator: WordEmbeddingsModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The word embedding models were based on Word2Vec, trained on a mix of different datasets. We used public data and in-house annotated documents.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finance_word_embeddings_en_1.0.0_3.0_1716300545868.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finance_word_embeddings_en_1.0.0_3.0_1716300545868.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
model =  nlp.WordEmbeddingsModel.pretrained("finance_word_embeddings","en","finance/models")\
	.setInputCols(["sentence","token"])\
	.setOutputCol("embeddings")
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finance_word_embeddings|
|Type:|embeddings|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[word_embeddings]|
|Language:|en|
|Size:|103.4 MB|
|Case sensitive:|false|
|Dimension:|200|

## References

Public data and in-house annotated documents