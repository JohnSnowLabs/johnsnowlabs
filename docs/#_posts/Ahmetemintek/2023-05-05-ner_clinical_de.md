---
layout: model
title: Detect Problems, Tests and Treatments (ner_clinical) in German
author: John Snow Labs
name: ner_clinical
date: 2023-05-05
tags: [ner, clinical, licensed, de]
task: Named Entity Recognition
language: de
edition: Healthcare NLP 4.4.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms in German. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/14.German_Healthcare_Models.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_de_4.4.0_3.0_1683310968546.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_de_4.4.0_3.0_1683310968546.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
        .setInputCol("text")\
        .setOutputCol("document")
         
sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
        .setInputCols(["sentence"])\
        .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d", "de", "clinical/models")\
        .setInputCols(["sentence", "token"])\
        .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_clinical", "de", "clinical/models") \
        .setInputCols(["sentence", "token", "embeddings"]) \
        .setOutputCol("ner")

ner_converter = NerConverterInternal()\
         .setInputCols(["sentence", "token", "ner"])\
         .setOutputCol("ner_chunk")

nlpPipeline = Pipeline(stages=[document_assembler, 
                               sentence_detector, 
                               tokenizer, 
                               word_embeddings, 
                               clinical_ner, 
                               ner_converter])

model = nlpPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text= """Verschlechterung von Schmerzen oder Schwäche in den Beinen , Verlust der Darm - oder Blasenfunktion oder andere besorgniserregende Symptome. 
Der Patient erhielt empirisch Ampicillin , Gentamycin und Flagyl sowie Narcan zur Umkehrung von Fentanyl .
ALT war 181 , AST war 156 , LDH war 336 , alkalische Phosphatase war 214 und Bilirubin war insgesamt 12,7 ."""

results = model.transform(spark.createDataFrame([[sample_text]], ["text"]))
```
```scala
val document_assembler = new DocumentAssembler()
        .setInputCol("text")
        .setOutputCol("document")
         
val sentence_detector =  SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
        .setInputCols("document")
        .setOutputCol("sentence")

val tokenizer = new Tokenizer()
        .setInputCols("sentence")
        .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d", "de", "clinical/models")
        .setInputCols(Array("sentence", "token"))
        .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_clinical", "de", "clinical/models")
        .setInputCols(Array("sentence", "token", "embeddings"))
        .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
         .setInputCols(Array("sentence", "token", "ner"))
         .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, ner, ner_converter))

val data = Seq("""Verschlechterung von Schmerzen oder Schwäche in den Beinen , Verlust der Darm - oder Blasenfunktion oder andere besorgniserregende Symptome. 
Der Patient erhielt empirisch Ampicillin , Gentamycin und Flagyl sowie Narcan zur Umkehrung von Fentanyl .
ALT war 181 , AST war 156 , LDH war 336 , alkalische Phosphatase war 214 und Bilirubin war insgesamt 12,7 .""").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------+---------+
|chunk                 |ner_label|
+----------------------+---------+
|Schmerzen             |PROBLEM  |
|Schwäche in den Beinen|PROBLEM  |
|Verlust der Darm      |PROBLEM  |
|Blasenfunktion        |PROBLEM  |
|Symptome              |PROBLEM  |
|empirisch Ampicillin  |TREATMENT|
|Gentamycin            |TREATMENT|
|Flagyl                |TREATMENT|
|Narcan                |TREATMENT|
|Fentanyl              |TREATMENT|
|ALT                   |TEST     |
|AST                   |TEST     |
|LDH                   |TEST     |
|alkalische Phosphatase|TEST     |
|Bilirubin             |TEST     |
+----------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical|
|Compatibility:|Healthcare NLP 4.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|de|
|Size:|2.1 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
   B-PROBLEM       0.78      0.77      0.77       407
      B-TEST       0.77      0.92      0.84       220
 B-TREATMENT       0.82      0.71      0.76       241
   I-PROBLEM       0.87      0.78      0.82       386
      I-TEST       0.66      0.93      0.77        57
 I-TREATMENT       0.68      0.76      0.72        76
           O       0.96      0.97      0.96      4323
    accuracy       -         -         0.92      5710
   macro-avg       0.79      0.83      0.81      5710
weighted-avg       0.92      0.92      0.92      5710
```
