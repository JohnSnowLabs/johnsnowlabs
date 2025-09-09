---
layout: model
title: HPO Code To Gene Mapping
author: John Snow Labs
name: hpo_code_gene_mapper
date: 2025-07-28
tags: [licensed, en, gene, hpo, mapping]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.0.4
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps HPO codes to related genes. It also returns all the possible genes in the `all_k_resolutions` in the metadata.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_code_gene_mapper_en_6.0.4_3.0_1753715824444.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_code_gene_mapper_en_6.0.4_3.0_1753715824444.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

chunk_assembler = Doc2Chunk()\
      .setInputCols(["document"])\
      .setOutputCol("hpo_code")

mapperModel = ChunkMapperModel.pretrained("hpo_code_gene_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_code"])\
    .setOutputCol("mappings")\
    .setRels(["gene"])

mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["HP:0000002"],["HP:6001080"],["HP:0009484"]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

chunk_assembler = nlp.Doc2Chunk()\
      .setInputCols(["document"])\
      .setOutputCol("hpo_code")

mapperModel = medical.ChunkMapperModel.pretrained("hpo_code_gene_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_code"])\
    .setOutputCol("mappings")\
    .setRels(["gene"])

mapper_pipeline = nlp.Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["HP:0000002"],["HP:6001080"],["HP:0009484"]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val chunk_assembler = new Doc2Chunk()
      .setInputCols("document")
      .setOutputCol("hpo_code")

val mapperModel = ChunkMapperModel.pretrained("hpo_code_gene_mapper", "en", "clinical/models")
    .setInputCols("hpo_code")
    .setOutputCol("mappings")
    .setRels(Array("gene"))

val mapper_pipeline = new Pipeline().setStages(Array(
    document_assembler,
    chunk_assembler,
    mapperModel
))


val data = Seq("HP:0000002","HP:6001080","HP:0009484").toDF("text")

val result = mapper_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+----------+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  hpo_code|   gene|                                                                                                                                                         all_k_resolutions|
+----------+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|HP:0000002|  DUSP6|DUSP6:::FGF8:::FGFR1:::GNRH1:::GNRHR:::KISS1:::LRP5:::NHLH2:::TAC3:::TACR3:::FGF17:::NOG:::COPB2:::HS6ST1:::NSMF:::CHD7:::WDR11:::PROK2:::SPRY4:::KISS1R:::TMEM67:::PROKR2|
|HP:6001080|HSD11B1|                                                                                                                                                                HSD11B1:::|
|HP:0009484|    SHH|                                                                                                                                                               SHH:::LMBR1|
+----------+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_code_gene_mapper|
|Compatibility:|Healthcare NLP 6.0.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|920.9 KB|
