---
layout: model
title: Explain Clinical Document Biomarker - Light
author: John Snow Labs
name: explain_clinical_doc_biomarker_light
date: 2025-06-27
tags: [licensed, en, clinical, pipeline, ner, biomarker]
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

This pipeline is designed to extract biomarker related entities from text. In this pipeline, 3 NER models and a text matcher are used to extract the biomarkers and their results.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_biomarker_light_en_6.0.2_3.4_1751029808447.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_biomarker_light_en_6.0.2_3.4_1751029808447.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_biomarker_light", "en", "clinical/models")

result = ner_pipeline.annotate("""Immunohistochemistry study showed that the tumor cells are positive for epithelial markers-cytokeratin (AE1/AE3) stain, and myoepithelial markers, including cytokeratin 5/6 (CK 5/6), p63, and S100 stains.
 Expressions of hormone receptors, including ER, PR, and Her-2/Neu, were all negative.
 In the bone- marrow (BM) aspiration, blasts accounted for 88.1% of ANCs, which were positive for CD9 and CD10 on flow cytometry. 
 Measurements of serum tumor markers showed elevated level of Cyfra21-1: 4.77 ng/mL, NSE: 19.60 ng/mL, and SCCA: 2.58 ng/mL. 
 Immunohistochemical staining showed positive staining for CK5/6, P40, and negative staining for TTF-1 and weakly positive staining for ALK.
 """)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_biomarker_light", "en", "clinical/models")

val result = ner_pipeline.annotate("""Immunohistochemistry study showed that the tumor cells are positive for epithelial markers-cytokeratin (AE1/AE3) stain, and myoepithelial markers, including cytokeratin 5/6 (CK 5/6), p63, and S100 stains.
 Expressions of hormone receptors, including ER, PR, and Her-2/Neu, were all negative.
 In the bone- marrow (BM) aspiration, blasts accounted for 88.1% of ANCs, which were positive for CD9 and CD10 on flow cytometry. 
 Measurements of serum tumor markers showed elevated level of Cyfra21-1: 4.77 ng/mL, NSE: 19.60 ng/mL, and SCCA: 2.58 ng/mL. 
 Immunohistochemical staining showed positive staining for CK5/6, P40, and negative staining for TTF-1 and weakly positive staining for ALK.
 """)

```
</div>

## Results

```bash
|    | chunks                         |   begin |   end | entities         |
|---:|:-------------------------------|--------:|------:|:-----------------|
|  0 | positive                       |      59 |    66 | Biomarker_Result |
|  1 | epithelial markers-cytokeratin |      72 |   101 | Biomarker        |
|  2 | AE1/AE3                        |     104 |   110 | Biomarker        |
|  3 | myoepithelial markers          |     124 |   144 | Biomarker        |
|  4 | cytokeratin 5/6                |     157 |   171 | Biomarker        |
|  5 | CK 5/6                         |     174 |   179 | Biomarker        |
|  6 | p63                            |     183 |   185 | Biomarker        |
|  7 | S100                           |     192 |   195 | Biomarker        |
|  8 | hormone receptors              |     221 |   237 | Biomarker        |
|  9 | ER                             |     250 |   251 | Biomarker        |
| 10 | PR                             |     254 |   255 | Biomarker        |
| 11 | Her-2/Neu                      |     262 |   270 | Biomarker        |
| 12 | negative                       |     282 |   289 | Biomarker_Result |
| 13 | positive                       |     377 |   384 | Biomarker_Result |
| 14 | CD9                            |     390 |   392 | Biomarker        |
| 15 | CD10                           |     398 |   401 | Biomarker        |
| 16 | tumor markers                  |     446 |   458 | Biomarker        |
| 17 | elevated level                 |     467 |   480 | Biomarker_Result |
| 18 | Cyfra21-1                      |     485 |   493 | Biomarker        |
| 19 | 4.77 ng/mL                     |     496 |   505 | Biomarker_Result |
| 20 | NSE                            |     508 |   510 | Biomarker        |
| 21 | 19.60 ng/mL                    |     513 |   523 | Biomarker_Result |
| 22 | SCCA                           |     530 |   533 | Biomarker        |
| 23 | 2.58 ng/mL                     |     536 |   545 | Biomarker_Result |
| 24 | positive staining              |     586 |   602 | Biomarker_Result |
| 25 | CK5/6                          |     608 |   612 | Biomarker        |
| 26 | P40                            |     615 |   617 | Biomarker        |
| 27 | negative staining              |     624 |   640 | Biomarker_Result |
| 28 | TTF-1                          |     646 |   650 | Biomarker        |
| 29 | weakly positive staining       |     656 |   679 | Biomarker_Result |
| 30 | ALK                            |     685 |   687 | Biomarker        |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_biomarker_light|
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
- TextMatcherInternalModel
- ChunkMergeModel