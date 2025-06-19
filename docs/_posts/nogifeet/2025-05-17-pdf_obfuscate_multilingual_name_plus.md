---
layout: model
title: PDF Obfuscate Multilingual Name Plus
author: John Snow Labs
name: pdf_obfuscate_multilingual_name_plus
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
The Clinical Obfuscation for PDF Pipeline is a powerful solution for transforming sensitive PDF documents into safe, shareable assets. It enables organizations to unlock the value of clinical data while ensuring strict compliance with HIPAA, GDPR, and institutional privacy standards.
The pipeline is designed to obfuscate Personally Identifiable Information (PII) in input PDF documents, while preserving readability and format integrity. Its key features include:

### Entity-Level Obfuscation
Detected entities (e.g., names, dates, IDs) are individually replaced with synthetic but realistic alternatives, ensuring sensitive information is protected.

### Layout-Aware Replacement
Replacement entities are carefully chosen to match the visual space of the originals, avoiding issues like text overflow or underfitting.

### Supported Entity Types
The pipeline can obfuscate the following types of information:
HOSPITAL, NAME, PATIENT, ID, MEDICALRECORD, IDNUM, COUNTRY, LOCATION, STREET, STATE, ZIP, CONTACT, PHONE, DATE.

### Preserved Document Appearance
The output is a PDF document visually similar to the original, with obfuscated text rendered on top of the original positions of sensitive entities.

### Document-Wide Consistency
Replacement is consistent across the document. For example, if "Lilian Clarke" is replaced by "Nelly Huffman" on page 1, all subsequent instances of "Lilian Clarke" are replaced with the same synthetic name throughout the document.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/pdf_obfuscate_multilingual_name_plus_en_6.0.0_3.0_1747131526000.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/pdf_obfuscate_multilingual_name_plus_en_6.0.0_3.0_1747131526000.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline
deid_pipeline = PretrainedPipeline("pdf_obfuscate_multilingual_name_plus", "en", "clinical/ocr")

deid_pipeline.transform(input_pdfs)

```

</div>

{:.model-param}
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
