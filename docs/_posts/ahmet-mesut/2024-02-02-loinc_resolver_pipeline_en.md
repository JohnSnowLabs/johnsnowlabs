---
layout: model
title: Pipeline for Logical Observation Identifiers Names and Codes (LOINC)
author: John Snow Labs
name: loinc_resolver_pipeline
date: 2024-02-02
tags: [licensed, en, loinc, pipeline, resolver]
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

This pipeline extracts `Test` entities from clinical texts and maps them to their corresponding Logical Observation Identifiers Names and Codes (LOINC) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/loinc_resolver_pipeline_en_5.2.1_3.2_1706884816860.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/loinc_resolver_pipeline_en_5.2.1_3.2_1706884816860.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("loinc_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""A 65-year-old woman presents to the office with generalized fatigue for the last 4 months.
  She used to walk 1 mile each evening but now gets tired after 1-2 blocks. She has a history of Crohn disease and hypertension
  for which she receives appropriate medications. She is married and lives with her husband. She eats a balanced diet that
  includes chicken, fish, pork, fruits, and vegetables. She rarely drinks alcohol and denies tobacco use. Her vital signs are
  within normal limits. A physical examination is unremarkable. Laboratory studies show the following: Hemoglobin: 9.8 g/dL, Hematocrit: 32%, Mean Corpuscular Volume: 110 μm3""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("loinc_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""A 65-year-old woman presents to the office with generalized fatigue for the last 4 months.
  She used to walk 1 mile each evening but now gets tired after 1-2 blocks. She has a history of Crohn disease and hypertension
  for which she receives appropriate medications. She is married and lives with her husband. She eats a balanced diet that
  includes chicken, fish, pork, fruits, and vegetables. She rarely drinks alcohol and denies tobacco use. Her vital signs are
  within normal limits. A physical examination is unremarkable. Laboratory studies show the following: Hemoglobin: 9.8 g/dL, Hematocrit: 32%, Mean Corpuscular Volume: 110 μm3""")

```
</div>

## Results

```bash

+-----------------------+-----+----------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|                  chunk|label|loinc_code|                                                            resolution|                                                             all_codes|                                                       all_resolutions|
+-----------------------+-----+----------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|            Vital signs| Test|    8716-3|                                             Vital signs [Vital signs]|8716-3:::67801-1:::80339-5:::34566-0:::29274-8:::95634-2:::31210-8:...|Vital signs [Vital signs]:::EMS vital signs [EMS vital signs]:::Vit...|
| A physical examination| Test|  LP7801-6|                                         Physical exam [Physical exam]|LP7801-6:::55286-9:::11384-5:::67668-4:::100223-7:::29545-1:::79897...|Physical exam [Physical exam]:::Physical examination by body areas ...|
|     Laboratory studies| Test|   26436-6|                               Laboratory studies [Laboratory studies]|26436-6:::LP36394-2:::52482-7:::ATTACH.LAB:::11502-2:::LA7451-3:::3...|Laboratory studies [Laboratory studies]:::Laboratory device [Labora...|
|             Hemoglobin| Test|   14775-1|                                               Hemoglobin [Hemoglobin]|14775-1:::LP30929-1:::34663-5:::18277-4:::10346-5:::LP30932-5:::532...|Hemoglobin [Hemoglobin]:::Hemoglobin G [Hemoglobin G]:::Hemoglobin ...|
|             Hematocrit| Test|   11151-8|                                               Hematocrit [Hematocrit]|11151-8:::16931-8:::32354-3:::20570-8:::11153-4:::39227-4:::42908-4...|Hematocrit [Hematocrit]:::Hematocrit/Hemoglobin [Hematocrit/Hemoglo...|
|Mean Corpuscular Volume| Test|   11272-2|Erythrocyte mean corpuscular volume [Erythrocyte mean corpuscular v...|11272-2:::30386-7:::48706-6:::30899-9:::51641-9:::33878-0:::LP15006...|Erythrocyte mean corpuscular volume [Erythrocyte mean corpuscular v...|
+-----------------------+-----+----------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|loinc_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.0 GB|

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