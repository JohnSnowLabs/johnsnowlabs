---
layout: model
title: Pipeline for Extracting Clinical Entities Related to SNOMED Drug Codes
author: John Snow Labs
name: ner_snomed_drug_pipeline
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

This pipeline is designed to extract all entities mappable to SNOMED Drug codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_snomed_drug_pipeline_en_6.0.2_3.4_1750879440870.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_snomed_drug_pipeline_en_6.0.2_3.4_1750879440870.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_snomed_drug_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD on 2023-12-01.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_snomed_drug_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD on 2023-12-01.
""")

```
</div>

## Results

```bash
|    | chunks       |   begin |   end | entities   |
|---:|:-------------|--------:|------:|:-----------|
|  0 | aspirin      |      26 |    32 | DRUG       |
|  1 | paracetamol  |      70 |    80 | DRUG       |
|  2 | amoxicillin  |     110 |   120 | DRUG       |
|  3 | lansoprazole |     145 |   156 | DRUG       |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_snomed_drug_pipeline|
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
- TextMatcherInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel