---
layout: model
title: Explain Clinical Document - Biomarker
author: John Snow Labs
name: explain_clinical_doc_biomarker
date: 2024-03-11
tags: [licensed, en, biomarker, pipeline, ner, relation_extraction]
task: [Named Entity Recognition, Relation Extraction, Text Classification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline designed for the precise extraction of biomarker entities from clinical documents. At its core, this pipeline integrates a rule-based TextMatcherInternal annotator with advanced MedicalNerModel annotators. This combination enables to capture biomarker-related information with high precision and reliability and then establish relations between the extracted entities from the clinical documents.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_biomarker_en_5.3.0_3.4_1710145606821.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_biomarker_en_5.3.0_3.4_1710145606821.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

biomarker_pipeline = PretrainedPipeline("explain_clinical_doc_biomarker", "en", "clinical/models")

result = biomarker_pipeline.annotate("""In the bone- marrow (BM) aspiration, blasts accounted for 88.1% of ANCs, which were positive for CD9 and CD10 on flow cytometry. Measurements of serum tumor markers showed elevated level of Cyfra21-1: 4.77 ng/mL, NSE: 19.60 ng/mL, and SCCA: 2.58 ng/mL. Immunohistochemical staining showed positive staining for CK5/6, P40, and negative staining for TTF-1 and weakly positive staining for ALK.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val biomarker_pipeline = PretrainedPipeline("explain_clinical_doc_biomarker", "en", "clinical/models")

val result = biomarker_pipeline.annotate("""In the bone- marrow (BM) aspiration, blasts accounted for 88.1% of ANCs, which were positive for CD9 and CD10 on flow cytometry. Measurements of serum tumor markers showed elevated level of Cyfra21-1: 4.77 ng/mL, NSE: 19.60 ng/mL, and SCCA: 2.58 ng/mL. Immunohistochemical staining showed positive staining for CK5/6, P40, and negative staining for TTF-1 and weakly positive staining for ALK.""")

```
</div>

## Results

```bash

# NER Result
+------------------------+-----+---+----------------+
|chunk                   |begin|end|label           |
+------------------------+-----+---+----------------+
|positive                |84   |91 |Biomarker_Result|
|CD9                     |97   |99 |Biomarker       |
|CD10                    |105  |108|Biomarker       |
|tumor markers           |151  |163|Biomarker       |
|elevated level          |172  |185|Biomarker_Result|
|Cyfra21-1               |190  |198|Biomarker       |
|4.77 ng/mL              |201  |210|Biomarker_Result|
|NSE                     |213  |215|Biomarker       |
|19.60 ng/mL             |218  |228|Biomarker_Result|
|SCCA                    |235  |238|Biomarker       |
|2.58 ng/mL              |241  |250|Biomarker_Result|
|positive                |289  |296|Biomarker_Result|
|CK5/6                   |311  |315|Biomarker       |
|P40                     |318  |320|Biomarker       |
|negative                |327  |334|Biomarker_Result|
|TTF-1                   |349  |353|Biomarker       |
|weakly positive staining|359  |382|Biomarker_Result|
|ALK                     |388  |390|Biomarker       |
+------------------------+-----+---+----------------+

# RE Result
|    |   sentence |   entity1_begin |   entity1_end | chunk1                   | entity1          |   entity2_begin |   entity2_end | chunk2         | entity2          | relation      |   confidence |
|---:|-----------:|----------------:|--------------:|:-------------------------|:-----------------|----------------:|--------------:|:---------------|:-----------------|:--------------|-------------:|
|  0 |          0 |              84 |            91 | positive                 | Biomarker_Result |              97 |            99 | CD9            | Biomarker        | is_finding_of |     0.993281 |
|  1 |          0 |              84 |            91 | positive                 | Biomarker_Result |             105 |           108 | CD10           | Biomarker        | is_finding_of |     0.998891 |
|  2 |          1 |             151 |           163 | tumor markers            | Biomarker        |             172 |           185 | elevated level | Biomarker_Result | is_finding_of |     0.900508 |
|  6 |          1 |             172 |           185 | elevated level           | Biomarker_Result |             190 |           198 | Cyfra21-1      | Biomarker        | is_finding_of |     0.995038 |
|  9 |          1 |             190 |           198 | Cyfra21-1                | Biomarker        |             201 |           210 | 4.77 ng/mL     | Biomarker_Result | is_finding_of |     0.981873 |
| 10 |          1 |             190 |           198 | Cyfra21-1                | Biomarker        |             218 |           228 | 19.60 ng/mL    | Biomarker_Result | is_finding_of |     0.541739 |
| 14 |          1 |             213 |           215 | NSE                      | Biomarker        |             218 |           228 | 19.60 ng/mL    | Biomarker_Result | is_finding_of |     0.988173 |
| 17 |          1 |             235 |           238 | SCCA                     | Biomarker        |             241 |           250 | 2.58 ng/mL     | Biomarker_Result | is_finding_of |     0.995757 |
| 18 |          2 |             289 |           296 | positive                 | Biomarker_Result |             311 |           315 | CK5/6          | Biomarker        | is_finding_of |     0.866368 |
| 19 |          2 |             289 |           296 | positive                 | Biomarker_Result |             318 |           320 | P40            | Biomarker        | is_finding_of |     0.895999 |
| 26 |          2 |             327 |           334 | negative                 | Biomarker_Result |             349 |           353 | TTF-1          | Biomarker        | is_finding_of |     0.994164 |
| 29 |          2 |             359 |           382 | weakly positive staining | Biomarker_Result |             388 |           390 | ALK            | Biomarker        | is_finding_of |     0.988431 |

# Classification Result
+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+-----+
|sentence_ID|                                                                                                                                   sentence|class|
+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+-----+
|          0|           In the bone- marrow (BM) aspiration, blasts accounted for 88.1% of ANCs, which were positive for CD9 and CD10 on flow cytometry.|    1|
|          1|                Measurements of serum tumor markers showed elevated level of Cyfra21-1: 4.77 ng/mL, NSE: 19.60 ng/mL, and SCCA: 2.58 ng/mL.|    1|
|          2|Immunohistochemical staining showed positive staining for CK5/6, P40, and negative staining for TTF-1 and weakly positive staining for ALK.|    1|
+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+-----+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_biomarker|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalBertForSequenceClassification
- TextMatcherInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
