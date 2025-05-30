---
layout: model
title: Pipeline to Detect Mentions of Tumors in Text
author: John Snow Labs
name: nerdl_tumour_demo_pipeline
date: 2023-03-14
tags: [ner, clinical, licensed, en]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.3.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [nerdl_tumour_demo](https://nlp.johnsnowlabs.com/2021/04/01/nerdl_tumour_demo_en.html) model.

## Predicted Entities

`Grading`, `Laterality`, `Localization`, `Size`, `Staging`, `X`


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/nerdl_tumour_demo_pipeline_en_4.3.0_3.2_1678837464087.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/nerdl_tumour_demo_pipeline_en_4.3.0_3.2_1678837464087.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("nerdl_tumour_demo_pipeline", "en", "clinical/models")

text = '''The final diagnosis was metastatic breast carcinoma, and it was classified as T2N1M1 stage IV. The histological grade of this 4 cm tumor was grade 2.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("nerdl_tumour_demo_pipeline", "en", "clinical/models")

val text = "The final diagnosis was metastatic breast carcinoma, and it was classified as T2N1M1 stage IV. The histological grade of this 4 cm tumor was grade 2."

val result = pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | ner_chunks       |   begin |   end | ner_label    | confidence   |
|---:|:-----------------|--------:|------:|:-------------|:-------------|
|  0 | breast carcinoma |      35 |    50 | Localization |              |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|nerdl_tumour_demo_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.3.0+|
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