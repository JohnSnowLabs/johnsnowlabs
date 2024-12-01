---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/ocr_release_notes
key: docs-ocr-release-notes
modify_date: "2024-09-26"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.4.1

Release date: 26-09-2024

## Visual NLP 5.4.1 Release Notes 🕶️

**We are glad to announce that Visual NLP 5.4.1 has been released. 
This release comes with new models, notebooks, examples, and bug fixes!!! 📢📢📢**

</div><div class="h3-box" markdown="1">

## Highlights 🔴

* New models for information extraction from Scanned Forms, scoring F1 92.86 on the FUNSD Entity Extraction dataset, and 89.23 on FUNSD Relation Extraction task. This significantly outperforms the Form Understanding capabilities of the AWS, Azure, and Google ‘Form AI’ services.
* New blogpost on Form Extraction in which we deep dive into the advantages of the models released today against different cloud providers.
* New PDF Deidentification Pipeline, that ingests PDFs and returns a de-identified version of the PDF.

</div><div class="h3-box" markdown="1">

## Other Changes 🟡

* Memory Improvements for Models that cut memory requirements of most models by half.
* Minor enhancements, changes, and bug fixes that ensure the quality of the library continues to improve over time.

</div><div class="h3-box" markdown="1">

### New models for information extraction from Scanned Forms

This model scores F1 92.86 on the FUNSD Entity Extraction dataset, and 89.23 on FUNSD Relation Extraction task. This significantly outperforms the Form Understanding capabilities of the AWS, Azure, and Google ‘Form AI’ services.

Two new annotators that work together were added:


* VisualDocumentNerGeo: This is a Visual NER model based on Geolayout, which achieves a F1-score of 92.86 on the Entity Extraction part of FUNSD. To use it call,
```
ner = VisualDocumentNerGeo().
  pretrained("visual_ner_geo_v1", "en", "clinical/ocr/")
```

* GeoRelationExtractor: This is a Relation Extraction model based on Geolayout, which achieves a F1-score of 89.45 on the Relation Extraction part of FUNSD. To use it call,

```
re = GeoRelationExtractor().
  pretrained("visual_re_geo_v2", "en", "clinical/ocr/")
```

To see these two models combined on a real example, please check this [sample notebook](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/FormRecognition/FormRecognitionGeo.ipynb).

</div><div class="h3-box" markdown="1">

### New PDF Deidentification Pipeline

A new PDF deidentification pipeline, `pdf_deid_subentity_context_augmented_pipeline` has been added to the library. This new pipeline has the ability to ingest PDFs, apply PHI masking through bounding boxes, and re-create the input PDF as a new document in which the PHI has been removed. The pipeline is ready to use and requires no configuration to handle most use cases.</br>
You can check an example of this pipeline in action in [this notebook](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrPdfDeidSubentityContextAugmentedPipeline.ipynb).

</div><div class="h3-box" markdown="1">

###  Memory Improvements for Models

All ONNX models have been refactored to reduce the memory footprint of the graph. There are two sources of memory problems in ML: models and data. Here we tackle model memory consumption by cutting the memory requirements of models by half.

</div><div class="h3-box" markdown="1">

### Minor enhancements, changes, and bug fixes.

* New `display_xml()` function for displaying tables as XMLs: similar to existing `display_tables()` function, but with XML output instead of Jupyter markdown.

* Enhanced memory management on ImageToTextV2: lifecycle of ONNX session is now aligned with Spark query plan. This means that models are instantiated only one time for each partition, and no leaks occur across multiple calls to transform() on the same pipeline. This results in a more efficient utilisation of memory.

* GPU support in Pix2Struct models: Pix2struct checkpoints for Chart Extraction and Visual Question Answering can leverage GPU like this,

```
visual_question_answering = VisualQuestionAnswering()\
    .pretrained("info_docvqa_pix2struct_jsl_base_opt", "en", "clinical/ocr")\
    .setUseGPU(True)
```

* Better support for different coordinate formats: we improved the way in which coordinates are handled within Visual NLP. Now, each annotator can detect whether coordinates being fed are regular coordinates or rotated coordinates. Forget about things like `ImageDrawRegions.setRotated()` to choose a specific input format, now everything happens automatically behind the scenes.

 * New blogpost on Form Extraction
We have recently released a new [Medium blogpost](https://medium.com/john-snow-labs/visual-document-understanding-benchmark-comparative-analysis-of-in-house-and-cloud-based-form-75f6fbf1ae5f) where we compare our in-house models against different cloud providers. We provide metrics and discuss the results.

Key takeaways are that first, Visual NLP's small models can beat cloud providers while at the same time remaining fast and providing more deployment options. Second, in order to obtain a model to be used in practice, fine tuning is mandatory.
 

This release is compatible with Spark-NLP 5.4.1, and Spark NLP for Healthcare 5.4.1.

</div><div class="h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}