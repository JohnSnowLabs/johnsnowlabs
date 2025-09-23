---
layout: model
title: Detect PHI for Deidentification (Document Wise - Subentity)
author: John Snow Labs
name: ner_deid_subentity_docwise_augmented_pipeline_v2
date: 2025-03-24
tags: [deidentification, deid, en, licensed, clinical, pipeline, docwise, subentity]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 5.5.3
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

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_docwise_augmented_pipeline_v2_en_5.5.3_3.4_1742853581260.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_docwise_augmented_pipeline_v2_en_5.5.3_3.4_1742853581260.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("ner_deid_subentity_docwise_augmented_pipeline_v2", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)

```

{:.jsl-block}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = nlp.PretrainedPipeline("ner_deid_subentity_docwise_augmented_pipeline_v2", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)


```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("ner_deid_subentity_docwise_augmented_pipeline_v2", "en", "clinical/models")

val text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."""

val deid_result = deid_pipeline.fullAnnotate(text)



```
</div>

## Results

```bash

+--------------------+-----+---+-------------+
|result              |begin|end|entity       |
+--------------------+-----+---+-------------+
|John Lee            |4    |11 |DOCTOR       |
|Royal Medical Clinic|19   |38 |HOSPITAL     |
|Chicago             |43   |49 |CITY         |
|11/05/2024          |80   |89 |DATE         |
|56467890            |131  |138|MEDICALRECORD|
|Emma Wilson         |154  |164|PATIENT      |
|50                  |170  |171|AGE          |
|444-456-7890        |205  |216|PHONE        |
+--------------------+-----+---+-------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_subentity_docwise_augmented_pipeline_v2|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.5 GB|

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
- PretrainedZeroShotNER
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