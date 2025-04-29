---
layout: model
title: Detect Substance Usage Entities (SUBSTANCE_USE)
author: John Snow Labs
name: ner_substance_use_benchmark_pipeline
date: 2025-03-28
tags: [licensed, clinical, en, pipeline, ner, substance_use, benchmark]
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

This pipeline can be used to extracts `substance usage` information in medical text.
`SUBSTANCE_USE`: Mentions of illegal recreational drugs use. Include also substances that can create dependency including here caffeine and tea. “overdose, cocaine, illicit substance intoxication, coffee, etc.”.

## Predicted Entities

`SUBSTANCE_USE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_substance_use_benchmark_pipeline_en_5.5.3_3.4_1743121281304.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_substance_use_benchmark_pipeline_en_5.5.3_3.4_1743121281304.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_substance_use_benchmark_pipeline", "en", "clinical/models")

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

ner_pipeline = nlp.PretrainedPipeline("ner_substance_use_benchmark_pipeline", "en", "clinical/models")

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

val ner_pipeline = PretrainedPipeline("ner_substance_use_benchmark_pipeline", "en", "clinical/models")

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
|    | chunk            |   begin |   end | ner_label     |
|---:|:-----------------|--------:|------:|:--------------|
|  0 | illicit drug use |      68 |    83 | SUBSTANCE_USE |
|  1 | drug use         |     320 |   327 | SUBSTANCE_USE |
|  2 | illegal drug use |     462 |   477 | SUBSTANCE_USE |
|  3 | IV drug use      |     745 |   755 | SUBSTANCE_USE |
|  4 | heroin use       |     821 |   830 | SUBSTANCE_USE |
|  5 | using cocaine    |     876 |   888 | SUBSTANCE_USE |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_substance_use_benchmark_pipeline|
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
- ChunkMergeModel
- ChunkMergeModel

## Benchmarking

```bash
        label  precision    recall  f1-score   support
            O      1.000     1.000     1.000     82313
SUBSTANCE_USE      1.000     0.981     0.990       258
     accuracy      -         -         1.000     82571
    macro-avg      1.000     0.990     0.995     82571
 weighted-avg      1.000     1.000     1.000     82571
```