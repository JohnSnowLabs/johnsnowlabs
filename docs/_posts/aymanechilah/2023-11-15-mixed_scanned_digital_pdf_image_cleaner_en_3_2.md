---
layout: model
title: Pretrained Pipeline for Reading and Removing Noise in Mixed Scanned and Digital PDF Documents
author: John Snow Labs
name: mixed_scanned_digital_pdf_image_cleaner
date: 2023-11-15
tags: [en, licensed]
task: OCR Text Detection
language: en
nav_key: models
edition: Visual NLP 5.0.2
spark_version: 3.2.1
supported: true
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained pipeline designed to remove noise in input printed documents, enhancing OCR readability for more accurate text extraction.

## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/PP_MIXED_SCANNED_DIGITAL_PDF_IMAGE_CLEANER/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrPretrainedPipelinesMixedScannedDigitalPdfImageCleaner.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/mixed_scanned_digital_pdf_image_cleaner_en_4.3.4_3.0_1679597686000.zip){:.button.button-orange.button-orange-trans.arr.button-icon}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
pdf_pipeline = PretrainedPipeline('mixed_scanned_digital_pdf_image_cleaner', 'en', 'clinical/ocr')

pdf_path = '/content/pdfs/'
pdf_example_df = spark.read.format("binaryFile").load(pdf_path).cache()

result = pdf_pipeline.transform(pdf_example_df)
```
```scala
val pdf_pipeline = new PretrainedPipeline("mixed_scanned_digital_pdf_image_cleaner", "en", "clinical/ocr")

val pdf_path = "/content/pdfs/"
val pdf_example_df = spark.read.format("binaryFile").load(pdf_path).cache()

val result = pdf_pipeline.transform(pdf_example_df)
```
</div>


## Example

### Input
![Screenshot](/assets/images/examples_ocr/image4.png)

### Output
![Screenshot](/assets/images/examples_ocr/image4_out.png)
```bash
Sample specifications written by
 , BLEND CASING RECASING

- OLD GOLD STRAIGHT Tobacco Blend

Control for Sample No. 5030

Cigarettes:

OLD GOLD STRAIGHT

 

John H. M. Bohlken

FINAL FLAVOR MENTHOL FLAVOR

Tars and Nicotine, Taste Panel, Burning Time, Gas Phase Analysis,
Benzo (A) Pyrene Analyses — T/C -CF~ O.C S51: Fee -

Written by -- John H. M. Bohlken
Original to -Mr. C. L. Tucker, dr.
Copies to ---Dr. A. W. Spears

C

~
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|mixed_scanned_digital_pdf_image_cleaner|
|Type:|ocr|
|Compatibility:|Visual NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
