---
layout: model
title: Sentence Entity Resolver for ICD-10-CM (general 3 character codes - augmented)
author: John Snow Labs
name: sbiobertresolve_icd10cm_generalised_augmented
date: 2024-09-05
tags: [licensed, en, entity_resolution, icd10cm, clinical]
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

This model maps extracted medical entities to ICD-10-CM codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. It predicts ICD-10-CM codes up to 3 characters (according to ICD-10-CM code structure the first three characters represent general type of the injury or disease).

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_generalised_augmented_en_5.4.0_3.0_1725534260823.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_generalised_augmented_en_5.4.0_3.0_1725534260823.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models") \
	.setInputCols(["sentence", "token", "embeddings"]) \
	.setOutputCol("ner")

ner_converter = NerConverterInternal() \
 	  .setInputCols(["sentence", "token", "ner"]) \
	  .setOutputCol("ner_chunk")	  .setWhiteList(["PROBLEM"])

chunk2doc = Chunk2Doc()\
  	.setInputCols("ner_chunk")\
  	.setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
	  .setInputCols(["ner_chunk_doc"])\
	  .setOutputCol("sbert_embeddings")\
	  .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_generalised_augmented","en", "clinical/models") \
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

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""]]).toDF("text")

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

val ner_model = MedicalNerModel.pretrained("ner_clinical","en","clinical/models")
  .setInputCols(Array("sentence","token","embeddings"))
  .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
  .setInputCols(Array("sentence","token","ner"))
  .setOutputCol("ner_chunk")
  .setWhiteList(Array("PROBLEM"))

val chunk2doc = new Chunk2Doc()
  .setInputCols("ner_chunk")
  .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sbert_embeddings")
  .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_generalised_augmented","en","clinical/models")
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

val data = Seq([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""]]).toDF("text")

val result = nlpPipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-------------------------------------+-----+---+---------+------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                                chunk|begin|end|ner_label|icd10cm_code|                                                 description|                                                 resolutions|                                                   all_codes|
+-------------------------------------+-----+---+---------+------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|        gestational diabetes mellitus|   39| 67|  PROBLEM|         O24|gestational diabetes mellitus [gestational diabetes melli...|gestational diabetes mellitus [gestational diabetes melli...|                                             O24:::Z86:::Z87|
|subsequent type two diabetes mellitus|  117|153|  PROBLEM|         O24|pre-existing type 2 diabetes mellitus [pre-existing type ...|pre-existing type 2 diabetes mellitus [pre-existing type ...|                                       O24:::E11:::E13:::Z86|
|                              obesity|  172|178|  PROBLEM|         E66|                              obesity [obesity, unspecified]|obesity [obesity, unspecified]:::obese [body mass index [...|               E66:::Z68:::Q13:::Z86:::E34:::H35:::Z83:::Q55|
|                    a body mass index|  185|201|  PROBLEM|         Z68|finding of body mass index [body mass index [bmi] 40.0-44...|finding of body mass index [body mass index [bmi] 40.0-44...|         Z68:::E66:::R22:::R41:::M62:::P29:::R19:::R89:::M21|
|                             polyuria|  261|268|  PROBLEM|         R35|                                         polyuria [polyuria]|polyuria [polyuria]:::polyuric state (disorder) [diabetes...|R35:::E23:::R31:::N40:::E72:::O04:::R30:::R80:::N03:::P96...|
|                           polydipsia|  271|280|  PROBLEM|         R63|                                     polydipsia [polydipsia]|polydipsia [polydipsia]:::psychogenic polydipsia [other i...|R63:::F63:::E23:::O40:::G47:::M79:::R06:::H53:::I44:::Q30...|
|                        poor appetite|  283|295|  PROBLEM|         R63|                                    poor appetite [anorexia]|poor appetite [anorexia]:::poor feeding [feeding problem ...|R63:::P92:::R43:::E86:::R19:::F52:::Z72:::R06:::Z76:::R53...|
|                             vomiting|  302|309|  PROBLEM|         R11|                                         vomiting [vomiting]|vomiting [vomiting]:::periodic vomiting [cyclical vomitin...|                                             R11:::G43:::P92|
|        a respiratory tract infection|  403|431|  PROBLEM|         J98|respiratory tract infection [other specified respiratory ...|respiratory tract infection [other specified respiratory ...|J98:::J06:::A49:::J22:::J20:::Z59:::T17:::J04:::Z13:::J18...|
+-------------------------------------+-----+---+---------+------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd10cm_generalised_augmented|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|1.3 GB|
|Case sensitive:|false|