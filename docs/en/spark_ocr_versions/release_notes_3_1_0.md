---
layout: docs
header: true
seotitle: Spark NLP
title: Spark NLP release notes 3.1.0
permalink: /docs/en/spark_ocr_versions/release_notes_3_1_0
key: docs-release-notes
modify_date: "2022-01-06"
show_nav: true
sidebar:
    nav: sparknlp
---

<div class="h3-box" markdown="1">

## 3.1.0

Release date: 16-04-2021

#### Overview

Image processing on GPU. It is in 3.5 times faster than on CPU.

More details please read in [GPU image preprocessing in Spark OCR](https://medium.com/spark-nlp/gpu-image-pre-processing-in-spark-ocr-3-1-0-6fc27560a9bb)

</div><div class="h3-box" markdown="1">

#### New Features

* [GPUImageTransformer](/docs/en/ocr_pipeline_components#gpuimagetransformer) with support: scaling, erosion, delation, Otsu and Huang thresholding.
* Added [display_images](/docs/en/ocr_structures#displayimages) util function for displaying images from Spark DataFrame in Jupyter notebooks.

</div><div class="h3-box" markdown="1">

#### Enhancements

* Improve [display_image](/docs/en/ocr_structures#displayimage) util function.

</div><div class="h3-box" markdown="1">

#### Bug fixes

* Fixed issue with extra dependencies in [start](/docs/en/ocr_install#using-start-function) function

</div><div class="h3-box" markdown="1">

#### New notebooks

* [GPU image processing](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/3.1.0/jupyter/SparkOCRGPUOperations.ipynb)

</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>
{%- include docs-sparckocr-pagination.html -%}