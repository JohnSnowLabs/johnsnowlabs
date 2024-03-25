---
layout: model
title: Explain Clinical Document - Risk Factors
author: John Snow Labs
name: explain_clinical_doc_risk_factors
date: 2024-03-25
tags: [licensed, en, relation_extraction, clinical, pipeline, risk_factors, ner, assertion]
task: [Pipeline Healthcare, Named Entity Recognition, Relation Extraction, Assertion Status]
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

This pipeline is designed to

- extract all clinical/medical entities, which may be considered as risk factors from text,

- assign assertion status to the extracted entities,

- establish relations between the extracted entities.

6 NER models, one assertion model and one relation extraction model were used in order to achieve those tasks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_risk_factors_en_5.3.0_3.0_1711373987295.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_risk_factors_en_5.3.0_3.0_1711373987295.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_risk_factors", "en", "clinical/models")

result = ner_pipeline.annotate("""
Barbara, a 62-year-old with a history of high blood pressure and heavy smoking for 40 years, has been experiencing chest pain radiating down her left arm, along with shortness of breath and fatigue for the past week. These symptoms, combined with her risk factors, raise concerns for coronary artery disease (CAD) and potential angina. Her doctor recommends a stress test, where she'll walk on a treadmill while monitored for changes in heart rhythm and blood flow. If the test suggests blockage, a coronary angiogram might be necessary. This minimally invasive procedure uses X-rays and contrast dye to visualize her coronary arteries and pinpoint any blockages.
Depending on the severity of the blockage, treatment options could include:
Medication management: This could involve medications for elevated blood pressure, cholesterol, and blood clots, as well as nitroglycerin to relieve angina symptoms.
Angioplasty: A procedure where a thin catheter is inserted into a blocked artery and a tiny balloon is inflated to open it. A stent, a small wire mesh tube, might be placed to keep the artery open.
Coronary artery bypass surgery (CABG): If the blockages are severe or numerous, CABG might be necessary. This open-heart surgery involves grafting healthy blood vessels from another part of the body to bypass the blocked coronary arteries.
Following diagnosis and treatment, Barbara will likely need to make significant lifestyle changes, including quitting smoking, adopting a heart-healthy diet, and increasing physical activity. Regular doctor visits and medication adherence will be crucial to manage her CAD and prevent future complications.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_risk_factors", "en", "clinical/models")

val result = ner_pipeline.annotate("""
Barbara, a 62-year-old with a history of high blood pressure and heavy smoking for 40 years, has been experiencing chest pain radiating down her left arm, along with shortness of breath and fatigue for the past week. These symptoms, combined with her risk factors, raise concerns for coronary artery disease (CAD) and potential angina. Her doctor recommends a stress test, where she'll walk on a treadmill while monitored for changes in heart rhythm and blood flow. If the test suggests blockage, a coronary angiogram might be necessary. This minimally invasive procedure uses X-rays and contrast dye to visualize her coronary arteries and pinpoint any blockages.
Depending on the severity of the blockage, treatment options could include:
Medication management: This could involve medications for elevated blood pressure, cholesterol, and blood clots, as well as nitroglycerin to relieve angina symptoms.
Angioplasty: A procedure where a thin catheter is inserted into a blocked artery and a tiny balloon is inflated to open it. A stent, a small wire mesh tube, might be placed to keep the artery open.
Coronary artery bypass surgery (CABG): If the blockages are severe or numerous, CABG might be necessary. This open-heart surgery involves grafting healthy blood vessels from another part of the body to bypass the blocked coronary arteries.
Following diagnosis and treatment, Barbara will likely need to make significant lifestyle changes, including quitting smoking, adopting a heart-healthy diet, and increasing physical activity. Regular doctor visits and medication adherence will be crucial to manage her CAD and prevent future complications.
""")

```
</div>

## Results

```bash
|    | chunks                         |   begin |   end | entities                  |
|---:|:-------------------------------|--------:|------:|:--------------------------|
|  0 | high blood pressure            |      41 |    59 | Hypertension              |
|  1 | smoking                        |      71 |    77 | Smoking                   |
|  2 | chest pain                     |     115 |   124 | Symptom                   |
|  3 | shortness of breath            |     166 |   184 | Symptom                   |
|  4 | fatigue                        |     190 |   196 | Symptom                   |
|  5 | coronary artery disease        |     284 |   306 | Heart_Disease             |
|  6 | CAD                            |     309 |   311 | Heart_Disease             |
|  7 | angina                         |     328 |   333 | Heart_Disease             |
|  8 | stress                         |     360 |   365 | Mental_Health             |
|  9 | coronary arteries              |     618 |   634 | Disease_Syndrome_Disorder |
| 10 | elevated blood pressure        |     798 |   820 | Hypertension              |
| 11 | cholesterol                    |     823 |   833 | Disease_Syndrome_Disorder |
| 12 | blood clots                    |     840 |   850 | Disease_Syndrome_Disorder |
| 13 | nitroglycerin                  |     864 |   876 | DRUG                      |
| 14 | angina                         |     889 |   894 | Disease_Syndrome_Disorder |
| 15 | Angioplasty                    |     906 |   916 | Procedure                 |
| 16 | blocked artery                 |     972 |   985 | Disease_Syndrome_Disorder |
| 17 | Coronary artery bypass surgery |    1104 |  1133 | Procedure                 |
| 18 | CABG                           |    1136 |  1139 | Procedure                 |
| 19 | CABG                           |    1184 |  1187 | Procedure                 |
| 20 | open-heart surgery             |    1214 |  1231 | Procedure                 |
| 21 | grafting                       |    1242 |  1249 | Procedure                 |
| 22 | bypass                         |    1306 |  1311 | Procedure                 |
| 23 | coronary arteries              |    1325 |  1341 | Disease_Syndrome_Disorder |
| 24 | smoking                        |    1462 |  1468 | Smoking                   |
| 25 | heart-healthy diet             |    1482 |  1499 | Diet                      |
| 26 | physical activity              |    1517 |  1533 | Exercise                  |
| 27 | CAD                            |    1613 |  1615 | Heart_Disease             |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_risk_factors|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
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
- ChunkMergeModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- GenericREModel