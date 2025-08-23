---
layout: model
title: Pipeline for Extracting Clinical Entities Related to SNOMED Conditions Codes
author: John Snow Labs
name: ner_snomed_conditions_pipeline
date: 2025-06-25
tags: [licensed, en, clinical, pipeline, ner]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to extract all entities mappable to SNOMED Conditions codes.

2 NER models are used to achieve those tasks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_snomed_conditions_pipeline_en_6.0.2_3.4_1750877903379.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_snomed_conditions_pipeline_en_6.0.2_3.4_1750877903379.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_snomed_conditions_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
Medical professionals rushed in the bustling emergency room to attend to the patient with distressed breathing.
The attending physician immediately noted signs of respiratory distress, including stridor, a high-pitched sound indicative of upper respiratory tract obstruction.
The patient, struggling to breathe, exhibited dyspnea. 
Concern raised when they began experiencing syncope, sudden loss of consciousness likely stemming from inadequate oxygenation. 
Further examination revealed a respiratory tract hemorrhage.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_snomed_conditions_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
Medical professionals rushed in the bustling emergency room to attend to the patient with distressed breathing.
The attending physician immediately noted signs of respiratory distress, including stridor, a high-pitched sound indicative of upper respiratory tract obstruction.
The patient, struggling to breathe, exhibited dyspnea. 
Concern raised when they began experiencing syncope, sudden loss of consciousness likely stemming from inadequate oxygenation. 
Further examination revealed a respiratory tract hemorrhage.
""")

```
</div>

## Results

```bash
|    | chunks                              |   begin |   end | entities                  |
|---:|:------------------------------------|--------:|------:|:--------------------------|
|  0 | distressed breathing                |      91 |   110 | Symptom                   |
|  1 | respiratory distress                |     164 |   183 | VS_Finding                |
|  2 | stridor                             |     196 |   202 | Symptom                   |
|  3 | a high-pitched sound                |     205 |   224 | PROBLEM                   |
|  4 | upper respiratory tract obstruction |     240 |   274 | Disease_Syndrome_Disorder |
|  5 | struggling to breathe               |     290 |   310 | Symptom                   |
|  6 | dyspnea                             |     323 |   329 | Symptom                   |
|  7 | syncope                             |     377 |   383 | Symptom                   |
|  8 | sudden loss of consciousness        |     386 |   413 | PROBLEM                   |
|  9 | inadequate oxygenation              |     436 |   457 | Symptom                   |
| 10 | a respiratory tract hemorrhage      |     490 |   519 | PROBLEM                   |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_snomed_conditions_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
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
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel