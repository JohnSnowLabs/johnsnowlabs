---
layout: model
title: Sentence Entity Resolver for MeSH Codes (mpnet_embeddings_biolord_2023_c Embeddings)
author: John Snow Labs
name: biolordresolve_mesh_2026
date: 2026-08-10
tags: [en, entity_resolution, licensed, clinical, mesh, biolord]
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

This model maps clinical/veterinary entities to MeSH (Medical Subject Headings) Unique Identifiers (UI) using `mpnet_embeddings_biolord_2023_c` Sentence Embeddings.

Trained on the MeSH 2026 dataset (NLM-native descriptors, entry terms, supplemental concept records, and pharmacologic actions only).

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_mesh_2026_en_6.4.1_3.4_1786393391468.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_mesh_2026_en_6.4.1_3.4_1786393391468.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

chunk2doc = Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)\
    .setBatchSize(1)

resolver = SentenceEntityResolverModel.pretrained("biolordresolve_mesh_2026","en","clinical/models")\
    .setInputCols(["embeddings"])\
    .setOutputCol("mesh_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient has a long history of diabetes mellitus and hypertension, and presented today with pneumonia and possible myocardial infarction."]]).toDF("text")
result = pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner_model = medical.NerModel.pretrained("ner_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)\
    .setBatchSize(1)

resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_mesh_2026","en","clinical/models")\
    .setInputCols(["embeddings"])\
    .setOutputCol("mesh_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient has a long history of diabetes mellitus and hypertension, and presented today with pneumonia and possible myocardial infarction."]]).toDF("text")
result = pipeline.fit(data).transform(data)
```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val ner_model = MedicalNerModel
    .pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val chunk2doc = new Chunk2Doc()
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("ner_chunk_doc")

val embedder = MPNetEmbeddings
    .pretrained("mpnet_embeddings_biolord_2023_c", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("embeddings")
    .setCaseSensitive(false)
    .setBatchSize(1)

val resolver = SentenceEntityResolverModel
    .pretrained("biolordresolve_mesh_2026", "en", "clinical/models")
    .setInputCols(Array("embeddings"))
    .setOutputCol("mesh_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("The patient has a long history of diabetes mellitus and hypertension, and presented today with pneumonia and possible myocardial infarction.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk             | entity   | MeSH Code   | Resolution            | all_k_results                                                      | all_k_cosine_distances                              | all_k_resolutions                                                                   |
|:----------------------|:---------|:------------|:----------------------|:-------------------------------------------------------------------|:----------------------------------------------------|:------------------------------------------------------------------------------------|
| diabetes mellitus     | PROBLEM  | D003920     | diabetes mellitus     | D003920:::D005905:::C070071:::D003924:::D003922:::D002271          | 0.0000:::0.0755:::0.0978:::0.1024:::0.1100:::0.1429 | diabetes mellitus:::diabeta:::diabeton:::noninsulin dependent diabetes mellitus:... |
| hypertension          | PROBLEM  | D006973     | hypertension          | D006973:::D000075222:::D000096003:::D006974:::D058246:::D000092244 | 0.0000:::0.1106:::0.1139:::0.1724:::0.1804:::0.1828 | hypertension:::hypertension, essential:::hypertensive crises:::malignant hyperte... |
| pneumonia             | PROBLEM  | D011014     | pneumonia             | D011014:::D001996:::D018410:::D000098968:::D000092124              | 0.0000:::0.2264:::0.2603:::0.2638:::0.2705          | pneumonia:::bronchial pneumonias:::bacterial pneumonias:::community acquired pne... |
| myocardial infarction | PROBLEM  | D009203     | myocardial infarction | D009203:::D056989:::D056988:::D000088442                           | 0.0000:::0.1924:::0.1937:::0.2328                   | myocardial infarction:::diaphragmatic myocardial infarctions:::anteroseptal myoc... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_mesh_2026|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[mesh_code]|
|Language:|en|
|Size:|1.7 GB|
|Case sensitive:|false|