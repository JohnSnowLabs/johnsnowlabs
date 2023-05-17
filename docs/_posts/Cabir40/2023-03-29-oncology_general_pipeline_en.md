---
layout: model
title: General Oncology Pipeline
author: John Snow Labs
name: oncology_general_pipeline
date: 2023-03-29
tags: [licensed, pipeline, oncology, en]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline includes Named-Entity Recognition, Assertion Status and Relation Extraction models to extract information from oncology texts. This pipeline extracts diagnoses, treatments, tests, anatomical references and demographic entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/oncology_general_pipeline_en_4.3.2_3.2_1680110018146.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/oncology_general_pipeline_en_4.3.2_3.2_1680110018146.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("oncology_general_pipeline", "en", "clinical/models")

text = '''The patient underwent a left mastectomy for a left breast cancer two months ago.
The tumor is positive for ER and PR.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("oncology_general_pipeline", "en", "clinical/models")

val text = "The patient underwent a left mastectomy for a left breast cancer two months ago.
The tumor is positive for ER and PR."

val result = pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
"
******************** ner_oncology_wip results ********************

| chunk          | ner_label        |
|:---------------|:-----------------|
| left           | Direction        |
| mastectomy     | Cancer_Surgery   |
| left           | Direction        |
| breast cancer  | Cancer_Dx        |
| two months ago | Relative_Date    |
| tumor          | Tumor_Finding    |
| positive       | Biomarker_Result |
| ER             | Biomarker        |
| PR             | Biomarker        |


******************** ner_oncology_diagnosis_wip results ********************

| chunk         | ner_label     |
|:--------------|:--------------|
| breast cancer | Cancer_Dx     |
| tumor         | Tumor_Finding |


******************** ner_oncology_tnm_wip results ********************

| chunk         | ner_label   |
|:--------------|:------------|
| breast cancer | Cancer_Dx   |
| tumor         | Tumor       |


******************** ner_oncology_therapy_wip results ********************

| chunk      | ner_label      |
|:-----------|:---------------|
| mastectomy | Cancer_Surgery |


******************** ner_oncology_test_wip results ********************

| chunk    | ner_label        |
|:---------|:-----------------|
| positive | Biomarker_Result |
| ER       | Biomarker        |
| PR       | Biomarker        |


******************** assertion_oncology_wip results ********************

| chunk         | ner_label      | assertion   |
|:--------------|:---------------|:------------|
| mastectomy    | Cancer_Surgery | Past        |
| breast cancer | Cancer_Dx      | Present     |
| tumor         | Tumor_Finding  | Present     |
| ER            | Biomarker      | Present     |
| PR            | Biomarker      | Present     |


******************** re_oncology_wip results ********************

| chunk1        | entity1          | chunk2         | entity2       | relation      |
|:--------------|:-----------------|:---------------|:--------------|:--------------|
| mastectomy    | Cancer_Surgery   | two months ago | Relative_Date | is_related_to |
| breast cancer | Cancer_Dx        | two months ago | Relative_Date | is_related_to |
| tumor         | Tumor_Finding    | ER             | Biomarker     | O             |
| tumor         | Tumor_Finding    | PR             | Biomarker     | O             |
| positive      | Biomarker_Result | ER             | Biomarker     | is_related_to |
| positive      | Biomarker_Result | PR             | Biomarker     | is_related_to |


******************** re_oncology_granular_wip results ********************

| chunk1        | entity1          | chunk2         | entity2       | relation      |
|:--------------|:-----------------|:---------------|:--------------|:--------------|
| mastectomy    | Cancer_Surgery   | two months ago | Relative_Date | is_date_of    |
| breast cancer | Cancer_Dx        | two months ago | Relative_Date | is_date_of    |
| tumor         | Tumor_Finding    | ER             | Biomarker     | O             |
| tumor         | Tumor_Finding    | PR             | Biomarker     | O             |
| positive      | Biomarker_Result | ER             | Biomarker     | is_finding_of |
| positive      | Biomarker_Result | PR             | Biomarker     | is_finding_of |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|oncology_general_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.3.2+|
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
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- ChunkMergeModel
- ChunkMergeModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
- RelationExtractionModel