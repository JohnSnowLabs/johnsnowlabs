---
layout: model
title: Sentence Entity Resolver for SNOMED (sbiobertresolve_snomed_procedures_measurements)
author: John Snow Labs
name: sbiobertresolve_snomed_procedures_measurements
date: 2026-03-16
tags: [en, snomed, resolver, licensed, clinical, procedure, measurements]
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

This model maps Procedure and Measurements (Tests) to their corresponding SNOMED codes using sbiobert_base_cased_mli Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_procedures_measurements_en_6.3.0_3.4_1773692020731.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_procedures_measurements_en_6.3.0_3.4_1773692020731.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
      .setWhiteList(['Procedure','Test'])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_jsl_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_procedures_measurements", "en", "clinical/models") \
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


sample_text = """Based on the severity of her abdominal examination and the persistence of her symptoms, it has been determined that she requires a laparoscopic jejunectomy, possible appendectomy, and cholecystectomy.Laboratory values indicate a white blood cell count of 15.3, plasma hemoglobin level of 12.8, and normal platelet count. Alkaline phosphatase is elevated at 184, while liver function tests are otherwise normal. Electrolyte levels are within the normal range. Glucose levels are at 134, BUN is 4, and creatinine is 0.7."""

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
      .setWhiteList(['Procedure','Test'])

chunk2doc = nlp.Chunk2Doc() \
      .setInputCols("ner_jsl_chunk") \
      .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
     .setInputCols(["ner_chunk_doc"])\
     .setOutputCol("sbert_embeddings")\
     .setCaseSensitive(False)

snomed_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_procedures_measurements", "en", "clinical/models") \
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

sample_text = """Based on the severity of her abdominal examination and the persistence of her symptoms, it has been determined that she requires a laparoscopic jejunectomy, possible appendectomy, and cholecystectomy.Laboratory values indicate a white blood cell count of 15.3, plasma hemoglobin level of 12.8, and normal platelet count. Alkaline phosphatase is elevated at 184, while liver function tests are otherwise normal. Electrolyte levels are within the normal range. Glucose levels are at 134, BUN is 4, and creatinine is 0.7."""

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
  .setWhiteList(['Procedure','Test'])

val chunk2doc = new Chunk2Doc()
  .setInputCols(Array("ner_jsl_chunk"))
  .setOutputCol("ner_chunk_doc")

val sbertEmbedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sbert_embeddings")
  .setCaseSensitive(false)

val snomedResolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_procedures_measurements", "en", "clinical/models")
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


val sample_text = """Based on the severity of her abdominal examination and the persistence of her symptoms, it has been determined that she requires a laparoscopic jejunectomy, possible appendectomy, and cholecystectomy.Laboratory values indicate a white blood cell count of 15.3, plasma hemoglobin level of 12.8, and normal platelet count. Alkaline phosphatase is elevated at 184, while liver function tests are otherwise normal. Electrolyte levels are within the normal range. Glucose levels are at 134, BUN is 4, and creatinine is 0.7."""

val df= Seq(sample_text).toDF("text")

val result= nlpPipeline.fit(df).transform(df)

```
</div>

## Results

```bash

| sent_id | ner_chunk                | entity    | snomed_code | resolutions                      | all_codes                                          | all_resolutions                                    |
|---------|--------------------------|-----------|-------------|----------------------------------|----------------------------------------------------|----------------------------------------------------|
| 0       | laparoscopic jejunectomy | Procedure | 1220546008  | laparoscopic jejunectomy         | ['1220546008', '6025007', '307195003', '1220549... | ['laparoscopic jejunectomy', 'laparoscopic appe... |
| 0       | appendectomy             | Procedure | 80146002    | appendectomy                     | ['80146002', '17041004', '82730006', '174045003... | ['appendectomy', 'appendicotomy', 'secondary ap... |
| 0       | cholecystectomy          | Procedure | 38102005    | cholecystectomy                  | ['38102005', '6402000', '44337006', '45595009',... | ['cholecystectomy', 'choledochectomy', 'cholecy... |
| 1       | white blood cell count   | Test      | 767002      | white blood cell count           | ['767002', '252305002', '165511009', '44190001'... | ['white blood cell count', 'white blood cell te... |
| 1       | plasma hemoglobin level  | Test      | 104142005   | plasma hemoglobin level          | ['104142005', '271510004', '313995005', '271026... | ['plasma hemoglobin level', 'hemoglobin s level... |
| 1       | platelet count           | Test      | 61928009    | platelet count                   | ['61928009', '250314004', '8574009', '75672003'... | ['platelet count', 'plateletcrit', 'platelet es... |
| 2       | Alkaline phosphatase     | Test      | 88810008    | alkaline phosphatase measurement | ['88810008', '45745006', '271234008', '39096200... | ['alkaline phosphatase measurement', 'alkaline ... |
| 2       | liver function tests     | Test      | 26958001    | liver function tests             | ['26958001', '269856004', '736164009', '2878580... | ['liver function tests', 'liver enzyme levels',... |
| 2       | Electrolyte levels       | Test      | 79301008    | electrolytes measurement         | ['79301008', '276025008', '312474003', '4011420... | ['electrolytes measurement', 'electrolyte regul... |
| 3       | Glucose levels           | Test      | 36048009    | glucose measurement              | ['36048009', '72191006', '302789003', '16688800... | ['glucose measurement', 'plasma glucose', 'capi... |
| 3       | BUN                      | Test      | 24509005    | bun measurement                  | ['24509005', '16227009', '85651007', '174651007... | ['bun measurement', 'cinching', 'bost operation... |
| 3       | creatinine               | Test      | 113075003   | serum creatinine                 | ['113075003', '70901006', '313936008', '2507450... | ['serum creatinine', 'creatinine measurement', ... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_procedures_measurements|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|340.6 MB|
|Case sensitive:|false|