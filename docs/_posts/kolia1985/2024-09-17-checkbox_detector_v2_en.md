---
layout: model
title: Checkbox Detector v2
author: John Snow Labs
name: checkbox_detector_v2
date: 2024-09-17
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

Checkbox Detector v2

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/checkbox_detector_v2_en_5.0.0_3.0_1726554881547.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/checkbox_detector_v2_en_5.0.0_3.0_1726554881547.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

checkBoxDetector = ImageCheckBoxDetector() \
    .pretrained("checkbox_detector_v2", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setLabels(["no", "yes"]) \
    .setOutputLabels(["no", "yes"]) \
    .setScoreThreshold(0.1) \
    .setOutputCol("check_box")  \
    .setMargin(-5) \
    .setOutputFormat(DetectorOutputFormat.REGIONS)

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
checkBoxDetector = ImageCheckBoxDetector() \
    .pretrained("checkbox_detector_v2", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setLabels(["no", "yes"]) \
    .setOutputLabels(["no", "yes"]) \
    .setScoreThreshold(0.1) \
    .setOutputCol("check_box")  \
    .setMargin(-5) \
    .setOutputFormat(DetectorOutputFormat.REGIONS)
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|checkbox_detector_v2|
|Type:|ocr|
|Compatibility:|Visual NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Output Labels:|[regions]|
|Language:|en|
|Size:|24.2 MB|