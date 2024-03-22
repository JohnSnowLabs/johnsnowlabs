---
layout: model
title: Pipeline to Detect Medication Entities
author: John Snow Labs
name: ner_medication_pipeline
date: 2024-03-22
tags: [licensed, en, medication, ner, pipeline]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

A pretrained pipeline to detect medication entities. It was built on the top of `ner_posology`, `ner_jsl` and `drug_matcher` models.
Predicted entities: `DRUG`, `DOSAGE`, `FREQUENCY`, `ROUTE` and `STRENGTH`.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_medication_pipeline_en_5.3.0_3.0_1711109995717.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_medication_pipeline_en_5.3.0_3.0_1711109995717.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_medication_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""John Smith, a 55-year-old male with a medical history of hypertension, Type 2 Diabetes Mellitus, Hyperlipidemia, Gastroesophageal Reflux Disease (GERD), and chronic constipation, presented with persistent epigastric pain, heartburn, and infrequent bowel movements. He described the epigastric pain as burning and worsening after meals, often accompanied by heartburn and regurgitation, particularly when lying down. Additionally, he reported discomfort and bloating associated with infrequent bowel movements. In response, his doctor prescribed a regimen tailored to his conditions: Thiamine 100 mg q.day , Folic acid 1 mg q.day , multivitamins q.day , Calcium carbonate plus Vitamin D 250 mg t.i.d. , Heparin 5000 units subcutaneously b.i.d. , Prilosec 20 mg q.day , Senna two tabs qhs . The patient was advised to follow a low-fat diet, avoid spicy and acidic foods, and elevate the head of the bed to alleviate GERD symptoms. Lifestyle modifications including regular exercise, smoking cessation, and moderation in alcohol consumption were recommended to manage his chronic conditions effectively. A follow-up appointment in two weeks was scheduled.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_medication_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""John Smith, a 55-year-old male with a medical history of hypertension, Type 2 Diabetes Mellitus, Hyperlipidemia, Gastroesophageal Reflux Disease (GERD), and chronic constipation, presented with persistent epigastric pain, heartburn, and infrequent bowel movements. He described the epigastric pain as burning and worsening after meals, often accompanied by heartburn and regurgitation, particularly when lying down. Additionally, he reported discomfort and bloating associated with infrequent bowel movements. In response, his doctor prescribed a regimen tailored to his conditions: Thiamine 100 mg q.day , Folic acid 1 mg q.day , multivitamins q.day , Calcium carbonate plus Vitamin D 250 mg t.i.d. , Heparin 5000 units subcutaneously b.i.d. , Prilosec 20 mg q.day , Senna two tabs qhs . The patient was advised to follow a low-fat diet, avoid spicy and acidic foods, and elevate the head of the bed to alleviate GERD symptoms. Lifestyle modifications including regular exercise, smoking cessation, and moderation in alcohol consumption were recommended to manage his chronic conditions effectively. A follow-up appointment in two weeks was scheduled.""")

```
</div>

## Results

```bash

+-----------------+---------+
| medication_chunk|ner_label|
+-----------------+---------+
|         Thiamine|     DRUG|
|           100 mg| STRENGTH|
|            q.day|FREQUENCY|
|       Folic acid|     DRUG|
|             1 mg| STRENGTH|
|            q.day|FREQUENCY|
|    multivitamins|     DRUG|
|            q.day|FREQUENCY|
|Calcium carbonate|     DRUG|
|        Vitamin D|     DRUG|
|           250 mg| STRENGTH|
|            t.i.d|FREQUENCY|
|          Heparin|     DRUG|
|       5000 units|   DOSAGE|
|   subcutaneously|    ROUTE|
|            b.i.d|FREQUENCY|
|         Prilosec|     DRUG|
|            20 mg| STRENGTH|
|            q.day|FREQUENCY|
|            Senna|     DRUG|
|              two|   DOSAGE|
|             tabs|     FORM|
|              qhs|FREQUENCY|
+-----------------+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_medication_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
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
- TextMatcherInternalModel
- ChunkMergeModel
