---
layout: model
title: DiT model finetuned on FUNSD for text detection
author: John Snow Labs
name: image_text_detector_dit
date: 2023-07-11
tags: [en, licensed]
task: OCR Text Detection
language: en
nav_key: models
edition: Visual NLP 4.0.0
spark_version: 3.2.1
supported: true
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

DiT was proposed in "DiT: Self-supervised Pre-training for Document Image Transformer" by Junlong Li, Yiheng Xu, Tengchao Lv, Lei Cui, Cha Zhang, and Furu Wei. DiT applies the self-supervised objective of BEiT (BERT pre-training of Image Transformers) to 42 million document images. This model is specifically trained for document text detection within the FUNSD (Form Understanding in Noisy Scanned Documents) dataset, a comprehensive collection of labeled document images. It comprises 199 real, fully annotated, scanned forms documents that are noisy and vary widely in appearance.

The abstract from the paper is the following: Image Transformer has recently achieved significant progress for natural image understanding, either using supervised (ViT, DeiT, etc.) or self-supervised (BEiT, MAE, etc.) pre-training techniques. In this paper, we propose DiT, a self-supervised pre-trained Document Image Transformer model using large-scale unlabeled text images for Document AI tasks, which is essential since no supervised counterparts ever exist due to the lack of human labeled document images. We leverage DiT as the backbone network in a variety of vision-based Document AI tasks, including document image classification, document layout analysis, as well as table detection. Experiment results have illustrated that the self-supervised pre-trained DiT model achieves new state-of-the-art results on these downstream tasks, e.g. document image classification (91.11 → 92.69), document layout analysis (91.0 → 94.9) and table detection (94.23 → 96.55).


## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/TEXT_DETECTION_DIT/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrImageTextDetection.ipynb){:.button.button-orange.button-orange-trans.co.button-icon} 
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/image_text_detector_dit_en_4.4.0_3.0_1692086682871.zip){:.button.button-orange.button-orange-trans.arr.button-icon} 

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
binary_to_image = BinaryToImage()\
    .setInputCol("content") \
    .setOutputCol("image") \
    .setImageType(ImageType.TYPE_3BYTE_BGR)

text_detector = ImageTextDetectorDit \
    .pretrained("image_text_detector_dit", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setOutputCol("text_regions") \
    .setScoreThreshold(0.5)

draw_regions = ImageDrawRegions() \
    .setInputCol("image") \
    .setInputRegionsCol("text_regions") \
    .setOutputCol("image_with_regions") \
    .setRectColor(Color.green) \
    .setRotated(True)

pipeline = PipelineModel(stages=[
    binary_to_image,
    text_detector,
    draw_regions
])

test_image_path = pkg_resources.resource_filename('sparkocr', 'resources/ocr/images/check.jpg')
bin_df = spark.read.format("binaryFile").option("recursiveFileLookup","true").load(test_image_path)

results = pipeline.transform(bin_df).cache()
```
```scala
val binary_to_image = new BinaryToImage()
    .setInputCol("content")
    .setOutputCol("image")
    .setImageType(ImageType.TYPE_3BYTE_BGR)

val text_detector = new ImageTextDetectorDit
    .pretrained("image_text_detector_dit", "en", "clinical/ocr")
    .setInputCol("image")
    .setOutputCol("text_regions")
    .setScoreThreshold(0.5)

val draw_regions = new ImageDrawRegions()
    .setInputCol("image")
    .setInputRegionsCol("text_regions")
    .setOutputCol("image_with_regions")
    .setRectColor(Color.green)
    .setRotated(True)

val pipeline = new new PipelineModel().setStages(Array(
    binary_to_image,
    text_detector,
    draw_regions))

val test_image_path = pkg_resources.resource_filename("sparkocr", "resources/ocr/images/check.jpg")
val bin_df = spark.read.format("binaryFile").option("recursiveFileLookup","true").load(test_image_path)

val results = pipeline.transform(bin_df).cache()
```
</div>

## Example

### Input:
![Screenshot](/assets/images/examples_ocr/funsd_img_2.jpg)

## Output text
![Screenshot](/assets/images/examples_ocr/funsd_img_2_dit_td.png)


{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|image_text_detector_dit|
|Type:|ocr|
|Compatibility:|Visual NLP 4.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|

## References

IIT-CDIP, FUNSD