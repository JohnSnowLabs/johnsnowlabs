---
layout: model
title: Dicom De-identification Pipeline
author: John Snow Labs
name: dicom_died_pipeline
date: 2024-08-27
tags: [en, licensed]
task: De-identification
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to mask PHI information in Dicom. Masked entities include AGE, BIOID, CITY, COUNTRY, DATE, DEVICE, DOCTOR, EMAIL, FAX, HEALTHPLAN, HOSPITAL, IDNUM, LOCATION, MEDICALRECORD, ORGANIZATION, PATIENT, PHONE, PROFESSION, STATE, STREET, URL, USERNAME, ZIP, ACCOUNT, LICENSE, VIN, SSN, DLN, PLATE, and IPADDR. The output is a Dicom document, similar to the one at the input, but with black bounding boxes on top of the targeted entities and de-identified metadata.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/dicom_died_pipeline_en_5.3.3_3.0_1724774052059.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/dicom_died_pipeline_en_5.3.3_3.0_1724774052059.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("dicom_died_pipeline", "en", "clinical/models")

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("dicom_died_pipeline", "en", "clinical/models")
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|dicom_died_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DicomToMetadata
- DicomToImageV3
- ImageTextDetectorV2
- ImageToTextV3
- DicomDeidentifier
- PipelineModel
- PositionFinder
- DicomDrawRegions
- DicomMetadataDeidentifier