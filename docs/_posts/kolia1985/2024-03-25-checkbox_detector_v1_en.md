---
layout: model
title: Check Box Detector
author: John Snow Labs
name: checkbox_detector_v1
date: 2024-03-25
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

Check Box Detector

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/checkbox_detector_v1_en_5.0.0_3.0_1711346758339.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/checkbox_detector_v1_en_5.0.0_3.0_1711346758339.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
    checkBoxDetector = ImageCheckBoxDetector \
      .pretrained("checkbox_detector_v1") \
      .setInputCol("image") \
      .setOutputCol("hocr") \
      .setOutputFormat(DetectorOutputFormat.HOCR)
```
```scala
    val checkBoxDetector = ImageCheckBoxDetector
      .pretrained("checkbox_detector_v1")
      .setInputCol("image")
      .setOutputCol("hocr")
      .setOutputFormat(DetectorOutputFormat.HOCR)
```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|checkbox_detector_v1|
|Type:|ocr|
|Compatibility:|Visual NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Output Labels:|[regions]|
|Language:|en|
|Size:|278.7 MB|