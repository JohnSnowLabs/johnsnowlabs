---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_deid_generic_nonMedical_medium) - Pipeline
author: John Snow Labs
name: zeroshot_ner_deid_generic_nonMedical_medium_pipeline
date: 2026-03-02
tags: [en, ner, deid, licensed, clinical, zeroshot, generic, pipeline]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.3.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline implements Zero-shot Named Entity Recognition (NER) using a pre-trained language model with contextual understanding. It enables entity extraction across different domains without task-specific fine-tuning.

Unlike fully flexible zero-shot setups, this pipeline operates with a fixed label schema to ensure consistent and standardized outputs. The supported entity labels are:

"NAME", "AGE", "DATE", "LOCATION", "ID", "CONTACT", "PROFESSION"

All predictions are restricted to this predefined set of labels. This design ensures production stability, output consistency, and reliable performance within the defined entity scope.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_generic_nonMedical_medium_pipeline_en_6.3.0_3.4_1772489808958.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_generic_nonMedical_medium_pipeline_en_6.3.0_3.4_1772489808958.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("zeroshot_ner_deid_generic_nonMedical_medium_pipeline", "en", "clinical/models")

sample_text = """ Mr. James Wilson is a 65-year-old male who presented to the emergency department at Boston General Hospital on 10/25/2023. 
He lives at 123 Oak Street, Springfield, IL 62704. He can be contacted at 555-0199. 
His SSN is 999-00-1234. Dr. Gregory House is the attending physician."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("zeroshot_ner_deid_generic_nonMedical_medium_pipeline", "en", "clinical/models")

sample_text = """ Mr. James Wilson is a 65-year-old male who presented to the emergency department at Boston General Hospital on 10/25/2023. 
He lives at 123 Oak Street, Springfield, IL 62704. He can be contacted at 555-0199. 
His SSN is 999-00-1234. Dr. Gregory House is the attending physician."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("zeroshot_ner_deid_generic_nonMedical_medium_pipeline", "en", "clinical/models")

val sample_text = """ Mr. James Wilson is a 65-year-old male who presented to the emergency department at Boston General Hospital on 10/25/2023. 
He lives at 123 Oak Street, Springfield, IL 62704. He can be contacted at 555-0199. 
His SSN is 999-00-1234. Dr. Gregory House is the attending physician."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk                   | begin | end | ner_label | confidence |
| :---------------------- | ----: | --: | :-------- | ---------: |
| James Wilson            |     4 |  15 | NAME      |  0.9993062 |
| 65-year-old             |    22 |  32 | AGE       |  0.9988632 |
| Boston General Hospital |    84 | 106 | LOCATION  |  0.9958438 |
| 10/25/2023              |   111 | 120 | DATE      |   0.992315 |
| 123 Oak Street          |   136 | 149 | LOCATION  |  0.9757989 |
| Springfield             |   152 | 162 | LOCATION  |  0.9798023 |
| IL                      |   165 | 166 | LOCATION  |  0.9987602 |
| 62704                   |   168 | 172 | LOCATION  |  0.9594391 |
| 555-0199                |   198 | 205 | CONTACT   |  0.9907244 |
| SSN                     |   213 | 215 | LOCATION  |  0.7714427 |
| 999-00-1234             |   220 | 230 | ID        |  0.9963062 |
| Gregory House           |   237 | 249 | NAME      |  0.9979722 |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_deid_generic_nonMedical_medium_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|789.8 MB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- PretrainedZeroShotNER
- NerConverterInternalModel