---
layout: model
title: Pipeline to Mapping Entities (Disease or Syndrome) with Corresponding UMLS CUI Codes
author: John Snow Labs
name: umls_disease_syndrome_mapping
date: 2026-03-04
tags: [en, umls, disease_syndrome, mapping, licensed, clinical, chunk_mapper, pipeline]
task: [Chunk Mapping, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.3.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of umls_disease_syndrome_mapper model and maps entities (Disease or Syndrome) with corresponding UMLS CUI codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_disease_syndrome_mapping_en_6.3.0_3.4_1772648258116.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_disease_syndrome_mapping_en_6.3.0_3.4_1772648258116.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("umls_disease_syndrome_mapping", "en", "clinical/models")

sample_text = """ A 35-year-old male with a history of obesity and gestational diabetes mellitus and acyclovir allergy."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("umls_disease_syndrome_mapping", "en", "clinical/models")

sample_text = """ A 35-year-old male with a history of obesity and gestational diabetes mellitus and acyclovir allergy."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("umls_disease_syndrome_mapping", "en", "clinical/models")

val sample_text = """ A 35-year-old male with a history of obesity and gestational diabetes mellitus and acyclovir allergy."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk                         | umls_code |
| :---------------------------- | :-------- |
| obesity                       | C0028754  |
| gestational diabetes mellitus | C0085207  |
| acyclovir allergy             | C0571297  |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_disease_syndrome_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMapperModel