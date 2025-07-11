---
layout: model
title: Explain Clinical Document Oncology - Light
author: John Snow Labs
name: explain_clinical_doc_oncology_light
date: 2025-06-27
tags: [licensed, en, clinical, pipeline, ner, oncology]
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

This pipeline is designed to extract oncology-related clinical/medical entities. In this pipeline, 4 NER models and 2 text matchers are used to extract the clinical entity labels.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_oncology_light_en_6.0.2_3.4_1751025747063.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_oncology_light_en_6.0.2_3.4_1751025747063.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_oncology_light", "en", "clinical/models")

result = ner_pipeline.annotate("""A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy,
 total anterior hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago.
 The patient's medical compliance was poor and failed to complete her chemotherapy (cyclophosphamide 750 mg/m2, carboplatin 300 mg/m2).
 Recently, she noted a palpable right breast mass, 15 cm in size which nearly occupied the whole right breast in 2 months.
 Core needle biopsy revealed metaplastic carcinoma.
 Neoadjuvant chemotherapy with the regimens of Taxotere (75 mg/m2), Epirubicin (75 mg/m2), and Cyclophosphamide (500 mg/m2) was given for 6 cycles with poor response,
 followed by a modified radical mastectomy (MRM) with dissection of axillary lymph nodes and skin grafting.
 Postoperatively, radiotherapy was done with 5000 cGy in 25 fractions.
 The histopathologic examination revealed a metaplastic carcinoma with squamous differentiation associated with adenomyoepithelioma.
 Immunohistochemistry study showed that the tumor cells are positive for epithelial markers-cytokeratin (AE1/AE3) stain, and myoepithelial markers, including cytokeratin 5/6 (CK 5/6), p63, and S100 stains.
 Expressions of hormone receptors, including ER, PR, and Her-2/Neu, were all negative.
 """)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_oncology_light", "en", "clinical/models")

val result = ner_pipeline.annotate("""A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy,
 total anterior hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago.
 The patient's medical compliance was poor and failed to complete her chemotherapy (cyclophosphamide 750 mg/m2, carboplatin 300 mg/m2).
 Recently, she noted a palpable right breast mass, 15 cm in size which nearly occupied the whole right breast in 2 months.
 Core needle biopsy revealed metaplastic carcinoma.
 Neoadjuvant chemotherapy with the regimens of Taxotere (75 mg/m2), Epirubicin (75 mg/m2), and Cyclophosphamide (500 mg/m2) was given for 6 cycles with poor response,
 followed by a modified radical mastectomy (MRM) with dissection of axillary lymph nodes and skin grafting.
 Postoperatively, radiotherapy was done with 5000 cGy in 25 fractions.
 The histopathologic examination revealed a metaplastic carcinoma with squamous differentiation associated with adenomyoepithelioma.
 Immunohistochemistry study showed that the tumor cells are positive for epithelial markers-cytokeratin (AE1/AE3) stain, and myoepithelial markers, including cytokeratin 5/6 (CK 5/6), p63, and S100 stains.
 Expressions of hormone receptors, including ER, PR, and Her-2/Neu, were all negative.
 """)

```
</div>

## Results

```bash
|    | chunks                                |   begin |   end | entities              |
|---:|:--------------------------------------|--------:|------:|:----------------------|
|  0 | debulking surgery                     |      37 |    53 | Cancer_Surgery        |
|  1 | bilateral oophorectomy                |      56 |    77 | Cancer_Surgery        |
|  2 | omentectomy                           |      84 |    94 | Cancer_Surgery        |
|  3 | total anterior hysterectomy           |      98 |   124 | Cancer_Surgery        |
|  4 | radical pelvic lymph nodes dissection |     131 |   167 | Cancer_Surgery        |
|  5 | ovarian carcinoma                     |     176 |   192 | Cancer_Dx             |
|  6 | mucinous-type carcinoma               |     195 |   217 | Cancer_Dx             |
|  7 | stage Ic                              |     220 |   227 | Staging               |
|  8 | 1 year ago                            |     230 |   239 | Relative_Date         |
|  9 | chemotherapy                          |     312 |   323 | Chemotherapy          |
| 10 | cyclophosphamide                      |     326 |   341 | Chemotherapy          |
| 11 | 750 mg/m2                             |     343 |   351 | Dosage                |
| 12 | carboplatin                           |     354 |   364 | Chemotherapy          |
| 13 | 300 mg/m2                             |     366 |   374 | Dosage                |
| 14 | right                                 |     410 |   414 | Direction             |
| 15 | breast                                |     416 |   421 | Site_Breast           |
| 16 | mass                                  |     423 |   426 | Tumor_Finding         |
| 17 | 15 cm                                 |     429 |   433 | Tumor_Size            |
| 18 | right                                 |     475 |   479 | Direction             |
| 19 | breast                                |     481 |   486 | Site_Breast           |
| 20 | in 2 months                           |     488 |   498 | Relative_Date         |
| 21 | Core needle biopsy                    |     502 |   519 | Pathology_Test        |
| 22 | metaplastic carcinoma                 |     530 |   550 | Cancer_Dx             |
| 23 | Neoadjuvant chemotherapy              |     554 |   577 | Chemotherapy          |
| 24 | Taxotere                              |     600 |   607 | Chemotherapy          |
| 25 | 75 mg/m2                              |     610 |   617 | Dosage                |
| 26 | Epirubicin                            |     621 |   630 | Chemotherapy          |
| 27 | 75 mg/m2                              |     633 |   640 | Dosage                |
| 28 | Cyclophosphamide                      |     648 |   663 | Chemotherapy          |
| 29 | 500 mg/m2                             |     666 |   674 | Dosage                |
| 30 | 6 cycles                              |     691 |   698 | Cycle_Count           |
| 31 | poor response                         |     705 |   717 | Response_To_Treatment |
| 32 | modified radical mastectomy           |     735 |   761 | Cancer_Surgery        |
| 33 | MRM                                   |     764 |   766 | Cancer_Surgery        |
| 34 | dissection of axillary lymph nodes    |     774 |   807 | Cancer_Surgery        |
| 35 | skin grafting                         |     813 |   825 | Cancer_Surgery        |
| 36 | radiotherapy                          |     846 |   857 | Radiotherapy          |
| 37 | 5000 cGy                              |     873 |   880 | Radiation_Dose        |
| 38 | 25 fractions                          |     885 |   896 | Cycle_Count           |
| 39 | histopathologic examination           |     904 |   930 | Pathology_Test        |
| 40 | metaplastic carcinoma                 |     943 |   963 | Cancer_Dx             |
| 41 | squamous differentiation              |     970 |   993 | Histological_Type     |
| 42 | adenomyoepithelioma                   |    1011 |  1029 | Cancer_Dx             |
| 43 | Immunohistochemistry study            |    1033 |  1058 | Pathology_Test        |
| 44 | tumor cells                           |    1076 |  1086 | Pathology_Result      |
| 45 | positive                              |    1092 |  1099 | Biomarker_Result      |
| 46 | epithelial markers-cytokeratin        |    1105 |  1134 | Biomarker             |
| 47 | AE1/AE3                               |    1137 |  1143 | Biomarker             |
| 48 | myoepithelial markers                 |    1157 |  1177 | Biomarker             |
| 49 | cytokeratin 5/6                       |    1190 |  1204 | Biomarker             |
| 50 | CK 5/6                                |    1207 |  1212 | Biomarker             |
| 51 | p63                                   |    1216 |  1218 | Biomarker             |
| 52 | S100                                  |    1225 |  1228 | Biomarker             |
| 53 | hormone receptors                     |    1254 |  1270 | Biomarker             |
| 54 | ER                                    |    1283 |  1284 | Biomarker             |
| 55 | PR                                    |    1287 |  1288 | Biomarker             |
| 56 | Her-2/Neu                             |    1295 |  1303 | Oncogene              |
| 57 | negative                              |    1315 |  1322 | Biomarker_Result      |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_oncology_light|
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
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- ChunkMergeModel