---
layout: model
title: Mapping HPO Codes with Their Corresponding Parent Terms
author: John Snow Labs
name: hpo_parent_mapper
date: 2026-07-21
tags: [en, chunk_mapper, licensed, clinical, hpo, parent]
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

This model maps HPO codes to their full ancestor hierarchy in the Human Phenotype Ontology (HPO) — every parent term from the given code up to the ontology root, not just the direct parent. For each ancestor it returns the HPO code, label, and official ontology description, joined into one or more ancestor paths (multiple paths are returned for codes with more than one parent branch). Also returns the code's own canonical label via the `resolution` relation. Trained on the Human Phenotype Ontology (HPO) 2026-06-23 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_parent_mapper_en_6.4.0_3.4_1784595486814.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_parent_mapper_en_6.4.0_3.4_1784595486814.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

hpo_parent_mapper = ChunkMapperModel.pretrained("hpo_parent_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["resolution", "parents"])  # or just ["parents"]

pipeline = Pipeline(stages=[document_assembler, chunk_assembler, hpo_parent_mapper])
data = spark.createDataFrame([["HP:0002354"]]).toDF("text")
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

hpo_parent_mapper = medical.ChunkMapperModel.pretrained("hpo_parent_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["resolution", "parents"])  # or just ["parents"]

pipeline = nlp.Pipeline(stages=[document_assembler, chunk_assembler, hpo_parent_mapper])
data = spark.createDataFrame([["HP:0002354"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val chunkAssembler = new Doc2Chunk()
    .setInputCols("document")
    .setOutputCol("ner_chunk")

val hpoParentMapper = ChunkMapperModel
    .pretrained("hpo_parent_mapper", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("resolution", "parents"))  // or just Array("parents")

val pipeline = new Pipeline().setStages(Array(documentAssembler, chunkAssembler, hpoParentMapper))
val data = Seq("HP:0002354").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| code       | resolution                |   n_ancestor_paths | sample_ancestor_path                                                                                                                                                                                                                                                                                            |
|:-----------|:--------------------------|-------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HP:0002354 | Memory impairment         |                  1 | HP:0100543: Cognitive impairment ## An individual with cognitive impairment may experience difficulties in remembering, learning new things, concentrating, or making decisions. => HP:0011446: Abnormality of mental function ## This includes abnormalities in speech, mood, emotions, behavior, and cogni... |
| HP:0001629 | Ventricular septal defect |                  2 | HP:0010438: Abnormal ventricular septum morphology ## A structural abnormality of the interventricular septum. => HP:0001671: Abnormal cardiac septum morphology ## An anomaly of the intra-atrial or intraventricular septum. => HP:0001627: Abnormal heart morphology ## Any structural anomaly of the hea... |
| HP:0000252 | Microcephaly              |                  4 | HP:0007364: Aplasia/Hypoplasia of the cerebrum ## Absent/small cerebrum => HP:0002060: Abnormal cerebral morphology ## Any structural abnormality of the telencephalon, which is also known as the cerebrum. => HP:0100547: Abnormal forebrain morphology ## An abnormality of the forebrain, which has as i... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_parent_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|9.7 MB|