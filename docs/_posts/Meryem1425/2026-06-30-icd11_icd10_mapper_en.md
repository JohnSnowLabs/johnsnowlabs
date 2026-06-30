---
layout: model
title: Mapping ICD11 Codes with Their Corresponding ICD10 Codes (icd11_icd10_mapper)
author: John Snow Labs
name: icd11_icd10_mapper
date: 2026-06-30
tags: [licensed, en, mapper, icd10, icd11, clinical]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts to ICD11 codes to ICD10 codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd11_icd10_mapper_en_6.4.1_3.0_1782833571824.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd11_icd10_mapper_en_6.4.1_3.0_1782833571824.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

doc2chunk = Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("ner_chunk")

mapper = ChunkMapperModel.pretrained("icd11_icd10_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")

pipeline = Pipeline().setStages([
    document_assembler,
    doc2chunk,
    mapper
])

data = spark.createDataFrame([["""[["3A00.01"],["7A00"],["3A00.01"],["BA00.0"]]"""]]).toDF("text")

result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

doc2chunk = nlp.Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("ner_chunk")

mapper = nlp.ChunkMapperModel.pretrained("icd11_icd10_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    doc2chunk,
    mapper
])

data = spark.createDataFrame([["""[["3A00.01"],["7A00"],["3A00.01"],["BA00.0"]]"""]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val doc2chunk = new Doc2Chunk()
    .setInputCols(Array("document"))
    .setOutputCol("ner_chunk")

val mapper = ChunkMapperModel.pretrained("icd11_icd10_mapper","en","clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    doc2chunk,
    mapper
))

val data = Seq(Array("3A00.01","7A00","3A00.01","BA00.0")).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
"
+----------+----------+
|icd11_code|icd10_code|
+----------+----------+
|3A00.01   |[D50.0]   |
|7A00      |[F51.0]   |
|3A00.01   |[D50.0]   |
|BA00.0    |[I10]     |
+----------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd11_icd10_mapper|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|213.7 KB|
