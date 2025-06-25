---
layout: model
title: Pipeline for Extracting Clinical Entities Related to UMLS CUI Codes
author: John Snow Labs
name: ner_umls_clinical_findings_pipeline
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

This pipeline is designed to extract all entities mappable to UMLS CUI codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_umls_clinical_findings_pipeline_en_6.0.2_3.4_1750861841492.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_umls_clinical_findings_pipeline_en_6.0.2_3.4_1750861841492.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_umls_clinical_findings_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""HTG-induced pancreatitis associated with an acute hepatitis, and obesity.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_umls_clinical_findings_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""HTG-induced pancreatitis associated with an acute hepatitis, and obesity.""")

```
</div>

## Results

```bash
|    | chunks                   |   begin |   end | entities   |
|---:|:-------------------------|--------:|------:|:-----------|
|  0 | HTG-induced pancreatitis |       1 |    24 | PROBLEM    |
|  1 | an acute hepatitis       |      42 |    59 | PROBLEM    |
|  2 | obesity                  |      66 |    72 | PROBLEM    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_umls_clinical_findings_pipeline|
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