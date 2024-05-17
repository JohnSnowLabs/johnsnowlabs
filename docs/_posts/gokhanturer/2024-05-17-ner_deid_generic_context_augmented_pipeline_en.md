---
layout: model
title: Detect PHI for Deidentification (Generic - Context Augmented)
author: John Snow Labs
name: ner_deid_generic_context_augmented_pipeline
date: 2024-05-17
tags: [deidentification, deid, en, licensed, clinical, pipeline, ner, phi, generic]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.2
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to extract PHI information such as AGE`, `CONTACT`, `DATE`, `LOCATION`, `NAME`, `PROFESSION`,  `IDNUM`, `MEDICALRECORD`, `ORGANIZATION`, `PHONE`, `ACCOUNT`, `LICENSE`, `VIN`, `SSN`, `DLN`, `PLATE` entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_context_augmented_pipeline_en_5.3.2_3.0_1715968098284.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_context_augmented_pipeline_en_5.3.2_3.0_1715968098284.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("ner_deid_generic_context_augmented_pipeline", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

result = deid_pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("ner_deid_generic_context_augmented_pipeline", "en", "clinical/models")

val text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

val result = deid_pipeline.fullAnnotate(text)
```
</div>

## Results

```bash

|    | chunk             |   begin |   end | entity   |
|---:|:------------------|--------:|------:|:---------|
|  0 | Hendrickson, Ora  |       7 |    22 | NAME     |
|  1 | 2093-01-13        |      41 |    50 | DATE     |
|  2 | John Green        |      66 |    75 | NAME     |
|  3 | 1231511863        |      82 |    91 | ID       |
|  4 | 60                |     121 |   122 | AGE      |
|  5 | Day Hospital      |     158 |   169 | LOCATION |
|  6 | 01/13/93          |     189 |   196 | DATE     |
|  7 | 1HGBH41JXMN109286 |     215 |   231 | VIN      |
|  8 | #333-44-6666      |     238 |   249 | SSN      |
|  9 | A334455B          |     273 |   280 | DLN      |
| 10 | (302) 786-5227    |     289 |   302 | PHONE    |
| 11 | 0295 Keats Street |     305 |   321 | LOCATION |
| 12 | San Francisco     |     324 |   336 | LOCATION |
| 13 | smith@gmail.com   |     347 |   361 | EMAIL    |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_generic_context_augmented_pipeline|
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
- TextMatcherInternalModel
- ContextualParserModel
- RegexMatcherModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ChunkMergeModel
- ChunkMergeModel
