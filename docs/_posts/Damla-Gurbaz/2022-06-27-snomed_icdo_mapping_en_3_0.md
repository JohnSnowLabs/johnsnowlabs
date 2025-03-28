---
layout: model
title: Pipeline to Mapping SNOMED Codes with Their Corresponding ICDO Codes
author: John Snow Labs
name: snomed_icdo_mapping
date: 2022-06-27
tags: [snomed, icdo, pipeline, chunk_mapper, clinical, licensed, en]
task: Pipeline Healthcare
language: en
nav_key: models
edition: Healthcare NLP 3.5.3
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"

deploy:
  sagemaker_link: 
  snowflake_link: 
  databricks_link: https://marketplace.databricks.com/details/e3d2930b-b3bc-4f26-9d35-e81fa9fdd161/John-Snow-Labs_SNOMED-Codes-to-ICDO-Codes-Mapper

---

## Description

This pretrained pipeline is built on the top of `snomed_icdo_mapper` model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_icdo_mapping_en_3.5.3_3.0_1656364941154.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_icdo_mapping_en_3.5.3_3.0_1656364941154.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

pipeline = PretrainedPipeline("snomed_icdo_mapping", "en", "clinical/models")
result= pipeline.fullAnnotate(["10376009", "2026006", "26638004"])
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("snomed_icdo_mapping", "en", "clinical/models")

val result= pipeline.fullAnnotate(["10376009", "2026006", "26638004"])
```


{:.nlu-block}
```python
import nlu
nlu.load("en.map_entity.snomed_to_icdo.pipe").predict("""Put your text here.""")
```

</div>

## Results

```bash
|   | snomed_code | icdo_code |
|--:|------------:|----------:|
| 0 |    10376009 |    8050/2 |
| 1 |     2026006 |    9014/0 |
| 2 |    26638004 |    8322/0 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_icdo_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 3.5.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|208.7 KB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ChunkMapperModel
