---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_4_4_0
key: docs-ocr-release-notes
modify_date: "2023-03-14"
show_nav: true
sidebar:
    nav: spark-ocr
---

<div class="h3-box" markdown="1">

## 4.4.0

Release date: 15-04-2023

We're glad to announce that Visual NLP 😎 4.4.0 has been released.

### Highlights
* Pretrained Pipelines for Visual NLP
* Deprecations & Changes
* Improvements
* New notebooks

#### Pretrained Pipelines for Visual NLP
We are adding support for pretrained pipelines that will allow to package an entire set of models and transformations into single unit. For starters, this is the list of pretrained pipelines we are releasing today,

* mixed_scanned_digital_pdf: OCR pipeline to support a mix of digital and scanned documents as inputs.
* mixed_scanned_digital_pdf_image_cleaner: OCR pipeline to support a mix of digital and scanned documents as inputs. The ImageTextCleaner transformer will be applied to those PDFs containing scanned images.
* mixed_scanned_digital_pdf_skew_correction: OCR pipeline to support a mix of digital and scanned documents as inputs. The ImageSkewCorrector transformer will be applied to those PDFs containing scanned images.
* image_handwritten_transformer_extraction: OCR on handwritten texts contained in images.
* image_printed_transformer_extraction: OCR printed texts contained on images.
* pdf_printed_transformer_extraction: OCR printed texts contained in PDFs.
* pdf_handwritten_transformer_extraction: OCR handwritten texts contained in PDFs.


#### Deprecations & Changes
Some ImageToTextV2 models have been deprecated in favor of new optimized versions that work entirely on the JVM, and also now work in LightPipelines.

ocr_base_handwritten -> ocr_base_handwritten_v2
ocr_base_printed -> ocr_base_printed_v2

Also, the optimized versions are available through,
ocr_base_printed_v2_opt
ocr_base_handwritten_v2_opt

Note: If you don't upgrade, you can continue to use the same model names.

VisualDocumentNer: one class to rule(and load) all Visual NER models! You should replace VisualDocumentNerV2 instances with this class name, and just provide the right pretrained model name, e.g.,

VisualDocumentNer.pretrained("visual_document_NER_SROIE0526")

or

VisualDocumentNer.pretrained("lilt_roberta_funsd_v1")

Also, LayoutLMv2 models have been deprecated in favor of Lilt based versions, e.g.,

layoutlmv2_funsd -> lilt_roberta_funsd_v1

Accordingly, these changes have been reflected in sample notebook, which has been renamed,
SparkOCRVisualDocumentNERv2.ipynb -> SparkOCRVisualDocumentNer-FormParsing.ipynb

Finally, VisualDocumentNer fine tuning notebooks are currently deprecated until new ones are included on next release.


#### Improvements
We improved digital PDF data ingestion for documents containing ligature glyphs which are used in some fonts. Ligature glyphs are symbols that may represent two or more characters. For instance, 'f' and 'i' may be represented as one char 'fi'. We improved our transformer to process them correctly.

#### New Notebooks
[SparkOcrPretrainedPipelines.ipynb](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrPretrainedPipelines.ipynb): use this notebook to learn how to use the new pretrained pipelines feature added to Visual NLP 4.4.0.

This release is compatible with Spark NLP 4.4.0 and Spark NLP for Healthcare 4.4.0.

</div><div class="prev_ver h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
