---
layout: model
title: Pipeline to Detect PHI for Deidentification (Generic - Augmented)
author: John Snow Labs
name: ner_deid_generic_augmented_pipeline
date: 2023-06-13
tags: [licensed, ner, clinical, deidentification, generic, en]
task: [Named Entity Recognition, De-identification]
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

This pretrained pipeline is built on the top of [ner_deid_generic_augmented](https://nlp.johnsnowlabs.com/2021/06/30/ner_deid_generic_augmented_en.html) model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_augmented_pipeline_en_4.4.4_3.2_1686664043324.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_augmented_pipeline_en_4.4.4_3.2_1686664043324.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_deid_generic_augmented_pipeline", "en", "clinical/models")

pipeline.annotate("A. Record date : 2093-01-13, David Hale, M.D., Name : Hendrickson, Ora MR. # 7194334 Date : 01/13/93 PCP : Oliveira, 25 -year-old, Record date : 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227.")
```
```scala
val pipeline = new PretrainedPipeline("ner_deid_generic_augmented_pipeline", "en", "clinical/models")

pipeline.annotate("A. Record date : 2093-01-13, David Hale, M.D., Name : Hendrickson, Ora MR. # 7194334 Date : 01/13/93 PCP : Oliveira, 25 -year-old, Record date : 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227.")
```


{:.nlu-block}
```python
import nlu
nlu.load("en.med_ner.deid_generic_augmented.pipeline").predict("""A. Record date : 2093-01-13, David Hale, M.D., Name : Hendrickson, Ora MR. # 7194334 Date : 01/13/93 PCP : Oliveira, 25 -year-old, Record date : 1-11-2000. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227.""")
```

</div>



## Results

```bash
+-------------------------------------------------+---------+
|chunk                                            |ner_label|
+-------------------------------------------------+---------+
|2093-01-13                                       |DATE     |
|David Hale                                       |NAME     |
|Hendrickson                                      |NAME     |
|Ora MR.                                          |LOCATION |
|7194334                                          |ID       |
|01/13/93                                         |DATE     |
|Oliveira                                         |NAME     |
|25                                               |AGE      |
|1-11-2000                                        |DATE     |
|Cocke County Baptist Hospital. 0295 Keats Street.|LOCATION |
|(302) 786-5227                                   |CONTACT  |
+-------------------------------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_generic_augmented_pipeline|
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