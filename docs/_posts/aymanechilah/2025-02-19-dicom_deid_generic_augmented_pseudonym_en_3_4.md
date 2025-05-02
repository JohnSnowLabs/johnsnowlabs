---
layout: model
title: Pseudonym Dicom de-identification
author: John Snow Labs
name: dicom_deid_generic_augmented_pseudonym
date: 2025-02-19
tags: [en, licensed]
task: Dicom De-identification
language: en
nav_key: models
edition: Visual NLP 5.5.0
spark_version: 3.4.1
supported: true
recommended: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline anonymizes DICOM metadata by replacing personal identifiers with pseudonyms instead of removing them. It ensures that PHI is no longer traceable while maintaining data integrity for longitudinal studies and collaborations.

Obfuscation mode: Removes PII from images and replaces sensitive metadata values (e.g., patient names, IDs) with randomized or pseudonymized data, preserving the overall structure and usability of the metadata.

## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/PP_DICOM_DEID/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/Dicom/SparkOcrDicomPretrainedPipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
<!-- [Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/dicom_deid_generic_augmented_pseudonym_en_5.5.0_3.0_1737198071000.zip){:.button.button-orange.button-orange-trans.arr.button-icon} -->


## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
dicom_df = spark.read.format("binaryFile").load(dicom_path)

pipeline = PretrainedPipeline("dicom_deid_generic_augmented_pseudonym", "en", "clinical/ocr")

result = pipeline.transform(dicom_df).cache()
```
```scala
val dicom_df = spark.read.format("binaryFile").load(dicom_path)

val pipeline = new PretrainedPipeline("dicom_deid_generic_augmented_pseudonym", "en", "clinical/ocr")

val result = pipeline.transform(dicom_df).cache()
```
</div>

## Example

### Input:
![Screenshot](/assets/images/examples_ocr/pp_deid_metadata.png)
![Screenshot](/assets/images/examples_ocr/pp_deid_image.png)

### Output:
![Screenshot](/assets/images/examples_ocr/pp3_metadata.png)
![Screenshot](/assets/images/examples_ocr/pp3_deid.png)

## Model Information

{:.table-model}
|---|---|
|Model Name:|dicom_deid_generic_augmented_pseudonym|
|Type:|pipeline|
|Compatibility:|Visual NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|


