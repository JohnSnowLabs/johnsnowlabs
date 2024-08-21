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

This pipeline can be used to mask PHI information in PDFs. Masked entities include AGE, BIOID, CITY, COUNTRY, DATE, DEVICE, DOCTOR, EMAIL, FAX, HEALTHPLAN, HOSPITAL, IDNUM, LOCATION, MEDICALRECORD, ORGANIZATION, PATIENT, PHONE, PROFESSION, STATE, STREET, URL, USERNAME, ZIP, ACCOUNT, LICENSE, VIN, SSN, DLN, PLATE, and IPADDR.
The output is a PDF document, similar to the one at the input, but with black bounding boxes on top of the targeted entities.

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


## Speed Benchmarks

- **Dataset:** 1000 scanned PDF pages.
- **Instance :** 
  - m5n.4xlarge (16 vCPUs, 64 GiB memory) 
  - m5n.8xlarge (32 vCPUs, 128 GiB memory)
- **AMI:** ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20240411
- **Versions:**
  - **spark-nlp Version:** v5.4.0
  - **visual-nlp Version:** v5.3.2
  - **spark-nlp-jsl Version :** v5.3.2
  - **Spark Version :** v3.4.1
- **Visual NLP Pipeline:** 'pdf_deid_subentity_context_augmented_pipeline'


#### Benchmark Table

{:.table-model-big}
| Instance      | memory | cores | input\_data\_pages| partition     | second per page | timing  |
| ------------- | ------ | ----- | ----------------- | ------------- | --------------- | ------- |
| m5n.4xlarge   | 64 GB  | 16    | 1000              | 10            | 0.24            | 4 mins  |
| m5n.8xlarge   | 128 GB | 32    | 1000              | 32            | 0.15            | 2.5 mins|
