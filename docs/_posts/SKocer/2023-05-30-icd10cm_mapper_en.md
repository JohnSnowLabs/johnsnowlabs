---
layout: model
title: Mapping Entities with Corresponding ICD-10-CM Codes
author: John Snow Labs
name: icd10cm_mapper
date: 2023-05-30
tags: [icd10cm, chunk_mapper, clinical, licensed, en]
task: Chunk Mapping
language: en
edition: Healthcare NLP 4.4.2
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps entities with their corresponding ICD-10-CM codes.

`Important Note`: Mappers extract additional information such as extended descriptions and categories related to Concept codes (such as RxNorm, ICD10, CPT, MESH, NDC, UMLS, etc.). They generally take Concept Codes, which are the outputs of EntityResolvers, as input. When creating a pipeline that contains 'Mapper', it is necessary to use the ChunkMapperModel after an EntityResolverModel.


## Predicted Entities

`icd10cm_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_mapper_en_4.4.2_3.0_1685478700624.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_mapper_en_4.4.2_3.0_1685478700624.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols("sentence")\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel\
    .pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel\
    .pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

chunkerMapper = ChunkMapperModel\
    .pretrained("icd10cm_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["icd10cm_code"])

mapper_pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer, 
    word_embeddings,
    ner_model, 
    ner_converter, 
    chunkerMapper])


test_data = spark.createDataFrame([["A 35-year-old male with a history of chronic renal insufficiency, type 2 diabetes mellitus diagnosed eight years prior, hypertension, and hyperlipidemia, presented with a two-week history of polydipsia, poor appetite, and vomiting."]]).toDF("text")

mapper_model = mapper_pipeline.fit(test_data)

result= mapper_model.transform(test_data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel
    .pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

val chunkerMapper = ChunkMapperModel
    .pretrained("icd10cm_mapper", "en", "clinical/models")
    .setInputCols("ner_chunk")
    .setOutputCol("mappings")
    .setRels("icd10cm_code")

val mapper_pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer, 
    word_embeddings,
    ner_model, 
    ner_converter, 
    chunkerMapper))


val data = Seq("A 35-year-old male with a history of chronic renal insufficiency, type 2 diabetes mellitus diagnosed eight years prior, hypertension, and hyperlipidemia, presented with a two-week history of polydipsia, poor appetite, and vomiting.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------------------------+-------+------------+
|ner_chunk                  |entity |icd10cm_code|
+---------------------------+-------+------------+
|chronic renal insufficiency|PROBLEM|N18.9       |
|type 2 diabetes mellitus   |PROBLEM|E11         |
|hypertension               |PROBLEM|I10         |
|hyperlipidemia             |PROBLEM|E78.5       |
|polydipsia                 |PROBLEM|R63.1       |
|poor appetite              |PROBLEM|R63.0       |
|vomiting                   |PROBLEM|R11.1       |
+---------------------------+-------+------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_mapper|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|14.1 MB|