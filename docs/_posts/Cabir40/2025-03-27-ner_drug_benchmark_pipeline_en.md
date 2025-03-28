---
layout: model
title: Detect Drug Entities (DRUG)
author: John Snow Labs
name: ner_drug_benchmark_pipeline
date: 2025-03-27
tags: [licensed, clinical, en, pipeline, ner, drug, benchmark]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.5.3
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to extract posology information in medical text.

## Predicted Entities

`DRUG`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_drug_benchmark_pipeline_en_5.5.3_3.4_1743116243013.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_drug_benchmark_pipeline_en_5.5.3_3.4_1743116243013.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_drug_benchmark_pipeline", "en", "clinical/models")

text = """The patient was admitted to the Surgical Intensive Care Unit postoperatively with stable hemodynamics on Lidocaine at one , Dobutamine at 200 and Nipride .
The patient was extubated by postoperative day # 1 but was noted to be relatively hypoxemic with high oxygen requirement .
Chest x-ray demonstrating pulmonary edema .
Aggressive diuresis was undertaken and the patient responded , albeit sluggishly .
In addition , he remained agitated .
This was attributed to mild hypoxia and / or his underlying psychiatric diagnoses and he was treated with Haldol appropriately .
On day # 2 the patient continued to diurese and this was maintained with the Lasix/ Mannitol infusion .
His urine output remained at 150 to 200 cc. an hour .
Despite this , his chest x-ray continued to show severe pulmonary edema and the clinical picture correlated .
He required anti-hypertensive therapy initially with Nipride which was changed to Hydralazine to avoid shunting .
Consequently his Pronestyl was discontinued .
In addition , the patient was given magnesium to bring his level above 2 ."""

result = ner_pipeline.fullAnnotate(text)
```

{:.jsl-block}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = nlp.PretrainedPipeline("ner_drug_benchmark_pipeline", "en", "clinical/models")

text = """The patient was admitted to the Surgical Intensive Care Unit postoperatively with stable hemodynamics on Lidocaine at one , Dobutamine at 200 and Nipride .
The patient was extubated by postoperative day # 1 but was noted to be relatively hypoxemic with high oxygen requirement .
Chest x-ray demonstrating pulmonary edema .
Aggressive diuresis was undertaken and the patient responded , albeit sluggishly .
In addition , he remained agitated .
This was attributed to mild hypoxia and / or his underlying psychiatric diagnoses and he was treated with Haldol appropriately .
On day # 2 the patient continued to diurese and this was maintained with the Lasix/ Mannitol infusion .
His urine output remained at 150 to 200 cc. an hour .
Despite this , his chest x-ray continued to show severe pulmonary edema and the clinical picture correlated .
He required anti-hypertensive therapy initially with Nipride which was changed to Hydralazine to avoid shunting .
Consequently his Pronestyl was discontinued .
In addition , the patient was given magnesium to bring his level above 2 ."""

result = ner_pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_drug_benchmark_pipeline", "en", "clinical/models")

val text = """The patient was admitted to the Surgical Intensive Care Unit postoperatively with stable hemodynamics on Lidocaine at one , Dobutamine at 200 and Nipride .
The patient was extubated by postoperative day # 1 but was noted to be relatively hypoxemic with high oxygen requirement .
Chest x-ray demonstrating pulmonary edema .
Aggressive diuresis was undertaken and the patient responded , albeit sluggishly .
In addition , he remained agitated .
This was attributed to mild hypoxia and / or his underlying psychiatric diagnoses and he was treated with Haldol appropriately .
On day # 2 the patient continued to diurese and this was maintained with the Lasix/ Mannitol infusion .
His urine output remained at 150 to 200 cc. an hour .
Despite this , his chest x-ray continued to show severe pulmonary edema and the clinical picture correlated .
He required anti-hypertensive therapy initially with Nipride which was changed to Hydralazine to avoid shunting .
Consequently his Pronestyl was discontinued .
In addition , the patient was given magnesium to bring his level above 2 ."""

val result = ner_pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | chunk       |   begin |   end | ner_label   |
|---:|:------------|--------:|------:|:------------|
|  0 | Lidocaine   |     105 |   113 | DRUG        |
|  1 | Dobutamine  |     124 |   133 | DRUG        |
|  2 | Nipride     |     146 |   152 | DRUG        |
|  3 | Haldol      |     549 |   554 | DRUG        |
|  4 | Lasix/      |     649 |   654 | DRUG        |
|  5 | Mannitol    |     656 |   663 | DRUG        |
|  6 | Nipride     |     893 |   899 | DRUG        |
|  7 | Hydralazine |     922 |   932 | DRUG        |
|  8 | Pronestyl   |     971 |   979 | DRUG        |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_drug_benchmark_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- WordEmbeddingsModel
- TextMatcherInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel

## Benchmarking

```bash

       label  precision    recall  f1-score   support
        DRUG      0.989     0.957     0.973      1373
           O      0.999     1.000     1.000     81198
    accuracy                          0.999     82571
   macro avg      0.994     0.978     0.986     82571
weighted avg      0.999     0.999     0.999     82571

```