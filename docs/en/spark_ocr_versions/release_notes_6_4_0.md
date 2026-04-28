---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_6_4_0
key: docs-ocr-release-notes
modify_date: "2026-04-28"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.4.0

Release date: 28-04-2026

## Visual NLP 6.4.0 Release Notes 🕶️

**We are glad to announce that Visual NLP 6.4.0 has been released! Dicom improvements, a new OCR engine, and much more. 📢📢📢**

</div><div class="h3-box" markdown="1">

## Main Changes 🔴

* Dicom Processing Improvements
* New Optimized Fast Dicom Pipeline
* New V4 OCR engine
* New Yolo based Layout analysis model
* New OpenVino Text Detector model
* Two new AWS Marketplace listings

</div><div class="h3-box" markdown="1">

## Dicom Processing Improvements

Dicom processing pipelines now support sampling of the frames in each study. This new strategy allows pipelines to run faster by looking into only a subset of all the frames in the study. The changes are spread across different components.

### DicomToImageV3 Changes

* Added a new param `setFrameSamplingStrategy()`. Valid values are `['Consecutive', 'Stride', 'Random', 'Middle']` for sub-sampling the frames.
* Added a new param `setFrameDimsCol()`, which contains metadata information about the image.
* Fixed the selection of frames via `setInputCols()`: `DicomToImageV3` accepts a column `parts`, which is a per-dicom-file integer list representing a cherry-picked list of frame ids.

```python
DicomToImageV3.setInputCols(['content', 'parts'])
```

Some corner cases were fixed in this feature.

* Added page number information in the `pagenum` col.

### DicomDrawRegion Changes

* This component renders the regions into the frames of the input dicoms. When frame sampling was performed in previous stages, this component will now perform the extrapolation of the regions that were analyzed to all the frames in the dicom file.

### DicomMetadataDeidentifier

* Added guardrails for `remove`, `delete`, and `replaceWithLiteral` actions when applied to VR SQ.
* Added support for removing or deleting group tags through a group strategy file via `setGroupStrategyFile("group_strategy.csv")`, for example deletion of all overlay tags in group `60xx`.
* Improved private tag removal with `setRemovePrivateTags(True)` to consistently delete private tags from the DICOM file.
* Improved tracking of DICOM object references to better preserve and trace metadata tag operations.

If you do not want to build from scratch, but want to leverage this and other optimizations, check the next section.

</div><div class="h3-box" markdown="1">

## New Optimized Fast Dicom Pipeline

This new pipeline leverages image re-scaling, compression, and frame sub-sampling for improved performance. Just call it like this:

```python
from sparkocr.pretrained import DicomPretrainedPipeline
dcm_pipe = DicomPretrainedPipeline("dicom_deid_fully_optimized")
clean_dcm_df = dcm_pipe.transform(dicom_df)
```

</div><div class="h3-box" markdown="1">

## New V4 OCR engine

This model is a new OCR model that operates with an external Text Detector for high-recall use cases such as de-identification. Contrary to V2 families, which were Transformer-based, this one is CNN-based, which allows it to deliver reasonable throughput even on CPU. The model is competitive accuracy-wise as well.

```python
text_detector = ImageTextDetectorCraft()\
  .pretrained("text_detection_v4", "en", "clinical/ocr")\
  .setInputCol("image")\
  .setOutputCol("regions")\
  .setSizeThreshold(10)\
  .setLinkThreshold(0.3)\
  .setTextThreshold(0.4)\
  .setWithRefiner(False)

text_extractor = ImageToTextV4()\
  .pretrained("text_recognition_v4", "en", "clinical/ocr")\
  .setInputCols(["image", "regions"])\
  .setOutputCol("text")
```

</div><div class="h3-box" markdown="1">

## New Yolo based Layout analysis model

This new model can detect layout entities `{Text, Title, List, Table, Figure}`. It is similar in accuracy to other DiT-based models in the library, but with a speed-up of up to 10X over DiT options such as `ImageLayoutAnalyzerDit`.

This is how you use it:

```python
doc_layout = DocumentLayoutAnalyzer \
    .pretrained("doc_layout_jsl", "en", "clinical/ocr")
```

</div><div class="h3-box" markdown="1">

## New OpenVino Text Detector model

Our `ImageTextDetector` annotator, which is used in many OCR and de-identification pipelines, now supports checkpoints with OpenVino. To use it, call the annotator exactly the same way, but pass the `image_text_detector_open_vino` model name like this:

```python
ImageTextDetector.pretrained("image_text_detector_open_vino", "clinical/ocr", "en")
```

This model delivers a speed-up of around `2.2X` when used on CPUs that support AI acceleration features such as `AVX-512`, `VNNI`, and `bfloat16`. For example, AWS's [C7a family](https://aws.amazon.com/ec2/instance-types/c7a/).

</div><div class="h3-box" markdown="1">

## Two new AWS Marketplace listings

* [Vision OCR LLM](https://aws.amazon.com/marketplace/pp/prodview-d7un4r7xpiwje): highly accurate text extraction model.
* [Vision OCR Structured LLM](https://aws.amazon.com/marketplace/pp/prodview-rrpnzcxjmhtfy): a highly accurate VLM-based text extraction model that can handle text and tables.

</div><div class="h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
