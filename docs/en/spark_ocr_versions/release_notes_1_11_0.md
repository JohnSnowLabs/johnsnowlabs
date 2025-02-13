---
layout: docs
header: true
seotitle: Spark NLP
title: Spark NLP release notes 1.11.0
permalink: /docs/en/spark_ocr_versions/release_notes_1_11_0
key: docs-release-notes
modify_date: "2022-01-06"
show_nav: true
sidebar:
    nav: sparknlp
---

<div class="h3-box" markdown="1">

## 1.11.0

Release date: 25-02-2021

#### Overview

Support German, French, Spanish and Russian languages.
Improving [PositionsFinder](/docs/en/ocr_pipeline_components#positionsfinder) and ImageToText for better support de-identification.

</div><div class="h3-box" markdown="1">

#### New Features

* Loading model data from S3 in [ImageToText](/docs/en/ocr_pipeline_components#imagetotext).
* Added support German, French, Spanish, Russian languages in [ImageToText](/docs/en/ocr_pipeline_components#imagetotext).
* Added different OCR model types: Base, Best, Fast in [ImageToText](/docs/en/ocr_pipeline_components#imagetotext).

</div><div class="h3-box" markdown="1">

#### Enhancements

* Added spaces symbols to the output positions in the [ImageToText](/docs/en/ocr_pipeline_components#imagetotext) transformer.
* Eliminate python-levensthein from dependencies for simplify installation.

</div><div class="h3-box" markdown="1">

#### Bugfixes

* Fixed issue with extracting coordinates in  in [ImageToText](/docs/en/ocr_pipeline_components#imagetotext).
* Fixed loading model data on cluster in yarn mode.

</div><div class="h3-box" markdown="1">

#### New notebooks

* [Languages Support](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/1.11.0/jupyter/SparkOcrLanguagesSupport.ipynb)
* [Image DeIdentification](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/1.11.0/jupyter/SparkOcrImageDeIdentification.ipynb)


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>
{%- include docs-sparckocr-pagination.html -%}