---
layout: model
title: Pretrained Pipeline for Reading Handwritten Text with PDF Documents
author: John Snow Labs
name: pdf_handwritten_transformer_extraction
date: 2023-11-15
tags: [en, licensed, handwritten, pdf, ocr]
task: OCR Text Detection
language: en
nav_key: models
edition: Visual NLP 5.0.2
spark_version: 3.2.1
supported: true
recommended: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained pipeline designed to extract handwritten text from document PDFs. It empowers accurate and efficient conversion of handwritten content into digital text, making it an invaluable tool for text recognition tasks.


## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/PP_PDF_HANDWRITTEN_TRANSFORMER_EXTRACTION/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrPretrainedPipelinesPdfHandwrittenTransformerExtraction.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/pdf_handwritten_transformer_extraction_en_5.0.2_3.0_1699469925000.zip){:.button.button-orange.button-orange-trans.arr.button-icon}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
pdf_pipeline = PretrainedPipeline('pdf_handwritten_transformer_extraction', 'en', 'clinical/ocr')

pdf_path = '/content/pdfs/'
pdf_example_df = spark.read.format("binaryFile").load(pdf_path).cache()

result = pdf_pipeline.transform(pdf_example_df)
```
```scala
val pdf_pipeline = new PretrainedPipeline("pdf_handwritten_transformer_extraction", "en", "clinical/ocr")

val pdf_path = "/content/pdfs/"
val pdf_example_df = spark.read.format("binaryFile").load(pdf_path).cache()

val result = pdf_pipeline.transform(pdf_example_df)
```
</div>

## Example

### Input
![Screenshot](/assets/images/examples_ocr/image3_1.jpg)

### Output
```bash
"This is an example of handwritten
text .
Let's # check the performance !
I hope it will be awesome ."
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|pdf_handwritten_transformer_extraction|
|Type:|pipeline|
|Compatibility:|Visual NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
