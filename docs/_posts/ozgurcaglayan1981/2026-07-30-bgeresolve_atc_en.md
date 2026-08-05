---
layout: model
title: Sentence Entity Resolver for ATC (bge_base_en_v1_5_onnx embeddings)
author: John Snow Labs
name: bgeresolve_atc
date: 2026-07-30
tags: [en, entity_resolution, licensed, clinical, atc, bge]
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

This model maps drugs entities to ATC (Anatomic Therapeutic Chemical) codes using `bge_base_en_v1_5_onnx` Sentence Embeddings. Trained on the WHO ATC-DDD dataset (release 2026-04-25).

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_atc_en_6.4.1_3.4_1785445055939.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_atc_en_6.4.1_3.4_1785445055939.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

atc_resolver = SentenceEntityResolverModel.pretrained("bgeresolve_atc", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

atc_resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_atc", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

val embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")
    .setCaseSensitive(false)

val atc_resolver = SentenceEntityResolverModel.pretrained("bgeresolve_atc", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
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
| metformin    | DRUG     | A10BA02    | metformin    | A10BA02:::A10BB07:::A10BD07:::A10BD13:::A10BD14:::A10BH04:::A10BD10:::A10BD17:::... | 0.0000:::0.5619:::0.5648:::0.5930:::0.6003:::0.6014:::0.6034:::0.6121:::0.6125::... | 0.0000:::0.1579:::0.1595:::0.1758:::0.1802:::0.1808:::0.1820:::0.1873:::0.1876::... | metformin :::glipizide / metformin :::metformin / sitagliptin :::metformin and a... | ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::... |
| atorvastatin | DRUG     | C10AA05    | atorvastatin | C10AA05:::C10BA05:::C10AA02:::C10BX03:::C10AA04:::C10AA06:::C10BX08:::C10BA08:::... | 0.0000:::0.6086:::0.6206:::0.6311:::0.6335:::0.6591:::0.6618:::0.6680:::0.6759::... | 0.0000:::0.1852:::0.1926:::0.1992:::0.2006:::0.2172:::0.2190:::0.2231:::0.2284::... | atorvastatin:::atorvastatin / ezetimibe :::lovastatin:::amlodipine / atorvastati... | ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::... |
| amoxicillin  | DRUG     | J01CA04    | amoxicillin  | J01CA04:::J01CR02:::R05CB02                                                         | 0.0000:::0.5697:::0.5825                                                            | 0.0000:::0.1623:::0.1696                                                            | amoxicillin:::amoxicillin and enzyme inhibitor:::amoxicillin / bromhexine           | ATC 5th:::ATC 5th:::ATC 5th                                                         |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_atc|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[atc_code]|
|Language:|en|
|Size:|110.3 MB|
|Case sensitive:|false|
