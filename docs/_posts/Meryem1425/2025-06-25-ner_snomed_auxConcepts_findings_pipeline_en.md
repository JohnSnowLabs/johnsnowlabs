---
layout: model
title: Pipeline for Extracting Clinical Entities Related to SNOMED (Findings and Concepts) Codes
author: John Snow Labs
name: ner_snomed_auxConcepts_findings_pipeline
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

This pipeline is designed to extract all entities mappable to SNOMED (Findings and Concepts) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_snomed_auxConcepts_findings_pipeline_en_6.0.2_3.4_1750883031752.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_snomed_auxConcepts_findings_pipeline_en_6.0.2_3.4_1750883031752.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_snomed_auxConcepts_findings_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, chronic obstructive pulmonary disease, gastritis, and transient ischemic attack. 
He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. 
He underwent cardiac catheterization because of the left main coronary artery stenosis, which was complicated by hypotension and bradycardia. 
He required atropine, IV fluids, and dopamine. He was subsequently transferred to the CCU for close monitoring
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_snomed_auxConcepts_findings_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, chronic obstructive pulmonary disease, gastritis, and transient ischemic attack. 
He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. 
He underwent cardiac catheterization because of the left main coronary artery stenosis, which was complicated by hypotension and bradycardia. 
He required atropine, IV fluids, and dopamine. He was subsequently transferred to the CCU for close monitoring
""")

```
</div>

## Results

```bash
|    | chunks                                 |   begin |   end | entities                  |
|---:|:---------------------------------------|--------:|------:|:--------------------------|
|  0 | tobacco                                |      53 |    59 | Smoking                   |
|  1 | hypertension                           |      66 |    77 | Hypertension              |
|  2 | chronic renal insufficiency            |      80 |   106 | Kidney_Disease            |
|  3 | chronic obstructive pulmonary disease  |     109 |   145 | Disease_Syndrome_Disorder |
|  4 | gastritis                              |     148 |   156 | Disease_Syndrome_Disorder |
|  5 | transient ischemic attack              |     163 |   187 | Cerebrovascular_Disease   |
|  6 | ST elevation                           |     232 |   243 | snomed_term               |
|  7 | cardiac catheterization                |     305 |   327 | Procedure                 |
|  8 | the left main coronary artery stenosis |     340 |   377 | PROBLEM                   |
|  9 | hypotension                            |     405 |   415 | VS_Finding                |
| 10 | bradycardia                            |     421 |   431 | VS_Finding                |
| 11 | atropine                               |     447 |   454 | Drug_Ingredient           |
| 12 | IV fluids                              |     457 |   465 | TREATMENT                 |
| 13 | dopamine                               |     472 |   479 | Drug_Ingredient           |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_snomed_auxConcepts_findings_pipeline|
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
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- ChunkMergeModel