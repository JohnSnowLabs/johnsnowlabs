---
layout: model
title: Explain Document Voice Of Patient (VOP)
author: John Snow Labs
name: explain_document_vop
date: 2024-01-15
tags: [licensed, clinical, en, vop, pipeline, ner, assertion, relation_extraction]
task: [Named Entity Recognition, Assertion Status, Relation Extraction, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.2
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_document_vop_en_5.2.0_3.2_1705353221923.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_document_vop_en_5.2.0_3.2_1705353221923.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
# NER and Assertion Status Results
|    | chunks                      | entities     | assertion              |
|---:|-----------------------------|--------------|------------------------|
|  0 | feeling really tired        | Symptom      | Present_Or_Past        |
|  1 | all the time                | Duration     | Present_Or_Past        |
|  2 | losing weight               | Symptom      | Present_Or_Past        |
|  3 | sugar levels                | Test         | Present_Or_Past        |
|  4 | high                        | TestResult   | Present_Or_Past        |
|  5 | type 2 diabetes             | Disease      | Present_Or_Past        |
|  6 | He                          | Gender       | SomeoneElse            |
|  7 | metformin                   | Drug         | Present_Or_Past        |
|  8 | 500 mg                      | Strength     | Present_Or_Past        |
|  9 | twice a day                 | Frequency    | Present_Or_Past        |
| 10 | glipizide                   | Drug         | Present_Or_Past        |
| 11 | 5 mg                        | Strength     | Present_Or_Past        |
| 12 | before breakfast and dinner | Frequency    | Present_Or_Past        |
| 13 | exercise                    | HealthStatus | Hypothetical_Or_Absent |
| 14 | Now                         | DateTime     | Present_Or_Past        |
| 15 | chronic acid reflux disease | Disease      | Present_Or_Past        |
| 16 | GERD                        | Disease      | Present_Or_Past        |
| 17 | Now                         | DateTime     | Present_Or_Past        |
| 18 | daily                       | Frequency    | Present_Or_Past        |
| 19 | pill                        | Drug         | Present_Or_Past        |
| 20 | omeprazole                  | Drug         | Present_Or_Past        |
| 21 | 20 mg                       | Strength     | Present_Or_Past        |
| 22 | stomach acid                | Drug         | Present_Or_Past        |
| 23 | heartburn symptoms          | Symptom      | Present_Or_Past        |

# Relation Extraction Results
|    | sentence | entity1_begin | entity1_end | chunk1       | entity1   | entity2_begin | entity2_end | chunk2                      | entity2    | relation        | confidence |
|---:|---------:|--------------:|------------:|--------------|-----------|---------------|-------------|-----------------------------|------------|-----------------|-----------:|
|  0 | 1        | 109           | 120         | sugar levels | Test      | 146           | 149         | high                        | TestResult | Test-TestResult | 1.0        |
|  1 | 3        | 219           | 227         | metformin    | Drug      | 229           | 234         | 500 mg                      | Strength   | Drug-Strength   | 1.0        |
|  2 | 3        | 219           | 227         | metformin    | Drug      | 236           | 246         | twice a day                 | Frequency  | Drug-Frequency  | 1.0        |
|  3 | 3        | 219           | 227         | metformin    | Drug      | 253           | 261         | glipizide                   | Drug       | Drug-Drug       | 1.0        |
|  4 | 3        | 219           | 227         | metformin    | Drug      | 263           | 266         | 5 mg                        | Strength   | Drug-Strength   | 1.0        |
|  5 | 3        | 229           | 234         | 500 mg       | Strength  | 253           | 261         | glipizide                   | Drug       | Strength-Drug   | 1.0        |
|  6 | 3        | 253           | 261         | glipizide    | Drug      | 263           | 266         | 5 mg                        | Strength   | Drug-Strength   | 1.0        |
|  7 | 3        | 253           | 261         | glipizide    | Drug      | 268           | 294         | before breakfast and dinner | Frequency  | Drug-Frequency  | 1.0        |
|  8 | 6        | 422           | 426         | daily        | Frequency | 428           | 431         | pill                        | Drug       | Frequency-Drug  | 1.0        |
|  9 | 6        | 422           | 426         | daily        | Frequency | 440           | 449         | omeprazole                  | Drug       | Frequency-Drug  | 1.0        |
| 10 | 6        | 428           | 431         | pill         | Drug      | 440           | 449         | omeprazole                  | Drug       | Drug-Drug       | 1.0        |
| 11 | 6        | 428           | 431         | pill         | Drug      | 451           | 455         | 20 mg                       | Strength   | Drug-Strength   | 1.0        |
| 12 | 6        | 440           | 449         | omeprazole   | Drug      | 451           | 455         | 20 mg                       | Strength   | Drug-Strength   | 1.0        |
| 13 | 6        | 440           | 449         | omeprazole   | Drug      | 471           | 482         | stomach acid                | Drug       | Drug-Drug       | 1.0        |
| 14 | 6        | 451           | 455         | 20 mg        | Strength  | 471           | 482         | stomach acid                | Drug       | Strength-Drug   | 1.0        |
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
