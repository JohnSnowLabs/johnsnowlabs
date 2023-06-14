---
layout: model
title: Self Report Classification Pipeline - Voice of the Patient
author: John Snow Labs
name: bert_sequence_classifier_vop_self_report_pipeline
date: 2023-06-14
tags: [licensed, en, clinical, vop, classification]
task: Text Classification
language: en
edition: Healthcare NLP 4.4.3
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline includes the Medical Bert for Sequence Classification model to classify texts depending on if they are self-reported or if they refer to another person.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_self_report_pipeline_en_4.4.3_3.2_1686702483761.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_self_report_pipeline_en_4.4.3_3.2_1686702483761.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("bert_sequence_classifier_vop_self_report_pipeline", "en", "clinical/models")

pipeline.annotate("My friend was treated for her skin cancer two years ago.")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("bert_sequence_classifier_vop_self_report_pipeline", "en", "clinical/models")

val result = pipeline.annotate(My friend was treated for her skin cancer two years ago.)
```
</div>

## Results

```bash
| text                                                     | prediction   |
|:---------------------------------------------------------|:-------------|
| My friend was treated for her skin cancer two years ago. | 3rd_Person   |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_vop_self_report_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|406.4 MB|

## Included Models

- DocumentAssembler
- TokenizerModel
- MedicalBertForSequenceClassification