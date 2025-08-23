---
layout: model
title: Pipeline for Logical Observation Identifiers Names and Codes (LOINC-Numeric)
author: John Snow Labs
name: loinc_numeric_resolver_pipeline
date: 2024-10-08
tags: [licensed, en, clinical, loinc, pipeline, resolver]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts `TEST` entities and maps them to their correspondings Logical Observation Identifiers Names and Codes(LOINC) codes using `sbiobert_base_cased_mli` sentence embeddings. It was prepared with the numeric LOINC codes, without the inclusion of LOINC “Document Ontology” codes starting with the letter “L”. It also provides the official resolution of the codes within the brackets.

## Predicted Entities

`TEST`, `Test_Result`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/loinc_numeric_resolver_pipeline_en_5.5.0_3.0_1728417134407.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/loinc_numeric_resolver_pipeline_en_5.5.0_3.0_1728417134407.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

loinc_pipeline = PretrainedPipeline("loinc_numeric_resolver_pipeline", "en", "clinical/models")

text = """A 65-year-old woman presents to the office with generalized fatigue for the last 4 months. She used to walk 1 mile each evening but now gets tired after 1-2 blocks. She has a history of Crohn disease and hypertension for which she receives appropriate medications. She is married and lives with her husband. She eats a balanced diet that includes chicken, fish, pork, fruits, and vegetables. She rarely drinks alcohol and denies tobacco use.  A physical examination is unremarkable. Laboratory studies show the following:
Hemoglobin: 9.8 g/dL
Hematocrit: 32%
Mean Corpuscular Volume: 110 μm3"""

result = loinc_pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val loinc_pipeline = PretrainedPipeline("loinc_numeric_resolver_pipeline", "en", "clinical/models")

val text = """A 65-year-old woman presents to the office with generalized fatigue for the last 4 months. She used to walk 1 mile each evening but now gets tired after 1-2 blocks. She has a history of Crohn disease and hypertension for which she receives appropriate medications. She is married and lives with her husband. She eats a balanced diet that includes chicken, fish, pork, fruits, and vegetables. She rarely drinks alcohol and denies tobacco use.  A physical examination is unremarkable. Laboratory studies show the following:
Hemoglobin: 9.8 g/dL
Hematocrit: 32%
Mean Corpuscular Volume: 110 μm3"""

val result = loinc_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

+-----------------------+-----+---+-------+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+
|                 chunks|begin|end|   code|                                                        all_codes|                                                      resolutions|                                                    all_distances|
+-----------------------+-----+---+-------+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+
| A physical examination|  443|464|55286-9|[55286-9, 11384-5, 29544-4, 29545-1, 32427-7, 11435-5, 29271-4...|[Physical exam by body areas [Physical exam by body areas], Ph...|[0.0713, 0.0913, 0.0910, 0.0961, 0.1114, 0.1119, 0.1153, 0.112...|
|     Laboratory studies|  483|500|26436-6|[26436-6, 52482-7, 11502-2, 34075-2, 100455-5, 85069-3, 101129...|[Laboratory studies (set) [Laboratory studies (set)], Laborato...|[0.0469, 0.0648, 0.0748, 0.0947, 0.0967, 0.1285, 0.1257, 0.129...|
|             Hemoglobin|  522|531|10346-5|[10346-5, 15082-1, 11559-2, 2030-5, 34618-9, 38896-7, 717-9, 1...|[Haemoglobin [Hemoglobin A [Units/volume] in Blood by Electrop...|[0.0214, 0.0356, 0.0563, 0.0654, 0.0886, 0.0891, 0.1005, 0.105...|
|             Hematocrit|  543|552|32354-3|[32354-3, 20570-8, 11153-4, 13508-7, 104874-3, 42908-4, 11559-...|[Hematocrit [Volume Fraction] of Arterial blood [Hematocrit [V...|[0.0590, 0.0625, 0.0675, 0.0737, 0.0890, 0.1035, 0.1060, 0.107...|
|Mean Corpuscular Volume|  559|581|30386-7|[30386-7, 101864-7, 20161-6, 18033-1, 19853-1, 101150-1, 59117...|[Erythrocyte mean corpuscular diameter [Length] [Erythrocyte m...|[0.1344, 0.1333, 0.1350, 0.1359, 0.1353, 0.1427, 0.1523, 0.147...|
+-----------------------+-----+---+-------+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|loinc_numeric_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.0+|
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
