---
layout: model
title: Pipeline for ICD-10-PCS
author: John Snow Labs
name: icd10pcs_resolver_pipeline
date: 2024-02-02
tags: [licensed, en, icd10pcs, pipeline, resolver, procedure]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts `Procedure` entities from clinical texts and map them to their corresponding ICD-10-PCS codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10pcs_resolver_pipeline_en_5.2.1_3.2_1706889288566.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10pcs_resolver_pipeline_en_5.2.1_3.2_1706889288566.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("icd10pcs_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""[['Given the severity of her abdominal examination and her persistence of her symptoms,\n            it is detected that need for laparoscopic appendectomy and possible jejunectomy\n            as well as pyeloplasty. We recommend performing a mediastinoscopy']]""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("icd10pcs_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""[['Given the severity of her abdominal examination and her persistence of her symptoms,\n            it is detected that need for laparoscopic appendectomy and possible jejunectomy\n            as well as pyeloplasty. We recommend performing a mediastinoscopy']]""")

```
</div>

## Results

```bash

+-------------------------+---------+-------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|                    chunk|    label|icd10pcs_code|                                                            resolution|                                                             all_codes|                                                       all_resolutions|
+-------------------------+---------+-------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|laparoscopic appendectomy|Procedure|      0DTJ8ZZ|             resection of appendix, endo [resection of appendix, endo]|0DTJ8ZZ:::0DT84ZZ:::0DTJ4ZZ:::0WBH4ZZ:::0DTR4ZZ:::0DBJ8ZZ:::0DTG4ZZ...|resection of appendix, endo [resection of appendix, endo]:::resecti...|
|              jejunectomy|Procedure|      0DBA8ZZ|                 excision of jejunum, endo [excision of jejunum, endo]|0DBA8ZZ:::0DTA8ZZ:::0D5A8ZZ:::0DLA8ZZ:::0DBA8ZX:::0DT88ZZ:::0DCA8ZZ...|excision of jejunum, endo [excision of jejunum, endo]:::resection o...|
|              pyeloplasty|Procedure|      0TS84ZZ|reposition bilateral ureters, perc endo approach [reposition bilate...|0TS84ZZ:::0TS74ZZ:::069B3ZZ:::06SB3ZZ:::0TR74JZ:::0TQ43ZZ:::049A3ZZ...|reposition bilateral ureters, perc endo approach [reposition bilate...|
|          mediastinoscopy|Procedure|      BB1CZZZ|               fluoroscopy of mediastinum [fluoroscopy of mediastinum]|BB1CZZZ:::0WJC4ZZ:::BB4CZZZ:::0WJC3ZZ:::0WHC33Z:::0WHC43Z:::0WHC3YZ...|fluoroscopy of mediastinum [fluoroscopy of mediastinum]:::inspectio...|
+-------------------------+---------+-------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10pcs_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel