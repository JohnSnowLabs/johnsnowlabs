---
layout: model
title: Pretrained Pipeline for Table Structure Extraction
author: John Snow Labs
name: basic_table_extractor
date: 2024-09-30
tags: [en, licensed]
task: Table Structure Extraction
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

This is a pretrained pipeline designed for conducting Table Structure Extraction on mixed scanned and digital PDF documents. The model accurately identifies and extracts tables from PDFs, regardless of whether the document is scanned or digitally generated. By analyzing the structure and layout of the document, it can effectively detect tables, identify rows, columns, and cell boundaries, and reconstruct the table's structure in a usable format.

## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/PP_BASIC_TABLE_EXTRACTOR/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrPretrainedPipelinesBasicTableExtractor.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/basic_table_extractor_en_5.3.2_3.0_1715800396000.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/basic_table_extractor_en_5.3.2_3.0_1715800396000.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}


## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
pipeline = PretrainedPipeline('basic_table_extractor', 'en', 'clinical/ocr')

pdf_path = '/content/pdfs/'
pdf_example_df = spark.read.format("binaryFile").load(pdf_path).cache()

result = pipeline.transform(pdf_example_df)
```
```scala
val pipeline = new PretrainedPipeline("basic_table_extractor", "en", "clinical/ocr")

val pdf_path = "/content/pdfs/"
val pdf_example_df = spark.read.format("binaryFile").load(pdf_path).cache()

val result = pipeline.transform(pdf_example_df)
```
</div>

## Example

{%- capture input_image -%}
![Screenshot](/assets/images/examples_ocr/table4_1.jpg)
{%- endcapture -%}

{%- capture output_image -%}
![Screenshot](/assets/images/examples_ocr/table4_1-output.jpg)
{%- endcapture -%}

{% include templates/input_output_image.md
input_image=input_image
output_image=output_image
%}

## Model Information

{:.table-model}
|---|---|
|Model Name:|basic_table_extractor|
|Type:|ocr|
|Compatibility:|Visual NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|


