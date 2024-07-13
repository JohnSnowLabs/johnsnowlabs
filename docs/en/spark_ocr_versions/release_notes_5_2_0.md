---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_5_2_0
key: docs-ocr-release-notes
modify_date: "2024-02-23"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.2.0

Release date: 23-02-2024


## Visual NLP 5.2.0 Release Notes 🕶️

**We are glad to announce that Visual NLP 5.2.0 has been released. This release comes with new models, bug fixes, blog posts, and more!! 📢📢📢**

</div><div class="h3-box" markdown="1">

## Highlights 🔴
+ New Chart-To-Text dePlot based models.
+ Support for Confidence Scores in Visual Question Answering Models.
+ Improved stability and new metrics for ImageToTextV2 models.
+ New Blog Post on ImageToTextV2 models.
+ Docker image for Visual NLP.
+ New Pretrained pipeline basic_table_extractor
+ Spark 3.5 support.
+ Bug Fixes
+ Other Changes

</div><div class="h3-box" markdown="1">

## New Chart-To-Text dePlot based models 📈
Chart To Text is the task of converting an image chart into a serialized textual version representation of the chart. To understand this, consider the following example,

![5.2.0](/assets/images/ocr/chart.png)

Maps to the following text based representation,

![5.2.0](/assets/images/ocr/extracted_graph.png)

For an end-to-end example, please check [this notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrChartToTextTable.ipynb).

</div><div class="h3-box" markdown="1">

## Support for Confidence Scores in Visual Question Answering Models. 📍
Now, VisualQuestionAnswering models support confidence scores. The output schema for VisualQuestionAnswering models has been updated to include questions, answers and confidence scores. To enable confidence scores in the output of these models you should call `setConfidenceScore(true)`. For example,


![5.2.0](/assets/images/ocr/new_schema_vqa.png)

shows the schema and sample output for the case of two questions, with their corresponding answers and confidence scores.

</div><div class="h3-box" markdown="1">

## Improved stability and new metrics for ImageToTextV2 models. ⚡️
ImageToTextV2, our Transformer-based OCR has been improved, and extensively stress tested for stability and reliability.
These are the latest metrics for accuracy and runtime performance for all checkpoints,

![5.2.0](/assets/images/ocr/ocr_table.png)

A key takeaway from this chart is the following: _The [Dbu/h] is four times higher for CPU compared to GPU, with no variance in accuracy. Utilizing GPU can achieve identical outcomes at one-fourth of the cost. GPU is your friend!_

</div><div class="h3-box" markdown="1">

## New Blog Post in ImageToTextV2 models. 💥
Want to learn about the best practices to scale out your OCR pipelines?. Read the full article [here](https://medium.com/john-snow-labs/unleashing-the-power-of-high-throughput-inference-with-tr-ocr-1f0fa3bc46c6).

</div><div class="h3-box" markdown="1">

## Docker image for Visual NLP. 🔥
For users that require running inside a container we have created the following [instructions](https://github.com/JohnSnowLabs/spark-ocr-workshop/tree/master/docker/visual-ner) and [sample notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/docker/visual-ner/content/VisualNlp.ipynb).

</div><div class="h3-box" markdown="1">

## New Pretrained pipeline `basic_table_extractor`

This is a complete Table Extraction Pipeline. Following, it's a basic example of how to call this pipeline,
![5.2.0](/assets/images/ocr/basic_table_extractor.png)

And you should also check the full example in [this notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/webinars/zs_table_processing/TableExtractionBasics.ipynb).

</div><div class="h3-box" markdown="1">

## Spark 3.5 support 🎯
We extended support to Apache Spark 3.5. All tests were run using Spark 3.5 and Python 3.10.

</div><div class="h3-box" markdown="1">

## Other Changes
* Pix2struct models now support caching, both docvqa_pix2struct_jsl and docvqa_pix2struct_jsl_opt pix2struct based checkpoints now support caching, which is enabled by default.
* This release is compatible with ```Spark NLP 5.2.2``` and Spark NLP for``` Healthcare 5.2.1```

</div><div class="prev_ver h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}