---
layout: model
title: Mapping Phenotype Entities with Corresponding HPO Codes (Pretrained Pipeline)
author: John Snow Labs
name: hpo_mapper_pipeline_v2
date: 2025-06-26
tags: [licensed, en, clinical, hpo, pipeline, ner, assertion, mapper]
task: [Named Entity Recognition, Chunk Mapping, Assertion Status, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to map extracted phenotype entities from clinical or biomedical text to their corresponding Human Phenotype Ontology (HPO) codes and assign their assertion status. It ensures that observed symptoms, signs, and clinical abnormalities are standardized using HPO terminology.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.1.Code_Mapping_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_mapper_pipeline_v2_en_6.0.2_3.4_1750940556294.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_mapper_pipeline_v2_en_6.0.2_3.4_1750940556294.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("hpo_mapper_pipeline_v2", "en", "clinical/models")

result = pipeline.fullAnnotate("""APNEA: Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity.
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation.
Mother is A+, GBS unknown, and infant delivered
for decreasing fetal movement and preeclampsia.
Long finger and toes detected.
he has a increased overbite expression.
""")

```

{:.jsl-block}
```python

pipeline = nlp.PretrainedPipeline("hpo_mapper_pipeline_v2", "en", "clinical/models")


result = pipeline.fullAnnotate("""APNEA: Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity.
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation.
Mother is A+, GBS unknown, and infant delivered
for decreasing fetal movement and preeclampsia.
Long finger and toes detected.
he has a increased overbite expression.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("hpo_mapper_pipeline_v2", "en", "clinical/models")

val result = pipeline.fullAnnotate("""APNEA: Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity.
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation.
Mother is A+, GBS unknown, and infant delivered
for decreasing fetal movement and preeclampsia.
Long finger and toes detected.
he has a increased overbite expression.
""")

```
</div>

## Results

```bash

+----------+-----------------------+-------------------------+-----+---+--------+
|hpo_code  |matched_text           |ner_chunk                |begin|end|result  |
+----------+-----------------------+-------------------------+-----+---+--------+
|HP:0002904|hyperbilirubinemia     |hyperbilirubinemia       |104  |121|present |
|HP:0002104|Apnea                  |apnea                    |16   |20 |possible|
|HP:0034236|apnea prematurity      |apnea of prematurity     |16   |35 |present |
|HP:0100806|Sepsis                 |sepsis                   |186  |191|present |
|HP:0100602|preeclampsia           |preeclampsia             |287  |298|present |
|HP:0100807|long finger            |Long finger              |301  |311|present |
|HP:0001558|decrease fetal movement|decreasing fetal movement|257  |281|present |
|HP:0011094|Increased overbite     |increased overbite       |341  |358|present |
|HP:0011094|overbite               |overbite                 |351  |358|present |
+----------+-----------------------+-------------------------+-----+---+--------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_mapper_pipeline_v2|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- InternalDocumentSplitter
- TokenizerModel
- TextMatcherInternalModel
- WordEmbeddingsModel
- ChunkMapperModel
- AssertionDLModel