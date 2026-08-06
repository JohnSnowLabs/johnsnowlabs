---
layout: model
title: Sentence Entity Resolver for HCPCS Codes (MPNetEmbeddings)
author: John Snow Labs
name: biolordresolve_hcpcs
date: 2026-08-06
tags: [en, entity_resolution, licensed, clinical, hcpcs, biolord]
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

This model maps entities to HCPCS (Healthcare Common Procedure Coding System) codes using `mpnet_embeddings_biolord_2023_c` Sentence Embeddings. Trained on the current CMS HCPCS Level II Alpha-Numeric master file (release 20260701), with an aux label (`domain_id` — the OMOP CDM domain, e.g. Device/Drug/Procedure/Observation/Measurement) returned alongside the resolved code.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_hcpcs_en_6.4.1_3.4_1785977477412.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_hcpcs_en_6.4.1_3.4_1785977477412.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("ner_chunk")

sbert_embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

hcpcs_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_hcpcs", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("hcpcs_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages=[
    document_assembler, sbert_embedder, hcpcs_resolver
])

# 4 domain terms in one DataFrame (Device/Drug/Observation/Measurement) -- each row resolved
# independently, demonstrates the domain_id aux label across all 4 categories at once.
data = spark.createDataFrame([[t] for t in ['Unilateral breast prosthesis mastectomy bra with integrated form', 'Injection, brentuximab vedotin, 1 mg', 'Documented spirometry results with fev1/fvc under 70%', 'Alcohol and/or drug screening']], ["text"])
result = resolver_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("ner_chunk")

sbert_embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

hcpcs_resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_hcpcs", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("hcpcs_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = nlp.Pipeline(stages=[
    document_assembler, sbert_embedder, hcpcs_resolver
])

# 4 domain terms in one DataFrame (Device/Drug/Observation/Measurement) -- each row resolved
# independently, demonstrates the domain_id aux label across all 4 categories at once.
data = spark.createDataFrame([[t] for t in ['Unilateral breast prosthesis mastectomy bra with integrated form', 'Injection, brentuximab vedotin, 1 mg', 'Documented spirometry results with fev1/fvc under 70%', 'Alcohol and/or drug screening']], ["text"])
result = resolver_pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("ner_chunk")

val sbertEmbedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("sentence_embeddings")
    .setCaseSensitive(false)

val hcpcsResolver = SentenceEntityResolverModel.pretrained("biolordresolve_hcpcs", "en", "clinical/models")
    .setInputCols(Array("sentence_embeddings"))
    .setOutputCol("hcpcs_code")
    .setDistanceFunction("EUCLIDEAN")

val resolverPipeline = new Pipeline().setStages(Array(
    documentAssembler, sbertEmbedder, hcpcsResolver
))

// 4 domain terms in one DataFrame (Device/Drug/Observation/Measurement) -- each row resolved
// independently, demonstrates the domain_id aux label across all 4 categories at once.
val data = Seq("Unilateral breast prosthesis mastectomy bra with integrated form", "Injection, brentuximab vedotin, 1 mg", "Documented spirometry results with fev1/fvc under 70%", "Alcohol and/or drug screening").toDF("text")
val result = resolverPipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                                                        | hcpcs_code   | resolution                                                                                                | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:-----------------------------------------------------------------|:-------------|:----------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| Unilateral breast prosthesis mastectomy bra with integrated form | L8001        | Breast prosthesis, mastectomy bra, with integrated breast prosthesis form, unilateral, any size, any type | L8001:::L8000:::L8002:::L8020:::L8030:::L8035:::L8015:::L8600:::L8031:::M1280:::... | 0.0865:::0.1999:::0.2090:::0.2731:::0.3186:::0.3261:::0.3317:::0.3598:::0.3927::... | Breast prosthesis, mastectomy bra, with integrated breast prosthesis form, unila... | Device:::Device:::Device:::Device:::Device:::Device:::Device:::Device:::Device::... |
| Injection, brentuximab vedotin, 1 mg                             | J9042        | Injection, brentuximab vedotin, 1 mg                                                                      | J9042:::J9326:::J9273:::J9309:::J9039:::J9229:::J0202:::J9176:::J9055:::J9053:::... | 0.0000:::0.2016:::0.2323:::0.2607:::0.2660:::0.2697:::0.2733:::0.2814:::0.2821::... | Injection, brentuximab vedotin, 1 mg:::Injection, telisotuzumab vedotin-tllv, 1 ... | Drug:::Drug:::Drug:::Drug:::Drug:::Drug:::Drug:::Drug:::Drug:::null:::Drug:::Dru... |
| Documented spirometry results with fev1/fvc under 70%            | G8924        | Spirometry results documented (fev1/fvc < 70%)                                                            | G8924:::M1214:::M1216:::M1213:::M1217:::A4614:::M1215:::S8110:::G9432:::G8396:::... | 0.1389:::0.2215:::0.2241:::0.2371:::0.5209:::0.5521:::0.5537:::0.6012:::0.6106::... | Spirometry results documented (fev1/fvc < 70%):::Spirometry results with confirm... | Observation:::Observation:::Observation:::Observation:::Observation:::Device:::O... |
| Alcohol and/or drug screening                                    | H0049        | Alcohol and/or drug screening                                                                             | H0049:::H0001:::H0003:::H0048:::G0442:::G2196:::G2197:::H0002:::H0028:::G9622:::... | 0.0000:::0.1424:::0.1469:::0.2789:::0.3269:::0.3507:::0.3563:::0.3941:::0.3985::... | Alcohol and/or drug screening:::Alcohol and/or drug assessment:::Alcohol and/or ... | Measurement:::Procedure:::Measurement:::Measurement:::Procedure:::Observation:::... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_hcpcs|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[hcpcs_code]|
|Language:|en|
|Size:|21.3 MB|
|Case sensitive:|false|