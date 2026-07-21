---
layout: model
title: Mapping Genes with Their Corresponding HPO Codes
author: John Snow Labs
name: gene_hpo_code_mapper
date: 2026-07-21
tags: [en, chunk_mapper, licensed, clinical, hpo, gene]
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

This model maps gene symbols to their associated HPO code(s), based on gene-phenotype associations curated by the Human Phenotype Ontology (HPO) project (reverse direction of `hpo_code_gene_mapper`). Genes linked to more than one HPO code return every associated code via the `all_k_resolutions` metadata field. Trained on the Human Phenotype Ontology (HPO) 2026-06-23 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/gene_hpo_code_mapper_en_6.4.0_3.4_1784640820746.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/gene_hpo_code_mapper_en_6.4.0_3.4_1784640820746.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

chunk_assembler = Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("ner_chunk")

gene_hpo_code_mapper = ChunkMapperModel.pretrained("gene_hpo_code_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["hpo_code"])

pipeline = Pipeline(stages=[document_assembler, chunk_assembler, gene_hpo_code_mapper])
data = spark.createDataFrame([["CHN1"], ["MDH1"], ["SNAP25"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

chunk_assembler = nlp.Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("ner_chunk")

gene_hpo_code_mapper = medical.ChunkMapperModel.pretrained("gene_hpo_code_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["hpo_code"])

pipeline = nlp.Pipeline(stages=[document_assembler, chunk_assembler, gene_hpo_code_mapper])
data = spark.createDataFrame([["CHN1"], ["MDH1"], ["SNAP25"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val chunkAssembler = new Doc2Chunk()
    .setInputCols("document")
    .setOutputCol("ner_chunk")

val geneHpoCodeMapper = ChunkMapperModel
    .pretrained("gene_hpo_code_mapper", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("hpo_code"))

val pipeline = new Pipeline().setStages(Array(documentAssembler, chunkAssembler, geneHpoCodeMapper))
val data = Seq("CHN1", "MDH1", "SNAP25").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| gene   | hpo_code   | all_k_resolutions                                                                                       |
|:-------|:-----------|:--------------------------------------------------------------------------------------------------------|
| CHN1   | HP:0001177 | HP:0001177:::HP:0001156:::HP:0025186:::HP:0001199:::HP:0009921:::HP:0001250:::HP:0001263:::HP:000740... |
| MDH1   | HP:0500149 | HP:0500149:::HP:0001276:::HP:0001250:::HP:0001263:::HP:0100876:::HP:0002521:::HP:0001338:::HP:000000... |
| SNAP25 | HP:0002465 | HP:0002465:::HP:0002421:::HP:0003701:::HP:0001270:::HP:0001288:::HP:0001283:::HP:0001284:::HP:000125... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|gene_hpo_code_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|771.7 KB|