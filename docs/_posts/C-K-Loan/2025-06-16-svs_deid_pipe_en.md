---
layout: model
title: SVS DEID
author: John Snow Labs
name: svs_deid_pipe
date: 2025-06-16
tags: [en, licensed]
task: De-identification
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

SVS DEID

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/svs_deid_pipe_en_5.5.0_3.4_1750039413709.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/svs_deid_pipe_en_5.5.0_3.4_1750039413709.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
SVS DEID
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|svs_deid_pipe|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|

## Included Models

- BinaryToImage
- ImageTextDetectorCraft
- ImageToTextV2
- DocumentAssembler
- DocumentNormalizer
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- RegexMatcherModel
- ChunkConverter
- NerConverterInternalModel
- ChunkMergeModel
- PositionFinder
- ImageDrawRegions