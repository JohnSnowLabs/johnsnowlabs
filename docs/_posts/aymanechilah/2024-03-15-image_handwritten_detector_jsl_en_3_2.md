---
layout: model
title: Handwritten Text and Signature Detection
author: John Snow Labs
name: image_handwritten_detector_jsl
date: 2024-03-15
tags: [en, licensed]
task: Handwritten Text and Signature Detection
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

Object detection model trained to detect handwritten text one of the foremost architectures in the state-of-the-art, meticulously selected through benchmark evaluations and comparative analyses. Trained on an extensive and diverse dataset, this model has been finely tuned for precise handwritten text detection within documents. Its efficacy has been verified through rigorous testing, demonstrating exceptional performance in handwritten text detection across a spectrum of document formats.

## Predicted Entities

[Live Demo](https://demo.johnsnowlabs.com/ocr/DETECT_HANDWRITTEN/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOCRHandwrittenAndSignatureDetection.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/image_handwritten_detector_jsl_en_5.1.2_3.0_1703781670000.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/image_handwritten_detector_jsl_en_5.1.2_3.0_1703781670000.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
binary_to_image = BinaryToImage() \
    .setImageType(ImageType.TYPE_3BYTE_BGR)

text_detector = ImageDocumentRegionDetector \
    .pretrained("image_handwritten_detector_jsl", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setOutputCol("regions") \
    .setScoreThreshold(0.25)

draw_regions = ImageDrawRegions() \
    .setInputCol("image") \
    .setInputRegionsCol("regions") \
    .setOutputCol("image_with_regions") \
    .setFilledRect(False) \
    .setRectColor(Color.gray)

pipeline = PipelineModel(stages=[
    binary_to_image,
    text_detector,
    draw_regions
])

img_path = '/content/image_hw.jpeg'
image_df = spark.read.format("binaryFile").load(img_path).sort("path")

result = pipeline.transform(image_df)
```
```scala
val binary_to_image = BinaryToImage() 
    .setImageType(ImageType.TYPE_3BYTE_BGR)

val text_detector = ImageDocumentRegionDetector 
    .pretrained("image_handwritten_detector_jsl", "en", "clinical/ocr") 
    .setInputCol("image") 
    .setOutputCol("regions") 
    .setScoreThreshold(0.25)

val draw_regions = ImageDrawRegions() 
    .setInputCol("image") 
    .setInputRegionsCol("regions") 
    .setOutputCol("image_with_regions")
    .setFilledRect(False)
    .setRectColor(Color.gray)

val pipeline = new PipelineModel().setStages(Array(
    binary_to_image,
    text_detector,
    draw_regions))

val img_path = "/content/image_hw.jpeg"
val image_df = spark.read.format("binaryFile").load(img_path).sort("path")

val result = pipeline.transform(image_df)
```

</div>


## Example

{%- capture input_image -%}
![Screenshot](/assets/images/examples_ocr/hw_detection_input.png)
{%- endcapture -%}

{%- capture output_image -%}
![Screenshot](/assets/images/examples_ocr/hw_detection_output.png)
{%- endcapture -%}


{% include templates/input_output_image.md
input_image=input_image
output_image=output_image
%}



## Model Information

{:.table-model}
|---|---|
|Model Name:|image_handwritten_detector_jsl|
|Type:|ocr|
|Compatibility:|Visual NLP 5.2.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|

