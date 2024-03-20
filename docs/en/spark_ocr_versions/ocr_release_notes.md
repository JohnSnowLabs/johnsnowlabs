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

</div><div class="h3-box" markdown="1">

<<<<<<< Updated upstream
## Visual NLP 5.1.2 Release Notes 🕶️
=======
 ## Visual NLP 5.2.0 Release Notes 🕶️


>>>>>>> Stashed changes

**We are glad to announce that Visual NLP 5.2.0 has been released. This release comes with new models, bug fixes, blog posts, and more!! 📢📢📢**

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

<<<<<<< Updated upstream
</div><div class="h3-box" markdown="1">

## New optimized OCR checkpoints with up to 5x speed ups and GPU support 🚀
ImageToTextV2, is our Transformer-based OCR model which delivers SOTA accuracy across different pipelines like Text Extraction(OCR), Table Extraction, and Deidentification.
We've added new checkpoints together with more options to choose which optimizations to apply.

</div><div class="h3-box" markdown="1">

### New checkpoints for ImageToTextV2 📍
All previous checkpoints have been updated to work with the latest optimizations, and in addition these 4 new checkpoints have been added,
=======
## New Chart-To-Text dePlot based models 📈
Chart To Text is the task of converting an image chart into a serialized textual version representation of the chart. To understand this, consider the following example,

![image](/assets/images/ocr/chart.png)
>>>>>>> Stashed changes

Maps to the following text based representation,

![image](/assets/images/ocr/extracted_graph.png)

<<<<<<< Updated upstream
</div><div class="h3-box" markdown="1">

### New options for ImageToTextV2 ⚡️
ImageToTextV2 now supports the following configurations:
* setUseCaching(Boolean): whether or not to use caching during processing.
* setBatchSize(Integer): the batch size dictates the size of the groups that are processes internally at a single time by the model, typically used when setUseGPU() is set to true. 

</div><div class="h3-box" markdown="1">

### Choosing the best checkpoint for your problem 💥
We put together this grid reflecting performance and accuracy metrics to help you choose the most appropriate checkpoint for your use case.
* Accuracy
=======
For an end-to-end example, please check [this notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrChartToTextTable.ipynb).

## Support for Confidence Scores in Visual Question Answering Models. 📍
Now, VisualQuestionAnswering models support confidence scores. The output schema for VisualQuestionAnswering models has been updated to include questions, answers and confidence scores. To enable confidence scores in the output of these models you should call `setConfidenceScore(true)`. For example,
>>>>>>> Stashed changes


![image](/assets/images/ocr/new_schema_vqa.png)

shows the schema and sample output for the case of two questions, with their corresponding answers and confidence scores.

## Improved stability and new metrics for ImageToTextV2 models. ⚡️
ImageToTextV2, our Transformer-based OCR has been improved, and extensively stress tested for stability and reliability.
These are the latest metrics for accuracy and runtime performance for all checkpoints,

![image](/assets/images/ocr/ocr_table.png)

<<<<<<< Updated upstream
</div><div class="h3-box" markdown="1">

## New improved Table Extraction Pipeline with improved Cell Detection stage. 🔥
Starting in this release, our HocrToTextTable annotator can receive information related to cells regions to improve the quality of results in Table Extraction tasks. This is particularly useful for cases in which cells are multi-line, or for borderless tables.  </br>
This is what a pipeline would look like,
```
binary_to_image = BinaryToImage()
=======
A key takeaway from this chart is the following: _The [Dbu/h] is four times higher for CPU compared to GPU, with no variance in accuracy. Utilizing GPU can achieve identical outcomes at one-fourth of the cost. GPU is your friend!_
>>>>>>> Stashed changes

## New Blog Post in ImageToTextV2 models. 💥
Want to learn about the best practices to scale out your OCR pipelines?. Read the full article [here](https://medium.com/john-snow-labs/unleashing-the-power-of-high-throughput-inference-with-tr-ocr-1f0fa3bc46c6).


## Docker image for Visual NLP. 🔥
For users that require running inside a container we have created the following [instructions](https://github.com/JohnSnowLabs/spark-ocr-workshop/tree/master/docker/visual-ner) and [sample notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/docker/visual-ner/content/VisualNlp.ipynb).

## New Pretrained pipeline `basic_table_extractor`

This is a complete Table Extraction Pipeline. Following, it's a basic example of how to call this pipeline,
![image](/assets/images/ocr/basic_table_extractor.png)

And you should also check the full example in [this notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/webinars/zs_table_processing/TableExtractionBasics.ipynb).

<<<<<<< Updated upstream
</div><div class="h3-box" markdown="1">
=======
## Spark 3.5 support 🎯
We extended support to Apache Spark 3.5. All tests were run using Spark 3.5 and Python 3.10.
>>>>>>> Stashed changes

## Other Changes
* Pix2struct models now support caching, both docvqa_pix2struct_jsl and docvqa_pix2struct_jsl_opt pix2struct based checkpoints now support caching, which is enabled by default.

<<<<<<< Updated upstream
</div><div class="h3-box" markdown="1">

## Bug Fixes 🪲
* ImageSplitRegions does not work after Table Detector.
* VisualDocumentNerLilt output has been fixed to include entire tokens instead of pieces.
* Null Regions in HocrToTextTable are handled properly.
* display_tables can now handle empty tables better.
* Vulnerabilities in Python dependencies.
=======
>>>>>>> Stashed changes


* This release is compatible with ```Spark NLP 5.2.2``` and Spark NLP for``` Healthcare 5.2.1```

</div><div class="prev_ver h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
