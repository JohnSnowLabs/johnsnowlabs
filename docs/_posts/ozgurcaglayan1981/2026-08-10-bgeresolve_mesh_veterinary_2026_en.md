---
layout: model
title: Sentence Entity Resolver for MeSH Codes - Veterinary (bge_base_en_v1_5_onnx Embeddings)
author: John Snow Labs
name: bgeresolve_mesh_veterinary_2026
date: 2026-08-10
tags: [en, entity_resolution, licensed, clinical, mesh, bge, veterinary]
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

Trained on the MeSH 2026 dataset, augmented by JSL with a veterinary-focused scope.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_mesh_veterinary_2026_en_6.4.1_3.4_1786395767689.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_mesh_veterinary_2026_en_6.4.1_3.4_1786395767689.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

resolver = SentenceEntityResolverModel.pretrained("bgeresolve_mesh_veterinary_2026","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("mesh_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The dog was diagnosed with rabies and treated with vaccination; tick infestations were also noted, along with coccidiosis."]]).toDF("text")
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

resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_mesh_veterinary_2026","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("mesh_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The dog was diagnosed with rabies and treated with vaccination; tick infestations were also noted, along with coccidiosis."]]).toDF("text")
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
    .pretrained("bgeresolve_mesh_veterinary_2026", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
    .setOutputCol("mesh_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("The dog was diagnosed with rabies and treated with vaccination; tick infestations were also noted, along with coccidiosis.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk         | entity    | MeSH Code   | Resolution        | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:------------------|:----------|:------------|:------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| rabies            | PROBLEM   | D011818     | rabies            | D011818:::D011820:::D018114:::D017992                                               | 0.0000:::0.0597:::0.2011:::0.2824                                                   | rabies:::rabies virus:::rabies virus group:::parvovirus, raccoon                    |
| vaccination       | TREATMENT | D014611     | vaccination       | D014611:::D007114:::D032541:::D004673:::D007117:::D003888                           | 0.0000:::0.1301:::0.1885:::0.1915:::0.1979:::0.2168                                 | vaccination:::immunization:::vaccination, mass:::vaccination encephalitis:::boos... |
| tick infestations | PROBLEM   | D013984     | tick infestations | D013984:::D013987:::D064927:::D004478:::D000712:::D008924:::D026863:::D017282:::... | 0.0000:::0.1277:::0.1788:::0.1809:::0.1847:::0.1860:::0.2003:::0.2039:::0.2056::... | tick infestations:::ticks:::tick bites:::ectoparasitic infestations:::tick fever... |
| coccidiosis       | PROBLEM   | D003048     | coccidiosis       | D003048:::D003047                                                                   | 0.0000:::0.1034                                                                     | coccidiosis:::coccidioidomycosis                                                    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_mesh_veterinary_2026|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[mesh_code]|
|Language:|en|
|Size:|539.7 MB|
|Case sensitive:|false|