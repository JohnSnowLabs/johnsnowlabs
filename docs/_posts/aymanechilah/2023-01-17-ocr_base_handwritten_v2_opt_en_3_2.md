---
layout: model
title: Оcr base v2 optimized for handwritten text
author: John Snow Labs
name: ocr_base_handwritten_v2_opt
date: 2023-01-17
tags: [en, licensed]
task: OCR Text Detection & Recognition
language: en
nav_key: models
edition: Visual NLP 4.2.4
spark_version: 3.2.1
supported: true
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Ocr base handwritten model v2 optimized for recognise handwritten text based on a TrOCR model pretrained with handwritten datasets. It is an Ocr base model for recognise handwritten text based on TrOcr architecture.  The TrOCR model was proposed in TrOCR: Transformer-based Optical Character Recognition with Pre-trained Models by Minghao Li, Tengchao Lv, Lei Cui, Yijuan Lu, Dinei Florencio, Cha Zhang, Zhoujun Li, Furu Wei. TrOCR consists of an image Transformer encoder and an autoregressive text Transformer decoder to perform optical character recognition (OCR).  The abstract from the paper is the following:  Text recognition is a long-standing research problem for document digitalization. Existing approaches for text recognition are usually built based on CNN for image understanding and RNN for char-level text generation. In addition, another language model is usually needed to improve the overall accuracy as a post-processing step. In this paper, we propose an end-to-end text recognition approach with pre-trained image Transformer and text Transformer models, namely TrOCR, which leverages the Transformer architecture for both image understanding and wordpiece-level text generation. The TrOCR model is simple but effective, and can be pre-trained with large-scale synthetic data and fine-tuned with human-labeled datasets. Experiments show that the TrOCR model outperforms the current state-of-the-art models on both printed and handwritten text recognition tasks.


## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/RECOGNIZE_HANDWRITTEN/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrImageToTextHandwritten_V2_opt.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/ocr_base_handwritten_v2_opt_en_4.2.2_3.0_1670608549000.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/ocr_base_handwritten_v2_opt_en_4.2.2_3.0_1670608549000.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}


## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
binary_to_image = BinaryToImage() \
    .setInputCol("content") \
    .setOutputCol("image") \
    .setImageType(ImageType.TYPE_3BYTE_BGR)

text_detector = ImageTextDetectorV2 \
    .pretrained("image_text_detector_v2", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setOutputCol("text_regions") \
    .setWithRefiner(True) \
    .setSizeThreshold(-1) \
    .setLinkThreshold(0.3) \
    .setWidth(500)

ocr = ImageToTextV2.pretrained("ocr_base_handwritten_v2_opt", "en", "clinical/ocr") \
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

# Download image:
# !wget -q https://github.com/JohnSnowLabs/spark-ocr-workshop/raw/4.0.0-release-candidate/jupyter/data/handwritten/handwritten_example.jpg
imagePath = 'handwritten_example.jpg'
image_df = spark.read.format("binaryFile").load(imagePath)

result = pipeline.transform(image_df).cache()
```
```scala
val binary_to_image = new BinaryToImage() 
    .setInputCol("content") 
    .setOutputCol("image") 
    .setImageType(ImageType.TYPE_3BYTE_BGR)

val text_detector = ImageTextDetectorV2 
    .pretrained("image_text_detector_v2", "en", "clinical/ocr") 
    .setInputCol("image") 
    .setOutputCol("text_regions") 
    .setWithRefiner(True) 
    .setSizeThreshold(-1) 
    .setLinkThreshold(0.3) 
    .setWidth(500)

val ocr = ImageToTextV2
    .pretrained("ocr_base_handwritten_v2_opt", "en", "clinical/ocr") 
    .setInputCols(Array("image", "text_regions")) 
    .setGroupImages(True) 
    .setOutputCol("text") 
    .setRegionsColumn("text_regions")

val draw_regions = new ImageDrawRegions() 
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

# Download image:
# !wget -q https://github.com/JohnSnowLabs/spark-ocr-workshop/raw/4.0.0-release-candidate/jupyter/data/handwritten/handwritten_example.jpg
val imagePath = "handwritten_example.jpg"
val image_df = spark.read.format("binaryFile").load(imagePath)

val result = pipeline.transform(image_df).cache()
```
</div>

## Example

{%- capture input_image -%}
![Screenshot](/assets/images/examples_ocr/image3.png)
{%- endcapture -%}

{%- capture output_image -%}
![Screenshot](/assets/images/examples_ocr/image3_out2.png)
{%- endcapture -%}


{% include templates/input_output_image.md
input_image=input_image
output_image=output_image
%}

## Output text

```bash
This is an example of handwritten
beerxt
Let's # check the performance !
I hope it will be awesome
```

## Model Information

{:.table-model}
|---|---|
|Model Name:|ocr_base_handwritten_v2_opt|
|Type:|ocr|
|Compatibility:|Visual NLP 4.2.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|


