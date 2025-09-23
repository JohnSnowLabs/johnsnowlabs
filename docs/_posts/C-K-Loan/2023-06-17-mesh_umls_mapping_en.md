---
layout: model
title: Pipeline to Mapping MESH Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: mesh_umls_mapping
date: 2023-06-17
tags: [en, licensed, clinical, resolver, pipeline, chunk_mapping, mesh, umls]
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
  databricks_link: https://marketplace.databricks.com/details/5b4cc372-b9b5-4632-9090-89ddfbef7fe5/John-Snow-Labs_MeSH-to-UMLS-Code-Mapper

---

## Description

This pretrained pipeline is built on the top of `mesh_umls_mapper` model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.1.Code_Mapping_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/mesh_umls_mapping_en_4.4.4_3.0_1686979222270.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/mesh_umls_mapping_en_4.4.4_3.0_1686979222270.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

pipeline = PretrainedPipeline("mesh_umls_mapping", "en", "clinical/models")
result = pipeline.fullAnnotate(["C028491", "D019326", "C579867"])
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("mesh_umls_mapping", "en", "clinical/models")

val result = pipeline.fullAnnotate(["C028491", "D019326", "C579867"])
```


{:.nlu-block}
```python
import nlu
nlu.load("en.mesh.umls.mapping").predict("""Put your text here.""")
```

</div>



## Results

```bash
|   | mesh_code | umls_code |
|--:|----------:|----------:|
| 0 |   C028491 |  C0043904 |
| 1 |   D019326 |  C0045010 |
| 2 |   C579867 |  C3696376 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|mesh_umls_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.9 MB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ChunkMapperModel