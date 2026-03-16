---
layout: model
title: Sentence Entity Resolver for SNOMED (sbiobertresolve_snomed_veterinary)
author: John Snow Labs
name: sbiobertresolve_snomed_veterinary
date: 2026-03-16
tags: [en, snomed, resolver, licensed, clinical, veterinary]
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

This model maps veterinary-related entities and concepts to SNOMED codes using sbiobert_base_cased_mli Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/05.0.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_veterinary_en_6.3.0_3.4_1773696345835.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_veterinary_en_6.3.0_3.4_1773696345835.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_clinical  = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
      .setInputCols(["sentence", "token", "embeddings"])\
      .setOutputCol("ner")


ner_converter  = NerConverterInternal()\
      .setInputCols(["sentence", "token", "ner"])\
      .setOutputCol("ner_chunk")\
      .setWhiteList(['PROBLEM'])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_veterinary", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("snomed_code")

snomed_pipeline = Pipeline(stages = [
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_clinical,
    ner_converter,
    chunk2doc,
    sbert_embedder,
    snomed_resolver
])


sample_text = """The veterinary team, is closely monitoring the patient for signs of lymphoblastic lymphoma, a malignant neoplasm of lymphoid origin. They are also treating the patient's osteoarthritis, a degenerative joint disease. Additionally, the team is vigilantly observing the facility for potential outbreaks of mink distemper."""

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

ner_clinical = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models") \
      .setInputCols(["sentence", "token", "embeddings"]) \
      .setOutputCol("ner")

ner_converter   = medical.NerConverterInternal()\
      .setInputCols(["sentence", "token", "ner"])\
      .setOutputCol("ner_chunk")\
      .setWhiteList(['PROBLEM'])

chunk2doc = nlp.Chunk2Doc() \
      .setInputCols("ner_chunk") \
      .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

snomed_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_veterinary", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")

nlpPipeline= nlp.Pipeline(stages = [
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    ner_clinical,
    ner_converter,
    chunk2doc,
    sbert_embedder,
    snomed_resolver
])

sample_text = """The veterinary team, is closely monitoring the patient for signs of lymphoblastic lymphoma, a malignant neoplasm of lymphoid origin. They are also treating the patient's osteoarthritis, a degenerative joint disease. Additionally, the team is vigilantly observing the facility for potential outbreaks of mink distemper."""

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

val nerClinical = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

val nerConverter = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")
  .setWhiteList(['PROBLEM'])

val chunk2doc = new Chunk2Doc()
  .setInputCols(Array("ner_chunk"))
  .setOutputCol("ner_chunk_doc")

val sbertEmbedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
    .setInputCols(["ner_chunk_doc"])
    .setOutputCol("sentence_embeddings")
    .setCaseSensitive(False)

val snomedResolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_veterinary", "en", "clinical/models")
  .setInputCols(Array("sentence_embeddings"))
  .setOutputCol("snomed_code")
  .setDistanceFunction("EUCLIDEAN")

val nlpPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  wordEmbeddings,
  nerClinical,
  nerConverter,
  chunk2doc,
  sbertEmbedder,
  snomedResolver
))


val sample_text = """The veterinary team, is closely monitoring the patient for signs of lymphoblastic lymphoma, a malignant neoplasm of lymphoid origin. They are also treating the patient's osteoarthritis, a degenerative joint disease. Additionally, the team is vigilantly observing the facility for potential outbreaks of mink distemper."""

val df= Seq(sample_text).toDF("text")

val result= nlpPipeline.fit(df).transform(df)

```
</div>

## Results

```bash

| sent_id | ner_chunk                               | entity  | snomed_code     | resolutions                                        | all_codes                                          | all_resolutions                                    |
|---------|-----------------------------------------|---------|-----------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|
| 0       | lymphoblastic lymphoma                  | PROBLEM | 312281000009102 | lymphoblastic lymphoma                             | ['312281000009102', '1217301006', '421246008', ... | ['lymphoblastic lymphoma', 'malignant lymphobla... |
| 0       | a malignant neoplasm of lymphoid origin | PROBLEM | 443495005       | neoplasm of lymphoid system structure              | ['443495005', '1156403002', '277604002', '12722... | ['neoplasm of lymphoid system structure', 'comp... |
| 1       | the patient's osteoarthritis            | PROBLEM | 201826000       | erosive osteoarthrosis                             | ['201826000', '43829003', '735598004', '4435240... | ['erosive osteoarthrosis', 'chronic osteoarthri... |
| 1       | a degenerative joint disease            | PROBLEM | 201819000       | degenerative joint disease involving multiple j... | ['201819000', '1287058006', '363056008', '39926... | ['degenerative joint disease involving multiple... |
| 2       | mink distemper                          | PROBLEM | 348361000009108 | mink distemper                                     | ['348361000009108', '86031000009108', '20719100... | ['mink distemper', 'dendropicos obsoletus', 'xe... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_veterinary|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|745.3 MB|
|Case sensitive:|false|
