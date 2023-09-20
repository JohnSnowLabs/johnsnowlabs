---
layout: model
title: HCP Consult Classification Pipeline - Voice of the Patient
author: John Snow Labs
name: bert_sequence_classifier_vop_hcp_consult_pipeline
date: 2023-06-21
tags: [licensed, en, clinical, classification, vop]
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

This pretrained pipeline includes the Medical Bert for Sequence Classification model to identify texts that mention a HCP consult. The pipeline is built on the top of  [bert_sequence_classifier_vop_hcp_consult](https://nlp.johnsnowlabs.com/2023/06/13/bert_sequence_classifier_vop_hcp_consult_en.html) model.

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOP/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/VOICE_OF_PATIENT.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_hcp_consult_pipeline_en_4.4.4_3.4_1687379867981.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_hcp_consult_pipeline_en_4.4.4_3.4_1687379867981.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("bert_sequence_classifier_vop_hcp_consult_pipeline", "en", "clinical/models")

pipeline.annotate("My son has been to two doctors who gave him antibiotic drops but they also say the problem might related to allergies.")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("bert_sequence_classifier_vop_hcp_consult_pipeline", "en", "clinical/models")

val result = pipeline.annotate(My son has been to two doctors who gave him antibiotic drops but they also say the problem might related to allergies.)
```
</div>


## Results

```bash
| text                                                                                                                   | prediction       |
|:-----------------------------------------------------------------------------------------------------------------------|:-----------------|
| My son has been to two doctors who gave him antibiotic drops but they also say the problem might related to allergies. | Consulted_By_HCP |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_vop_hcp_consult_pipeline|
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
