---
layout: model
title: Mapping HCPCS Codes with Corresponding National Drug Codes (NDC) and Drug Brand Names
author: John Snow Labs
name: hcpcs_ndc_mapper
date: 2026-07-26
tags: [en, chunk_mapper, licensed, clinical, ndc, hcpcs]
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

This pretrained model establishes connections between HCPCS codes and their corresponding National Drug Codes (NDC) along with associated drug brand names. Trained on the PDAC NDC/HCPCS Crosswalk (release pdac-2026-07-05).

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hcpcs_ndc_mapper_en_6.4.0_3.4_1785072742271.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hcpcs_ndc_mapper_en_6.4.0_3.4_1785072742271.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

doc2chunk = Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("chunk")

chunkerMapper = ChunkMapperModel.pretrained("hcpcs_ndc_mapper", "en", "clinical/models")\
    .setInputCols(["chunk"])\
    .setOutputCol("mappings")\
    .setRels(["ndc_code", "brand_name"])

pipeline = Pipeline(stages=[
    document_assembler,
    doc2chunk,
    chunkerMapper
])

data = spark.createDataFrame([["Q5106"], ["J9211"], ["J7508"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

doc2chunk = nlp.Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("chunk")

chunkerMapper = medical.ChunkMapperModel.pretrained("hcpcs_ndc_mapper", "en", "clinical/models")\
    .setInputCols(["chunk"])\
    .setOutputCol("mappings")\
    .setRels(["ndc_code", "brand_name"])

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    doc2chunk,
    chunkerMapper
])

data = spark.createDataFrame([["Q5106"], ["J9211"], ["J7508"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val doc2chunk = new Doc2Chunk()
    .setInputCols("document")
    .setOutputCol("chunk")

val chunkerMapper = ChunkMapperModel
    .pretrained("hcpcs_ndc_mapper", "en", "clinical/models")
    .setInputCols(Array("chunk"))
    .setOutputCol("mappings")
    .setRels(Array("ndc_code", "brand_name"))

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    doc2chunk,
    chunkerMapper
))

val data = Seq("Q5106", "J9211", "J7508").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| HCPCS Code   | NDC Code      | Brand Name                                 | All NDC Codes                                                                                                                                                                                                                                                                 | All Brand Names                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:-------------|:--------------|:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Q5106        | 00069-1305-10 | RETACRIT (PF) 2000 U/1 ML                  | 00069-1305-10:::00069-1306-10:::00069-1307-10:::00069-1308-10:::00069-1309-04:::00069-1318-10:::59353-0002-01:::59353-0002-10:::59353-0003-01:::59353-0003-10:::59353-0004-01:::59353-0004-10:::59353-0010-01:::59353-0010-10:::59353-0220-01:::59353-0220-10                 | RETACRIT (PF) 2000 U/1 ML:::RETACRIT (PF) 3000 U/1 ML:::RETACRIT (PF) 4000 U/1 ML:::RETACRIT (PF) 10000 U/1 ML:::RETACRIT (PF) 40000 U/1 ML:::RETACRIT (10X2ML;MDV,LATEX-FREE) 10000 U/1 ML:::RETACRIT (PF) 2000 U/1 ML:::RETACRIT (PF) 2000 U/1 ML:::RETACRIT (PF) 3000 U/1 ML:::RETACRIT (PF) 3000 U/1 ML:::RETACRIT (PF) 4000 U/1 ML:::RETACRIT (PF) 4000 U/1 ML:::RETACRIT (PF) 10000 U/1 ML:::RETACRIT (PF) 10000 U/1 ML:::RETACRIT  10000 U/1 ML:::RETACRIT  10000 U/1 ML                                                                                                                                                                                                                                                                                            |
| J9211        | 00013-2576-05 | IDAMYCIN PFS (SDV,PF,LATEX-FREE) 1 MG/1 ML | 00013-2576-05:::00013-2576-91:::00013-2586-10:::00013-2586-91:::00013-2596-20:::00143-9217-01:::00143-9218-01:::00143-9219-01:::00143-9306-01:::00143-9307-01:::00143-9308-01:::59762-2576-01:::59762-2586-01:::59762-2596-01:::71288-0184-05:::71288-0185-10:::71288-0186-20 | IDAMYCIN PFS (SDV,PF,LATEX-FREE) 1 MG/1 ML:::IDAMYCIN PFS (SDV,PF,CYTOSAFE VIAL,PF) 1 MG/ML:::IDAMYCIN PFS (GLASS SDV,PF,LATEX-FREE) 1 MG/1 ML:::IDAMYCIN PFS (SDV.PF,CYTOSAFE VIAL,PF) 1 MG/ML:::IDAMYCIN PFS (GLASS SDV,PF,LATEX-FREE) 1 MG/1 ML:::IDARUBICIN HYDROCHLORIDE (PF) 1 MG/1 ML:::IDARUBICIN HYDROCHLORIDE (PF) 1 MG/1 ML:::IDARUBICIN HYDROCHLORIDE (PF) 1 MG/1 ML:::IDARUBICIN HCL NOVAPLUS (SDV,PF) 1 MG/1 ML:::IDARUBICIN HCL NOVAPLUS (SDV,PF) 1 MG/1 ML:::IDARUBICIN HCL NOVAPLUS (SDV,PF) 1 MG/1 ML:::IDARUBICIN HYDROCHLORIDE (PF) 1 MG/ML:::IDARUBICIN HYDROCHLORIDE (PF) 1 MG/ML:::IDARUBICIN HYDROCHLORIDE (PF) 1 MG/ML:::IDARUBICIN HYDROCHLORIDE SDV 1 MG/1 ML:::IDARUBICIN HYDROCHLORIDE SDV 1 MG/1 ML:::IDARUBICIN HYDROCHLORIDE SDV 1 MG/1 ML |
| J7508        | 00469-0647-73 | ASTAGRAF XL 0.5 MG                         | 00469-0647-73:::00469-0677-73:::00469-0687-73:::69238-2780-03:::69238-2781-03:::69238-2782-03                                                                                                                                                                                 | ASTAGRAF XL 0.5 MG:::ASTAGRAF XL 1 MG:::ASTAGRAF XL 5 MG:::TACROLIMUS HARD GELATIN 0.5 MG:::TACROLIMUS HARD GELATIN 1 MG:::TACROLIMUS HARD GELATIN 5 MG                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hcpcs_ndc_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|99.1 KB|