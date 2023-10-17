---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_5_0_1
key: docs-ocr-release-notes
modify_date: "2023-09-21"
show_nav: true
sidebar:
    nav: spark-ocr
---

<div class="h3-box" markdown="1">

## 5.0.1

Release date: 21-09-2023

**We are glad to announce that Visual NLP 5.0.1 has been released! 🚀🚀🚀   New features, new models, bug fixes, and more!  📢📢📢**


🚨 **New Features**

+ New Dit based Text Detection Model: Continuing with our commitment to empower Text Extraction and De-identification pipelines we are delivering a new model for text detection, it was trained on the FUNSD dataset, and its utilization is similar to other related models,

ImageTextDetector \
.pretrained("image_text_detector_dit", "en", "clinical/ocr") \
.setInputCol("image")
.setOutputCol("region")
.setScoreThreshold(0.5)

It is currently the best performing model at the FUNSD dataset, achieving an accuracy of 94% vs Craft detector which achieved 78.7%, and is recommended for De-identification and Text Extraction pipelines.

+ Dit based VisualDocumentClassifierV3 now supports fine tuning: check the new tutorial, and notebook, on how to fine-tune Dit-based VisualDocumentClassifierV3 on the RVL-CDIP dataset using a Docker image. 

+ New Pretrained Pipeline for Table Extraction: this new pipeline, digital_pdf_table_extractor, extracts tables from digital PDFs. Check and end-to-end example in this notebook.

+ New notebook explaining how to do inference on RvlCdip with VisualDocumentClassiferV3 on Databricks: check this new notebook explaining how you can process the entire RVL-CDIP dataset using auto-scaling in Databricks in few minutes.

+ New RvlCdipReader to help read both training and test parts of the RvlCdip document classification dataset. Check this notebook for an example.


🪲 **Bug Fixes**

+ Avoid to use downloadable metrics script for Lilt NER training: now all the metric computation can be handled offline for Lilt NER model training.
+ The bug in data consumption for VisualDocumentNer Lilt models was fixed: this bug affected data ingestion during fine tuning, and affected the quality of the resulting models.
+ Serialization issues preventing ImageTableDetector and HocrToTextTable from working properly in a pipeline were fixed.
+ PositionFinder has improved error reporting logic.
+ ImageToText MacOS errors were solved.





</div><div class="prev_ver h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
