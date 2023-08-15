---
layout: model
title: Image Text Detector based on the Craft with Refiner
author: John Snow Labs
name: image_text_detector_opt
date: 2023-08-15
tags: [en, licensed]
task: OCR Text Detection & Recognition
language: en
edition: Visual NLP 4.4.0
spark_version: 3.0
supported: true
annotator: ImageTextDetectorCraft
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

CRAFT: Character-Region Awareness For Text detection, is designed with a convolutional neural network producing the character region score and affinity score. The region score is used to localize individual characters in the image, and the affinity score is used to group each character into a single instance. To compensate for the lack of character-level annotations, we propose a weakly supervised learning framework that estimates character level ground truths in existing real word-level datasets.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/image_text_detector_opt_en_4.4.0_3.0_1692096077487.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/image_text_detector_opt_en_4.4.0_3.0_1692096077487.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

text_detector = ImageTextDetector.pretrained("image_text_detector_opt", "en", "clinical/ocr")
text_detector.setInputCol("image")
text_detector.setOutputCol("text_regions")

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
text_detector = ImageTextDetector.pretrained("image_text_detector_opt", "en", "clinical/ocr")
text_detector.setInputCol("image")
text_detector.setOutputCol("text_regions")
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|image_text_detector_opt|
|Type:|ocr|
|Compatibility:|Visual NLP 4.4.0+|
|License:|Licensed|
|Edition:|Official|
|Output Labels:|[text_regions]|
|Language:|en|
|Size:|79.5 MB|