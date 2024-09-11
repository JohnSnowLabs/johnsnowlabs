---
layout: model
title: Visual Document Ner Geo V1
author: John Snow Labs
name: visual_ner_geo_v1
date: 2024-09-11
tags: [en, licensed]
task: Named Entity Recognition
language: en
edition: Visual NLP 5.0.0
spark_version: 3.0
supported: true
annotator: VisualDocumentNerGeo
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Visual Document Ner Geo V1

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/visual_ner_geo_v1_en_5.0.0_3.0_1726035025061.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/visual_ner_geo_v1_en_5.0.0_3.0_1726035025061.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

ner = VisualDocumentNerGeo().pretrained("visual_ner_geo_v1", "en", "clinical/ocr/") \
            .setInputCols(["features", "tokens", "image"]) \
            .setWhiteList(["other", "i-header", "b-header", "i-question", "b-question", "i-answer", "b-answer"]) \
            .setLabels(["other", "i-header", "b-header", "i-question", "b-question", "i-answer", "b-answer"]) \
            .setOutputCol("entities")

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
ner = VisualDocumentNerGeo().pretrained("visual_ner_geo_v1", "en", "clinical/ocr/") \
            .setInputCols(["features", "tokens", "image"]) \
            .setWhiteList(["other", "i-header", "b-header", "i-question", "b-question", "i-answer", "b-answer"]) \
            .setLabels(["other", "i-header", "b-header", "i-question", "b-question", "i-answer", "b-answer"]) \
            .setOutputCol("entities")
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|visual_ner_geo_v1|
|Type:|ocr|
|Compatibility:|Visual NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[features, tokens, image]|
|Output Labels:|[entities]|
|Language:|en|
|Size:|1.5 GB|