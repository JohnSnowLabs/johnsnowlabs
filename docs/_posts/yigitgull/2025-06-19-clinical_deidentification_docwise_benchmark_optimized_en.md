---
layout: model
title: Clinical Deidentification Pipeline (Document Wise)
author: John Snow Labs
name: clinical_deidentification_docwise_benchmark_optimized
date: 2025-06-19
tags: [deidentification, deid, en, licensed, clinical, pipeline, docwise]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.0.2
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
`LOCATION-OTHER`, `URL`, `DEVICE`, `CITY`, `ZIP`, `STATE`, `PATIENT`, `STREET`, `PHONE`, `HOSPITAL`, `EMAIL`, `IDNUM`, `BIOID`, `FAX`, `LOCATION_OTHER`, `DLN`,
`SSN`, `ACCOUNT`, `PLATE`, `VIN`, `LICENSE`, `IP` entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_docwise_benchmark_optimized_en_6.0.2_3.4_1750347669806.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_docwise_benchmark_optimized_en_6.0.2_3.4_1750347669806.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_docwise_benchmark_optimized", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)


```

{:.jsl-block}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = nlp.PretrainedPipeline("clinical_deidentification_docwise_benchmark_optimized", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_docwise_benchmark_optimized", "en", "clinical/models")

val text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

val deid_result = deid_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash
|    | text                                                                                       | result                                                                                                                                                                                         | result                                                                                                                                                                                                                                |
|---:|:-------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024. | ['Dr. <DOCTOR>, from <HOSPITAL> in <CITY>, attended to the patient on <DATE>.\nThe patient’s medical record number is <ID>.\nThe patient, <PATIENT>, is <AGE>, her Contact number: <PHONE> .'] | ['Dr. Valerie Aho, from Mercy Hospital Aurora in Berea, attended to the patient on 30/05/2024.\nThe patient’s medical record number is 78689012.\nThe patient, Johnathon Bunde, is 55 years old, her Contact number: 666-678-9012 .'] |
|    | The patient’s medical record number is 56467890.                                           |                                                                                                                                                                                                |                                                                                                                                                                                                                                       |
|    | The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 .              |                                                                                                                                                                                                |                                                                                                                                                                                                                                       |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_docwise_benchmark_optimized|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- InternalDocumentSplitter
- TokenizerModel
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
- RegexMatcherInternalModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- ContextualParserModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- ContextualParserModel
- ContextualParserModel
- ChunkMergeModel
- ChunkMergeModel
- LightDeIdentification
- LightDeIdentification