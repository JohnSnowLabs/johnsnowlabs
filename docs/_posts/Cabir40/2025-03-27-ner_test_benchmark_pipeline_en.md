---
layout: model
title: Detect Test Entities (TEST)
author: John Snow Labs
name: ner_test_benchmark_pipeline
date: 2025-03-27
tags: [licensed, clinical, en, pipeline, ner, test, benchmark]
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

This pipeline can be used to extract `test` mentions in medical text.

## Predicted Entities

`TEST`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_test_benchmark_pipeline_en_5.5.3_3.4_1743112378089.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_test_benchmark_pipeline_en_5.5.3_3.4_1743112378089.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_test_benchmark_pipeline", "en", "clinical/models")

text = """PHYSICAL EXAMINATION :
On physical examination , the patient was a well developed , stocky gentleman .
The blood pressure was 115/80 , pulse 80 , respirations of 20 , venous pressure elevated at 3 cm above the clavicle at 90 degrees .
There were very small , barely palpable carotid pulses .
There was dullness at the right base , with a high diaphragm and possibly some fluid .
The cardiac examination showed a left ventricular tap at the fifth intercostal space left of the midclavicular line .
There was a grade II / VI systolic ejection murmur in the aortic area , no third sound , and paradoxical splitting of the second sound .
The liver was not palpable .
There were diminished pulses in the legs .
LABORATORY DATA :
The hemoglobin was 14.4 grams percent , white blood count 6,900 , platelet count 125,000 , sodium 137 mEq. per liter , potassium of 4.7 , BUN and creatinine of 23 and 1.3 mg percent .
The electrocardiogram showed left ventricular hypertrophy and non-specific ST-T wave changes .
The chest film showed massive cardiomegaly with pulmonary venous engorgement ."""

result = ner_pipeline.fullAnnotate(text)
```

{:.jsl-block}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = nlp.PretrainedPipeline("ner_test_benchmark_pipeline", "en", "clinical/models")

text = """PHYSICAL EXAMINATION :
On physical examination , the patient was a well developed , stocky gentleman .
The blood pressure was 115/80 , pulse 80 , respirations of 20 , venous pressure elevated at 3 cm above the clavicle at 90 degrees .
There were very small , barely palpable carotid pulses .
There was dullness at the right base , with a high diaphragm and possibly some fluid .
The cardiac examination showed a left ventricular tap at the fifth intercostal space left of the midclavicular line .
There was a grade II / VI systolic ejection murmur in the aortic area , no third sound , and paradoxical splitting of the second sound .
The liver was not palpable .
There were diminished pulses in the legs .
LABORATORY DATA :
The hemoglobin was 14.4 grams percent , white blood count 6,900 , platelet count 125,000 , sodium 137 mEq. per liter , potassium of 4.7 , BUN and creatinine of 23 and 1.3 mg percent .
The electrocardiogram showed left ventricular hypertrophy and non-specific ST-T wave changes .
The chest film showed massive cardiomegaly with pulmonary venous engorgement ."""

result = ner_pipeline.fullAnnotate(text)
```

```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_test_benchmark_pipeline", "en", "clinical/models")

val text = """PHYSICAL EXAMINATION :
On physical examination , the patient was a well developed , stocky gentleman .
The blood pressure was 115/80 , pulse 80 , respirations of 20 , venous pressure elevated at 3 cm above the clavicle at 90 degrees .
There were very small , barely palpable carotid pulses .
There was dullness at the right base , with a high diaphragm and possibly some fluid .
The cardiac examination showed a left ventricular tap at the fifth intercostal space left of the midclavicular line .
There was a grade II / VI systolic ejection murmur in the aortic area , no third sound , and paradoxical splitting of the second sound .
The liver was not palpable .
There were diminished pulses in the legs .
LABORATORY DATA :
The hemoglobin was 14.4 grams percent , white blood count 6,900 , platelet count 125,000 , sodium 137 mEq. per liter , potassium of 4.7 , BUN and creatinine of 23 and 1.3 mg percent .
The electrocardiogram showed left ventricular hypertrophy and non-specific ST-T wave changes .
The chest film showed massive cardiomegaly with pulmonary venous engorgement ."""

val result = ner_pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | chunk                |   begin |   end | ner_label   |
|---:|:---------------------|--------:|------:|:------------|
|  0 | PHYSICAL EXAMINATION |       0 |    19 | TEST        |
|  1 | physical examination |      26 |    45 | TEST        |
|  2 | blood pressure       |     107 |   120 | TEST        |
|  3 | pulse                |     135 |   139 | TEST        |
|  4 | respirations         |     146 |   157 | TEST        |
|  5 | venous pressure      |     167 |   181 | TEST        |
|  6 | pulses               |     283 |   288 | TEST        |
|  7 | cardiac examination  |     383 |   401 | TEST        |
|  8 | pulses               |     685 |   690 | TEST        |
|  9 | hemoglobin           |     728 |   737 | TEST        |
| 10 | white blood count    |     764 |   780 | TEST        |
| 11 | platelet count       |     790 |   803 | TEST        |
| 12 | sodium               |     815 |   820 | TEST        |
| 13 | mEq                  |     826 |   828 | TEST        |
| 14 | potassium            |     843 |   851 | TEST        |
| 15 | BUN                  |     862 |   864 | TEST        |
| 16 | creatinine           |     870 |   879 | TEST        |
| 17 | electrocardiogram    |     912 |   928 | TEST        |
| 18 | chest film           |    1007 |  1016 | TEST        |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_test_benchmark_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

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
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel

## Benchmarking

```bash
       label  precision    recall  f1-score   support
           O      0.995     0.996     0.996     79006
        TEST      0.914     0.897     0.906      3565
    accuracy      -         -         0.992     82571
   macro-avg      0.955     0.946     0.951     82571
weighted-avg      0.992     0.992     0.992     82571
```