---
layout: model
title: Document Visual Question Answering optimized with Pix2Struct
author: John Snow Labs
name: docvqa_pix2struct
date: 2023-11-20
tags: [en, licensed, docvqa]
task: Document Visual Question Answering
language: en
nav_key: models
edition: Visual NLP 5.1.0
spark_version: 3.2.1
supported: true
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The Pix2Struct model, as detailed in the paper titled "Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding" authored by Kenton Lee, Mandar Joshi, Iulia Turc, Hexiang Hu, Fangyu Liu, Julian Eisenschlos, Urvashi Khandelwal, Peter Shaw, Ming-Wei Chang, and Kristina Toutanova, introduces a novel approach to visually-situated language understanding.

In this context, the Pix2Struct model, originally conceived as an image-to-text model for visual language understanding, has been adapted through retraining to address the specific task of answering questions within the domain of DocVQA (Document Visual Question Answering). This approach highlights the versatility and adaptability of the model for specialized tasks, demonstrating how it can be successfully applied in specific contexts such as the one mentioned.


## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/VISUAL_QUESTION_ANSWERING/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrVisualQuestionAnsweringPix2Struct.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/docvqa_pix2struct_jsl_en_5.1.0_3.0_1699645004215.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
binary_to_image = BinaryToImage()\
    .setOutputCol("image") \
    .setImageType(ImageType.TYPE_3BYTE_BGR)

visual_question_answering = VisualQuestionAnswering()\
    .pretrained("docvqa_pix2struct_jsl", "en", "clinical/ocr")\
    .setInputCol(["image"])\
    .setOutputCol("answers")\
    .setQuestionsCol("questions")

# OCR pipeline
pipeline = PipelineModel(stages=[
    binary_to_image,
    visual_question_answering
])

test_image_path = "./data/docvqa/population.jpeg"
bin_df = spark.read.format("binaryFile").load(test_image_path)

questions = [["What's the estimated population in poverty of Lawrence?",
  "What's the population of Stoddard?",
  "What is the page number of the document?",
  "What is the date of the document?"]]
questions_df = spark.createDataFrame([questions])
questions_df = questions_df.withColumnRenamed("_1", "questions")
image_and_questions = bin_df.join(questions_df)

results = pipeline.transform(image_and_questions).cache()
```
```scala
val binary_to_image = BinaryToImage()
    .setOutputCol("image") 
    .setImageType(ImageType.TYPE_3BYTE_BGR)

val visual_question_answering = VisualQuestionAnswering()
    .pretrained("docvqa_pix2struct", "en", "clinical/ocr")
    .setInputCol(Array("image"))
    .setOutputCol("answers")
    .setQuestionsCol("questions")

# OCR pipeline
val pipeline = new PipelineModel().setStages(Array(
    binary_to_image,
    visual_question_answering))

val test_image_path = "./data/docvqa/population.jpeg"
val bin_df = spark.read.format("binaryFile").load(test_image_path)

val questions = Array(Array("What's the estimated population in poverty of Lawrence?",
  "What's the population of Stoddard?",
  "What is the page number of the document?",
  "What is the date of the document?"))
val questions_df = spark.createDataFrame(Array(questions)).withColumnRenamed("_1", "questions")
val image_and_questions = bin_df.join(questions_df)

val results = pipeline.transform(image_and_questions).cache()
```
</div>

## Example

### Input:

Questions:
```bash
- What's the estimated population in poverty of Lawrence?
- What's the population of Stoddard?
- What is the page number of the document?
- What is the date of the document?                                                                                                                    
```

Image:
![Screenshot](/assets/images/examples_ocr/scanned_table.png)

### Output:
```bash
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|answers                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[What's the estimated population in poverty of Lawrence? ->  5,696, What's the population of Stoddard? ->  26,000, What is the page number of the document? ->  6, What is the date of the document? ->  January, 1970]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```


{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|docvqa_pix2struct|
|Type:|ocr|
|Compatibility:|Visual NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|

