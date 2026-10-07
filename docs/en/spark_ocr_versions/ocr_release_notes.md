---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/ocr_release_notes
key: docs-ocr-release-notes
modify_date: "07-10-2026"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 7.0.0

Release date: 07-10-2026

## Visual NLP 7.0.0 Release Notes 🕶️

**We are glad to announce that Visual NLP 7.0.0 has been released! This is a release with multiple small, but impactful changes. 📢📢📢**

</div><div class="h3-box" markdown="1">

## Main Changes 🔴

* Added support for latest Spark 4.X versions, and continue with our efforts to support Scala 2.13 and Java 17.
* Dicom Processing improvements, and also improvements in our Pathology (SVS) Processing capabilities.
* New models and pipelines.
* A new Infrastructure Stack (Cloudformation) to run SVS and Dicom de-identification in AWS, and new instructions on how to run on Databricks.

</div><div class="h3-box" markdown="1">

## Important changes in `start()` function

Following the guidelines of open source Spark-NLP, JAR artifact selection in `start()` function is now determined by PySpark version, as follows,

| Spark Version | Scala Version | JAR Artifact |
|---|---|---|
| Spark 3.x | Scala 2.12 | spark-ocr 3.x |
| Spark 4.0.0 | Scala 2.13 | spark-ocr 400 |
| Other Spark 4.x | Scala 2.13 | spark-ocr 4.0.1+ |

</div><div class="h3-box" markdown="1">

## Dicom Changes

* Updates the `DicomPretrainedPipeline` to support strategy files used in de-identification of Dicom tags. Also, `DicomPretrainedPipeline` now supports `load()/save()`.
* New `replaceWithMapping` action in `DicomMetadataDeidentifier`: replaces tag values from an external mapping column (`externalMapping`), with optional nested-tag handling.
* Overlay extraction off by default (new `extractOverlay` param).
* Fixes for YBR 8-bit compression, compression ratio calculation, JPEG baseline 12-bit and Monochrome1 white pixels.
* `DicomDrawRegions` has been fixed for reliability and the dependency on `python-gdcm` has been removed, making setup of the Visual NLP Python package easier.

</div><div class="h3-box" markdown="1">

## Pathology (SVS) files improvement

* Added support for non-square tile grids that enables for processing of a wider variety of files.
* Improved heuristics in layer selection for image deid to reduce processing times and memory peaks.
* Supports in-place masking of large SVS files for improved memory management.
* `remove_phi()` now fails on files with no readable pages to help spot broken input files.

</div><div class="h3-box" markdown="1">

## Databricks Cluster Setup Instructions

Updated instructions for Databricks cluster setup according to latest Databricks releases. Check the documentation [here](https://github.com/JohnSnowLabs/visual-nlp-workshop/tree/master/databricks), and related notebook [VisualNLP_DB_Cluster_Setup.ipynb](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/databricks/VisualNLP_Cluster_Setup.ipynb).

</div><div class="h3-box" markdown="1">

## New Infrastructure Stack for SVS/DICOM

![New Infrastructure Stack for SVS/DICOM](https://github.com/user-attachments/assets/7b36b372-4f74-4f40-9669-a0b73b28fd93)

In a nutshell, this architecture works as follows,

`S3 → EventBridge → Lambda → AWS Batch (EC2, c7a.2xlarge) → container → S3`

* **S3**: stores the data.
* **EventBridge**: notices that something happened.
* **Lambda**: decides what should be processed and submits a Batch job.
* **AWS Batch**: allocates compute and starts your container.
* **A container**: reads from S3, performs inference, and writes results back to S3.

The DICOM version follows the same infrastructure pattern as the SVS one, targeting DICOM files instead of `.svs` whole-slide images.

Links for both SVS and DICOM versions can be found [here](https://github.com/JohnSnowLabs/visual-nlp-workshop/tree/master/products/awsbatch).

</div><div class="h3-box" markdown="1">

## New Layout architecture & model

New `ImageObjectDetectorRtDetr` architecture: RT-DETR / RT-DETRv2 ONNX object detector with COCO labels by default, GPU option and LightPipeline support. It can detect 17 layout classes:

```
caption, footnote, formula, list_item, page_footer, page_header, picture, section_header, table, text, title, document_index, code, checkbox_selected, checkbox_unselected, form, key_value_region.
```

To see it in action check [SparkOcrLayoutDetectionRtDetr.ipynb](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrLayoutDetectionRtDetr.ipynb).

</div><div class="h3-box" markdown="1">

## Dicom Deidentification Skill

Agentic Pipeline building for Dicom Deidentification is here! The Visual NLP DICOM Skill gives an LLM a grounded way to generate John Snow Labs Visual NLP pipeline examples for specific DICOM de-identification tasks. Check blogpost [here](https://www.johnsnowlabs.com/generate-dicom-de-identification-pipelines-with-the-visual-nlp-dicom-skill/).

</div><div class="h3-box" markdown="1">

## New Pipelines

Added form support through `doc_data_loader_digital_hybrid_tables_forms_vlm1` and `doc_data_loader_digital_hybrid_tables_forms_vlm2`, and the full list of data loader pipelines is:

| Pipeline | Digital PDF | Simple Page | Complex Page | Tables | Forms |
|------------|-----------------|-------------------|---------------------|-----------|----------|
| **doc_data_loader_digital_easy** | PdfToText | V4 | V4 | N/A | N/A |
| **doc_data_loader_digital_hybrid** | PdfToText | V1 | V4 | N/A | N/A |
| **doc_data_loader_digital_hybrid_tables_vlm1** | PdfToText | V1 | vlm1 | vlm1 | N/A |
| **doc_data_loader_digital_hybrid_tables_vlm2** | PdfToText | V1 | vlm2 | vlm2 | N/A |
| **doc_data_loader_digital_hybrid_tables_forms_vlm1** | PdfToText | V1 | vlm1 | vlm1 | vlm1 |
| **doc_data_loader_digital_hybrid_tables_forms_vlm2** | PdfToText | V1 | vlm2 | vlm2 | vlm2 |

You can see these pipelines in action here: [SparkOcrDocDataLoaderPipelines.ipynb](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrDocDataLoaderPipelines.ipynb).

</div><div class="h3-box" markdown="1">

## Compatibility:
Spark-NLP 7.0.0, and Spark-NLP for Healthcare 7.0.0.

</div><div class="h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
