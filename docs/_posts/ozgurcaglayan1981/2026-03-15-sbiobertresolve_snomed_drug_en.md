---
layout: model
title: Sentence Entity Resolver for SNOMED (sbiobertresolve_snomed_drug)
author: John Snow Labs
name: sbiobertresolve_snomed_drug
date: 2026-03-15
tags: [en, snomed, resolver, licensed, clinical, drug]
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

This model maps clinical conditions to their corresponding SNOMED (domain: Drugs) codes using sbiobert_base_cased_mli Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_drug_en_6.3.0_3.4_1773618787606.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_drug_en_6.3.0_3.4_1773618787606.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

clinical_ner  = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")


ner_converter  = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(['DRUG'])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_drug", "en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("snomed_code")

snomed_pipeline = Pipeline(stages = [
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    chunk2doc,
    sbert_embedder,
    snomed_resolver
])


sample_text = """John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD on 2023-12-01."""

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

clinical_ner  = medical.NerModel.pretrained("ner_posology", "en", "clinical/models") \
      .setInputCols(["sentence", "token", "embeddings"]) \
      .setOutputCol("ner")

ner_converter  = medical.NerConverterInternal()\
      .setInputCols(["sentence", "token", "ner"]) \
      .setOutputCol("ner_chunk")\
      .setWhiteList(['DRUG'])

chunk2doc = nlp.Chunk2Doc() \
      .setInputCols("ner_chunk") \
      .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
     .setInputCols(["ner_chunk_doc"])\
     .setOutputCol("sbert_embeddings")\
     .setCaseSensitive(False)

snomed_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_drug", "en", "clinical/models") \
     .setInputCols(["sbert_embeddings"]) \
     .setOutputCol("snomed_code")\
     .setDistanceFunction("EUCLIDEAN")

nlpPipeline= nlp.Pipeline(stages = [
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    chunk2doc,
    sbert_embedder,
    snomed_resolver
])

sample_text = """John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD on 2023-12-01."""

df= spark.createDataFrame([[sample_text]]).toDF("text")

result= nlpPipeline.fit(df).transform(df)



```
```scala


val document_assembler = DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

val ner_converter = NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")
  .setWhiteList(Array("DRUG"))

val c2doc = Chunk2Doc()
  .setInputCols("ner_chunk")
  .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sentence_embeddings")


val snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_drug", "en", "clinical/models")
  .setInputCols(Array("sentence_embeddings"))
  .setOutputCol("snomed_code")
  .setDistanceFunction("EUCLIDEAN")


resolver_pipeline = new Pipeline().setStages(
    document_assembler,
    sentenceDetectorDL,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    c2doc,
    sbert_embedder,
    snomed_resolver)


val sample_text = """John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD on 2023-12-01."""

val df= Seq(sample_text).toDF("text")

val result= nlpPipeline.fit(df).transform(df)

```
</div>

## Results

```bash

| sent_id | ner_chunk    | entity | snomed_code | resolutions  | all_codes                                          | all_resolutions                                    |
|---------|--------------|--------|-------------|--------------|----------------------------------------------------|----------------------------------------------------|
| 0       | aspirin      | DRUG   | 7947003     | aspirin      | ['7947003', '358427004', '426365001', '41256600... | ['aspirin', 'oral aspirin', 'aspirin, buffered'... |
| 0       | paracetamol  | DRUG   | 387517004   | paracetamol  | ['387517004', '90332006', '1285524005', '437876... | ['paracetamol', 'paracetamol product', 'propace... |
| 0       | amoxicillin  | DRUG   | 27658006    | amoxicillin  | ['27658006', '350162003', '372687004', '4274830... | ['amoxicillin', 'oral amoxicillin', 'amoxycilli... |
| 0       | lansoprazole | DRUG   | 108666007   | lansoprazole | ['108666007', '437961004', '441863009', '716069... | ['lansoprazole', 'oral form lansoprazole', 'dex... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_drug|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|325.7 MB|
|Case sensitive:|false|