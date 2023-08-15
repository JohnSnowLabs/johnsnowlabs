---
layout: model
title: Image Text Detector DIT
author: John Snow Labs
name: image_text_detector_dit
date: 2023-08-15
tags: [en, licensed]
task: OCR Text Detection & Recognition
language: en
edition: Visual NLP 4.4.0
spark_version: 3.0
supported: true
annotator: ImageTextDetectorDit
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Image Text Detector based on DIT

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/image_text_detector_dit_en_4.4.0_3.0_1692086682871.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/image_text_detector_dit_en_4.4.0_3.0_1692086682871.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

text_detector = ImageTextDetector.pretrained("image_text-detector_dit", "en", "clinical/ocr")
text_detector.setInputCol("image")
text_detector.setOutputCol("text_regions")

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
text_detector = ImageTextDetector.pretrained("image_text-detector_dit", "en", "clinical/ocr")
text_detector.setInputCol("image")
text_detector.setOutputCol("text_regions")
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|image_text_detector_dit|
|Type:|ocr|
|Compatibility:|Visual NLP 4.4.0+|
|License:|Licensed|
|Edition:|Official|
|Output Labels:|[region]|
|Language:|en|
|Size:|420.6 MB|