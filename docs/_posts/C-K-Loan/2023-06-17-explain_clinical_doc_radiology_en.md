---
layout: model
title: Pipeline to Detect Radiology Entities, Assign Assertion Status and Find Relations
author: John Snow Labs
name: explain_clinical_doc_radiology
date: 2023-06-17
tags: [licensed, clinical, en, ner, assertion, relation_extraction, radiology]
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

A pipeline for detecting posology entities with the `ner_radiology` NER model, assigning their assertion status with `assertion_dl_radiology` model, and extracting relations between posology-related terminology with `re_test_problem_finding` relation extraction model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_radiology_en_4.4.4_3.0_1686988742305.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_radiology_en_4.4.4_3.0_1686988742305.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("explain_clinical_doc_radiology", "en", "clinical/models")

text = """Bilateral breast ultrasound was subsequently performed, which demonstrated an ovoid mass measuring approximately 0.5 x 0.5 x 0.4 cm in diameter located within the anteromedial aspect of the left shoulder. This mass demonstrates isoechoic echotexture to the adjacent muscle, with no evidence of internal color flow. This may represent benign fibrous tissue or a lipoma."""

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("explain_clinical_doc_radiology", "en", "clinical/models")

val text = """Bilateral breast ultrasound was subsequently performed, which demonstrated an ovoid mass measuring approximately 0.5 x 0.5 x 0.4 cm in diameter located within the anteromedial aspect of the left shoulder. This mass demonstrates isoechoic echotexture to the adjacent muscle, with no evidence of internal color flow. This may represent benign fibrous tissue or a lipoma."""

val result = pipeline.fullAnnotate(text)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.explain_doc.clinical_radiology.pipeline").predict("""Bilateral breast ultrasound was subsequently performed, which demonstrated an ovoid mass measuring approximately 0.5 x 0.5 x 0.4 cm in diameter located within the anteromedial aspect of the left shoulder. This mass demonstrates isoechoic echotexture to the adjacent muscle, with no evidence of internal color flow. This may represent benign fibrous tissue or a lipoma.""")
```

</div>

## Results

```bash
+----+------------------------------------------+---------------------------+
|    | chunks                                   | entities                  |
|---:|:-----------------------------------------|:--------------------------|
|  0 | Bilateral breast                         | BodyPart                  |
|  1 | ultrasound                               | ImagingTest               |
|  2 | ovoid mass                               | ImagingFindings           |
|  3 | 0.5 x 0.5 x 0.4                          | Measurements              |
|  4 | cm                                       | Units                     |
|  5 | anteromedial aspect of the left shoulder | BodyPart                  |
|  6 | mass                                     | ImagingFindings           |
|  7 | isoechoic echotexture                    | ImagingFindings           |
|  8 | muscle                                   | BodyPart                  |
|  9 | internal color flow                      | ImagingFindings           |
| 10 | benign fibrous tissue                    | ImagingFindings           |
| 11 | lipoma                                   | Disease_Syndrome_Disorder |
+----+------------------------------------------+---------------------------+

+----+-----------------------+---------------------------+-------------+
|    | chunks                | entities                  | assertion   |
|---:|:----------------------|:--------------------------|:------------|
|  0 | ultrasound            | ImagingTest               | Confirmed   |
|  1 | ovoid mass            | ImagingFindings           | Confirmed   |
|  2 | mass                  | ImagingFindings           | Confirmed   |
|  3 | isoechoic echotexture | ImagingFindings           | Confirmed   |
|  4 | internal color flow   | ImagingFindings           | Negative    |
|  5 | benign fibrous tissue | ImagingFindings           | Suspected   |
|  6 | lipoma                | Disease_Syndrome_Disorder | Suspected   |
+----+-----------------------+---------------------------+-------------+

+---------+-----------------+-----------------------+---------------------------+------------+
|relation | entity1         | chunk1                | entity2                   | chunk2     |
|--------:|:----------------|:----------------------|:--------------------------|:-----------|
|       1 | ImagingTest     | ultrasound            | ImagingFindings           | ovoid mass |
|       0 | ImagingFindings | benign fibrous tissue | Disease_Syndrome_Disorder | lipoma     |
+---------+-----------------+-----------------------+---------------------------+------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_radiology|
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
- NerConverter
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel