---
layout: model
title: Mapping HCPCS Codes with Their Corresponding Entities
author: John Snow Labs
name: hcpcs_mapper
date: 2026-08-06
tags: [en, chunk_mapper, licensed, clinical, hcpcs]
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

This model maps entities extracted from text to their corresponding HCPCS (Healthcare Common Procedure Coding System) codes. It performs a direct lookup against the full training text , providing fast, exact-match code mapping without requiring embeddings at inference time. Trained on the current CMS HCPCS Level II Alpha-Numeric master file (release 20260701).

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hcpcs_mapper_en_6.4.1_3.4_1786006372539.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hcpcs_mapper_en_6.4.1_3.4_1786006372539.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

doc2chunk = Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("ner_chunk")

hcpcs_mapper = ChunkMapperModel.pretrained("hcpcs_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["hcpcs_code"])

pipeline = Pipeline(stages=[
    document_assembler, doc2chunk, hcpcs_mapper
])

# 4 domain terms in one DataFrame (Device/Drug/Observation/Measurement) -- each row looked up
# independently against the dictionary.
data = spark.createDataFrame([[t] for t in ['Breast prosthesis, mastectomy bra, with integrated breast prosthesis form, unilateral, any size, any type', 'Injection, brentuximab vedotin, 1 mg', 'Spirometry results documented (fev1/fvc < 70%)', 'Alcohol and/or drug screening']], ["text"])
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

doc2chunk = nlp.Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("ner_chunk")

hcpcs_mapper = medical.ChunkMapperModel.pretrained("hcpcs_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["hcpcs_code"])

pipeline = nlp.Pipeline(stages=[
    document_assembler, doc2chunk, hcpcs_mapper
])

# 4 domain terms in one DataFrame (Device/Drug/Observation/Measurement) -- each row looked up
# independently against the dictionary.
data = spark.createDataFrame([[t] for t in ['Breast prosthesis, mastectomy bra, with integrated breast prosthesis form, unilateral, any size, any type', 'Injection, brentuximab vedotin, 1 mg', 'Spirometry results documented (fev1/fvc < 70%)', 'Alcohol and/or drug screening']], ["text"])
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val doc2Chunk = new Doc2Chunk()
    .setInputCols(Array("document"))
    .setOutputCol("ner_chunk")

val hcpcsMapper = ChunkMapperModel.pretrained("hcpcs_mapper", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("hcpcs_code"))

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, doc2Chunk, hcpcsMapper
))

// 4 domain terms in one DataFrame (Device/Drug/Observation/Measurement) -- each row looked up
// independently against the dictionary.
val data = Seq("Breast prosthesis, mastectomy bra, with integrated breast prosthesis form, unilateral, any size, any type", "Injection, brentuximab vedotin, 1 mg", "Spirometry results documented (fev1/fvc < 70%)", "Alcohol and/or drug screening").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                                                                                                 | hcpcs_code   |
|:----------------------------------------------------------------------------------------------------------|:-------------|
| Breast prosthesis, mastectomy bra, with integrated breast prosthesis form, unilateral, any size, any type | L8001        |
| Injection, brentuximab vedotin, 1 mg                                                                      | J9042        |
| Spirometry results documented (fev1/fvc < 70%)                                                            | G8924        |
| Alcohol and/or drug screening                                                                             | H0049        |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hcpcs_mapper|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|313.2 KB|
