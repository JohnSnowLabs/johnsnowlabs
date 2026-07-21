---
layout: model
title: Mapping HPO Codes with Their Corresponding Diseases
author: John Snow Labs
name: hpo_disease_mapper
date: 2026-07-21
tags: [en, chunk_mapper, licensed, clinical, hpo, disease]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.4
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps HPO codes to the real disease(s) they are associated with, based on the Human Phenotype Ontology's own phenotype-disease annotations (OMIM, Orphanet, and DECIPHER identifiers). Two positionally-aligned relations are available: `disease_id` and `disease_name`. Trained on the Human Phenotype Ontology (HPO) 2026-06-23 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_disease_mapper_en_6.4.0_3.4_1784666560448.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_disease_mapper_en_6.4.0_3.4_1784666560448.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

hpo_disease_mapper = ChunkMapperModel.pretrained("hpo_disease_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_code"])\
    .setOutputCol("mappings")\
    .setRels(["disease_id"])  # or disease_name

pipeline = Pipeline(stages=[document_assembler, chunk_assembler, hpo_disease_mapper])
data = spark.createDataFrame([["HP:0000025"], ["HP:0000058"], ["HP:0000002"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

chunk_assembler = nlp.Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("hpo_code")

hpo_disease_mapper = medical.ChunkMapperModel.pretrained("hpo_disease_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_code"])\
    .setOutputCol("mappings")\
    .setRels(["disease_id"])  # or disease_name

pipeline = nlp.Pipeline(stages=[document_assembler, chunk_assembler, hpo_disease_mapper])
data = spark.createDataFrame([["HP:0000025"], ["HP:0000058"], ["HP:0000002"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val chunkAssembler = new Doc2Chunk()
    .setInputCols("document")
    .setOutputCol("hpo_code")

val hpoDiseaseMapper = ChunkMapperModel
    .pretrained("hpo_disease_mapper", "en", "clinical/models")
    .setInputCols(Array("hpo_code"))
    .setOutputCol("mappings")
    .setRels(Array("disease_id"))  // or disease_name

val pipeline = new Pipeline().setStages(Array(documentAssembler, chunkAssembler, hpoDiseaseMapper))
val data = Seq("HP:0000025", "HP:0000058", "HP:0000002").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| hpo_code   |   n_diseases | disease_id   | all_k_resolutions                                                                                                                         |
|:-----------|-------------:|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------|
| HP:0000025 |            1 | ORPHA:904    | ORPHA:904:::                                                                                                                              |
| HP:0000058 |            3 | ORPHA:251510 | ORPHA:251510:::ORPHA:37202:::ORPHA:325345                                                                                                 |
| HP:0000002 |           10 | OMIM:144750  | OMIM:144750:::OMIM:186570:::OMIM:617800:::OMIM:621382:::OMIM:621091:::OMIM:612475:::OMIM:616977:::ORPHA:209964:::ORPHA:140976:::ORPHA:432 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_disease_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|4.6 MB|