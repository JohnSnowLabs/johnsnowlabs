---
layout: model
title: Explain Clinical Document - Biomarker
author: John Snow Labs
name: explain_clinical_doc_biomarker
date: 2024-03-11
tags: [licensed, en, biomarker, pipeline, ner, relation_extraction]
task: [Named Entity Recognition, Relation Extraction, Pipeline Healthcare]
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

This pipeline designed for the precise extraction of biomarker entities from clinical documents. At its core, this pipeline integrates a rule-based TextMatcherInternal annotator with advanced MedicalNerModel annotators. This combination enables to capture biomarker-related information with high precision and reliability and then establish relations between the extracted entities from the clinical documents.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_biomarker_en_5.3.0_3.0_1710143149515.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_biomarker_en_5.3.0_3.0_1710143149515.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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