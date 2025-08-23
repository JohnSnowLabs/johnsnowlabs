---
layout: model
title: Pipeline for Extracting Clinical Entities Related to SNOMED (Clinical Findings) Codes
author: John Snow Labs
name: ner_snomed_findings_pipeline
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

This pipeline is designed to extract all entities mappable to SNOMED (Clinical Findings) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_snomed_findings_pipeline_en_6.0.2_3.4_1750880775412.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_snomed_findings_pipeline_en_6.0.2_3.4_1750880775412.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_snomed_findings_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
The patient exhibited recurrent upper respiratory tract infections, fever, unintentional weight loss, and occasional night sweats. 
Clinically, they appeared cachectic and pale, with notable hepatosplenomegaly. Laboratory results confirmed pancytopenia.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_snomed_findings_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
The patient exhibited recurrent upper respiratory tract infections, fever, unintentional weight loss, and occasional night sweats. 
Clinically, they appeared cachectic and pale, with notable hepatosplenomegaly. Laboratory results confirmed pancytopenia.
""")

```
</div>

## Results

```bash
|    | chunks                                       |   begin |   end | entities   |
|---:|:---------------------------------------------|--------:|------:|:-----------|
|  0 | recurrent upper respiratory tract infections |      23 |    66 | PROBLEM    |
|  1 | fever                                        |      69 |    73 | PROBLEM    |
|  2 | unintentional weight loss                    |      76 |   100 | PROBLEM    |
|  3 | occasional night sweats                      |     107 |   129 | PROBLEM    |
|  4 | cachectic                                    |     159 |   167 | PROBLEM    |
|  5 | pale                                         |     173 |   176 | PROBLEM    |
|  6 | notable hepatosplenomegaly                   |     184 |   209 | PROBLEM    |
|  7 | pancytopenia                                 |     241 |   252 | PROBLEM    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_snomed_findings_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel