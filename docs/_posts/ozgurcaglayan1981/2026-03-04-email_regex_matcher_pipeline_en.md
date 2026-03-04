---
layout: model
title: Email Regex Matcher
author: John Snow Labs
name: email_regex_matcher_pipeline
date: 2026-03-04
tags: [en, contextualparser, licensed, clinical, email, pipeline]
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

This pipeline,  extracts emails in clinical notes using rule-based RegexMatcherInternal annotator.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/email_regex_matcher_pipeline_en_6.3.0_3.4_1772592437954.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/email_regex_matcher_pipeline_en_6.3.0_3.4_1772592437954.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("email_regex_matcher_pipeline", "en", "clinical/models")

sample_text = """ ID: 1231511863, The driver's license no:A334455B, the SSN:324598674 and info@domain.net, mail: tech@support.org, e-mail: hale@gmail.com .
 E-mail: sales@gmail.com.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("email_regex_matcher_pipeline", "en", "clinical/models")

sample_text = """ ID: 1231511863, The driver's license no:A334455B, the SSN:324598674 and info@domain.net, mail: tech@support.org, e-mail: hale@gmail.com .
 E-mail: sales@gmail.com.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("email_regex_matcher_pipeline", "en", "clinical/models")

val sample_text = """ ID: 1231511863, The driver's license no:A334455B, the SSN:324598674 and info@domain.net, mail: tech@support.org, e-mail: hale@gmail.com .
 E-mail: sales@gmail.com.
"""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk            |   begin |   end | label   |
|:-----------------|--------:|------:|:--------|
| info@domain.net  |      72 |    86 | EMAIL   |
| tech@support.org |      95 |   110 | EMAIL   |
| hale@gmail.com   |     121 |   134 | EMAIL   |
| sales@gmail.com  |     147 |   161 | EMAIL   |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|email_regex_matcher_pipeline|
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