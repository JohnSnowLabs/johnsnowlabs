---
layout: model
title: Sentence Embeddings - Biobert cased (MedNLI, onnx)
author: John Snow Labs
name: sbiobert_base_cased_mli_onnx
date: 2023-07-10
tags: [en, licensed, onnx]
task: Embeddings
language: en
edition: Healthcare NLP 5.0.0
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobert_base_cased_mli_onnx_en_5.0.0_3.0_1689000999960.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobert_base_cased_mli_onnx_en_5.0.0_3.0_1689000999960.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

Use as part of an nlp pipeline with the following stages: DocumentAssembler, SentenceDetector, BertSentenceEmbeddings. The output of this model can be used in tasks like NER, Classification, Entity Resolution etc.

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
sbiobert_embeddings = BertSentenceEmbeddings\
.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
.setInputCols(["ner_chunk_doc"])\
.setOutputCol("sbert_embeddings")
```
```scala
val sbiobert_embeddings = BertSentenceEmbeddings
.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")
.setInputCols(Array("ner_chunk_doc"))
.setOutputCol("sbert_embeddings"
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
|Compatibility:|Healthcare NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|399.7 MB|
|Case sensitive:|true|