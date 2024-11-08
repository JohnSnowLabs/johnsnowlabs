---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_5_3_2
key: docs-ocr-release-notes
modify_date: "2024-05-15"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.3.2

Release date: 15-05-2024

## Visual NLP 5.3.2 Release Notes 🕶️

**We are glad to announce that Visual NLP 5.3.2 has been released.!!! 📢📢📢**

</div><div class="h3-box" markdown="1">

## Highlights 🔴

+ Ocr Metrics against Cloud Providers: Textract, and CGP.
+ LightPipeline support for Table Recognition and Clustering.
+ PositionFinder supports entities spawning multiple lines.
+ Other Changes.

</div><div class="h3-box" markdown="1">

### Ocr Metrics against Cloud Providers: Textract, and CGP.
Next are metrics for Text Detection and Recognition tasks collected on the FUNSD dataset, the final metric is the average F score across Text Detection and Recognition tasks.

{:.table-model-big}
|Detection | Recognition |  | Detection Metrics |  | Recognition Metrics |  |
|-- | -- | -- | -- | -- | -- | -- |
| | |  Precision | Recall | Precision | Recall |Avg. F Score|
|Google OCR | Google OCR | 0.3528 | 0.7776 | 0.8889 | 0.8823 | 0.6854 |
|Amazon Textract | Amazon Textract | 0.5284 | 0.8534 | 0.8236 | 0.8539 | 0.7455|
|ImageTextDetector (memOpt) | ImageToTextV2 (base checkpoint) | 0.6199 | 0.9044 | 0.9354 | 0.9331 | 0.8349|
|ImageTextDetector (memOpt) | ImageToTextV2 (large checkpoint) | 0.6199 | 0.9044 | 0.9457 | 0.9426 | **0.8398**|
|ImageTextDetectorV2 | ImageToTextV2 (base checkpoint) | 0.598 | 0.9046 | 0.9354 | 0.9331 | 0.8271|
|ImageTextDetectorV2 | ImageToTextV2 (large checkpoint) | 0.598 | 0.9046 | 0.9457 | 0.9426 | **0.8320**|
|ImageTextDetector (memOpt) | ImageToText | 0.6199 | 0.9044 | 0.464 | 0.4654 | 0.6001|

Not only the scores are slightly better than those of cloud providers, but also the cost is lower(*),

{:.table-model-big}
|Service | Cost(USD)|
|-- | --|
|Amazon | 120|
|Azure | 30|
|Google | 43.5|
|JSL | 17.6|


(*) JSL costs were estimated assuming a Databricks setup.

</div><div class="h3-box" markdown="1">

### LightPipeline support for Table Recognition and Clustering
Now you can use Table Extraction and Clustering pipelines as LightPipelines. To do so you just need to create the LightPipeline as usual, check this example using PretrainedPipeline,

[Full Example here.](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrLightPipelinesBase64.ipynb)
* new `LightPipeline.fromBinary()` method that allows the usage of in-memory binary buffers as inputs to Visual NLP pipelines.

```
lp = PretrainedPipeline("digital_pdf_table_extractor")
lp.fromLocalPath("page_with_tables.png")

```
For other examples please check [this notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrImageTableRecognitionWHOCR.ipynb).

</div><div class="h3-box" markdown="1">

### PositionFinder 
For cases in which entities spawn multiple lines, PositionFinder was not working properly.

![5.3.2](/assets/images/ocr/highlight.png)

Now, the expected bounding boxes for the entity are returned. Keep in mind that as before more than one bounding box will be returned, and all will share the same `chunk_id`.

</div><div class="h3-box" markdown="1">

### Other Changes
* CVE related to commons-compress was removed.
* Bug Fixes: ImageToPdf rendering images outside page boundaries.

</div><div class="prev_ver h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}