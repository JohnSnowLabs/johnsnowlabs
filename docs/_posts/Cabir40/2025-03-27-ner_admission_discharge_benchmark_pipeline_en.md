---
layout: model
title: Detect Clinical Events (ADMISSION_DISCHARGE)
author: John Snow Labs
name: ner_admission_discharge_benchmark_pipeline
date: 2025-03-27
tags: [en, licensed, clinical, pipeline, ner, admission_discharge, benchmark]
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

This pipeline can be used to detect clinical `Admission Discharge` in medical text, with a focus on admission entities.

## Predicted Entities

`ADMISSION_DISCHARGE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_admission_discharge_benchmark_pipeline_en_5.5.3_3.4_1743108380355.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_admission_discharge_benchmark_pipeline_en_5.5.3_3.4_1743108380355.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_admission_discharge_benchmark_pipeline", "en", "clinical/models")

text = """
ADMISSION DATE :
12-6-93
DISCHARGE DATE :
12-9-93
IDENTIFYING DATA :
This 75 year old female was transferred from Iming Medical Center for angioplasty .
PRINCIPAL DIAGNOSIS :
Unstable angina .
ASSOCIATED DIAGNOSIS :
Hypertension .
PRINCIPAL PROCEDURE :
Right and circumflex angioplasty , cardiac catheterization on 12-6-93 .
HISTORY OF PRESENT ILLNESS :
This 75 year old woman was previously admitted here in November 1993 for chronic angina .
She had mild mitral regurgitation and a slightly diminished ejection fraction .
There was a 90% right coronary stenosis which was reduced to 30 with a balloon angioplasty .
There were three lesions in the circumflex , dilated successfully .
However , the low circumflex marginal vessel could not be crossed with the balloon .
"""

result = ner_pipeline.fullAnnotate(text)
```

{:.jsl-block}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = nlp.PretrainedPipeline("ner_admission_discharge_benchmark_pipeline", "en", "clinical/models")

text = """
ADMISSION DATE :
12-6-93
DISCHARGE DATE :
12-9-93
IDENTIFYING DATA :
This 75 year old female was transferred from Iming Medical Center for angioplasty .
PRINCIPAL DIAGNOSIS :
Unstable angina .
ASSOCIATED DIAGNOSIS :
Hypertension .
PRINCIPAL PROCEDURE :
Right and circumflex angioplasty , cardiac catheterization on 12-6-93 .
HISTORY OF PRESENT ILLNESS :
This 75 year old woman was previously admitted here in November 1993 for chronic angina .
She had mild mitral regurgitation and a slightly diminished ejection fraction .
There was a 90% right coronary stenosis which was reduced to 30 with a balloon angioplasty .
There were three lesions in the circumflex , dilated successfully .
However , the low circumflex marginal vessel could not be crossed with the balloon .
"""

result = ner_pipeline.fullAnnotate(text)
```

```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_admission_discharge_benchmark_pipeline", "en", "clinical/models")

val text = """
ADMISSION DATE :
12-6-93
DISCHARGE DATE :
12-9-93
IDENTIFYING DATA :
This 75 year old female was transferred from Iming Medical Center for angioplasty .
PRINCIPAL DIAGNOSIS :
Unstable angina .
ASSOCIATED DIAGNOSIS :
Hypertension .
PRINCIPAL PROCEDURE :
Right and circumflex angioplasty , cardiac catheterization on 12-6-93 .
HISTORY OF PRESENT ILLNESS :
This 75 year old woman was previously admitted here in November 1993 for chronic angina .
She had mild mitral regurgitation and a slightly diminished ejection fraction .
There was a 90% right coronary stenosis which was reduced to 30 with a balloon angioplasty .
There were three lesions in the circumflex , dilated successfully .
However , the low circumflex marginal vessel could not be crossed with the balloon .
"""

val result = ner_pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | chunk     |   begin |   end | ner_label           |
|---:|:----------|--------:|------:|:--------------------|
|  0 | ADMISSION |       1 |     9 | ADMISSION_DISCHARGE |
|  1 | DISCHARGE |      26 |    34 | ADMISSION_DISCHARGE |
|  2 | admitted  |     393 |   400 | ADMISSION_DISCHARGE |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_admission_discharge_benchmark_pipeline|
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
- ChunkMergeModel
- ChunkMergeModel


## Benchmarking
```bash
              label  precision    recall  f1-score   support
ADMISSION_DISCHARGE      0.983     0.986     0.984       799
                  O      1.000     1.000     1.000     81772
           accuracy      -         -         1.000     82571
          macro-avg      0.991     0.993     0.992     82571
       weighted-avg      1.000     1.000     1.000     82571
```