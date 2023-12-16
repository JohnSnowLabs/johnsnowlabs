---
layout: model
title: Detect Problems, Tests and Treatments (ner_clinical) in Swedish
author: John Snow Labs
name: ner_clinical
date: 2023-09-20
tags: [licensed, clinical, ner, sv]
task: Named Entity Recognition
language: sv
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms in Swedish. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_sv_5.1.0_3.0_1695229037274.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_sv_5.1.0_3.0_1695229037274.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","sv") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "sv", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
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

sample_text = """Patienten hade inga ytterligare klagomål och den 10 mars 2012 var hans vita blodkroppar 2,3, neutrofiler 50%, band 2%, lymfocyter 5% , monocyter 40% och blaster 1%. instruktioner i 250 ml långsam IV-infusion över en timme."""

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

val embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","sv")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical", "sv", "clinical/models")
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

sample_data = Seq("""Patienten hade inga ytterligare klagomål och den 10 mars 2012 var hans vita blodkroppar 2,3, neutrofiler 50%, band 2%, lymfocyter 5% , monocyter 40% och blaster 1%. instruktioner i 250 ml långsam IV-infusion över en timme.""").toDS.toDF("text")


val result = pipeline.fit(sample_data).transform(sample_data)
```
</div>

## Results

```bash
+---------------------+-----+---+---------+
|chunk                |begin|end|ner_label|
+---------------------+-----+---+---------+
|ytterligare klagomål |20   |39 |PROBLEM  |
|hans vita blodkroppar|66   |86 |TEST     |
|neutrofiler          |93   |103|TEST     |
|band                 |110  |113|TEST     |
|lymfocyter           |119  |128|TEST     |
|monocyter            |135  |143|TEST     |
|blaster              |153  |159|TEST     |
|långsam IV-infusion  |188  |206|TREATMENT|
+---------------------+-----+---+---------+
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
|Language:|sv|
|Size:|2.9 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
        TEST       0.86      0.79      0.82       317
     PROBLEM       0.82      0.84      0.83       823
   TREATMENT       0.76      0.73      0.74       396
   micro-avg       0.81      0.80      0.80      1536
   macro-avg       0.81      0.79      0.80      1536
weighted-avg       0.81      0.80      0.80      1536
```
