---
layout: model
title: Detect Genes/Proteins (BC2GM) in Medical Text - ONNX
author: John Snow Labs
name: bert_token_classifier_ner_bc2gm_gene_onnx
date: 2025-09-10
tags: [medical, clinical, ner, en, licensed, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.1.0
spark_version: 3.0
supported: true
engine: onnx
annotator: MedicalBertForTokenClassifier
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

`bert_token_classifier_ner_bc2gm_gene` is a **BERT-based token classification model** fine-tuned for **Named Entity Recognition (NER) of genes and proteins**.  
It is trained on biomedical data and can recognize mentions of gene and protein names in scientific and clinical text.

## Predicted Entities

`B-GENE/PROTEIN`, `O`, `I-GENE/PROTEIN`, `PAD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_bc2gm_gene_onnx_en_6.1.0_3.0_1757523376673.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_bc2gm_gene_onnx_en_6.1.0_3.0_1757523376673.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import MedicalBertForTokenClassifier
from sparknlp.annotator import Tokenizer, NerConverter
from pyspark.ml import Pipeline

document_assembler = (
    DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

tokenizer = (
    Tokenizer()
    .setInputCols(["document"])
    .setOutputCol("token")
)

token_classifier = (
    MedicalBertForTokenClassifier.pretrained(
        "bert_token_classifier_ner_bc2gm_gene_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "document"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
    NerConverter()
    .setInputCols(["document", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "ROCK-I, Kinectin, and mDia2 can bind the wild type forms of both RhoA and Cdc42 in a GTP-dependent manner in vitro. These results support the hypothesis that in the presence of tryptophan the ribosome translating tnaC blocks Rho ' s access to the boxA and rut sites, thereby preventing transcription termination."
data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```
```scala
import com.johnsnowlabs.nlp.base.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.Tokenizer
import com.johnsnowlabs.nlp.annotators.ner.NerConverter
import com.johnsnowlabs.nlp.annotators.classifier.dl.MedicalBertForTokenClassifier
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier
  .pretrained("bert_token_classifier_ner_bc2gm_gene_onnx", "en", "clinical/models")
  .setInputCols("token", "document")
  .setOutputCol("ner")
  .setCaseSensitive(true)

val nerConverter = new NerConverter()
  .setInputCols("document", "token", "ner")
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    tokenizer,
    tokenClassifier,
    nerConverter
  ))

val testSentence = "ROCK-I, Kinectin, and mDia2 can bind the wild type forms of both RhoA and Cdc42 in a GTP-dependent manner in vitro. These results support the hypothesis that in the presence of tryptophan the ribosome translating tnaC blocks Rho ' s access to the boxA and rut sites, thereby preventing transcription termination."
val data = Seq(testSentence).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+---------+------------+
|text     |entity      |
+---------+------------+
|ROCK-I   |GENE/PROTEIN|
|Kinectin |GENE/PROTEIN|
|mDia2    |GENE/PROTEIN|
|RhoA     |GENE/PROTEIN|
|Cdc42    |GENE/PROTEIN|
|tnaC     |GENE/PROTEIN|
|Rho      |GENE/PROTEIN|
|boxA     |GENE/PROTEIN|
|rut sites|GENE/PROTEIN|
+---------+------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_bc2gm_gene_onnx|
|Compatibility:|Healthcare NLP 6.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|403.7 MB|
|Case sensitive:|true|
|Max sentence length:|128|
