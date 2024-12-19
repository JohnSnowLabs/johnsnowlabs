---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_deid_subentity_merged_large)
author: John Snow Labs
name: zeroshot_ner_deid_subentity_merged_large
date: 2024-12-17
tags: [licensed, en, ner, zeroshot, clinical, deid, subentity]
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

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_subentity_merged_large_en_5.5.1_3.0_1734472523759.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_subentity_merged_large_en_5.5.1_3.0_1734472523759.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

labels =["DOCTOR", "PATIENT", "AGE", "DATE", "HOSPITAL", "CITY", "STREET", "STATE", "COUNTRY", "PHONE", "IDNUM", "EMAIL", "ZIP", "ORGANIZATION", "PROFESSION", "USERNAME"]

pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_subentity_merged_large", "en", "clinical/models")\
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

data = spark.createDataFrame([["""Record date: 2093-01-13, Age: 25, # 719435. Dr. John Green,  Phone (302) 786-5227, 0295 Keats Street, San Francisco.
Jennifer Smith is 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM),
one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting."""]]).toDF("text")

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

labels =["DOCTOR", "PATIENT", "AGE", "DATE", "HOSPITAL", "CITY", "STREET", "STATE", "COUNTRY", "PHONE", "IDNUM", "EMAIL", "ZIP", "ORGANIZATION", "PROFESSION", "USERNAME"]

pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_subentity_merged_large", "en", "clinical/models")\
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

data = spark.createDataFrame([["""Record date: 2093-01-13, Age: 25, # 719435. Dr. John Green,  Phone (302) 786-5227, 0295 Keats Street, San Francisco.
Jennifer Smith is 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM),
one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting."""]]).toDF("text")

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

val labels = Array("DOCTOR", "PATIENT", "AGE", "DATE", "HOSPITAL", "CITY", "STREET", "STATE", "COUNTRY", "PHONE", "IDNUM", "EMAIL", "ZIP", "ORGANIZATION", "PROFESSION", "USERNAME")

val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_subentity_merged_large", "en", "clinical/models")
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

val data = Seq("""Record date: 2093-01-13, Age: 25, # 719435. Dr. John Green,  Phone (302) 786-5227, 0295 Keats Street, San Francisco.
Jennifer Smith is 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM),
one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------------+-----+---+---------+----------+
|chunk            |begin|end|ner_label|confidence|
+-----------------+-----+---+---------+----------+
|2093-01-13       |13   |22 |DATE     |0.99999905|
|25               |30   |31 |AGE      |0.9999857 |
|719435           |36   |41 |IDNUM    |0.9999993 |
|John Green       |48   |57 |DOCTOR   |0.99999964|
|(302) 786-5227   |67   |80 |PHONE    |0.9998485 |
|0295 Keats Street|83   |99 |STREET   |0.9999916 |
|San Francisco    |102  |114|CITY     |0.9996729 |
|Jennifer Smith   |117  |130|PATIENT  |0.99999857|
|28-year-old      |135  |145|AGE      |0.99997365|
+-----------------+-----+---+---------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_deid_subentity_merged_large|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|