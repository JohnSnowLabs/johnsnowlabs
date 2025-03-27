---
layout: model
title: Detect Treatment Entities (ALCOHOL_USE)
author: John Snow Labs
name: ner_alcohol_use_benchmark_pipeline
date: 2025-03-27
tags: [licensed, clinical, en, pipeline, ner, alcohol_use, benchmark]
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

This pipeline can be used to detect and label alcohol-related entities within medical text.
Alcohol refers to beverages containing ethanol, a psychoactive substance that is widely consumed for its pleasurable effects.

## Predicted Entities

`ALCOHOL_USE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_alcohol_use_benchmark_pipeline_en_5.5.3_3.4_1743119650970.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_alcohol_use_benchmark_pipeline_en_5.5.3_3.4_1743119650970.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_alcohol_use_benchmark_pipeline", "en", "clinical/models")

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

ner_pipeline = nlp.PretrainedPipeline("ner_alcohol_use_benchmark_pipeline", "en", "clinical/models")

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

val ner_pipeline = PretrainedPipeline("ner_alcohol_use_benchmark_pipeline", "en", "clinical/models")

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
|    | chunk               |   begin |   end | ner_label   |
|---:|:--------------------|--------:|------:|:------------|
|  0 | alcohol             |      57 |    63 | ALCOHOL_USE |
|  1 | drink               |     231 |   235 | ALCOHOL_USE |
|  2 | alcohol             |     248 |   254 | ALCOHOL_USE |
|  3 | alcoholic drinks    |     277 |   292 | ALCOHOL_USE |
|  4 | liquor              |     347 |   352 | ALCOHOL_USE |
|  5 | alcohol use         |     400 |   410 | ALCOHOL_USE |
|  6 | Drinking            |     414 |   421 | ALCOHOL_USE |
|  7 | consume alcohol     |     636 |   650 | ALCOHOL_USE |
|  8 | alcoholic beverages |     685 |   703 | ALCOHOL_USE |
|  9 | alcohol             |     879 |   885 | ALCOHOL_USE |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_alcohol_use_benchmark_pipeline|
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
- TextMatcherInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel

## Benchmarking

```bash

       label  precision    recall  f1-score   support
 ALCOHOL_USE      0.991     0.970     0.980       230
           O      1.000     1.000     1.000     82341
    accuracy                          1.000     82571
   macro avg      0.996     0.985     0.990     82571
weighted avg      1.000     1.000     1.000     82571

```