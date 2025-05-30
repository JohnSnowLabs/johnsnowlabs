---
layout: model
title: Pipeline to Detect PHI in text (base)
author: John Snow Labs
name: ner_deid_sd_pipeline
date: 2023-06-16
tags: [ner, clinical, licensed, en]
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

This pretrained pipeline is built on the top of [ner_deid_sd](https://nlp.johnsnowlabs.com/2021/04/01/ner_deid_sd_en.html) model.

## Predicted Entities

`NAME`, `LOCATION`, `DATE`, `AGE`, `PROFESSION`, `ID`, `CONTACT`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_sd_pipeline_en_4.4.4_3.2_1686948413205.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_sd_pipeline_en_4.4.4_3.2_1686948413205.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_deid_sd_pipeline", "en", "clinical/models")

text = '''Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 302-786-5227.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_deid_sd_pipeline", "en", "clinical/models")

val text = "Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 302-786-5227."

val result = pipeline.fullAnnotate(text)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.deid.sd.pipeline").predict("""Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 302-786-5227.""")
```

</div>



## Results

```bash
|    | ner_chunks                    |   begin |   end | ner_label   |   confidence |
|---:|:------------------------------|--------:|------:|:------------|-------------:|
|  0 | 2093-01-13                    |      14 |    23 | DATE        |     0.9952   |
|  1 | David Hale                    |      27 |    36 | NAME        |     0.9834   |
|  2 | Hendrickson Ora               |      55 |    69 | NAME        |     0.97745  |
|  3 | 7194334                       |      78 |    84 | ID          |     0.999    |
|  4 | 01/13/93                      |      93 |   100 | DATE        |     0.983    |
|  5 | Oliveira                      |     110 |   117 | NAME        |     0.9965   |
|  6 | 25                            |     121 |   122 | AGE         |     0.9899   |
|  7 | 2079-11-09                    |     150 |   159 | DATE        |     0.9841   |
|  8 | Cocke County Baptist Hospital |     163 |   191 | LOCATION    |     0.84345  |
|  9 | 0295 Keats Street             |     195 |   211 | LOCATION    |     0.775333 |
| 10 | 302-786-5227                  |     221 |   232 | CONTACT     |     0.9492   |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_sd_pipeline|
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