---
layout: model
title: NER Pipeline for Treatments - Voice of the Patient
author: John Snow Labs
name: ner_vop_treatment_pipeline
date: 2023-06-22
tags: [licensed, ner, en, vop, treatment, clinical, pipeline]
task: Named Entity Recognition
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

This pipeline extracts mentions of treatment entities from health-related text in colloquial language.

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOP/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/VOICE_OF_PATIENT.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_treatment_pipeline_en_4.4.4_3.4_1687446331084.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_treatment_pipeline_en_4.4.4_3.4_1687446331084.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_vop_treatment_pipeline", "en", "clinical/models")

pipeline.annotate("
My grandpa was diagnosed with type 2 diabetes and had to make some changes to his lifestyle. He also takes metformin and glipizide to help regulate his blood sugar levels. It's been a bit of an adjustment, but he's doing well.
")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_vop_treatment_pipeline", "en", "clinical/models")

val result = pipeline.annotate("
My grandpa was diagnosed with type 2 diabetes and had to make some changes to his lifestyle. He also takes metformin and glipizide to help regulate his blood sugar levels. It's been a bit of an adjustment, but he's doing well.
")
```
</div>


## Results

```bash
| chunk     | ner_label   |
|:----------|:------------|
| metformin | Drug        |
| glipizide | Drug        |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_treatment_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|791.6 MB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
