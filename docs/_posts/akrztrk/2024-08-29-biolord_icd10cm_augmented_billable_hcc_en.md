---
layout: model
title: Sentence Entity Resolver for Billable ICD10-CM HCC Codes
author: John Snow Labs
name: biolord_icd10cm_augmented_billable_hcc
date: 2024-08-29
tags: [licensed, en, biolord, icd10cm, entity_resolution, hcc, clinical]
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

This model maps extracted medical entities to ICD-10-CM codes using `mpnet_embeddings_biolord_2023_c`
MPNet Embeddings and it supports 7-digit codes with Hierarchical Condition Categories (HCC) status.
It has been updated by dropping the invalid codes that exist in the previous versions. In the result,
look for the `all_k_aux_labels` parameter in the metadata to get HCC status. The HCC status can be divided to get further
information: `billable status`, `hcc status`, and `hcc score`.
For example if the result is `1||1||8`: `the billable status is 1`, `hcc status is 1`, and `hcc score is 8`.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolord_icd10cm_augmented_billable_hcc_en_5.4.0_3.0_1724927811385.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolord_icd10cm_augmented_billable_hcc_en_5.4.0_3.0_1724927811385.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings =MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("mpnet_embeddings")

icd_resolver = SentenceEntityResolverModel.pretrained("biolord_icd10cm_augmented_billable_hcc", "en", "clinical/models")\
    .setInputCols(["mpnet_embeddings"])\
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

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation, and subsequent type 2 diabetes mellitus associated with obesity (BMI of 33.5 kg/m2), presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""]]).toDF("text")

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

val embeddings =MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("mpnet_embeddings")

val icd_resolver = SentenceEntityResolverModel.pretrained("biolord_icd10cm_augmented_billable_hcc", "en", "clinical/models")
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

val data = Seq([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation, and subsequent type 2 diabetes mellitus associated with obesity (BMI of 33.5 kg/m2), presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""]]).toDF("text")

val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------------------------------+-----+---+---------+----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                              chunk|begin|end|ner_label|icd10_code|                                                 description|                                                 resolutions|                                                   all_codes|                                                    hcc_list|
+-----------------------------------+-----+---+---------+----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|      gestational diabetes mellitus|   39| 67|  PROBLEM|     O24.4|gestational diabetes mellitus [gestational diabetes melli...|gestational diabetes mellitus [gestational diabetes melli...|O24.4:::O24.41:::O24.9:::Z86.32:::O24.0:::O24.42:::O24.43...|0||0||0:::0||0||0:::0||0||0:::1||0||0:::0||0||0:::0||0||0...|
|subsequent type 2 diabetes mellitus|  118|152|  PROBLEM|     E11.8|complication of type ii diabetes mellitus [type 2 diabete...|complication of type ii diabetes mellitus [type 2 diabete...|E11.8:::Z86.39:::E11.9:::E11.69:::E11.65:::E11.6:::E11.2:...|1||1||18:::1||0||0:::1||1||19:::1||1||18:::1||1||18:::0||...|
|                            obesity|  170|176|  PROBLEM|     E66.9|                              obesity [obesity, unspecified]|obesity [obesity, unspecified]:::overweight and obesity [...|E66.9:::E66:::E66.8:::Z68.41:::P90:::E66.01:::Q13.0:::E66...|1||0||0:::0||0||0:::1||0||0:::1||1||22:::1||0||0:::1||1||...|
|                           polyuria|  236|243|  PROBLEM|    R35.89|                             other polyuria [other polyuria]|other polyuria [other polyuria]:::polyuria [polyuria]:::m...|R35.89:::R35:::R35.0:::R35.81:::N40.1:::R80.8:::N40:::R82...|1||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0...|
|                         polydipsia|  246|255|  PROBLEM|     E23.2|                     primary polydipsia [diabetes insipidus]|primary polydipsia [diabetes insipidus]:::polydipsia [pol...|E23.2:::R63.1:::F63.89:::Z13.8:::E87.0:::F10.99:::R63.8::...|1||1||23:::1||0||0:::1||0||0:::0||0||0:::1||0||0:::1||1||...|
|                      poor appetite|  258|270|  PROBLEM|     R63.0|                                    poor appetite [anorexia]|poor appetite [anorexia]:::non-organic loss of appetite [...|R63.0:::F50.8:::P92.9:::R63.8:::Z72.4:::Z73.89:::R46.89::...|1||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0...|
|                           vomiting|  277|284|  PROBLEM|    R11.10|                   vomiting symptoms [vomiting, unspecified]|vomiting symptoms [vomiting, unspecified]:::vomiting [vom...|R11.10:::R11.1:::R11:::R11.2:::K91.0:::P92.1:::R11.0:::R1...|1||0||0:::0||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0...|
|      a respiratory tract infection|  378|406|  PROBLEM|     J98.8|rti - respiratory tract infection [other specified respir...|rti - respiratory tract infection [other specified respir...|J98.8:::B58.3:::J06.9:::B39.4:::J22:::Z59.3:::J98.51:::J1...|1||0||0:::1||1||6:::1||0||0:::1||0||0:::1||0||0:::1||0||0...|
+-----------------------------------+-----+---+---------+----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolord_icd10cm_augmented_billable_hcc|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|1.3 GB|
|Case sensitive:|false|
