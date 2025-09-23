---
layout: model
title: Detect Organism in Medical Text - ONNX
author: John Snow Labs
name: bert_token_classifier_ner_species_onnx
date: 2025-09-11
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

Species-800 is a corpus for species entities, which is based on manually annotated abstracts. It comprises 800 PubMed abstracts that contain identified organism mentions.

This model is trained with the BertForTokenClassification method from the transformers library and imported into Spark NLP.

## Predicted Entities

`I-SPECIES`, `O`, `B-SPECIES`, `PAD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_species_onnx_en_6.1.1_3.0_1757563237859.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_species_onnx_en_6.1.1_3.0_1757563237859.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
        "bert_token_classifier_ner_species_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "sentence"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
    NerConverterInternal()
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

test_sentence = "As determined by 16S rRNA gene sequence analysis, strain 6C (T) represents a distinct species belonging to the class Betaproteobacteria and is most closely related to Thiomonas intermedia DSM 18155 (T) and Thiomonas perometabolis DSM 18570 (T)."
data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```
{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")
   
sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

tokenClassifier = medical.BertForTokenClassification.pretrained("bert_token_classifier_ner_species_onnx", "en", "clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")


pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    tokenClassifier,
    ner_converter
])

data = spark.createDataFrame(["As determined by 16S rRNA gene sequence analysis, strain 6C (T) represents a distinct species belonging to the class Betaproteobacteria and is most closely related to Thiomonas intermedia DSM 18155 (T) and Thiomonas perometabolis DSM 18570 (T)."], StringType()).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

```

```scala
import com.johnsnowlabs.nlp.base.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.Tokenizer
import com.johnsnowlabs.nlp.annotators.ner.NerConverter
import com.johnsnowlabs.nlp.annotators.classifier.dl.MedicalBertForTokenClassifier
import com.johnsnowlabs.nlp.annotators.sentence_detector_dl.SentenceDetectorDLApproach
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetectorDLModel()
  .pretrained("sentence_detector_dl","xx")
  .setInputCols("document")
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier
  .pretrained("bert_token_classifier_ner_species_onnx", "en", "clinical/models")
  .setInputCols(Array("token", "document"))
  .setOutputCol("ner")
  .setCaseSensitive(true)

val nerConverter = new NerConverterInternal()
  .setInputCols(Array("document", "token", "ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    tokenClassifier,
    nerConverter
  ))

val testSentence = "As determined by 16S rRNA gene sequence analysis, strain 6C (T) represents a distinct species belonging to the class Betaproteobacteria and is most closely related to Thiomonas intermedia DSM 18155 (T) and Thiomonas perometabolis DSM 18570 (T)."
val data = Seq(testSentence).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+-----------------------+-------+
|text                   |entity |
+-----------------------+-------+
|6C (T)                 |SPECIES|
|Betaproteobacteria     |SPECIES|
|Thiomonas intermedia   |SPECIES|
|DSM 18155 (T)          |SPECIES|
|Thiomonas perometabolis|SPECIES|
|DSM 18570 (T).         |SPECIES|
+-----------------------+-------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_species_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|403.7 MB|
|Case sensitive:|true|
|Max sentence length:|128|