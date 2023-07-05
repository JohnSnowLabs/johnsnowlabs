---
layout: model
title: Detect Problems, Tests and Treatments (Dutch)
author: John Snow Labs
name: ner_clinical
date: 2023-07-05
tags: [licensed, nl, clinical, ner]
task: Named Entity Recognition
language: nl
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms. The SparkNLP deep learning model (NerDL) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_nl_4.4.4_3.0_1688590137805.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_nl_4.4.4_3.0_1688590137805.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d", "nl")\
  .setInputCols(["sentence", "token"])\
  .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "nl", "clinical/models")\
  .setInputCols(["sentence", "token","embeddings"])\
  .setOutputCol("ner")

ner_converter = NerConverterInternal()\
.setInputCols(['sentence', 'token', 'ner'])\
.setOutputCol('ner_chunk')

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
    ])

sample_df = spark.createDataFrame([["Dhr. Van Dijk, 58 jaar oud, kwam naar de kliniek met klachten van aanhoudende hoest, koorts en kortademigheid. We hebben besloten om een röntgenfoto van de borst, bloedonderzoek en een CT-scan te laten uitvoeren. De resultaten wezen op een ernstige longontsteking, een verhoogd aantal witte bloedcellen en mogelijk COPD. Hem is een antibiotica kuur en een sterke hoestsiroop voorgeschreven. Daarnaast adviseren we hem een voedzaam dieet te volgen."]]).toDF("text")

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

val embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d", "nl")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical", "nl", "clinical/models")
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
    ner_converter))

val sample_data = Seq("Dhr. Van Dijk, 58 jaar oud, kwam naar de kliniek met klachten van aanhoudende hoest, koorts en kortademigheid. We hebben besloten om een röntgenfoto van de borst, bloedonderzoek en een CT-scan te laten uitvoeren. De resultaten wezen op een ernstige longontsteking, een verhoogd aantal witte bloedcellen en mogelijk COPD. Hem is een antibiotica kuur en een sterke hoestsiroop voorgeschreven. Daarnaast adviseren we hem een voedzaam dieet te volgen.").toDS.toDF("text")

val result = pipeline.fit(sample_data).transform(sample_data)
```
</div>

## Results

```bash
+-------------------------------------+-----+---+---------+----------+
|chunk                                |begin|end|ner_label|confidence|
+-------------------------------------+-----+---+---------+----------+
|aanhoudende hoest                    |66   |82 |PROBLEM  |0.8191    |
|koorts                               |85   |90 |PROBLEM  |0.9932    |
|kortademigheid                       |95   |108|PROBLEM  |0.9917    |
|röntgenfoto van de borst             |137  |160|TEST     |0.60539997|
|bloedonderzoek                       |163  |176|TEST     |0.9186    |
|een CT-scan                          |181  |191|TEST     |0.7307    |
|ernstige longontsteking              |240  |262|PROBLEM  |0.7775    |
|een verhoogd aantal witte bloedcellen|265  |301|PROBLEM  |0.45136   |
|COPD                                 |315  |318|PROBLEM  |0.9806    |
|antibiotica kuur                     |332  |347|TREATMENT|0.62645   |
|een sterke hoestsiroop               |352  |373|TREATMENT|0.4657    |
|een voedzaam dieet                   |418  |435|TREATMENT|0.6946666 |
+-------------------------------------+-----+---+---------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token, embeddings]|
|Output Labels:|[ner]|
|Language:|nl|
|Size:|888.0 KB|

## Benchmarking

```bash
       label   precision  recall  f1-score   support
     PROBLEM        0.68    0.71      0.69       434
        TEST        0.79    0.83      0.81       377
   TREATMENT        0.71    0.80      0.75       271
   micro-avg        0.73    0.77      0.75      1082
   macro-avg        0.73    0.78      0.75      1082
weighted-avg        0.73    0.77      0.75      1082
```
