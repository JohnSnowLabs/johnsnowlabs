---
layout: model
title: Explain Clinical Document Pipeline - CARP
author: John Snow Labs
name: explain_clinical_doc_carp
date: 2023-06-17
tags: [pipeline, en, clinical, licensed]
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

A pipeline with `ner_clinical`, `assertion_dl`, `re_clinical` and `ner_posology`. It will extract clinical and medication entities, assign assertion status and find relationships between clinical entities.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_carp_en_4.4.4_3.0_1686978853744.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_carp_en_4.4.4_3.0_1686978853744.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("explain_clinical_doc_carp", "en", "clinical/models")

text = """A 28-year-old female with a history of gestational diabetes mellitus, used to take metformin 1000 mg two times a day, presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting. She was seen by the endocrinology service and discharged on 40 units of insulin glargine at night, 12 units of insulin lispro with meals."""

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("explain_clinical_doc_carp", "en", "clinical/models")

val text = """A 28-year-old female with a history of gestational diabetes mellitus, used to take metformin 1000 mg two times a day, presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting. She was seen by the endocrinology service and discharged on 40 units of insulin glargine at night, 12 units of insulin lispro with meals."""

val result = pipeline.fullAnnotate(text)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.explain_doc.carp").predict("""A 28-year-old female with a history of gestational diabetes mellitus, used to take metformin 1000 mg two times a day, presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting. She was seen by the endocrinology service and discharged on 40 units of insulin glargine at night, 12 units of insulin lispro with meals.""")
```

</div>


## Results

```bash
|   | chunks                        | ner_clinical | assertion | posology_chunk   | ner_posology | relations |
|---|-------------------------------|--------------|-----------|------------------|--------------|-----------|
| 0 | gestational diabetes mellitus | PROBLEM      | present   | metformin        | Drug         | TrAP      |
| 1 | metformin                     | TREATMENT    | present   | 1000 mg          | Strength     | TrCP      |
| 2 | polyuria                      | PROBLEM      | present   | two times a day  | Frequency    | TrCP      |
| 3 | polydipsia                    | PROBLEM      | present   | 40 units         | Dosage       | TrWP      |
| 4 | poor appetite                 | PROBLEM      | present   | insulin glargine | Drug         | TrCP      |
| 5 | vomiting                      | PROBLEM      | present   | at night         | Frequency    | TrAP      |
| 6 | insulin glargine              | TREATMENT    | present   | 12 units         | Dosage       | TrAP      |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_carp|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- PerceptronModel
- DependencyParserModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- AssertionDLModel
- RelationExtractionModel