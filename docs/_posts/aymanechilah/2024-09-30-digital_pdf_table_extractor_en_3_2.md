---
layout: model
title: Pretrained Pipeline for Table Extraction
author: John Snow Labs
name: digital_pdf_table_extractor
date: 2024-09-30
tags: [en, licensed]
task: Table Extraction
language: en
nav_key: models
edition: Visual NLP 5.4.0
spark_version: 3.2.1
supported: true
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained pipeline for conducting Table Extraction on mixed scanned and digital PDF documents. It ensures precise and efficient table extraction from PDFs of various origins and formats by first detecting tables in the input documents and then extracting the table structure.


## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/PP_DIGITAL_PDF_TABLE_EXTRACTOR/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrPretrainedPipelinesMixedScannedDigitalPdf.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/digital_pdf_table_extractor_en_5.3.2_3.0_1715800396000.zip){:.button.button-orange.button-orange-trans.arr.button-icon} -->
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/digital_pdf_table_extractor_en_5.3.2_3.0_1715800396000.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}


## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
pipeline = PretrainedPipeline('digital_pdf_table_extractor', 'en', 'clinical/ocr')

pdf_path = '/content/pdfs/'
pdf_example_df = spark.read.format("binaryFile").load(pdf_path).cache()

result = pipeline.transform(pdf_example_df)
```
```scala
val pipeline = new PretrainedPipeline("digital_pdf_table_extractor", "en", "clinical/ocr")

val pdf_path = "/content/pdfs/"
val pdf_example_df = spark.read.format("binaryFile").load(pdf_path).cache()

val result = pipeline.transform(pdf_example_df)
```
</div>

## Example

{%- capture input_image -%}
![Screenshot](/assets/images/examples_ocr/BiomedPap_bio-202402-0013-3.jpg)
{%- endcapture -%}

{%- capture output_image -%}
![Screenshot](/assets/images/examples_ocr/BiomedPap_bio-202402-0013-3-output.jpg)
{%- endcapture -%}

{% include templates/input_output_image.md
input_image=input_image
output_image=output_image
%}

## Model Information

{:.table-model}
|---|---|
|Model Name:|digital_pdf_table_extractor|
|Type:|ocr|
|Compatibility:|Visual NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|


