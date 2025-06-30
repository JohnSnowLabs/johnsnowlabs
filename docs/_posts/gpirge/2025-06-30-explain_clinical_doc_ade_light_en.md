---
layout: model
title: Explain Clinical Document Medications & ADE - Light
author: John Snow Labs
name: explain_clinical_doc_ade_light
date: 2025-06-30
tags: [licensed, en, clinical, pipeline, ner, medication, ade]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to extract `ADE` and `DRUG` entities,
 and establish relations between the extracted `DRUG` and `ADE` results from the clinical documents.

2 NER models and a text matcher are used to accomplish the designated tasks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_ade_light_en_6.0.2_3.4_1751286030451.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_ade_light_en_6.0.2_3.4_1751286030451.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_ade_light", "en", "clinical/models")

result = ner_pipeline.annotate("""We describe the side effects of 5-FU in a colon cancer patient who suffered severe mucositis, desquamating dermatitis, prolonged myelosuppression, and neurologic toxicity that required admission to the intensive care unit. 
Anterior lumbosacral radiculopathy after intrathecal methotrexate treatment and acute erythroid leukemia after cyclophosphamide therapy for multiple myeloma: report of two cases.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_ade_light", "en", "clinical/models")

val result = ner_pipeline.annotate("""We describe the side effects of 5-FU in a colon cancer patient who suffered severe mucositis, desquamating dermatitis, prolonged myelosuppression, and neurologic toxicity that required admission to the intensive care unit. 
Anterior lumbosacral radiculopathy after intrathecal methotrexate treatment and acute erythroid leukemia after cyclophosphamide therapy for multiple myeloma: report of two cases.""")

```
</div>

## Results

```bash


NER Result

|    | chunks                             |   begin |   end | entities   |
|---:|:-----------------------------------|--------:|------:|:-----------|
|  0 | 5-FU                               |      32 |    35 | DRUG       |
|  1 | severe mucositis                   |      76 |    91 | ADE        |
|  2 | desquamating dermatitis            |      94 |   116 | ADE        |
|  3 | prolonged myelosuppression         |     119 |   144 | ADE        |
|  4 | neurologic toxicity                |     151 |   169 | ADE        |
|  5 | Anterior lumbosacral radiculopathy |     224 |   257 | ADE        |
|  6 | methotrexate                       |     277 |   288 | DRUG       |
|  7 | acute erythroid leukemia           |     304 |   327 | ADE        |
|  8 | cyclophosphamide                   |     335 |   350 | DRUG       |

# RE Result

|    |   relation | entity1   |   entity1_begin |   entity1_end | chunk1                             | entity2   |   entity2_begin |   entity2_end | chunk2                     |   confidence |
|---:|-----------:|:----------|----------------:|--------------:|:-----------------------------------|:----------|----------------:|--------------:|:---------------------------|-------------:|
|  0 |          1 | DRUG      |              32 |            35 | 5-FU                               | ADE       |              76 |            91 | severe mucositis           |            1 |
|  1 |          1 | DRUG      |              32 |            35 | 5-FU                               | ADE       |              94 |           116 | desquamating dermatitis    |            1 |
|  2 |          1 | DRUG      |              32 |            35 | 5-FU                               | ADE       |             119 |           144 | prolonged myelosuppression |            1 |
|  3 |          1 | DRUG      |              32 |            35 | 5-FU                               | ADE       |             151 |           169 | neurologic toxicity        |            1 |
|  4 |          1 | ADE       |             223 |           256 | Anterior lumbosacral radiculopathy | DRUG      |             276 |           287 | methotrexate               |            1 |
|  5 |          1 | ADE       |             223 |           256 | Anterior lumbosacral radiculopathy | DRUG      |             334 |           349 | cyclophosphamide           |            1 |
|  6 |          1 | DRUG      |             276 |           287 | methotrexate                       | ADE       |             303 |           326 | acute erythroid leukemia   |            1 |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_ade_light|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

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
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel