---
layout: model
title: Mapping MedDRA-LLT (Lowest Level Term) Codes with Their Corresponding ICD-10 Codes
author: John Snow Labs
name: meddra_llt_icd10_mapper
date: 2024-03-14
tags: [licensed, en, icd_10, meddra, mapping]
task: Chunk Mapping
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps MedDRA-LLT (Lowest Level Term) codes to corresponding ICD10 codes. Some of the MedDRA LLT codes map to more than ICD-10 codes. You can find all the mapped ICD-10 codes in the `all_k_resolutions` column in the metadata.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
      .setInputCol('text')\
      .setOutputCol('doc')

chunk_assembler = Doc2Chunk()\
      .setInputCols(['doc'])\
      .setOutputCol('ner_chunk')
 
mapperModel = ChunkMapperModel.load('meddra_llt_icd10_mapper')\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["icd10_code"])


mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["10045275.0"], ["10067585.0"], ["10026182.0"]]).toDF("text")

mapper_model = mapper_pipeline.fit(data)
result = mapper_model.transform(data)
```
```scala
val document_assembler = DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("doc")

val chunk_assembler = Doc2Chunk()
      .setInputCols(Array("doc"))
      .setOutputCol("ner_chunk")
 
val mapperModel = ChunkMapperModel.load("meddra_llt_icd10_mapper")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("icd10_code"))


val mapper_pipeline = new Pipeline().setStages(Array(
    document_assembler,
    chunk_assembler,
    mapperModel
)

val data = Seq("10045275.0", "10067585.0", "10026182.0").toDF("text")

val mapper_model = mapper_pipeline.fit(data)
val result = mapper_model.transform(data)
```
</div>

## Results

```bash
+-----------+-------------------------------------------------+--------------------------------------------------------+
|meddra_code|icd10_code                                       |all_k_resolutions                                       |
+-----------+-------------------------------------------------+--------------------------------------------------------+
|10045275.0 |A01:Typhoid and paratyphoid fevers               |A01:Typhoid and paratyphoid fevers:::A01.0:Typhoid fever|
|10067585.0 |E11:Type 2 diabetes mellitus                     |E11:Type 2 diabetes mellitus:::                         |
|10026182.0 |C15.9:Malignant neoplasm: Oesophagus, unspecified|C15.9:Malignant neoplasm: Oesophagus, unspecified:::    |
+-----------+-------------------------------------------------+--------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|meddra_llt_icd10_mapper|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|216.1 KB|

## References

This model is trained with the January 2024 release of ICD-10 to MedDRA Map dataset.

To utilize this model, possession of a valid MedDRA license is requisite. If you possess one and wish to use this model, kindly contact us at support@johnsnowlabs.com.
