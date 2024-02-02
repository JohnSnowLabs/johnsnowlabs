---
layout: model
title: Pipeline for ICD-O
author: John Snow Labs
name: icdo_resolver_pipeline
date: 2024-02-02
tags: [licensed, en, icdo, pipeline, resolver]
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

This pipeline extracts oncological entities from clinical texts and map them to their corresponding ICD-O codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icdo_resolver_pipeline_en_5.2.1_3.4_1706887384588.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icdo_resolver_pipeline_en_5.2.1_3.4_1706887384588.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("icdo_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""TRAF6 is a  putative oncogene in a variety of cancers  including
bladder cancer and skin cancer . WWP2 appears to regulate the expression of the well characterized
tumor  suppressor phosphatase and tensin homolog (PTEN) in endometrial cancer and squamous cell carcinoma.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("icdo_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""TRAF6 is a  putative oncogene in a variety of cancers  including
bladder cancer and skin cancer . WWP2 appears to regulate the expression of the well characterized
tumor  suppressor phosphatase and tensin homolog (PTEN) in endometrial cancer and squamous cell carcinoma.""")

```
</div>

## Results

```bash

+------------------+-----------------+------------+-----------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|             chunk|            label|   icdO_code|             resolution|                                                             all_codes|                                                       all_resolutions|
+------------------+-----------------+------------+-----------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|           cancers|      Oncological|      8000/3|                 cancer|8000/3:::8010/3:::8010/9:::800:::8420/3:::8140/3:::8010/3-C76.0:::8...|cancer:::carcinoma:::carcinomatosis:::neoplasms:::ceruminous carcin...|
|    bladder cancer|      Oncological|8010/3-C67.9|  carcinoma, of bladder|8010/3-C67.9:::8010/3-C67.5:::8230/3-C67.9:::8140/3-C67.9:::8441/3-...|carcinoma, of bladder:::carcinoma, of bladder neck:::solid carcinom...|
|       skin cancer|      Oncological|8010/3-C44.9|     carcinoma, of skin|8010/3-C44.9:::8010/9-C44.9:::8070/3-C44.9:::8140/3-C44.9:::8980/3-...|carcinoma, of skin:::carcinomatosis of skin:::squamous cell carcino...|
|             tumor|      Oncological|      8000/1|                  tumor|8000/1:::8040/1:::8001/1:::9365/3:::8000/6:::8103/0:::9364/3:::8940...|tumor:::tumorlet:::tumor cells:::askin tumor:::tumor, secondary:::p...|
|endometrial cancer|      Oncological|      8380/3| endometrioid carcinoma|8380/3:::8010/3-C54.1:::8380/3-C57.9:::8575/3-C54.1:::8560/3-C54.1:...|endometrioid carcinoma:::carcinoma, of endometrium:::endometrioid a...|
|     squamous cell|Histological_Type|     805-808|squamous cell neoplasms|805-808:::8070/3:::C08.1:::C32.2:::9084/0:::C09.1:::8075/3:::C44.0:...|squamous cell neoplasms:::squamous carcinoma:::sublingual gland:::s...|
|         carcinoma|        Cancer_Dx|      8010/3|              carcinoma|8010/3:::8010/9:::8420/3:::8480/3:::8240/3:::8550/3:::8140/3:::8010...|carcinoma:::carcinomatosis:::ceruminous carcinoma:::mucous carcinom...|
+------------------+-----------------+------------+-----------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icdo_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.3 GB|

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