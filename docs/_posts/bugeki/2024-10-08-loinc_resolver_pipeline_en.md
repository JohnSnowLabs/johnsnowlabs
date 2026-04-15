---
layout: model
title: Pipeline for Logical Observation Identifiers Names and Codes (LOINC)
author: John Snow Labs
name: loinc_resolver_pipeline
date: 2024-10-08
tags: [licensed, en, loinc, pipeline, resolver]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"

deploy:
  sagemaker_link: https://aws.amazon.com/marketplace/pp/prodview-idfcekbznwtlq
  snowflake_link: https://app.snowflake.com/marketplace/listing/GZTYZ4386LJDV/john-snow-labs-loinc-sentence-entity-resolver
  databricks_link: 

---

## Description

This pipeline extracts `Test` entities from clinical texts and maps them to their corresponding Logical Observation Identifiers Names and Codes (LOINC) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

## Predicted Entities

`loinc_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/loinc_resolver_pipeline_en_5.5.0_3.4_1728411236477.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/loinc_resolver_pipeline_en_5.5.0_3.4_1728411236477.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

{% if page.deploy %}
## Available as Private API Endpoint

{:.tac}
{% include display_platform_information.html %}
{% endif %}

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
  within normal limits. A physical examination is unremarkable. Laboratory studies show the following: Hemoglobin: 9.8 g/dL, 
  Hematocrit: 32%, Mean Corpuscular Volume: 110 μm3""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("loinc_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""A 65-year-old woman presents to the office with generalized fatigue for the last 4 months.
  She used to walk 1 mile each evening but now gets tired after 1-2 blocks. She has a history of Crohn disease and hypertension
  for which she receives appropriate medications. She is married and lives with her husband. She eats a balanced diet that
  includes chicken, fish, pork, fruits, and vegetables. She rarely drinks alcohol and denies tobacco use. Her vital signs are
  within normal limits. A physical examination is unremarkable. Laboratory studies show the following: Hemoglobin: 9.8 g/dL, 
  Hematocrit: 32%, Mean Corpuscular Volume: 110 μm3""")

```
</div>

## Results

```bash

+-----------------------+-----+----------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|                  chunk|label|loinc_code|                                                            resolution|                                                             all_codes|                                                       all_resolutions|
+-----------------------+-----+----------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|            Vital signs| Test|    8716-3|                                             Vital signs [Vital signs]|8716-3:::LP133943-3:::LP204118-6:::80339-5:::34566-0:::29274-8:::95...|Vital signs [Vital signs]:::EMS vital signs [EMS vital signs]:::Vit...|
| A physical examination| Test|  LP7801-6|                                         Physical exam [Physical exam]|LP7801-6:::LP269267-3:::LP94385-9:::55286-9:::11384-5:::LP133607-4:...|Physical exam [Physical exam]:::Estimated from physical examination...|
|     Laboratory studies| Test| LP74124-6|                               Laboratory studies [Laboratory studies]|LP74124-6:::26436-6:::LP36394-2:::52482-7:::ATTACH.LAB:::11502-2:::...|Laboratory studies [Laboratory studies]:::Laboratory studies (set) ...|
|             Hemoglobin| Test| LP14449-0|                                               Hemoglobin [Hemoglobin]|LP14449-0:::LP30929-1:::LP16455-5:::10346-5:::LP16428-2:::LP14554-7...|Hemoglobin [Hemoglobin]:::Hemoglobin G [Hemoglobin G]:::Hemoglobin ...|
|             Hematocrit| Test| LP15101-6|                                               Hematocrit [Hematocrit]|LP15101-6:::LP308151-2:::32354-3:::20570-8:::11153-4:::LP74090-9:::...|Hematocrit [Hematocrit]:::Hematocrit/Hemoglobin [Hematocrit/Hemoglo...|
|Mean Corpuscular Volume| Test| LP15191-7|Erythrocyte mean corpuscular volume [Erythrocyte mean corpuscular v...|LP15191-7:::LP17688-0:::LP62885-6:::LP29006-1:::LP66395-2:::LP41110...|Erythrocyte mean corpuscular volume [Erythrocyte mean corpuscular v...|
+-----------------------+-----+----------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|loinc_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.2 GB|

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
