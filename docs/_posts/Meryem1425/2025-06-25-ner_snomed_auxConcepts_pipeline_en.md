---
layout: model
title: Pipeline for Extracting Clinical Entities Related to SNOMED Concept Codes
author: John Snow Labs
name: ner_snomed_auxConcepts_pipeline
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

This pipeline is designed to extract all entities mappable to SNOMED Concept codes.

2 NER models are used to achieve those tasks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_snomed_auxConcepts_pipeline_en_6.0.2_3.4_1750869483327.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_snomed_auxConcepts_pipeline_en_6.0.2_3.4_1750869483327.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_snomed_auxConcepts_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. 
He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. 
He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. 
He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_snomed_auxConcepts_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. 
He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. 
He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. 
He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction.
""")

```
</div>

## Results

```bash
|    | chunks                  |   begin |   end | entities        |
|---:|:------------------------|--------:|------:|:----------------|
|  0 | tobacco                 |      53 |    59 | Smoking         |
|  1 | nonspecific             |     179 |   189 | Modifier        |
|  2 | cardiac catheterization |     268 |   290 | Procedure       |
|  3 | atropine                |     440 |   447 | Drug_Ingredient |
|  4 | IV fluids               |     450 |   458 | TREATMENT       |
|  5 | dopamine                |     465 |   472 | Drug_Ingredient |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_snomed_auxConcepts_pipeline|
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
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- ChunkMergeModel