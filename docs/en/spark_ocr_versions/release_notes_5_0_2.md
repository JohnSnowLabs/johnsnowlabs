---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_5_0_2
key: docs-ocr-release-notes
modify_date: "2023-10-16"
show_nav: true
sidebar:
    nav: spark-ocr
---

<div class="h3-box" markdown="1">

## 5.0.2

Release date: 16-10-2023

**We are glad to announce that Visual NLP 5.0.2 has been released! 🚀🚀🚀   New features, new models, bug fixes, and more!  📢📢📢** 


This is a small compatibility release to ensure the product runs smoothly on Google Colab, and that it remains compatible with the latest versions of Spark NLP and Spark NLP for Healthcare.

**Changes :** 📣

+ Google Colab installation issues have been solved. 

+ New setting for M1 compatibility in Spark-NLP dependency: 
  ```bash
  start(m1=True|False)
  use m1=True 
  ``` 
  use m1=True enables the M1 compatible version of Spark-NLP.

+  ```  New ImageToTextV3 annotator ```  : this is a new version of the original LSTM based ImageToText annotator, with the difference that it accepts input regions in a similar fashion to ImageToTextV2. In the original ImageToText implementation all layout analysis happens implicitly within the annotator itself, without external help.

This release is compatible with ```Spark NLP 5.1.1``` and Spark NLP for``` Healthcare 5.1.1```





</div><div class="prev_ver h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
