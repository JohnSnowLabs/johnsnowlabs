---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_5_4_2
key: docs-ocr-release-notes
modify_date: "2024-11-12"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.4.2

Release date: 12-11-2024

## Visual NLP 5.4.2 Release Notes 🕶️

**We are glad to announce that Visual NLP 5.4.2 has been released!. This is a small release with improvements in Dicom Processing, and some bug fixes. 📢📢📢**

</div><div class="h3-box" markdown="1">

## Highlights 🔴

* Dicom Improvements: better general support for Dicom files, improved dependency resolution in Dicom Transformers, and other minor changes.
* Other Changes: GPU support in ImageTextDetector, and new SVS de-identification tool.

## Dicom Improvements
* Improved support for different Transfer Syntaxes, now all transfer syntaxes as stated by the Dicom Standard are supported.

* Dependency resolution of external packages improved, Dicom dependencies will be pulled into the environment only when the user requires Dicom functionalities. Also, the support for different environments and different Python versions has been improved.

* Support for a placeholder text in DicomMetadataDeidentifier to mark metadata values that have been removed. 
Example,
 ```
# Text to be used to replace values of blacklisted tags.
DicomMetadataDeidentifier.setPlaceholderText("anonymous")
 ```
* display_dicom() function now displays overlay data properly.

</div><div class="h3-box" markdown="1">

## Other Changes
* ImageTextDetector now supports GPU, to enable it, call 

```
ImageTextDetector.setUseGPU(True)
```

* New PHI removal tool: this is a new functionality to process SVS files and remove sensitive metadata and associated images. By default, macro images, label images, and specific metadata tags: "ImageDescription.Filename", "ImageDescription.Date", "ImageDescription.Time", and "ImageDescription.User" are removed.
Tags to be removed can be customized.

Example,

```
from sparkocr.utils.svs.deidentifier import remove_phi
 
input_path = "./inputs"
output_path = "./outputs"
remove_phi(input, output)


# with customized tags
remove_phi(input, output, tags=["ImageDescription.ScannerSerialId"])
```
 
For more details check this [sample notebook](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/misc/svs-deidentification.ipynb).
 
* Dicom Documentation has been extended to cover every Dicom Transformer in the library. Take a look [here](https://nlp.johnsnowlabs.com/docs/en/ocr_pipeline_components#dicom-processing).



## Bug Fixes

* Python Transformers now can work in PretrainedPipelines.
* Model Downloader errors on newer Spark versions are now solved.

 

This release is compatible with Spark-NLP 5.4.1, and Spark NLP for Healthcare 5.4.1.

</div><div class="h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
