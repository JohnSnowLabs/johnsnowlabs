---
layout: model
title: Self Report Classification Pipeline - Voice of the Patient
author: John Snow Labs
name: bert_sequence_classifier_vop_self_report_pipeline
date: 2023-06-22
tags: [licensed, en, clinical, vop, classification]
task: Text Classification
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline includes the Medical Bert for Sequence Classification model to classify texts depending on if they are self-reported or if they refer to another person. The pipeline is built on the top of  [bert_sequence_classifier_vop_self_report](https://nlp.johnsnowlabs.com/2023/06/13/bert_sequence_classifier_vop_self_report_en.html) model.

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOP/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/VOICE_OF_PATIENT.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_self_report_pipeline_en_4.4.4_3.4_1687409754808.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_self_report_pipeline_en_4.4.4_3.4_1687409754808.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|406.4 MB|

## Included Models

- DocumentAssembler
- TokenizerModel
- MedicalBertForSequenceClassification
