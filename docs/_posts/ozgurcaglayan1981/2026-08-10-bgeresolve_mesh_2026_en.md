---
layout: model
title: Sentence Entity Resolver for MeSH Codes (bge_base_en_v1_5_onnx Embeddings)
author: John Snow Labs
name: bgeresolve_mesh_2026
date: 2026-08-10
tags: [en, entity_resolution, licensed, clinical, mesh, bge]
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

Trained on the MeSH 2026 dataset (NLM-native descriptors, entry terms, supplemental concept records, and pharmacologic actions only).

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_mesh_2026_en_6.4.1_3.4_1786393893621.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_mesh_2026_en_6.4.1_3.4_1786393893621.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

resolver = SentenceEntityResolverModel.pretrained("bgeresolve_mesh_2026","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_mesh_2026","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

val embedder = BGEEmbeddings
    .pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("bgeresolve_mesh_2026", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
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
| ner_chunk             | entity   | MeSH Code   | Resolution            | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:----------------------|:---------|:------------|:----------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| diabetes mellitus     | PROBLEM  | D003920     | diabetes mellitus     | D003920:::D003924:::D003922:::D048909:::D000071698:::D016640:::C563959:::C566602... | 0.0000:::0.1077:::0.1174:::0.1290:::0.1528:::0.1642:::0.1884:::0.1911:::0.1949::... | diabetes mellitus:::type 2 diabetes mellitus:::type 1 diabetes mellitus:::diabet... |
| hypertension          | PROBLEM  | D006973     | hypertension          | D006973:::D001794:::D006977:::D000092244:::D000075222:::D000959:::D000096003:::D... | 0.0000:::0.0933:::0.1142:::0.1500:::0.1896:::0.1966:::0.2072:::0.2082:::0.2084::... | hypertension:::blood pressure:::renal hypertension:::systolic hypertension:::ess... |
| pneumonia             | PROBLEM  | D011014     | pneumonia             | D011014:::D011018:::D018410:::D001996:::D011024:::D011019:::D011020:::D017564:::... | 0.0000:::0.1131:::0.1131:::0.1355:::0.1498:::0.1626:::0.1719:::0.1750:::0.1780::... | pneumonia:::pneumococcal pneumonia:::bacterial pneumonia:::bronchial pneumonia::... |
| myocardial infarction | PROBLEM  | D009203     | myocardial infarction | D009203:::D007238:::D017202:::D000789:::D000072658:::D056989:::D000072657           | 0.0000:::0.1326:::0.1335:::0.1668:::0.1751:::0.1806:::0.1865                        | myocardial infarction:::infarction:::myocardial ischemia:::myocardial preinfarct... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_mesh_2026|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[mesh_code]|
|Language:|en|
|Size:|1.7 GB|
|Case sensitive:|false|