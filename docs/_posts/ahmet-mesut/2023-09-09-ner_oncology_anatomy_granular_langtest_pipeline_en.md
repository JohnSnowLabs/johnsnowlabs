---
layout: model
title: Pipeline to Extract Granular Anatomical Entities from Oncology Texts (langtest)
author: John Snow Labs
name: ner_oncology_anatomy_granular_langtest_pipeline
date: 2023-09-09
tags: [licensed, en, oncology, anatomy, granular, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.1.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_oncology_anatomy_granular_langtest](https://nlp.johnsnowlabs.com/2023/09/03/ner_oncology_anatomy_granular_langtest_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_anatomy_granular_langtest_pipeline_en_5.1.0_3.4_1694288750457.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_anatomy_granular_langtest_pipeline_en_5.1.0_3.4_1694288750457.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_oncology_anatomy_granular_langtest_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient presented a mass in her left breast, and a possible metastasis in her lungs and in her liver.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_oncology_anatomy_granular_langtest_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient presented a mass in her left breast, and a possible metastasis in her lungs and in her liver.""")

```
</div>

## Results

```bash
|    | chunks   |   begin |   end | entities    |
|---:|:---------|--------:|------:|:------------|
|  0 | left     |      36 |    39 | Direction   |
|  1 | breast   |      41 |    46 | Site_Breast |
|  2 | lungs    |      82 |    86 | Site_Lung   |
|  3 | liver    |      99 |   103 | Site_Liver  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_anatomy_granular_langtest_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.1.0+|
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