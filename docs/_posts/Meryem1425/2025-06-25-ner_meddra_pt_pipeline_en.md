---
layout: model
title: Pipeline for Extracting Clinical Entities Related to MedDRA PT (Preferred Term) Codes
author: John Snow Labs
name: ner_meddra_pt_pipeline
date: 2025-06-25
tags: [licensed, en, clinical, pipeline, ner]
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

This pipeline is designed to extract all entities mappable to MedDRA PT (Preferred Term) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_meddra_pt_pipeline_en_6.0.2_3.4_1750861074389.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_meddra_pt_pipeline_en_6.0.2_3.4_1750861074389.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_meddra_pt_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""This is an 82-year-old male with a history of prior tobacco use, benign hypertension, chronic renal insufficiency, chronic bronchitis, gastritis, and ischemic attack. 
He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. 
He underwent cardiac catheterization because of the left main coronary artery stenosis, which was complicated by hypotension and bradycardia. 
We describe the side effects of 5-FU in a colon cancer patient who suffered mucositis and dermatitis.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_meddra_pt_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""This is an 82-year-old male with a history of prior tobacco use, benign hypertension, chronic renal insufficiency, chronic bronchitis, gastritis, and ischemic attack. 
He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. 
He underwent cardiac catheterization because of the left main coronary artery stenosis, which was complicated by hypotension and bradycardia. 
We describe the side effects of 5-FU in a colon cancer patient who suffered mucositis and dermatitis.""")

```
</div>

## Results

```bash
|    | chunks                                 |   begin |   end | entities                  |
|---:|:---------------------------------------|--------:|------:|:--------------------------|
|  0 | tobacco                                |      53 |    59 | Smoking                   |
|  1 | benign hypertension                    |      66 |    84 | PROBLEM                   |
|  2 | chronic renal insufficiency            |      87 |   113 | Kidney_Disease            |
|  3 | chronic bronchitis                     |     116 |   133 | PROBLEM                   |
|  4 | gastritis                              |     136 |   144 | Disease_Syndrome_Disorder |
|  5 | ischemic attack                        |     151 |   165 | Cerebrovascular_Disease   |
|  6 | ST elevation                           |     210 |   221 | PROBLEM                   |
|  7 | cardiac catheterization                |     283 |   305 | Procedure                 |
|  8 | the left main coronary artery stenosis |     318 |   355 | PROBLEM                   |
|  9 | hypotension                            |     383 |   393 | VS_Finding                |
| 10 | bradycardia                            |     399 |   409 | VS_Finding                |
| 11 | the side effects                       |     425 |   440 | PROBLEM                   |
| 12 | a colon cancer                         |     453 |   466 | PROBLEM                   |
| 13 | mucositis                              |     489 |   497 | Disease_Syndrome_Disorder |
| 14 | dermatitis                             |     503 |   512 | Disease_Syndrome_Disorder |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_meddra_pt_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
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
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel