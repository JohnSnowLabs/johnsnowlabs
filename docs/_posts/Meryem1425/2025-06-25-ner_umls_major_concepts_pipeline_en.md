---
layout: model
title: Pipeline for Extracting Clinical Entities Related to 4 major categories of UMLS CUI Codes
author: John Snow Labs
name: ner_umls_major_concepts_pipeline
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

This pipeline is designed to extract all entities mappable to 4 major categories of UMLS CUI codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_umls_major_concepts_pipeline_en_6.0.2_3.4_1750866489885.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_umls_major_concepts_pipeline_en_6.0.2_3.4_1750866489885.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_umls_major_concepts_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""A female patient got influenza vaccine and one day after she has complains of ankle pain. 
She has only history of gestational diabetes mellitus diagnosed prior to presentation and subsequent type two diabetes mellitus (T2DM).""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_umls_major_concepts_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""A female patient got influenza vaccine and one day after she has complains of ankle pain. 
She has only history of gestational diabetes mellitus diagnosed prior to presentation and subsequent type two diabetes mellitus (T2DM).""")

```
</div>

## Results

```bash
|    | chunks                        |   begin |   end | entities     |
|---:|:------------------------------|--------:|------:|:-------------|
|  0 | influenza vaccine             |      21 |    37 | Vaccine_Name |
|  1 | one day after                 |      43 |    55 | RelativeDate |
|  2 | ankle pain                    |      78 |    87 | Symptom      |
|  3 | gestational diabetes mellitus |     115 |   143 | Diabetes     |
|  4 | type two diabetes mellitus    |     192 |   217 | Diabetes     |
|  5 | T2DM                          |     220 |   223 | Diabetes     |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_umls_major_concepts_pipeline|
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