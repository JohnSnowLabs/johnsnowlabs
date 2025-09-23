---
layout: model
title: NER Pipeline Benchmark Large (Document Wise)
author: John Snow Labs
name: ner_docwise_benchmark_large
date: 2025-07-31
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

This pipeline can be used to detect PHI entities in medical texts using Named Entity Recognition (NER).
It identifies various types of sensitive entities such as:
'CONTACT', 'DATE', 'ID', 'LOCATION', 'PROFESSION', 'DOCTOR', 'EMAIL', 'PATIENT', 'URL', 'USERNAME',
'CITY', 'COUNTRY', 'DLN', 'HOSPITAL', 'IDNUM', 'LOCATION_OTHER', 'MEDICALRECORD', 'STATE', 'STREET', 'ZIP', 'AGE',
'PHONE', 'ORGANIZATION', 'SSN', 'ACCOUNT', 'PLATE', 'VIN', 'LICENSE', and 'IP'.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_docwise_benchmark_large_en_6.0.4_3.4_1753992108698.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_docwise_benchmark_large_en_6.0.4_3.4_1753992108698.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("ner_docwise_benchmark_large", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)


```

{:.jsl-block}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = nlp.PretrainedPipeline("ner_docwise_benchmark_large", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("ner_docwise_benchmark_large", "en", "clinical/models")

val text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

val deid_result = deid_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash
|    | text                                                                                       | result                                                                                                                   |
|---:|:-------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|
|  0 | Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024. | ['John Lee', 'Royal Medical Clinic', 'Chicago', '11/05/2024', '56467890', 'Emma Wilson', '50 years old', '444-456-7890'] |
|    | The patient’s medical record number is 56467890.                                           |                                                                                                                          |
|    | The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 .              |                                                                                                                          |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_docwise_benchmark_large|
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