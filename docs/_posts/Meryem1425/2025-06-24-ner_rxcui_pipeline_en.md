---
layout: model
title: Pipeline for Extracting Clinical Entities Related to RxCUI Codes
author: John Snow Labs
name: ner_rxcui_pipeline
date: 2025-06-24
tags: [licensed, en, clinical, pipeline, ner]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to extract all entities mappable to RxCUI codes.

1 NER model and a Text Matcher are used to achieve those tasks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_rxcui_pipeline_en_6.0.2_3.4_1750795558380.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_rxcui_pipeline_en_6.0.2_3.4_1750795558380.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_rxcui_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
The patient was prescribed Albuterol inhaler when needed. She was seen by the endocrinology service, prescribed Avandia 4 mg at nights,
Coumadin 5 mg with meals, Metformin 100 mg two times a day, and a daily dose of Lisinopril 10 mg.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_rxcui_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
The patient was prescribed Albuterol inhaler when needed. She was seen by the endocrinology service, prescribed Avandia 4 mg at nights,
Coumadin 5 mg with meals, Metformin 100 mg two times a day, and a daily dose of Lisinopril 10 mg.
""")

```
</div>

## Results

```bash
|    | chunks            |   begin |   end | entities   |
|---:|:------------------|--------:|------:|:-----------|
|  0 | Albuterol inhaler |      28 |    44 | DRUG       |
|  1 | Avandia 4 mg      |     113 |   124 | DRUG       |
|  2 | Coumadin 5 mg     |     137 |   149 | DRUG       |
|  3 | Metformin 100 mg  |     163 |   178 | DRUG       |
|  4 | Lisinopril 10 mg  |     217 |   232 | DRUG       |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_rxcui_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- TextMatcherInternalModel
- ChunkMergeModel