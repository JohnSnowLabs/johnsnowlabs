---
layout: model
title: SSN Number Contextual Parser Pipeline
author: John Snow Labs
name: ssn_parser_pipeline
date: 2026-03-04
tags: [en, contextualparser, licensed, clinical, ssn, pipeline]
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

This pipeline, extracts SSN number entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ssn_parser_pipeline_en_6.3.0_3.4_1772588508318.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ssn_parser_pipeline_en_6.3.0_3.4_1772588508318.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ssn_parser_pipeline", "en", "clinical/models")

sample_text = """ San Diego, CA, USA
Email: medunites@firsthospital.com
Patient John Davies, 62 y.o. ssn: 023-92-7136 was discharged after 12 hours of monitoring without any signs of internal damage.
TSICU Admission 65332 on 24/06/2019 by ambulance VIN 4Y1SL65848Z411439
Patient Mary Smith, 45 y.o. ssn: 456-78-9012 was admitted for routine checkup on 25/06/2019.
Patient Robert Johnson, 38 y.o. ssn: 789-12-3456 underwent surgery on 26/06/2019.
Patient Sarah Williams, 55 y.o. ssn: 234-56-7890 was treated in emergency room on 27/06/2019.
Patient Michael Brown, 41 y.o. ssn: 567-89-0123 was released after observation on 28/06/2019."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("ssn_parser_pipeline", "en", "clinical/models")

sample_text = """ San Diego, CA, USA
Email: medunites@firsthospital.com
Patient John Davies, 62 y.o. ssn: 023-92-7136 was discharged after 12 hours of monitoring without any signs of internal damage.
TSICU Admission 65332 on 24/06/2019 by ambulance VIN 4Y1SL65848Z411439
Patient Mary Smith, 45 y.o. ssn: 456-78-9012 was admitted for routine checkup on 25/06/2019.
Patient Robert Johnson, 38 y.o. ssn: 789-12-3456 underwent surgery on 26/06/2019.
Patient Sarah Williams, 55 y.o. ssn: 234-56-7890 was treated in emergency room on 27/06/2019.
Patient Michael Brown, 41 y.o. ssn: 567-89-0123 was released after observation on 28/06/2019."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("ssn_parser_pipeline", "en", "clinical/models")

val sample_text = """ San Diego, CA, USA
Email: medunites@firsthospital.com
Patient John Davies, 62 y.o. ssn: 023-92-7136 was discharged after 12 hours of monitoring without any signs of internal damage.
TSICU Admission 65332 on 24/06/2019 by ambulance VIN 4Y1SL65848Z411439
Patient Mary Smith, 45 y.o. ssn: 456-78-9012 was admitted for routine checkup on 25/06/2019.
Patient Robert Johnson, 38 y.o. ssn: 789-12-3456 underwent surgery on 26/06/2019.
Patient Sarah Williams, 55 y.o. ssn: 234-56-7890 was treated in emergency room on 27/06/2019.
Patient Michael Brown, 41 y.o. ssn: 567-89-0123 was released after observation on 28/06/2019."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk       |   begin |   end | label   |
|:------------|--------:|------:|:--------|
| 023-92-7136 |      88 |    98 | SSN     |
| 456-78-9012 |     286 |   296 | SSN     |
| 789-12-3456 |     383 |   393 | SSN     |
| 234-56-7890 |     465 |   475 | SSN     |
| 567-89-0123 |     558 |   568 | SSN     |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ssn_parser_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|396.6 KB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- ContextualParserModel
- ChunkConverter