---
layout: model
title: Checkbox Detection
author: John Snow Labs
name: checkbox_detector_v1
date: 2024-04-15
tags: [en, licensed]
task: Checkbox Detection & Recognition
language: en
nav_key: models
edition: Visual NLP 5.3.1
spark_version: 3.2.1
supported: true
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Object detection model trained to detect document checkboxes one of the foremost architectures in the state-of-the-art, meticulously selected through benchmark evaluations and comparative analyses. Trained on an extensive and diverse dataset, this model has been finely tuned for precise document checkbox detection and classification within documents. Its efficacy has been verified through rigorous testing, demonstrating exceptional performance in document checkbox detection across a spectrum of document formats.

## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/CHECKBOX_DETECTION/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrCheckBoxDetection.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/checkbox_detector_v1_en_5.0.0_3.0_1711346758339.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/checkbox_detector_v1_en_5.0.0_3.0_1711346758339.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
binary_to_image = BinaryToImage() \
    .setImageType(ImageType.TYPE_3BYTE_BGR)

check_box_detector = ImageCheckBoxDetector \
    .pretrained("checkbox_detector_v1", "en", "clinical/ocr") \
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
```scala
val binary_to_image = BinaryToImage()
    .setImageType(ImageType.TYPE_3BYTE_BGR)

val check_box_detector = ImageCheckBoxDetector
    .pretrained("checkbox_detector_v1", "en", "clinical/ocr")
    .setInputCol("image") 
    .setLabels(Array("No", "Yes")) 
    .setOutputLabels(Array("No", "Yes")) 
    .setScoreThreshold(0.1) 
    .setOutputCol("regions") 
    .setOutputFormat(DetectorOutputFormat.REGIONS)

val draw_regions = ImageDrawRegions() 
    .setInputCol("image") 
    .setInputRegionsCol("regions") 
    .setOutputCol("image_with_regions") 
    .setRectColor(Color.green) 
    .setRotated(False)

val pipeline = new PipelineModel().setStages(Array(
    binary_to_image,
    check_box_detector,
    draw_regions))

val imagePath = "cboxes.png"
val image_df = spark.read.format("binaryFile").load(imagePath).sort("path")

val result = pipeline.transform(image_df)
```

</div>


## Example

### Input:
![Screenshot](/assets/images/examples_ocr/cboxes.png)

### Checkbox Detection:
![Screenshot](/assets/images/examples_ocr/cboxes_out.png)

### Checkbox to text:
![Screenshot](/assets/images/examples_ocr/cboxes_out_process.png)


## Model Information

{:.table-model}
|---|---|
|Model Name:|checkbox_detector_v1|
|Type:|ocr|
|Compatibility:|Visual NLP 5.1.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|

