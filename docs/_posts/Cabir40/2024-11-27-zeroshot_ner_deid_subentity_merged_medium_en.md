---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_deid_subentity_merged_medium)
author: John Snow Labs
name: zeroshot_ner_deid_subentity_merged_medium
date: 2024-11-27
tags: [licensed, clinical, en, ner, deid, zeroshot]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PretrainedZeroShotNER
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Zero-shot Named Entity Recognition (NER) enables the identification of entities in text . With minimal effort, leveraging pre-trained language models and contextual understanding, zero-shot NER expands entity recognition capabilities to new domains and languages, driving advancements in natural language processing and AI applications.

## Predicted Entities

`DOCTOR`, `PATIENT`, `AGE`, `DATE`, `HOSPITAL`, `CITY`, `STREET`, `STATE`, `COUNTRY`, `PHONE`, `IDNUM`, `EMAIL`, `ZIP`, `ORGANIZATION`, `PROFESSION`, `USERNAME`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_subentity_merged_medium_en_5.5.0_3.0_1732701620086.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_subentity_merged_medium_en_5.5.0_3.0_1732701620086.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
 
labels = ['DOCTOR', 'PATIENT', 'AGE', 'DATE', 'HOSPITAL', 'CITY', 'STREET', 'STATE', 'COUNTRY', 'PHONE', 'IDNUM', 'EMAIL','ZIP', 'ORGANIZATION', 'PROFESSION', 'USERNAME']
 
pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_subentity_merged_medium", "en", "clinical/models")\
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

data = spark.createDataFrame([["""Dr. John Taylor, ID: 982345, a cardiologist at St. Mary's Hospital in Boston, was contacted on 05/10/2023 regarding a 45-year-old."""]]).toDF("text")

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
 
labels = ['DOCTOR', 'PATIENT', 'AGE', 'DATE', 'HOSPITAL', 'CITY', 'STREET', 'STATE', 'COUNTRY', 'PHONE', 'IDNUM', 'EMAIL','ZIP', 'ORGANIZATION', 'PROFESSION', 'USERNAME']
 
pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_subentity_merged_medium", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("entities")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)
 
ner_converter = medical.NerConverterInternal()\
    .setInputCols("sentence", "token", "entities")\
    .setOutputCol("ner_chunks_internal")
 
 
pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
])

data = spark.createDataFrame([["""Dr. John Taylor, ID: 982345, a cardiologist at St. Mary's Hospital in Boston, was contacted on 05/10/2023 regarding a 45-year-old."""]]).toDF("text")

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
 
labels = ["DOCTOR", "PATIENT", "AGE", "DATE", "HOSPITAL", "CITY", "STREET", "STATE", "COUNTRY", "PHONE", "IDNUM", "EMAIL", "ZIP", "ORGANIZATION", "PROFESSION", "USERNAME"]
 
val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_subentity_merged_medium", "en", "clinical/models")
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

val data = Seq([["""Dr. John Taylor, ID: 982345, a cardiologist at St. Mary's Hospital in Boston, was contacted on 05/10/2023 regarding a 45-year-old."""]]).toDF("text")

val result = resolver_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------+-------------------+-----+---+----------+
|sentence|              chunk|begin|end| ner_label|
+--------+-------------------+-----+---+----------+
|       0|    Dr. John Taylor|    0| 14|    DOCTOR|
|       0|             982345|   21| 26|     IDNUM|
|       0|       cardiologist|   31| 42|PROFESSION|
|       0|St. Mary's Hospital|   47| 65|  HOSPITAL|
|       0|             Boston|   70| 75|      CITY|
|       0|         05/10/2023|   95|104|      DATE|
|       0|        45-year-old|  118|128|       AGE|
+--------+-------------------+-----+---+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_deid_subentity_merged_medium|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|706.7 MB|
