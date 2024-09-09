---
layout: model
title: Pipeline to Mapping RxNorm Codes with Corresponding National Drug Codes (NDC)
author: John Snow Labs
name: rxnorm_ndc_mapping
date: 2023-06-17
tags: [en, licensed, clinical, pipeline, chunk_mapping, rxnorm, ndc]
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
  databricks_link: https://marketplace.databricks.com/details/bf4cd2a7-55b5-40fa-b010-c89f54b29ab8/John-Snow-Labs_RxNorm-to-NDC-Code-Converter

---

## Description

This pretrained pipeline maps RXNORM codes to NDC codes without using any text data. You’ll just feed white space-delimited RXNORM codes and it will return the corresponding two different types of ndc codes which are called `package ndc` and `product ndc`.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_ndc_mapping_en_4.4.4_3.0_1686990370017.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_ndc_mapping_en_4.4.4_3.0_1686990370017.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

pipeline = PretrainedPipeline("rxnorm_ndc_mapping", "en", "clinical/models")
result = pipeline.fullAnnotate(["1652674", "259934"])
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("rxnorm_ndc_mapping", "en", "clinical/models")
val result = pipeline.fullAnnotate(["1652674", "259934"])
```


{:.nlu-block}
```python
import nlu
nlu.load("en.map_entity.rxnorm_to_ndc.pipe").predict("""Put your text here.""")
```

</div>


## Results

```bash
|   | rxnorm_code |   package_ndc | product_ndc |
|--:|------------:|--------------:|------------:|
| 0 |     1652674 | 62135-0625-60 |  46708-0499 |
| 1 |      259934 | 13349-0010-39 |  13349-0010 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxnorm_ndc_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.0 MB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ChunkMapperModel
- ChunkMapperModel