---
layout: model
title: Pipeline to Detect Drug Entities - Generic
author: John Snow Labs
name: ner_medication_generic_pipeline
date: 2024-04-25
tags: [licensed, en, medication, ner, pipeline]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pre-trained pipeline is designed to identify generic `DRUG` entities in clinical texts. It was built on top of the `ner_posology_greedy`, `ner_jsl_greedy`, `ner_drugs_large` and `drug_matcher` models to detect the entities `DRUG`, `DOSAGE`, `ROUTE` and `STRENGTH`, chunking them into a larger entity as `DRUG` when they appear together.
The main distinction from the `medication_ner_pipeline` is that it chunks these entities together, whereas the `medication_ner_pipeline` chunks them separately.

Predicted entities: `DRUG`

## Predicted Entities

`DRUG`


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_medication_generic_pipeline_en_5.3.1_3.2_1714046788033.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_medication_generic_pipeline_en_5.3.1_3.2_1714046788033.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_medication_generic_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient described the epigastric pain as burning and worsening after meals, often accompanied by heartburn and regurgitation, particularly when lying down.
Additionally, he reported discomfort and bloating associated with infrequent bowel movements. In response, his doctor prescribed a regimen tailored to his conditions:
Thiamine 100 mg , Folic acid 1 mg , multivitamins , Calcium carbonate plus Vitamin D 250 mg , Heparin 5000 units subcutaneously , Prilosec 20 mg , Senna two tabs .""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_medication_generic_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient described the epigastric pain as burning and worsening after meals, often accompanied by heartburn and regurgitation, particularly when lying down.
Additionally, he reported discomfort and bloating associated with infrequent bowel movements. In response, his doctor prescribed a regimen tailored to his conditions:
Thiamine 100 mg , Folic acid 1 mg , multivitamins , Calcium carbonate plus Vitamin D 250 mg , Heparin 5000 units subcutaneously , Prilosec 20 mg , Senna two tabs .""")

```
</div>

## Results

```bash

+---------------------------------+---------+
|medication_greedy_chunk          |ner_label|
+---------------------------------+---------+
|Thiamine 100 mg                  |DRUG     |
|Folic acid 1 mg                  |DRUG     |
|multivitamins                    |DRUG     |
|Calcium carbonate                |DRUG     |
|Vitamin D 250 mg                 |DRUG     |
|Heparin 5000 units subcutaneously|DRUG     |
|Prilosec 20 mg                   |DRUG     |
|Senna two tabs                   |DRUG     |
+---------------------------------+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_medication_generic_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.1+|
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
- MedicalNerModel
- NerConverter
- TextMatcherInternalModel
- ChunkMergeModel
