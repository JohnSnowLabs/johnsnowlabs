---
layout: model
title: Sentence Entity Resolver for SNOMED (sbiobertresolve_snomed_no_class)
author: John Snow Labs
name: sbiobertresolve_snomed_no_class
date: 2026-03-16
tags: [en, snomed, resolver, licensed, clinical, no_class]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.3.0
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model utilizes BERT sentence embeddings from sbiobert_base_cased_mli to map extracted medical entities (no concept class) to SNOMED codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/05.0.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_no_class_en_6.3.0_3.4_1773691164073.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_no_class_en_6.3.0_3.4_1773691164073.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
      .setOutputCol("embeddings")

ner_jsl  = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
      .setInputCols(["sentence", "token", "embeddings"])\
      .setOutputCol("ner_jsl")


ner_jsl_converter  = NerConverterInternal()\
      .setInputCols(["sentence", "token", "ner_jsl"])\
      .setOutputCol("ner_jsl_chunk")\
      .setWhiteList(["Drug",
                 "Drug_Ingredient",
                 "Drug_BrandName",
                 "Disease_Syndrome_Disorder",
                 "Kidney_Disease",
                 "Heart_Disease",
                 "Diabetes",
                 "Oncological"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_jsl_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_no_class", "en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("snomed_code")

snomed_pipeline = Pipeline(stages = [
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    chunk2doc,
    sbert_embedder,
    snomed_resolver
])


sample_text = """John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01."""

df= spark.createDataFrame([[sample_text]]).toDF("text")

result= nlpPipeline.fit(df).transform(df)

```

{:.jsl-block}
```python


documentAssembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
      .setInputCols(["document"])\
      .setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
      .setInputCols(["sentence"]) \
      .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en", "clinical/models")\
      .setInputCols(["sentence", "token"])\
      .setOutputCol("embeddings")

ner_jsl = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models") \
      .setInputCols(["sentence", "token", "embeddings"]) \
      .setOutputCol("ner_jsl")

ner_jsl_converter   = medical.NerConverterInternal()\
      .setInputCols(["sentence", "token", "ner_jsl"])\
      .setOutputCol("ner_jsl_chunk")\
      .setWhiteList(["Drug",
                 "Drug_Ingredient",
                 "Drug_BrandName",
                 "Disease_Syndrome_Disorder",
                 "Kidney_Disease",
                 "Heart_Disease",
                 "Diabetes",
                 "Oncological"])

chunk2doc = nlp.Chunk2Doc() \
      .setInputCols("ner_jsl_chunk") \
      .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
     .setInputCols(["ner_chunk_doc"])\
     .setOutputCol("sbert_embeddings")\
     .setCaseSensitive(False)

snomed_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_no_class", "en", "clinical/models") \
     .setInputCols(["sbert_embeddings"]) \
     .setOutputCol("snomed_code")\
     .setDistanceFunction("EUCLIDEAN")

nlpPipeline= nlp.Pipeline(stages = [
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    chunk2doc,
    sbert_embedder,
    snomed_resolver
])

sample_text = """John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01."""

df= spark.createDataFrame([[sample_text]]).toDF("text")

result= nlpPipeline.fit(df).transform(df)



```
```scala


val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val nerJsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner_jsl")

val nerJslConverter = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner_jsl"))
  .setOutputCol("ner_jsl_chunk")
  .setWhiteList(["Drug",
                 "Drug_Ingredient",
                 "Drug_BrandName",
                 "Disease_Syndrome_Disorder",
                 "Kidney_Disease",
                 "Heart_Disease",
                 "Diabetes",
                 "Oncological"])

val chunk2doc = new Chunk2Doc()
  .setInputCols(Array("ner_jsl_chunk"))
  .setOutputCol("ner_chunk_doc")

val sbertEmbedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sbert_embeddings")
  .setCaseSensitive(false)

val snomedResolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_no_class", "en", "clinical/models")
  .setInputCols(Array("sbert_embeddings"))
  .setOutputCol("snomed_code")
  .setDistanceFunction("EUCLIDEAN")

val nlpPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  wordEmbeddings,
  nerJsl,
  nerJslConverter,
  chunk2doc,
  sbertEmbedder,
  snomedResolver
))


val sample_text = """John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01."""

val df= Seq(sample_text).toDF("text")

val result= nlpPipeline.fit(df).transform(df)

```
</div>

## Results

```bash

| sent_id | ner_chunk         | entity                    | snomed_code       | resolutions                  | all_codes                                          | all_resolutions                                    |
|---------|-------------------|---------------------------|-------------------|------------------------------|----------------------------------------------------|----------------------------------------------------|
| 0       | ofloxacin         | Drug_Ingredient           | 230471000087100   | besifloxacin hydrochloride   | ['230471000087100', '933450921000036101', '4557... | ['besifloxacin hydrochloride', 'leniolisib', 'c... |
| 0       | conjunctivitis    | Disease_Syndrome_Disorder | 1371396001        | allergic rhinoconjunctivitis | ['1371396001', '499932911000119106', '343631000... | ['allergic rhinoconjunctivitis', 'nodular episc... |
| 0       | cefixime          | Drug_Ingredient           | 467511000202104   | gefapixant citrate           | ['467511000202104', '455741000221101', '1695411... | ['gefapixant citrate', 'clonixin', 'durlobactam... |
| 0       | cystic urethritis | Disease_Syndrome_Disorder | 1366546000        | traumatic urethral stricture | ['1366546000', '1366548004', '15933781000119105... | ['traumatic urethral stricture', 'traumatic mem... |
| 0       | ibuprofen         | Drug_Ingredient           | 5691000122104     | mabuprofen                   | ['5691000122104', '484071000221104', '138027900... | ['mabuprofen', 'loxoprofen sodium', 'lidocaine ... |
| 0       | cilnidipine       | Drug_Ingredient           | 29670611000001104 | levomilnacipran              | ['29670611000001104', '1381610005', '1482100017... | ['levomilnacipran', 'ritalinic acid', 'lomifyll... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_no_class|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|61.4 MB|
|Case sensitive:|false|
