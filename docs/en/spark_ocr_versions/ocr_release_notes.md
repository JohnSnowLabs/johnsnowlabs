---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/ocr_release_notes
key: docs-ocr-release-notes
modify_date: "2025-05-09"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.3.0

Release date: 02-02-2026

## Visual NLP 6.3.0 Release Notes 🕶️

**We are glad to announce that Visual NLP 6.3.0, has been released! 📢📢📢**

</div><div class="h3-box" markdown="1">

## Main Changes 🔴

* Dicom Midi-B benchmarks.
* New features in: DicomToMetadata and DicomMetadataDeIdentifier.
* New Blogposts and notebooks.
* Bug Fixes and Maintenance

</div><div class="h3-box" markdown="1">
## Dicom Midi-B benchmarks
In this release, we tackled the [Midi-B dataset for Dicom De-identification](https://www.cancerimagingarchive.net/collection/midi-b-test-midi-b-validation/). Midi-B is a popular dataset for the Dicom De-Identification Task that appeared in 2025. Today we are releasing benchmarks, and a notebook to reproduce results.


</div><div class="h3-box" markdown="1">
## Benchmarks
The metrics in Midi-B dataset are organized as a set of accuracy numbers across a predefined set of actions. Two different subsets are provided, Validation and Test. We report results for both datasets and each of the actions defined in the dataset.

![Validation Report(Validation) MIDI-B.](/assets/images/ocr/midi_b_table_val.png)
![Validation Report(Test) MIDI-B.](/assets/images/ocr/midi_b_table_test.png)

## Notebooks

You can find all the details for how to run over the MIDI-B dataset in this notebook: [SparkOcrMIDIBSolution.ipynb](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/Dicom/SparkOcrMIDIBSolution.ipynb)
</div><div class="h3-box" markdown="1">

## New features in: DicomToMetadata and DicomMetadataDeIdentifier

### DicomToMetadata

Exposing tags to enable external NLP to operate on them.
* Added support for strategy file-driven configuration via the setStrategyFile parameter: a strategy file is a configuration file that helps in defining actions like the ones described in the charts above.
* Enabled the extraction of raw metadata tag value for all tags marked with cleanTag in the strategy file. As a result, a String column will be created in the output dataframe. The name of the output column for this raw tag text is configurable via setTagCol. The purpose of this column is to expose the content of the tags that are in natural language so the redaction can be carried out using NLP methods.
* Enabled extraction of tag mappings for all tags marked with the cleanTag action, as described in the item above, configurable through setTagMappingCol. This output column allows to map the tags values present in the tag column back to the original tag identifiers.
* Introduced setExtractTagForNer to optionally skip String tag extraction.

</div><div class="h3-box" markdown="1">

### DicomMetadataDeidentifier

DicomMetadataDeidentifier is the component in charge of redacting metadata tags in Dicom files. It can apply a wide variety of actions, some of which are pre-defined, and some of which are user-defined.
In this release, new actions were added:
* Added a new action shiftTimeByRandom (VR: TM) to randomly shift time values.
* Added two new actions shiftDateByFixedNbOfDays and shiftDateByRandomNbOfDays (VR: DA, DT) to shift date and datetime values.
* Added a new action shiftUnixTimeStampRandom (VR: SL, FD) to randomly shift Unix timestamp values.
* Added a new action ensureTagExists (VR: ALL) to ensure a tag exists with a default value.
Some other changes,
* Improved date and datetime handling to support all valid DICOM date formats.
* Improved hashUID and patientHashID implementations in accordance with DICOM guidelines.
* Added the ability to remove residual PHI post de-identification, ensuring sensitive metadata is fully cleared from the DICOM file.


</div><div class="h3-box" markdown="1">

## New Blogposts and notebooks

* Deidentifying Whole Slide Images(WSI) and deploying in SageMaker. Link [here](https://medium.com/john-snow-labs/de-identifying-whole-slide-images-wsi-deploying-on-sagemaker-part-3-25a4c57805c4).
* JSL-Vision vs. Closed Source Models Comparison. Link [here](https://medium.com/john-snow-labs/jsl-vision-vs-closed-source-models-document-intelligence-without-compromise-62728afe0c5b).
* JSL-Vision vs. Open-Source Models Comparison. Link [here](https://medium.com/john-snow-labs/jsl-vision-state-of-the-art-document-understanding-on-your-hardware-f4862f15d9f9).
* De-identifying Dicom files a step-by-step guide . Link [here](https://medium.com/john-snow-labs/de-identifying-dicom-files-a-step-by-step-guide-with-john-snow-labs-visual-nlp-2c21b60f92a8).

</div><div class="h3-box" markdown="1">

## Bug Fixes

* Improved support for accessing Python resources across different Python versions.
* Compatibility with Google Colab.

</div><div class="h3-box" markdown="1">

## Compatibility: 
Spark-NLP 6.3.2, and Spark-NLP for Healthcare 6.3.0, LV 1.11.0.
</div><div class="h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
