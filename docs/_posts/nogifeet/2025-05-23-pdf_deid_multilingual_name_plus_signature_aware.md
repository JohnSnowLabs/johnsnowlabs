---
layout: model
title: PDF Deidentification Multilingual Name Plus Signature Aware
author: John Snow Labs
name: pdf_deid_multilingual_name_plus_signature_aware
date: 2025-05-17
tags: [en, licensed]
task: De-identification
language: en
nav_key: models
edition: Visual NLP 6.0.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to mask PHI information in PDFs. 
The output is a PDF document, similar to the one at the input, but with black bounding boxes on top of the targeted entities, also includes removing signatures.

## Predicted Entities

``HOSPITAL``, ``NAME``, ``PATIENT``, ``ID``,``MEDICALRECORD``, ``IDNUM``, ``COUNTRY``, ``LOCATION``, ``STREET``, ``STATE``, ``ZIP``, ``CONTACT``, ``PHONE``, ``DATE``.

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/PP_PDF_DEIDENTIFICATION/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrPdfDeIdentificationPipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/pdf_deid_multilingual_name_plus_signature_aware_en_6.0.0_3.0_1747909126000.zip){:.button.button-orange.button-orange-trans.arr.button-icon}


## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline
deid_pipeline = PretrainedPipeline("pdf_deid_multilingual_name_plus_signature_aware", "en", "clinical/ocr")
```

</div>

{:.model-param}

## Example

### Input:
![Screenshot](/assets/images/examples_ocr/PDF2_Deid_Deidentification_2_page-0002.jpg)

### Output:
![Screenshot](/assets/images/examples_ocr/pipeline5_pdf2_im2.png)

## Model Information

{:.table-model}
|---|---|
|Model Name:|pdf_deid_multilingual_name_plus_signature_aware|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.0 GB|

## Included Models

- PdfToImage
- ImageToText
- DocumentAssembler
- SentenceDetectorDLModel
- RegexTokenizer
- PretrainedZeroShotNER
- NerConverter
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- XLMRobertaEmbeddings
- MedicalNerModel
- NerConverter
- ContextualParser
- ChunkConverter
- Merge
- DeIdentification
- NerOutputCleaner
- PositionFinder
- ImageDrawRegions
- HW_Signature_Detector
- ImageDrawRegions
- ImageToPdf 