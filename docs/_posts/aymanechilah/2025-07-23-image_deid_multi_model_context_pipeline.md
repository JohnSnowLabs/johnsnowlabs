---
layout: model
title: Image Deidentification Multi Model Context
author: John Snow Labs
name: image_deid_multi_model_context_pipeline
date: 2025-07-23
tags: [en, licensed]
task: De-identification
language: en
nav_key: models
edition: Visual NLP 6.0.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to mask PHI information in Images.
The output is an Image, similar to the one at the input, but with black bounding boxes on top of the targeted entities.

## Predicted Entities

``AGE``, ``CITY``, ``COUNTRY``, ``DATE``, ``DOCTOR``, ``EMAIL``, ``HOSPITAL``, ``IDNUM``, ``ORGANIZATION``, ``PATIENT``, ``PHONE``, ``PROFESSION``, ``STATE``, ``STREET``, ``USERNAME``, ``ZIP``, ``SIGNATURE``.


{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/PP_IMAGE_DEIDENTIFICATION/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/SparkOcrImageDeIdentificationPipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/image_deid_multi_model_context_pipeline_cpu_en_6.0.0_3.0_1749464326000.zip){:.button.button-orange.button-orange-trans.arr.button-icon}


## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline
deid_pipeline = PretrainedPipeline("image_deid_multi_model_context_pipeline_cpu", "en", "clinical/ocr")
```

```scala
import com.johnsnowlabs.ocr.pretrained.PretrainedPipeline
val deid_pipeline = PretrainedPipeline("image_deid_multi_model_context_pipeline_cpu", lang = "en", "clinical/ocr")
```

</div>

{:.model-param}

## Example

### Input:
![Screenshot](/assets/images/examples_ocr/deid_manip_1.png)

### Output:
![Screenshot](/assets/images/examples_ocr/deid_manip_2.png)

## Model Information

{:.table-model}
|---|---|
|Model Name:|image_deid_multi_model_context_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|5.3 GB|

## Included Models

- ImageToText
- DocumentAssembler
- SentenceDetectorDLModel
- Regex
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- EntityExtractor
- ContextualParserModel
- RegexMatcher
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcher
- ChunkMergeModel
- ChunkMergeModel
- XLMRobertaEmbeddings
- MedicalNerModel
- NerConverter 
- PretrainedZeroShotNER
- NerConverter
- PretrainedZeroShotNER
- NerConverter
- ChunkMergeModel
- PositionFinder
- ImageDrawRegions

