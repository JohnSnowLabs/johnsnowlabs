---
layout: model
title: Table Detection v3
author: John Snow Labs
name: table_detection_v3
date: 2024-03-15
tags: [en, licensed]
task: Table Detection
language: en
nav_key: models
edition: Visual NLP 5.2.0
spark_version: 3.2.1
supported: true
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Object detection model trained to detect tables leverages one of the foremost architectures in the state-of-the-art, meticulously selected through benchmark evaluations and comparative analyses. Trained on an extensive and diverse dataset, this model has been finely tuned for precise table detection within documents. Its efficacy has been verified through rigorous testing, demonstrating exceptional performance in table detection across a spectrum of document formats.

## Predicted Entities

``table``.

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/IMAGE_TABLE_DETECTION/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrImageTableDetection.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/table_detection_v3_en_5.2.0_3.0_1707370970000.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/table_detection_v3_en_5.2.0_3.0_1707370970000.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
binary_to_image = BinaryToImage()

cell_detector = ImageDocumentRegionDetector() \
    .pretrained("table_detection_v3", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setOutputCol("regions") \
    .setScoreThreshold(0.8)

draw_regions = ImageDrawRegions() \
    .setInputCol("image") \
    .setInputRegionsCol("regions") \
    .setOutputCol("image_with_regions") \
    .setRectColor(Color.red)


pipeline = PipelineModel(stages=[
    binary_to_image,
    cell_detector,
    draw_regions,
])

imagePath = 'document.jpg'
image_df = spark.read.format("binaryFile").load(imagePath).sort("path")

result = pipeline.transform(image_df)
```
```scala
val binary_to_image = BinaryToImage()

val cell_detector = ImageDocumentRegionDetector()
    .pretrained("table_detection_v3", "en", "clinical/ocr")
    .setInputCol("image")
    .setOutputCol("regions")
    .setScoreThreshold(0.8)

val draw_regions = ImageDrawRegions()
    .setInputCol("image")
    .setInputRegionsCol("regions")
    .setOutputCol("image_with_regions")
    .setRectColor(Color.red)

val pipeline = new PipelineModel().setStages(Array(
    binary_to_image,
    cell_detector,
    draw_regions))

val imagePath = "document.jpg"
val image_df = spark.read.format("binaryFile").load(imagePath).sort("path")

val result = pipeline.transform(image_df)
```

</div>


## Example

### Input:
![Screenshot](/assets/images/examples_ocr/image5.png)

### Output:
![Screenshot](/assets/images/examples_ocr/image5_tdv3.png)


## Model Information

{:.table-model}
|---|---|
|Model Name:|table_detection_v3|
|Type:|ocr|
|Compatibility:|Visual NLP 5.2.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|

