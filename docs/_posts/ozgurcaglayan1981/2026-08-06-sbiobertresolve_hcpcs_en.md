---
layout: model
title: Sentence Entity Resolver for HCPCS Codes
author: John Snow Labs
name: sbiobertresolve_hcpcs
date: 2026-08-06
tags: [en, entity_resolution, licensed, clinical, hcpcs, sbiobert]
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

This model maps entities to HCPCS (Healthcare Common Procedure Coding System) codes using `sbiobert_base_cased_mli_onnx` Sentence Bert Embeddings. Trained on the current CMS HCPCS Level II Alpha-Numeric master file (release 20260701). This update adds an aux label (`domain_id` — the OMOP CDM domain, e.g. Device/Drug/Procedure/Observation/Measurement) alongside the resolved code, which the previous version of this model did not return.

{:.btn-box}
[Live Demo](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_hcpcs_en_6.4.1_3.4_1785976182645.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_hcpcs_en_6.4.1_3.4_1785976182645.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("ner_chunk")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

hcpcs_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_hcpcs", "en", "clinical/models")\
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

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

hcpcs_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_hcpcs", "en", "clinical/models")\
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

val sbertEmbedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("sentence_embeddings")
    .setCaseSensitive(false)

val hcpcsResolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_hcpcs", "en", "clinical/models")
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
| Unilateral breast prosthesis mastectomy bra with integrated form | L8001        | Breast prosthesis, mastectomy bra, with integrated breast prosthesis form, unilateral, any size, any type | L8001:::L8020:::L8015:::S2066:::S2067:::S2068:::L8035:::L8002:::G9704:::L8031:::... | 0.1237:::0.1296:::0.1594:::0.1629:::0.1837:::0.1913:::0.2018:::0.2127:::0.2162::... | Breast prosthesis, mastectomy bra, with integrated breast prosthesis form, unila... | Device:::Device:::Device:::Procedure:::Procedure:::Procedure:::Device:::Device::... |
| Injection, brentuximab vedotin, 1 mg                             | J9042        | Injection, brentuximab vedotin, 1 mg                                                                      | J9042:::J9326:::J0179:::J1823:::J0584:::J9273:::J2327:::Q9997:::J9347:::J9350:::... | 0.0000:::0.0502:::0.0497:::0.0504:::0.0555:::0.0612:::0.0599:::0.0619:::0.0617::... | Injection, brentuximab vedotin, 1 mg:::Injection, telisotuzumab vedotin-tllv, 1 ... | Drug:::Drug:::Drug:::Drug:::Drug:::Drug:::Drug:::Drug:::Drug:::null:::Drug:::Dru... |
| Spirometry results showing fev1/fvc below 70%                    | G8924        | Spirometry results documented (fev1/fvc < 70%)                                                            | G8924:::M1214:::A7006:::M1213:::G8395:::M1371:::G8694:::A4306:::G9243:::G8934:::... | 0.0521:::0.1662:::0.3001:::0.2925:::0.3165:::0.3009:::0.3166:::0.3170:::0.3217::... | Spirometry results documented (fev1/fvc < 70%):::Spirometry results with confirm... | Observation:::Observation:::Device:::Observation:::Observation:::Observation:::O... |
| Alcohol and/or drug screening                                    | H0049        | Alcohol and/or drug screening                                                                             | H0049:::H0001:::H0006:::H0003:::H0022:::T1007:::T1012:::H0014:::H0020:::H0005:::... | 0.0000:::0.0354:::0.0829:::0.0930:::0.1171:::0.1172:::0.1228:::0.1318:::0.1711::... | Alcohol and/or drug screening:::Alcohol and/or drug assessment:::Alcohol and/or ... | Measurement:::Procedure:::Procedure:::Measurement:::Procedure:::Observation:::Ob... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_hcpcs|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[hcpcs_code]|
|Language:|en|
|Size:|21.3 MB|
|Case sensitive:|false|