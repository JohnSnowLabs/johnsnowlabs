---
layout: model
title: Pipeline to Detect PHI for Deidentification purposes (Italian)
author: John Snow Labs
name: ner_deid_subentity_pipeline
date: 2023-06-17
tags: [deid, it, licensed]
task: [Named Entity Recognition, De-identification]
language: it
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_deid_subentity](https://nlp.johnsnowlabs.com/2022/03/25/ner_deid_subentity_it_2_4.html) model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_pipeline_it_4.4.4_3.0_1686995957424.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_pipeline_it_4.4.4_3.0_1686995957424.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_deid_subentity_pipeline", "it", "clinical/models")

text = '''Ho visto Gastone Montanariello (49 anni) riferito all' Ospedale San Camillo per diabete mal controllato con sintomi risalenti a marzo 2015.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_deid_subentity_pipeline", "it", "clinical/models")

val text = "Ho visto Gastone Montanariello (49 anni) riferito all' Ospedale San Camillo per diabete mal controllato con sintomi risalenti a marzo 2015."

val result = pipeline.fullAnnotate(text)
```

{:.nlu-block}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_deid_subentity_pipeline", "it", "clinical/models")

text = '''Ho visto Gastone Montanariello (49 anni) riferito all' Ospedale San Camillo per diabete mal controllato con sintomi risalenti a marzo 2015.'''

result = pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | ner_chunks            |   begin |   end | ner_label   | confidence   |
|---:|:----------------------|--------:|------:|:------------|:-------------|
|  0 | Gastone Montanariello |       9 |    29 | PATIENT     |              |
|  1 | 49                    |      32 |    33 | AGE         |              |
|  2 | Ospedale San Camillo  |      55 |    74 | HOSPITAL    |              |
|  3 | marzo 2015            |     128 |   137 | DATE        |              |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_subentity_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|it|
|Size:|1.3 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel