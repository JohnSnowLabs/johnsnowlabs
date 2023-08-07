---
layout: model
title: Sound Medical Classification Pipeline - Voice of the Patient
author: John Snow Labs
name: bert_sequence_classifier_vop_sound_medical_pipeline
date: 2023-06-22
tags: [licensed, en, clinical, classification, vop]
task: Text Classification
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

This pretrained pipeline includes the Medical Bert for Sequence Classification model to identify whether the suggestion that is mentioned in the text is medically sound. The pipeline is built on the top of  [bert_sequence_classifier_vop_sound_medical](https://nlp.johnsnowlabs.com/2023/06/13/bert_sequence_classifier_vop_sound_medical_en.html) model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_sound_medical_pipeline_en_4.4.4_3.0_1687411348291.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_sound_medical_pipeline_en_4.4.4_3.0_1687411348291.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("bert_sequence_classifier_vop_sound_medical_pipeline", "en", "clinical/models")

pipeline.annotate("I had a lung surgery for emphyema and after surgery my xray showing some recovery.")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("bert_sequence_classifier_vop_sound_medical_pipeline", "en", "clinical/models")

val result = pipeline.annotate(I had a lung surgery for emphyema and after surgery my xray showing some recovery.)
```
</div>

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("bert_sequence_classifier_vop_sound_medical_pipeline", "en", "clinical/models")

pipeline.annotate("I had a lung surgery for emphyema and after surgery my xray showing some recovery.")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("bert_sequence_classifier_vop_sound_medical_pipeline", "en", "clinical/models")

val result = pipeline.annotate(I had a lung surgery for emphyema and after surgery my xray showing some recovery.)
```
</div>

## Results

```bash
Results


| text                                                                               | prediction   |
|:-----------------------------------------------------------------------------------|:-------------|
| I had a lung surgery for emphyema and after surgery my xray showing some recovery. | True         |


{:.model-param}
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_vop_sound_medical_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|406.4 MB|

## Included Models

- DocumentAssembler
- TokenizerModel
- MedicalBertForSequenceClassification