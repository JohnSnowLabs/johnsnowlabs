---
layout: model
title: Oncology Pipeline for Biomarkers
author: John Snow Labs
name: oncology_biomarker_pipeline
date: 2023-06-17
tags: [licensed, pipeline, oncology, biomarker, en]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline includes Named-Entity Recognition, Assertion Status and Relation Extraction models to extract information from oncology texts. This pipeline focuses on entities related to biomarkers.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/oncology_biomarker_pipeline_en_4.4.4_3.0_1686991190854.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/oncology_biomarker_pipeline_en_4.4.4_3.0_1686991190854.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("oncology_biomarker_pipeline", "en", "clinical/models")

text = '''Immunohistochemistry was negative for thyroid transcription factor-1 and napsin A. The test was positive for ER and PR, and negative for HER2.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("oncology_biomarker_pipeline", "en", "clinical/models")

val text = "Immunohistochemistry was negative for thyroid transcription factor-1 and napsin A. The test was positive for ER and PR, and negative for HER2."

val result = pipeline.fullAnnotate(text)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.oncology_biomarker.pipeline").predict("""Immunohistochemistry was negative for thyroid transcription factor-1 and napsin A. The test was positive for ER and PR, and negative for HER2.""")
```

</div>


## Results

```bash
******************** ner_oncology_wip results ********************

| chunk                          | ner_label        |
|:-------------------------------|:-----------------|
| negative                       | Biomarker_Result |
| thyroid transcription factor-1 | Biomarker        |
| napsin                         | Biomarker        |
| positive                       | Biomarker_Result |
| ER                             | Biomarker        |
| PR                             | Biomarker        |
| negative                       | Biomarker_Result |
| HER2                           | Oncogene         |


******************** ner_oncology_biomarker_wip results ********************

| chunk                          | ner_label        |
|:-------------------------------|:-----------------|
| negative                       | Biomarker_Result |
| thyroid transcription factor-1 | Biomarker        |
| napsin A                       | Biomarker        |
| positive                       | Biomarker_Result |
| ER                             | Biomarker        |
| PR                             | Biomarker        |
| negative                       | Biomarker_Result |
| HER2                           | Biomarker        |


******************** ner_oncology_test_wip results ********************

| chunk                          | ner_label        |
|:-------------------------------|:-----------------|
| Immunohistochemistry           | Pathology_Test   |
| negative                       | Biomarker_Result |
| thyroid transcription factor-1 | Biomarker        |
| napsin A                       | Biomarker        |
| positive                       | Biomarker_Result |
| ER                             | Biomarker        |
| PR                             | Biomarker        |
| negative                       | Biomarker_Result |
| HER2                           | Oncogene         |


******************** ner_biomarker results ********************

| chunk                          | ner_label             |
|:-------------------------------|:----------------------|
| Immunohistochemistry           | Test                  |
| negative                       | Biomarker_Measurement |
| thyroid transcription factor-1 | Biomarker             |
| napsin A                       | Biomarker             |
| positive                       | Biomarker_Measurement |
| ER                             | Biomarker             |
| PR                             | Biomarker             |
| negative                       | Biomarker_Measurement |
| HER2                           | Biomarker             |


******************** assertion_oncology_wip results ********************

| chunk                          | ner_label      | assertion   |
|:-------------------------------|:---------------|:------------|
| Immunohistochemistry           | Pathology_Test | Past        |
| thyroid transcription factor-1 | Biomarker      | Present     |
| napsin A                       | Biomarker      | Present     |
| ER                             | Biomarker      | Present     |
| PR                             | Biomarker      | Present     |
| HER2                           | Oncogene       | Present     |


******************** assertion_oncology_test_binary_wip results ********************

| chunk                          | ner_label      | assertion       |
|:-------------------------------|:---------------|:----------------|
| Immunohistochemistry           | Pathology_Test | Medical_History |
| thyroid transcription factor-1 | Biomarker      | Medical_History |
| napsin A                       | Biomarker      | Medical_History |
| ER                             | Biomarker      | Medical_History |
| PR                             | Biomarker      | Medical_History |
| HER2                           | Oncogene       | Medical_History |


******************** re_oncology_wip results ********************

| chunk1               | entity1          | chunk2                         | entity2          | relation      |
|:---------------------|:-----------------|:-------------------------------|:-----------------|:--------------|
| Immunohistochemistry | Pathology_Test   | negative                       | Biomarker_Result | O             |
| negative             | Biomarker_Result | thyroid transcription factor-1 | Biomarker        | is_related_to |
| negative             | Biomarker_Result | napsin A                       | Biomarker        | is_related_to |
| positive             | Biomarker_Result | ER                             | Biomarker        | is_related_to |
| positive             | Biomarker_Result | PR                             | Biomarker        | is_related_to |
| positive             | Biomarker_Result | HER2                           | Oncogene         | O             |
| ER                   | Biomarker        | negative                       | Biomarker_Result | O             |
| PR                   | Biomarker        | negative                       | Biomarker_Result | O             |
| negative             | Biomarker_Result | HER2                           | Oncogene         | is_related_to |


******************** re_oncology_granular_wip results ********************

| chunk1               | entity1          | chunk2                         | entity2          | relation      |
|:---------------------|:-----------------|:-------------------------------|:-----------------|:--------------|
| Immunohistochemistry | Pathology_Test   | negative                       | Biomarker_Result | O             |
| negative             | Biomarker_Result | thyroid transcription factor-1 | Biomarker        | is_finding_of |
| negative             | Biomarker_Result | napsin A                       | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | ER                             | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | PR                             | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | HER2                           | Oncogene         | is_finding_of |
| ER                   | Biomarker        | negative                       | Biomarker_Result | O             |
| PR                   | Biomarker        | negative                       | Biomarker_Result | O             |
| negative             | Biomarker_Result | HER2                           | Oncogene         | is_finding_of |


******************** re_oncology_biomarker_result_wip results ********************

| chunk1               | entity1          | chunk2                         | entity2          | relation      |
|:---------------------|:-----------------|:-------------------------------|:-----------------|:--------------|
| Immunohistochemistry | Pathology_Test   | negative                       | Biomarker_Result | is_finding_of |
| negative             | Biomarker_Result | thyroid transcription factor-1 | Biomarker        | is_finding_of |
| negative             | Biomarker_Result | napsin A                       | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | ER                             | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | PR                             | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | HER2                           | Oncogene         | O             |
| ER                   | Biomarker        | negative                       | Biomarker_Result | O             |
| PR                   | Biomarker        | negative                       | Biomarker_Result | O             |
| negative             | Biomarker_Result | HER2                           | Oncogene         | is_finding_of |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|oncology_biomarker_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
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
- ChunkMergeModel
- ChunkMergeModel
- AssertionDLModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
- RelationExtractionModel
- RelationExtractionModel