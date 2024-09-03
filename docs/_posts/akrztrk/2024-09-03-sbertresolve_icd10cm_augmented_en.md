---
layout: model
title: Sentence Entity Resolver for ICD-10-CM Codes (sbertresolve_icd10cm_augmented)
author: John Snow Labs
name: sbertresolve_icd10cm_augmented
date: 2024-09-03
tags: [licensed, en, icd10cm, entity_resolution, clinical]
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

This model maps clinical entities and concepts to ICD-10-CM codes using `sbert_jsl_medium_uncased` sentence bert embeddings. It also returns the official resolution text within the brackets inside the metadata. 
The model is augmented with synonyms, and previous augmentations are flexed according to cosine distances to unnormalized terms (ground truths).

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_augmented_en_5.4.0_3.0_1725380751641.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_augmented_en_5.4.0_3.0_1725380751641.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = BertSentenceEmbeddings.pretrained("sbert_jsl_medium_uncased", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bert_embeddings")\
    .setCaseSensitive(False)

icd_resolver = SentenceEntityResolverModel.pretrained("sbertresolve_icd10cm_augmented", "en", "clinical/models")\
    .setInputCols(["bert_embeddings"])\
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

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, three years prior to presentation, associated with acute hepatitis, and obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting."""]]).toDF("text")

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

val embeddings = BertSentenceEmbeddings.pretrained("sbert_jsl_medium_uncased", "en", "clinical/models")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("bert_embeddings")
    .setCaseSensitive(False)

val icd_resolver = SentenceEntityResolverModel.pretrained("sbertresolve_icd10cm_augmented", "en", "clinical/models")
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

val data = Seq([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, three years prior to presentation, associated with acute hepatitis, and obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting."""]]).toDF("text")

val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-------------------------------------+-----+---+---------+----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                                chunk|begin|end|ner_label|icd10_code|                                                 description|                                                 resolutions|                                                   all_codes|
+-------------------------------------+-----+---+---------+----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|        gestational diabetes mellitus|   39| 67|  PROBLEM|     O24.4|gestational diabetes mellitus [gestational diabetes melli...|gestational diabetes mellitus [gestational diabetes melli...|O24.4:::O24.41:::O24.43:::Z86.32:::P70.2:::O24.434:::E10....|
|subsequent type two diabetes mellitus|  117|153|  PROBLEM|       E11|         type 2 diabetes mellitus [type 2 diabetes mellitus]|type 2 diabetes mellitus [type 2 diabetes mellitus]:::typ...|E11:::E11.9:::E10.9:::E10:::E13.9:::Z83.3:::L83:::E11.8::...|
|                      acute hepatitis|  207|221|  PROBLEM|     K72.0|        acute hepatitis [acute and subacute hepatic failure]|acute hepatitis [acute and subacute hepatic failure]:::ac...|K72.0:::B15:::B17.2:::B17.1:::B16:::B17.9:::B18.8:::B15.9...|
|                              obesity|  228|234|  PROBLEM|     E66.9|                              obesity [obesity, unspecified]|obesity [obesity, unspecified]:::upper body obesity [othe...|E66.9:::E66.8:::P90:::Q13.0:::M79.4:::E66.812:::E66.811::...|
|                    a body mass index|  241|257|  PROBLEM|     E66.9|       observation of body mass index [obesity, unspecified]|observation of body mass index [obesity, unspecified]:::f...|E66.9:::Z68.41:::Z68:::E66.8:::Z68.45:::Z68.56:::Z68.4:::...|
|                             polyuria|  317|324|  PROBLEM|       R35|                                         polyuria [polyuria]|polyuria [polyuria]:::stranguria [dysuria]:::isosthenuria...|R35:::R30.0:::N28.89:::O04.8:::R82.4:::R82.2:::E73.9:::R8...|
|                           polydipsia|  327|336|  PROBLEM|     R63.1|                                     polydipsia [polydipsia]|polydipsia [polydipsia]:::polyotia [accessory auricle]:::...|R63.1:::Q17.0:::Q89.4:::Q89.09:::Q74.8:::H53.8:::H53.2:::...|
|                        poor appetite|  339|351|  PROBLEM|     R63.0|                                    poor appetite [anorexia]|poor appetite [anorexia]:::excessive appetite [polyphagia...|R63.0:::R63.2:::P92.9:::R45.81:::Z55.8:::R41.84:::R41.3::...|
|                             vomiting|  358|365|  PROBLEM|     R11.1|                                         vomiting [vomiting]|vomiting [vomiting]:::vomiting bile [vomiting following g...|R11.1:::K91.0:::K92.0:::A08.39:::R11:::P92.0:::P92.09:::R...|
+-------------------------------------+-----+---+---------+----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbertresolve_icd10cm_augmented|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|884.8 MB|
|Case sensitive:|false|
