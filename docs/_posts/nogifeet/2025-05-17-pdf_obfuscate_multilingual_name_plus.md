---
layout: model
title: PDF Obfuscate Multilingual Name Plus
author: John Snow Labs
name: pdf_obfuscate_multilingual_name_plus
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

deploy:
  sagemaker_link: https://aws.amazon.com/marketplace/pp/prodview-jju2zifvlabdy
  snowflake_link: 
  databricks_link: 

---

## Description
The Clinical Obfuscation for PDF Pipeline helps turn sensitive PDF documents into safe, shareable files. It finds personal information like names, dates, and IDs, and replaces them with fake but realistic alternatives. The replacements match the look and size of the original text, so the layout stays the same. Each piece of information is replaced the same way every time it appears. The final PDF looks like the original, but without exposing any real personal data.

## Predicted Entities
``HOSPITAL``, ``NAME``, ``PATIENT``, ``ID``, ``MEDICALRECORD``, ``IDNUM``, ``COUNTRY``, ``LOCATION``, ``STREET``, ``STATE``, ``ZIP``, ``CONTACT``, ``PHONE``, ``DATE``.

{:.btn-box}

[Live Demo](https://demo.johnsnowlabs.com/ocr/PP_PDF_DEIDENTIFICATION/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrPdfDeIdentificationPipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/pdf_obfuscate_multilingual_name_plus_en_6.0.0_3.0_1747131526000.zip){:.button.button-orange.button-orange-trans.arr.button-icon}


{% if page.deploy %}
## Available as Private API Endpoint

{:.tac}
{% include display_platform_information.html %}
{% endif %}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline
deid_pipeline = PretrainedPipeline("pdf_obfuscate_multilingual_name_plus", "en", "clinical/ocr")
```

</div>

{:.model-param}

## Example

### Input:
![Screenshot](/assets/images/examples_ocr/PDF3_Deid_Deidentification_3_page-0002.jpg)

### Output:
![Screenshot](/assets/images/examples_ocr/pipeline6_pdf3_im2.png)

## Model Information

{:.table-model}
|---|---|
|Model Name:|pdf_obfuscate_multilingual_name_plus|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.8 GB|

## Included Models

The following models are included in the pipeline,

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
- ImageToPdf 
