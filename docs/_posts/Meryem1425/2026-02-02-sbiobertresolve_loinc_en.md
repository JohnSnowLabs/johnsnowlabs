---
layout: model
title: Sentence Entity Resolver for Logical Observation Identifiers Names and Codes (LOINC) codes
author: John Snow Labs
name: sbiobertresolve_loinc
date: 2026-02-02
tags: [licensed, en, entity_resolution, loinc, clinical]
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

This model maps extracted medical entities to Logical Observation Identifiers Names and Codes (LOINC) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.
It also provides the official resolution of the codes within the brackets.

## Predicted Entities

`loinc_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_en_6.3.0_3.4_1770064907291.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_en_6.3.0_3.4_1770064907291.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
	
```python

document_assembler = DocumentAssembler()\
	.setInputCol("text")\
	.setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
	.setInputCols(["document"]) \
	.setOutputCol("sentence")

tokenizer = Tokenizer()\
	.setInputCols(["sentence"])\
	.setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
	.setInputCols(["sentence", "token"])\
	.setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models") \
	.setInputCols(["sentence", "token", "embeddings"]) \
	.setOutputCol("ner")

ner_converter = NerConverterInternal() \
 	.setInputCols(["sentence", "token", "ner"]) \
	.setOutputCol("ner_chunk")\
	.setWhiteList(["Test"])

chunk2doc = Chunk2Doc()\
  .setInputCols("ner_chunk")\
  .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
	.setInputCols(["ner_chunk_doc"])\
	.setOutputCol("sbert_embeddings")\
	.setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc","en", "clinical/models") \
	.setInputCols(["sbert_embeddings"]) \
	.setOutputCol("resolution")\
	.setDistanceFunction("EUCLIDEAN")


nlpPipeline = Pipeline(stages=[document_assembler,
                               sentence_detector,
                               tokenizer,
                               word_embeddings,
                               ner_model,
                               ner_converter,
                               chunk2doc,
                               sbert_embedder,
                               resolver])

data = spark.createDataFrame([["""A 65-year-old woman presents to the office with generalized fatigue for the last 4 months.
  She used to walk 1 mile each evening but now gets tired after 1-2 blocks. She has a history of Crohn disease and hypertension
  for which she receives appropriate medications. She is married and lives with her husband. She eats a balanced diet that
  includes chicken, fish, pork, fruits, and vegetables. She rarely drinks alcohol and denies tobacco use. A physical examination
  is unremarkable. Laboratory studies show the following: Hemoglobin: 9.8g/dL, Hematocrit: 32%, Mean Corpuscular Volume: 110 μm3"""]]).toDF("text")

result = nlpPipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
	.setInputCol("text")\
	.setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
	.setInputCols(["document"]) \
	.setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
	.setInputCols(["sentence"])\
	.setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
	.setInputCols(["sentence", "token"])\
	.setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models") \
	.setInputCols(["sentence", "token", "embeddings"]) \
	.setOutputCol("ner")

ner_converter = medical.NerConverterInternal() \
 	.setInputCols(["sentence", "token", "ner"]) \
	.setOutputCol("ner_chunk")\
	.setWhiteList(["Test"])

chunk2doc = medical.Chunk2Doc()\
  .setInputCols("ner_chunk")\
  .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
	.setInputCols(["ner_chunk_doc"])\
	.setOutputCol("sbert_embeddings")\
	.setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc","en", "clinical/models") \
	.setInputCols(["sbert_embeddings"]) \
	.setOutputCol("resolution")\
	.setDistanceFunction("EUCLIDEAN")

nlpPipeline = nlp.Pipeline(stages=[document_assembler,
                               sentence_detector,
                               tokenizer,
                               word_embeddings,
                               ner_model,
                               ner_converter,
                               chunk2doc,
                               sbert_embedder,
                               resolver])

data = spark.createDataFrame([["""A 65-year-old woman presents to the office with generalized fatigue for the last 4 months.
  She used to walk 1 mile each evening but now gets tired after 1-2 blocks. She has a history of Crohn disease and hypertension
  for which she receives appropriate medications. She is married and lives with her husband. She eats a balanced diet that
  includes chicken, fish, pork, fruits, and vegetables. She rarely drinks alcohol and denies tobacco use. A physical examination
  is unremarkable. Laboratory studies show the following: Hemoglobin: 9.8g/dL, Hematocrit: 32%, Mean Corpuscular Volume: 110 μm3"""]]).toDF("text")

result = nlpPipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
  .setInputCols(Array("sentence","token"))
  .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_jsl","en","clinical/models")
  .setInputCols(Array("sentence","token","embeddings"))
  .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
  .setInputCols(Array("sentence","token","ner"))
  .setOutputCol("ner_chunk")
  .setWhiteList(Array("Test"))

val chunk2doc = new Chunk2Doc()
  .setInputCols("ner_chunk")
  .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sbert_embeddings")
  .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc","en","clinical/models")
  .setInputCols(Array("sbert_embeddings"))
  .setOutputCol("resolution")
  .setDistanceFunction("EUCLIDEAN")

val nlpPipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_converter,
    chunk2doc,
    sbert_embedder,
    resolver))

val data = Seq([["""A 65-year-old woman presents to the office with generalized fatigue for the last 4 months.
  She used to walk 1 mile each evening but now gets tired after 1-2 blocks. She has a history of Crohn disease and hypertension
  for which she receives appropriate medications. She is married and lives with her husband. She eats a balanced diet that
  includes chicken, fish, pork, fruits, and vegetables. She rarely drinks alcohol and denies tobacco use. A physical examination
  is unremarkable. Laboratory studies show the following: Hemoglobin: 9.8g/dL, Hematocrit: 32%, Mean Corpuscular Volume: 110 μm3"""]]).toDF("text")

val result = nlpPipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------------------+-----+---+---------+----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                  chunk|begin|end|ner_label|loinc_code|                                                 description|                                                 resolutions|                                                   all_codes|                                                  aux_labels|
+-----------------------+-----+---+---------+----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|   physical examination|  450|469|     Test|   29544-4|                       Physical findings [Physical findings]|Physical findings [Physical findings]:::Physical findings...|29544-4:::29545-1:::55286-9:::11435-5:::11384-5:::8709-8:...|ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACT...|
|     Laboratory studies|  490|507|     Test|   26436-6|         Laboratory studies (set) [Laboratory studies (set)]|Laboratory studies (set) [Laboratory studies (set)]:::Lab...|26436-6:::52482-7:::11502-2:::34075-2:::100455-5:::85069-...|ACTIVE:::DISCOURAGED:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:...|
|             Hemoglobin|  529|538|     Test|   10346-5|Hemoglobin [Hemoglobin A [Units/volume] in Blood by Elect...|Hemoglobin [Hemoglobin A [Units/volume] in Blood by Elect...|10346-5:::109592-6:::11559-2:::2030-5:::34618-9:::38896-7...|ACTIVE:::TRIAL:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTI...|
|             Hematocrit|  550|559|     Test|   11559-2|   Fractional hemoglobin [Fractional oxyhemoglobin in Blood]|Fractional hemoglobin [Fractional oxyhemoglobin in Blood]...|11559-2:::10346-5:::41986-1:::48703-3:::55103-6:::8478-0:...|ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACT...|
|Mean Corpuscular Volume|  567|589|     Test|   30386-7|Erythrocyte mean corpuscular diameter [Length] [Erythrocy...|Erythrocyte mean corpuscular diameter [Length] [Erythrocy...|30386-7:::101864-7:::20161-6:::18033-1:::19853-1:::101150...|ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACT...|
+-----------------------+-----+---+---------+----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_loinc|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[loinc_code]|
|Language:|en|
|Size:|690.8 MB|
|Case sensitive:|false|

## References
This model is trained with LOINC v2.81 dataset
