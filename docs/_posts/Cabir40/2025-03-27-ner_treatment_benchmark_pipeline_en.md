---
layout: model
title: Detect Treatment Entities (TREATMENT)
author: John Snow Labs
name: ner_treatment_benchmark_pipeline
date: 2025-03-27
tags: [licensed, clinical, en, pipeline, ner, treatment, benchmark]
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

This pipeline can be used to extract treatments mentioned in medical text.

## Predicted Entities

`TREATMENT`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_treatment_benchmark_pipeline_en_5.5.3_3.4_1743118842328.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_treatment_benchmark_pipeline_en_5.5.3_3.4_1743118842328.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_treatment_benchmark_pipeline", "en", "clinical/models")

text = """IN SUMMARY :
The patient was assessed as a 72 year old woman with a background of stage IIIC ovarian carcinoma and documented local recurrence who presents for line 2 of cycle 1 chemotherapy with Adriamycin , Ifex and MESNA .
She also has a low-grade fever of unknown etiology , has a background history of deep venous thrombosis and is therefore currently on anticoagulation and she shows evidence of dehydration and failure to thrive .
It was decided at that time to hold off with the chemotherapy .
The patient was started on Ampicillin and Gentamicin for urinary tract infection which ultimately grew out Escherichia coli sensitive to the above antibiotics and for right lower lobe pneumonia on x-ray .
She was started on nebulizers around-the-clock and chest physical therapy .
On 6/5/94 they were 21 and 2.2 respectively .
Her Coumadin anticoagulation was adjusted to give a prothrombin time between 16 and 18 and an I and R of 2.5-3 .
On June 5 , 1994 it was decided that Mrs. Neathe was not stable enough with a line 2 cycle I chemotherapy with Ifex , Adriamycin and MESNA .
She was therefore well hydrated and was started on her chemotherapy .
In view of her kidney damage it was suggested to change her intravenous antibiotics from Ancef and Gentamicin to Ancef and ciprofloxacin which she tolerated well .
A Neuro-Oncology consult was sought which felt this was probably secondary to Ifex intoxication and her chemotherapy was stopped .
An electroencephalogram was requested and was negative .
No computerized tomography scan or magnetic resonance imaging study of the head was performed .
"""

result = ner_pipeline.fullAnnotate(text)
```

{:.jsl-block}
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = nlp.PretrainedPipeline("ner_treatment_benchmark_pipeline", "en", "clinical/models")

text = """IN SUMMARY :
The patient was assessed as a 72 year old woman with a background of stage IIIC ovarian carcinoma and documented local recurrence who presents for line 2 of cycle 1 chemotherapy with Adriamycin , Ifex and MESNA .
She also has a low-grade fever of unknown etiology , has a background history of deep venous thrombosis and is therefore currently on anticoagulation and she shows evidence of dehydration and failure to thrive .
It was decided at that time to hold off with the chemotherapy .
The patient was started on Ampicillin and Gentamicin for urinary tract infection which ultimately grew out Escherichia coli sensitive to the above antibiotics and for right lower lobe pneumonia on x-ray .
She was started on nebulizers around-the-clock and chest physical therapy .
On 6/5/94 they were 21 and 2.2 respectively .
Her Coumadin anticoagulation was adjusted to give a prothrombin time between 16 and 18 and an I and R of 2.5-3 .
On June 5 , 1994 it was decided that Mrs. Neathe was not stable enough with a line 2 cycle I chemotherapy with Ifex , Adriamycin and MESNA .
She was therefore well hydrated and was started on her chemotherapy .
In view of her kidney damage it was suggested to change her intravenous antibiotics from Ancef and Gentamicin to Ancef and ciprofloxacin which she tolerated well .
A Neuro-Oncology consult was sought which felt this was probably secondary to Ifex intoxication and her chemotherapy was stopped .
An electroencephalogram was requested and was negative .
No computerized tomography scan or magnetic resonance imaging study of the head was performed .
"""

result = ner_pipeline.fullAnnotate(text)
```

```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_treatment_benchmark_pipeline", "en", "clinical/models")

val text = """IN SUMMARY :
The patient was assessed as a 72 year old woman with a background of stage IIIC ovarian carcinoma and documented local recurrence who presents for line 2 of cycle 1 chemotherapy with Adriamycin , Ifex and MESNA .
She also has a low-grade fever of unknown etiology , has a background history of deep venous thrombosis and is therefore currently on anticoagulation and she shows evidence of dehydration and failure to thrive .
It was decided at that time to hold off with the chemotherapy .
The patient was started on Ampicillin and Gentamicin for urinary tract infection which ultimately grew out Escherichia coli sensitive to the above antibiotics and for right lower lobe pneumonia on x-ray .
She was started on nebulizers around-the-clock and chest physical therapy .
On 6/5/94 they were 21 and 2.2 respectively .
Her Coumadin anticoagulation was adjusted to give a prothrombin time between 16 and 18 and an I and R of 2.5-3 .
On June 5 , 1994 it was decided that Mrs. Neathe was not stable enough with a line 2 cycle I chemotherapy with Ifex , Adriamycin and MESNA .
She was therefore well hydrated and was started on her chemotherapy .
In view of her kidney damage it was suggested to change her intravenous antibiotics from Ancef and Gentamicin to Ancef and ciprofloxacin which she tolerated well .
A Neuro-Oncology consult was sought which felt this was probably secondary to Ifex intoxication and her chemotherapy was stopped .
An electroencephalogram was requested and was negative .
No computerized tomography scan or magnetic resonance imaging study of the head was performed .
"""

val result = ner_pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | chunk            |   begin |   end | ner_label   |
|---:|:-----------------|--------:|------:|:------------|
|  0 | chemotherapy     |     178 |   189 | TREATMENT   |
|  1 | anticoagulation  |     360 |   374 | TREATMENT   |
|  2 | chemotherapy     |     487 |   498 | TREATMENT   |
|  3 | antibiotics      |     649 |   659 | TREATMENT   |
|  4 | nebulizers       |     726 |   735 | TREATMENT   |
|  5 | physical therapy |     764 |   779 | TREATMENT   |
|  6 | anticoagulation  |     842 |   856 | TREATMENT   |
|  7 | chemotherapy     |    1035 |  1046 | TREATMENT   |
|  8 | chemotherapy     |    1138 |  1149 | TREATMENT   |
|  9 | antibiotics      |    1225 |  1235 | TREATMENT   |
| 10 | chemotherapy     |    1421 |  1432 | TREATMENT   |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_treatment_benchmark_pipeline|
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
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel

## Benchmarking

```bash
       label  precision    recall  f1-score   support
           O      0.999     0.999     0.999     82021
   TREATMENT      0.900     0.918     0.909       550
    accuracy      -         -         0.999     82571
   macro-avg      0.950     0.959     0.954     82571
weighted-avg      0.999     0.999     0.999     82571
```