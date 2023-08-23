---
layout: model
title: Oncology Pipeline for Therapies
author: John Snow Labs
name: oncology_therapy_pipeline
date: 2023-06-17
tags: [licensed, pipeline, oncology, en]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline includes Named-Entity Recognition and Assertion Status models to extract information from oncology texts. This pipeline focuses on entities related to therapies.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/oncology_therapy_pipeline_en_4.4.4_3.0_1686991329521.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/oncology_therapy_pipeline_en_4.4.4_3.0_1686991329521.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("oncology_therapy_pipeline", "en", "clinical/models")

text = '''The patient underwent a mastectomy two years ago. She is currently receiving her second cycle of adriamycin and cyclophosphamide, and is in good overall condition.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("oncology_therapy_pipeline", "en", "clinical/models")

val text = "The patient underwent a mastectomy two years ago. She is currently receiving her second cycle of adriamycin and cyclophosphamide, and is in good overall condition."

val result = pipeline.fullAnnotate(text)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.oncology_therpay.pipeline").predict("""The patient underwent a mastectomy two years ago. She is currently receiving her second cycle of adriamycin and cyclophosphamide, and is in good overall condition.""")
```

</div>

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("oncology_therapy_pipeline", "en", "clinical/models")

text = '''The patient underwent a mastectomy two years ago. She is currently receiving her second cycle of adriamycin and cyclophosphamide, and is in good overall condition.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("oncology_therapy_pipeline", "en", "clinical/models")

val text = "The patient underwent a mastectomy two years ago. She is currently receiving her second cycle of adriamycin and cyclophosphamide, and is in good overall condition."

val result = pipeline.fullAnnotate(text)
```

{:.nlu-block}
```python
import nlu
nlu.load("en.oncology_therpay.pipeline").predict("""The patient underwent a mastectomy two years ago. She is currently receiving her second cycle of adriamycin and cyclophosphamide, and is in good overall condition.""")
```
</div>

## Results

```bash
Results


"
******************** ner_oncology_wip results ********************

| chunk            | ner_label      |
|:-----------------|:---------------|
| mastectomy       | Cancer_Surgery |
| second cycle     | Cycle_Number   |
| adriamycin       | Chemotherapy   |
| cyclophosphamide | Chemotherapy   |


******************** ner_oncology_wip results ********************

| chunk            | ner_label      |
|:-----------------|:---------------|
| mastectomy       | Cancer_Surgery |
| second cycle     | Cycle_Number   |
| adriamycin       | Chemotherapy   |
| cyclophosphamide | Chemotherapy   |


******************** ner_oncology_wip results ********************

| chunk            | ner_label      |
|:-----------------|:---------------|
| mastectomy       | Cancer_Surgery |
| second cycle     | Cycle_Number   |
| adriamycin       | Cancer_Therapy |
| cyclophosphamide | Cancer_Therapy |


******************** ner_oncology_unspecific_posology_wip results ********************

| chunk            | ner_label            |
|:-----------------|:---------------------|
| mastectomy       | Cancer_Therapy       |
| second cycle     | Posology_Information |
| adriamycin       | Cancer_Therapy       |
| cyclophosphamide | Cancer_Therapy       |


******************** assertion_oncology_wip results ********************

| chunk            | ner_label      | assertion   |
|:-----------------|:---------------|:------------|
| mastectomy       | Cancer_Surgery | Past        |
| adriamycin       | Chemotherapy   | Present     |
| cyclophosphamide | Chemotherapy   | Present     |


******************** assertion_oncology_treatment_binary_wip results ********************

| chunk            | ner_label      | assertion       |
|:-----------------|:---------------|:----------------|
| mastectomy       | Cancer_Surgery | Present_Or_Past |
| adriamycin       | Chemotherapy   | Present_Or_Past |
| cyclophosphamide | Chemotherapy   | Present_Or_Past |



{:.model-param}
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|oncology_therapy_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- ChunkMergeModel
- ChunkMergeModel
- AssertionDLModel
- AssertionDLModel