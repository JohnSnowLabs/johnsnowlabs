---
layout: model
title: Text detection v4
author: John Snow Labs
name: text_detection_v4
date: 2026-04-02
tags: [en, licensed]
task: OCR Text Detection & Recognition
language: en
edition: Visual NLP 6.3.1
spark_version: 3.0
supported: true
annotator: ImageTextDetectorCraft
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

New text detection model for Craft based detectors

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/text_detection_v4_en_6.3.1_3.0_1775150706476.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/text_detection_v4_en_6.3.1_3.0_1775150706476.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
        text_detector = ImageTextDetectorCraft \
            .pretrained("text_detection_v4", "en", "clinical/ocr") \
            .setInputCol("image") \
            .setOutputCol("regions") \
            .setSizeThreshold(10) \
            .setLinkThreshold(0.3) \
            .setTextThreshold(0.4) \
            .setWithRefiner(False) \
            .setUseGPU(False)
```
```scala
    val textDetector = ImageTextDetectorCraft
      .pretrained("text_detection_v4", "en", "clinical/ocr")
      .setInputCol("image")
      .setOutputCol("regions")
      .setSizeThreshold(10)
      .setLinkThreshold(0.3)
      .setTextThreshold(0.4)
      .setWithRefiner(false)
```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|text_detection_v4|
|Type:|ocr|
|Compatibility:|Visual NLP 6.3.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|77.1 MB|