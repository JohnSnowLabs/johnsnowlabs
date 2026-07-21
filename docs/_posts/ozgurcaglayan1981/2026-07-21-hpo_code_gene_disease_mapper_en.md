---
layout: model
title: Mapping HPO Codes with Their Corresponding Genes and Related Phenotypes
author: John Snow Labs
name: hpo_code_gene_disease_mapper
date: 2026-07-21
tags: [en, chunk_mapper, licensed, clinical, hpo, gene, disease]
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

This model maps HPO codes to their associated gene(s), and for each gene returns the phenotype terms associated with that gene elsewhere in the Human Phenotype Ontology (HPO). Codes linked to more than one gene return every associated gene's phenotype list via the `all_k_resolutions` metadata field. Trained on the Human Phenotype Ontology (HPO) 2026-06-23 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_code_gene_disease_mapper_en_6.4.0_3.4_1784663524659.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_code_gene_disease_mapper_en_6.4.0_3.4_1784663524659.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

hpo_code_gene_disease_mapper = ChunkMapperModel.pretrained("hpo_code_gene_disease_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_code"])\
    .setOutputCol("mappings")\
    .setRels(["hpo_gene_disease"])

pipeline = Pipeline(stages=[document_assembler, chunk_assembler, hpo_code_gene_disease_mapper])
data = spark.createDataFrame([["HP:0000002"], ["HP:6001080"], ["HP:0009484"]]).toDF("text")
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

hpo_code_gene_disease_mapper = medical.ChunkMapperModel.pretrained("hpo_code_gene_disease_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_code"])\
    .setOutputCol("mappings")\
    .setRels(["hpo_gene_disease"])

pipeline = nlp.Pipeline(stages=[document_assembler, chunk_assembler, hpo_code_gene_disease_mapper])
data = spark.createDataFrame([["HP:0000002"], ["HP:6001080"], ["HP:0009484"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val chunkAssembler = new Doc2Chunk()
    .setInputCols("document")
    .setOutputCol("hpo_code")

val hpoCodeGeneDiseaseMapper = ChunkMapperModel
    .pretrained("hpo_code_gene_disease_mapper", "en", "clinical/models")
    .setInputCols(Array("hpo_code"))
    .setOutputCol("mappings")
    .setRels(Array("hpo_gene_disease"))

val pipeline = new Pipeline().setStages(Array(documentAssembler, chunkAssembler, hpoCodeGeneDiseaseMapper))
val data = Seq("HP:0000002", "HP:6001080", "HP:0009484").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| hpo_code   |   n_genes | gene_disease                                                                                                                                              | all_k_resolutions                                                                                                                                         |
|:-----------|----------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| HP:0000002 |        25 | {"TBCB": ["polyneuropathy", "motor delay", "hypotonia", "intellectual disability", "spasticity", "slender finger", "interictal eeg abnormality", "abno... | {"TBCB": ["polyneuropathy", "motor delay", "hypotonia", "intellectual disability", "spasticity", "slender finger", "interictal eeg abnormality", "abno... |
| HP:6001080 |         1 | {"HSD11B1": ["abnormal circulating deoxycorticosterone level", "autosomal dominant inheritance", "elevated serum 11-deoxycortisol", "decreased circula... | {"HSD11B1": ["abnormal circulating deoxycorticosterone level", "autosomal dominant inheritance", "elevated serum 11-deoxycortisol", "decreased circula... |
| HP:0009484 |         2 | {"SHH": ["abnormal thumb morphology", "hand polydactyly", "poor speech", "expressive language delay", "limb dystonia", "oromotor apraxia", "single nar... | {"SHH": ["abnormal thumb morphology", "hand polydactyly", "poor speech", "expressive language delay", "limb dystonia", "oromotor apraxia", "single nar... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_code_gene_disease_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|122.3 MB|