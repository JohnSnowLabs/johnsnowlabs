---
layout: model
title: Table Cell Detection
author: John Snow Labs
name: region_cell_detection
date: 2024-03-15
tags: [en, licensed]
task: Table Cell Detection & Table Recognition
language: en
nav_key: models
edition: Visual NLP 5.1.2
spark_version: 3.2.1
supported: true
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Object detection model trained to detect table cells one of the foremost architectures in the state-of-the-art, meticulously selected through benchmark evaluations and comparative analyses. Trained on an extensive and diverse dataset, this model has been finely tuned for precise table cell detection within documents. Its efficacy has been verified through rigorous testing, demonstrating exceptional performance in table cell detection across a spectrum of document formats.

## Predicted Entities

``cells``.

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/IMAGE_REGION_CELL_DETECTION/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrImageTableRecognitionWHOCR.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/region_cell_detection_en_5.1.2_3.0_1702887854966.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/region_cell_detection_en_5.1.2_3.0_1702887854966.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
binary_to_image = BinaryToImage()

img_to_hocr = ImageToHocr() \
    .setInputCol("image") \
    .setOutputCol("hocr") \
    .setIgnoreResolution(False) \
    .setOcrParams(["preserve_interword_spaces=0"])

cell_detector = ImageDocumentRegionDetector() \
    .pretrained("region_cell_detection", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setOutputCol("cells") \
    .setScoreThreshold(0.8)

draw_regions = ImageDrawRegions() \
    .setInputCol("image") \
    .setInputRegionsCol("cells") \
    .setOutputCol("image_with_regions") \
    .setRectColor(Color.red)

hocr_to_table = HocrToTextTable() \
    .setInputCol("hocr") \
    .setRegionCol("table_regions") \
    .setOutputCol("tables") \
    .setUseCellsCol("cells")

pipeline = PipelineModel(stages=[
    binary_to_image,
    img_to_hocr,
    cell_detector,
    draw_regions,
    hocr_to_table
])

imagePath = 'resources/ocr/table.jpg'
image_df = spark.read.format("binaryFile").load(imagePath).sort("path")

result = pipeline.transform(image_df)
```
```scala
val binary_to_image = BinaryToImage()

val img_to_hocr = ImageToHocr()
    .setInputCol("image")
    .setOutputCol("hocr")
    .setIgnoreResolution(False)
    .setOcrParams(Array("preserve_interword_spaces=0"))

val cell_detector = ImageDocumentRegionDetector()
    .pretrained("region_cell_detection", "en", "clinical/ocr")
    .setInputCol("image")
    .setOutputCol("cells")
    .setScoreThreshold(0.8)

val draw_regions = ImageDrawRegions()
    .setInputCol("image")
    .setInputRegionsCol("cells")
    .setOutputCol("image_with_regions")
    .setRectColor(Color.red)

val hocr_to_table = HocrToTextTable()
    .setInputCol("hocr")
    .setRegionCol("table_regions")
    .setOutputCol("tables")
    .setUseCellsCol("cells")

val pipeline = new PipelineModel().setStages(Array(
    binary_to_image,
    img_to_hocr,
    cell_detector,
    draw_regions,
    hocr_to_table))

val imagePath = "resources/ocr/table.jpg"
val image_df = spark.read.format("binaryFile").load(imagePath).sort("path")

val result = pipeline.transform(image_df)
```

</div>


## Example

### Input:
![Screenshot](/assets/images/examples_ocr/table_celldetector_input.png)

### Cell Detection:
![Screenshot](/assets/images/examples_ocr/table_celldetector_v1_cells.png)

### Table Structure Recognition:
![Screenshot](/assets/images/examples_ocr/table_celldetector_v1_tsr.png)



## Model Information

{:.table-model}
|---|---|
|Model Name:|region_cell_detection|
|Type:|ocr|
|Compatibility:|Visual NLP 5.1.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|

