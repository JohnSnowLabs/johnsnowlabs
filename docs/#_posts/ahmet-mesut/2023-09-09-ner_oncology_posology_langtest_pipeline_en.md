---
layout: model
title: Pipeline to Extract Cancer Therapies and Granular Posology Information (langtest)
author: John Snow Labs
name: ner_oncology_posology_langtest_pipeline
date: 2023-09-09
tags: [licensed, en, oncology, posology, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.1.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_oncology_posology_langtest](https://nlp.johnsnowlabs.com/2023/09/04/ner_oncology_posology_langtest_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_posology_langtest_pipeline_en_5.1.0_3.4_1694292192837.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_posology_langtest_pipeline_en_5.1.0_3.4_1694292192837.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_oncology_posology_langtest_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses. She is currently receiving his second cycle of chemotherapy and is in good overall condition.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_oncology_posology_langtest_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses. She is currently receiving his second cycle of chemotherapy and is in good overall condition.""")

```
</div>

## Results

```bash
|    | chunks           |   begin |   end | entities       |
|---:|:-----------------|--------:|------:|:---------------|
|  0 | adriamycin       |      46 |    55 | Cancer_Therapy |
|  1 | 60 mg/m2         |      58 |    65 | Dosage         |
|  2 | cyclophosphamide |      72 |    87 | Cancer_Therapy |
|  3 | 600 mg/m2        |      90 |    98 | Dosage         |
|  4 | six courses      |     106 |   116 | Cycle_Count    |
|  5 | second cycle     |     150 |   161 | Cycle_Number   |
|  6 | chemotherapy     |     166 |   177 | Cancer_Therapy |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_posology_langtest_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.1.0+|
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
- NerConverter