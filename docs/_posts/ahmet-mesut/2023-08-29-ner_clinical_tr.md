---
layout: model
title: Detect Problems, Tests, and Treatments (Turkish)
author: John Snow Labs
name: ner_clinical
date: 2023-08-29
tags: [licensed, clinical, ner, tr]
task: Named Entity Recognition
language: tr
edition: Healthcare NLP 5.0.2
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms in Turkish. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state-of-the-art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_tr_5.0.2_3.0_1693344151891.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_tr_5.0.2_3.0_1693344151891.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","tr") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "tr", "clinical/models")\
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

sample_text = """Hasta sıcak ve soğuk yiyecekler yerken diş hassasiyetinden şikayetçiydi. 
                 Olası çürük veya diş kökü problemlerini değerlendirmek için klinik ve radyografik muayene yapıldı ve diş köküne yakın bir boşluk tespit edildi.
                 Sorunu gidermek için restoratif tedavi uygulandı."""

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

val embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","tr")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical", "tr", "clinical/models")
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

val sample_data = Seq("""Hasta sıcak ve soğuk yiyecekler yerken diş hassasiyetinden şikayetçiydi. 
                 Olası çürük veya diş kökü problemlerini değerlendirmek için klinik ve radyografik muayene yapıldı ve diş köküne yakın bir boşluk tespit edildi.
                 Sorunu gidermek için restoratif tedavi uygulandı.""").toDS.toDF("text")

val result = pipeline.fit(sample_data).transform(sample_data)
```
</div>

## Results

```bash
+---------------------------------------+-----+---+---------+
|chunk                                  |begin|end|ner_label|
+---------------------------------------+-----+---+---------+
|soğuk yiyecekler yerken diş hassasiyeti|18   |56 |PROBLEM  |
|radyografik muayene                    |144  |162|TEST     |
|restoratif tedavi                      |234  |250|TREATMENT|
+---------------------------------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical|
|Compatibility:|Healthcare NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|tr|
|Size:|2.9 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
        TEST       0.86      0.80      0.83       404
   TREATMENT       0.77      0.73      0.75       393
     PROBLEM       0.78      0.76      0.77       841
   micro_avg       0.79      0.76      0.78      1638
   macro_avg       0.80      0.76      0.78      1638
weighted_avg       0.79      0.76      0.78      1638
```