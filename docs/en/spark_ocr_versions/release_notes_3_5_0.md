---
layout: docs
header: true
seotitle: Spark NLP
title: Spark NLP release notes 3.5.0
permalink: /docs/en/spark_ocr_versions/release_notes_3_5_0
key: docs-release-notes
modify_date: "2022-01-06"
show_nav: true
sidebar:
    nav: sparknlp
---

<div class="h3-box" markdown="1">

## 3.5.0

Release date: 15-07-2021

#### Overview

Improve table detection and table recognition.

More details please read in [Extract Tabular Data from PDF in Spark OCR](https://medium.com/spark-nlp/extract-tabular-data-from-pdf-in-spark-ocr-b02136bc0fcb)

</div><div class="h3-box" markdown="1">

#### New Features

* Added new method to [ImageTableCellDetector](/docs/en/ocr_table_recognition#imagetablecelldetector) which support 
borderless tables and combined tables.
* Added __Wolf__ and __Singh__ adaptive binarization methods to the [ImageAdaptiveThresholding](../ocr_pipeline_components#imageadaptivethresholding).

</div><div class="h3-box" markdown="1">

#### Enhancements

* Added possibility to use different type of images as input for [ImageTableDetector](/docs/en/ocr_table_recognition#imagetabledetector).
* Added [display_pdf](/docs/en/ocr_structures#displaypdf) and [display_images_horizontal](/docs/en/ocr_structures#displayimageshorizontal) util functions.

</div><div class="h3-box" markdown="1">

#### New notebooks

* [Tables Recognition from PDF](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/3.5.0/jupyter/SparkOcrImageTableRecognitionPdf.ipynb)
* [Pdf de-identification on Databricks](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/3.5.0/databricks/python/SparkOcrDeIdentification.ipynb)
* [Dicom de-identification on Databricks](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/3.5.0/databricks/python/SparkOCRDeIdentificationDicom.ipynb)

</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>
{%- include docs-sparckocr-pagination.html -%}