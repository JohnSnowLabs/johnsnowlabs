---
layout: model
title: PDF Deidentification Multilingual Name Plus Signature Aware
author: John Snow Labs
name: pdf_deid_multilingual_name_plus_signature_aware
date: 2025-05-17
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

This pipeline can be used to mask PHI information in PDFs. Masked entities include 'HOSPITAL', 'NAME', 'PATIENT', 'ID','MEDICALRECORD', 'IDNUM', 'COUNTRY', 'LOCATION', 'STREET', 'STATE', 'ZIP', 'CONTACT', 'PHONE', 'DATE'.
The output is a PDF document, similar to the one at the input, but with black bounding boxes on top of the targeted entities, also includes removing signatures.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/pdf_deid_multilingual_name_plus_signature_aware_en_6.0.0_3.0_1747909126000.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/pdf_deid_multilingual_name_plus_signature_aware_en_6.0.0_3.0_1747909126000.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline
deid_pipeline = PretrainedPipeline("pdf_deid_multilingual_name_plus_signature_aware", "en", "clinical/ocr")
```

</div>

{:.model-param}
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