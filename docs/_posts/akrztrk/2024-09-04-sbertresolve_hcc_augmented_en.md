---
layout: model
title: Sentence Entity Resolver for Hierarchical Condition Categories (HCC) codes (Augmented)
author: John Snow Labs
name: sbertresolve_hcc_augmented
date: 2024-09-04
tags: [licensed, en, hcc, entity_resolution, clinical]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted medical entities to Hierarchical Condition Categories (HCC) codes using `sbert_jsl_medium_uncased` Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbertresolve_hcc_augmented_en_5.4.0_3.0_1725452848605.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbertresolve_hcc_augmented_en_5.4.0_3.0_1725452848605.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embeddings = BertSentenceEmbeddings.pretrained("sbert_jsl_medium_uncased", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bert_embeddings")\
    .setCaseSensitive(False)

icd_resolver = SentenceEntityResolverModel.pretrained("sbertresolve_hcc_augmented", "en", "clinical/models")\
    .setInputCols(["bert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages = [document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       embeddings,
                                       icd_resolver])

data = spark.createDataFrame([["""The patient's medical record indicates reticulosarcoma of the spleen and chronic obstructive pulmonary disease, requiring comprehensive care and management."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList("PROBLEM")

val c2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val embeddings = BertSentenceEmbeddings.pretrained("sbert_jsl_medium_uncased", "en", "clinical/models")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("bert_embeddings")
    .setCaseSensitive(False)

val icd_resolver = SentenceEntityResolverModel.pretrained("sbertresolve_hcc_augmented", "en", "clinical/models")
    .setInputCols("mpnet_embeddings")
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(document_assembler,
                               sentenceDetectorDL,
                               tokenizer,
                               word_embeddings,
                               ner,
                               ner_converter,
                               c2doc,
                               embeddings,
                               icd10_resolver))

val data = Seq([["""The patient's medical record indicates reticulosarcoma of the spleen and chronic obstructive pulmonary disease, requiring comprehensive care and management."""]]).toDF("text")

val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-------------------------------------+-----+---+---------+--------+------------------------------------------------------------+------------------------------------------------------------+-----------+
|                                chunk|begin|end|ner_label|hcc_code|                                                 description|                                                 resolutions|  all_codes|
+-------------------------------------+-----+---+---------+--------+------------------------------------------------------------+------------------------------------------------------------+-----------+
|        reticulosarcoma of the spleen|   39| 67|  PROBLEM|       0|   reticulosarcoma of spleen [diffuse large b-cell lymphoma]|reticulosarcoma of spleen [diffuse large b-cell lymphoma]...|0:::10:::11|
|chronic obstructive pulmonary disease|   73|109|  PROBLEM|     111|chronic obstructive pulmonary disease [chronic obstructiv...|chronic obstructive pulmonary disease [chronic obstructiv...|    111:::0|
+-------------------------------------+-----+---+---------+--------+------------------------------------------------------------+------------------------------------------------------------+-----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbertresolve_hcc_augmented|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[hcc_code]|
|Language:|en|
|Size:|886.8 MB|
|Case sensitive:|false|
