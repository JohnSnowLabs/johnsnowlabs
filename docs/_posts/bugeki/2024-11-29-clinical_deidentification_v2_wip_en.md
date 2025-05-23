---
layout: model
title: Clinical Deidentification Pipeline (Sentence Wise)
author: John Snow Labs
name: clinical_deidentification_v2_wip
date: 2024-11-29
tags: [deidentification, deid, en, licensed, clinical, pipeline, sent_wise]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text.
The pipeline can mask and obfuscate `MEDICALRECORD`, `ORGANIZATION`, `PROFESSION`, `HEALTHPLAN`, `DOCTOR`, `USERNAME`, `LOCATION-OTHER`, `URL`, `DEVICE`, `CITY`, `DATE`,
`ZIP`, `STATE`, `PATIENT`, `COUNTRY`, `STREET`, `PHONE`, `HOSPITAL`, `EMAIL`, `IDNUM`, `BIOID`, `FAX`, `AGE`, `LOCATION`, `LOCATION_OTHER`, `DLN`, `CONTACT`, `NAME`,
`SSN`, `ACCOUNT`, `PLATE`, `VIN`, `LICENSE`, `IP` entities.

## Predicted Entities

`MEDICALRECORD`, `ORGANIZATION`, `PROFESSION`, `HEALTHPLAN`, `DOCTOR`, `USERNAME`, `LOCATION-OTHER`, `URL`, `DEVICE`, `CITY`, `DATE`,
`ZIP`, `STATE`, `PATIENT`, `COUNTRY`, `STREET`, `PHONE`, `HOSPITAL`, `EMAIL`, `IDNUM`, `BIOID`, `FAX`, `AGE`, `LOCATION`, `LOCATION_OTHER`, `DLN`, `CONTACT`, `NAME`,
`SSN`, `ACCOUNT`, `PLATE`, `VIN`, `LICENSE`, `IP`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_v2_wip_en_5.5.0_3.4_1732871228669.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_v2_wip_en_5.5.0_3.4_1732871228669.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_v2_wip", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)

print(''.join([i.metadata['masked'] for i in deid_result['obfuscated']]))
print(''.join([i.result for i in deid_result['obfuscated']]))


```

{:.jsl-block}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = nlp.PretrainedPipeline("clinical_deidentification_v2_wip", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)

print(''.join([i.metadata['masked'] for i in deid_result['obfuscated']]))
print(''.join([i.result for i in deid_result['obfuscated']]))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_v2_wip", "en", "clinical/models")

val text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."""

val deid_result = deid_pipeline.fullAnnotate(text)

println(deid_result("obfuscated").map(_("metadata")("masked").toString).mkString(""))
println(deid_result("obfuscated").map(_("result").toString).mkString(""))


```
</div>

## Results

```bash
Masked with entity labels
------------------------------
Dr. <DOCTOR>, from <HOSPITAL> in <CITY>,  attended to the patient on <DATE>.
The patient’s medical record number is <MEDICALRECORD>.
The patient, <PATIENT>, is <AGE> years old,  her Contact number: <PHONE> .

Obfuscated
------------------------------
Dr. Alissa Irving, from KINDRED HOSPITAL SEATTLE in Geleen,  attended to the patient on 22/06/2024.
The patient’s medical record number is 16109604.
The patient, Burnette Carte, is 49 years old,  her Contact number: 540-981-1914 .

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_v2_wip|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcherInternalModel
- ContextualParserModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- ContextualParserModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- ChunkMergeModel
- ChunkMergeModel
- DeIdentificationModel
- Finisher
