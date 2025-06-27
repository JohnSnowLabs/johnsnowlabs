---
layout: model
title: Explain Clinical Document Medications - Light
author: John Snow Labs
name: explain_clinical_doc_medication_light
date: 2025-06-27
tags: [licensed, en, clinical, pipeline, ner, medication]
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

This pipeline is designed to extract medication entities from texts. 

2 NER models and a text matcher are used to extract the medication entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_medication_light_en_6.0.2_3.4_1751045799607.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_medication_light_en_6.0.2_3.4_1751045799607.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_medication_light", "en", "clinical/models")

result = ner_pipeline.annotate("""John Smith, a 55-year-old male with a medical history of hypertension, Type 2 Diabetes Mellitus, Hyperlipidemia, Gastroesophageal Reflux Disease (GERD), 
and chronic constipation, presented with persistent epigastric pain, heartburn, and infrequent bowel movements. 
He described the epigastric pain as burning and worsening after meals, often accompanied by heartburn and regurgitation, particularly when lying down. 
In response, his doctor prescribed a regimen tailored to his conditions: 
Thiamine 100 mg q.day , Folic acid 1 mg q.day , multivitamins q.day , Calcium carbonate plus Vitamin D 250 mg t.i.d. , Heparin 5000 units subcutaneously b.i.d. , Prilosec 20 mg q.day , Senna two tabs qhs.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_medication_light", "en", "clinical/models")

val result = ner_pipeline.annotate("""John Smith, a 55-year-old male with a medical history of hypertension, Type 2 Diabetes Mellitus, Hyperlipidemia, Gastroesophageal Reflux Disease (GERD), 
and chronic constipation, presented with persistent epigastric pain, heartburn, and infrequent bowel movements. 
He described the epigastric pain as burning and worsening after meals, often accompanied by heartburn and regurgitation, particularly when lying down. 
In response, his doctor prescribed a regimen tailored to his conditions: 
Thiamine 100 mg q.day , Folic acid 1 mg q.day , multivitamins q.day , Calcium carbonate plus Vitamin D 250 mg t.i.d. , Heparin 5000 units subcutaneously b.i.d. , Prilosec 20 mg q.day , Senna two tabs qhs.
""")

```
</div>

## Results

```bash
|    | chunks            |   begin |   end | entities   |
|---:|:------------------|--------:|------:|:-----------|
|  0 | Thiamine          |     493 |   500 | DRUG       |
|  1 | 100 mg            |     502 |   507 | STRENGTH   |
|  2 | q.day             |     509 |   513 | FREQUENCY  |
|  3 | Folic acid        |     517 |   526 | DRUG       |
|  4 | 1 mg              |     528 |   531 | STRENGTH   |
|  5 | q.day             |     533 |   537 | FREQUENCY  |
|  6 | multivitamins     |     541 |   553 | DRUG       |
|  7 | q.day             |     555 |   559 | FREQUENCY  |
|  8 | Calcium carbonate |     563 |   579 | DRUG       |
|  9 | Vitamin D         |     586 |   594 | DRUG       |
| 10 | 250 mg            |     596 |   601 | STRENGTH   |
| 11 | t.i.d             |     603 |   607 | FREQUENCY  |
| 12 | Heparin           |     612 |   618 | DRUG       |
| 13 | 5000 units        |     620 |   629 | DOSAGE     |
| 14 | subcutaneously    |     631 |   644 | ROUTE      |
| 15 | b.i.d             |     646 |   650 | FREQUENCY  |
| 16 | Prilosec          |     655 |   662 | DRUG       |
| 17 | 20 mg             |     664 |   668 | STRENGTH   |
| 18 | q.day             |     670 |   674 | FREQUENCY  |
| 19 | Senna             |     678 |   682 | DRUG       |
| 20 | two               |     684 |   686 | DOSAGE     |
| 21 | tabs              |     688 |   691 | FORM       |
| 22 | qhs               |     693 |   695 | FREQUENCY  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_medication_light|
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
- TextMatcherInternalModel
- ChunkMergeModel