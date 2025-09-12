---
layout: model
title: Self-Reported Covid-19 Symptoms Classifier (BERT) ONNX
author: John Snow Labs
name: bert_sequence_classifier_self_reported_symptoms_tweet_onnx
date: 2025-09-12
tags: [es, clinical, licensed, public_health, classifier, sequence_classification, covid_19, tweet, symptom, onnx]
task: Text Classification
language: es
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

This model is a [BERT based](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) classifier that can classify the origin of symptoms related to Covid-19 from Spanish tweets. 
This model is intended for direct use as a classification model and the target classes are: Lit-News_mentions, Self_reports, non-personal_reports.

## Predicted Entities

`Lit-News_mentions`, `Self_reports`, `non-personal_reports`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_self_reported_symptoms_tweet_onnx_es_6.1.1_3.0_1757690978032.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_self_reported_symptoms_tweet_onnx_es_6.1.1_3.0_1757690978032.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
        "bert_sequence_classifier_self_reported_symptoms_tweet_onnx",
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

data = spark.createDataFrame(["Las vacunas 3 y hablamos inminidad vivo  Son bichito vivo dentro de lÃ­quido de la vacuna suelen tener reacciones alÃorgicas si que sepan",
                              "Yo pense que me estaba dando el  coronavirus porque cuando me levante  casi no podia respirar pero que si era que tenia la nariz topada de mocos.",
                              "Tos, dolor de garganta y fiebre, los síntomas más reportados por los porteños con coronavirus"], StringType()).toDF("text")

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
        "bert_sequence_classifier_self_reported_symptoms_tweet_onnx",
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

data = spark.createDataFrame(["Las vacunas 3 y hablamos inminidad vivo  Son bichito vivo dentro de lÃ­quido de la vacuna suelen tener reacciones alÃorgicas si que sepan",
                              "Yo pense que me estaba dando el  coronavirus porque cuando me levante  casi no podia respirar pero que si era que tenia la nariz topada de mocos.",
                              "Tos, dolor de garganta y fiebre, los síntomas más reportados por los porteños con coronavirus"], StringType()).toDF("text")

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
  .pretrained("bert_sequence_classifier_self_reported_symptoms_tweet_onnx", "en", "clinical/models")
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

val data = Seq(
  "Las vacunas 3 y hablamos inminidad vivo  Son bichito vivo dentro de lÃ­quido de la vacuna suelen tener reacciones alÃorgicas si que sepan",
  "Yo pense que me estaba dando el  coronavirus porque cuando me levante  casi no podia respirar pero que si era que tenia la nariz topada de mocos.",
  "Tos, dolor de garganta y fiebre, los síntomas más reportados por los porteños con coronavirus"
).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
|text                                                                                                                                             |result                |
+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
|Las vacunas 3 y hablamos inminidad vivo  Son bichito vivo dentro de lÃ­quido de la vacuna suelen tener reacciones alÃorgicas si que sepan         |[non-personal_reports]|
|Yo pense que me estaba dando el  coronavirus porque cuando me levante  casi no podia respirar pero que si era que tenia la nariz topada de mocos.|[Self_reports]        |
|Tos, dolor de garganta y fiebre, los síntomas más reportados por los porteños con coronavirus                                                    |[Lit-News_mentions]   |
+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_self_reported_symptoms_tweet_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|es|
|Size:|443.9 MB|
|Case sensitive:|true|