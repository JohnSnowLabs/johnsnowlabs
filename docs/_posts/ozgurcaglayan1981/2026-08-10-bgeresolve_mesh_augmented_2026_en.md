---
layout: model
title: Sentence Entity Resolver for MeSH Codes - Augmented (bge_base_en_v1_5_onnx Embeddings)
author: John Snow Labs
name: bgeresolve_mesh_augmented_2026
date: 2026-08-10
tags: [en, entity_resolution, licensed, clinical, mesh, bge, augmented]
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

This model maps clinical/veterinary entities to MeSH (Medical Subject Headings) Unique Identifiers (UI) using `bge_base_en_v1_5_onnx` Sentence Embeddings.

Trained on the MeSH 2026 augmented dataset (NLM-native content plus an expanded synonym pool).

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_mesh_augmented_2026_en_6.4.1_3.4_1786394778754.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_mesh_augmented_2026_en_6.4.1_3.4_1786394778754.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("bgeresolve_mesh_augmented_2026","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("mesh_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient received vaccination and was also being monitored for tuberculosis."]]).toDF("text")
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

embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_mesh_augmented_2026","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("mesh_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient received vaccination and was also being monitored for tuberculosis."]]).toDF("text")
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

val embedder = BGEEmbeddings
    .pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("bgeresolve_mesh_augmented_2026", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
    .setOutputCol("mesh_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("The patient received vaccination and was also being monitored for tuberculosis.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk    | entity    | MeSH Code   | Resolution   | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:-------------|:----------|:------------|:-------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| vaccination  | TREATMENT | D014611     | vaccination  | D014611:::D007114:::D000073887:::D000078782:::D032541:::D000088823:::D004673:::D... | 0.0000:::0.1301:::0.1560:::0.1718:::0.1885:::0.1888:::0.1915:::0.1924:::0.1937      | vaccination:::immunization:::vaccination coverage:::vaccinology:::vaccination, m... |
| tuberculosis | PROBLEM   | D014376     | tuberculosis | D014376:::D000099298:::D009169:::D014397:::D014379:::D014388:::D014396:::D014378... | 0.0000:::0.1047:::0.1073:::0.1251:::0.1817:::0.1913:::0.1947:::0.2081:::0.2100::... | tuberculosis:::tuberculosis disease:::mycobacterium tuberculosis:::pulmonary tub... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_mesh_augmented_2026|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[mesh_code]|
|Language:|en|
|Size:|2.9 GB|
|Case sensitive:|false|