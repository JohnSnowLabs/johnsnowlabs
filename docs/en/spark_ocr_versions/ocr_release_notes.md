---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/ocr_release_notes
key: docs-ocr-release-notes
modify_date: "25-11-2026"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 7.0.1

Release date: 25-11-2026

## Visual NLP 7.0.1 Release Notes 🕶️

**We are glad to announce that Visual NLP 7.0.1 has been released! This release brings new fast text detectors, a logo detector, de-identification of digital PDFs, and many improvements in Dicom and SVS processing. 📢📢📢**

</div><div class="h3-box" markdown="1">

## Main Changes 🔴

* New `ImageTextDetectorFast` and `ImageTextDetectorLite`: fast OpenVINO text detectors that run on CPU.
* New `ImageLogoDetector` to find logos in document images.
* New `PdfDeidentifier`: de-identification of digital PDFs that keeps the output PDF digital.
* Dicom improvements: wildcard and private tag rules in strategy files, more reliable de-identification of tags, and lower memory usage.
* Pathology (SVS) improvements: a simpler API, a blanket de-identification mode, and better detection of PHI.
* A new data loader pipeline and many bug fixes.
* Support for PySpark up to 4.x.

</div><div class="h3-box" markdown="1">

## New Text Detectors: ImageTextDetectorFast and ImageTextDetectorLite

Two new text detectors that use OpenVINO (f32) models. They are a fast alternative to `ImageTextDetectorCraft` in CPU pipelines.

```python
text_detector = ImageTextDetectorFast.pretrained("image_text_detector_fast_ov", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setOutputCol("text_regions")

# or

text_detector = ImageTextDetectorLite.pretrained("image_text_detector_lite_ov", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setOutputCol("text_regions")
```

* `setWidth()` and `setHeight()` set the input size of the model. The default, 0, keeps the current behavior (`limitSideLength` for Fast, `longSide` for Lite). If you set only one side, the other one keeps the aspect ratio of the image.
* New `flagRegionsCol` param, also in `ImageTextDetectorCraft`: images with no regions in this column are skipped and return no regions. This replaces the `SQLTransformer` stages used in Dicom flagging pipelines, and saves time when only some images need OCR.

To see them in action check [SparkOcrDicomFlaggingPretrainedPipelines.ipynb](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/Dicom/SparkOcrDicomFlaggingPretrainedPipelines.ipynb).

</div><div class="h3-box" markdown="1">

## New Logo Detector

New `ImageLogoDetector`, a YOLO ONNX detector that finds logos in images.

```python
logo_detector = ImageLogoDetector.pretrained("logo_detector_v1", "en", "clinical/ocr") \
    .setInputCol("image") \
    .setOutputCol("logo_regions") \
    .setScoreThreshold(0.55)
```

You can see this model in action here: [SparkOcrImageLogoDetection.ipynb](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrImageLogoDetection.ipynb).

</div><div class="h3-box" markdown="1">

## Digital PDF De-identification

New `PdfDeidentifier` replaces the detected entities in the text of digital PDFs, with no need to turn pages into images. The result is still a digital PDF: fonts, layout and the rest of the page stay as they were.
A few settings worth mentioning,

* `aggregatePages` (default `True`): merges the pages of each document into one de-identified PDF.
* `fitToWidth`: scales each replacement to the width of the original text.
* `wholeWords`: replaces matches on word boundaries only.
* `allOccurrences`: a cursor is kept both in the entities and in the document to track the position at which the input entities are located in the PDF, and by default each input entity replaces one occurrence, the next one in the document. When this setting is `True`, every other whole-word occurrence of the entity text in the PDF is also replaced.

To see it in action check [ObfuscationDigitalPDF.ipynb](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/deid-and-obfuscation/ObfuscationDigitalPDF.ipynb).

</div><div class="h3-box" markdown="1">

## Dicom Changes

* Strategy files now support wildcard and private tag rules. `DicomToMetadata` and `DicomMetadataDeidentifier` share the same rule parser, so both stages always select the same tags:
  * `(0029, *)`: every element of a group, at any depth. `x` matches any hex digit, for example `(60xx, *)` covers the overlay groups 6000-60FF.
  * `(PRIVATE)`: every private data element, at any depth.
  * The VR column of a wildcard rule can be `*` (any VR), `TEXT` (PN, LO, SH, ST, LT, UT, UC), or a list like `LO|LT`.
  * Wildcard rules support the `cleanTag`, `delete` and `remove` actions. Exact rules always take precedence over wildcards.
  * Legacy group rules like `"(0020,)",GROUP,...` keep working.
* `DicomMetadataDeidentifier` now maps NER results to tags by the original position of each document, instead of by order. There's a new `tagTextCol` param to support this new mechanism, with default `tag_text`.
* New `lazyFrameRead` param in `DicomToImageV3` (default `True`): reads frames one at a time instead of loading all the frames of a multi-frame file into memory during frame extraction.
* Support for compressed images in `DicomToImageV3`.
* New utilities to save Dicom files and work with their metadata.
* Fixes in blanket de-identification and `DicomDrawRegions`.
* `ImageTableDetector` now supports `useGPU`.

</div><div class="h3-box" markdown="1">

## Pathology (SVS) files improvement

* Simpler de-identification API, which replaces the previous tile functions:
  * `svs_to_images()` writes a low-resolution image of the slide and its thumbnail. Run any image de-identification pipeline on them.
  * `redact_phi_in_svs()` takes the regions the pipeline found and draws them on every pyramid level of the slide and on its thumbnail. It can modify the original file or write a new one.
  * `get_overlapping_tiles()` lists the tiles that `redact_phi_in_svs()` would rewrite, without changing anything.
* PHI is detected on an image of the whole slide and on its thumbnail, so words are no longer cut across tiles and text written on the slide, such as pen annotations, is found more reliably.
* Faster redaction, through threaded tile redrawing and a vectorized JPEG encoder.
* `remove_phi()` can now write a single slide into an output folder.

</div><div class="h3-box" markdown="1">

## New Pipelines & Models

* `image_text_detector_fast`: a drop-in replacement for our previous text detectors. It is about 5x faster than the fastest one we had before (CRAFT OpenVINO), 6-7x faster end to end in the Dicom de-identification pipelines, and it finds more of the text (89% of the text regions against 82-83%, measured in multiple datasets).

* `image_text_detector_lite`: a `flagging` model that detects the presence of text with high recall. It is a blazing-fast model (about 12 ms per image with OpenVINO, **on CPU!**) that can be applied at the very beginning of OCR/NLP pipelines to rule out frames/pages without text.

* `logo_detector_v1`: detects logos (graphic marks and brand wordmarks) in document images, so they can be masked or obfuscated instead of being read as text. On 200 [FATURA](https://arxiv.org/abs/2311.11856) invoices (CC BY 4.0) from templates not used in training, at the default threshold (0.55): precision 1.00, recall 1.00, mAP50-95 0.91. About 70 ms per page **on CPU**.

* `dicom_deid_generic_augmented_fast`: a Dicom de-identification pipeline that uses the image_text_detector_fast text detector defined above + the deid_generic_augmented (https://nlp.johnsnowlabs.com/2021/06/30/ner_deid_generic_augmented_en.html) NLP pipeline.

* `dicom_deid_generic_augmented_flagging`: the same as above, but using `image_text_detector_lite` at the very beginning to flag the frames without text and skip them altogether. It pays off on datasets where many frames have no text.

* `dicom_deid_generic_augmented_flagging_ov`: the same as above with the OpenVINO version of image_text_detector_lite. This is the fastest of the three pipelines.

</div><div class="h3-box" markdown="1">

## Bug Fixes

* `ImageToTextV2` returns empty text when the detector finds no regions, in-line with `ImageToTextV3`. Without a regions column it still reads the whole image.
* `ImageToTextV2`, `ImageToTextV3` and `ImageToTextV4` crop input regions to the image area, and drop regions outside it. This increases the quality of the final output.
* Saving `ImageTextDetectorCraft` OpenVINO models with refiner has been fixed.
* Image transformers (`ImageAdaptiveThresholding`, `ImageErosion`, `ImageEnhanceContrast`, `ImageRemoveGlare`, `ImageRemoveObjects`, `ImageSkewCorrector`, `ImageScaler`, binarizers, and others) and `ImageInpainting` now support compressed images at the input.
* Fixed positions in `DocumentCoordinatesToText`, and a merging issue in `RegionsMerger`.

</div><div class="h3-box" markdown="1">

## Compatibility:
Spark-NLP 7.0.1, and Spark-NLP for Healthcare 7.0.1. PySpark `>=3.0.0,<=4.3.0`.

</div><div class="h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
