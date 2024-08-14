---
layout: model
title: Checkbox section detector V1
author: John Snow Labs
name: checkbox_section_detector_v1
date: 2024-08-14
tags: [en, licensed]
task: OCR Object Detection
language: en
edition: Visual NLP 5.0.0
spark_version: 3.0
supported: true
annotator: ImageTableDetector
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Model detects  sections with check-boxes on the image document.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/checkbox_section_detector_v1_en_5.0.0_3.0_1723630949985.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/checkbox_section_detector_v1_en_5.0.0_3.0_1723630949985.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

binary_to_image = BinaryToImage() \
    .setImageType(ImageType.TYPE_3BYTE_BGR)

check_box_detector = ImageCheckBoxDetector \
    .pretrained("checkbox_section_detector_v1", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setLabels(["No", "Yes"]) \
    .setOutputLabels(["No", "Yes"]) \
    .setScoreThreshold(0.1) \
    .setOutputCol("regions") \
    .setOutputFormat(DetectorOutputFormat.REGIONS)

draw_regions = ImageDrawRegions() \
    .setInputCol("image") \
    .setInputRegionsCol("regions") \
    .setOutputCol("image_with_regions") \
    .setRectColor(Color.green) \
    .setRotated(False)

pipeline = PipelineModel(stages=[
    binary_to_image,
    check_box_detector,
    draw_regions
])

imagePath = 'cboxes.png'
image_df = spark.read.format("binaryFile").load(imagePath).sort("path")

result = pipeline.transform(image_df)

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
binary_to_image = BinaryToImage() \
    .setImageType(ImageType.TYPE_3BYTE_BGR)

check_box_detector = ImageCheckBoxDetector \
    .pretrained("checkbox_section_detector_v1", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setLabels(["No", "Yes"]) \
    .setOutputLabels(["No", "Yes"]) \
    .setScoreThreshold(0.1) \
    .setOutputCol("regions") \
    .setOutputFormat(DetectorOutputFormat.REGIONS)

draw_regions = ImageDrawRegions() \
    .setInputCol("image") \
    .setInputRegionsCol("regions") \
    .setOutputCol("image_with_regions") \
    .setRectColor(Color.green) \
    .setRotated(False)

pipeline = PipelineModel(stages=[
    binary_to_image,
    check_box_detector,
    draw_regions
])

imagePath = 'cboxes.png'
image_df = spark.read.format("binaryFile").load(imagePath).sort("path")

result = pipeline.transform(image_df)
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|checkbox_section_detector_v1|
|Type:|ocr|
|Compatibility:|Visual NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Output Labels:|[regions]|
|Language:|en|
|Size:|10.5 MB|