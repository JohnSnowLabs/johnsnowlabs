---
layout: model
title: Pipeline to Detect Problem, Test and Treatment (Dutch)
author: John Snow Labs
name: ner_clinical_pipeline
date: 2023-09-02
tags: [licensed, nl, clinical, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: nl
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pipeline_nl_5.0.2_3.2_1693693120717.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pipeline_nl_5.0.2_3.2_1693693120717.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_clinical_pipeline", "nl", "clinical/models")

result = ner_pipeline.annotate("""Een 50-jarige vrouw kwam naar de orthopedische polikliniek met klachten van aanhoudende pijn, zwelling en bewegingsbeperking in haar rechterknie. Ze meldde een voorgeschiedenis van artrose en eerder knieletsel. Klinisch onderzoek en röntgenfoto's toonden vernauwing van de gewrichtsruimte, osteofytvorming en kraakbeendegeneratie. Er werd een MRI-scan besteld om de diagnose te bevestigen en de ernst ervan te beoordelen. De MRI toonde uitgebreid kraakbeenverlies en botveranderingen die overeenkwamen met gevorderde artrose. Na afweging van de toestand en voorkeuren van de patiënt werd een behandelplan met fysiotherapie en de mogelijkheid van een gewrichtsvervangende operatie besproken.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_clinical_pipeline", "nl", "clinical/models")

val result = ner_pipeline.annotate("""Een 50-jarige vrouw kwam naar de orthopedische polikliniek met klachten van aanhoudende pijn, zwelling en bewegingsbeperking in haar rechterknie. Ze meldde een voorgeschiedenis van artrose en eerder knieletsel. Klinisch onderzoek en röntgenfoto's toonden vernauwing van de gewrichtsruimte, osteofytvorming en kraakbeendegeneratie. Er werd een MRI-scan besteld om de diagnose te bevestigen en de ernst ervan te beoordelen. De MRI toonde uitgebreid kraakbeenverlies en botveranderingen die overeenkwamen met gevorderde artrose. Na afweging van de toestand en voorkeuren van de patiënt werd een behandelplan met fysiotherapie en de mogelijkheid van een gewrichtsvervangende operatie besproken.""")

```
</div>

## Results

```bash
|    | chunks                                 |   begin |   end | entities   |
|---:|:---------------------------------------|--------:|------:|:-----------|
|  0 | aanhoudende pijn                       |      76 |    91 | PROBLEM    |
|  1 | zwelling                               |      94 |   101 | PROBLEM    |
|  2 | bewegingsbeperking in haar rechterknie |     106 |   143 | PROBLEM    |
|  3 | artrose                                |     181 |   187 | PROBLEM    |
|  4 | knieletsel                             |     199 |   208 | PROBLEM    |
|  5 | Klinisch onderzoek                     |     211 |   228 | TEST       |
|  6 | röntgenfoto's                          |     233 |   245 | TEST       |
|  7 | vernauwing van de gewrichtsruimte      |     255 |   287 | PROBLEM    |
|  8 | osteofytvorming                        |     290 |   304 | PROBLEM    |
|  9 | kraakbeendegeneratie                   |     309 |   328 | PROBLEM    |
| 10 | een MRI-scan                           |     339 |   350 | TEST       |
| 11 | De MRI                                 |     422 |   427 | TEST       |
| 12 | uitgebreid kraakbeenverlies            |     436 |   462 | PROBLEM    |
| 13 | botveranderingen                       |     467 |   482 | PROBLEM    |
| 14 | gevorderde artrose                     |     506 |   523 | PROBLEM    |
| 15 | een behandelplan                       |     588 |   603 | TREATMENT  |
| 16 | fysiotherapie                          |     609 |   621 | TREATMENT  |
| 17 | een gewrichtsvervangende operatie      |     646 |   678 | TREATMENT  |
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
|Language:|nl|
|Size:|1.2 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
