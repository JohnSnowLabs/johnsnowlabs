---
layout: model
title: Sentence Entity Resolver for HCPCS Codes (BGEEmbeddings)
author: John Snow Labs
name: bgeresolve_hcpcs
date: 2026-08-06
tags: [en, entity_resolution, licensed, clinical, hcpcs, bge]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps entities to HCPCS (Healthcare Common Procedure Coding System) codes using `bge_base_en_v1_5_onnx` Sentence Embeddings. Trained on the current CMS HCPCS Level II Alpha-Numeric master file (release 20260701), with an aux label (`domain_id` — the OMOP CDM domain, e.g. Device/Drug/Procedure/Observation/Measurement) returned alongside the resolved code.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_hcpcs_en_6.4.1_3.4_1785977923935.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_hcpcs_en_6.4.1_3.4_1785977923935.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("ner_chunk")

sbert_embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

hcpcs_resolver = SentenceEntityResolverModel.pretrained("bgeresolve_hcpcs", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("hcpcs_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages=[
    document_assembler, sbert_embedder, hcpcs_resolver
])

# 4 domain terms in one DataFrame (Device/Drug/Observation/Measurement) -- each row resolved
# independently, demonstrates the domain_id aux label across all 4 categories at once.
data = spark.createDataFrame([[t] for t in ['Unilateral breast prosthesis mastectomy bra with integrated form', 'Injection, brentuximab vedotin, 1 mg', 'Spirometry results showing fev1/fvc below 70%', 'Alcohol and/or drug screening']], ["text"])
result = resolver_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("ner_chunk")

sbert_embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

hcpcs_resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_hcpcs", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("hcpcs_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = nlp.Pipeline(stages=[
    document_assembler, sbert_embedder, hcpcs_resolver
])

# 4 domain terms in one DataFrame (Device/Drug/Observation/Measurement) -- each row resolved
# independently, demonstrates the domain_id aux label across all 4 categories at once.
data = spark.createDataFrame([[t] for t in ['Unilateral breast prosthesis mastectomy bra with integrated form', 'Injection, brentuximab vedotin, 1 mg', 'Spirometry results showing fev1/fvc below 70%', 'Alcohol and/or drug screening']], ["text"])
result = resolver_pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("ner_chunk")

val sbertEmbedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("sentence_embeddings")
    .setCaseSensitive(false)

val hcpcsResolver = SentenceEntityResolverModel.pretrained("bgeresolve_hcpcs", "en", "clinical/models")
    .setInputCols(Array("sentence_embeddings"))
    .setOutputCol("hcpcs_code")
    .setDistanceFunction("EUCLIDEAN")

val resolverPipeline = new Pipeline().setStages(Array(
    documentAssembler, sbertEmbedder, hcpcsResolver
))

// 4 domain terms in one DataFrame (Device/Drug/Observation/Measurement) -- each row resolved
// independently, demonstrates the domain_id aux label across all 4 categories at once.
val data = Seq("Unilateral breast prosthesis mastectomy bra with integrated form", "Injection, brentuximab vedotin, 1 mg", "Spirometry results showing fev1/fvc below 70%", "Alcohol and/or drug screening").toDF("text")
val result = resolverPipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                                                        | hcpcs_code   | resolution                                                                                                | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:-----------------------------------------------------------------|:-------------|:----------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| Unilateral breast prosthesis mastectomy bra with integrated form | L8001        | Breast prosthesis, mastectomy bra, with integrated breast prosthesis form, unilateral, any size, any type | L8001:::L8002:::L8015:::L8000:::L8020:::L8035:::L8031:::L8039:::L8030:::C1789:::... | 0.0886:::0.1215:::0.1467:::0.1474:::0.1515:::0.1778:::0.1902:::0.1943:::0.1943::... | Breast prosthesis, mastectomy bra, with integrated breast prosthesis form, unila... | Device:::Device:::Device:::Device:::Device:::Device:::Device:::Device:::Device::... |
| Injection, brentuximab vedotin, 1 mg                             | J9042        | Injection, brentuximab vedotin, 1 mg                                                                      | J9042:::J9273:::J9326:::J9309:::J3380:::J9271:::J0517:::J2182:::J9295:::J2329:::... | 0.0000:::0.1009:::0.1073:::0.1094:::0.1229:::0.1229:::0.1343:::0.1353:::0.1364::... | Injection, brentuximab vedotin, 1 mg:::Injection, tisotumab vedotin-tftv, 1 mg::... | Drug:::Drug:::Drug:::Drug:::Drug:::Drug:::Drug:::Drug:::Drug:::Drug:::Drug:::Dru... |
| Spirometry results showing fev1/fvc below 70%                    | G8924        | Spirometry results documented (fev1/fvc < 70%)                                                            | G8924:::M1213:::M1214:::M1216:::M1218:::M1460:::M1326:::M1215:::S5180:::G9605:::... | 0.0780:::0.1255:::0.1399:::0.1547:::0.3301:::0.3373:::0.3527:::0.3530:::0.3553::... | Spirometry results documented (fev1/fvc < 70%):::No history of spirometry result... | Observation:::Observation:::Observation:::Observation:::Observation:::Observatio... |
| Alcohol and/or drug screening                                    | H0049        | Alcohol and/or drug screening                                                                             | H0049:::H0001:::H0003:::G0442:::G2197:::H0048:::G2196:::H0006:::H0014:::G9622:::... | 0.0000:::0.0858:::0.1236:::0.2411:::0.2428:::0.2486:::0.2496:::0.2501:::0.2522::... | Alcohol and/or drug screening:::Alcohol and/or drug assessment:::Alcohol and/or ... | Measurement:::Procedure:::Measurement:::Procedure:::Observation:::Measurement:::... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_hcpcs|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[hcpcs_code]|
|Language:|en|
|Size:|21.3 MB|
|Case sensitive:|false|