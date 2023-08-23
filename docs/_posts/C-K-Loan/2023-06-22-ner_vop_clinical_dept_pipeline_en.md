---
layout: model
title: NER Pipeline for Clinical Department - Voice of the Patient
author: John Snow Labs
name: ner_vop_clinical_dept_pipeline
date: 2023-06-22
tags: [licensed, ner, en, vop, pipeline]
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

This pipeline extracts mentions of clinical departments and medical devices from health-related text in colloquial language.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_clinical_dept_pipeline_en_4.4.4_3.4_1687433807703.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_clinical_dept_pipeline_en_4.4.4_3.4_1687433807703.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
Results


| chunk                 | ner_label     |
|:----------------------|:--------------|
| orthopedic department | ClinicalDept  |
| titanium plate        | MedicalDevice |


{:.model-param}
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_clinical_dept_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
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