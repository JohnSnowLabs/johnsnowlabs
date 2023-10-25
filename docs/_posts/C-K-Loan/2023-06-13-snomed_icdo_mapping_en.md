---
layout: model
title: Pipeline to Mapping SNOMED Codes with Their Corresponding ICDO Codes
author: John Snow Labs
name: snomed_icdo_mapping
date: 2023-06-13
tags: [en, licensed, clinical, pipeline, chunk_mapping, snomed, icdo]
task: Chunk Mapping
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of `snomed_icdo_mapper` model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_icdo_mapping_en_4.4.4_3.2_1686665539427.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_icdo_mapping_en_4.4.4_3.2_1686665539427.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("snomed_icdo_mapping", "en", "clinical/models")

result = pipeline.fullAnnotate(10376009 2026006 26638004)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("snomed_icdo_mapping", "en", "clinical/models")

val result = pipeline.fullAnnotate(10376009 2026006 26638004)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.map_entity.snomed_to_icdo.pipe").predict("""Put your text here.""")
```

</div>


## Results

```bash
|    | snomed_code                   | icdo_code                |
|---:|:------------------------------|:-------------------------|
|  0 | 10376009 | 2026006 | 26638004 | 8050/2 | 9014/0 | 8322/0 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_icdo_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|212.8 KB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ChunkMapperModel