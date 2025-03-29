---
layout: model
title: Detect Symptom or Sign Entities (SYMPTOM_OR_SIGN)
author: John Snow Labs
name: ner_symptom_or_sign_benchmark_pipeline
date: 2025-03-28
tags: [licensed, clinical, en, pipeline, ner, symptom_or_sign, benchmark]
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

This pipeline can be used to extracts `symptom or sign` information in medical text.

## Predicted Entities

`SYMPTOM_OR_SIGN`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_symptom_or_sign_benchmark_pipeline_en_5.5.3_3.4_1743164685231.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_symptom_or_sign_benchmark_pipeline_en_5.5.3_3.4_1743164685231.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_symptom_or_sign_benchmark_pipeline", "en", "clinical/models")

text = """IDENTIFYING DATA AND CHIEF COMPLAINT :
Mrs. Saujule T. Neathe is a 73 year old Gravida 6 Para 4 abortions 2 with a background history of stage IIIC papillary serous adenocarcinoma of the ovary who presents on 5/30/94 for failure to thrive , right lower lobe pneumonia and obstructive uropathy .
This course of chemotherapy was complicated only by persistent diarrhea and some nausea and vomiting .
An abdominopelvic computerized tomography scan during that admission showed recurrent disease in the pelvis with bilateral hydronephrosis .
Two days following discharge , however , the patient was admitted to Sephsandpot Center because of a decreased urinary output and persistent nausea and vomiting and anorexia .
PHYSICAL EXAMINATION :
( on admission ) showed the patient to be low-grade febrile with temperature of 99.6. She was noted to be a thin , cachectic woman in no apparent distress . Head and neck examination remarkable only for extreme dry mucous membranes consistent with dehydration .
Abdomen :
showed well healed midline scar , non-distended , non-tender , bowel sounds were good , multiple small nodules were palpated subcutaneously in the upper abdomen which was non-tender , there was no costovertebral angle tenderness .
Pelvic and rectal examinations confirmed recurrence of tumor mass in the pelvis .
The patient was occult blood negative .
Extremities : showed no evidence of acute deep venous thrombosis . However , left leg had two plus pitting edema to the knee whereas the right leg had minimal edema .
"""

result = ner_pipeline.fullAnnotate(text)
```

{:.jsl-block}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = nlp.PretrainedPipeline("ner_symptom_or_sign_benchmark_pipeline", "en", "clinical/models")

text = """IDENTIFYING DATA AND CHIEF COMPLAINT :
Mrs. Saujule T. Neathe is a 73 year old Gravida 6 Para 4 abortions 2 with a background history of stage IIIC papillary serous adenocarcinoma of the ovary who presents on 5/30/94 for failure to thrive , right lower lobe pneumonia and obstructive uropathy .
This course of chemotherapy was complicated only by persistent diarrhea and some nausea and vomiting .
An abdominopelvic computerized tomography scan during that admission showed recurrent disease in the pelvis with bilateral hydronephrosis .
Two days following discharge , however , the patient was admitted to Sephsandpot Center because of a decreased urinary output and persistent nausea and vomiting and anorexia .
PHYSICAL EXAMINATION :
( on admission ) showed the patient to be low-grade febrile with temperature of 99.6. She was noted to be a thin , cachectic woman in no apparent distress . Head and neck examination remarkable only for extreme dry mucous membranes consistent with dehydration .
Abdomen :
showed well healed midline scar , non-distended , non-tender , bowel sounds were good , multiple small nodules were palpated subcutaneously in the upper abdomen which was non-tender , there was no costovertebral angle tenderness .
Pelvic and rectal examinations confirmed recurrence of tumor mass in the pelvis .
The patient was occult blood negative .
Extremities : showed no evidence of acute deep venous thrombosis . However , left leg had two plus pitting edema to the knee whereas the right leg had minimal edema .
"""

result = ner_pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_symptom_or_sign_benchmark_pipeline", "en", "clinical/models")

val text = """IDENTIFYING DATA AND CHIEF COMPLAINT :
Mrs. Saujule T. Neathe is a 73 year old Gravida 6 Para 4 abortions 2 with a background history of stage IIIC papillary serous adenocarcinoma of the ovary who presents on 5/30/94 for failure to thrive , right lower lobe pneumonia and obstructive uropathy .
This course of chemotherapy was complicated only by persistent diarrhea and some nausea and vomiting .
An abdominopelvic computerized tomography scan during that admission showed recurrent disease in the pelvis with bilateral hydronephrosis .
Two days following discharge , however , the patient was admitted to Sephsandpot Center because of a decreased urinary output and persistent nausea and vomiting and anorexia .
PHYSICAL EXAMINATION :
( on admission ) showed the patient to be low-grade febrile with temperature of 99.6. She was noted to be a thin , cachectic woman in no apparent distress . Head and neck examination remarkable only for extreme dry mucous membranes consistent with dehydration .
Abdomen :
showed well healed midline scar , non-distended , non-tender , bowel sounds were good , multiple small nodules were palpated subcutaneously in the upper abdomen which was non-tender , there was no costovertebral angle tenderness .
Pelvic and rectal examinations confirmed recurrence of tumor mass in the pelvis .
The patient was occult blood negative .
Extremities : showed no evidence of acute deep venous thrombosis . However , left leg had two plus pitting edema to the knee whereas the right leg had minimal edema .
"""

val result = ner_pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | chunk                           |   begin |   end | ner_label       |
|---:|:--------------------------------|--------:|------:|:----------------|
|  0 | failure to thrive               |     221 |   237 | SYMPTOM_OR_SIGN |
|  1 | nausea                          |     376 |   381 | SYMPTOM_OR_SIGN |
|  2 | vomiting                        |     387 |   394 | SYMPTOM_OR_SIGN |
|  3 | decreased urinary output        |     639 |   662 | SYMPTOM_OR_SIGN |
|  4 | nausea                          |     679 |   684 | SYMPTOM_OR_SIGN |
|  5 | vomiting                        |     690 |   697 | SYMPTOM_OR_SIGN |
|  6 | febrile                         |     789 |   795 | SYMPTOM_OR_SIGN |
|  7 | thin                            |     845 |   848 | SYMPTOM_OR_SIGN |
|  8 | cachectic                       |     852 |   860 | SYMPTOM_OR_SIGN |
|  9 | dry mucous membranes            |     948 |   967 | SYMPTOM_OR_SIGN |
| 10 | scar                            |    1036 |  1039 | SYMPTOM_OR_SIGN |
| 11 | non-tender                      |    1059 |  1068 | SYMPTOM_OR_SIGN |
| 12 | nodules                         |    1112 |  1118 | SYMPTOM_OR_SIGN |
| 13 | non-tender                      |    1180 |  1189 | SYMPTOM_OR_SIGN |
| 14 | costovertebral angle tenderness |    1206 |  1236 | SYMPTOM_OR_SIGN |
| 15 | mass                            |    1301 |  1304 | SYMPTOM_OR_SIGN |
| 16 | pitting edema                   |    1461 |  1473 | SYMPTOM_OR_SIGN |
| 17 | edema                           |    1521 |  1525 | SYMPTOM_OR_SIGN |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_symptom_or_sign_benchmark_pipeline|
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
- MedicalNerModel
- NerConverterInternalModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel

## Benchmarking

```bash

          label  precision    recall  f1-score   support
              O      0.993     0.995     0.994     79865
SYMPTOM_OR_SIGN      0.848     0.787     0.816      2706
       accuracy      -         -         0.988     82571
      macro-avg      0.920     0.891     0.905     82571
   weighted-avg      0.988     0.988     0.988     82571

```