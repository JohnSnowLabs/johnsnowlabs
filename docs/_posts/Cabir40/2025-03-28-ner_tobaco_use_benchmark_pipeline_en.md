---
layout: model
title: Detect Smoking / Tobaco Entities (TOBACO_USE)
author: John Snow Labs
name: ner_tobaco_use_benchmark_pipeline
date: 2025-03-28
tags: [licensed, clinical, en, pipeline, ner, tobaco_use, benchmark]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.5.3
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to detect and label smoking-related entities within medical text.
Smoking/Tobacco typically involves inhaling smoke from burning tobacco, a highly addictive substance.

## Predicted Entities

`TOBACO_USE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_tobaco_use_benchmark_pipeline_en_5.5.3_3.4_1743120280709.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_tobaco_use_benchmark_pipeline_en_5.5.3_3.4_1743120280709.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_tobaco_use_benchmark_pipeline", "en", "clinical/models")

text = """SOCIAL HISTORY : The patient is a nonsmoker . Denies any alcohol or illicit drug use . The patient does live with his family .
SOCIAL HISTORY : The patient smokes approximately 2 packs per day times greater than 40 years . He does drink occasional alcohol approximately 5 to 6 alcoholic drinks per month . He denies any drug use . He is a retired liquor store owner .
SOCIAL HISTORY : Patient admits alcohol use , Drinking is described as heavy , Patient denies illegal drug use , Patient denies STD history , Patient denies tobacco use .
SOCIAL HISTORY : The patient is employed in the finance department . He is a nonsmoker . He does consume alcohol on the weekend as much as 3 to 4 alcoholic beverages per day on the weekends . He denies any IV drug use or abuse .
SOCIAL HISTORY : She is married .Employed with the US Post Office .She is a mother of three . Denies tobacco , alcohol or illicit drug use . MEDICATIONS . Coumadin 1 mg daily .Last INR was on Tuesday , August 14 , 2007 , and her INR was 2.3.2 . Amiodarone 100 mg p.o . daily .
"""

result = ner_pipeline.fullAnnotate(text)
```

{:.jsl-block}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = nlp.PretrainedPipeline("ner_tobaco_use_benchmark_pipeline", "en", "clinical/models")

text = """SOCIAL HISTORY : The patient is a nonsmoker . Denies any alcohol or illicit drug use . The patient does live with his family .
SOCIAL HISTORY : The patient smokes approximately 2 packs per day times greater than 40 years . He does drink occasional alcohol approximately 5 to 6 alcoholic drinks per month . He denies any drug use . He is a retired liquor store owner .
SOCIAL HISTORY : Patient admits alcohol use , Drinking is described as heavy , Patient denies illegal drug use , Patient denies STD history , Patient denies tobacco use .
SOCIAL HISTORY : The patient is employed in the finance department . He is a nonsmoker . He does consume alcohol on the weekend as much as 3 to 4 alcoholic beverages per day on the weekends . He denies any IV drug use or abuse .
SOCIAL HISTORY : She is married .Employed with the US Post Office .She is a mother of three . Denies tobacco , alcohol or illicit drug use . MEDICATIONS . Coumadin 1 mg daily .Last INR was on Tuesday , August 14 , 2007 , and her INR was 2.3.2 . Amiodarone 100 mg p.o . daily .
"""

result = ner_pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_tobaco_use_benchmark_pipeline", "en", "clinical/models")

val text = """SOCIAL HISTORY : The patient is a nonsmoker . Denies any alcohol or illicit drug use . The patient does live with his family .
SOCIAL HISTORY : The patient smokes approximately 2 packs per day times greater than 40 years . He does drink occasional alcohol approximately 5 to 6 alcoholic drinks per month . He denies any drug use . He is a retired liquor store owner .
SOCIAL HISTORY : Patient admits alcohol use , Drinking is described as heavy , Patient denies illegal drug use , Patient denies STD history , Patient denies tobacco use .
SOCIAL HISTORY : The patient is employed in the finance department . He is a nonsmoker . He does consume alcohol on the weekend as much as 3 to 4 alcoholic beverages per day on the weekends . He denies any IV drug use or abuse .
SOCIAL HISTORY : She is married .Employed with the US Post Office .She is a mother of three . Denies tobacco , alcohol or illicit drug use . MEDICATIONS . Coumadin 1 mg daily .Last INR was on Tuesday , August 14 , 2007 , and her INR was 2.3.2 . Amiodarone 100 mg p.o . daily .
"""

val result = ner_pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | chunk     |   begin |   end | ner_label   |
|---:|:----------|--------:|------:|:------------|
|  0 | nonsmoker |      34 |    42 | TOBACO_USE  |
|  1 | smokes    |     156 |   161 | TOBACO_USE  |
|  2 | tobacco   |     525 |   531 | TOBACO_USE  |
|  3 | nonsmoker |     616 |   624 | TOBACO_USE  |
|  4 | tobacco   |     869 |   875 | TOBACO_USE  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_tobaco_use_benchmark_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.3+|
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
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel

## Benchmarking

```bash

       label  precision    recall  f1-score   support
           O      1.000     1.000     1.000     82397
  TOBACO_USE      1.000     0.994     0.997       174
    accuracy                          1.000     82571
   macro avg      1.000     0.997     0.999     82571
weighted avg      1.000     1.000     1.000     82571

```