---
layout: model
title: Clinical Deidentification Pipeline (Sentence Wise)
author: John Snow Labs
name: ner_deid_nameAugmented_pipeline_v3
date: 2025-03-25
tags: [deidentification, deid, en, licensed, clinical, pipeline, name]
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
The pipeline can mask and obfuscate `ACCOUNT`, `AGE`, `BIOID`, `CITY`, `CONTACT`, `COUNTRY`, `DATE`, `DEVICE`, `DLN`, `EMAIL`, `FAX`, `HEALTHPLAN`, `IDNUM`, `IP`, `LICENSE`,
`LOCATION`, `MEDICALRECORD`, `NAME`, `ORGANIZATION`, `PHONE`, `PLATE`, `PROFESSION`, `SSN`, `STATE`, `STREET`, `VIN`, `ZIP` entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_nameAugmented_pipeline_v3_en_5.5.3_3.4_1742879543250.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_nameAugmented_pipeline_v3_en_5.5.3_3.4_1742879543250.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("ner_deid_nameAugmented_pipeline_v3", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline2.fullAnnotate(text)[0]


```

{:.jsl-block}
```python

deid_pipeline = nlp.PretrainedPipeline("ner_deid_nameAugmented_pipeline_v3", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)[0]



```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("ner_deid_nameAugmented_pipeline_v3", "en", "clinical/models")

val text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."""

val deid_result = deid_pipeline.fullAnnotate(text)[0]


```
</div>

## Results

```bash

+--------------------+-----+---+-------------+
|result              |begin|end|entity       |
+--------------------+-----+---+-------------+
|John Lee            |4    |11 |NAME         |
|Royal Medical Clinic|19   |38 |LOCATION     |
|Chicago             |43   |49 |CITY         |
|11/05/2024          |80   |89 |DATE         |
|56467890            |131  |138|MEDICALRECORD|
|Emma Wilson         |153  |163|NAME         |
|50                  |169  |170|AGE          |
|444-456-7890        |204  |215|PHONE        |
+--------------------+-----+---+-------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_nameAugmented_pipeline_v3|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.9 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- NerDLModel
- NerConverterInternalModel
- WordEmbeddingsModel
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
