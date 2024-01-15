---
layout: model
title: Explain Document Voice Of Patient (VOP)
author: John Snow Labs
name: explain_document_vop
date: 2024-01-15
tags: [licensed, clinical, en, vop, pipeline, ner, assertion, relation_extraction]
task: [Named Entity Recognition, Assertion Status, Relation Extraction, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to:

    - extract all clinical/medical entities from text,

    - assign assertion status to the extracted entities,

    - establish relations between the extracted entities.

6 NER models, one assertion model and one relation extraction model were used in order to achieve those tasks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_document_vop_en_5.2.0_3.0_1705351698242.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_document_vop_en_5.2.0_3.0_1705351698242.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_document_vop", "en", "clinical/models")

result = ner_pipeline.annotate("""I had been feeling really tired all the time and was losing weight without even trying. My doctor checked my sugar levels and they came out to be high. So, I have type 2 diabetes. 
He put me on two medications - I take metformin 500 mg twice a day, and glipizide 5 mg before breakfast and dinner. I also have to watch what I eat and try to exercise more.
Now, I also have chronic acid reflux disease or GERD. Now I take a daily pill called omeprazole 20 mg to reduce the stomach acid and control the heartburn symptoms.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_document_vop", "en", "clinical/models")

val result = ner_pipeline.annotate("""I had been feeling really tired all the time and was losing weight without even trying. My doctor checked my sugar levels and they came out to be high. So, I have type 2 diabetes. 
He put me on two medications - I take metformin 500 mg twice a day, and glipizide 5 mg before breakfast and dinner. I also have to watch what I eat and try to exercise more.
Now, I also have chronic acid reflux disease or GERD. Now I take a daily pill called omeprazole 20 mg to reduce the stomach acid and control the heartburn symptoms.""")

```
</div>

## Results

```bash
|    | chunks                      |   begin |   end | entities     |
|---:|:----------------------------|--------:|------:|:-------------|
|  0 | feeling really tired        |      11 |    30 | Symptom      |
|  1 | all the time                |      32 |    43 | Duration     |
|  2 | losing weight               |      53 |    65 | Symptom      |
|  3 | sugar levels                |     109 |   120 | Test         |
|  4 | high                        |     146 |   149 | TestResult   |
|  5 | type 2 diabetes             |     163 |   177 | Disease      |
|  6 | He                          |     181 |   182 | Gender       |
|  7 | metformin                   |     219 |   227 | Drug         |
|  8 | 500 mg                      |     229 |   234 | Strength     |
|  9 | twice a day                 |     236 |   246 | Frequency    |
| 10 | glipizide                   |     253 |   261 | Drug         |
| 11 | 5 mg                        |     263 |   266 | Strength     |
| 12 | before breakfast and dinner |     268 |   294 | Frequency    |
| 13 | exercise                    |     340 |   347 | HealthStatus |
| 14 | Now                         |     355 |   357 | DateTime     |
| 15 | chronic acid reflux disease |     372 |   398 | Disease      |
| 16 | GERD                        |     403 |   406 | Disease      |
| 17 | Now                         |     409 |   411 | DateTime     |
| 18 | daily                       |     422 |   426 | Frequency    |
| 19 | pill                        |     428 |   431 | Drug         |
| 20 | omeprazole                  |     440 |   449 | Drug         |
| 21 | 20 mg                       |     451 |   455 | Strength     |
| 22 | stomach acid                |     471 |   482 | Drug         |
| 23 | heartburn symptoms          |     500 |   517 | Symptom      |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_document_vop|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
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
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- GenericREModel