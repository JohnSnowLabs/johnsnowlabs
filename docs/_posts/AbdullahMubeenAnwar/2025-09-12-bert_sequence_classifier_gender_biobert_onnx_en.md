---
layout: model
title: Gender Classifier (BERT) ONNX
author: John Snow Labs
name: bert_sequence_classifier_gender_biobert_onnx
date: 2025-09-12
tags: [bert, sequence_classification, en, licensed, onnx]
task: Text Classification
language: en
edition: Healthcare NLP 6.1.1
spark_version: 3.0
supported: true
engine: onnx
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model classifies the gender of a patient in a clinical document using context.


This model is a [BioBERT-based](https://github.com/dmis-lab/biobert) classifier.

## Predicted Entities

`Female`, `Male`, `Unknown`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_gender_biobert_onnx_en_6.1.1_3.0_1757683741648.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_gender_biobert_onnx_en_6.1.1_3.0_1757683741648.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import SentenceDetectorDLModel, MedicalBertForTokenClassifier
from sparknlp.annotator import Tokenizer, NerConverter
from pyspark.ml import Pipeline

document_assembler = (
    DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

sentenceDetector = (
    SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(["document"])
    .setOutputCol("sentence")
)

tokenizer = (
    Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")
)

token_classifier = (
    MedicalBertForTokenClassifier.pretrained(
        "bert_sequence_classifier_gender_biobert_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "sentence"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
    NerConverter()
    .setInputCols(["sentence", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    token_classifier,
    ner_converter
])

data = spark.createDataFrame([["The patient took Advil and he experienced an adverse reaction."]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = (
    nlp.DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

sentenceDetector = (
    nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(["document"])
    .setOutputCol("sentence")
)

tokenizer = (
    nlp.Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")
)

token_classifier = (
    medical.MedicalBertForTokenClassifier.pretrained(
        "bert_sequence_classifier_gender_biobert_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "sentence"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
    nlp.NerConverter()
    .setInputCols(["sentence", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    token_classifier,
    ner_converter
])

data = spark.createDataFrame([["The patient took Advil and he experienced an adverse reaction."]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import org.apache.spark.ml.Pipeline
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetectorDLModel()
  .pretrained("sentence_detector_dl","xx")
  .setInputCols(["document"])
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier
  .pretrained("bert_sequence_classifier_gender_biobert_onnx", "en", "clinical/models")
  .setInputCols("token", "document")
  .setOutputCol("ner")
  .setCaseSensitive(true)

val nerConverter = new NerConverter()
  .setInputCols("document", "token", "ner")
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    tokenClassifier,
    nerConverter
  ))

val data = Seq("The patient took Advil and he experienced an adverse reaction.").toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+---------------------------------------------------------------+------+
|text                                                           |result|
+---------------------------------------------------------------+------+
|The patient took Advil and he experienced an adverse reaction. |[Male]|
+---------------------------------------------------------------+------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_gender_biobert_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|