---
layout: model
title: Pretrained Pipeline for Reading Printed Text with Image Documents
author: John Snow Labs
name: image_printed_transformer_extraction
date: 2023-11-15
tags: [en, licensed, printed, ocr]
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

Pretrained pipeline designed to extract printed text from document images. It empowers accurate and efficient conversion of printed content into digital text, making it an invaluable tool for text recognition tasks.


## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/PP_IMAGE_PRINTED_TRANSFORMER_EXTRACTION/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrPretrainedPipelinesImagePrintedTransformerExtraction.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/image_printed_transformer_extraction_en_5.0.2_3.0_1699469925000.zip){:.button.button-orange.button-orange-trans.arr.button-icon}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
img_pipeline = PretrainedPipeline('image_printed_transformer_extraction', 'en', 'clinical/ocr')

img_path = '/content/images/'
img_example_df = spark.read.format("binaryFile").load(img_path).cache()

result = img_pipeline.transform(img_example_df)
```
```scala
val img_pipeline = new PretrainedPipeline("image_printed_transformer_extraction", "en", "clinical/ocr")

val img_path = "/content/images/"
val img_example_df = spark.read.format("binaryFile").load(img_path).cache()

val result = img_pipeline.transform(img_example_df)
```
</div>

## Example

### Input
![Screenshot](/assets/images/examples_ocr/image2.png)

### Output
```bash
STARBUCKS Store #19208
11902 Euclid Avenue
Cleveland, OH (216) 229-U749

CHK 664250
12/07/2014 06:43 PM
112003. Drawers 2. Reg: 2

¥t Pep Mocha 4.5
Sbux Card 495
AMXARKERARANG 228
Subtotal $4.95
Total $4.95
Change Cue BO LOO
- Check Closed ~

"49/07/2014 06:43 py

oBUX Card «3228 New Balance: 37.45
Card is registertd
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|image_printed_transformer_extraction|
|Type:|pipeline|
|Compatibility:|Visual NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
