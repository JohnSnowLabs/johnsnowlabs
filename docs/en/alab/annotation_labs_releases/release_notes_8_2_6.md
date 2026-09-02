---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 8.2.6
permalink: /docs/en/alab/annotation_labs_releases/release_notes_8_2_6
key: docs-licensed-release-notes
modify_date: 2026-09-02
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">

**Generative AI Lab 8.2.6** is an improvement release focused on DICOM processing and usability. This release expands DICOM OCR compatibility, improves zoom and pan interactions for medical images, and increases the supported task file name length to accommodate longer file names commonly found in DICOM and other medical documents.

## Improvements

### Increased Task File Name Length

**What's Improved**

The maximum supported task file name length has been increased to 150 characters, allowing files with longer names to be imported and processed without exceeding the previous file name restriction.
This is particularly useful for DICOM files and other medical documents, where file names may contain longer identifiers or descriptive information.

### Expanded DICOM OCR Compatibility

**What's Improved**

The DICOM OCR import pipeline has been enhanced to support a broader range of valid DICOM images and encoding scenarios.

DICOM processing now provides improved handling of JPEG Lossless pixel data, missing overlay information, and image extraction conditions that could previously interrupt OCR processing. These changes improve compatibility across different DICOM sources and make the import pipeline more resilient when processing heterogeneous medical imaging datasets.

### Improved Zoom and Pan for DICOM Images

**What's Improved**

Zoom and pan interactions have been improved for DICOM images, providing smoother and more reliable navigation when inspecting medical images within annotation tasks.

Users can more easily enlarge image regions and reposition the image while reviewing detailed visual content.



---
## Versions

</div>

{%- include docs-annotation-pagination.html -%}