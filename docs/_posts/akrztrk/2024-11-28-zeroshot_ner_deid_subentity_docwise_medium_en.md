---
layout: model
title: Pretrained Zero-Shot PHI Detection for Deidentification (Zero-shot - Medium - Subentity - Docwise)
author: John Snow Labs
name: zeroshot_ner_deid_subentity_docwise_medium
date: 2024-11-28
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_subentity_docwise_medium_en_5.5.1_3.0_1732834164971.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_subentity_docwise_medium_en_5.5.1_3.0_1732834164971.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_subentity_docwise_medium", "en", "clinical/models")\
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

labels = Array("AGE", "CITY", "COUNTRY", "DATE", "DOCTOR", "HOSPITAL", "IDNUM", "ORGANIZATION", 
          "PATIENT", "PHONE", "PROFESSION", "STATE", "STREET", "ZIP")

val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_subentity_docwise_medium", "en", "clinical/models")
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
|Emily Davis    |1    |11 |PATIENT  |0.99571335|
|34-year-old    |16   |26 |AGE      |0.99942374|
|Michael Johnson|39   |53 |DOCTOR   |0.99911386|
|CarePlus Clinic|73   |87 |HOSPITAL |0.87801534|
|456 Elm Street |101  |114|STREET   |0.99828523|
|NewYork        |117  |123|CITY     |0.9850912 |
|NY             |126  |127|STATE    |0.9824218 |
|March 15, 2024 |208  |221|DATE     |0.9994097 |
+---------------+-----+---+---------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_deid_subentity_docwise_medium|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|711.7 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
         AGE     0.8287    0.9367    0.8794      1074
        CITY     0.7973    0.9067    0.8485       525
     COUNTRY     0.8430    0.8146    0.8286       178
        DATE     0.9867    0.9675    0.9770      7995
      DOCTOR     0.9698    0.9125    0.9403      5134
    HOSPITAL     0.8397    0.8379    0.8388      2276
       IDNUM     0.8720    0.5780    0.6952       955
           O     0.9965    0.9959    0.9962    315085
ORGANIZATION     0.5846    0.6032    0.5938       189
     PATIENT     0.8419    0.9547    0.8947      2364
       PHONE     0.6293    0.8455    0.7216       492
  PROFESSION     0.7300    0.9028    0.8072       494
       STATE     0.6954    0.9073    0.7874       302
      STREET     0.8969    0.9636    0.9291       605
         ZIP     0.8879    1.0000    0.9406       198
    accuracy                         0.9903    337866
   macro avg     0.8267    0.8751    0.8452    337866
weighted avg     0.9908    0.9903    0.9904    337866
```
