---
layout: model
title: Chart to Text
author: John Snow Labs
name: chart_to_text_deplot_jsl
date: 2024-04-15
tags: [en, licensed]
task: Chart to Text
language: en
nav_key: models
edition: Visual NLP 5.2.0
spark_version: 3.2.1
supported: true
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description


DePlot, as outlined in the paper "DePlot: One-shot visual language reasoning by plot-to-table translation," offers a groundbreaking one-shot solution for visual language reasoning, requiring minimal training data compared to previous models. By breaking down the process into plot-to-text translation and subsequent reasoning, DePlot converts images of plots or charts into structured tables, enabling pretrained large language models (LLMs) to perform robust reasoning with just a few prompts. Trained end-to-end on standardized tasks, DePlot demonstrates a significant 24.0% improvement over state-of-the-art models on human-written queries, showcasing its efficiency even with limited data. Integrated within the Pix2Struct architecture, DePlot excels in Visual Question Answering tasks, rendering input questions on images and accurately predicting answers.


## Predicted Entities


{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/PDF_CHART_TO_TEXT/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrPdfToChartToTextLLM.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/chart_to_text_deplot_jsl_en_5.2.0_3.0_1708181444215.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/chart_to_text_deplot_jsl_en_5.2.0_3.0_1708181444215.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}


## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
binary_to_image = BinaryToImage()\
    .setOutputCol("image") \
    .setImageType(ImageType.TYPE_3BYTE_BGR)

chart_to_text = ChartToTextTable()\
    .pretrained("chart_to_text_deplot_jsl", "en", "clinical/ocr")\
    .setInputCol(["image"])\
    .setOutputCol("answers")\
    .setUseCaching(False)

# OCR pipeline
pipeline = PipelineModel(stages=[
    binary_to_image,
    chart_to_text
])

image_path = pkg_resources.resource_filename('sparkocr', 'resources/ocr/images/figure.jpg')
image_example_df = spark.read.format("binaryFile").load(image_path)

result = pipeline.transform(image_example_df).cache()
```
```scala
val binary_to_image = BinaryToImage()
    .setOutputCol("image")
    .setImageType(ImageType.TYPE_3BYTE_BGR)

val chart_to_text = ChartToTextTable()
    .pretrained("chart_to_text_deplot_jsl", "en", "clinical/ocr")
    .setInputCol(Array("image"))
    .setOutputCol("answers")
    .setUseCaching(False)

val pipeline = new PipelineModel().setStages(Array(
    binary_to_image,
    chart_to_text))

val image_path = pkg_resources.resource_filename("sparkocr", "resources/ocr/images/figure.jpg")
val image_example_df = spark.read.format("binaryFile").load(image_path)

val result = pipeline.transform(image_example_df).cache()
```
</div>

## Example

### Input:

![Screenshot](/assets/images/examples_ocr/figure.png)

### Output:
```bash
|[  TITLE |  <0x0A> AGE RANGE | MAL | FEMALE <0x0A> <50 | 0.70 | 1.10 <0x0A> 50-64 | 6.10 | 8 <0x0A> 65-74 | 16.40 | 15.10 <0x0A> 75-84 | 26.50 | 20.10 <0x0A> 85+ | 42.50 | 31.60] |
```


{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|chart_to_text_deplot_jsl|
|Type:|ocr|
|Compatibility:|Visual NLP 5.2.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|

