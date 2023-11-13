---
layout: model
title: Pretrained Pipeline for Reading Handwritten Text with Image Documents
author: John Snow Labs
name: image_handwritten_transformer_extraction
date: 2023-11-06
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

Pretrained pipeline designed to extract handwritten text from document images. It empowers accurate and efficient conversion of handwritten content into digital text, making it an invaluable tool for text recognition tasks.


## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/PP_IMAGE_HANDWRITTEN_TRANSFORMER_EXTRACTION/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/tutorials/SparkOcrPretrainedPipelinesImageHandwrittenTransformerExtraction.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/image_handwritten_transformer_extraction_en_5.0.2_3.0_1680289435000.zip){:.button.button-orange.button-orange-trans.arr.button-icon}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
img_pipeline = PretrainedPipeline('image_handwritten_transformer_extraction', 'en', 'clinical/ocr')

img_path = '/content/images/'
img_example_df = spark.read.format("binaryFile").load(img_path).cache()

result = img_pipeline.transform(img_example_df)
```
```scala
val img_pipeline = new PretrainedPipeline("image_handwritten_transformer_extraction", "en", "clinical/ocr")

val img_path = "/content/images/"
val img_example_df = spark.read.format("binaryFile").load(img_path).cache()

val result = img_pipeline.transform(img_example_df)
```
</div>

## Example

### Input
![Screenshot](/assets/images/examples_ocr/image3_1.jpg)

### Output
```bash
This is an example of handwritten
text .
Let's # check the performance !
I hope it will be awesome .
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|image_handwritten_transformer_extraction|
|Type:|ocr|
|Compatibility:|Visual NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
