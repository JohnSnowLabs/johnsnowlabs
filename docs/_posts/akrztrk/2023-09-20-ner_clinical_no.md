---
layout: model
title: Detect Problems, Tests and Treatments (ner_clinical) in Norwegian
author: John Snow Labs
name: ner_clinical
date: 2023-09-20
tags: [ner, clinical, licensed, "no"]
task: Named Entity Recognition
language: "no"
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms in Norwegian. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_no_5.1.0_3.0_1695229936666.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_no_5.1.0_3.0_1695229936666.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","no") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "no", "clinical/models") \
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

sample_text = """Natrium var 140, kalium 3,7 ,klorid 96, bikarbonat 30, BUN og kreatinin 14/0,9 , glukose105, hematokrit42, hvittblodtall 8,6 , blodplater 644, protrombintid 10,4 , delvis tromboplastintid 28,7 , urinanalyse spor av hvite blodceller, svake skjulte røde blodceller."""


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

val embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","no")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical", "no", "clinical/models")
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

sample_data = Seq("""Natrium var 140, kalium 3,7 ,klorid 96, bikarbonat 30, BUN og kreatinin 14/0,9 , glukose105, hematokrit42, hvittblodtall 8,6 , blodplater 644, protrombintid 10,4 , delvis tromboplastintid 28,7 , urinanalyse spor av hvite blodceller, svake skjulte røde blodceller.""").toDS.toDF("text")


val result = pipeline.fit(sample_data).transform(sample_data)
```
</div>

## Results

```bash
+-----------------------------+-----+---+---------+
|chunk                        |begin|end|ner_label|
+-----------------------------+-----+---+---------+
|Natrium                      |0    |6  |TEST     |
|kalium                       |17   |22 |TEST     |
|klorid                       |29   |34 |TEST     |
|bikarbonat                   |40   |49 |TEST     |
|BUN                          |55   |57 |TEST     |
|kreatinin                    |62   |70 |TEST     |
|glukose105                   |81   |90 |TEST     |
|hematokrit42                 |93   |104|TEST     |
|hvittblodtall                |107  |119|TEST     |
|blodplater                   |127  |136|TEST     |
|protrombintid                |143  |155|TEST     |
|delvis tromboplastintid      |164  |186|TEST     |
|urinanalyse                  |195  |205|TEST     |
|spor av hvite blodceller     |207  |230|PROBLEM  |
|svake skjulte røde blodceller|233  |261|PROBLEM  |
+-----------------------------+-----+---+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|no|
|Size:|2.9 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
   TREATMENT       0.69      0.75      0.72       358
        TEST       0.89      0.87      0.88       415
     PROBLEM       0.88      0.74      0.81       749
   micro-avg       0.83      0.78      0.81      1522
   macro-avg       0.82      0.79      0.80      1522
weighted-avg       0.84      0.78      0.81      1522
```