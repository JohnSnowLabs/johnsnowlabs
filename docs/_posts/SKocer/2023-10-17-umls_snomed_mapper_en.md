---
layout: model
title: Mapping UMLS Codes with Their Corresponding SNOMED Codes
author: John Snow Labs
name: umls_snomed_mapper
date: 2023-10-17
tags: [snomed, umls, chunk_mapper, clinical, licensed, en]
task: Chunk Mapping
language: en
edition: Healthcare NLP 5.1.1
spark_version: 3.0
supported: true
annotator: DocMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps UMLS codes to corresponding SNOMED codes.

## Predicted Entities

`snomed_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_snomed_mapper_en_5.1.1_3.0_1697518217236.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_snomed_mapper_en_5.1.1_3.0_1697518217236.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

chunkerMapper = DocMapperModel.pretrained("umls_snomed_mapper", "en", "clinical/models")\
      .setInputCols(["document"])\
      .setOutputCol("mappings")\
      .setRels(["snomed_code"])

pipeline = Pipeline().setStages([document_assembler,
                                     chunkerMapper])

df = spark.createDataFrame([["C0000248"], ["C3503397"]]).toDF("text")

res = pipeline.fit(df).transform(df)
```
```scala
val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val chunkerMapper = DocMapperModel.pretrained("umls_snomed_mapper", "en", "clinical/models")
      .setInputCols("document")
      .setOutputCol("mappings")
      .setRels("snomed_code")
    
val pipeline = new Pipeline(stages = Array(
        document_assembler,
        chunkerMapper
))

val data = Seq([["C0000248"], ["C3503397"]]).toDS.toDF("text")

val result= pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------+-----------+-----------+
|umls_code|snomed_code|relation   |
+---------+-----------+-----------+
|C0000248 |725541001  |snomed_code|
|C3503397 |769507002  |snomed_code|
+---------+-----------+-----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_snomed_mapper|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|6.7 MB|