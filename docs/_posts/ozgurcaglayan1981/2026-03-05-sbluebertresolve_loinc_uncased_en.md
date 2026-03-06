---
layout: model
title: Sentence Entity Resolver for Logical Observation Identifiers Names and Codes (LOINC) codes (sbluebert_base_uncased_mli embeddings)
author: John Snow Labs
name: sbluebertresolve_loinc_uncased
date: 2026-03-05
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

This model maps extracted medical entities to Logical Observation Identifiers Names and Codes (LOINC) codes using `sbluebert_base_uncased_mli` Sentence Bert Embeddings.
It also provides the official resolution of the codes within the brackets.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbluebertresolve_loinc_uncased_en_6.3.0_3.4_1772754582255.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbluebertresolve_loinc_uncased_en_6.3.0_3.4_1772754582255.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models")\
	.setInputCols(["sentence", "token", "embeddings"])\
	.setOutputCol("ner_radiology")

ner_converter = NerConverterInternal()\
	.setInputCols(["sentence", "token", "ner_radiology"])\
	.setOutputCol("ner_chunk_radiology")\
	.setWhiteList(["Test"])

ner_model_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
	.setInputCols(["sentence", "token", "embeddings"])\
	.setOutputCol("ner_jsl")

ner_converter_jsl = NerConverterInternal()\
	.setInputCols(["sentence", "token", "ner_jsl"])\
	.setOutputCol("ner_chunk_jsl")\
	.setWhiteList(["Test"])

chunk_merger = ChunkMergeApproach()\
	.setInputCols("ner_chunk_jsl", "ner_chunk_radiology")\
	.setOutputCol('merged_ner_chunk')

chunk2doc = Chunk2Doc()\
	.setInputCols("merged_ner_chunk")\
	.setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbluebert_base_uncased_mli", "en", "clinical/models")\
	.setInputCols(["ner_chunk_doc"])\
	.setOutputCol("sbluebert_embeddings")\
	.setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbluebertresolve_loinc_uncased","en", "clinical/models") \
	.setInputCols(["sbluebert_embeddings"]) \
	.setOutputCol("resolution")\
	.setDistanceFunction("EUCLIDEAN")


nlpPipeline = Pipeline(stages=[document_assembler,
								sentence_detector,
								tokenizer,
								word_embeddings,
								ner_model,
								ner_converter,
								ner_model_jsl,
								ner_converter_jsl,
								chunk_merger,
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

ner_model = medical.NerModel.pretrained("ner_radiology", "en", "clinical/models")\
 	.setInputCols(["sentence", "token", "embeddings"])\
 	.setOutputCol("ner_radiology")

ner_converter = medical.NerConverterInternal()\
  	  .setInputCols(["sentence", "token", "ner_radiology"])\
 	  .setOutputCol("ner_chunk_radiology")\
	  .setWhiteList(["Test"])

ner_model_jsl = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models")\
 	.setInputCols(["sentence", "token", "embeddings"])\
 	.setOutputCol("ner_jsl")

ner_converter_jsl = medical.NerConverterInternal()\
  	  .setInputCols(["sentence", "token", "ner_jsl"])\
 	  .setOutputCol("ner_chunk_jsl")\
	  .setWhiteList(["Test"])

chunk_merger = medical.ChunkMergeApproach()\
    .setInputCols("ner_chunk_jsl", "ner_chunk_radiology")\
    .setOutputCol('merged_ner_chunk')

chunk2doc = medical.Chunk2Doc()\
  	.setInputCols("merged_ner_chunk")\
  	.setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbluebert_base_uncased_mli", "en", "clinical/models")\
		.setInputCols(["ner_chunk_doc"])\
		.setOutputCol("sbluebert_embeddings")\
		.setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbluebertresolve_loinc_uncased","en", "clinical/models") \
	.setInputCols(["sbluebert_embeddings"]) \
	.setOutputCol("resolution")\
	.setDistanceFunction("EUCLIDEAN")


nlpPipeline = nlp.Pipeline(stages=[document_assembler,
                               sentence_detector,
                               tokenizer,
                               word_embeddings,
                               ner_model,
                               ner_converter,
  							   ner_model_jsl,
							   ner_converter_jsl,
 							   chunk_merger,
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

val ner_model = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models")\
 	.setInputCols(["sentence", "token", "embeddings"])\
 	.setOutputCol("ner_radiology")

val ner_converter = new NerConverterInternal()\
  	  .setInputCols(["sentence", "token", "ner_radiology"])\
 	  .setOutputCol("ner_chunk_radiology")\
	  .setWhiteList(["Test"])

val ner_model_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
 	.setInputCols(["sentence", "token", "embeddings"])\
 	.setOutputCol("ner_jsl")

val ner_converter_jsl = new NerConverterInternal()\
  	  .setInputCols(["sentence", "token", "ner_jsl"])\
 	  .setOutputCol("ner_chunk_jsl")\
	  .setWhiteList(["Test"])

val chunk_merger = new ChunkMergeApproach()\
    .setInputCols("ner_chunk_jsl", "ner_chunk_radiology")\
    .setOutputCol('merged_ner_chunk')

val chunk2doc = new Chunk2Doc()\
  	.setInputCols("merged_ner_chunk")\
  	.setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbluebert_base_uncased_mli", "en", "clinical/models")\
		.setInputCols(["ner_chunk_doc"])\
		.setOutputCol("sbluebert_embeddings")\
		.setCaseSensitive(False)

val resolver = SentenceEntityResolverModel.pretrained("sbluebertresolve_loinc_uncased","en", "clinical/models") \
	.setInputCols(["sbluebert_embeddings"]) \
	.setOutputCol("resolution")\
	.setDistanceFunction("EUCLIDEAN")


val nlpPipeline = new Pipeline(stages=[document_assembler,
                               sentence_detector,
                               tokenizer,
                               word_embeddings,
                               ner_model,
                               ner_converter,
							   ner_model_jsl,
 							   ner_converter_jsl,
							   chunk_merger,
                               chunk2doc,
                               sbert_embedder,
                               resolver])

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

| chunk                   | begin | end | ner_label | loinc_code | description                                                     | resolutions                                                                 | all_codes                                                                 | aux_labels                                                                |
|-------------------------|------:|----:|-----------|------------|-----------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
| physical examination    | 450   | 469 | Test      | 29544-4    | Physical findings [Physical findings]                           | Physical findings [Physical findings]:::Physical exam by ...                | 29544-4:::11384-5:::100223-7:::29545-1:::100038-9:::89492...              | ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACT...              |
| Laboratory studies      | 490   | 507 | Test      | 26436-6    | Laboratory studies (set) [Laboratory studies (set)]             | Laboratory studies (set) [Laboratory studies (set)]:::Lab...                | 26436-6:::11502-2:::52482-7:::34075-2:::100455-5:::56850-...              | ACTIVE:::ACTIVE:::DISCOURAGED:::ACTIVE:::ACTIVE:::ACTIVE:...              |
| Hemoglobin              | 529   | 538 | Test      | 10346-5    | Hemoglobin [Hemoglobin A [Units/volume] in Blood by Elect...]   | Hemoglobin [Hemoglobin A [Units/volume] in Blood by Elect...]               | 10346-5:::2030-5:::109592-6:::11559-2:::50191-6:::101634-...              | ACTIVE:::ACTIVE:::TRIAL:::ACTIVE:::ACTIVE:::ACTIVE:::ACTI...              |
| Hematocrit              | 550   | 559 | Test      | 101655-9   | Hct [Basic metabolic and hematocrit panel - Blood]              | Hct [Basic metabolic and hematocrit panel - Blood]:::stea...                | 101655-9:::103845-4:::10346-5:::16966-4:::12250-7:::24360...              | ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::DISCOURAGED:::ACTIVE:...              |
| Mean Corpuscular Volume | 567   | 589 | Test      | 82627-1    | Mean phase [Mean phase [Angle] Left ventricle SPECT --W s...]   | Mean phase [Mean phase [Angle] Left ventricle SPECT --W s...]               | 82627-1:::33878-0:::59117-2:::60949-5:::8478-0:::103205-1...              | ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACTIVE:::ACT...              |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbluebertresolve_loinc_uncased|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sbluebert_embeddings]|
|Output Labels:|[loinc_code]|
|Language:|en|
|Size:|693.1 MB|
|Case sensitive:|false|
