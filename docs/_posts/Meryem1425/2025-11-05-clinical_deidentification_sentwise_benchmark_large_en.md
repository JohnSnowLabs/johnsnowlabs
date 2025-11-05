---
layout: model
title: Clinical Deidentification Pipeline Benchmark Large (Sentence Wise)
author: John Snow Labs
name: clinical_deidentification_sentwise_benchmark_large
date: 2025-11-05
tags: [deidentification, deid, en, licensed, clinical, pipeline, sentwise]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.0.4
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text.
The pipeline can mask and obfuscate 'LOCATION', 'CONTACT', 'PROFESSION', 'DATE', 'IDNUM', 'MEDICALRECORD', 'DOCTOR', 'USERNAME', 'CITY', 'ZIP', 'STATE', 'PATIENT', 'COUNTRY', 'STREET', 'HOSPITAL', 'DLN', 'AGE', 'PHONE', 'EMAIL', 'ORGANIZATION', 'SSN', 'ACCOUNT', 'PLATE', 'VIN', 'LICENSE', 'URL', 'IP' entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_sentwise_benchmark_large_en_6.0.4_3.4_1762368957324.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_sentwise_benchmark_large_en_6.0.4_3.4_1762368957324.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_sentwise_benchmark_large", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)


```

{:.jsl-block}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = nlp.PretrainedPipeline("clinical_deidentification_sentwise_benchmark_large", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_sentwise_benchmark_large", "en", "clinical/models")

val text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

val deid_result = deid_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

# Masked with entity labels
# ------------------------------
# Dr. <DOCTOR>, from <HOSPITAL> in <CITY>,  attended to the patient on <DATE>.
# The patient’s medical record number is <MEDICALRECORD>
# patient, <PATIENT>, is <AGE> years old,  her Contact number: <PHONE> .

# Obfuscated
# ------------------------------
# Dr. Edwardo Graft, from MCBRIDE ORTHOPEDIC HOSPITAL in CLAMART,  attended to the patient on 14/06/2024.
# The patient’s medical record number is 78295621.
# The patient, Nathaneil Bakes, is 43 years old,  her Contact number: 308-657-8469 .
# 
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_sentwise_benchmark_large|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.4 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- PretrainedZeroShotNER
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