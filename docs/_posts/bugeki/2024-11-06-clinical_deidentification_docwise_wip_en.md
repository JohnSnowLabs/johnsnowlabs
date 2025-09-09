---
layout: model
title: Clinical Deidentification Pipeline (Document Wise)
author: John Snow Labs
name: clinical_deidentification_docwise_wip
date: 2024-11-06
tags: [deidentification, deid, en, licensed, clinical, pipeline, docwise]
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
The pipeline can mask and obfuscate `LOCATION`, `CONTACT`, `PROFESSION`, `NAME`, `DATE`, `AGE`, `MEDICALRECORD`, `ORGANIZATION`, `HEALTHPLAN`, `DOCTOR`, `USERNAME`,
`LOCATION-OTHER`, `URL`, `DEVICE`, `CITY`, `ZIP`, `STATE`, `PATIENT`, `COUNTRY`, `STREET`, `PHONE`, `HOSPITAL`, `EMAIL`, `IDNUM`, `BIOID`, `FAX`, `LOCATION_OTHER`, `DLN`,
`SSN`, `ACCOUNT`, `PLATE`, `VIN`, `LICENSE`, `IP` entities.

## Predicted Entities

`NAME`, `DATE`, `IDNUM`, `ZIP`, `SSN`, `ACCOUNT`, `LICENSE`, `AGE`, `PHONE`, `COUNTRY`, `STATE`, `CITY`, `PLATE`, `VIN`, `MEDICALRECORD`, `EMAIL`, `URL`, `LOCATION`, `PROFESSION`, `CONTACT`, `PATIENT`, `HOSPITAL`, `ORGANIZATION`, `STREET`, `DOCTOR`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_docwise_wip_en_5.5.0_3.4_1730921636336.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_docwise_wip_en_5.5.0_3.4_1730921636336.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_docwise_wip", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)

print(''.join([i.result for i in deid_result['mask_entity']]))
print(''.join([i.result for i in deid_result['obfuscated']]))


```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_docwise_wip", "en", "clinical/models")

val text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."""

val deid_result = deid_pipeline.fullAnnotate(text)

println(deid_result("mask_entity").map(_("result").toString).mkString(""))
println(deid_result("obfuscated").map(_("result").toString).mkString(""))


```
</div>

## Results

```bash

Masked with entity labels
------------------------------
Dr. <DOCTOR>, from <HOSPITAL> in <CITY>,  attended to the patient on <DATE>.
The patient’s medical record number is <MEDICALRECORD>
patient, <PATIENT>, is <AGE> years old,  her Contact number: <PHONE> .

Obfuscated
------------------------------
Dr. Edwardo Graft, from MCBRIDE ORTHOPEDIC HOSPITAL in CLAMART,  attended to the patient on 14/06/2024.
The patient’s medical record number is 78295621.
The patient, Nathaneil Bakes, is 43 years old,  her Contact number: 308-657-8469 .

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_docwise_wip|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- InternalDocumentSplitter
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- MedicalNerModel
- MedicalNerModel
- NerConverterInternalModel
- NerConverterInternalModel
- NerConverterInternalModel
- ChunkMergeModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- ContextualParserModel
- RegexMatcherInternalModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- TextMatcherInternalModel
- ChunkMergeModel
- ChunkMergeModel
- LightDeIdentification
- LightDeIdentification
