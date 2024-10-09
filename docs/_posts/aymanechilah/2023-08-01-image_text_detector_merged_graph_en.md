---
layout: model
title: image_text_detector_merged_graph
author: John Snow Labs
name: image_text_detector_merged_graph
date: 2023-08-01
tags: [en, licensed]
task: OCR Text Detection & Recognition
language: en
edition: Visual NLP 4.4.0
spark_version: 3.2
supported: true
annotator: ImageTextDetector
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

image_text_detector_merged_graph

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/image_text_detector_merged_graph_en_4.4.0_3.2_1690884088029.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/image_text_detector_merged_graph_en_4.4.0_3.2_1690884088029.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
text_detector = ImageTextDetector \

    .load("spark_image_text_detector_merged_graph") \

    .setInputCol("image") \

    .setOutputCol("text_regions") \

    .setWidth(500) \

    .setHeight(0)
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|image_text_detector_merged_graph|
|Type:|ocr|
|Compatibility:|Visual NLP 4.4.0+|
|License:|Licensed|
|Edition:|Official|
|Output Labels:|[text_regions]|
|Language:|en|
|Size:|78.9 MB|