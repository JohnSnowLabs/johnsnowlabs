---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_deid_generic_multi_medium)
author: John Snow Labs
name: zeroshot_ner_deid_generic_multi_medium
date: 2024-12-21
tags: [licensed, ner, multilingual, xx, deidentification, zeroshot, clinical]
task: Named Entity Recognition
language: xx
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

`AGE`, `CONTACT`, `DATE`, `ID`, `LOCATION`, `NAME`, `PROFESSION`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_generic_multi_medium_xx_5.5.1_3.0_1734802677175.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_generic_multi_medium_xx_5.5.1_3.0_1734802677175.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

labels = ['AGE', 'CONTACT', 'DATE', 'ID', 'LOCATION', 'NAME', 'PROFESSION'] # You can change the entities
pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_generic_multi_medium", "xx", "clinical/models")\
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

data = spark.createDataFrame(pd.DataFrame({"text": text_list}))

result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

labels = ['AGE', 'CONTACT', 'DATE', 'ID', 'LOCATION', 'NAME', 'PROFESSION'] # You can change the entities
pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_generic_multi_medium", "xx", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("ner")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)

ner_converter = medical.NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
])

data = spark.createDataFrame(pd.DataFrame({"text": text_list}))

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

labels = ("AGE", "CONTACT", "DATE", "ID", "LOCATION", "NAME", "PROFESSION") # You can change the entities
val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_generic_multi_medium", "xx", "clinical/models")
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

val data = Seq(text_list).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------------------------+-----+---+----------+----------+
|chunk                        |begin|end|ner_label |confidence|
+-----------------------------+-----+---+----------+----------+
|2093-01-13                   |14   |23 |DATE      |0.99615186|
|David Hale                   |26   |35 |NAME      |0.98314935|
|Hendrickson, Ora             |51   |66 |NAME      |0.96979237|
|7194334                      |74   |80 |ID        |0.9644373 |
|01/13/93                     |89   |96 |DATE      |0.9986671 |
|Oliveira                     |104  |111|NAME      |0.99810505|
|25                           |114  |115|AGE       |0.9994655 |
|1-11-2000                    |142  |150|DATE      |0.9994399 |
|Cocke County Baptist Hospital|153  |181|LOCATION  |0.99385923|
|0295 Keats Street            |184  |200|LOCATION  |0.89783734|
|+1 (302) 786-5227            |209  |225|CONTACT   |0.9993845 |
|Brothers Coal-Mine           |292  |309|LOCATION  |0.992808  |
|Michel Martinez              |24   |38 |NAME      |0.9997186 |
|49 ans                       |41   |46 |AGE       |0.98479503|
|Centre Hospitalier De Plaisir|60   |88 |LOCATION  |0.9974356 |
|Mars 2015                    |148  |156|DATE      |0.998803  |
|Michael Berger               |0    |13 |NAME      |0.99908125|
|12 Dezember 2018             |34   |49 |DATE      |0.9974299 |
|St. Elisabeth-Krankenhaus    |55   |79 |LOCATION  |0.98758394|
|Bad Kissingen                |84   |96 |LOCATION  |0.99479914|
|76                           |128  |129|AGE       |0.999879  |
|Gastone Montanariello        |9    |29 |NAME      |0.9998877 |
|49                           |32   |33 |AGE       |0.9993649 |
|Ospedale San Camillo         |55   |74 |LOCATION  |0.9952013 |
|marzo 2015                   |128  |137|DATE      |0.99773514|
|Antonio Miguel               |0    |13 |NAME      |0.99518305|
|35                           |37   |38 |AGE       |0.99973243|
|auxiliar de                  |67   |77 |PROFESSION|0.99798226|
|Cadiz                        |102  |106|LOCATION  |0.9954631 |
|14 de Marzo                  |172  |182|DATE      |0.80013317|
|Clinica San Carlos           |258  |275|LOCATION  |0.98601055|
|Pedro Gonçalves              |41   |55 |NAME      |0.9709792 |
|2569870                      |62   |68 |ID        |0.96495014|
|Rua Das Flores 23            |81   |97 |LOCATION  |0.9807811 |
|Porto                        |119  |123|LOCATION  |0.9970907 |
|21754-987                    |141  |149|ID        |0.94950974|
|10/10/1963                   |191  |200|DATE      |0.9991333 |
|53                           |210  |211|AGE       |0.99909186|
|17/06/2016                   |248  |257|DATE      |0.99890924|
|Maria Santos                 |269  |280|NAME      |0.9983767 |
|Spitalul Pentru Ochi de Deal |0    |27 |LOCATION  |0.9891909 |
|Drumul Oprea Nr. 972         |30   |49 |LOCATION  |0.81992376|
|Vaslui                       |51   |56 |LOCATION  |0.99835473|
|737405                       |59   |64 |LOCATION  |0.9978582 |
|România                      |66   |72 |LOCATION  |0.9882665 |
|+40(235)413773               |79   |92 |CONTACT   |0.99975044|
|25 May 2022                  |119  |129|DATE      |0.99882215|
|BUREAN MARIA                 |158  |169|NAME      |0.9974591 |
|77                           |180  |181|AGE       |0.9999099 |
|Agota Evelyn                 |191  |202|NAME      |0.8714715 |
|2450502264401                |218  |230|ID        |0.9667498 |
+-----------------------------+-----+---+----------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_deid_generic_multi_medium|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|xx|
|Size:|713.9 MB|

## Benchmarking

```bash

       label  precision    recall  f1-score   support
         AGE       0.95      0.97      0.96      3355
     CONTACT       0.97      0.74      0.84      1444
        DATE       0.82      0.95      0.88      2272
          ID       0.83      0.86      0.85       967
    LOCATION       0.88      0.88      0.88      7470
        NAME       0.93      0.92      0.92      5375
           O       0.98      0.98      0.98    116684
  PROFESSION       0.85      0.90      0.87      2698
    accuracy          -         -      0.97    140265
   macro avg       0.90      0.90      0.90    140265
weighted avg       0.97      0.97      0.97    140265

```