---
layout: model
title: Pipeline to Mapping RxNorm Codes with Corresponding National Drug Codes (NDC)
author: John Snow Labs
name: rxnorm_ndc_mapping
date: 2023-06-16
tags: [en, licensed, clinical, pipeline, chunk_mapping, rxnorm, ndc]
task: Chunk Mapping
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline maps RXNORM codes to NDC codes without using any text data. You’ll just feed white space-delimited RXNORM codes and it will return the corresponding two different types of ndc codes which are called `package ndc` and `product ndc`.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_ndc_mapping_en_4.4.4_3.4_1686933027116.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_ndc_mapping_en_4.4.4_3.4_1686933027116.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("rxnorm_ndc_mapping", "en", "clinical/models")

result = pipeline.fullAnnotate(1652674 259934)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("rxnorm_ndc_mapping", "en", "clinical/models")

val result = pipeline.fullAnnotate(1652674 259934)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.map_entity.rxnorm_to_ndc.pipe").predict("""Put your text here.""")
```

</div>



## Results

```bash
{'document': ['1652674 259934'],
'package_ndc': ['62135-0625-60', '13349-0010-39'],
'product_ndc': ['46708-0499', '13349-0010'],
'rxnorm_code': ['1652674', '259934']}
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