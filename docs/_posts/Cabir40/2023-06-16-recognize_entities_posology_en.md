---
layout: model
title: Pipeline for detecting posology entities
author: John Snow Labs
name: recognize_entities_posology
date: 2023-06-16
tags: [pipeline, en, licensed, clinical]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

A pipeline with `ner_posology`. It will only extract medication entities.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/recognize_entities_posology_en_4.4.4_3.2_1686943601343.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/recognize_entities_posology_en_4.4.4_3.2_1686943601343.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
pipeline = PretrainedPipeline('recognize_entities_posology', 'en', 'clinical/models')

res = pipeline.fullAnnotate("""A 28-year-old female with a history of gestational diabetes mellitus, used to take metformin 1000 mg two times a day, presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .
She was seen by the endocrinology service and discharged on 40 units of insulin glargine at night, 12 units of insulin lispro with meals.
""")
```
```scala
val era_pipeline = new PretrainedPipeline("recognize_entities_posology", "en", "clinical/models")

val result = era_pipeline.fullAnnotate("""A 28-year-old female with a history of gestational diabetes mellitus, used to take metformin 1000 mg two times a day, presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .
She was seen by the endocrinology service and discharged on 40 units of insulin glargine at night, 12 units of insulin lispro with meals.
""")(0)

```


{:.nlu-block}
```python
import nlu
nlu.load("en.recognize_entities.posology").predict("""A 28-year-old female with a history of gestational diabetes mellitus, used to take metformin 1000 mg two times a day, presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .
She was seen by the endocrinology service and discharged on 40 units of insulin glargine at night, 12 units of insulin lispro with meals.
""")
```

</div>

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
pipeline = PretrainedPipeline('recognize_entities_posology', 'en', 'clinical/models')

res = pipeline.fullAnnotate("""A 28-year-old female with a history of gestational diabetes mellitus, used to take metformin 1000 mg two times a day, presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .
She was seen by the endocrinology service and discharged on 40 units of insulin glargine at night, 12 units of insulin lispro with meals.
""")
```
```scala
val era_pipeline = new PretrainedPipeline("recognize_entities_posology", "en", "clinical/models")

val result = era_pipeline.fullAnnotate("""A 28-year-old female with a history of gestational diabetes mellitus, used to take metformin 1000 mg two times a day, presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .
She was seen by the endocrinology service and discharged on 40 units of insulin glargine at night, 12 units of insulin lispro with meals.
""")(0)
```

{:.nlu-block}
```python
import nlu
nlu.load("en.recognize_entities.posology").predict("""A 28-year-old female with a history of gestational diabetes mellitus, used to take metformin 1000 mg two times a day, presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .
She was seen by the endocrinology service and discharged on 40 units of insulin glargine at night, 12 units of insulin lispro with meals.
""")
```
</div>

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
pipeline = PretrainedPipeline('recognize_entities_posology', 'en', 'clinical/models')

res = pipeline.fullAnnotate("""A 28-year-old female with a history of gestational diabetes mellitus, used to take metformin 1000 mg two times a day, presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .
She was seen by the endocrinology service and discharged on 40 units of insulin glargine at night, 12 units of insulin lispro with meals.
""")
```
```scala
val era_pipeline = new PretrainedPipeline("recognize_entities_posology", "en", "clinical/models")

val result = era_pipeline.fullAnnotate("""A 28-year-old female with a history of gestational diabetes mellitus, used to take metformin 1000 mg two times a day, presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .
She was seen by the endocrinology service and discharged on 40 units of insulin glargine at night, 12 units of insulin lispro with meals.
""")(0)
```

{:.nlu-block}
```python
import nlu
nlu.load("en.recognize_entities.posology").predict("""A 28-year-old female with a history of gestational diabetes mellitus, used to take metformin 1000 mg two times a day, presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting .
She was seen by the endocrinology service and discharged on 40 units of insulin glargine at night, 12 units of insulin lispro with meals.
""")
```
</div>

## Results

```bash
Results


Results


|    | chunk            |   begin |   end | entity    |
|---:|:-----------------|--------:|------:|:----------|
|  0 | metformin        |      83 |    91 | DRUG      |
|  1 | 1000 mg          |      93 |    99 | STRENGTH  |
|  2 | two times a day  |     101 |   115 | FREQUENCY |
|  3 | 40 units         |     270 |   277 | DOSAGE    |
|  4 | insulin glargine |     282 |   297 | DRUG      |
|  5 | at night         |     299 |   306 | FREQUENCY |
|  6 | 12 units         |     309 |   316 | DOSAGE    |
|  7 | insulin lispro   |     321 |   334 | DRUG      |
|  8 | with meals       |     336 |   345 | FREQUENCY |



{:.model-param}


{:.model-param}
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|recognize_entities_posology|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter