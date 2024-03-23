---
layout: model
title: Pipeline for Snomed Concept, Findings Version
author: John Snow Labs
name: snomed_findings_resolver_pipeline
date: 2024-03-03
tags: [licensed, en, snomed, pipeline, resolver]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.4
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_findings_resolver_pipeline_en_5.3.0_3.4_1709489839090.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_findings_resolver_pipeline_en_5.3.0_3.4_1709489839090.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("snomed_findings_resolver_pipeline", "en", "clinical/models")

result = snomed_pipeline.annotate("""The patient exhibited recurrent upper respiratory tract infections, fever, unintentional weight loss, and occasional night sweats. Clinically, they appeared cachectic and pale, with notable hepatosplenomegaly. Laboratory results confirmed pancytopenia.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("snomed_findings_resolver_pipeline", "en", "clinical/models")

val result = snomed_pipeline.annotate("""The patient exhibited recurrent upper respiratory tract infections, fever, unintentional weight loss, and occasional night sweats. Clinically, they appeared cachectic and pale, with notable hepatosplenomegaly. Laboratory results confirmed pancytopenia.""")

```
</div>

## Results

```bash

+----------------------------------+-----+---+---------+-----------+-------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                             chunk|begin|end|ner_label|snomed_code|                                 resolution|                                           all_k_resolutions|                                                 all_k_codes|
+----------------------------------+-----+---+---------+-----------+-------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|upper respiratory tract infections|   32| 65|  PROBLEM|  195708003|recurrent upper respiratory tract infection|recurrent upper respiratory tract infection:::upper respi...|195708003:::54150009:::312118003:::448739000:::4519910001...|
|                             fever|   68| 72|  PROBLEM|  386661006|                                      fever|fever:::intermittent fever:::sustained fever:::prolonged ...|386661006:::77957000:::271751000:::248435007:::12579009::...|
|         unintentional weight loss|   75| 99|  PROBLEM|  448765001|                  unintentional weight loss|unintentional weight loss:::unexplained weight loss:::int...|448765001:::422868009:::416528001:::267024001:::89362005:...|
|                      night sweats|  117|128|  PROBLEM|   42984000|                               night sweats|night sweats:::frequent night waking:::night waking:::nig...|42984000:::423052008:::67233009:::102549009:::36163009:::...|
|                         cachectic|  157|165|  PROBLEM|  238108007|                                  cachectic|cachectic:::cachexia associated with aids:::cardiac cache...|238108007:::422003001:::284529003:::788876001:::240128005...|
|                              pale|  171|174|  PROBLEM|  398979000|                            pale complexion|pale complexion:::pale liver:::pale tongue:::pale lung:::...|398979000:::95199009:::719637000:::95200007:::70396004:::...|
|                hepatosplenomegaly|  190|207|  PROBLEM|   36760000|                         hepatosplenomegaly|hepatosplenomegaly:::congestive splenomegaly:::neonatal h...|36760000:::19058002:::80378000:::16294009:::191382009:::8...|
|                      pancytopenia|  239|250|  PROBLEM|  127034005|                               pancytopenia|pancytopenia:::drug induced pancytopenia:::pancytopenia -...|127034005:::736024007:::5876000:::124961001:::417672002::...|
+----------------------------------+-----+---+---------+-----------+-------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_findings_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
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
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
