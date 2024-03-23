---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_4_4_3
key: docs-ocr-release-notes
modify_date: "2023-05-30"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 4.4.3

Release date: 33-06-2023

We are glad to announce that Visual NLP 😎 4.4.3 has been released. 

#### Highlights

In line with our unwavering dedication to delivering top-notch products, Visual NLP is backed by our steadfast commitment to quality and stability. We have meticulously addressed various issues and introduced enhancements to ensure a seamless user experience. By diligently resolving bugs, improving error handling, and expanding functionality, we prioritize the reliability and robustness of Visual NLP.

* ImageToText Auxiliary Data Download Fix:
Resolved an issue related to downloading auxiliary data in ImageToText, ensuring seamless data retrieval.

* Expanded DICOM Compression Algorithm Support:
Introduced support for additional compression algorithms in the images returned by DicomDrawRegions, including,

   * JPEGBaseline8Bit: 8-bit basic lossy JPEG encoding.
   * JPEGLSLossless: lossless JPEG encoding.
   * RLELossless: lossless run-length-encoding.

You can change it by calling the API like this,

DicomDrawRegions.setCompression(<your-method>)

The default value is RLELossless.

* Serialization Error Fix in PositionFinder:
Rectified a serialization error that previously existed in PositionFinder, resolving the issue encountered since version 4.3.2.

* Enhanced Exception Handling and Error Reporting in DICOM Transformers:
Implemented improvements in exception handling and error reporting within DICOM transformers, resulting in enhanced stability and preventing unexpected crashes. Error information is now conveniently available in the 'exception' column.

* ImageToTextV2 Introduces 'Positions' Column:
Expanded the capabilities of ImageToTextV2 to include a newly introduced 'positions' column, aligning it with similar functionality of ImageToText. The 'positions' column contains coordinates that are used to locate text in images and PDFs, and is consumed by annotators like PositionFinder.

* Resolved Path Error in DicomDrawRegions:
Rectified a path error within DicomDrawRegions, ensuring its proper functionality. Among the functionalities affected was this notebook: SparkOcrDicomDeIdentification.ipynb


* Improved Matching Strategy in PositionFinder:
PositionFinder now employs an advanced matching strategy to accurately identify the coordinates of entities, even in cases where spaces and newlines are present within the entity.
We added a more complex example to showcase capabilities: SparkOcrPDFDeIdentification.ipynb


* ImageToPdf Preserves Input Columns:
ImageToPdf has been enhanced to retain all input columns, preventing any loss of valuable data during the conversion process.


This release is compatible with Spark NLP 4.4.4 and Spark NLP for Healthcare 4.4.3.

</div><div class="prev_ver h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
