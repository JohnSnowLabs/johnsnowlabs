---
layout: model
title: Pipeline to Detect Clinical Events (Admissions)
author: John Snow Labs
name: ner_events_admission_clinical_pipeline
date: 2023-06-16
tags: [ner, clinical, licensed, en]
task: Named Entity Recognition
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

This pretrained pipeline is built on the top of [ner_events_admission_clinical](https://nlp.johnsnowlabs.com/2021/03/31/ner_events_admission_clinical_en.html) model.

## Predicted Entities

`ADMISSION`, `CLINICAL_DEPT`, `DATE`, `DISCHARGE`, `DURATION`, `EVIDENTIAL`, `FREQUENCY`, `OCCURRENCE`, `PROBLEM`, `TEST`, `TIME`, `TREATMENT`



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_events_admission_clinical_pipeline_en_4.4.4_3.2_1686949951027.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_events_admission_clinical_pipeline_en_4.4.4_3.2_1686949951027.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_events_admission_clinical_pipeline", "en", "clinical/models")

text = '''The patient presented to the emergency room last evening.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_events_admission_clinical_pipeline", "en", "clinical/models")

val text = "The patient presented to the emergency room last evening."

val result = pipeline.fullAnnotate(text)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.med_ner.events_admission_clinical.pipeline").predict("""The patient presented to the emergency room last evening.""")
```

</div>


## Results

```bash
|    | ner_chunk          |   begin |   end | ner_label     |   confidence |
|---:|:-------------------|--------:|------:|:--------------|-------------:|
|  0 | presented          |      12 |    20 | OCCURRENCE    |       0.6219 |
|  1 | the emergency room |      25 |    42 | CLINICAL_DEPT |       0.812  |
|  2 | last evening       |      44 |    55 | TIME          |       0.9534 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_events_admission_clinical_pipeline|
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