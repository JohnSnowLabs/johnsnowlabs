---
layout: model
title: RE Pipeline between Body Parts and Direction Entities
author: John Snow Labs
name: re_bodypart_directions_pipeline
date: 2023-06-13
tags: [licensed, clinical, relation_extraction, body_part, directions, en]
task: Relation Extraction
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [re_bodypart_directions](https://nlp.johnsnowlabs.com/2021/01/18/re_bodypart_directions_en.html) model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/re_bodypart_directions_pipeline_en_4.4.4_3.2_1686664392280.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/re_bodypart_directions_pipeline_en_4.4.4_3.2_1686664392280.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("re_bodypart_directions_pipeline", "en", "clinical/models")

pipeline.fullAnnotate("MRI demonstrated infarction in the upper brain stem , left cerebellum and  right basil ganglia")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("re_bodypart_directions_pipeline", "en", "clinical/models")

pipeline.fullAnnotate("MRI demonstrated infarction in the upper brain stem , left cerebellum and  right basil ganglia")
```


{:.nlu-block}
```python
import nlu
nlu.load("en.relation.bodypart_directions.pipeline").predict("""MRI demonstrated infarction in the upper brain stem , left cerebellum and  right basil ganglia""")
```

</div>



## Results

```bash

| index | relations | entity1                     | entity1_begin | entity1_end | chunk1     | entity2                     | entity2_end | entity2_end | chunk2        | confidence |
|-------|-----------|-----------------------------|---------------|-------------|------------|-----------------------------|-------------|-------------|---------------|------------|
| 0     | 1         | Direction                   | 35            | 39          | upper      | Internal_organ_or_component | 41          | 50          | brain stem    | 0.9999989  |
| 1     | 0         | Direction                   | 35            | 39          | upper      | Internal_organ_or_component | 59          | 68          | cerebellum    | 0.99992585 |
| 2     | 0         | Direction                   | 35            | 39          | upper      | Internal_organ_or_component | 81          | 93          | basil ganglia | 0.9999999  |
| 3     | 0         | Internal_organ_or_component | 41            | 50          | brain stem | Direction                   | 54          | 57          | left          | 0.999811   |
| 4     | 0         | Internal_organ_or_component | 41            | 50          | brain stem | Direction                   | 75          | 79          | right         | 0.9998203  |
| 5     | 1         | Direction                   | 54            | 57          | left       | Internal_organ_or_component | 59          | 68          | cerebellum    | 1.0        |
| 6     | 0         | Direction                   | 54            | 57          | left       | Internal_organ_or_component | 81          | 93          | basil ganglia | 0.97616416 |
| 7     | 0         | Internal_organ_or_component | 59            | 68          | cerebellum | Direction                   | 75          | 79          | right         | 0.953046   |
| 8     | 1         | Direction                   | 75            | 79          | right      | Internal_organ_or_component | 81          | 93          | basil ganglia | 1.0        |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|re_bodypart_directions_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- PerceptronModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- DependencyParserModel
- RelationExtractionModel