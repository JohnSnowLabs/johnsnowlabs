---
layout: model
title: HPO Code To Gene, Gene To Disease Mapping
author: John Snow Labs
name: hpo_code_gene_disease_mapper
date: 2025-08-05
tags: [licensed, en, gene, disease, mapping, hpo]
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

This pretrained model maps HPO codes to their associated genes and further maps those genes to related diseases.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_code_gene_disease_mapper_en_6.0.4_3.0_1754424435921.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_code_gene_disease_mapper_en_6.0.4_3.0_1754424435921.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

mapperModel = ChunkMapperModel.pretrained("hpo_code_gene_disease_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_code"])\
    .setOutputCol("mappings")\
    .setRels(["hpo_gene_disease"])

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

mapperModel = medical.ChunkMapperModel.pretrained("hpo_code_gene_disease_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_code"])\
    .setOutputCol("mappings")\
    .setRels(["hpo_gene_disease"])

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

val mapperModel = ChunkMapperModel.pretrained("hpo_code_gene_disease_mapper", "en", "clinical/models")
    .setInputCols("hpo_code")
    .setOutputCol("mappings")
    .setRels(Array("hpo_gene_disease"))

val mapper_pipeline = new Pipeline().setStages(Array(
    document_assembler,
    chunk_assembler,
    mapperModel
))


val data = Seq(("HP:0000002"),("HP:6001080"),("HP:0009484")).toDF("text")

val result = mapper_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+----------+------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
|  hpo_code|                                                                                                            gene_disease|                                                                                                       all_k_resolutions|
+----------+------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
|HP:0000002|{"DUSP6": ["eunuchoid habitus", "gait disturbance", "seizure", "hypotonia", "ataxia", "dysarthria", "decreased testic...|{"DUSP6": ["eunuchoid habitus", "gait disturbance", "seizure", "hypotonia", "ataxia", "dysarthria", "decreased testic...|
|HP:6001080|{"HSD11B1": ["autosomal dominant inheritance", "low tetrahydrocortisol (thf) plus 5-alpha-thf/tetrahydrocortisone (th...|{"HSD11B1": ["autosomal dominant inheritance", "low tetrahydrocortisol (thf) plus 5-alpha-thf/tetrahydrocortisone (th...|
|HP:0009484|{"SHH": ["abnormal thumb morphology", "hand polydactyly", "poor speech", "expressive language delay", "limb dystonia"...|{"SHH": ["abnormal thumb morphology", "hand polydactyly", "poor speech", "expressive language delay", "limb dystonia"...|
+----------+------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_code_gene_disease_mapper|
|Compatibility:|Healthcare NLP 6.0.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|113.2 MB|
