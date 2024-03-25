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
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to:

- extract all clinical/medical entities, which may be considered as risk factors from text,

- assign assertion status to the extracted entities,

- establish relations between the extracted entities.

6 NER models, one assertion model and one relation extraction model were used in order to achieve those tasks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_risk_factors_en_5.3.0_3.2_1711386508334.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_risk_factors_en_5.3.0_3.2_1711386508334.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

  ```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_risk_factors", "en", "clinical/models")

result = ner_pipeline.annotate("""
Barbara, a 62-year-old with a history of high blood pressure for 40 years, experiencing chest pain radiating down her left arm. These symptoms, combined with her risk factors, raise concerns for coronary artery disease (CAD) and potential angina. Her doctor recommends a Cardiopulmonary exercise test, where she'll walk on a treadmill while monitored for changes in heart rhythm and blood flow. If the test suggests atherosclerotic plaque buildup, a coronary angiogram might be necessary. This minimally invasive procedure uses X-rays and contrast dye to pinpoint any Atherosclerotic plaque buildup.
Depending on the severity of the blockage, treatment options could include:
Medication management: This could involve medications for elevated blood pressure, cholesterol, and blood clots, as well as nitroglycerin to relieve angina symptoms.
Angioplasty can be considered as a procedure where a thin catheter is inserted into a blocked artery and a tiny balloon is inflated to open it. A stent, a small wire mesh tube, might be placed to keep the artery open.
Coronary artery bypass surgery (CABG): If the blockages are severe or numerous, CABG might be necessary. This open-heart surgery involves grafting healthy blood vessels from another part of the body to bypass the blocked coronary arteries.
Following diagnosis and treatment, Barbara will likely need to make significant lifestyle changes, including quitting smoking, adopting a heart-healthy diet, and increasing physical activity. Regular doctor visits and medication adherence will be crucial to manage her CAD and prevent future complications.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_risk_factors", "en", "clinical/models")

val result = ner_pipeline.annotate("""
Barbara, a 62-year-old with a history of high blood pressure for 40 years, experiencing chest pain radiating down her left arm. These symptoms, combined with her risk factors, raise concerns for coronary artery disease (CAD) and potential angina. Her doctor recommends a Cardiopulmonary exercise test, where she'll walk on a treadmill while monitored for changes in heart rhythm and blood flow. If the test suggests atherosclerotic plaque buildup, a coronary angiogram might be necessary. This minimally invasive procedure uses X-rays and contrast dye to pinpoint any Atherosclerotic plaque buildup.
Depending on the severity of the blockage, treatment options could include:
Medication management: This could involve medications for elevated blood pressure, cholesterol, and blood clots, as well as nitroglycerin to relieve angina symptoms.
Angioplasty can be considered as a procedure where a thin catheter is inserted into a blocked artery and a tiny balloon is inflated to open it. A stent, a small wire mesh tube, might be placed to keep the artery open.
Coronary artery bypass surgery (CABG): If the blockages are severe or numerous, CABG might be necessary. This open-heart surgery involves grafting healthy blood vessels from another part of the body to bypass the blocked coronary arteries.
Following diagnosis and treatment, Barbara will likely need to make significant lifestyle changes, including quitting smoking, adopting a heart-healthy diet, and increasing physical activity. Regular doctor visits and medication adherence will be crucial to manage her CAD and prevent future complications.
""")

```
</div>

## NER Results

```bash
|    | chunks                         |   begin |   end | entities                  |
|---:|:-------------------------------|--------:|------:|:--------------------------|
|  0 | high blood pressure            |      41 |    59 | Hypertension              |
|  1 | chest pain                     |      88 |    97 | Symptom                   |
|  2 | coronary artery disease        |     195 |   217 | Heart_Disease             |
|  3 | CAD                            |     220 |   222 | Heart_Disease             |
|  4 | angina                         |     239 |   244 | Heart_Disease             |
|  5 | exercise                       |     287 |   294 | Exercise                  |
|  6 | atherosclerotic plaque         |     416 |   437 | Disease_Syndrome_Disorder |
|  7 | Atherosclerotic plaque         |     568 |   589 | Disease_Syndrome_Disorder |
|  8 | elevated blood pressure        |     734 |   756 | Hypertension              |
|  9 | cholesterol                    |     759 |   769 | Disease_Syndrome_Disorder |
| 10 | blood clots                    |     776 |   786 | Disease_Syndrome_Disorder |
| 11 | nitroglycerin                  |     800 |   812 | DRUG                      |
| 12 | angina                         |     825 |   830 | Disease_Syndrome_Disorder |
| 13 | Angioplasty                    |     842 |   852 | Procedure                 |
| 14 | blocked artery                 |     928 |   941 | Disease_Syndrome_Disorder |
| 15 | Coronary artery bypass surgery |    1060 |  1089 | Procedure                 |
| 16 | CABG                           |    1092 |  1095 | Procedure                 |
| 17 | CABG                           |    1140 |  1143 | Procedure                 |
| 18 | open-heart surgery             |    1170 |  1187 | Procedure                 |
| 19 | grafting                       |    1198 |  1205 | Procedure                 |
| 20 | bypass                         |    1262 |  1267 | Procedure                 |
| 21 | coronary arteries              |    1281 |  1297 | Disease_Syndrome_Disorder |
| 22 | smoking                        |    1418 |  1424 | Smoking                   |
| 23 | heart-healthy diet             |    1438 |  1455 | Diet                      |
| 24 | physical activity              |    1473 |  1489 | Exercise                  |
| 25 | CAD                            |    1569 |  1571 | Heart_Disease             |

# Assertion Status Results

|    | chunks                         | entities                  | assertion    |
|---:|:-------------------------------|:--------------------------|:-------------|
|  0 | high blood pressure            | Hypertension              | Present      |
|  1 | chest pain                     | Symptom                   | Hypothetical |
|  2 | coronary artery disease        | Heart_Disease             | Possible     |
|  3 | CAD                            | Heart_Disease             | Possible     |
|  4 | angina                         | Heart_Disease             | Possible     |
|  5 | atherosclerotic plaque         | Disease_Syndrome_Disorder | Possible     |
|  6 | Atherosclerotic plaque         | Disease_Syndrome_Disorder | Hypothetical |
|  7 | elevated blood pressure        | Hypertension              | Hypothetical |
|  8 | cholesterol                    | Disease_Syndrome_Disorder | Planned      |
|  9 | blood clots                    | Disease_Syndrome_Disorder | Planned      |
| 10 | angina                         | Disease_Syndrome_Disorder | Hypothetical |
| 11 | Angioplasty                    | Procedure                 | Hypothetical |
| 12 | blocked artery                 | Disease_Syndrome_Disorder | Past         |
| 13 | Coronary artery bypass surgery | Procedure                 | Past         |
| 14 | CABG                           | Procedure                 | Past         |
| 15 | CABG                           | Procedure                 | Hypothetical |
| 16 | open-heart surgery             | Procedure                 | Past         |
| 17 | grafting                       | Procedure                 | Past         |
| 18 | bypass                         | Procedure                 | Past         |
| 19 | coronary arteries              | Disease_Syndrome_Disorder | Hypothetical |
| 20 | smoking                        | Substance_Use_Disorder    | Hypothetical |
| 21 | CAD                            | Heart_Disease             | Hypothetical |

# Relation Extraction Results



|    |   sentence |   entity1_begin |   entity1_end | chunk1                  | entity1                   |   entity2_begin |   entity2_end | chunk2            | entity2                   | relation                            |   confidence |
|---:|-----------:|----------------:|--------------:|:------------------------|:--------------------------|----------------:|--------------:|:------------------|:--------------------------|:------------------------------------|-------------:|
|  0 |          6 |             734 |           756 | elevated blood pressure | Hypertension              |             800 |           812 | nitroglycerin     | DRUG                      | Hypertension-DRUG                   |            1 |
|  1 |          6 |             759 |           769 | cholesterol             | Disease_Syndrome_Disorder |             800 |           812 | nitroglycerin     | DRUG                      | Disease_Syndrome_Disorder-DRUG      |            1 |
|  2 |          6 |             776 |           786 | blood clots             | Disease_Syndrome_Disorder |             800 |           812 | nitroglycerin     | DRUG                      | Disease_Syndrome_Disorder-DRUG      |            1 |
|  3 |          6 |             800 |           812 | nitroglycerin           | DRUG                      |             825 |           830 | angina            | Disease_Syndrome_Disorder | DRUG-Disease_Syndrome_Disorder      |            1 |
|  4 |         10 |            1262 |          1267 | bypass                  | Procedure                 |            1281 |          1297 | coronary arteries | Disease_Syndrome_Disorder | Procedure-Disease_Syndrome_Disorder |            1 |

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
