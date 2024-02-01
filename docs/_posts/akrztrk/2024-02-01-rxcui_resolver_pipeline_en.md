---
layout: model
title: Pipeline for RxNorm Concept Unique Identifier (RxCUI) Sentence Entity Resolver
author: John Snow Labs
name: rxcui_resolver_pipeline
date: 2024-02-01
tags: [licensed, en, entity_resolution, clinical, pipeline, rxcui]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This advanced pipeline extracts medical entities from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding RxNorm Concept Unique Identifier (RxCUI) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxcui_resolver_pipeline_en_5.2.1_3.4_1706796279531.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxcui_resolver_pipeline_en_5.2.1_3.4_1706796279531.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("rxcui_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""He was seen by the endocrinology service and she was discharged on 50 mg of eltrombopag oral at night, 5 mg amlodipine with meals, and metformin 1000 mg two times a day.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("rxcui_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""He was seen by the endocrinology service and she was discharged on 50 mg of eltrombopag oral at night, 5 mg amlodipine with meals, and metformin 1000 mg two times a day.""")

```
</div>

## Results

```bash
|    | chunks                    |   begin |   end | entities   |   Code | description                                 | resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | all_codes                                                                                                                                                                                                                                       |
|---:|:--------------------------|--------:|------:|:-----------|-------:|:--------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | 50 mg of eltrombopag oral |      67 |    91 | DRUG       | 825427 | eltrombopag 50 MG Oral Tablet               | eltrombopag 50 MG Oral Tablet:::alpelisib 50 MG Oral Tablet:::encorafenib 50 MG Oral Capsule:::alteplase 50 MG Injection [Activase]:::enasidenib 50 MG Oral Tablet:::olaparib 50 MG Oral Capsule:::encorafenib 50 MG Oral Capsule [Braftovi]:::alteplase 50 MG Injection:::olaparib 50 MG Oral Capsule [Lynparza]:::ivacaftor 50 MG Oral Granules:::dolasetron 50 MG Oral Tablet:::enasidenib 50 MG Oral Tablet [Idhifa]:::ubrogepant 50 MG Oral Tablet:::lasmiditan 50 MG Oral Tablet:::altretamine 50 MG Oral Capsule:::pamabrom 50 MG Oral Capsule:::dolasetron 50 MG Oral Tablet [Anzemet]:::venetoclax 50 MG Oral Tablet:::cangrelor 50 MG Injection:::tucatinib 50 MG Oral Tablet:::venlafaxine 50 MG Oral Tablet:::dabrafenib 50 MG Oral Capsule:::lasmiditan 50 MG Oral Tablet [Reyvow]:::armodafinil 50 MG Oral Tablet [Nuvigil]:::prasterone 50 MG Oral Capsule              | 825427:::2169316:::2049111:::1804806:::1940374:::1597587:::2049117:::1804804:::1597593:::1606862:::310007:::1940376:::2268229:::2256945:::197323:::832080:::213091:::1747574:::1656056:::2361298:::314277:::1424916:::2256947:::805663:::242339 |
|  1 | 5 mg amlodipine           |     103 |   117 | DRUG       | 197361 | amlodipine 5 MG Oral Tablet                 | amlodipine 5 MG Oral Tablet:::levamlodipine 5 MG Oral Tablet:::nebivolol 5 MG Oral Tablet:::amlodipine 5 MG Oral Tablet [Norvasc]:::lisinopril 5 MG Oral Tablet:::levamlodipine 5 MG Oral Tablet [Conjupri]:::aripiprazole 5 MG Oral Tablet:::haloperidol 5 MG Oral Tablet:::amlodipine 2.5 MG Oral Tablet:::timolol 5 MG Oral Tablet:::escitalopram 5 MG Oral Tablet:::ramipril 5 MG Oral Tablet:::aripiprazole 5 MG Oral Tablet [Abilify]:::pindolol 5 MG Oral Tablet:::loxapine 5 MG Oral Capsule:::tadalafil 5 MG Oral Tablet:::Sensor aripiprazole 5 MG Oral Tablet:::prasugrel 5 MG Oral Tablet:::haloperidol 5 MG/ML Injectable Solution:::ramipril 5 MG Oral Capsule:::ivabradine 5 MG Oral Tablet:::asenapine 5 MG Sublingual Tablet:::lomitapide 5 MG Oral Capsule [Juxtapid]:::levamlodipine 2.5 MG Oral Tablet:::dronabinol 5 MG/ML Oral Solution                          | 197361:::2377371:::387013:::212549:::311354:::2377373:::402131:::310672:::308136:::198286:::351249:::251857:::404602:::198105:::311386:::403957:::1998462:::855818:::204416:::198189:::1649485:::859981:::1364498:::2377367:::1928948           |
|  2 | metformin 1000 mg         |     135 |   151 | DRUG       | 861004 | metformin hydrochloride 1000 MG Oral Tablet | metformin hydrochloride 1000 MG Oral Tablet:::cefepime 1000 MG Injection:::ifosfamide 1000 MG Injection:::methotrexate 1000 MG Injection:::cefazolin 1000 MG Injection:::cefotetan 1000 MG Injection:::taurine 1000 MG Oral Capsule:::cefoxitin 1000 MG Injection:::nafcillin 1000 MG Injection:::ertapenem 1000 MG Injection:::ampicillin 1000 MG Injection:::cefiderocol 1000 MG Injection:::aztreonam 1000 MG Injection:::ifosfamide 1000 MG Injection [Ifex]:::arginine 1000 MG Oral Tablet:::pralidoxime chloride 1000 MG Injection:::sucralfate 1000 MG Oral Tablet:::metformin hydrochloride 1000 MG Oral Tablet [Glucophage]:::cefotaxime 1000 MG Injection:::streptozocin 1000 MG Injection:::ceftazidime 1000 MG Injection:::gemcitabine 1000 MG Injection:::ertapenem 1000 MG Injection [Invanz]:::meropenem 1000 MG Injection:::methylsulfonylmethane 1000 MG Oral Capsule | 861004:::1665093:::1791593:::311625:::1665050:::1722919:::847074:::1665102:::1721458:::1734683:::1721475:::2265706:::1664981:::1791595:::636337:::312576:::314234:::861006:::1656313:::239180:::1659283:::1719003:::1734686:::1722939:::259239  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxcui_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel