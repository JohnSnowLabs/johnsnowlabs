---
layout: model
title: Detect Drug Entities - Pipeline
author: John Snow Labs
name: ner_drugs_large_v2_pipeline
date: 2026-03-04
tags: [en, clinical, licensed, ner, pipeline]
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

This pipeline, combines dosage, strength, form, and route into a single entity: Drug.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_drugs_large_v2_pipeline_en_6.3.0_3.4_1772642735940.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_drugs_large_v2_pipeline_en_6.3.0_3.4_1772642735940.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_drugs_large_v2_pipeline", "en", "clinical/models")

sample_text = """ 
The patient is a 40-year-old white male who presents with a chief complaint of 'chest pain'.
The patient is diabetic and has a prior history of coronary artery disease.
The patient presents today stating that his chest pain started yesterday evening and has been somewhat intermittent.
He has been advised Aspirin 81 milligrams QDay.
Humulin N. insulin 50 units in a.m.
HCTZ 50 mg QDay. Nitroglycerin 1/150 sublingually PRN chest pain.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("ner_drugs_large_v2_pipeline", "en", "clinical/models")

sample_text = """ 
The patient is a 40-year-old white male who presents with a chief complaint of 'chest pain'.
The patient is diabetic and has a prior history of coronary artery disease.
The patient presents today stating that his chest pain started yesterday evening and has been somewhat intermittent.
He has been advised Aspirin 81 milligrams QDay.
Humulin N. insulin 50 units in a.m.
HCTZ 50 mg QDay. Nitroglycerin 1/150 sublingually PRN chest pain.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("ner_drugs_large_v2_pipeline", "en", "clinical/models")

val sample_text = """ 
The patient is a 40-year-old white male who presents with a chief complaint of 'chest pain'.
The patient is diabetic and has a prior history of coronary artery disease.
The patient presents today stating that his chest pain started yesterday evening and has been somewhat intermittent.
He has been advised Aspirin 81 milligrams QDay.
Humulin N. insulin 50 units in a.m.
HCTZ 50 mg QDay. Nitroglycerin 1/150 sublingually PRN chest pain.
"""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk         | begin | end | ner_label |
| :------------ | ----: | --: | :-------- |
| Aspirin       |   307 | 313 | DRUG      |
| Humulin N     |   335 | 343 | DRUG      |
| insulin       |   346 | 352 | DRUG      |
| HCTZ          |   371 | 374 | DRUG      |
| Nitroglycerin |   388 | 400 | DRUG      |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_drugs_large_v2_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.0 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel