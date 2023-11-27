---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/ocr_release_notes
key: docs-ocr-release-notes
modify_date: "2023-11-17"
show_nav: true
sidebar:
    nav: spark-ocr
---

<div class="h3-box" markdown="1">

## 5.1.0

Release date: 17-11-2023


**We are glad to announce that Visual NLP 5.1.0 has been released! This release comes with new models, annotators, bug fixes, and more!.📢📢📢**

**New Models &  Annotators**
* VisualQuestionAnsweringPix2Struct: we are adding a new Visual Question Answering(VQA) checkpoint for Pix2Struct. Document VQA is the task of answering questions about documents, in which visual clues are important in the answer.
The practical impact of this type of models is that you can create "data extractors" for your own particular use case without fine-tuning on your data. So you can ask questions about tables, or forms or other structures in which the visual information is relevant, in a zero-shot manner.

We started our journey with Donut-like models, which were great in many different tasks. Check [this code and example](https://nlp.johnsnowlabs.com/2023/01/17/docvqa_donut_base_en_3_2.html), and [this webinar](https://www.johnsnowlabs.com/watch-zero-shot-visual-question-answering/), in case you missed it.
![image](/assets/images/ocr/pix2struct_sample.png)

```
|[What's the estimated population in poverty of Lawrence? ->  5,696, What's the population of Stoddard? ->  26,000, What is the page number of the document? ->  6, What is the date in the document? ->  January, 1970]|

```

Now, we're taking one step further and integrating Pix2Struct which, when compared to Donut, scores 5 points higher in the 'base' version, and 9 points higher in the 'large' version, on DocVQA dataset. This is an optimized and in house fine tuned checkpoint.
Check [this notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrVisualPix2Struct.ipynb) with examples on how to use it.

* DocumentLayoutAnalyzer: document layout analysis is a fundamental task in Visual NLP, it is the task of detecting sections in a document. Typical examples for these sections are: text, title, list, table, or figure.
![image](/assets/images/ocr/dit-layout-sample.png)


 
   Identifying these sections is the first step that enables other downstream processing tasks like OCR or Table Extraction.
Check [this notebook](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOCRDocumentLayoutAnalyzer.ipynb) for an example on how to apply this new model to sample documents.

* DicomDeidentifier: new annotator that allows deidentification of Dicom Images using Dicom metadata contained in the same Dicom document. This is a rule-based annotator which leverages PHI collected from the metadata like patient names or test results to deidentify PHI contained on images in the Dicom file. It also supports a black list parameter to remove specific content present in the image text.
This annotator can work either in isolation or combined with Spark NLP for Healthcare NER models. By using ChunkMergeApproach, NER models can be combined with DicomDeidentifier to deliver an ensemble of ML and Rule Based techniques to cover the most challenging de-identification scenarios.
We encourage you to check [an example](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Dicom/SparkOcrDicomDeIdentificationV3.ipynb), and other Dicom related notebooks,
[jupyter/Dicom](https://github.com/JohnSnowLabs/spark-ocr-workshop/tree/master/jupyter/Dicom).
As well as related blogposts,

    * [DICOM de-identification at scale in Visual NLP — Part 1.](https://medium.com/john-snow-labs/dicom-de-identification-at-scale-in-visual-nlp-part-1-68784177f5f0)

    * [DICOM de-identification at scale in Visual NLP — Part 2.](https://medium.com/john-snow-labs/dicom-de-identification-at-scale-in-visual-nlp-part-2-361af5e36412)

    * [DICOM de-identification at scale in Visual NLP — Part 3.](https://medium.com/john-snow-labs/dicom-de-identification-at-scale-in-visual-nlp-part-3-ac750be386cb)

**Bug Fixes & Changes**

+ VisualQuestionAnswering is the new single entry point for downloading all Visual Question Answering models. You should use it like this,

```
VisualQuestionAnswering.pretrained("docvqa_donut_base")
```

or 

```
VisualQuestionAnswering.pretrained("docvqa_pix2struct_jsl")	
```
* VisualDocumentClassifierV3, fit() method now allows the initial checkpoint to be present in local storage, instead of being downloaded from JSL Models Hub. Simply pass the 'base_model_path' param like this,
```
VisualDocumentClassifierV3.fit(base_model_path='path_to_local_chkpt')
```
* Some serialization problems affecting ONNX models running in a cluster have been resolved.
* Transformer OCR pretrained pipelines have been updated to use faster components and to avoid some serialization issues under some Spark versions, check [this query](https://nlp.johnsnowlabs.com/models?edition=Visual+NLP&type=pipeline) on Models Hub.

* This release is compatible with ```Spark NLP 5.1.2``` and Spark NLP for``` Healthcare 5.1.2```


</div><div class="prev_ver h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
