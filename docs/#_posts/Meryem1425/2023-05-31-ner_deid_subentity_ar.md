---
layout: model
title: Detect Subentity PHI for Deidentification (Arabic)
author: John Snow Labs
name: ner_deid_subentity
date: 2023-05-31
tags: [licensed, clinical, ner, deidentification, arabic, ar]
task: Named Entity Recognition
language: ar
edition: Healthcare NLP 4.4.2
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Named Entity Recognition annotators allow for a generic model to be trained by using a Deep Learning architecture (Char CNNs - BiLSTM - CRF - word embeddings) inspired on a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM,CNN.

Deidentification NER (Arabic) is a Named Entity Recognition model that annotates text to find protected health information that may need to be de-identified. It detects 17 entities. This NER model is trained with a combination of custom datasets, and several data augmentation mechanisms. This model Word2Vec Arabic Clinical Embeddings.

## Predicted Entities

`PATIENT`, `HOSPITAL`, `DATE`, `ORGANIZATION`, `CITY`, `STREET`, `USERNAME`, `SEX`, `IDNUM`, `EMAIL`, `ZIP`, `MEDICALRECORD`, `PROFESSION`, `PHONE`, `COUNTRY`, `DOCTOR`, `AGE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.1.Clinical_Multi_Language_Deidentification.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_ar_4.4.2_3.0_1685559675615.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_ar_4.4.2_3.0_1685559675615.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = WordEmbeddingsModel.pretrained("arabic_w2v_cc_300d", "ar")\
    .setInputCols(["document", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_deid_subentity", "ar", "clinical/models")\
        .setInputCols(["sentence","token","embeddings"])\
        .setOutputCol("ner")

ner_converter = NerConverterInternal()\
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
عالج الدكتور محمد المريض أحمد البالغ من العمر 55 سنة  في 15/05/2000  في مستشفى مدينة الرباط. رقم هاتفه هو  0610948235 وبريده الإلكتروني
mohamedmell@gmail.com.
 '''

data = spark.createDataFrame([[text]]).toDF("text")

results = nlpPipeline .fit(data).transform(data)

```
```scala
val documentAssembler = new DocumentAssembler()
.setInputCol("text")
.setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
.setInputCols(Array("document"))
.setOutputCol("sentence")

val tokenizer = new Tokenizer()
.setInputCols(Array("sentence"))
.setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("arabic_w2v_cc_300d", "ar")
.setInputCols(Array("sentence","token"))
.setOutputCol("word_embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_deid_subentity", "ar", "clinical/models")
.setInputCols(Array("sentence","token","word_embeddings"))
.setOutputCol("ner")

val ner_converter = new NerConverterInternal()
.setInputCols(Array("sentence", "token", "ner"))
.setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, 
    sentenceDetector, 
    tokenizer, 
    embeddings, 
    clinical_ner, 
    ner_converter))

text = '''
عالج الدكتور محمد المريض أحمد البالغ من العمر 55 سنة  في 15/05/2000  في مستشفى مدينة الرباط. رقم هاتفه هو  0610948235 وبريده الإلكتروني
mohamedmell@gmail.com.
 '''

val data = Seq(text).toDS.toDF("text")

val results = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------------------------------------+----------------+
|chunk                                             |ner_label|
+------------------------------------------------+---------------+
|محمد                                                 |DOCTOR   |
|55 سنة                                              |AGE          |
|15/05/2000                                   |DATE        |
|الرباط                                                |CITY          |
|0610948235                                 |PHONE     |
|mohamedmell@gmail.com       |EMAIL       |
+------------------------------------------------+--------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_subentity|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|ar|
|Size:|15.0 MB|

## Benchmarking

```bash
        label     tp    fp    fn  total  precision  recall      f1
      PATIENT  196.0  26.0  32.0  228.0     0.8829  0.8596  0.8711
     HOSPITAL  193.0  41.0  37.0  230.0     0.8248  0.8391  0.8319
         DATE  877.0  14.0   8.0  885.0     0.9843   0.991  0.9876
 ORGANIZATION   41.0  11.0   6.0   47.0     0.7885  0.8723  0.8283
         CITY  260.0   8.0   5.0  265.0     0.9701  0.9811  0.9756
       STREET  103.0   3.0   0.0  103.0     0.9717     1.0  0.9856
     USERNAME    8.0   0.0   0.0    8.0        1.0     1.0     1.0
          SEX  300.0   9.0  69.0  369.0     0.9709   0.813   0.885
        IDNUM   13.0   1.0   0.0   13.0     0.9286     1.0   0.963
        EMAIL  112.0   5.0   0.0  112.0     0.9573     1.0  0.9782
          ZIP   80.0   4.0   0.0   80.0     0.9524     1.0  0.9756
MEDICALRECORD   17.0   1.0   0.0   17.0     0.9444     1.0  0.9714
   PROFESSION  303.0  27.0  32.0  335.0     0.9182  0.9045  0.9113
        PHONE   38.0   4.0   2.0   40.0     0.9048    0.95  0.9268
      COUNTRY  158.0  10.0   8.0  166.0     0.9405  0.9518  0.9461
       DOCTOR  440.0  23.0  34.0  474.0     0.9503  0.9283  0.9392
          AGE  610.0  18.0   7.0  617.0     0.9713  0.9887  0.9799
        macro     -     -     -      -       -       -      0.9386
        micro     -     -     -      -       -       -      0.9434
```