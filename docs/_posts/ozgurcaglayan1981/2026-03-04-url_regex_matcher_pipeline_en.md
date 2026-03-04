---
layout: model
title: URL Regex Matcher Pipeline
author: John Snow Labs
name: url_regex_matcher_pipeline
date: 2026-03-04
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

This pipeline, extracts URLs in clinical notes using rule-based RegexMatcherInternal annotator.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/url_regex_matcher_pipeline_en_6.3.0_3.4_1772593153467.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/url_regex_matcher_pipeline_en_6.3.0_3.4_1772593153467.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("url_regex_matcher_pipeline", "en", "clinical/models")

sample_text = """ Name: ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
        For more details, visit our website at www.johnsnowlabs.com or check out http://example.com for general info.
        For secure access, go to https://secure.example.com. File transfers can be done via ftp://files.example.com.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("url_regex_matcher_pipeline", "en", "clinical/models")

sample_text = """ Name: ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
        For more details, visit our website at www.johnsnowlabs.com or check out http://example.com for general info.
        For secure access, go to https://secure.example.com. File transfers can be done via ftp://files.example.com.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("url_regex_matcher_pipeline", "en", "clinical/models")

val sample_text = """ Name: ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
        For more details, visit our website at www.johnsnowlabs.com or check out http://example.com for general info.
        For secure access, go to https://secure.example.com. File transfers can be done via ftp://files.example.com.
"""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk                      |   begin |   end | label   |
|:---------------------------|--------:|------:|:--------|
| www.johnsnowlabs.com       |     142 |   161 | URL     |
| http://example.com         |     176 |   193 | URL     |
| https://secure.example.com |     246 |   271 | URL     |
| ftp://files.example.com    |     305 |   327 | URL     |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|url_regex_matcher_pipeline|
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