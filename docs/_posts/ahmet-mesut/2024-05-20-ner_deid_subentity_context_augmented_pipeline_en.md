---
layout: model
title: Detect PHI for Deidentification (Subentity- Context Augmented)
author: John Snow Labs
name: ner_deid_subentity_context_augmented_pipeline
date: 2024-05-20
tags: [deidentification, en, licensed, clinical, pipeline, ner, phi, subentity]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.2
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to extract PHI information such as `AGE`, `BIOID`, `CITY`, `COUNTRY`, `DATE`, `DEVICE`, `DOCTOR`, `EMAIL`, `FAX`, `HEALTHPLAN`, `HOSPITAL`, `IDNUM`, `LOCATION`, `MEDICALRECORD`, `ORGANIZATION`, `PATIENT`, `PHONE`, `PROFESSION`, `STATE`, `STREET`, `URL`, `USERNAME`, `ZIP`, `ACCOUNT`, `LICENSE`, `VIN`, `SSN`, `DLN`, `PLATE`, `IPADDR` entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_context_augmented_pipeline_en_5.3.2_3.2_1716192476978.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_context_augmented_pipeline_en_5.3.2_3.2_1716192476978.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("ner_deid_subentity_context_augmented_pipeline", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR: 719435.
Dr. John Green, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

result = deid_pipeline.fullAnnotate(text)


```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("ner_deid_subentity_context_augmented_pipeline", "en", "clinical/models")

val text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR: 719435.
Dr. John Green, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

val result = deid_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

|    | chunk             |   begin |   end | entity        |
|---:|:------------------|--------:|------:|:--------------|
|  0 | Hendrickson, Ora  |       7 |    22 | PATIENT       |
|  1 | 2093-01-13        |      38 |    47 | DATE          |
|  2 | 719435            |      54 |    59 | MEDICALRECORD |
|  3 | John Green        |      66 |    75 | DOCTOR        |
|  4 | 203.120.223.13    |      81 |    94 | IPADDR        |
|  5 | 60                |     105 |   106 | AGE           |
|  6 | Day Hospital      |     142 |   153 | HOSPITAL      |
|  7 | 01/13/93          |     173 |   180 | DATE          |
|  8 | 1HGBH41JXMN109286 |     199 |   215 | VIN           |
|  9 | #333-44-6666      |     222 |   233 | SSN           |
| 10 | A334455B          |     257 |   264 | DLN           |
| 11 | (302) 786-5227    |     273 |   286 | PHONE         |
| 12 | 0295 Keats Street |     289 |   305 | STREET        |
| 13 | San Francisco     |     308 |   320 | CITY          |
| 14 | smith@gmail.com   |     331 |   345 | EMAIL         |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_subentity_context_augmented_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.2+|
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
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- TextMatcherModel
- ContextualParserModel
- RegexMatcherModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcherInternalModel
- ChunkMergeModel
- ChunkMergeModel