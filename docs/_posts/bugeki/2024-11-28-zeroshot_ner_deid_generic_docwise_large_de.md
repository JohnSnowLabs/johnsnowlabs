---
layout: model
title: Pretrained Zero-Shot PHI Detection for Deidentification (Zero-shot - Large - Generic - Docwise)
author: John Snow Labs
name: zeroshot_ner_deid_generic_docwise_large
date: 2024-11-28
tags: [licensed, de, ner, deid, zeroshot]
task: Named Entity Recognition
language: de
edition: Healthcare NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PretrainedZeroShotNER
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Zero-shot Named Entity Recognition (NER) enables the identification of entities in text with minimal effort. By leveraging pre-trained language models and contextual understanding, zero-shot NER extends entity recognition capabilities to new domains and languages.
While the model card includes default labels as examples, it is important to highlight that users are not limited to these labels. The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. For best results, it is recommended to use labels that are conceptually similar to the provided defaults.

## Predicted Entities

`DATE`, `NAME`, `LOCATION`, `PROFESSION`, `AGE`, `ID`, `CONTACT`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_generic_docwise_large_de_5.5.0_3.0_1732794412019.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_generic_docwise_large_de_5.5.0_3.0_1732794412019.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

labels = ['AGE', 'CONTACT', 'DATE', 'ID', 'LOCATION', 'NAME', 'PROFESSION']
pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_generic_docwise_large", "de", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("entities")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)

ner_converter = NerConverterInternal()\
    .setInputCols("sentence", "token", "entities")\
    .setOutputCol("ner_chunks_internal")


pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
])

data = spark.createDataFrame([["""Michael Berger wird am Morgen des 12 Dezember 2018 ins St. Elisabeth-Krankenhaus
in Bad Kissingen eingeliefert. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen."""]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

labels = ["AGE", "CONTACT", "DATE", "ID", "LOCATION", "NAME", "PROFESSION"]
val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_generic_docwise_large", "de", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("entities")
    .setPredictionThreshold(0.5)
    .setLabels(labels)

val ner_converter = new NerConverterInternal()    .setInputCols(Array("sentence", "token", "entities"))
    .setOutputCol("ner_chunks_internal")


val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
))

val data = Seq([["""Michael Berger wird am Morgen des 12 Dezember 2018 ins St. Elisabeth-Krankenhaus
in Bad Kissingen eingeliefert. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen."""]]).toDF("text")

val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-------------------------+-----+---+---------+----------+
|chunk                    |begin|end|ner_label|confidence|
+-------------------------+-----+---+---------+----------+
|Michael Berger           |1    |14 |NAME     |0.9996613 |
|12 Dezember 2018         |35   |50 |DATE     |0.9999614 |
|St. Elisabeth-Krankenhaus|56   |80 |LOCATION |0.9775322 |
|Bad Kissingen            |85   |97 |LOCATION |0.9796306 |
|Berger                   |118  |123|NAME     |0.7341295 |
|76                       |129  |130|AGE      |0.99980086|
+-------------------------+-----+---+---------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_deid_generic_docwise_large|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|de|
|Size:|1.6 GB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support

         AGE    0.9567    0.9918    0.9739      245
     CONTACT    0.7778    0.8235       0.8       17
        DATE    0.9767         1    0.9882      126
          ID    0.8330    0.8621    0.8475       29
    LOCATION    0.8438     0.924     0.882      263
        NAME    0.9742    0.9326    0.9529      445
  PROFESSION    0.6552    0.9383    0.7716       81

    accuracy                        0.9841     10352
   macro avg    0.8766    0.9327    0.9010     10352
weighted avg    0.9856    0.9841    0.9846     10352
```
