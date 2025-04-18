---
layout: model
title: Pipeline to Detect Adverse Drug Events
author: John Snow Labs
name: ner_ade_clinical_pipeline
date: 2022-03-21
tags: [licensed, ner, clinical, en]
task: Named Entity Recognition
language: en
nav_key: models
edition: Healthcare NLP 3.4.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_ade_clinical](https://nlp.johnsnowlabs.com/2021/04/01/ner_ade_clinical_en.html) model.

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ADE/){:.button.button-orange}{:target="_blank"}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings_JSL/Healthcare/16.Adverse_Drug_Event_ADE_NER_and_Classifier.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_ade_clinical_pipeline_en_3.4.1_3.0_1647874530624.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_ade_clinical_pipeline_en_3.4.1_3.0_1647874530624.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
pipeline = PretrainedPipeline("ner_ade_clinical_pipeline", "en", "clinical/models")


pipeline.annotate("Been taking Lipitor for 15 years, have experienced severe fatigue a lot!!!. Doctor moved me to voltaren 2 months ago, so far, have only experienced cramps")
```
```scala
val pipeline = new PretrainedPipeline("ner_ade_clinical_pipeline", "en", "clinical/models")


pipeline.annotate("Been taking Lipitor for 15 years, have experienced severe fatigue a lot!!!. Doctor moved me to voltaren 2 months ago, so far, have only experienced cramps")
```


{:.nlu-block}
```python
import nlu
nlu.load("en.med_ner.ade_clinical.pipeline").predict("""Been taking Lipitor for 15 years, have experienced severe fatigue a lot!!!. Doctor moved me to voltaren 2 months ago, so far, have only experienced cramps""")
```

</div>

## Results

```bash
+--------------+---------+
|chunk         |ner_label|
+--------------+---------+
|Lipitor       |DRUG     |
|severe fatigue|ADE      |
|voltaren      |DRUG     |
|cramps        |ADE      |
+--------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_ade_clinical_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 3.4.1+|
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
