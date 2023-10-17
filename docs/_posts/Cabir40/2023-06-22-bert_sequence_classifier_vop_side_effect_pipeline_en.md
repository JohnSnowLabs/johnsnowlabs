---
layout: model
title: Side Effect Classification Pipeline - Voice of the Patient
author: John Snow Labs
name: bert_sequence_classifier_vop_side_effect_pipeline
date: 2023-06-22
tags: [pipeline, classification, side_effect, vop, clinical, en, licensed]
task: Text Classification
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

This pretrained pipeline includes the Medical Bert for Sequence Classification model to classify health-related text in colloquial language according to the presence or absence of mentions of side effects. The pipeline is built on the top of [bert_sequence_classifier_vop_side_effect](https://nlp.johnsnowlabs.com/2023/05/24/bert_sequence_classifier_vop_side_effect_en.html) model.

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOP/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/VOICE_OF_PATIENT.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_side_effect_pipeline_en_4.4.4_3.2_1687410712057.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_side_effect_pipeline_en_4.4.4_3.2_1687410712057.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

This pipeline includes the Medical Bert for Sequence Classification model to classify health-related text in colloquial language according to the presence or absence of mentions of side effects.

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("bert_sequence_classifier_vop_side_effect_pipeline", "en", "clinical/models")

pipeline.annotate("I felt kind of dizzy after taking that medication for a month.")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("bert_sequence_classifier_vop_side_effect_pipeline", "en", "clinical/models")

val result = pipeline.annotate(I felt kind of dizzy after taking that medication for a month.)
```
</div>


## Results

```bash

| text                                                           | prediction   |
|:---------------------------------------------------------------|:-------------|
| I felt kind of dizzy after taking that medication for a month. | True         |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_vop_side_effect_pipeline|
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
