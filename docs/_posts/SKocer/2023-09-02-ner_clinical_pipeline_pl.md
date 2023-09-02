---
layout: model
title: Pipeline to Detect Problem, Test and Treatment (Turkish)
author: John Snow Labs
name: ner_clinical_pipeline
date: 2023-09-02
tags: [licensed, pl, clinical, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: pl
edition: Healthcare NLP 5.0.2
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_clinical](https://nlp.johnsnowlabs.com/2023/08/29/ner_clinical_tr.html) model.

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pipeline_pl_5.0.2_3.2_1693690490759.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pipeline_pl_5.0.2_3.2_1693690490759.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_clinical_pipeline", "pl", "clinical/models")

result = ner_pipeline.annotate("""50-letnia kobieta zgłosiła się do kliniki ortopedycznej skarżąc się na uporczywy ból, obrzęk i ograniczony zakres ruchu w prawym kolanie. Pacjentka zgłosiła historię choroby zwyrodnieniowej stawów i wcześniejszy uraz kolana. Przeprowadzono badanie kliniczne i wykonano zdjęcia rentgenowskie, które wykazały zwężenie przestrzeni stawowej, tworzenie się osteofitów i oznaki zwyrodnienia chrząstki. Aby potwierdzić diagnozę i ocenić stopień zaawansowania, zlecono rezonans magnetyczny. Rezonans magnetyczny wykazał rozległą utratę chrząstki i zmiany kostne odpowiadające zaawansowanej chorobie zwyrodnieniowej stawów. Po rozważeniu stanu pacjenta i jego preferencji, omówiono plan leczenia, który obejmował kontrolę bólu, fizjoterapię i możliwość operacji wymiany stawu.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_clinical_pipeline", "pl", "clinical/models")

val result = ner_pipeline.annotate("""50-letnia kobieta zgłosiła się do kliniki ortopedycznej skarżąc się na uporczywy ból, obrzęk i ograniczony zakres ruchu w prawym kolanie. Pacjentka zgłosiła historię choroby zwyrodnieniowej stawów i wcześniejszy uraz kolana. Przeprowadzono badanie kliniczne i wykonano zdjęcia rentgenowskie, które wykazały zwężenie przestrzeni stawowej, tworzenie się osteofitów i oznaki zwyrodnienia chrząstki. Aby potwierdzić diagnozę i ocenić stopień zaawansowania, zlecono rezonans magnetyczny. Rezonans magnetyczny wykazał rozległą utratę chrząstki i zmiany kostne odpowiadające zaawansowanej chorobie zwyrodnieniowej stawów. Po rozważeniu stanu pacjenta i jego preferencji, omówiono plan leczenia, który obejmował kontrolę bólu, fizjoterapię i możliwość operacji wymiany stawu.""")

```
</div>

## Results

```bash
|    | chunks                                                                    |   begin |   end | entities   |
|---:|:--------------------------------------------------------------------------|--------:|------:|:-----------|
|  0 | uporczywy ból                                                             |      71 |    83 | PROBLEM    |
|  1 | obrzęk                                                                    |      86 |    91 | PROBLEM    |
|  2 | ograniczony zakres ruchu w prawym kolanie                                 |      95 |   135 | PROBLEM    |
|  3 | choroby zwyrodnieniowej stawów                                            |     166 |   195 | PROBLEM    |
|  4 | wcześniejszy uraz kolana                                                  |     199 |   222 | PROBLEM    |
|  5 | badanie kliniczne                                                         |     240 |   256 | TEST       |
|  6 | zdjęcia rentgenowskie                                                     |     269 |   289 | TEST       |
|  7 | zwężenie przestrzeni stawowej                                             |     307 |   335 | PROBLEM    |
|  8 | tworzenie się osteofitów                                                  |     338 |   361 | PROBLEM    |
|  9 | oznaki zwyrodnienia chrząstki                                             |     365 |   393 | PROBLEM    |
| 10 | rezonans magnetyczny                                                      |     461 |   480 | TEST       |
| 11 | Rezonans magnetyczny                                                      |     483 |   502 | TEST       |
| 12 | zmiany kostne odpowiadające zaawansowanej chorobie zwyrodnieniowej stawów |     540 |   612 | PROBLEM    |
| 13 | fizjoterapię                                                              |     719 |   730 | TREATMENT  |
| 14 | operacji wymiany stawu                                                    |     744 |   765 | TREATMENT  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|pl|
|Size:|1.2 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
