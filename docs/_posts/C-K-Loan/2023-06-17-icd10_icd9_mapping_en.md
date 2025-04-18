---
layout: model
title: Pipeline to Mapping ICD10-CM Codes with Their Corresponding ICD-9-CM Codes
author: John Snow Labs
name: icd10_icd9_mapping
date: 2023-06-17
tags: [en, licensed, icd10cm, icd9, pipeline, chunk_mapping]
task: Chunk Mapping
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"

deploy:
  sagemaker_link: 
  snowflake_link: 
  databricks_link: https://marketplace.databricks.com/details/5c645046-e195-4164-a5f5-d3015a7f7647/John-Snow-Labs_ICD10-to-ICD9-Code-Converter

---

## Description

This pretrained pipeline is built on the top of `icd10_icd9_mapper` model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10_icd9_mapping_en_4.4.4_3.0_1686979254089.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10_icd9_mapping_en_4.4.4_3.0_1686979254089.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

{% if page.deploy %}
## Available as Private API Endpoint

{:.tac}
{% include display_platform_information.html %}
{% endif %}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("icd10_icd9_mapping", "en", "clinical/models")
result = pipeline.fullAnnotate(["Z833", "A0100", "A000"])
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("icd10_icd9_mapping", "en", "clinical/models")

val result = pipeline.fullAnnotate(["Z833", "A0100", "A000"])
```


{:.nlu-block}
```python
import nlu
nlu.load("en.icd10_icd9.mapping").predict("""Put your text here.""")
```

</div>



## Results

```bash
|   | icd10cm_code | icd9_code |
|--:|-------------:|----------:|
| 0 |         Z833 |      V180 |
| 1 |        A0100 |      0020 |
| 2 |         A000 |      0010 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10_icd9_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|593.6 KB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ChunkMapperModel