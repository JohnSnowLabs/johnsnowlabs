---
layout: model
title: Detect Generic PHI for Deidentification (AraBERT, Arabic)
author: John Snow Labs
name: ner_deid_arabert_generic
date: 2023-09-13
tags: [licensed, ner, clinical, deidentification, generic, arabic, ar, arabert, bert]
task: Named Entity Recognition
language: ar
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Named Entity Recognition annotators allow for a generic model to be trained by using a Deep Learning architecture (Char CNNs - BiLSTM - CRF - word embeddings) inspired on a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM,CNN.

Deidentification NER (Arabic) is a Named Entity Recognition model that annotates text to find protected health information that may need to be de-identified. It detects 8 entities. This NER model is trained with a combination of custom datasets, and several data augmentation mechanisms. This model uses AraBERT Arabic Embeddings.

## Predicted Entities

`CONTACT`, `NAME`, `DATE`, `ID`, `SEX`, `LOCATION`, `PROFESSION`, `AGE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_arabert_generic_ar_5.1.0_3.0_1694620155009.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_arabert_generic_ar_5.1.0_3.0_1694620155009.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
documentAssembler = DocumentAssembler()\
        .setInputCol("text")\
        .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")\
        .setInputCols(["document"])\
        .setOutputCol("sentence")

tokenizer = Tokenizer()\
        .setInputCols(["sentence"])\
        .setOutputCol("token")

embeddings = BertEmbeddings.pretrained("bert_embeddings_bert_base_arabert","ar") \
.setInputCols(["document", "token"]) \
.setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_deid_arabert_generic", "ar", "clinical/models")\
        .setInputCols(["sentence","token","embeddings"])\
        .setOutputCol("ner")

ner_converter = NerConverter()\
        .setInputCols(["sentence","token","ner"])\
        .setOutputCol("ner_chunk")

nlpPipeline = Pipeline(stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,
        embeddings,
        clinical_ner,
        ner_converter])

text = '''
عالج الدكتور محمد المريض أحمد البالغ من العمر 55 سنة  في 15/05/2000  في مستشفى مدينة الرباط. رقم هاتفه هو  0610948234 وبريده الإلكتروني
abcd@gmail.com.
 '''

data = spark.createDataFrame([[text]]).toDF("text")

results = nlpPipeline .fit(data).transform(data)

```
```scala
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = SentenceDetector
  .pretrained("sentence_detector_dl", "xx")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val embeddings = BertEmbeddings
  .pretrained("bert_embeddings_bert_base_arabert", "ar")
  .setInputCols(Array("document", "token"))
  .setOutputCol("embeddings")
  .setCaseSensitive(true)  

val clinicalNer = MedicalNerModel
  .pretrained("ner_deid_arabert_generic", "ar", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

val nerConverter = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")

val nlpPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  clinicalNer,
  nerConverter
))

val text = '''
عالج الدكتور محمد المريض أحمد البالغ من العمر 55 سنة  في 15/05/2000  في مستشفى مدينة الرباط. رقم هاتفه هو  0610948234 وبريده الإلكتروني
abcd@gmail.com.
 '''

val data: DataFrame = spark.createDataFrame(Seq((text,))).toDF("text")

val results = nlpPipeline.fit(data).transform(data)

```
</div>

## Results

```bash
+---------------------------+-------------------------------------------+
|chunk                         |ner_label|
+---------------------------+-------------------------------------------+
|55 سنة                                  |AGE      |
|15/05/2000                      |DATE     |
|0610948234                     |ID          |
|abcd@gmail.com            |CONTACT  |
+---------------------------+-------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_arabert_generic|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|ar|
|Size:|16.3 MB|

## Benchmarking

```bash

  Label         Precision         Recall            F1
  AGE           95.89905362776025 98.7012987012987  97.27999999999999
  CONTACT       99.3103448275862  94.73684210526315 96.96969696969695
  DATE          97.62443438914026 97.07536557930258 97.3491257755217
  ID            73.17073170731707 100.0             84.50704225352112
  LOCATION      89.93464052287582 83.80024360535931 86.75914249684743
  NAME          86.44536652835409 89.28571428571429 87.84258608573437
  PROFESSION    88.29787234042553 74.32835820895522 80.71312803889789
  SEX           97.14285714285714 81.6              88.69565217391305
  Macro         -                 -                 0.9372647
  Micro         -                 -                 0.9505749
```
