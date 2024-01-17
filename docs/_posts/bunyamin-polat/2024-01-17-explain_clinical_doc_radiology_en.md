---
layout: model
title: Explain Clinical Document - Radiology
author: John Snow Labs
name: explain_clinical_doc_radiology
date: 2024-01-17
tags: [licensed, en, radiology, pipeline, ner, assertion, relation_extraction]
task: [Named Entity Recognition, Assertion Status, Relation Extraction, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This specialized radiology pipeline can;

- extract radiology related entities,

- assign assertion status to the extracted entities,

- establish relations between the extracted entities from the clinical documents.

In this pipeline, five NER, one assertion and one relation extraction model were used to achive those tasks

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_radiology_en_5.2.1_3.0_1705528099960.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_radiology_en_5.2.1_3.0_1705528099960.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_radiology", "en", "clinical/models")

result = ner_pipeline.annotate("""Bilateral breast ultrasound was subsequently performed, which demonstrated an ovoid mass measuring approximately 0.5 x 0.5 x 0.4 cm in diameter located within the anteromedial aspect of the left shoulder. This mass demonstrates isoechoic echotexture to the adjacent muscle, with no evidence of internal color flow. This may represent benign fibrous tissue or a lipoma.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_radiology", "en", "clinical/models")

val result = ner_pipeline.annotate("""Bilateral breast ultrasound was subsequently performed, which demonstrated an ovoid mass measuring approximately 0.5 x 0.5 x 0.4 cm in diameter located within the anteromedial aspect of the left shoulder. This mass demonstrates isoechoic echotexture to the adjacent muscle, with no evidence of internal color flow. This may represent benign fibrous tissue or a lipoma.""")

```
</div>

## Results

```bash


|    |   sentence_id | chunks                                   |   begin |   end | entities                  |
|---:|--------------:|:-----------------------------------------|--------:|------:|:--------------------------|
|  0 |             0 | Bilateral breast                         |       0 |    15 | BodyPart                  |
|  1 |             0 | ultrasound                               |      17 |    26 | Imaging_Test              |
|  2 |             0 | ovoid mass                               |      78 |    87 | ImagingFindings           |
|  3 |             0 | 0.5 x 0.5 x 0.4 cm                       |     113 |   130 | Measurements              |
|  4 |             0 | anteromedial aspect of the left shoulder |     163 |   202 | BodyPart                  |
|  5 |             1 | mass                                     |     210 |   213 | ImagingFindings           |
|  6 |             1 | isoechoic echotexture                    |     228 |   248 | ImagingFindings           |
|  7 |             1 | adjacent muscle                          |     257 |   271 | BodyPart                  |
|  8 |             1 | internal color flow                      |     294 |   312 | ImagingFindings           |
|  9 |             2 | benign fibrous tissue                    |     334 |   354 | ImagingFindings           |
| 10 |             2 | lipoma                                   |     361 |   366 | Disease_Syndrome_Disorder |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_radiology|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
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
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel