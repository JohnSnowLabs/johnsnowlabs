---
layout: model
title: Detect Alcohol, Smoking/Tobacco, and Subtance Usage Entities (CONSUMPTION)
author: John Snow Labs
name: ner_consumption_benchmark_pipeline
date: 2025-03-28
tags: [licensed, clinical, en, pipeline, ner, consumption, benchmark]
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

This pipeline can be used to extracts `Consumption` (Alcohol, Smoking/Tobaco, and Substance Usage) related information in medical text.
Alcohol refers to beverages containing ethanol, a psychoactive substance that is widely consumed for its pleasurable effects. 
Smoking typically involves inhaling smoke from burning tobacco, a highly addictive substance. 
Substance mentions of illegal recreational drugs use. Include also substances that can create dependency including here caffeine and tea. “overdose, cocaine, illicit substance intoxication, coffee, etc

## Predicted Entities

`CONSUMPTION`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_consumption_benchmark_pipeline_en_5.5.3_3.4_1743125946593.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_consumption_benchmark_pipeline_en_5.5.3_3.4_1743125946593.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_consumption_benchmark_pipeline", "en", "clinical/models")

text = """SOCIAL HISTORY : The patient is a nonsmoker . Denies any alcohol or illicit drug use . The patient does live with his family .
SOCIAL HISTORY : The patient smokes approximately 2 packs per day times greater than 40 years . He does drink occasional alcohol approximately 5 to 6 alcoholic drinks per month . He denies any drug use . He is a retired liquor store owner .
SOCIAL HISTORY : Patient admits alcohol use , Drinking is described as heavy , Patient denies illegal drug use , Patient denies STD history , Patient denies tobacco use .
SOCIAL HISTORY : The patient is employed in the finance department . He is a nonsmoker . He does consume alcohol on the weekend as much as 3 to 4 alcoholic beverages per day on the weekends . He denies any IV drug use or abuse .
SOCIAL HISTORY : The patient is a smoker . Admits to heroin use , alcohol abuse as well . Also admits today using cocaine .
"""

result = ner_pipeline.fullAnnotate(text)
```

{:.jsl-block}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = nlp.PretrainedPipeline("ner_consumption_benchmark_pipeline", "en", "clinical/models")

text = """SOCIAL HISTORY : The patient is a nonsmoker . Denies any alcohol or illicit drug use . The patient does live with his family .
SOCIAL HISTORY : The patient smokes approximately 2 packs per day times greater than 40 years . He does drink occasional alcohol approximately 5 to 6 alcoholic drinks per month . He denies any drug use . He is a retired liquor store owner .
SOCIAL HISTORY : Patient admits alcohol use , Drinking is described as heavy , Patient denies illegal drug use , Patient denies STD history , Patient denies tobacco use .
SOCIAL HISTORY : The patient is employed in the finance department . He is a nonsmoker . He does consume alcohol on the weekend as much as 3 to 4 alcoholic beverages per day on the weekends . He denies any IV drug use or abuse .
SOCIAL HISTORY : The patient is a smoker . Admits to heroin use , alcohol abuse as well . Also admits today using cocaine .
"""

result = ner_pipeline.fullAnnotate(text)
```

```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_consumption_benchmark_pipeline", "en", "clinical/models")

val text = """SOCIAL HISTORY : The patient is a nonsmoker . Denies any alcohol or illicit drug use . The patient does live with his family .
SOCIAL HISTORY : The patient smokes approximately 2 packs per day times greater than 40 years . He does drink occasional alcohol approximately 5 to 6 alcoholic drinks per month . He denies any drug use . He is a retired liquor store owner .
SOCIAL HISTORY : Patient admits alcohol use , Drinking is described as heavy , Patient denies illegal drug use , Patient denies STD history , Patient denies tobacco use .
SOCIAL HISTORY : The patient is employed in the finance department . He is a nonsmoker . He does consume alcohol on the weekend as much as 3 to 4 alcoholic beverages per day on the weekends . He denies any IV drug use or abuse .
SOCIAL HISTORY : The patient is a smoker . Admits to heroin use , alcohol abuse as well . Also admits today using cocaine .
"""

val result = ner_pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | chunk               |   begin |   end | ner_label   |
|---:|:--------------------|--------:|------:|:------------|
|  0 | nonsmoker           |      34 |    42 | CONSUMPTION |
|  1 | alcohol             |      57 |    63 | CONSUMPTION |
|  2 | illicit drug use    |      68 |    83 | CONSUMPTION |
|  3 | smokes              |     156 |   161 | CONSUMPTION |
|  4 | drink               |     231 |   235 | CONSUMPTION |
|  5 | alcohol             |     248 |   254 | CONSUMPTION |
|  6 | alcoholic drinks    |     277 |   292 | CONSUMPTION |
|  7 | drug use            |     320 |   327 | CONSUMPTION |
|  8 | alcohol use         |     400 |   410 | CONSUMPTION |
|  9 | Drinking            |     414 |   421 | CONSUMPTION |
| 10 | illegal drug use    |     462 |   477 | CONSUMPTION |
| 11 | tobacco             |     525 |   531 | CONSUMPTION |
| 12 | nonsmoker           |     616 |   624 | CONSUMPTION |
| 13 | consume alcohol     |     636 |   650 | CONSUMPTION |
| 14 | alcoholic beverages |     685 |   703 | CONSUMPTION |
| 15 | IV drug use         |     745 |   755 | CONSUMPTION |
| 16 | smoker              |     802 |   807 | CONSUMPTION |
| 17 | heroin use          |     821 |   830 | CONSUMPTION |
| 18 | alcohol abuse       |     834 |   846 | CONSUMPTION |
| 19 | using cocaine       |     876 |   888 | CONSUMPTION |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_consumption_benchmark_pipeline|
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
 CONSUMPTION      0.988     0.977     0.983       662
           O      1.000     1.000     1.000     81909
    accuracy      -         -         1.000     82571
   macro-avg      0.994     0.989     0.991     82571
weighted-avg      1.000     1.000     1.000     82571
```