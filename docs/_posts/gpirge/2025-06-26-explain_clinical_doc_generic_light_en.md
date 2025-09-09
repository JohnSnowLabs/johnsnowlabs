---
layout: model
title: Explain Clinical Document Generic - Light
author: John Snow Labs
name: explain_clinical_doc_generic_light
date: 2025-06-26
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

This pipeline is designed to extract clinical/medical entities. In this pipeline, 4 NER models are used to extract these Clinical Entity Labels: PROBLEM, TEST, TREATMENT

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_generic_light_en_6.0.2_3.4_1750957688424.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_generic_light_en_6.0.2_3.4_1750957688424.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_generic_light", "en", "clinical/models")

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

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_generic_light", "en", "clinical/models")

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
|    | chunks                                |   begin |   end | entities       |
|---:|:--------------------------------------|--------:|------:|:---------------|
|  0 | debulking surgery                     |      37 |    53 | TREATMENT      |
|  1 | bilateral oophorectomy                |      56 |    77 | CANCER_SURGERY |
|  2 | omentectomy                           |      84 |    94 | TREATMENT      |
|  3 | total anterior hysterectomy           |      98 |   124 | TREATMENT      |
|  4 | radical pelvic lymph nodes dissection |     131 |   167 | TREATMENT      |
|  5 | ovarian carcinoma                     |     176 |   192 | PROBLEM        |
|  6 | mucinous-type carcinoma               |     195 |   217 | PROBLEM        |
|  7 | stage Ic                              |     220 |   227 | PROBLEM        |
|  8 | her chemotherapy                      |     308 |   323 | TREATMENT      |
|  9 | cyclophosphamide                      |     326 |   341 | TREATMENT      |
| 10 | carboplatin                           |     354 |   364 | TREATMENT      |
| 11 | a palpable right breast mass          |     400 |   427 | PROBLEM        |
| 12 | Core needle biopsy                    |     504 |   521 | TREATMENT      |
| 13 | metaplastic carcinoma                 |     532 |   552 | PROBLEM        |
| 14 | Neoadjuvant chemotherapy              |     557 |   580 | TREATMENT      |
| 15 | the regimens                          |     587 |   598 | TREATMENT      |
| 16 | Taxotere                              |     603 |   610 | TREATMENT      |
| 17 | Epirubicin                            |     624 |   633 | TREATMENT      |
| 18 | Cyclophosphamide                      |     651 |   666 | TREATMENT      |
| 19 | poor response                         |     708 |   720 | PROBLEM        |
| 20 | a modified radical mastectomy         |     737 |   765 | TREATMENT      |
| 21 | MRM                                   |     768 |   770 | TEST           |
| 22 | dissection of axillary lymph nodes    |     778 |   811 | TREATMENT      |
| 23 | skin grafting                         |     817 |   829 | TREATMENT      |
| 24 | radiotherapy                          |     851 |   862 | TREATMENT      |
| 25 | The histopathologic examination       |     906 |   936 | TEST           |
| 26 | a metaplastic carcinoma               |     947 |   969 | PROBLEM        |
| 27 | squamous differentiation              |     976 |   999 | PROBLEM        |
| 28 | adenomyoepithelioma                   |    1017 |  1035 | PROBLEM        |
| 29 | Immunohistochemistry study            |    1040 |  1065 | TEST           |
| 30 | the tumor cells                       |    1079 |  1093 | PROBLEM        |
| 31 | epithelial markers-cytokeratin        |    1112 |  1141 | PROBLEM        |
| 32 | AE1/AE3                               |    1144 |  1150 | TEST           |
| 33 | stain                                 |    1153 |  1157 | TEST           |
| 34 | myoepithelial markers                 |    1164 |  1184 | TEST           |
| 35 | cytokeratin                           |    1197 |  1207 | TEST           |
| 36 | CK                                    |    1214 |  1215 | TEST           |
| 37 | p63                                   |    1223 |  1225 | TEST           |
| 38 | S100 stains                           |    1232 |  1242 | TEST           |
| 39 | hormone receptors                     |    1261 |  1277 | TEST           |
| 40 | ER                                    |    1290 |  1291 | TEST           |
| 41 | PR                                    |    1294 |  1295 | TEST           |
| 42 | Her-2/Neu                             |    1302 |  1310 | TEST           |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_generic_light|
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
- ChunkMergeModel