---
layout: model
title: Pipeline to Mapping Entities (Drug Substances) with Corresponding UMLS CUI Codes
author: John Snow Labs
name: umls_drug_substance_mapping
date: 2026-03-03
tags: [en, umls, drug_substance, mapping, licensed, clinical, chunk_mapper, pipeline]
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

This pretrained pipeline is built on the top of umls_drug_substance_mapper model and maps entities (Drug Substances) with corresponding UMLS CUI codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_drug_substance_mapping_en_6.3.0_3.4_1772501358835.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_drug_substance_mapping_en_6.3.0_3.4_1772501358835.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("umls_drug_substance_mapping", "en", "clinical/models")

sample_text = """ The patient was given  metformin, lenvatinib and gallopamil 50 MG Oral Tablet."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("umls_drug_substance_mapping", "en", "clinical/models")

sample_text = """ The patient was given  metformin, lenvatinib and gallopamil 50 MG Oral Tablet."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("umls_drug_substance_mapping", "en", "clinical/models")

val sample_text = """ The patient was given  metformin, lenvatinib and gallopamil 50 MG Oral Tablet."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| ner_chunk                    | umls_code |
| :--------------------------- | :-------- |
| metformin                    | C0025598  |
| lenvatinib                   | C2986924  |
| gallopamil 50 MG Oral Tablet | C0787234  |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_drug_substance_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMapperModel