---
layout: docs
header: true
seotitle: Spark NLP
title: Spark NLP release notes 1.4.0
permalink: /docs/en/spark_ocr_versions/release_notes_1_4_0
key: docs-release-notes
modify_date: "2022-01-06"
show_nav: true
sidebar:
    nav: sparknlp
---

<div class="h3-box" markdown="1">

## 1.4.0

Release date: 23-06-2020

#### Overview

Added support Dicom format and improved support image morphological operations.

</div><div class="h3-box" markdown="1">

#### Enhancements

* Updated [start](/docs/en/ocr_install#using-start-function) function. Improved support Spark NLP internal.
* `ImageMorphologyOpening` and `ImageErosion` are removed.
* Improved existing transformers for support de-identification Dicom documents.
* Added possibility to draw filled rectangles to [ImageDrawRegions](/docs/en/ocr_pipeline_components#imagedrawregions).

</div><div class="h3-box" markdown="1">

#### New Features

* Support reading and writing Dicom documents.
* Added [ImageMorphologyOperation](/docs/en/ocr_pipeline_components#imagemorphologyoperation) transformer which support:
 erosion, dilation, opening and closing operations.

</div><div class="h3-box" markdown="1">

#### Bugfixes

* Fixed issue in [ImageToText](/docs/en/ocr_pipeline_components#imagetotext) related to extraction coordinates.


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>
{%- include docs-sparckocr-pagination.html -%}