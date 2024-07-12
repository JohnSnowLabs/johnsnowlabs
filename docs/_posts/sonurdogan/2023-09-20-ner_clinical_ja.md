---
layout: model
title: Detect Problems, Tests and Treatments (ner_clinical) in Japanese
author: John Snow Labs
name: ner_clinical
date: 2023-09-20
tags: [ner, clinical, licensed, ja]
task: Named Entity Recognition
language: ja
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms in Japanese. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_ja_5.1.0_3.0_1695242153966.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_ja_5.1.0_3.0_1695242153966.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

clinical_embeddings = BertEmbeddings.pretrained("bert_embeddings_bert_large_japanese","ja") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "ja", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])

sample_df = spark.createDataFrame([["""中等度肺高血圧 、 PA圧 48/24、 1+僧帽弁逆流 、 重度大動脈弁狭窄 、 LVEDP 19、 駆出率 43%。 クロトリマゾール 、1錠 p.o . q.i.d .;"""]]).toDF("text")

result = pipeline.fit(sample_df).transform(sample_df)
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

val clinical_embeddings = BertEmbeddings.pretrained("bert_embeddings_bert_large_japanese","ja")
    .setInputCols(Array("document", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical", "ja", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter))

val sample_data = Seq("""中等度肺高血圧 、 PA圧 48/24、 1+僧帽弁逆流 、 重度大動脈弁狭窄 、 LVEDP 19、 駆出率 43%。 クロトリマゾール 、1錠 p.o . q.i.d .;""").toDS.toDF("text")

val result = pipeline.fit(sample_data).transform(sample_data)
```
</div>

## Results

```bash
+----------------+-----+---+---------+
|chunk           |begin|end|ner_label|
+----------------+-----+---+---------+
|中等度肺高血圧  |0    |6  |PROBLEM  |
|PA圧            |10   |12 |TEST     |
|1+僧帽弁逆流    |21   |27 |PROBLEM  |
|重度大動脈弁狭窄|31   |38 |PROBLEM  |
|LVEDP           |42   |46 |TEST     |
|駆出率          |52   |54 |TEST     |
|クロトリマゾール|61   |68 |TREATMENT|
+----------------+-----+---+---------+
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
|Language:|ja|
|Size:|4.3 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
        TEST       0.90      0.90      0.90       105
     PROBLEM       0.86      0.90      0.89       134
   TREATMENT       0.71      0.61      0.66        36
   micro-avg       0.86      0.86      0.86       275
   macro-avg       0.83      0.80      0.81       275
weighted-avg       0.86      0.86      0.86       275
```
