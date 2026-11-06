---
layout: model
title: Clinical Deidentification Pipeline Rule Based (Document Wise)
author: John Snow Labs
name: clinical_deidentification_docwise_rule_based
date: 2026-11-05
tags: [deidentification, deid, en, licensed, clinical, pipeline, docwise, rule_based]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 7.0.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This rule-based pipeline (no NER models) can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text.
Names, hospitals and street addresses are not detected, since those require NER models.
The pipeline can mask and obfuscate 'MEDICALRECORD', 'CITY', 'ZIP', 'STATE', 'COUNTRY', 'DLN', 'IDNUM', 'SSN', 'ACCOUNT', 'PLATE', 'VIN', 'LICENSE', 'AGE', 'PHONE', 'DATE', 'EMAIL', 'URL', 'IP' entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_docwise_rule_based_en_7.0.0_3.4_1793896131220.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_docwise_rule_based_en_7.0.0_3.4_1793896131220.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_docwise_rule_based", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)

print(deid_result[0]["masked"][0].result)
print(deid_result[0]["obfuscated"][0].result)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp

deid_pipeline = nlp.PretrainedPipeline("clinical_deidentification_docwise_rule_based", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)

print(deid_result[0]["masked"][0].result)
print(deid_result[0]["obfuscated"][0].result)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_docwise_rule_based", "en", "clinical/models")

val text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

val deid_result = deid_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

Masked with entity labels
------------------------------
Dr. John Lee, from Royal Medical Clinic in <CITY>, attended to the patient on <DATE>.
The patient’s medical record number is <MEDICALRECORD>.
The patient, Emma Wilson, is <AGE>, her Contact number: <PHONE> .

Obfuscated
------------------------------
Dr. John Lee, from Royal Medical Clinic in Berea, attended to the patient on 24/06/2024.
The patient’s medical record number is 78689012.
The patient, Emma Wilson, is 55 years old, her Contact number: 666-678-9012 .

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_docwise_rule_based|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 7.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.2 MB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- ContextualParserModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- ChunkMergeModel
- ChunkMergeModel
- ChunkMergeModel
- LightDeIdentification
- LightDeIdentification