---
layout: model
title: ICD10CM Neoplasms Entity Resolver
author: John Snow Labs
name: chunkresolve_icd10cm_neoplasms_clinical
date: 2021-04-02
tags: [entity_resolution, clinical, licensed, en]
task: Entity Resolution
language: en
nav_key: models
edition: Healthcare NLP 3.0.0
spark_version: 3.0
deprecated: true
annotator: ChunkEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Entity Resolution model Based on KNN using Word Embeddings + Word Movers Distance.

## Predicted Entities

ICD10-CM Codes and their normalized definition with ``clinical_embeddings``.

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_ICD10_CM/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icd10cm_neoplasms_clinical_en_3.0.0_3.0_1617355435147.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/chunkresolve_icd10cm_neoplasms_clinical_en_3.0.0_3.0_1617355435147.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
...
neoplasm_resolver = ChunkEntityResolverModel.pretrained("chunkresolve_icd10cm_neoplasms_clinical","en","clinical/models")\
	.setInputCols("token","chunk_embeddings")\
	.setOutputCol("entity")
pipeline_puerile = Pipeline(stages = [documentAssembler, sentenceDetector, tokenizer, word_embeddings, clinical_ner, ner_converter, chunk_embeddings, neoplasm_resolver])

model = pipeline_puerile.fit(spark.createDataFrame([["""The patient is a 5-month-old infant who presented initially on Monday with a cold, cough, and runny nose for 2 days. Mom states she had no fever. Her appetite was good but she was spitting up a lot. She had no difficulty breathing and her cough was described as dry and hacky. At that time, physical exam showed a right TM, which was red. Left TM was okay. She was fairly congested but looked happy and playful. She was started on Amoxil and Aldex and we told to recheck in 2 weeks to recheck her ear. Mom returned to clinic again today because she got much worse overnight. She was having difficulty breathing. She was much more congested and her appetite had decreased significantly today. She also spiked a temperature yesterday of 102.6 and always having trouble sleeping secondary to congestion."""]]).toDF("text"))

results = model.transform(data)
```
```scala
...
val neoplasm_resolver = ChunkEntityResolverModel.pretrained("chunkresolve_icd10cm_neoplasms_clinical","en","clinical/models")
	.setInputCols(Array("token","chunk_embeddings"))
	.setOutputCol("resolution")
val pipeline = new Pipeline().setStages(Array(documentAssembler, sentenceDetector, tokenizer, word_embeddings, clinical_ner, ner_converter, chunk_embeddings, neoplasm_resolver))

val data = Seq("The patient is a 5-month-old infant who presented initially on Monday with a cold, cough, and runny nose for 2 days. Mom states she had no fever. Her appetite was good but she was spitting up a lot. She had no difficulty breathing and her cough was described as dry and hacky. At that time, physical exam showed a right TM, which was red. Left TM was okay. She was fairly congested but looked happy and playful. She was started on Amoxil and Aldex and we told to recheck in 2 weeks to recheck her ear. Mom returned to clinic again today because she got much worse overnight. She was having difficulty breathing. She was much more congested and her appetite had decreased significantly today. She also spiked a temperature yesterday of 102.6 and always having trouble sleeping secondary to congestion.").toDF("text")
val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
chunk                entity                         icd10_neoplasm_description  icd10_neoplasm_code

0 patient              Organism        Acute myelomonocytic leukemia, in remission  C9251
1  infant              Organism          Malignant (primary) neoplasm, unspecified  C801
2    nose                 Organ                 Malignant neoplasm of nasal cavity  C300
3     She              Organism                Malignant neoplasm of thyroid gland  C73
4     She              Organism                Malignant neoplasm of thyroid gland  C73
5     She              Organism                Malignant neoplasm of thyroid gland  C73
6   Aldex  Gene_or_gene_product  Acute megakaryoblastic leukemia not having ach...  C9420
7     ear                 Organ  Other benign neoplasm of skin of right ear and...  D2321
8     She              Organism                Malignant neoplasm of thyroid gland  C73
9     She              Organism                Malignant neoplasm of thyroid gland  C73
10    She              Organism                Malignant neoplasm of thyroid gland  C73
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|chunkresolve_icd10cm_neoplasms_clinical|
|Compatibility:|Healthcare NLP 3.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token, chunk_embeddings]|
|Output Labels:|[icd10cm]|
|Language:|en|
