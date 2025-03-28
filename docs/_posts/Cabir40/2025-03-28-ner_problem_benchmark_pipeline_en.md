---
layout: model
title: Detect Problem Entities (PROBLEM)
author: John Snow Labs
name: ner_problem_benchmark_pipeline
date: 2025-03-28
tags: [licensed, clinical, en, pipeline, ner, problem, benchmark]
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

This pipeline can be used to extracts `problem` (diseases, disorders, injuries, symptoms, signs .etc) information in medical text.

## Predicted Entities

`PROBLEM`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_problem_benchmark_pipeline_en_5.5.3_3.4_1743125114956.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_problem_benchmark_pipeline_en_5.5.3_3.4_1743125114956.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_problem_benchmark_pipeline", "en", "clinical/models")

text = """HISTORY OF PRESENT ILLNESS :
Mr. He is a 77 year old male with squamous cell carcinoma of the lung .
Over the pat three to four weeks , he started having increased dyspnea and noted wheezing .
A bronchoscopy showed protrusion of the tumor into the right main stem bronchus with a positive needle biopsy , washings and brushings for squamous cell carcinoma .
A computerized tomography scan showed a large subcarinal mass .
PAST MEDICAL HISTORY :
His past medical history was significant for malignant bladder tumor in 1991 .
PHYSICAL EXAMINATION :
On physical examination , Mr. He had very marked inspiratory and expiratory stridor .
There were no nodes present .
The breath sounds were somewhat decreased through both lung fields .
His cardiac examination did not show any murmur , gallop , or cardiomegaly .
There was no hepatosplenomegaly , and no peripheral edema .
HOSPITAL COURSE :
A bronchoscopy with the intention of coring out tumor was carried out by Dr. Reg He , but all the tumor was extrinsic to the airway and he was unable to relieve the obstruction .
The tumor now involves the trachea as well as the right main bronchus .
His major complaint was of persistent severe coughing and secretions .
"""

result = ner_pipeline.fullAnnotate(text)
```

{:.jsl-block}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = nlp.PretrainedPipeline("ner_problem_benchmark_pipeline", "en", "clinical/models")

text = """HISTORY OF PRESENT ILLNESS :
Mr. He is a 77 year old male with squamous cell carcinoma of the lung .
Over the pat three to four weeks , he started having increased dyspnea and noted wheezing .
A bronchoscopy showed protrusion of the tumor into the right main stem bronchus with a positive needle biopsy , washings and brushings for squamous cell carcinoma .
A computerized tomography scan showed a large subcarinal mass .
PAST MEDICAL HISTORY :
His past medical history was significant for malignant bladder tumor in 1991 .
PHYSICAL EXAMINATION :
On physical examination , Mr. He had very marked inspiratory and expiratory stridor .
There were no nodes present .
The breath sounds were somewhat decreased through both lung fields .
His cardiac examination did not show any murmur , gallop , or cardiomegaly .
There was no hepatosplenomegaly , and no peripheral edema .
HOSPITAL COURSE :
A bronchoscopy with the intention of coring out tumor was carried out by Dr. Reg He , but all the tumor was extrinsic to the airway and he was unable to relieve the obstruction .
The tumor now involves the trachea as well as the right main bronchus .
His major complaint was of persistent severe coughing and secretions .
"""

result = ner_pipeline.fullAnnotate(text)
```

```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_problem_benchmark_pipeline", "en", "clinical/models")

val text = """HISTORY OF PRESENT ILLNESS :
Mr. He is a 77 year old male with squamous cell carcinoma of the lung .
Over the pat three to four weeks , he started having increased dyspnea and noted wheezing .
A bronchoscopy showed protrusion of the tumor into the right main stem bronchus with a positive needle biopsy , washings and brushings for squamous cell carcinoma .
A computerized tomography scan showed a large subcarinal mass .
PAST MEDICAL HISTORY :
His past medical history was significant for malignant bladder tumor in 1991 .
PHYSICAL EXAMINATION :
On physical examination , Mr. He had very marked inspiratory and expiratory stridor .
There were no nodes present .
The breath sounds were somewhat decreased through both lung fields .
His cardiac examination did not show any murmur , gallop , or cardiomegaly .
There was no hepatosplenomegaly , and no peripheral edema .
HOSPITAL COURSE :
A bronchoscopy with the intention of coring out tumor was carried out by Dr. Reg He , but all the tumor was extrinsic to the airway and he was unable to relieve the obstruction .
The tumor now involves the trachea as well as the right main bronchus .
His major complaint was of persistent severe coughing and secretions .
"""

val result = ner_pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | chunk                   |   begin |   end | ner_label   |
|---:|:------------------------|--------:|------:|:------------|
|  0 | squamous cell carcinoma |      63 |    85 | PROBLEM     |
|  1 | dyspnea                 |     164 |   170 | PROBLEM     |
|  2 | wheezing                |     182 |   189 | PROBLEM     |
|  3 | tumor                   |     233 |   237 | PROBLEM     |
|  4 | squamous cell carcinoma |     332 |   354 | PROBLEM     |
|  5 | mass                    |     415 |   418 | PROBLEM     |
|  6 | malignant bladder tumor |     490 |   512 | PROBLEM     |
|  7 | murmur                  |     773 |   778 | PROBLEM     |
|  8 | cardiomegaly            |     794 |   805 | PROBLEM     |
|  9 | hepatosplenomegaly      |     822 |   839 | PROBLEM     |
| 10 | peripheral edema        |     850 |   865 | PROBLEM     |
| 11 | tumor                   |     935 |   939 | PROBLEM     |
| 12 | tumor                   |     985 |   989 | PROBLEM     |
| 13 | obstruction             |    1052 |  1062 | PROBLEM     |
| 14 | tumor                   |    1070 |  1074 | PROBLEM     |
| 15 | coughing                |    1183 |  1190 | PROBLEM     |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_problem_benchmark_pipeline|
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
           O      0.989     0.996     0.993     76426
     PROBLEM      0.948     0.866     0.905      6145
    accuracy      -         -         0.986     82571
   macro-avg      0.969     0.931     0.949     82571
weighted-avg      0.986     0.986     0.986     82571
```