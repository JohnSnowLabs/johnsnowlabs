---
layout: model
title: PDF Deidentification (Subentity- Context Augmented)
author: John Snow Labs
name: pdf_deid_subentity_context_augmented_pipeline
date: 2024-06-12
tags: [en, licensed]
task: De-identification
language: en
edition: Healthcare NLP 5.3.2
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to extract PHI information from PDF such as AGE, BIOID, CITY, COUNTRY, DATE, DEVICE, DOCTOR, EMAIL, FAX, HEALTHPLAN, HOSPITAL, IDNUM, LOCATION, MEDICALRECORD, ORGANIZATION, PATIENT, PHONE, PROFESSION, STATE, STREET, URL, USERNAME, ZIP, ACCOUNT, LICENSE, VIN, SSN, DLN, PLATE, IPADDR entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/pdf_deid_subentity_context_augmented_pipeline_en_5.3.2_3.2_1718175278007.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/pdf_deid_subentity_context_augmented_pipeline_en_5.3.2_3.2_1718175278007.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("pdf_deid_subentity_context_augmented_pipeline", "en", "clinical/models")
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|pdf_deid_subentity_context_augmented_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- PdfToImage
- ImageToText
- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- TextMatcherModel
- ContextualParserModel
- RegexMatcherModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcherInternalModel
- ChunkMergeModel
- ChunkMergeModel
- PositionFinder
- ImageDrawRegions
- ImageToPdf
- PdfAssembler