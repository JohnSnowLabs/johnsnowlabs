---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_6_4_2
key: docs-ocr-release-notes
modify_date: "2026-07-08"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.4.2

Release date: 08-07-2026

## Visual NLP 6.4.2 Release Notes 🕶️

**We are glad to announce that Visual NLP 6.4.2 has been released! This new release comes with new models, new pipelines, sample notebooks, bug fixes and more! 📢📢📢**

</div><div class="h3-box" markdown="1">

## Main Changes 🔴

* New MedicalVisionLLM checkpoints
* New OpenVino Text Detection + OCR models
* New OpenVino Layout Analyzer model
* New Document Pretrained Pipelines
* New Notebooks
* Bug Fixes

</div><div class="h3-box" markdown="1">

## New Models

We have two new checkpoints for MedicalVisionLLM,

* `jsl-ocr-gguf-vlm1`: this is a small VLM model supporting tasks such as text with coordinates, structured JSON output, and OCR. It is applicable to Document Processing and Deidentification pipelines.
* `jsl-ocr-gguf-vlm2`: this is a small VLM model supporting tasks such as OCR and structured JSON output. The difference with `jsl-ocr-gguf-vlm1` is that this model is slightly more accurate in OCR, but it cannot return coordinates for the text.

Check this [sample notebook](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOCRMultiModelVLM.ipynb).

We are releasing a new pair of OpenVino Text Detection + OCR models, which you can use separately or combined.

* `text_detection_v4_ov`:
```python
ImageTextDetector() \
    .pretrained("text_detection_v4_ov", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setOutputCol("regions") \
    .setSizeThreshold(10) \
    .setLinkThreshold(0.3) \
    .setTextThreshold(0.4)
```

* `text_recognition_v4_ov`:
```python
ImageToTextV4() \
    .pretrained("text_recognition_v4_ov", "en", "clinical/ocr") \
    .setInputCols(["image", "regions"]) \
    .setOutputCol("text")
```

These two models are used in pretrained pipelines `doc_data_loader_digital_easy`, and `doc_data_loader_digital_hybrid`.

</div><div class="h3-box" markdown="1">

## New OpenVino Layout Analyzer Model

This new OpenVino based detection model can return bounding boxes for the following classes: "Caption", "Footnote", "Formula", "List-item", "Page-footer", "Page-header", "Picture", "Section-header", "Table", "Text", "Title".

```python
layout_detector = ImageLayoutDetector.pretrained("image_layout_detector_ov", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setOutputCol("region") \
    .setScoreThreshold(0.4) \
    .setIouThreshold(0.1) \
    .setPredictionLabels(prediction_classes)
```

**API:**

* `setScoreThreshold(0.4)`: score threshold by which detected regions are filtered before being returned, the intuition is that the larger this score the more results you will get. Defaults to 0.4.
* `setIouThreshold(0.1)`: threshold for the Non-Maximum Suppression (NMS) algorithm to eliminate redundant, overlapping bounding boxes predicted for the same object.
* `setPredictionLabels(prediction_classes)`: a list of the classes to whitelist in the returned results, like `["Formula", "Title"]`.

</div><div class="h3-box" markdown="1">

## New Document Pretrained Pipelines

We are releasing an initial set of 4 pipelines that provide different options to parse document collections containing different complexity levels. These pipelines support all popular image types, scanned PDFs, and digital PDFs, all the routing happens internally and is transparent to the user.

| Pipeline | Digital PDF | Simple Page | Complex Page | Tables |
|------------|-----------------|-------------------|---------------------|-----------|
| **doc_data_loader_digital_easy** | PdfToText | ImageToTextV4 | ImageToTextV4 | N/A |
| **doc_data_loader_digital_hybrid** | PdfToText | ImageToTextV1 | ImageToTextV4 | N/A |
| **doc_data_loader_digital_hybrid_tables_vlm1** | PdfToText | ImageToText | VLM1 | VLM1 |
| **doc_data_loader_digital_hybrid_tables_vlm2** | PdfToText | ImageToText | VLM2 | VLM2 |

For examples on how to use please check this [sample notebook](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrDocDataLoaderPipelines.ipynb).

</div><div class="h3-box" markdown="1">

## New Notebooks

* [New Small VLMs](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOCRMultiModelVLM.ipynb). Check this notebook to learn about new small VLMs along with supported tasks such as JSON extraction, OCR, and Table Extraction.
* [Document Pretrained Pipelines](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrDocDataLoaderPipelines.ipynb). Check this notebook to learn about new document pretrained pipelines. New pipelines can handle multiple input formats, and can extract text, process tables, and forms.
* [SparkOCRDocumentLayoutAnalyzer has been updated](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOCRDocumentLayoutAnalyzer.ipynb). Check this notebook to learn how to use the new OpenVino layout analyzer.
* [SparkOcrDicomVLM.ipynb](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/Dicom/SparkOcrDicomVLM.ipynb). Check this notebook to learn about using VLMs for Dicom de-identification.
* [SparkOCRVLMDeIdentification](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/deid-and-obfuscation/SparkOCRVLMDeIdentification.ipynb). Check this notebook for Document de-identification (PDF and images) with VLMs.

</div><div class="h3-box" markdown="1">

## Bug Fixes

* LP crashed when used in multi-threading settings.
* Handling of empty regions in DicomDrawRegions.
* Fixes for DicomMetadataDeIdentifier cleanTag action behavior.
* DicomDrawRegions general improvements.

</div><div class="h3-box" markdown="1">

## Compatibility:
Spark-NLP 6.4.2, and Spark-NLP for Healthcare 6.4.1.

</div><div class="h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
