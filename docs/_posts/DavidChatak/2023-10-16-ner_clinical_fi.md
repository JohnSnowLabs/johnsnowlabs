---
layout: model
title: Detect Problems, Tests and Treatments (ner_clinical) in Finnish
author: John Snow Labs
name: ner_clinical
date: 2023-10-16
tags: [ner, clinical, fi, licensed]
task: Named Entity Recognition
language: fi
edition: Healthcare NLP 5.1.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms in Finnish. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_fi_5.1.1_3.0_1697492251091.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_fi_5.1.1_3.0_1697492251091.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","fi") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "fi", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
    ])

sample_text = """Potilaan virtsanalyysi 19.10.97 osoitti kohtalaisen okkulttista verta , pH 5 , albumiini 1+, valkosoluja läsnä ,2-50 punasoluja , 10-20 valkosoluja , joitain bakteereja ja kohtalaisesti virtsarakon epiteelisoluja. FBS alle 200 = 0 yksikköä CZI FBS 201-250 = 2 yksikköä CZI FBS 251-300 = 4 yksikköä CZI FBS 301-350 = 6 yksikköä CZI FBS351-400 = 8 yksikköä CZI FBS suurempi kuin 400 = 10 yksikköä CZI."""

data = spark.createDataFrame([[sample_text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","fi")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical", "fi", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
))

sample_data = Seq("""Potilaan virtsanalyysi 19.10.97 osoitti kohtalaisen okkulttista verta , pH 5 , albumiini 1+, valkosoluja läsnä ,2-50 punasoluja , 10-20 valkosoluja , joitain bakteereja ja kohtalaisesti virtsarakon epiteelisoluja. FBS alle 200 = 0 yksikköä CZI FBS 201-250 = 2 yksikköä CZI FBS 251-300 = 4 yksikköä CZI FBS 301-350 = 6 yksikköä CZI FBS351-400 = 8 yksikköä CZI FBS suurempi kuin 400 = 10 yksikköä CZI.""").toDS.toDF("text")


val result = pipeline.fit(sample_data).transform(sample_data)

```
</div>

## Results

```bash
+----------------------------------------+-----+---+---------+
|chunk                                   |begin|end|ner_label|
+----------------------------------------+-----+---+---------+
|Potilaan virtsanalyysi                  |0    |21 |TEST     |
|kohtalaisen okkulttista verta           |40   |68 |PROBLEM  |
|pH                                      |72   |73 |TEST     |
|albumiini                               |79   |87 |TEST     |
|valkosoluja                             |93   |103|TEST     |
|punasoluja                              |117  |126|TEST     |
|valkosoluja                             |136  |146|TEST     |
|joitain bakteereja                      |150  |167|PROBLEM  |
|kohtalaisesti virtsarakon epiteelisoluja|172  |211|PROBLEM  |
|FBS                                     |214  |216|TEST     |
|CZI                                     |240  |242|TREATMENT|
|FBS                                     |244  |246|TEST     |
|CZI                                     |269  |271|TREATMENT|
|FBS                                     |273  |275|TEST     |
|CZI                                     |298  |300|TREATMENT|
|FBS                                     |302  |304|TEST     |
|CZI                                     |327  |329|TREATMENT|
|FBS351-400                              |331  |340|TEST     |
|CZI                                     |355  |357|TREATMENT|
|FBS                                     |359  |361|TEST     |
|CZI                                     |395  |397|TREATMENT|
+----------------------------------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|fi|
|Size:|2.9 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
   TREATMENT       0.67      0.74      0.70       275
        TEST       0.93      0.73      0.82       350
     PROBLEM       0.73      0.76      0.75       678
   micro-avg       0.76      0.75      0.75      1303
   macro-avg       0.78      0.74      0.76      1303
weighted-avg       0.77      0.75      0.76      1303
```
