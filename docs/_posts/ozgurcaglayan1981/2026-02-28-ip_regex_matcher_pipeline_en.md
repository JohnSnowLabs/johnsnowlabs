---
layout: model
title: URL Regex Matcher Pipeline
author: John Snow Labs
name: ip_regex_matcher_pipeline
date: 2026-02-28
tags: [en, contextualparser, licensed, clinical, url, pipeline]
task: [Contextual Parser, Pipeline Healthcare]
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

This pipeline,  extracts URLs in clinical notes using rule-based RegexMatcherInternal annotator.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ip_regex_matcher_pipeline_en_6.3.0_3.4_1772307798156.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ip_regex_matcher_pipeline_en_6.3.0_3.4_1772307798156.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ip_regex_matcher_pipeline", "en", "clinical/models")

sample_text = """ Name: ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
        Access the router at http://192.168.0.1 for configuration. Please connect to 10.0.0.1 to access the database..
        Visit http://198.51.100.42 for more information. File transfers can be done via ftp://files.example.com.
        The backup server is located at 172.16.254.1 and the monitoring system can be reached at 203.0.113.0.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("ip_regex_matcher_pipeline", "en", "clinical/models")

sample_text = """ Name: ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
        Access the router at http://192.168.0.1 for configuration. Please connect to 10.0.0.1 to access the database..
        Visit http://198.51.100.42 for more information. File transfers can be done via ftp://files.example.com.
        The backup server is located at 172.16.254.1 and the monitoring system can be reached at 203.0.113.0.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("ip_regex_matcher_pipeline", "en", "clinical/models")

val sample_text = """ Name: ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
        Access the router at http://192.168.0.1 for configuration. Please connect to 10.0.0.1 to access the database..
        Visit http://198.51.100.42 for more information. File transfers can be done via ftp://files.example.com.
        The backup server is located at 172.16.254.1 and the monitoring system can be reached at 203.0.113.0.
"""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk         |   begin |   end | label   |
|:--------------|--------:|------:|:--------|
| 192.168.0.1   |     131 |   141 | IP      |
| 10.0.0.1      |     180 |   187 | IP      |
| 198.51.100.42 |     235 |   247 | IP      |
| 172.16.254.1  |     367 |   378 | IP      |
| 203.0.113.0   |     424 |   434 | IP      |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ip_regex_matcher_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|6.9 KB|

## Included Models

- DocumentAssembler
- RegexMatcherInternalModel
- ChunkConverter