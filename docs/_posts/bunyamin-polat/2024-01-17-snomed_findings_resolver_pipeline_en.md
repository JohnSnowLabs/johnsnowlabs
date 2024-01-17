---
layout: model
title: Pipeline for Snomed Concept, Findings Version
author: John Snow Labs
name: snomed_findings_resolver_pipeline
date: 2024-01-17
tags: [licensed, en, snomed, pipeline, resolver]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts clinical findings and maps them to their corresponding SNOMED (CT version) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_findings_resolver_pipeline_en_5.2.1_3.0_1705496251793.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_findings_resolver_pipeline_en_5.2.1_3.0_1705496251793.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("snomed_findings_resolver_pipeline", "en", "clinical/models")

text = """The patient exhibited recurrent upper respiratory tract infections, subjective fevers, unintentional weight loss, and occasional night sweats. Clinically, they appeared cachectic and pale, with notable hepatosplenomegaly and swollen joints. Laboratory results confirmed pancytopenia."""

result = snomed_pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("snomed_findings_resolver_pipeline", "en", "clinical/models")

val text = """The patient exhibited recurrent upper respiratory tract infections, subjective fevers, unintentional weight loss, and occasional night sweats. Clinically, they appeared cachectic and pale, with notable hepatosplenomegaly and swollen joints. Laboratory results confirmed pancytopenia."""

val result = snomed_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

+--------------------------------------------+-----+---+---------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                                      chunks|begin|end|     code|                                         all_codes|                                       resolutions|                                     all_distances|
+--------------------------------------------+-----+---+---------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|recurrent upper respiratory tract infections|   22| 65|195708003|[195708003, 308130008, 195746005, 54150009, 783...|[recurrent upper respiratory tract infection, r...|[0.0073, 0.0664, 0.0664, 0.0694, 0.0712, 0.0737...|
|                           subjective fevers|   68| 84|103001002|[103001002, 248425001, 186694006, 77957000, 271...|[feeling feverish (finding), feels feverish, sw...|[0.0494, 0.0514, 0.0535, 0.0552, 0.0661, 0.0674...|
|                   unintentional weight loss|   87|111|448765001|[448765001, 422868009, 699205002, 416528001, 16...|[unintentional weight loss, unexplained weight ...|[0.0000, 0.0400, 0.0472, 0.0564, 0.0666, 0.0666...|
|                     occasional night sweats|  118|140|161859009|[161859009, 42984000, 139115006, 423052008, 672...|[night sweats, night sweats, night sweats, freq...|[0.0480, 0.0480, 0.0480, 0.1043, 0.1100, 0.1256...|
|                                   cachectic|  169|177|238108007|[238108007, 28928000, 74633007, 422003001, 2845...|[cachectic, cachexia, aids with cachexia, cache...|[0.0000, 0.0619, 0.0651, 0.0965, 0.0961, 0.0986...|
|                                        pale|  183|186|274643008|[274643008, 139121005, 161865009, 398979000, 16...|[pale, pale color, pale color, pale complexion,...|[0.0000, 0.0733, 0.0733, 0.0812, 0.0812, 0.0892...|
|                  notable hepatosplenomegaly|  194|219| 36760000|[36760000, 19058002, 80378000, 16294009, 469330...|[hepatosplenomegaly, congestive splenomegaly, n...|[0.0225, 0.0835, 0.0857, 0.0875, 0.0928, 0.0959...|
|                                pancytopenia|  251|262|127034005|[127034005, 736024007, 191249008, 5876000, 1249...|[pancytopenia, drug induced pancytopenia, pancy...|[0.0000, 0.0407, 0.0425, 0.0425, 0.0493, 0.0495...|
+--------------------------------------------+-----+---+---------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_findings_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.6 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
