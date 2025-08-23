---
layout: model
title: Pipeline for Extracting Clinical Entities Related to SNOMED (Procedures and Measurements) Codes
author: John Snow Labs
name: ner_snomed_procedures_measurements_pipeline
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

This pipeline is designed to extract all entities mappable to SNOMED (Procedures and Measurements) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_snomed_procedures_measurements_pipeline_en_6.0.2_3.4_1750881546019.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_snomed_procedures_measurements_pipeline_en_6.0.2_3.4_1750881546019.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_snomed_procedures_measurements_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
Based on the severity of her abdominal examination and the persistence of her symptoms,
            it has been determined that she requires a laparoscopic jejunectomy, possible appendectomy, and
            cholecystectomy.Laboratory values indicate a white blood cell count of 15.3,
            hemoglobin level of 12.8, and normal platelet count. Alkaline phosphatase is elevated at 184,
            while liver function tests are otherwise normal. Electrolyte levels are within the normal range.
            Glucose levels are at 134, BUN is 4, and creatinine is 0.7.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_snomed_procedures_measurements_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
Based on the severity of her abdominal examination and the persistence of her symptoms,
            it has been determined that she requires a laparoscopic jejunectomy, possible appendectomy, and
            cholecystectomy.Laboratory values indicate a white blood cell count of 15.3,
            hemoglobin level of 12.8, and normal platelet count. Alkaline phosphatase is elevated at 184,
            while liver function tests are otherwise normal. Electrolyte levels are within the normal range.
            Glucose levels are at 134, BUN is 4, and creatinine is 0.7.
""")

```
</div>

## Results

```bash
|    | chunks                   |   begin |   end | entities   |
|---:|:-------------------------|--------:|------:|:-----------|
|  0 | laparoscopic jejunectomy |     144 |   167 | Procedure  |
|  1 | appendectomy             |     179 |   190 | Procedure  |
|  2 | cholecystectomy          |     209 |   223 | Procedure  |
|  3 | white blood cell count   |     254 |   275 | Test       |
|  4 | hemoglobin level         |     298 |   313 | Test       |
|  5 | platelet count           |     335 |   348 | Test       |
|  6 | Alkaline phosphatase     |     351 |   370 | Test       |
|  7 | liver function tests     |     410 |   429 | Test       |
|  8 | Electrolyte levels       |     453 |   470 | Test       |
|  9 | Glucose levels           |     513 |   526 | Test       |
| 10 | BUN                      |     540 |   542 | Test       |
| 11 | creatinine               |     554 |   563 | Test       |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_snomed_procedures_measurements_pipeline|
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