---
layout: model
title: Sentence Embeddings - Biobert cased (MedNLI, onnx)
author: John Snow Labs
name: sbiobert_base_cased_mli_onnx
date: 2024-01-22
tags: [licensed, en, clinical, embeddings, onnx, sbiobert]
task: Embeddings
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
engine: onnx
annotator: BertSentenceEmbeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is trained to generate contextual sentence embeddings of input sentences. It has been fine-tuned on MedNLI dataset to provide sota performance on STS and SentEval Benchmarks.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobert_base_cased_mli_onnx_en_5.2.1_3.0_1705940372620.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobert_base_cased_mli_onnx_en_5.2.1_3.0_1705940372620.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

sbiobert_embeddings = BertSentenceEmbeddings\
  .pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
  .setInputCols(["ner_chunk_doc"])\
  .setOutputCol("sbert_embeddings")

```
```scala

val sbiobert_embeddings = BertSentenceEmbeddings
  .pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sbert_embeddings")
```
</div>

## Results

```bash
Gives a 768 dimensional vector representation of the sentence.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobert_base_cased_mli_onnx|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[sentence_embeddings_onnx]|
|Language:|en|
|Size:|403.1 MB|
|Case sensitive:|false|