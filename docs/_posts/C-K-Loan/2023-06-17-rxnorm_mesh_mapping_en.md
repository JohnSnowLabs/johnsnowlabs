---
layout: model
title: RxNorm to MeSH Code Mapping
author: John Snow Labs
name: rxnorm_mesh_mapping
date: 2023-06-17
tags: [rxnorm, mesh, en, licensed, pipeline]
task: Pipeline Healthcare
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
  databricks_link: https://marketplace.databricks.com/details/b1a7c3ca-3d76-4434-a979-7ed9ad720530/John-Snow-Labs_RxNorm-to-MeSH-Code-Mapper

---

## Description

This pretrained pipeline maps RxNorm codes to MeSH codes without using any text data. You’ll just feed white space-delimited RxNorm codes and it will return the corresponding MeSH codes as a list. If there is no mapping, the original code is returned with no mapping.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_mesh_mapping_en_4.4.4_3.0_1686979224907.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_mesh_mapping_en_4.4.4_3.0_1686979224907.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

pipeline = PretrainedPipeline("rxnorm_mesh_mapping","en","clinical/models")
result = pipeline.fullAnnotate(["1191", "6809", "47613"])
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("rxnorm_mesh_mapping","en","clinical/models")
val result = pipeline.annotate(["1191", "6809", "47613"])
```


{:.nlu-block}
```python
import nlu
nlu.load("en.resolve.rxnorm.mesh").predict("""Put your text here.""")
```

</div>


## Results

```bash
|   | rxnorm | mesh_code |
|--:|-------:|----------:|
| 0 |   1191 |   D001241 |
| 1 |   6809 |   D008687 |
| 2 |  47613 |   D019355 |


Note: 

| RxNorm     | Details             | 
| ---------- | -------------------:|
| 1191       | aspirin             |
| 6809       | metformin           |
| 47613      | calcium citrate     |

| MeSH       | Details             |
| ---------- | -------------------:|
| D001241    | Aspirin             |
| D008687    | Metformin           |
| D019355    | Calcium Citrate     |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxnorm_mesh_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|104.0 KB|

## Included Models

- DocumentAssembler
- TokenizerModel
- LemmatizerModel
- Finisher