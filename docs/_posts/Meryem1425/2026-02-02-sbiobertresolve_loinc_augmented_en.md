---
layout: model
title: Sentence Entity Resolver for LOINC (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_loinc_augmented
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

This model maps extracted clinical NER entities to Logical Observation Identifiers Names and Codes(LOINC) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. It trained on the augmented version of the dataset which is used in previous LOINC resolver models. It also provides the official resolution of the codes within the brackets.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_augmented_en_6.3.0_3.4_1770070086475.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_loinc_augmented_en_6.3.0_3.4_1770070086475.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models") \
	.setInputCols(["sentence", "token", "embeddings"]) \
	.setOutputCol("ner_radiology")

ner_converter = NerConverterInternal() \
 	.setInputCols(["sentence", "token", "ner_radiology"]) \
	.setOutputCol("ner_chunk_radiology")\
	.setWhiteList(["Test"])

ner_model_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models") \
	.setInputCols(["sentence", "token", "embeddings"]) \
	.setOutputCol("ner_jsl")

ner_converter_jsl = NerConverterInternal() \
 	.setInputCols(["sentence", "token", "ner_jsl"]) \
	.setOutputCol("ner_chunk_jsl")	.setWhiteList(["Test"])

chunk_merger = ChunkMergeApproach()\
  .setInputCols("ner_chunk_jsl", "ner_chunk_radiology")\
  .setOutputCol('merged_ner_chunk')

chunk2doc = Chunk2Doc()\
  .setInputCols("merged_ner_chunk")\
  .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
	.setInputCols(["ner_chunk_doc"])\
	.setOutputCol("sbert_embeddings")\
	.setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc_augmented","en", "clinical/models") \
	.setInputCols(["sbert_embeddings"]) \
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

data = spark.createDataFrame([["""The patient is a 22-year-old female with a history of obesity. She has a Body mass index (BMI) of 33.5 kg/m2, aspartate aminotransferase 64, and alanine aminotransferase 126."""]]).toDF("text")

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

ner_model = medical.NerModel.pretrained("ner_radiology", "en", "clinical/models") \
	.setInputCols(["sentence", "token", "embeddings"]) \
	.setOutputCol("ner_radiology")

ner_converter = medical.NerConverterInternal() \
 	.setInputCols(["sentence", "token", "ner_radiology"]) \
	.setOutputCol("ner_chunk_radiology")\
	.setWhiteList(["Test"])

ner_model_jsl = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models") \
	.setInputCols(["sentence", "token", "embeddings"]) \
	.setOutputCol("ner_jsl")

ner_converter_jsl = medical.NerConverterInternal() \
 	.setInputCols(["sentence", "token", "ner_jsl"]) \
	.setOutputCol("ner_chunk_jsl")\
	.setWhiteList(["Test"])

chunk_merger = medical.ChunkMergeApproach()\
  .setInputCols("ner_chunk_jsl", "ner_chunk_radiology")\
  .setOutputCol('merged_ner_chunk')

chunk2doc = medical.Chunk2Doc()\
  .setInputCols("merged_ner_chunk")\
  .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
	.setInputCols(["ner_chunk_doc"])\
	.setOutputCol("sbert_embeddings")\
	.setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc_augmented","en", "clinical/models") \
	.setInputCols(["sbert_embeddings"]) \
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

data = spark.createDataFrame([["""The patient is a 22-year-old female with a history of obesity. She has a Body mass index (BMI) of 33.5 kg/m2, aspartate aminotransferase 64, and alanine aminotransferase 126."""]]).toDF("text")

result = nlpPipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
	.setInputCols("document")
	.setOutputCol("sentence")

val tokenizer = new Tokenizer()
	.setInputCols("sentence")
	.setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
	.setInputCols(Array("sentence", "token"))
	.setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models")
	.setInputCols(Array("sentence", "token", "embeddings"))
	.setOutputCol("ner_radiology")

val ner_converter = new NerConverterInternal()
 	.setInputCols(Array("sentence", "token", "ner_radiology"))
	.setOutputCol("ner_chunk_radiology")
	.setWhiteList(Array("Test"))

val ner_model_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
	.setInputCols(Array("sentence", "token", "embeddings"))
	.setOutputCol("ner_jsl")

val ner_converter_jsl = new NerConverterInternal()
 	.setInputCols(Array("sentence", "token", "ner_jsl"))
	.setOutputCol("ner_chunk_jsl")
	.setWhiteList(Array("Test"))

val chunk_merger = new ChunkMergeApproach()
  .setInputCols(Array("ner_chunk_jsl", "ner_chunk_radiology"))
  .setOutputCol("merged_ner_chunk")

val chunk2doc = new Chunk2Doc()
  .setInputCols("merged_ner_chunk")
  .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
	.setInputCols("ner_chunk_doc")
	.setOutputCol("sbert_embeddings")
	.setCaseSensitive(false)

val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc_augmented","en", "clinical/models")
	.setInputCols("sbert_embeddings")
	.setOutputCol("resolution")
	.setDistanceFunction("EUCLIDEAN")

val nlpPipeline = new Pipeline().setStages(Array(
    document_assembler,
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
    resolver))

val data = Seq([["""The patient is a 22-year-old female with a history of obesity. She has a Body mass index (BMI) of 33.5 kg/m2, aspartate aminotransferase 64, and alanine aminotransferase 126."""]]).toDF("text")

val result = nlpPipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+--------------------------+-----+---+---------+----------+-------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                     chunk|begin|end|ner_label|loinc_code|                                            description|                                                 resolutions|                                                   all_codes|                                                  aux_labels|
+--------------------------+-----+---+---------+----------+-------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                       BMI|   90| 92|     Test|   39156-5|                    BMI [Body mass index (BMI) [Ratio]]|BMI [Body mass index (BMI) [Ratio]]:::BM [IDH1 gene exon ...|39156-5:::100305-2:::LP266933-3:::100225-2:::LP241982-0::...|Observation:::Measurement:::Observation:::Observation:::O...|
|aspartate aminotransferase|  110|135|     Test| LP15426-7|Aspartate aminotransferase [Aspartate aminotransferase]|Aspartate aminotransferase [Aspartate aminotransferase]::...|LP15426-7:::43822-6:::100739-2:::LP307348-5:::LP15333-5::...|Observation:::Measurement:::Observation:::Observation:::O...|
|  alanine aminotransferase|  145|168|     Test| LP15333-5|    Alanine aminotransferase [Alanine aminotransferase]|Alanine aminotransferase [Alanine aminotransferase]:::Ala...|LP15333-5:::77144-4:::LP307326-1:::100738-4:::LP307348-5:...|Observation:::Observation:::Observation:::Observation:::O...|
+--------------------------+-----+---+---------+----------+-------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_loinc_augmented|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[loinc_code]|
|Language:|en|
|Size:|1.2 GB|
|Case sensitive:|false|