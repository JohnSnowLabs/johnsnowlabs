---
layout: model
title: PDF Obfuscation Multi Model Context
author: John Snow Labs
name: pdf_obfuscation_multi_model_context_pipeline
date: 2025-05-09
tags: [en, licensed]
task: De-identification
language: en
edition: Healthcare NLP 6.0.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to mask PHI information in PDFs. 
The output is a PDF document, similar to the one at the input, but with fake obfuscated text on top of the targeted entities. 

## Predicted Entities

``AGE``, ``CITY``, ``COUNTRY``, ``DATE``, ``DOCTOR``, ``EMAIL``, ``HOSPITAL``, ``IDNUM``, ``ORGANIZATION``, ``PATIENT``, ``PHONE``, ``PROFESSION``, ``STATE``, ``STREET``, ``USERNAME``, ``ZIP``.


{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/PP_PDF_DEIDENTIFICATION/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrPdfDeIdentificationPipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/pdf_obfuscation_multi_model_context_pipeline_en_6.0.0_3.0_1746699526000.zip){:.button.button-orange.button-orange-trans.arr.button-icon}


## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline
deid_pipeline = PretrainedPipeline("pdf_obfuscation_multi_model_context_pipeline", "en", "clinical/ocr")
```

</div>

{:.model-param}

## Example

### Input:
![Screenshot](/assets/images/examples_ocr/PDF3_Deid_Deidentification_3_page-0001.jpg)

### Output:
![Screenshot](/assets/images/examples_ocr/pipeline3_pdf3_im1.png)

## Model Information

{:.table-model}
|---|---|
|Model Name:|pdf_obfuscation_multi_model_context_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.4 GB|

## Included Models

- PdfToImage
- ImageToText
- DocumentAssembler
- SentenceDetectorDLModel
- Regex
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- EntityExtractor
- ContextualParserModel
- RegexMatcher
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcher
- ChunkMergeModel
- ChunkMergeModel
- XLMRobertaEmbeddings
- MedicalNerModel
- NerConverter 
- PretrainedZeroShotNER
- NerConverter
- PretrainedZeroShotNER
- NerConverter
- ChunkMergeModel
- PositionFinder
- ImageDrawRegions
- ImageToPdf 