---
layout: model
title: Pipeline for Extracting Clinical Entities Related to UMLS CUI (Clinical Drug) Codes
author: John Snow Labs
name: ner_umls_clinical_drugs_pipeline
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

This pipeline is designed to extract all entities mappable to UMLS CUI (Clinical Drug) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_umls_clinical_drugs_pipeline_en_6.0.2_3.4_1750863770729.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_umls_clinical_drugs_pipeline_en_6.0.2_3.4_1750863770729.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_umls_clinical_drugs_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient was given Adapin 10 MG, coumadn 5 mg, Avandia 4 mg, Tegretol, zitiga.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_umls_clinical_drugs_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient was given Adapin 10 MG, coumadn 5 mg, Avandia 4 mg, Tegretol, zitiga.""")

```
</div>

## Results

```bash
|    | chunks       |   begin |   end | entities   |
|---:|:-------------|--------:|------:|:-----------|
|  0 | Adapin 10 MG |      23 |    34 | DRUG       |
|  1 | coumadn 5 mg |      37 |    48 | DRUG       |
|  2 | Avandia 4 mg |      51 |    62 | DRUG       |
|  3 | Tegretol     |      65 |    72 | DRUG       |
|  4 | zitiga       |      75 |    80 | DRUG       |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_umls_clinical_drugs_pipeline|
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