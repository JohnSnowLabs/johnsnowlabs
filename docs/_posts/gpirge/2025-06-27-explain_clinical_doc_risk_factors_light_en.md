---
layout: model
title: Explain Clinical Document Risk Factors - Light
author: John Snow Labs
name: explain_clinical_doc_risk_factors_light
date: 2025-06-27
tags: [licensed, en, clinical, pipeline, ner, risk_factors]
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

This pipeline is designed to extract entities that may be considered as risk factors from text. 

In this pipeline, 3 NER models and 2 text matchers are used to extract the related clinical/medical entity labels.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_risk_factors_light_en_6.0.2_3.4_1751052010831.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_risk_factors_light_en_6.0.2_3.4_1751052010831.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_risk_factors_light", "en", "clinical/models")

result = ner_pipeline.annotate("""A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy,
 total anterior hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago.
 The patient's medical compliance was poor and failed to complete her chemotherapy (cyclophosphamide 750 mg/m2, carboplatin 300 mg/m2).
 Recently, she noted a palpable right breast mass, 15 cm in size which nearly occupied the whole right breast in 2 months.
 Core needle biopsy revealed metaplastic carcinoma.
 Neoadjuvant chemotherapy with the regimens of Taxotere (75 mg/m2), Epirubicin (75 mg/m2), and Cyclophosphamide (500 mg/m2) was given for 6 cycles with poor response,
 followed by a modified radical mastectomy (MRM) with dissection of axillary lymph nodes and skin grafting.
 Postoperatively, radiotherapy was done with 5000 cGy in 25 fractions.
 The histopathologic examination revealed a metaplastic carcinoma with squamous differentiation associated with adenomyoepithelioma.
In response, his doctor prescribed a regimen tailored to his conditions:
Thiamine 100 mg q.day , Folic acid 1 mg q.day , multivitamins q.day , Calcium carbonate plus Vitamin D 250 mg t.i.d. , Heparin 5000 units subcutaneously b.i.d. , Prilosec 20 mg q.day , Senna two tabs qhs.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_risk_factors_light", "en", "clinical/models")

val result = ner_pipeline.annotate("""A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy,
 total anterior hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago.
 The patient's medical compliance was poor and failed to complete her chemotherapy (cyclophosphamide 750 mg/m2, carboplatin 300 mg/m2).
 Recently, she noted a palpable right breast mass, 15 cm in size which nearly occupied the whole right breast in 2 months.
 Core needle biopsy revealed metaplastic carcinoma.
 Neoadjuvant chemotherapy with the regimens of Taxotere (75 mg/m2), Epirubicin (75 mg/m2), and Cyclophosphamide (500 mg/m2) was given for 6 cycles with poor response,
 followed by a modified radical mastectomy (MRM) with dissection of axillary lymph nodes and skin grafting.
 Postoperatively, radiotherapy was done with 5000 cGy in 25 fractions.
 The histopathologic examination revealed a metaplastic carcinoma with squamous differentiation associated with adenomyoepithelioma.
In response, his doctor prescribed a regimen tailored to his conditions:
Thiamine 100 mg q.day , Folic acid 1 mg q.day , multivitamins q.day , Calcium carbonate plus Vitamin D 250 mg t.i.d. , Heparin 5000 units subcutaneously b.i.d. , Prilosec 20 mg q.day , Senna two tabs qhs.
""")

```
</div>

## Results

```bash
|    | chunks                                |   begin |   end | entities                  |
|---:|:--------------------------------------|--------:|------:|:--------------------------|
|  0 | debulking surgery                     |      37 |    53 | Procedure                 |
|  1 | bilateral oophorectomy                |      56 |    77 | Cancer_Surgery            |
|  2 | omentectomy                           |      84 |    94 | Procedure                 |
|  3 | total anterior hysterectomy           |      98 |   124 | Procedure                 |
|  4 | radical pelvic lymph nodes dissection |     131 |   167 | Procedure                 |
|  5 | ovarian carcinoma                     |     176 |   192 | Cancer_dx                 |
|  6 | mucinous-type carcinoma               |     195 |   217 | Disease_Syndrome_Disorder |
|  7 | chemotherapy                          |     312 |   323 | Chemotherapy              |
|  8 | cyclophosphamide                      |     326 |   341 | Chemotherapy              |
|  9 | carboplatin                           |     354 |   364 | Chemotherapy              |
| 10 | breast mass                           |     416 |   426 | Disease_Syndrome_Disorder |
| 11 | 15 cm                                 |     429 |   433 | Tumor_Size                |
| 12 | Core needle biopsy                    |     502 |   519 | Procedure                 |
| 13 | metaplastic carcinoma                 |     530 |   550 | Disease_Syndrome_Disorder |
| 14 | Neoadjuvant chemotherapy              |     554 |   577 | Chemotherapy              |
| 15 | Taxotere                              |     600 |   607 | Chemotherapy              |
| 16 | Epirubicin                            |     621 |   630 | Chemotherapy              |
| 17 | Cyclophosphamide                      |     648 |   663 | Chemotherapy              |
| 18 | modified radical mastectomy           |     735 |   761 | Procedure                 |
| 19 | MRM                                   |     764 |   766 | Cancer_Surgery            |
| 20 | dissection of axillary lymph nodes    |     774 |   807 | Procedure                 |
| 21 | skin grafting                         |     813 |   825 | Procedure                 |
| 22 | radiotherapy                          |     846 |   857 | Radiotherapy              |
| 23 | metaplastic carcinoma                 |     943 |   963 | Disease_Syndrome_Disorder |
| 24 | squamous differentiation              |     970 |   993 | Disease_Syndrome_Disorder |
| 25 | adenomyoepithelioma                   |    1011 |  1029 | Cancer_dx                 |
| 26 | Thiamine 100 mg                       |    1105 |  1119 | DRUG                      |
| 27 | Folic acid                            |    1129 |  1138 | Disease_Syndrome_Disorder |
| 28 | Calcium carbonate                     |    1175 |  1191 | DRUG                      |
| 29 | Heparin                               |    1224 |  1230 | DRUG                      |
| 30 | Prilosec 20 mg                        |    1267 |  1280 | DRUG                      |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_risk_factors_light|
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
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel