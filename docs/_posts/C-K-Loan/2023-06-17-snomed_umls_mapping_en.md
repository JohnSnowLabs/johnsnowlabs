---
layout: model
title: Pipeline to Mapping SNOMED Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: snomed_umls_mapping
date: 2023-06-17
tags: [en, licensed, clinical, pipeline, chunk_mapping, snomed, umls]
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
  databricks_link: https://marketplace.databricks.com/details/83306cbb-ac15-46e4-86a1-43036dd0c1ec/John-Snow-Labs_SNOMED-to-UMLS-Code-Mapper

---

## Description

This pretrained pipeline is built on the top of `snomed_umls_mapper` model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_umls_mapping_en_4.4.4_3.0_1686979230684.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_umls_mapping_en_4.4.4_3.0_1686979230684.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

pipeline = PretrainedPipeline("snomed_umls_mapping", "en", "clinical/models")
result = pipeline.fullAnnotate(["733187009", "449433008", "51264003"])
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("snomed_umls_mapping", "en", "clinical/models")
val result = pipeline.fullAnnotate(["733187009", "449433008", "51264003"])
```


{:.nlu-block}
```python
import nlu
nlu.load("en.snomed.umls.mapping").predict("""Put your text here.""")
```

</div>

## Results

```bash
|   | snomed_code | umls_code |
|--:|------------:|----------:|
| 0 |   733187009 |  C4546029 |
| 1 |   449433008 |  C3164619 |
| 2 |    51264003 |  C0271267 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_umls_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|5.1 MB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ChunkMapperModel