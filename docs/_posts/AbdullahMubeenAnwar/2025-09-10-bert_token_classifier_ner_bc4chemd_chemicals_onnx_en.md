---
layout: model
title: Detect Chemicals in Medical Text - ONNX
author: John Snow Labs
name: bert_token_classifier_ner_bc4chemd_chemicals_onnx
date: 2025-09-10
tags: [medical, clinical, ner, en, licensed, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.1.1
spark_version: 3.0
supported: true
engine: onnx
annotator: MedicalBertForTokenClassifier
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The automatic extraction of chemical information from text requires the recognition of chemical entity mentions as one of its key steps.

This model is trained with the BertForTokenClassification method from the transformers library and imported into Spark NLP. The model detects chemical entities from a medical text.

## Predicted Entities

`B-CHEM`, `O`, `I-CHEM`, `PAD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_bc4chemd_chemicals_onnx_en_6.1.1_3.0_1757524894770.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_bc4chemd_chemicals_onnx_en_6.1.1_3.0_1757524894770.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
        "bert_token_classifier_ner_bc4chemd_chemicals_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "document"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
     NerConverterInternal()
    .setInputCols(["document", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "The main isolated compounds were triterpenes (alpha - amyrin, beta - amyrin, lupeol, betulin, betulinic acid, uvaol, erythrodiol and oleanolic acid) and phenolic acid derivatives from 4 - hydroxybenzoic acid (gallic and protocatechuic acids and isocorilagin)."
data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```
{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")


tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")


token_classifier = medical.BertForTokenClassifier.pretrained(
        "bert_token_classifier_ner_bc4chemd_chemicals_onnx",
        "en",
        "clinical/models"
    )\
    .setInputCols(["token", "document"])\
    .setOutputCol("ner")\
    .setCaseSensitive(True)


ner_converter = medical.NerConverterInternal()\
    .setInputCols(["document", "token", "ner"])\
    .setOutputCol("ner_chunk")


pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "The main isolated compounds were triterpenes (alpha - amyrin, beta - amyrin, lupeol, betulin, betulinic acid, uvaol, erythrodiol and oleanolic acid) and phenolic acid derivatives from 4 - hydroxybenzoic acid (gallic and protocatechuic acids and isocorilagin)."
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
  .pretrained("bert_token_classifier_ner_bc4chemd_chemicals_onnx", "en", "clinical/models")
  .setInputCols(Array("token", "document"))
  .setOutputCol("ner")
  .setCaseSensitive(true)

val nerConverter = new  NerConverterInternal()
  .setInputCols(Array("document", "token", "ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    tokenizer,
    tokenClassifier,
    nerConverter
  ))

val testSentence = "The main isolated compounds were triterpenes (alpha - amyrin, beta - amyrin, lupeol, betulin, betulinic acid, uvaol, erythrodiol and oleanolic acid) and phenolic acid derivatives from 4 - hydroxybenzoic acid (gallic and protocatechuic acids and isocorilagin)."
val data = Seq(testSentence).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+-------------------------------+------+
|text                           |entity|
+-------------------------------+------+
|triterpenes                    |CHEM  |
|alpha - amyrin                 |CHEM  |
|beta - amyrin                  |CHEM  |
|lupeol                         |CHEM  |
|betulin                        |CHEM  |
|betulinic acid                 |CHEM  |
|uvaol                          |CHEM  |
|erythrodiol                    |CHEM  |
|oleanolic acid                 |CHEM  |
|phenolic acid                  |CHEM  |
|4 - hydroxybenzoic acid        |CHEM  |
|gallic and protocatechuic acids|CHEM  |
|isocorilagin                   |CHEM  |
+-------------------------------+------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_bc4chemd_chemicals_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|403.7 MB|
|Case sensitive:|true|
|Max sentence length:|128|
