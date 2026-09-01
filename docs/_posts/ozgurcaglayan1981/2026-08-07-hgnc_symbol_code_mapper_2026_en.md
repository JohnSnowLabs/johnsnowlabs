---
layout: model
title: Mapping Gene Symbols with Their Corresponding HGNC Codes
author: John Snow Labs
name: hgnc_symbol_code_mapper_2026
date: 2026-08-07
tags: [en, chunk_mapper, licensed, clinical, hgnc, gene]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps current approved gene symbols to their corresponding HGNC identifier. Trained on the HGNC monthly release dated 2026-08-04.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hgnc_symbol_code_mapper_2026_en_6.4.1_3.4_1786132264719.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hgnc_symbol_code_mapper_2026_en_6.4.1_3.4_1786132264719.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

code_mapper = ChunkMapperModel.pretrained("hgnc_symbol_code_mapper_2026","en","clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["hgnc_id"])

pipeline = Pipeline(stages=[document_assembler, chunk_assembler, code_mapper])

data = spark.createDataFrame([[s] for s in ['TP53', 'BRCA1', 'EGFR', 'KRAS', 'APC', 'NRAS', 'PTEN', 'XDH']]).toDF("text")
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

code_mapper = medical.ChunkMapperModel.pretrained("hgnc_symbol_code_mapper_2026","en","clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["hgnc_id"])

pipeline = nlp.Pipeline(stages=[document_assembler, chunk_assembler, code_mapper])

data = spark.createDataFrame([[s] for s in ['TP53', 'BRCA1', 'EGFR', 'KRAS', 'APC', 'NRAS', 'PTEN', 'XDH']]).toDF("text")
result = pipeline.fit(data).transform(data)
```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val chunkAssembler = new Doc2Chunk()
    .setInputCols("document")
    .setOutputCol("ner_chunk")

val codeMapper = ChunkMapperModel
    .pretrained("hgnc_symbol_code_mapper_2026", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("hgnc_id"))

val pipeline = new Pipeline().setStages(Array(documentAssembler, chunkAssembler, codeMapper))

val data = Seq("TP53", "BRCA1", "EGFR", "KRAS", "APC", "NRAS", "PTEN", "XDH").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| symbol   | HGNC Code   |
|:---------|:------------|
| TP53     | HGNC:11998  |
| BRCA1    | HGNC:1100   |
| EGFR     | HGNC:3236   |
| KRAS     | HGNC:6407   |
| APC      | HGNC:583    |
| NRAS     | HGNC:7989   |
| PTEN     | HGNC:9588   |
| XDH      | HGNC:12805  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hgnc_symbol_code_mapper_2026|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|618.4 KB|