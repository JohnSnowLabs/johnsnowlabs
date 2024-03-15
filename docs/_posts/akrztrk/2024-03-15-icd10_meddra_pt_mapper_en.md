---
layout: model
title: Mapping ICD10 Codes with Their Corresponding MedDRA PT (Preferred Term) Codes
author: John Snow Labs
name: icd10_meddra_pt_mapper
date: 2024-03-15
tags: [licensed, en, icd_10, meddra, mapping, mapper, clinical]
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

This pretrained model maps ICD-10 codes to corresponding MedDRA PT (Preferred Term) codes.

## Predicted Entities

`icd10 code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10_meddra_pt_mapper_en_5.3.0_3.0_1710508648341.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10_meddra_pt_mapper_en_5.3.0_3.0_1710508648341.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("ner_chunk")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("icd10_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver2chunk = Resolution2Chunk()\
    .setInputCols(["icd10_code"])\
    .setOutputCol("icd102chunk")

chunkerMapper = ChunkMapperModel.pretrained("icd10_meddra_pt_mapper", "en", "clinical/models")\
    .setInputCols(["icd102chunk"])\
    .setOutputCol("mappings")

pipeline = Pipeline(stages = [
    documentAssembler,
    sbert_embedder,
    icd10_resolver,
    resolver2chunk,
    chunkerMapper])

data = spark.createDataFrame([["Type 2 diabetes mellitus"], ["Typhoid fever"], ["Malignant neoplasm of oesophagus"]]).toDF("text")

mapper_model = pipeline.fit(data)
result = mapper_model.transform(data)
```
```scala
val documentAssembler = DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("ner_chunk")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(False)

val icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented", "en", "clinical/models")\
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("icd10_code")
    .setDistanceFunction("EUCLIDEAN")

val resolver2chunk = Resolution2Chunk()
    .setInputCols(Array("icd10_code"))
    .setOutputCol("icd102chunk")

val chunkerMapper = ChunkMapperModel.pretrained("icd10_meddra_pt_mapper", "en", "clinical/models")\
    .setInputCols(Array("icd102chunk"))
    .setOutputCol("mappings")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sbert_embedder,
    icd10_resolver,
    resolver2chunk,
    chunkerMapper))

val data = Seq(Array("Type 2 diabetes mellitus"), Array("Typhoid fever"), Array("Malignant neoplasm of oesophagus")).toDF("text")

val mapper_model = pipeline.fit(data)
val result = mapper_model.transform(data)
```
</div>

## Results

```bash
+--------------------------------+----------+-----------------------------------+
|chunk                           |icd10_code|meddra_code                        |
+--------------------------------+----------+-----------------------------------+
|Type 2 diabetes mellitus        |E11       |10067585.0:Type 2 diabetes mellitus|
|Typhoid fever                   |A01.0     |10045275.0:Typhoid fever           |
|Malignant neoplasm of oesophagus|C15.9     |10030155.0:Oesophageal carcinoma   |
+--------------------------------+----------+-----------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10_meddra_pt_mapper|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|210.0 KB|

## References

This model is trained with the January 2024 release of ICD-10 to MedDRA Map dataset.
