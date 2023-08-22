---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_5_0_0
key: docs-ocr-release-notes
modify_date: "2023-08-21"
show_nav: true
sidebar:
    nav: spark-ocr
---

<div class="h3-box" markdown="1">

## 5.0.0

Release date: 21-08-2023

We are glad to announce that Visual NLP 😎 5.0.0 has been released! 
This release comes with new models, bug fixes and more!

#### New Models
* New dit_base_finetuned_rvlcdip_opt: Dit based Visual Document Classification model. This is an optimized version of previous dit_base_finetuned_rvlcdip model. It has a reduced model size of 80MB(vs. 304 of original model), which reduces the memory footprint, also memory management within the model itself has been improved. It offers a speedup of 1.54x compared to the original implementation. The impact in accuracy is minimal, it achieves an accuracy of 91.55% over RVL-CDIP dataset compared to 91.83% of the original model.
Setting up the model is straightforward,

```
doc_class = VisualDocumentClassifierV3() \
    .pretrained("dit_base_finetuned_rvlcdip_opt", "en", "clinical/ocr") \
    .setInputCols(["image"]) \
    .setOutputCol("label")
```

Use [this notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOCRVisualDocumentClassifierv3.ipynb) as a reference.

* New image_text_detector_mem_opt: memory optimized Craft Text Detection Model. This is new a model that improves the performance and memory consumption of the previous ImageTextDetector models. This is the same CRAFT architecture, where memory management has been improved, and refiner network has been merged into a single graph with the main network. This removes expensive data movement and reduces memory consumption.
Setting up the model is straightforward,

```
text_detector = ImageTextDetector.pretrained("image_text_detector_opt", "en", "clinical/ocr")
text_detector.setInputCol("image")
text_detector.setOutputCol("text_regions")
```
Use [this notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/TextDetection/SparkOcrImageTextDetection.ipynb) as a reference.

+ New lilt_rvl_cdip_296K: Lilt based Visual Document Classification model: Language-independent Layout Transformer (LiLT) model for document classification. The model was trained on RVL-CDIP dataset that consists of 400.000 grayscale images in 16 classes.

Setting up the model is done like this,

```
doc_class = VisualDocumentClassifierLilt() \
    .pretrained("lilt_rvl_cdip_296K", "en", "clinical/ocr") \
    .setInputCol("hocr") \
    .setOutputCol("label")

```
Use [this notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOCRVisualDocumentClassifierLiLT.ipynb) as a reference.


#### New Annotators
* New DicomToPdf and DicomUpdatePdf annotators: the new annotators now make it possible to extract and update encapsulated PDF files within DICOM documents. This opens up opportunities to building de-identification pipelines for the purpose of anonymizing PDF documents that have been encapsulated(embedded) into Dicom files.

#### Bug Fixes
* ImageDrawAnnotations serialization issues were solved.
* FormRelationExtraction is now compatible with the new Lilt Visual Ner models.
* Pipeline serialization issues in Databricks affecting annotators like ImageHandwrittenDetector have been solved.
* Pillow related errors in Colab setup have been fixed. 

#### New Notebooks
* [VisualDocumentClassifierTraining](https://github.com/JohnSnowLabs/spark-ocr-workshop/tree/master/jupyter/VisualDocumentClassifierTraining), notebooks for Visual Documents Classifier fine tuning have been updated to use the new Lilt based models.
* [SparkOcrDeidentificationDicomWithEncapsulatedPDF.ipynb](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Dicom/SparkOcrDeidentificationDicomWithEncapsulatedPDF.ipynb), learn how to use the new DicomToPdf and DicomUpdatePdf.
* [SparkOcrDicomDeIdentificationV2Streaming.ipynb](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Dicom/SparkOcrDicomDeIdentificationV2Streaming.ipynb), learn how to setup a Spark Structured Streaming pipeline for Dicom Deidentification.


</div><div class="prev_ver h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
