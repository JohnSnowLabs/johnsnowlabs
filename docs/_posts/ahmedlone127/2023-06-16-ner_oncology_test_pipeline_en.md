---
layout: model
title: Pipeline to Extract Oncology Tests
author: John Snow Labs
name: ner_oncology_test_pipeline
date: 2023-06-16
tags: [licensed, clinical, oncology, en, ner, test]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_oncology_test](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_test_en.html) model.

## Predicted Entities

`Biomarker`, `Biomarker_Result`, `Imaging_Test`, `Oncogene`, `Pathology_Test`



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_test_pipeline_en_4.4.4_3.4_1686937802855.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_test_pipeline_en_4.4.4_3.4_1686937802855.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_oncology_test_pipeline", "en", "clinical/models")

text = ''' biopsy was conducted using an ultrasound guided thick-needle. His chest computed tomography (CT) scan was negative.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_oncology_test_pipeline", "en", "clinical/models")

val text = " biopsy was conducted using an ultrasound guided thick-needle. His chest computed tomography (CT) scan was negative."

val result = pipeline.fullAnnotate(text)
```

{:.nlu-block}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_oncology_test_pipeline", "en", "clinical/models")

text = ''' biopsy was conducted using an ultrasound guided thick-needle. His chest computed tomography (CT) scan was negative.'''

result = pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | ner_chunks                |   begin |   end | ner_label      |   confidence |
|---:|:--------------------------|--------:|------:|:---------------|-------------:|
|  0 | biopsy                    |       1 |     6 | Pathology_Test |      0.9987  |
|  1 | ultrasound guided         |      31 |    47 | Imaging_Test   |      0.87635 |
|  2 | chest computed tomography |      67 |    91 | Imaging_Test   |      0.9176  |
|  3 | CT                        |      94 |    95 | Imaging_Test   |      0.8294  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_test_pipeline|
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
- NerConverterInternalModel