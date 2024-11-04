---
layout: model
title: Detect PHI for Deidentification (Subentity - Langtest)
author: John Snow Labs
name: ner_deid_subentity_langtest
date: 2024-10-24
tags: [de, deid, ner, licensed, clinical, langtest]
task: De-identification
language: de
edition: Healthcare NLP 5.5.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Named Entity Recognition annotator allows for a generic model to be trained by utilizing a deep learning algorithm (Char CNNs - BiLSTM - CRF - word embeddings) inspired on a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM, CNN. Deidentification NER is a Named Entity Recognition model that annotates German text to find protected health information (PHI) that may need to be deidentified. It was trained with in-house annotations and detects 12 entities.

## Predicted Entities

`PATIENT`, `HOSPITAL`, `DATE`, `ORGANIZATION`, `CITY`, `STREET`, `USERNAME`, `PROFESSION`, `PHONE`, `COUNTRY`, `DOCTOR`, `AGE`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_DEID_DE/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.1.Clinical_Multi_Language_Deidentification.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_langtest_de_5.5.0_3.0_1729797788849.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_langtest_de_5.5.0_3.0_1729797788849.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d", "de", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

deid_ner = MedicalNerModel.pretrained("ner_deid_subentity_langtest", "de", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_deid_subentity_chunk")

nlpPipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector, 
    tokenizer,
    word_embeddings, 
    deid_ner, 
    ner_converter])

data = spark.createDataFrame([["""Am Morgen des 12. Dezember 2018 wird der Patient Michael Berger ins St. Elisabeth-Krankenhaus, einer Klinik in der Stadt Bad Kissingen, eingeliefer. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen."""]]).toDF("text")

result = nlpPipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val sentence_detector = new SentenceDetector()
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d", "de", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val deid_ner = MedicalNerModel.pretrained("ner_deid_subentity_langtest", "de", "clinical/models") 
    .setInputCols(Array("sentence", "token", "embeddings")) 
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_deid_subentity_chunk")

val nlpPipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector, 
    tokenizer, 
    word_embeddings, 
    deid_ner, 
    ner_converter))

val data = Seq("""Am Morgen des 12. Dezember 2018 wird der Patient Michael Berger ins St. Elisabeth-Krankenhaus, einer Klinik in der Stadt Bad Kissingen, eingeliefer. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen.""").toDS.toDF("text")

val result = nlpPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------------------+-----+---+---------+
|chunk                |begin|end|ner_label|
+---------------------+-----+---+---------+
|Dezember 2018        |18   |30 |DATE     |
|Michael Berger       |49   |62 |PATIENT  |
|Elisabeth-Krankenhaus|72   |92 |HOSPITAL |
|Bad Kissingen        |121  |133|CITY     |
|Berger               |154  |159|PATIENT  |
|76                   |165  |166|AGE      |
+---------------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_subentity_langtest|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|de|
|Size:|3.0 MB|

## Benchmarking

```bash
        label  precision    recall  f1-score   support
          AGE       0.96      0.97      0.96       476
         CITY       0.87      0.78      0.82       200
      COUNTRY       0.96      0.47      0.63       312
         DATE       1.00      1.00      1.00      4049
       DOCTOR       0.96      0.95      0.95      1453
     HOSPITAL       0.95      0.94      0.94      1598
MEDICALRECORD       0.88      0.92      0.90       217
 ORGANIZATION       0.82      0.73      0.77      1355
      PATIENT       0.90      0.91      0.90      2154
        PHONE       0.80      0.81      0.81        80
   PROFESSION       0.98      0.70      0.82       262
       STREET       0.85      0.96      0.90       128
     USERNAME       0.91      0.93      0.92        45
    micro-avg       0.94      0.91      0.93     12329
    macro-avg       0.91      0.85      0.87     12329
 weighted-avg       0.94      0.91      0.92     12329
```
