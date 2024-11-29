---
layout: model
title: Pretrained Zero-Shot PHI Detection for Deidentification (Zero-shot - Large - Subentity - Docwise)
author: John Snow Labs
name: zeroshot_ner_deid_subentity_docwise_large
date: 2024-11-29
tags: [licensed, en, ner, deid, zeroshot]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.5.1
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

`DATE`, `PATIENT`, `COUNTRY`, `PROFESSION`, `AGE`, `CITY`, `STATE`, `DOCTOR`, `HOSPITAL`, `IDNUM`, `ORGANIZATION`, `PHONE`, `STREET`, `ZIP`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_subentity_docwise_large_en_5.5.1_3.0_1732869419665.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_subentity_docwise_large_en_5.5.1_3.0_1732869419665.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

labels = ["AGE", "CITY", "COUNTRY", "DATE", "DOCTOR", "HOSPITAL", "IDNUM", "ORGANIZATION",
          "PATIENT", "PHONE", "PROFESSION", "STATE", "STREET", "ZIP"]

pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_subentity_docwise_large", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("ner")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)

ner_converter = NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")


pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
])

data = spark.createDataFrame([["""Emily Davis, a 34-year-old woman, Dr. Michael Johnson cares wit her, at CarePlus Clinic, located at 456 Elm Street, NewYork, NY has recommended starting insulin therapy. She has an appointment scheduled for March 15, 2024."""]]).toDF("text")

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

labels = ["AGE", "CITY", "COUNTRY", "DATE", "DOCTOR", "HOSPITAL", "IDNUM", "ORGANIZATION",
          "PATIENT", "PHONE", "PROFESSION", "STATE", "STREET", "ZIP"]

val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_subentity_docwise_large", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("ner")
    .setPredictionThreshold(0.5)
    .setLabels(labels)

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")


val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
))

val data = Seq([["""Emily Davis, a 34-year-old woman, Dr. Michael Johnson cares wit her, at CarePlus Clinic, located at 456 Elm Street, NewYork, NY has recommended starting insulin therapy. She has an appointment scheduled for March 15, 2024."""]]).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+---------------+-----+---+---------+----------+
|chunk          |begin|end|ner_label|confidence|
+---------------+-----+---+---------+----------+
|Emily Davis    |1    |11 |PATIENT  |0.9994733 |
|34-year-old    |16   |26 |AGE      |0.99977213|
|Michael Johnson|39   |53 |DOCTOR   |0.9995535 |
|CarePlus Clinic|73   |87 |HOSPITAL |0.9834484 |
|456 Elm Street |101  |114|STREET   |0.9990957 |
|NewYork        |117  |123|CITY     |0.9991258 |
|NY             |126  |127|STATE    |0.9988438 |
|March 15, 2024 |208  |221|DATE     |0.999948  |
+---------------+-----+---+---------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_deid_subentity_docwise_large|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|

       label  precision    recall  f1-score   support

         AGE     0.9392    0.9348    0.9370      1074
        CITY     0.8367    0.9467    0.8883       525
     COUNTRY     0.8750    0.8652    0.8701       178
        DATE     0.9895    0.9811    0.9853      7995
      DOCTOR     0.9766    0.9513    0.9638      5134
    HOSPITAL     0.8680    0.9130    0.8899      2276
       IDNUM     0.9322    0.8785    0.9046       955
           O     0.9980    0.9977    0.9978    315085
ORGANIZATION     0.7696    0.7778    0.7737       189
     PATIENT     0.8996    0.9590    0.9283      2364
       PHONE     0.9375    0.9146    0.9259       492
  PROFESSION     0.9213    0.9474    0.9341       494
       STATE     0.8671    0.9503    0.9068       302
      STREET     0.9882    0.9653    0.9766       605
         ZIP     0.8874    0.9949    0.9381       198

    accuracy                         0.9946    337866
   macro avg     0.9124    0.9318    0.9214    337866
weighted avg     0.9947    0.9946    0.9946    337866
