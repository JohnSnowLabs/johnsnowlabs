---
layout: model
title: Sentence Entity Resolver for CPT Codes (Procedures and Measurements) - Augmented (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_cpt_procedures_measurements_augmented
date: 2024-05-08
tags: [licensed, en, biolord, cpt, entity_resolution, clinical]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps medical entities to CPT codes using `mpnet_embeddings_biolord_2023_c` embeddings. The corpus of this model has been extented to measurements, and this model is capable of mapping both procedures and measurement concepts/entities to CPT codes. Measurement codes are helpful in codifying medical entities related to tests and their results.

**NOTE**: This model can be used with spark v3.4.0 and above versions.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_cpt_procedures_measurements_augmented_en_5.3.1_3.4_1715166832452.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_cpt_procedures_measurements_augmented_en_5.3.1_3.4_1715166832452.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()	  .setInputCol("text")	  .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") 	  .setInputCols(["document"])	  .setOutputCol("sentence")

tokenizer = Tokenizer()	  .setInputCols(["sentence"])	  .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")	  .setInputCols(["sentence", "token"])	  .setOutputCol("word_embeddings")

ner = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models") 	  .setInputCols(["sentence", "token", "word_embeddings"]) 	  .setOutputCol("ner")

ner_converter = NerConverterInternal()	  .setInputCols(["sentence", "token", "ner"])	  .setOutputCol("ner_chunk")	  .setWhiteList(["Procedure", "Test"])

c2doc = Chunk2Doc()	  .setInputCols("ner_chunk")	  .setOutputCol("ner_chunk_doc")

biolord_embedding = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")    .setInputCols(["ner_chunk_doc"])    .setOutputCol("embeddings")    .setCaseSensitive(False)

cpt_resolver = SentenceEntityResolverModel.load("biolordresolve_cpt_procedures_measurements_augmented")	  .setInputCols(["embeddings"]) 	  .setOutputCol("cpt_code")	  .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(
    stages = [
	              document_assembler,
	              sentenceDetectorDL,
	              tokenizer,
	              word_embeddings,
	              ner,
	              ner_converter,
	              c2doc,
	              biolord_embedding,
	              cpt_resolver])

data = spark.createDataFrame([["""She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node.
We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. At this time, chest tube placement and thoracoscopy, which were performed, which revealed epithelioid malignant mesothelioma."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)

```
```scala

val document_assembler =  new DocumentAssembler()
	  .setInputCol("text")
	  .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
	  .setInputCols(["document"])
	  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
	  .setInputCols(["sentence"])
	  .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
	  .setInputCols(Array("sentence", "token"))
	  .setOutputCol("word_embeddings")

val ner = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
	  .setInputCols(Array("sentence", "token", "word_embeddings"))
	  .setOutputCol("ner")

val ner_converter = new NerConverterInternal()	  .setInputCols(Array("sentence", "token", "ner"))	  .setOutputCol("ner_chunk")	  .setWhiteList(["Procedure", "Test"])

val c2doc = new Chunk2Doc()	  .setInputCols("ner_chunk")	  .setOutputCol("ner_chunk_doc")

val biolord_embedding = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")    .setInputCols(["ner_chunk_doc"])    .setOutputCol("embeddings")    .setCaseSensitive(False)

val cpt_resolver = SentenceEntityResolverModel.load("biolordresolve_cpt_procedures_measurements_augmented")	  .setInputCols(["embeddings"]) 	  .setOutputCol("cpt_code")	  .setDistanceFunction("EUCLIDEAN")

val resolver_pipeline = new Pipeline(
    stages = [
	              document_assembler,
	              sentenceDetectorDL,
	              tokenizer,
	              word_embeddings,
	              ner,
	              ner_converter,
	              c2doc,
	              biolord_embedding,
	              cpt_resolver])


val data = Seq([["""She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node.
We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. At this time, chest tube placement and thoracoscopy, which were performed, which revealed epithelioid malignant mesothelioma."""]]).toDF("text")

val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+--------------------+---------+--------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|           ner_chunk|   entity|cpt_code|                                                                      resolution|                                                                   all_k_results|                                                                 all_k_distances|                                                          all_k_cosine_distances|                                                              all_k_resolutions |
+--------------------+---------+--------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|CT scan of the chest|     Test|   71250|Diagnostic CT scan of chest [Computed tomography, thorax, diagnostic; without...|                   71250:::71270:::71260:::71275:::0174T:::72129:::78814:::78830|           0.5737:::0.6434:::0.6743:::0.7879:::0.8238:::0.8343:::0.8359:::0.8409|           0.1645:::0.2070:::0.2273:::0.3104:::0.3393:::0.3481:::0.3493:::0.3535|Diagnostic CT scan of chest [Computed tomography, thorax, diagnostic; without...|
|      pericardectomy|Procedure|   33030|Excision of pericardium [Pericardiectomy, subtotal or complete; without cardi...|       33030:::32659:::1006065:::33031:::32660:::33050:::32661:::1006058:::33020|  0.6004:::0.7039:::0.7178:::0.7396:::0.7462:::0.7514:::0.7839:::0.8003:::0.8154|  0.1802:::0.2477:::0.2576:::0.2735:::0.2784:::0.2823:::0.3072:::0.3203:::0.3324|Excision of pericardium [Pericardiectomy, subtotal or complete; without cardi...|
|chest tube placement|Procedure|   39503|Insertion of chest tube [Repair, neonatal diaphragmatic hernia, with or witho...|39503:::32002:::96440:::38794:::41145:::32553:::32020:::32551:::32557:::32556...|0.5587:::0.6656:::0.6703:::0.7365:::0.7641:::0.7651:::0.7672:::0.7708:::0.779...|0.1561:::0.2215:::0.2247:::0.2712:::0.2919:::0.2927:::0.2943:::0.2971:::0.303...|Insertion of chest tube [Repair, neonatal diaphragmatic hernia, with or witho...|
|        thoracoscopy|Procedure|   32601|Diagnostic thoracoscopy of mediastinal space [Thoracoscopy, diagnostic (separ...|32601:::32609:::1006006:::32668:::32654:::32605:::32651:::1020900:::32606:::3...|0.6078:::0.6117:::0.6249:::0.6292:::0.6309:::0.6537:::0.6544:::0.6903:::0.692...|0.1847:::0.1871:::0.1953:::0.1980:::0.1990:::0.2137:::0.2141:::0.2383:::0.239...|Diagnostic thoracoscopy of mediastinal space [Thoracoscopy, diagnostic (separ...|
+--------------------+---------+--------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_cpt_procedures_measurements_augmented|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[cpt_code]|
|Language:|en|
|Size:|362.6 MB|
|Case sensitive:|false|