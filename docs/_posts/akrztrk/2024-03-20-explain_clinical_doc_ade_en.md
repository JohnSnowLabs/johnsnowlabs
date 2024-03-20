---
layout: model
title: Explain Clinical Document - ADE (Adverse Drug Event)
author: John Snow Labs
name: explain_clinical_doc_ade
date: 2024-03-20
tags: [licensed, en, resolver, ade, adverse]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This specialized ADE (Adverse Drug Event) pipeline can;

- extract `ADE` and `DRUG` entities,

- classify sentences whether they contain ADE entities or not,

- establish relations between the extracted `DRUG` and `ADE` results from the clinical documents.

In this pipeline, two NER, one text matcher, one sentence classifier, one assertion status detection and one relation extraction model were employed to accomplish the designated tasks.

- Clinical Entity Labels:  `ADE`, `DRUG`

- Assertion Status Labels:  `present`, `absent`, `possible`, `conditional`, `associated_with_someone_else`, `hypothetical`

- Relation Extraction Labels:  `1`, `0`

- Classification Model Labels:  `ADE`, `noADE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_ade_en_5.3.0_3.4_1710950282941.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_ade_en_5.3.0_3.4_1710950282941.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ade_pipeline = PretrainedPipeline("explain_clinical_doc_ade", "en", "clinical/models")

result = ade_pipeline.fullAnnotate("""The side effects of 5-FU in a colon cancer patient who suffered severe mucositis, desquamating dermatitis and prolonged myelosuppression. Last week the patient experienced anterior lumbosacral radiculopathy and blurred vision after intrathecal methotrexate treatment.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ade_pipeline = PretrainedPipeline("explain_clinical_doc_ade", "en", "clinical/models")

val result = ade_pipeline.fullAnnotate("""The side effects of 5-FU in a colon cancer patient who suffered severe mucositis, desquamating dermatitis and prolonged myelosuppression. Last week the patient experienced anterior lumbosacral radiculopathy and blurred vision after intrathecal methotrexate treatment.""")

```
</div>

## Results

```bash


NER and ASSERTION Result

|    | chunks                             |   begin |   end | entities   | assertion   |
|---:|:-----------------------------------|--------:|------:|:-----------|:------------|
|  0 | 5-FU                               |      20 |    23 | DRUG       | Past        |
|  1 | severe mucositis                   |      64 |    79 | ADE        | Past        |
|  2 | desquamating dermatitis            |      82 |   104 | ADE        | Past        |
|  3 | myelosuppression                   |     120 |   135 | ADE        | Past        |
|  4 | anterior lumbosacral radiculopathy |     172 |   205 | ADE        | Past        |
|  5 | blurred vision                     |     211 |   224 | ADE        | Past        |
|  6 | methotrexate                       |     244 |   255 | DRUG       | Past        |

# RE Result

|    |   relation | entity1   |   entity1_begin |   entity1_end | chunk1                             | entity2   |   entity2_begin |   entity2_end | chunk2                  |   confidence |
|---:|-----------:|:----------|----------------:|--------------:|:-----------------------------------|:----------|----------------:|--------------:|:------------------------|-------------:|
|  0 |          1 | DRUG      |              20 |            23 | 5-FU                               | ADE       |              64 |            79 | severe mucositis        |            1 |
|  1 |          1 | DRUG      |              20 |            23 | 5-FU                               | ADE       |              82 |           104 | desquamating dermatitis |            1 |
|  2 |          1 | DRUG      |              20 |            23 | 5-FU                               | ADE       |             120 |           135 | myelosuppression        |            1 |
|  3 |          1 | ADE       |             172 |           205 | anterior lumbosacral radiculopathy | DRUG      |             244 |           255 | methotrexate            |            1 |
|  4 |          1 | ADE       |             211 |           224 | blurred vision                     | DRUG      |             244 |           255 | methotrexate            |            1 |

# Classification Result

|    |   sentence_ID | sentence                                                                                                                                  | prediction   |
|---:|--------------:|:------------------------------------------------------------------------------------------------------------------------------------------|:-------------|
|  0 |             0 | The side effects of 5-FU in a colon cancer patient who suffered severe mucositis, desquamating dermatitis and prolonged myelosuppression. | ADE          |
|  1 |             1 | Last week the patient experienced anterior lumbosacral radiculopathy and blurred vision after intrathecal methotrexate treatment.         | ADE          |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_ade|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- TextMatcherInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel
- ChunkMapperModel
- AssertionDLModel
- MedicalBertForSequenceClassification
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
