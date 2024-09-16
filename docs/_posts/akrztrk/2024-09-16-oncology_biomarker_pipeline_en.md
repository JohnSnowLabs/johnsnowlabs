---
layout: model
title: Oncology Pipeline for Biomarkers
author: John Snow Labs
name: oncology_biomarker_pipeline
date: 2024-09-16
tags: [licensed, en, oncology, biomarker, pipeline]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline includes Named-Entity Recognition, Assertion Status and Relation Extraction models to extract information from oncology texts. This pipeline focuses on entities related to biomarkers.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/oncology_biomarker_pipeline_en_5.4.1_3.2_1726507679804.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/oncology_biomarker_pipeline_en_5.4.1_3.2_1726507679804.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("oncology_biomarker_pipeline", "en", "clinical/models")

result = pipeline.fullAnnotate("""Immunohistochemistry was negative for thyroid transcription factor-1 and napsin A. The test was positive for ER and PR,
and negative for HER2.""")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("oncology_biomarker_pipeline", "en", "clinical/models")

val result = pipeline.fullAnnotate("""Immunohistochemistry was negative for thyroid transcription factor-1 and napsin A. The test was positive for ER and PR,
and negative for HER2.""")
```
</div>

## Results

```bash
******************** ner_biomarker results ********************

| chunk                          |   begin |   end | ner_label             |   confidence |
|:-------------------------------|--------:|------:|:----------------------|-------------:|
| Immunohistochemistry           |       0 |    19 | Test                  |     0.9561   |
| negative                       |      25 |    32 | Biomarker_Measurement |     0.968    |
| thyroid transcription factor-1 |      38 |    67 | Biomarker             |     0.610925 |
| napsin A                       |      73 |    80 | Biomarker             |     0.8696   |
| positive                       |      96 |   103 | Biomarker_Measurement |     0.9228   |
| ER                             |     109 |   110 | Biomarker             |     0.9978   |
| PR                             |     116 |   117 | Biomarker             |     0.9932   |
| negative                       |     124 |   131 | Biomarker_Measurement |     0.9781   |
| HER2                           |     137 |   140 | Biomarker             |     0.7243   |


******************** assertion results ********************

| chunk                          | ner_label        | assertion   | assertion_source   |
|:-------------------------------|:-----------------|:------------|:-------------------|
| Immunohistochemistry           | Pathology_Test   | Past        | assertion_oncology |
| negative                       | Biomarker_Result | Past        | assertion_oncology |
| thyroid transcription factor-1 | Biomarker        | Present     | assertion_oncology |
| napsin A                       | Biomarker        | Present     | assertion_oncology |
| positive                       | Biomarker_Result | Present     | assertion_oncology |
| ER                             | Biomarker        | Present     | assertion_oncology |
| PR                             | Biomarker        | Present     | assertion_oncology |
| negative                       | Biomarker_Result | Present     | assertion_oncology |
| HER2                           | Oncogene         | Present     | assertion_oncology |


******************** re results ********************

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
| Immunohistochemistry | Pathology_Test   | negative                       | Biomarker_Result | O             |
| negative             | Biomarker_Result | thyroid transcription factor-1 | Biomarker        | is_finding_of |
| negative             | Biomarker_Result | napsin A                       | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | ER                             | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | PR                             | Biomarker        | is_finding_of |
| positive             | Biomarker_Result | HER2                           | Oncogene         | is_finding_of |
| ER                   | Biomarker        | negative                       | Biomarker_Result | O             |
| PR                   | Biomarker        | negative                       | Biomarker_Result | O             |
| negative             | Biomarker_Result | HER2                           | Oncogene         | is_finding_of |
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
|Compatibility:|Healthcare NLP 5.4.1+|
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
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- TextMatcherInternalModel
- ChunkMergeModel
- ChunkMergeModel
- AssertionDLModel
- ChunkMergeModel
- AssertionDLModel
- AssertionMerger
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
- RelationExtractionModel
- RelationExtractionModel
- AnnotationMerger