---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_4_4_4
key: docs-ocr-release-notes
modify_date: "2023-08-02"
show_nav: true
sidebar:
    nav: spark-ocr
---

<div class="h3-box" markdown="1">

## 4.4.4

Release date: 02-08-2023

We are glad to announce that Visual NLP 4.4.4 😎 has been released!
This release includes a wide array of new features and bug fixes. Our dedication to maintaining stability and upholding quality remains unwavering, and this update reflects our commitment to enhancing your experience.

* Lilt based Visual Ner Fine-Tuning: we are adding fine tuning capabilities to our Lilt-based Visual NER models. Use NLP Lab or any other source to create your data, and quickly get new models. For an end-to-end example check [this notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Ner/VisualDocumentNerFinetuning.ipynb).

* ImageTextDetector has been refactored to provide a fully JVM implementation with the same capabilities of ImageToTextV2 transformer. It includes an optimized ONNX version of the CRAFT model with a refiner network. To use this new implementation, you can call it almost exactly as ImageToTextV2,

```python
    textDetector = ImageTextDetector
      .pretrained("image_text_detector_opt", "en", "clinical/ocr")\
      .setInputCol("image")\
      .setOutputCol("region")\
      .setWidth(500)
```
The accuracy is almost the same as that of ImageTextDetectorV2.  We will continue to improve the performance, memory consumption, and accuracy of this model, and eventually deprecate ImageTextDetectorV2.
Check [this sample notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/TextDetection/SparkOcrImageTextDetection.ipynb) for an end-to-end example.


* PdfToText support for handling ligatures: ligatures are special characters that represent more than one glyph like 'ffi' or 'fl', which are used to prettify the rendering in some PDFs. The new PdfToText.setNormalizeLigatures(Boolean) will determine whether ligatures are expanded into two or more characters when returned in the 'positions' column.
Default value is true(ligatures will be expanded).
Among other things, this helps the process of matching entities to coordinates in PositionFinder.

* PositionFinder has an improved matching strategy to map entities to coordinates that prevents entities from remaining unmapped in many situations. Also, error reporting has been improved, making it clear in the logs when for some reason an entity couldn't be located in the document, and coordinates were not returned.

#### Bug Fixes & Improvements
* Serialization problems in ImageDrawRegions and ImageDrawAnnotations were fixed.
* Some dependencies have been upgraded to newer versions to maintain .
* Improved exception handling in DicomDrawRegions(duplicated exceptions) & ImageTextDetectorV2(crash).

This release is compatible with Spark-NLP 4.4.4 and Spark-NLP for Healthcare 4.4.3

</div><div class="prev_ver h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
