---
layout: model
title: Clinical Deidentification Pipeline - Obfuscation (Medium)
author: John Snow Labs
name: clinical_deidentification_obfuscation_medium
date: 2024-02-09
tags: [licensed, en, clinical, deid, pipeline]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to detect the PHI information from medical texts and obfuscate (replace them with fake ones) in the resulting text.
Obfuscated entities: `LOCATION`, `CONTACT`, `PROFESSION`, `NAME`, `DATE`, `ID`, `AGE`, `MEDICALRECORD`, `ORGANIZATION`, `HEALTHPLAN`, `DOCTOR`, `USERNAME`, `LOCATION-OTHER`, `URL`, `DEVICE`, `CITY`, `ZIP`, `STATE`, `PATIENT`, `COUNTRY`, `STREET`, `PHONE`, `HOSPITAL`, `EMAIL`, `IDNUM`, `BIOID`, `FAX`, `SSN`, `ACCOUNT`, `DLN`, `PLATE`, `VIN`, `LICENSE`, `IPADDR`

## Predicted Entities

`LOCATION`, `CONTACT`, `PROFESSION`, `NAME`, `DATE`, `ID`, `AGE`, `MEDICALRECORD`, `ORGANIZATION`, `HEALTHPLAN`, `DOCTOR`, `USERNAME`, `LOCATION-OTHER`, `URL`, `DEVICE`, `CITY`, `ZIP`, `STATE`, `PATIENT`, `COUNTRY`, `STREET`, `PHONE`, `HOSPITAL`, `EMAIL`, `IDNUM`, `BIOID`, `FAX`, `SSN`, `ACCOUNT`, `DLN`, `PLATE`, `VIN`, `LICENSE`, `IPADDR`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_obfuscation_medium_en_5.2.1_3.0_1707483380096.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_obfuscation_medium_en_5.2.1_3.0_1707483380096.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_obfuscation_medium", "en", "clinical/models")

result = deid_pipeline.annotate("""Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 04/08/1993.
SSN #333-44-6666, Driver's license no: A334455B.
Phone 302-786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com.""")


```
```scala


import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_obfuscation_medium", "en", "clinical/models")

val result = deid_pipeline.annotate("""Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 04/08/1993.
SSN #333-44-6666, Driver's license no: A334455B.
Phone 302-786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com.""")


```
</div>

## Results

```bash
Obfuscated
------------------------------
Name : Kara Dies, Record date: 2093-03-11, MR #528413.
Dr. Leandrew Koyanagi, ID: 0272536644, IP 333.333.333.333.
He is a 78-year-old male was admitted to the VA MEDICAL CENTER - JOHN COCHRAN DIVISION for cystectomy on 30/09/1993.
SSN #308-23-1994, Driver's license no: I347425Z.
Phone 563-875-6433, 230 West Miller Street, Danielskuil, E-MAIL: Harolda@yahoo.com.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_obfuscation_medium|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- TextMatcherModel
- RegexMatcherModel
- ChunkMergeModel
- DeIdentificationModel
- Finisher
