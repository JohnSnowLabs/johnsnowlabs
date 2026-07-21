---
layout: model
title: Mapping HPO Codes with Their Corresponding EOM Ids
author: John Snow Labs
name: hpo_code_eom_mapper
date: 2026-07-21
tags: [en, chunk_mapper, licensed, clinical, hpo, eom]
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

This model maps HPO codes to their associated Elements of Morphology (EOM) id(s), based on the HPO project's own EOM crosswalk. Codes linked to more than one EOM id return every associated id via the `all_k_resolutions` metadata field. Trained on the Human Phenotype Ontology (HPO) 2026-06-23 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_code_eom_mapper_en_6.4.0_3.4_1784646871487.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_code_eom_mapper_en_6.4.0_3.4_1784646871487.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

hpo_code_eom_mapper = ChunkMapperModel.pretrained("hpo_code_eom_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_code"])\
    .setOutputCol("mappings")\
    .setRels(["eom"])

pipeline = Pipeline(stages=[document_assembler, chunk_assembler, hpo_code_eom_mapper])
data = spark.createDataFrame([["HP:0000154"], ["HP:0400001"], ["HP:0009765"]]).toDF("text")
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

hpo_code_eom_mapper = medical.ChunkMapperModel.pretrained("hpo_code_eom_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_code"])\
    .setOutputCol("mappings")\
    .setRels(["eom"])

pipeline = nlp.Pipeline(stages=[document_assembler, chunk_assembler, hpo_code_eom_mapper])
data = spark.createDataFrame([["HP:0000154"], ["HP:0400001"], ["HP:0009765"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val chunkAssembler = new Doc2Chunk()
    .setInputCols("document")
    .setOutputCol("hpo_code")

val hpoCodeEomMapper = ChunkMapperModel
    .pretrained("hpo_code_eom_mapper", "en", "clinical/models")
    .setInputCols(Array("hpo_code"))
    .setOutputCol("mappings")
    .setRels(Array("eom"))

val pipeline = new Pipeline().setStages(Array(documentAssembler, chunkAssembler, hpoCodeEomMapper))
val data = Seq("HP:0000154", "HP:0400001", "HP:0009765").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| hpo_code   | eom                  | all_k_resolutions       |
|:-----------|:---------------------|:------------------------|
| HP:0000154 | EOM:a6a2d57a281ead72 | EOM:a6a2d57a281ead72::: |
| HP:0400001 | EOM:8a5493c72e0dd13c | EOM:8a5493c72e0dd13c::: |
| HP:0009765 | EOM:49acd433e354541b | EOM:49acd433e354541b::: |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_code_eom_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|10.3 KB|