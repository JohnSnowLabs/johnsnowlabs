---
layout: model
title: Pipeline to Mapping RxNORM Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: rxnorm_umls_mapping
date: 2023-06-13
tags: [en, licensed, clinical, pipeline, chunk_mapping, rxnorm, umls]
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

This pretrained pipeline is built on the top of `rxnorm_umls_mapper` model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_umls_mapping_en_4.4.4_3.2_1686663532119.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_umls_mapping_en_4.4.4_3.2_1686663532119.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("rxnorm_umls_mapping", "en", "clinical/models")

result = pipeline.fullAnnotate(1161611 315677)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("rxnorm_umls_mapping", "en", "clinical/models")

val result = pipeline.fullAnnotate(1161611 315677)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.rxnorm.umls.mapping").predict("""Put your text here.""")
```

</div>


## Results

```bash
|    | rxnorm_code      | umls_code           |
|---:|:-----------------|:--------------------|
|  0 | 1161611 | 315677 | C3215948 | C0984912 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxnorm_umls_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.9 MB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ChunkMapperModel