---
layout: model
title: Document Visual Question Answering with Pix2Struct
author: John Snow Labs
name: docvqa_pix2struct
date: 2023-11-10
tags: [en, licensed]
task: Question Answering
language: en
edition: Visual NLP 5.1.0
spark_version: 3.2
supported: true
annotator: VisualQuestionAnsweringPix2Struct
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pix2Struct is an image encoder - text decoder model. This model is trained for Document Visual Question Answering (DocVQA).

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/docvqa_pix2struct_en_5.1.0_3.2_1699645004215.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/docvqa_pix2struct_en_5.1.0_3.2_1699645004215.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
binary_to_image = BinaryToImage()\
    .setInputCol("content") \
    .setOutputCol("image") \
    .setImageType(ImageType.TYPE_3BYTE_BGR)

visual_question_answering = VisualQuestionAnswering()\
    .pretrained("docvqa_pix2struct", "en", "clinical/ocr")\
    .setInputCol(["image"])\
    .setOutputCol("answers")\
    .setQuestionsCol("questions")

# OCR pipeline
pipeline = PipelineModel(stages=[
    binary_to_image,
    visual_question_answering
])

```
```scala
    val imageDf = spark.read.format("binaryFile").load(image_path)
    val questions = Seq(Array(
      "When is the Coffee Break?"
      )).toDF("questions")
    val imageWithQuestions = imageDf.join(questions)

    val binaryToImage = new BinaryToImage()
    .setOutputCol("image")
    .setImageType(BufferedImage.TYPE_3BYTE_BGR)

    val visualQA = VisualQuestionAnswering
    .pretrained("docvqa_pix2struct", "en", "clinical/ocr")
    .setQuestionsCol("questions")
    
    val pipeline = new Pipeline()
      .setStages(Array(binaryToImage, visualQA))
      .fit(imageWithQuestions)
```
</div>

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
|Size:|1.0 GB|