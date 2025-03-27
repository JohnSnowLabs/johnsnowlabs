---
layout: model
title: Detect Text Entities (PROCEDURE)
author: John Snow Labs
name: ner_procedure_benchmark_pipeline
date: 2025-03-27
tags: [licensed, clinical, en, pipeline, ner, procedure, benchmark]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.5.3
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to extract procedure mentions in medical text.

## Predicted Entities

`PROCEDURE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_procedure_benchmark_pipeline_en_5.5.3_3.4_1743115349171.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_procedure_benchmark_pipeline_en_5.5.3_3.4_1743115349171.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_procedure_benchmark_pipeline", "en", "clinical/models")

text = """PRINCIPAL PROCEDURE :
4-2-93 , right and left heart catheterization ( transeptal ) with coronary graft and left ventriculogram .
4-8-93 , open heart aortic valve replacement and bypass of right coronary artery .

Mr. No was on the pump for 2 hours and 25 minutes , with an aortic crossclamp time of 1 hour and 48 minutes .
Postoperatively , the patient was extubated on the first postoperative day .
He had a good deal of pulmonary congestion .
He seemed to be doing well until the morning of 4-13-93 when he suddenly became pulseless .
There was no evidence of ventricular fibrillation .
Cardiopulmonary resuscitation was immediately undertaken , but was not successful .
The patient had his chest opened for any evidence of tamponade and there was no evidence of bleeding .
The heart appeared to be flaccid .
We really have no good explanation of what this was all about .
He was being treated for a possible pneumonia .
He did have a good deal of pulmonary congestion , but this occurred suddenly and unexpectedly .
Cardiopulmonary resuscitation efforts were carried out for virtually one hour , but were unsuccessful .
The patient was pronounced dead on the morning of 4-13-93 .
A post mortem examination will be performed .
"""

result = ner_pipeline.fullAnnotate(text)
```

{:.jsl-block}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = nlp.PretrainedPipeline("ner_procedure_benchmark_pipeline", "en", "clinical/models")

text = """PRINCIPAL PROCEDURE :
4-2-93 , right and left heart catheterization ( transeptal ) with coronary graft and left ventriculogram .
4-8-93 , open heart aortic valve replacement and bypass of right coronary artery .

Mr. No was on the pump for 2 hours and 25 minutes , with an aortic crossclamp time of 1 hour and 48 minutes .
Postoperatively , the patient was extubated on the first postoperative day .
He had a good deal of pulmonary congestion .
He seemed to be doing well until the morning of 4-13-93 when he suddenly became pulseless .
There was no evidence of ventricular fibrillation .
Cardiopulmonary resuscitation was immediately undertaken , but was not successful .
The patient had his chest opened for any evidence of tamponade and there was no evidence of bleeding .
The heart appeared to be flaccid .
We really have no good explanation of what this was all about .
He was being treated for a possible pneumonia .
He did have a good deal of pulmonary congestion , but this occurred suddenly and unexpectedly .
Cardiopulmonary resuscitation efforts were carried out for virtually one hour , but were unsuccessful .
The patient was pronounced dead on the morning of 4-13-93 .
A post mortem examination will be performed .
"""

result = ner_pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_procedure_benchmark_pipeline", "en", "clinical/models")

val text = """PRINCIPAL PROCEDURE :
4-2-93 , right and left heart catheterization ( transeptal ) with coronary graft and left ventriculogram .
4-8-93 , open heart aortic valve replacement and bypass of right coronary artery .

Mr. No was on the pump for 2 hours and 25 minutes , with an aortic crossclamp time of 1 hour and 48 minutes .
Postoperatively , the patient was extubated on the first postoperative day .
He had a good deal of pulmonary congestion .
He seemed to be doing well until the morning of 4-13-93 when he suddenly became pulseless .
There was no evidence of ventricular fibrillation .
Cardiopulmonary resuscitation was immediately undertaken , but was not successful .
The patient had his chest opened for any evidence of tamponade and there was no evidence of bleeding .
The heart appeared to be flaccid .
We really have no good explanation of what this was all about .
He was being treated for a possible pneumonia .
He did have a good deal of pulmonary congestion , but this occurred suddenly and unexpectedly .
Cardiopulmonary resuscitation efforts were carried out for virtually one hour , but were unsuccessful .
The patient was pronounced dead on the morning of 4-13-93 .
A post mortem examination will be performed .
"""

val result = ner_pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | chunk                               |   begin |   end | ner_label   |
|---:|:------------------------------------|--------:|------:|:------------|
|  0 | heart catheterization               |      46 |    66 | PROCEDURE   |
|  1 | transeptal                          |      70 |    79 | PROCEDURE   |
|  2 | coronary graft                      |      88 |   101 | PROCEDURE   |
|  3 | left ventriculogram                 |     107 |   125 | PROCEDURE   |
|  4 | open heart aortic valve replacement |     138 |   172 | PROCEDURE   |
|  5 | bypass                              |     178 |   183 | PROCEDURE   |
|  6 | aortic crossclamp                   |     273 |   289 | PROCEDURE   |
|  7 | extubated                           |     357 |   365 | PROCEDURE   |
|  8 | Cardiopulmonary resuscitation       |     589 |   617 | PROCEDURE   |
|  9 | Cardiopulmonary resuscitation       |    1019 |  1047 | PROCEDURE   |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_procedure_benchmark_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- WordEmbeddingsModel
- TextMatcherInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel

## Benchmarking

```bash

        label  precision    recall  f1-score   support
           O      0.999     0.997     0.998     81024
   PROCEDURE      0.869     0.936     0.901      1547
    accuracy                          0.996     82571
   macro avg      0.934     0.967     0.950     82571
weighted avg      0.996     0.996     0.996     82571

```