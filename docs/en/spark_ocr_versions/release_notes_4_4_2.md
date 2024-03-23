---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_4_4_2
key: docs-ocr-release-notes
modify_date: "2023-05-30"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 4.4.2

Release date: 30-05-2023

We are glad to announce that Visual NLP 😎 4.4.2 has been released. This is a small release with mostly bug fixes and minor improvements.

#### Fixes
* ImageTextDetectorV2 initialization bug happening in some cluster environments is now fixed.
* PdfToText and PdfToHocr now return document dimensions using the same data type(integer).
* Remaining 2 vulnerabilities from release 4.4.1 in JAR package are now gone. 
* Fixed the problem causing the following exception in HocrToTextTable:  java.lang.UnsupportedOperationException.

New Features
+ Bounding boxes spawning multiple lines are now supported in PositionFinder!

original:
![image](/assets/images/ocr/position_finder_1.png)
masked:
![image](/assets/images/ocr/position_finder_2.png)

Here for "Lockheed Martin" PositionFinder will return two bounding boxes. Remember that you can still link the two bounding boxes to the original entity by using the 'chunk index'.

* Support for Spark 3.4.
* [Guidelines for building Visual NLP into a Java app.](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/java/build_env_setup.md)

</div><div class="prev_ver h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
