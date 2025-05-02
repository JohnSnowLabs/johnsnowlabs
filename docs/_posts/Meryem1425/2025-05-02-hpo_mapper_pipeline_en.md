---
layout: model
title: Mapping Phenotype Entities with Corresponding HPO Codes (Pretrained Pipeline)
author: John Snow Labs
name: hpo_mapper_pipeline
date: 2025-05-02
tags: [licensed, en, clinical, hpo, pipeline, ner, mapper]
task: [Named Entity Recognition, Chunk Mapping, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.0.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to map extracted phenotype entities from clinical or biomedical text to their corresponding Human Phenotype Ontology (HPO) codes. It ensures that observed symptoms, signs, and clinical abnormalities are standardized using HPO terminology.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_mapper_pipeline_en_6.0.0_3.0_1746195778533.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_mapper_pipeline_en_6.0.0_3.0_1746195778533.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("hpo_mapper_pipeline", "en", "clinical/models")

result = pipeline.fullAnnotate("""APNEA: Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity.
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation.""")

```

{:.jsl-block}
```python

pipeline = nlp.PretrainedPipeline("hpo_mapper_pipeline", "en", "clinical/models")


result = pipeline.fullAnnotate("""APNEA: Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity.
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("hpo_mapper_pipeline", "en", "clinical/models")

val result = pipeline.fullAnnotate("""APNEA: Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity.
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation.""")

```
</div>

## Results

```bash

+------------------+-----+---+-----+----------+
|             chunk|begin|end|label|  hpo_code|
+------------------+-----+---+-----+----------+
|             APNEA|    0|  4|  HPO|HP:0002104|
|             apnea|   16| 20|  HPO|HP:0002104|
|HYPERBILIRUBINEMIA|   66| 83|  HPO|HP:0002904|
|hyperbilirubinemia|   91|108|  HPO|HP:0002904|
|            sepsis|  167|172|  HPO|HP:0100806|
+------------------+-----+---+-----+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_mapper_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.0 MB|

## Included Models

- DocumentAssembler
- TokenizerModel
- StopWordsCleaner
- TokenAssembler
- SentenceDetectorDLModel
- TokenizerModel
- TextMatcherInternalModel
- ChunkMapperModel