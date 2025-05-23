---
layout: model
title: NER Pipeline for Clinical Department - Voice of the Patient
author: John Snow Labs
name: ner_vop_clinical_dept_pipeline
date: 2023-06-10
tags: [licensed, ner, en, vop, pipeline]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.3
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts mentions of clinical departments and medical devices from health-related text in colloquial language.

## Predicted Entities

`AdmissionDischarge`, `ClinicalDept`, `MedicalDevice`


{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOP/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/VOICE_OF_PATIENT.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_clinical_dept_pipeline_en_4.4.3_3.0_1686406177343.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_clinical_dept_pipeline_en_4.4.3_3.0_1686406177343.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_vop_clinical_dept_pipeline", "en", "clinical/models")

pipeline.annotate("
My little brother is having surgery tomorrow in the orthopedic department. He is getting a titanium plate put in his leg to help it heal faster. Wishing him a speedy recovery!
")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_vop_clinical_dept_pipeline", "en", "clinical/models")

val result = pipeline.annotate("
My little brother is having surgery tomorrow in the orthopedic department. He is getting a titanium plate put in his leg to help it heal faster. Wishing him a speedy recovery!
")
```
</div>

## Results

```bash
| chunk                 | ner_label     |
|:----------------------|:--------------|
| orthopedic department | ClinicalDept  |
| titanium plate        | MedicalDevice |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_clinical_dept_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|791.7 MB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
