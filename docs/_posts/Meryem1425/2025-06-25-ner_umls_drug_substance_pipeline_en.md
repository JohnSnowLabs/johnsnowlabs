---
layout: model
title: Pipeline for Extracting Clinical Entities Related to UMLS CUI (Drug & Substance) Codes
author: John Snow Labs
name: ner_umls_drug_substance_pipeline
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

This pipeline is designed to extract all entities mappable to UMLS CUI (Drug & Substance) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_umls_drug_substance_pipeline_en_6.0.2_3.4_1750865580389.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_umls_drug_substance_pipeline_en_6.0.2_3.4_1750865580389.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_umls_drug_substance_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient was given  metformin, lenvatinib and Magnesium hydroxide 100mg/1ml.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_umls_drug_substance_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient was given  metformin, lenvatinib and Magnesium hydroxide 100mg/1ml.""")

```
</div>

## Results

```bash
|    | chunks                        |   begin |   end | entities   |
|---:|:------------------------------|--------:|------:|:-----------|
|  0 | metformin                     |      24 |    32 | DRUG       |
|  1 | lenvatinib                    |      35 |    44 | DRUG       |
|  2 | Magnesium hydroxide 100mg/1ml |      50 |    78 | DRUG       |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_umls_drug_substance_pipeline|
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
- NerConverter
- TextMatcherInternalModel
- ChunkMergeModel