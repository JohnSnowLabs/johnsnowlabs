---
layout: model
title: Pipeline for Adverse Drug Events
author: John Snow Labs
name: explain_clinical_doc_ade
date: 2021-07-15
tags: [licensed, clinical, en, pipeline]
task: [Named Entity Recognition, Text Classification, Relation Extraction, Pipeline Healthcare]
language: en
nav_key: models
edition: Healthcare NLP 3.1.2
spark_version: 3.0
supported: true
recommended: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

A pipeline for Adverse Drug Events (ADE) with `ner_ade_biobert`, `assertion_dl_biobert`, `classifierdl_ade_conversational_biobert`, and `re_ade_biobert` . It will classify the document, extract ADE and DRUG clinical entities, assign assertion status to ADE entities, and relate Drugs with their ADEs.


{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ADE/){:.button.button-orange}
[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/16.Adverse_Drug_Event_ADE_NER_and_Classifier.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_ade_en_3.1.2_3.0_1626380200755.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_ade_en_3.1.2_3.0_1626380200755.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
pipeline = PretrainedPipeline('explain_clinical_doc_ade', 'en', 'clinical/models')

res = pipeline.fullAnnotate("""Been taking Lipitor for 3 months, have experienced severe fatigue a lot!!! ,   
I have only experienced cramps so far, after Doctor moved me to voltaren 2 months ago.""")


```
```scala
val era_pipeline = new PretrainedPipeline("explain_clinical_doc_ade", "en", "clinical/models")

val result = era_pipeline.fullAnnotate("""Been taking Lipitor for 3 months, have experienced severe fatigue a lot!!! ,   
I have only experienced cramps so far, after Doctor moved me to voltaren 2 months ago.""")(0)

```


{:.nlu-block}
```python
import nlu
nlu.load("en.explain_doc.clinical_ade").predict("""Been taking Lipitor for 3 months, have experienced severe fatigue a lot!!! , I have only experienced cramps so far, after Doctor moved me to voltaren 2 months ago.""")
```

</div>

## Results

```bash
Assertion:

|   |         chunks | entities | assertion |
|--:|---------------:|---------:|----------:|
| 0 |        Lipitor |     DRUG |      Past |
| 1 | severe fatigue |      ADE |      Past |
| 2 |         cramps |      ADE |   Present |
| 3 |       voltaren |     DRUG |      Past |

Relations:

|   | relation | entity1 |  chunk1 | entity2 |         chunk2 |
|--:|---------:|--------:|--------:|--------:|---------------:|
| 0 |        1 |    DRUG | Lipitor |     ADE | severe fatigue |
| 1 |        0 |     ADE |  cramps |    DRUG |       voltaren |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_ade|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 3.1.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|

## Included Models

- DocumentAssembler
- TokenizerModel
- BertEmbeddings
- SentenceEmbeddings
- ClassifierDLModel
- MedicalNerModel
- NerConverterInternal
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
- NerConverterInternal
- AssertionDLModel
