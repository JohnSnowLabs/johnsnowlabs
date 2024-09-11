---
layout: model
title: Visual Document Relation Extraction Geo V1
author: John Snow Labs
name: visual_re_geo_v1
date: 2024-09-11
tags: [en, licensed]
task: Relation Extraction
language: en
edition: Visual NLP 5.0.0
spark_version: 3.0
supported: true
annotator: GeoRelationExtractor
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Visual Document Relation Extraction Geo V1

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/visual_re_geo_v1_en_5.0.0_3.0_1726037999844.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/visual_re_geo_v1_en_5.0.0_3.0_1726037999844.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

re = GeoRelationExtractor().pretrained("visual_re_geo_v1", "en", "clinical/ocr/") \
            .setInputCols(["features", "entities", "image"]) \
            .setLabels(["other", "i-header", "b-header", "i-question", "b-question", "i-answer", "b-answer"]) \
            .setOutputCol("relations")

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
re = GeoRelationExtractor().pretrained("visual_re_geo_v1", "en", "clinical/ocr/") \
            .setInputCols(["features", "entities", "image"]) \
            .setLabels(["other", "i-header", "b-header", "i-question", "b-question", "i-answer", "b-answer"]) \
            .setOutputCol("relations")
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|visual_re_geo_v1|
|Type:|ocr|
|Compatibility:|Visual NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[hocr, image]|
|Output Labels:|[entities]|
|Language:|en|
|Size:|1.5 GB|