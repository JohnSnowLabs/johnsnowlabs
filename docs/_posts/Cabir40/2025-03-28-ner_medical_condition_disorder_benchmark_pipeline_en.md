---
layout: model
title: Detect Medical Conditions, Disorders, Diseases, and Injuries Entities (MEDICAL_CONDITION_DISORDER)
author: John Snow Labs
name: ner_medical_condition_disorder_benchmark_pipeline
date: 2025-03-28
tags: [licensed, clinical, en, pipeline, ner, medical_condition_disorder, benchmark]
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

This pipeline can be used to extracts `medical condition disorder` information in medical text.

## Predicted Entities

`MEDICAL_CONDITION_DISORDER`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_medical_condition_disorder_benchmark_pipeline_en_5.5.3_3.4_1743166011329.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_medical_condition_disorder_benchmark_pipeline_en_5.5.3_3.4_1743166011329.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_medical_condition_disorder_benchmark_pipeline", "en", "clinical/models")

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

ner_pipeline = nlp.PretrainedPipeline("ner_medical_condition_disorder_benchmark_pipeline", "en", "clinical/models")

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

val ner_pipeline = PretrainedPipeline("ner_medical_condition_disorder_benchmark_pipeline", "en", "clinical/models")

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
|    | chunk                           |   begin |   end | ner_label                  |
|---:|:--------------------------------|--------:|------:|:---------------------------|
|  0 | papillary serous adenocarcinoma |     148 |   178 | MEDICAL_CONDITION_DISORDER |
|  1 | pneumonia                       |     258 |   266 | MEDICAL_CONDITION_DISORDER |
|  2 | obstructive uropathy            |     272 |   291 | MEDICAL_CONDITION_DISORDER |
|  3 | disease                         |     484 |   490 | MEDICAL_CONDITION_DISORDER |
|  4 | hydronephrosis                  |     521 |   534 | MEDICAL_CONDITION_DISORDER |
|  5 | anorexia                        |     703 |   710 | MEDICAL_CONDITION_DISORDER |
|  6 | dehydration                     |     985 |   995 | MEDICAL_CONDITION_DISORDER |
|  7 | tumor                           |    1295 |  1299 | MEDICAL_CONDITION_DISORDER |
|  8 | deep venous thrombosis          |    1404 |  1425 | MEDICAL_CONDITION_DISORDER |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_medical_condition_disorder_benchmark_pipeline|
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
MEDICAL_CONDITION_DISORDER      0.936     0.834     0.882      3439
                         O      0.993     0.998     0.995     79132
                  accuracy      -         -         0.991     82571
                 macro-avg      0.964     0.916     0.939     82571
              weighted-avg      0.990     0.991     0.990     82571

```