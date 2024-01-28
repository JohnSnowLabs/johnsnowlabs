---
layout: model
title: Pipeline for LOINC Codes
author: John Snow Labs
name: loinc_numeric_resolver_pipeline
date: 2024-01-28
tags: [licensed, en, clinical, loinc, pipeline, resolver]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline maps extracted medical entities to Logical Observation Identifiers Names and Codes(LOINC) codes using `sbiobert_base_cased_mli` sentence embeddings. It is trained with the numeric LOINC codes, without the inclusion of LOINC “Document Ontology” codes starting with the letter “L”. It also provides the official resolution of the codes within the brackets.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/loinc_numeric_resolver_pipeline_en_5.2.1_3.4_1706452371826.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/loinc_numeric_resolver_pipeline_en_5.2.1_3.4_1706452371826.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

loinc_pipeline = PretrainedPipeline("loinc_numeric_resolver_pipeline", "en", "clinical/models")

text = """A 65-year-old woman presents to the office with generalized fatigue for the last 4 months. She used to walk 1 mile each evening but now gets tired after 1-2 blocks. She has a history of Crohn disease and hypertension for which she receives appropriate medications. She is married and lives with her husband. She eats a balanced diet that includes chicken, fish, pork, fruits, and vegetables. She rarely drinks alcohol and denies tobacco use. Her vital signs are within normal limits. A physical examination is unremarkable. Laboratory studies show the following:
Hemoglobin: 9.8 g/dL
Hematocrit: 32%
Mean Corpuscular Volume: 110 μm3"""

result = loinc_pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val loinc_pipeline = PretrainedPipeline("loinc_numeric_resolver_pipeline", "en", "clinical/models")

val text = """A 65-year-old woman presents to the office with generalized fatigue for the last 4 months. She used to walk 1 mile each evening but now gets tired after 1-2 blocks. She has a history of Crohn disease and hypertension for which she receives appropriate medications. She is married and lives with her husband. She eats a balanced diet that includes chicken, fish, pork, fruits, and vegetables. She rarely drinks alcohol and denies tobacco use. Her vital signs are within normal limits. A physical examination is unremarkable. Laboratory studies show the following:
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
|        Her vital signs|  442|456| 8716-3|[8716-3, 80339-5, 29274-8, 67801-1, 95634-2, 34566-0, 31210-8,...|[Vital signs [Vital signs], Vital signs assessment [Vital sign...|[0.1174, 0.1197, 0.1255, 0.1288, 0.1369, 0.1420, 0.1456, 0.174...|
| A physical examination|  484|505|55286-9|[55286-9, 11384-5, 67668-4, 100223-7, 29545-1, 79897-5, 32427-...|[Physical examination by body areas [Physical examination by b...|[0.0704, 0.0913, 0.0908, 0.0910, 0.0961, 0.1091, 0.1114, 0.111...|
|     Laboratory studies|  524|541|26436-6|[26436-6, 52482-7, 11502-2, 34075-2, 68989-3, 89756-1, 89763-7...|[Laboratory studies [Laboratory studies], Laboratory [Laborato...|[0.0000, 0.0648, 0.0748, 0.1057, 0.1051, 0.1096, 0.1128, 0.120...|
|             Hemoglobin|  563|572|14775-1|[14775-1, 34663-5, 18277-4, 10346-5, 53224-2, 40546-4, 4593-0,...|[Hemoglobin [Hemoglobin], Hemoglobin S [Hemoglobin S], Hemoglo...|[0.0000, 0.0199, 0.0234, 0.0242, 0.0304, 0.0338, 0.0373, 0.044...|
|             Hematocrit|  584|593|11151-8|[11151-8, 16931-8, 32354-3, 20570-8, 11153-4, 39227-4, 42908-4...|[Hematocrit [Hematocrit], Hematocrit/Hemoglobin [Hematocrit/He...|[0.0000, 0.0506, 0.0590, 0.0625, 0.0675, 0.0740, 0.1035, 0.101...|
|Mean Corpuscular Volume|  600|622|11272-2|[11272-2, 30386-7, 48706-6, 30899-9, 51641-9, 33878-0, 11666-5...|[Erythrocyte mean corpuscular volume [Erythrocyte mean corpusc...|[0.0857, 0.1056, 0.1270, 0.1213, 0.1289, 0.1257, 0.1352, 0.142...|
+-----------------------+-----+---+-------+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|loinc_numeric_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.9 GB|

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
