---
layout: model
title: Оcr large for printed text v2
author: John Snow Labs
name: ocr_large_printed_v2
date: 2024-03-15
tags: [en, licensed]
task: OCR Text Detection & Recognition
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

Ocr large model for recognise printed text based on TrOcr architecture. The TrOCR model was proposed in TrOCR: Transformer-based Optical Character Recognition with Pre-trained Models by Minghao Li, Tengchao Lv, Lei Cui, Yijuan Lu, Dinei Florencio, Cha Zhang, Zhoujun Li, Furu Wei. TrOCR consists of an image Transformer encoder and an autoregressive text Transformer decoder to perform optical character recognition (OCR).  The abstract from the paper is the following:  Text recognition is a long-standing research problem for document digitalization. Existing approaches for text recognition are usually built based on CNN for image understanding and RNN for char-level text generation. In addition, another language model is usually needed to improve the overall accuracy as a post-processing step. In this paper, we propose an end-to-end text recognition approach with pre-trained image Transformer and text Transformer models, namely TrOCR, which leverages the Transformer architecture for both image understanding and wordpiece-level text generation. The TrOCR model is simple but effective, and can be pre-trained with large-scale synthetic data and fine-tuned with human-labeled datasets. Experiments show that the TrOCR model outperforms the current state-of-the-art models on both printed and handwritten text recognition tasks.

## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/RECOGNIZE_PRINTED/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrImageToTextPrinted_V2_opt.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/ocr_large_printed_v2_en_5.1.2_3.0_1701749193000.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/ocr_large_printed_v2_en_5.1.2_3.0_1701749193000.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}


## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
binary_to_image = BinaryToImage() 
binary_to_image.setImageType(ImageType.TYPE_3BYTE_BGR)

text_detector = ImageTextDetectorV2 \
    .pretrained("image_text_detector_v2", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setOutputCol("text_regions") \
    .setWithRefiner(True) \
    .setSizeThreshold(-1) \
    .setLinkThreshold(0.3) \
    .setWidth(500)

ocr = ImageToTextV2.pretrained("ocr_large_printed_v2", "en", "clinical/ocr") \
    .setInputCols(["image", "text_regions"]) \
    .setGroupImages(True) \
    .setOutputCol("text") \
    .setRegionsColumn("text_regions")

draw_regions = ImageDrawRegions() \
    .setInputCol("image") \
    .setInputRegionsCol("text_regions") \
    .setOutputCol("image_with_regions") \
    .setRectColor(Color.green) \
    .setRotated(True)

pipeline = PipelineModel(stages=[
    binary_to_image,
    text_detector,
    ocr,
    draw_regions
])

image_path = pkg_resources.resource_filename('sparkocr', 'resources/ocr/images/check.jpg')
image_example_df = spark.read.format("binaryFile").load(image_path)

result = pipeline.transform(image_example_df).cache()
```
```scala
val binary_to_image = BinaryToImage() 
    .setImageType(ImageType.TYPE_3BYTE_BGR)

val text_detector = ImageTextDetectorV2
    .pretrained("image_text_detector_v2", "en", "clinical/ocr")
    .setInputCol("image")
    .setOutputCol("text_regions")
    .setWithRefiner(True)
    .setSizeThreshold(-1)
    .setLinkThreshold(0.3)
    .setWidth(500)

val ocr = ImageToTextV2.pretrained("ocr_large_printed_v2", "en", "clinical/ocr")
    .setInputCols(Array("image", "text_regions"))
    .setGroupImages(True)
    .setOutputCol("text")
    .setRegionsColumn("text_regions")

val draw_regions = ImageDrawRegions()
    .setInputCol("image")
    .setInputRegionsCol("text_regions")
    .setOutputCol("image_with_regions")
    .setRectColor(Color.green)
    .setRotated(True)

val pipeline = new PipelineModel().setStages(Array(
    binary_to_image,
    text_detector,
    ocr,
    draw_regions))

val image_path = pkg_resources.resource_filename("sparkocr", "resources/ocr/images/check.jpg")
val image_example_df = spark.read.format("binaryFile").load(image_path)

val result = pipeline.transform(image_example_df).cache()
```
</div>

## Example

{%- capture input_image -%}
![Screenshot](/assets/images/examples_ocr/image2.png)
{%- endcapture -%}

{%- capture output_image -%}
![Screenshot](/assets/images/examples_ocr/image2_out.png)
{%- endcapture -%}


{% include templates/input_output_image.md
input_image=input_image
output_image=output_image
%}

Output text:

```bash
       STARBUCKS STORE #10208
       11302 EUCLUD AVENUE
       CLEVELAND, OH (216) 229-0749

       CHK 664290
       12/07/2014 06:43 PM
       1912003 DRAWER: 2 REG: 2

      VT PEP MOCHA 4.95
      SBUX CARD 4.95
    XXXXXXXXXXXX3228

      SUBTOTAL $4.95
      TOTAL $4.95
       CHANGE DUE $0.00

    ---------- CHECK CLOSED
       12/07/2014 06:43 PM

      SBUX CARD X3228 NEW BALANCE: 37.45
   CARD IS REGISTERED
```
## Model Information

{:.table-model}
|---|---|
|Model Name:|ocr_large_printed_v2|
|Type:|ocr|
|Compatibility:|Visual NLP 5.2.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|


