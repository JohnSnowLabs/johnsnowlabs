---
layout: model
title: Detect Anatomical Structures (BODY_PART)
author: John Snow Labs
name: ner_body_part_benchmark_pipeline
date: 2025-03-27
tags: [licensed, clinical, en, pipeline, ner, body_part, benchmark]
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

This pipeline can be used to extract all types of anatomical references in medical text. It is a single-entity pipeline and generalizes all anatomical references to a single entity.

## Predicted Entities

`BODY_PART`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_body_part_benchmark_pipeline_en_5.5.3_3.4_1743111176684.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_body_part_benchmark_pipeline_en_5.5.3_3.4_1743111176684.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_body_part_benchmark_pipeline", "en", "clinical/models")

text = """HISTORY OF PRESENT ILLNESS :
Mr. He is a 77 year old male with squamous cell carcinoma of the lung .
The initial presentation was the orifice of the right upper lobe with mediastinoscopy positive for subcarinal lymph node .
He received 6,000 rads to his mediastinum with external beam .
Subsequently , he returned to Goo where he received another 3,000 rads via an endobronchial catheter , apparently due to recurrence .
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
Ultimately , only codeine at 30 mg q6h controlled him and this was very affective .
Inhalers provide only mild relief .
He is aware of his prognosis .
The patient was also seen by Dr. Lenchermoi Fyfesaul of the Oncology Service who did not feel that chemotherapy had anything of promise to offer .
Mr. He is an anxious man , but very pleasant .
He and his family understand his prognosis ."""

result = ner_pipeline.fullAnnotate(text)
```

{:.jsl-block}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = nlp.PretrainedPipeline("ner_body_part_benchmark_pipeline", "en", "clinical/models")

text = """HISTORY OF PRESENT ILLNESS :
Mr. He is a 77 year old male with squamous cell carcinoma of the lung .
The initial presentation was the orifice of the right upper lobe with mediastinoscopy positive for subcarinal lymph node .
He received 6,000 rads to his mediastinum with external beam .
Subsequently , he returned to Goo where he received another 3,000 rads via an endobronchial catheter , apparently due to recurrence .
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
Ultimately , only codeine at 30 mg q6h controlled him and this was very affective .
Inhalers provide only mild relief .
He is aware of his prognosis .
The patient was also seen by Dr. Lenchermoi Fyfesaul of the Oncology Service who did not feel that chemotherapy had anything of promise to offer .
Mr. He is an anxious man , but very pleasant .
He and his family understand his prognosis ."""

result = ner_pipeline.fullAnnotate(text)
```

```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_body_part_benchmark_pipeline", "en", "clinical/models")

val text = """HISTORY OF PRESENT ILLNESS :
Mr. He is a 77 year old male with squamous cell carcinoma of the lung .
The initial presentation was the orifice of the right upper lobe with mediastinoscopy positive for subcarinal lymph node .
He received 6,000 rads to his mediastinum with external beam .
Subsequently , he returned to Goo where he received another 3,000 rads via an endobronchial catheter , apparently due to recurrence .
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
Ultimately , only codeine at 30 mg q6h controlled him and this was very affective .
Inhalers provide only mild relief .
He is aware of his prognosis .
The patient was also seen by Dr. Lenchermoi Fyfesaul of the Oncology Service who did not feel that chemotherapy had anything of promise to offer .
Mr. He is an anxious man , but very pleasant .
He and his family understand his prognosis ."""

val result = ner_pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | chunk                 |   begin |   end | ner_label   |   confidence |
|---:|:----------------------|--------:|------:|:------------|-------------:|
|  0 | lung                  |      94 |    97 | BODY_PART   |     0.919    |
|  1 | upper lobe            |     155 |   164 | BODY_PART   |     0.41695  |
|  2 | subcarinal lymph node |     200 |   220 | BODY_PART   |     0.542533 |
|  3 | mediastinum           |     254 |   264 | BODY_PART   |     0.9389   |
|  4 | main stem bronchus    |     574 |   591 | BODY_PART   |     0.631967 |
|  5 | subcarinal            |     724 |   733 | BODY_PART   |     0.9834   |
|  6 | bladder               |     820 |   826 | BODY_PART   |     0.9283   |
|  7 | nodes                 |     967 |   971 | BODY_PART   |     0.6176   |
|  8 | lung fields           |    1038 |  1048 | BODY_PART   |     0.5019   |
|  9 | airway                |    1332 |  1337 | BODY_PART   |     0.552    |
| 10 | trachea               |    1413 |  1419 | BODY_PART   |     0.9391   |
| 11 | main bronchus         |    1442 |  1454 | BODY_PART   |     0.55815  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_body_part_benchmark_pipeline|
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
- TextMatcherInternalModel
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
   BODY_PART      0.777     0.895     0.832      2049
           O      0.997     0.993     0.995     80522
    accuracy      -         -         0.991     82571
   macro-avg      0.887     0.944     0.914     82571
weighted-avg      0.992     0.991     0.991     82571
```
