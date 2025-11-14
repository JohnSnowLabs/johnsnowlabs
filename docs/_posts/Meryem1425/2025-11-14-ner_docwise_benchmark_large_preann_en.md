---
layout: model
title: NER Pipeline Benchmark Large (Document Wise)
author: John Snow Labs
name: pp_docwise_benchmark_large_preann
date: 2025-11-14
tags: [ner, en, licensed, clinical, pipeline, docwise]
task: [Named Entity Recognition, Pipeline Healthcare]
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

This pipeline can be used to detect PHI entities in medical texts using Named Entity Recognition (NER). It identifies various types of sensitive entities such as:
'MEDICALRECORD', 'LOCATION', 'PROFESSION', 'DOCTOR', 'USERNAME', 'CITY', 'ZIP', 'STATE', 'PATIENT', 'COUNTRY', 'STREET', 'HOSPITAL', 'DLN', 'IDNUM', 'AGE', 'DATE', 'PHONE', 'EMAIL', 'ORGANIZATION', 'SSN', 'ACCOUNT', 'PLATE', 'VIN', 'LICENSE', 'URL', 'IP'

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/pp_docwise_benchmark_large_preann_en_6.0.4_3.4_1763089642103.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/pp_docwise_benchmark_large_preann_en_6.0.4_3.4_1763089642103.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_docwise = PretrainedPipeline("pp_docwise_benchmark_large_preann", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

result = ner_docwise.fullAnnotate(text)


```

{:.jsl-block}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_docwise = nlp.PretrainedPipeline("pp_docwise_benchmark_large_preann", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

result = ner_docwise.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_docwise = PretrainedPipeline("pp_docwise_benchmark_large_preann", "en", "clinical/models")

val text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

val result = ner_docwise.fullAnnotate(text)

```
</div>

## Results

```bash

+--------------------+-----+---+---------+
|chunk               |begin|end|ner_label|
+--------------------+-----+---+---------+
|John Lee            |4    |11 |DOCTOR   |
|Royal Medical Clinic|19   |38 |HOSPITAL |
|Chicago             |43   |49 |CITY     |
|11/05/2024          |79   |88 |DATE     |
|56467890            |130  |137|IDNUM    |
|Emma Wilson         |153  |163|PATIENT  |
|50 years old        |169  |180|AGE      |
|444-456-7890        |203  |214|PHONE    |
+--------------------+-----+---+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|pp_docwise_benchmark_large_preann|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.4 GB|

## Included Models

- DocumentAssembler
- InternalDocumentSplitter
- TokenizerModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- PretrainedZeroShotNER
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
