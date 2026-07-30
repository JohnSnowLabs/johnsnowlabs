---
layout: model
title: Sentence Entity Resolver for ATC (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_atc
date: 2026-07-30
tags: [en, entity_resolution, licensed, clinical, atc, biolord]
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

This model maps drugs entities to ATC (Anatomic Therapeutic Chemical) codes using `mpnet_embeddings_biolord_2023_c` Sentence Embeddings. Trained on the WHO ATC-DDD dataset (release 2026-04-25).

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_atc_en_6.4.1_3.4_1785444626580.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_atc_en_6.4.1_3.4_1785444626580.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

posology_ner = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

atc_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_atc", "en", "clinical/models")\
    .setInputCols(["embeddings"])\
    .setOutputCol("atc_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages=[
    document_assembler, sentenceDetectorDL, tokenizer, word_embeddings,
    posology_ner, ner_converter, c2doc, embedder, atc_resolver
])

data = spark.createDataFrame([["The patient was started on metformin 500 mg twice daily for type 2 diabetes and was also prescribed atorvastatin for hyperlipidemia. She was given amoxicillin for a sinus infection."]]).toDF("text")
result = resolver_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

posology_ner = medical.NerModel.pretrained("ner_posology", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

c2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

atc_resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_atc", "en", "clinical/models")\
    .setInputCols(["embeddings"])\
    .setOutputCol("atc_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = nlp.Pipeline(stages=[
    document_assembler, sentenceDetectorDL, tokenizer, word_embeddings,
    posology_ner, ner_converter, c2doc, embedder, atc_resolver
])

data = spark.createDataFrame([["The patient was started on metformin 500 mg twice daily for type 2 diabetes and was also prescribed atorvastatin for hyperlipidemia. She was given amoxicillin for a sinus infection."]]).toDF("text")
result = resolver_pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val posology_ner = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("DRUG"))

val c2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("embeddings")
    .setCaseSensitive(false)

val atc_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_atc", "en", "clinical/models")
    .setInputCols(Array("embeddings"))
    .setOutputCol("atc_code")
    .setDistanceFunction("EUCLIDEAN")

val resolver_pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    posology_ner, ner_converter, c2doc, embedder, atc_resolver
))

val data = Seq("The patient was started on metformin 500 mg twice daily for type 2 diabetes and was also prescribed atorvastatin for hyperlipidemia. She was given amoxicillin for a sinus infection.").toDF("text")
val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk    | entity   | atc_code   | resolution   | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:-------------|:---------|:-----------|:-------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| metformin    | DRUG     | A10BA02    | metformin    | A10BA02:::A10BD18:::A10BD28:::A10BD13:::A10BD11:::A10BD15:::A10BD20:::A10BD10:::... | 0.4268:::0.6164:::0.6204:::0.6258:::0.6401:::0.6488:::0.6597:::0.6606:::0.6607::... | 0.0911:::0.1900:::0.1924:::0.1958:::0.2049:::0.2105:::0.2176:::0.2182:::0.2183::... | metformin:::metformin and gemigliptin:::metformin and teneligliptin:::metformin ... | ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::... |
| atorvastatin | DRUG     | C10AA05    | atorvastatin | C10AA05:::C10BX03:::C10BA05:::C08CA01:::C10BA08:::C10BA16:::C10BX15:::C10AA06:::... | 0.2489:::0.6609:::0.6776:::0.7015:::0.7122:::0.7166:::0.7603:::0.7766:::0.7800::... | 0.0310:::0.2184:::0.2296:::0.2461:::0.2536:::0.2568:::0.2890:::0.3016:::0.3042::... | atorvastatin:::atorvastatin and amlodipine:::atorvastatin and ezetimibe:::Amlodi... | ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::... |
| amoxicillin  | DRUG     | J01CA04    | amoxicillin  | J01CA04:::J01CA20:::J01CF01:::J01CA01                                               | 0.3625:::0.6792:::0.7027:::0.7258                                                   | 0.0657:::0.2307:::0.2469:::0.2634                                                   | amoxicillin:::amoxicillin / clavulanate Oral Tablet:::dicloxacillin :::ampicilli... | ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th                                               |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_atc|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[atc_code]|
|Language:|en|
|Size:|110.4 MB|
|Case sensitive:|false|