---
layout: model
title: Detect Grade Stage Severity and Modifier Entities (GRADE_STAGE_SEVERITY)
author: John Snow Labs
name: ner_grade_stage_severity_benchmark_pipeline
date: 2025-03-28
tags: [licensed, clinical, en, pipeline, ner, grade_stage_severity, benchmark]
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

This pipeline can be used to extracts biomarker, grade stage and severity information in medical text.
`GRADE_STAGE_SEVERITY`:  Mentions of pathological grading, staging, severity and modifier of the diseases/cancers.

## Predicted Entities

`GRADE_STAGE_SEVERITY`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_grade_stage_severity_benchmark_pipeline_en_5.5.3_3.4_1743123356488.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_grade_stage_severity_benchmark_pipeline_en_5.5.3_3.4_1743123356488.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_grade_stage_severity_benchmark_pipeline", "en", "clinical/models")

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

ner_pipeline = nlp.PretrainedPipeline("ner_grade_stage_severity_benchmark_pipeline", "en", "clinical/models")

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

val ner_pipeline = PretrainedPipeline("ner_grade_stage_severity_benchmark_pipeline", "en", "clinical/models")

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
|    | chunk            |   begin |   end | ner_label            |
|---:|:-----------------|--------:|------:|:---------------------|
|  0 | stage IIIC       |     137 |   146 | GRADE_STAGE_SEVERITY |
|  1 | persistent       |     347 |   356 | GRADE_STAGE_SEVERITY |
|  2 | recurrent        |     474 |   482 | GRADE_STAGE_SEVERITY |
|  3 | persistent       |     668 |   677 | GRADE_STAGE_SEVERITY |
|  4 | low-grade        |     779 |   787 | GRADE_STAGE_SEVERITY |
|  5 | apparent         |     874 |   881 | GRADE_STAGE_SEVERITY |
|  6 | extreme          |     940 |   946 | GRADE_STAGE_SEVERITY |
|  7 | multiple         |    1097 |  1104 | GRADE_STAGE_SEVERITY |
|  8 | small            |    1106 |  1110 | GRADE_STAGE_SEVERITY |
|  9 | acute            |    1398 |  1402 | GRADE_STAGE_SEVERITY |
| 10 | two plus pitting |    1452 |  1467 | GRADE_STAGE_SEVERITY |
| 11 | minimal          |    1513 |  1519 | GRADE_STAGE_SEVERITY |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_grade_stage_severity_benchmark_pipeline|
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
- TextMatcherInternalModel
- ContextualParserModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel

## Benchmarking

```bash

               label  precision    recall  f1-score   support
GRADE_STAGE_SEVERITY      0.722     0.904     0.803       689
                   O      0.999     0.997     0.998     81882
            accuracy                          0.996     82571
           macro avg      0.861     0.951     0.900     82571
        weighted avg      0.997     0.996     0.996     82571

```