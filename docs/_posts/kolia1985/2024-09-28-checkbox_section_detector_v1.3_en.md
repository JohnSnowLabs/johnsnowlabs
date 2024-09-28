---
layout: model
title: Checkbox section detector v1.3
author: John Snow Labs
name: checkbox_section_detector_v1.3
date: 2024-09-28
tags: [en, licensed]
task: OCR Object Detection
language: en
edition: Visual NLP 5.0.0
spark_version: 3.0
supported: true
annotator: ImageCheckBoxDetector
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Checkbox section detector v1.3

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/checkbox_section_detector_v1.3_en_5.0.0_3.0_1727532417259.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/checkbox_section_detector_v1.3_en_5.0.0_3.0_1727532417259.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

regionDetector = ImageCheckBoxDetector \
    .pretrained("checkbox_section_detector_v1.3", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setLabels(["A", "B", "C", "D"]) \
    .setOutputLabels(["A"]) \
    .setScoreThreshold(0.7) \
    .setOutputCol("regions")  \
    .setMargin(20) \
    .setOutputFormat(DetectorOutputFormat.REGIONS)

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
regionDetector = ImageCheckBoxDetector \
    .pretrained("checkbox_section_detector_v1.3", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setLabels(["A", "B", "C", "D"]) \
    .setOutputLabels(["A"]) \
    .setScoreThreshold(0.7) \
    .setOutputCol("regions")  \
    .setMargin(20) \
    .setOutputFormat(DetectorOutputFormat.REGIONS)
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|checkbox_section_detector_v1.3|
|Type:|ocr|
|Compatibility:|Visual NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Output Labels:|[regions]|
|Language:|en|
|Size:|37.7 MB|