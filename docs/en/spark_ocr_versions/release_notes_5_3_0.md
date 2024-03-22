---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_5_3_0
key: docs-ocr-release-notes
modify_date: "2024-03-20"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.3.0

Release date: 20-03-2024


 ## Visual NLP 5.3.0 Release Notes 🕶️


**We are glad to announce that Visual NLP 5.3.0 has been released!. This is a small compatibility release, to ensure proper inter-operability against Spark NLP and Spark NLP for Healthcare, plus some LightPipelines features.!! 📢📢📢**


## Highlights 🔴

+ Tested against Spark NLP 5.3.1 and Spark NLP for Healthcare 5.3.0.
+ New Base64ToBinary annotator.
+ Positions output in ImageToText annotator has been fixed for LightPipelines.

## New Base64ToBinary Annotator
This new annotator, as its name suggests, serves the purpose of converting in-memory base64 encoded buffers into binary format. This is useful, among other things, for the use case in which your data is not stored in disk, and it can be really helpful in combination with PdfToText, or PdfToImage, e.g.,

```
base64_to_bin = Base64ToBinary()
base64_to_bin.setOutputCol("content")

pdf_to_image = PdfToImage()
pdf_to_image.setInputCol("content")
pdf_to_image.setOutputCol("image")
pdf_to_image.setImageType(ImageType.TYPE_3BYTE_BGR)


# Run OCR for each region
ocr = ImageToText()
ocr.setInputCol("image")
ocr.setOutputCol("text")

# OCR pipeline
pipeline = PipelineModel(stages=[
    base64_to_bin,
    pdf_to_image,
    ocr
])
```


For an end-to-end example which also includes LightPipelines please check [this notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrLightPipelinesBase64.ipynb).


</div><div class="prev_ver h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
