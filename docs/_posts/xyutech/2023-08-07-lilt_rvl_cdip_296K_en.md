---
layout: model
title: Visual Document Classification with LiLT
author: John Snow Labs
name: lilt_rvl_cdip_296K
date: 2023-08-07
tags: [en, licensed]
task: OCR Document Classification
language: en
edition: Visual NLP 5.0.0
spark_version: 3.2
supported: true
annotator: VisualDocumentClassifierLilt
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Language-Independent Layout Transformer (LiLT) model for document classification. The model was trained on RVL-CDIP dataset that consists of 400 000 grayscale images in 16 classes.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/lilt_rvl_cdip_296K_en_5.0.0_3.2_1691381949565.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/lilt_rvl_cdip_296K_en_5.0.0_3.2_1691381949565.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
        binary_to_image = BinaryToImage() \
            .setOutputCol("image") \
            .setImageType(ImageType.TYPE_3BYTE_BGR)

        img_to_hocr = ImageToHocr() \
            .setInputCol("image") \
            .setOutputCol("hocr") \
            .setIgnoreResolution(False) \
            .setOcrParams(["preserve_interword_spaces=0"])

        doc_class = VisualDocumentClassifierLilt \
            .pretrained("lilt_rvl_cdip_296K", "en", "clinical/ocr") \
            .loadONNXModel(model_file, spark_session) \
            .setInputCol("hocr") \
            .setOutputCol("label")
            
        pipeline = PipelineModel(stages=[
            binary_to_image,
            img_to_hocr,
            doc_class,
        ])
```
```scala
    var bin2imTransformer = new BinaryToImage()
    bin2imTransformer.setImageType(ImageType.TYPE_3BYTE_BGR)

    val ocr = new ImageToHocr()
      .setInputCol("image")
      .setOutputCol("hocr")
      .setIgnoreResolution(false)
      .setOcrParams(Array("preserve_interword_spaces=0"))

    val visualDocumentClassifier = VisualDocumentClassifierLilt
      .pretrained("lilt_rvl_cdip_296K", "en", "clinical/ocr")
      .setInputCol("hocr")
        
    val pipeline = new Pipeline()
      .setStages(Array(
        bin2imTransformer,
        ocr,
        visualDocumentClassifier
      ))

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|lilt_rvl_cdip_296K|
|Type:|ocr|
|Compatibility:|Visual NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|432.5 MB|

## References

RVL-CDIP

## Benchmarking

```bash
Accuracy 86%
```