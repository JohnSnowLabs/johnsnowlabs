---
layout: model
title: Pipeline to Detect Posology concepts (langtest)
author: John Snow Labs
name: ner_posology_langtest_pipeline
date: 2023-09-08
tags: [licensed, en, posology, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_posology_langtest](https://nlp.johnsnowlabs.com/2023/07/28/ner_posology_langtest_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_posology_langtest_pipeline_en_5.1.0_3.0_1694192086248.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_posology_langtest_pipeline_en_5.1.0_3.0_1694192086248.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_posology_langtest_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient is a 30-year-old female with a long history of insulin dependent diabetes, type 2; coronary artery disease; chronic renal insufficiency; peripheral vascular disease, also secondary to diabetes; who was originally admitted to an outside hospital for what appeared to be acute paraplegia, lower extremities. She did receive a course of Bactrim for 14 days for UTI. Evidently, at some point in time, the patient was noted to develop a pressure-type wound on the sole of her left foot and left great toe. She was also noted to have a large sacral wound; this is in a similar location with her previous laminectomy, and this continues to receive daily care. The patient was transferred secondary to inability to participate in full physical and occupational therapy and continue medical management of her diabetes, the sacral decubitus, left foot pressure wound, and associated complications of diabetes. She is given Fragmin 5000 units subcutaneously daily, Xenaderm to wounds topically b.i.d., Lantus 40 units subcutaneously at bedtime, OxyContin 30 mg p.o. q.12 h., folic acid 1 mg daily, levothyroxine 0.1 mg p.o. daily, Prevacid 30 mg daily, Avandia 4 mg daily, Norvasc 10 mg daily, Lexapro 20 mg daily, aspirin 81 mg daily, Senna 2 tablets p.o. q.a.m., Neurontin 400 mg p.o. t.i.d., Percocet 5/325 mg 2 tablets q.4 h. p.r.n., magnesium citrate 1 bottle p.o. p.r.n., sliding scale coverage insulin, Wellbutrin 100 mg p.o. daily, and Bactrim DS b.i.d.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_posology_langtest_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient is a 30-year-old female with a long history of insulin dependent diabetes, type 2; coronary artery disease; chronic renal insufficiency; peripheral vascular disease, also secondary to diabetes; who was originally admitted to an outside hospital for what appeared to be acute paraplegia, lower extremities. She did receive a course of Bactrim for 14 days for UTI. Evidently, at some point in time, the patient was noted to develop a pressure-type wound on the sole of her left foot and left great toe. She was also noted to have a large sacral wound; this is in a similar location with her previous laminectomy, and this continues to receive daily care. The patient was transferred secondary to inability to participate in full physical and occupational therapy and continue medical management of her diabetes, the sacral decubitus, left foot pressure wound, and associated complications of diabetes. She is given Fragmin 5000 units subcutaneously daily, Xenaderm to wounds topically b.i.d., Lantus 40 units subcutaneously at bedtime, OxyContin 30 mg p.o. q.12 h., folic acid 1 mg daily, levothyroxine 0.1 mg p.o. daily, Prevacid 30 mg daily, Avandia 4 mg daily, Norvasc 10 mg daily, Lexapro 20 mg daily, aspirin 81 mg daily, Senna 2 tablets p.o. q.a.m., Neurontin 400 mg p.o. t.i.d., Percocet 5/325 mg 2 tablets q.4 h. p.r.n., magnesium citrate 1 bottle p.o. p.r.n., sliding scale coverage insulin, Wellbutrin 100 mg p.o. daily, and Bactrim DS b.i.d.""")

```
</div>

## Results

```bash
|    | chunks            |   begin |   end | entities   |
|---:|:------------------|--------:|------:|:-----------|
|  0 | insulin           |      59 |    65 | DRUG       |
|  1 | Bactrim           |     346 |   352 | DRUG       |
|  2 | for 14 days       |     354 |   364 | DURATION   |
|  3 | Fragmin           |     925 |   931 | DRUG       |
|  4 | 5000 units        |     933 |   942 | DOSAGE     |
|  5 | subcutaneously    |     944 |   957 | ROUTE      |
|  6 | daily             |     959 |   963 | FREQUENCY  |
|  7 | topically         |     985 |   993 | ROUTE      |
|  8 | b.i.d             |     995 |   999 | FREQUENCY  |
|  9 | Lantus            |    1003 |  1008 | DRUG       |
| 10 | 40 units          |    1010 |  1017 | DOSAGE     |
| 11 | subcutaneously    |    1019 |  1032 | ROUTE      |
| 12 | at bedtime        |    1034 |  1043 | FREQUENCY  |
| 13 | OxyContin         |    1046 |  1054 | DRUG       |
| 14 | 30 mg             |    1056 |  1060 | STRENGTH   |
| 15 | p.o               |    1062 |  1064 | ROUTE      |
| 16 | q.12 h            |    1067 |  1072 | FREQUENCY  |
| 17 | folic acid        |    1076 |  1085 | DRUG       |
| 18 | 1 mg              |    1087 |  1090 | STRENGTH   |
| 19 | daily             |    1092 |  1096 | FREQUENCY  |
| 20 | levothyroxine     |    1099 |  1111 | DRUG       |
| 21 | 0.1 mg            |    1113 |  1118 | STRENGTH   |
| 22 | p.o               |    1120 |  1122 | ROUTE      |
| 23 | daily             |    1125 |  1129 | FREQUENCY  |
| 24 | Prevacid          |    1132 |  1139 | DRUG       |
| 25 | 30 mg             |    1141 |  1145 | STRENGTH   |
| 26 | daily             |    1147 |  1151 | FREQUENCY  |
| 27 | 4 mg              |    1162 |  1165 | STRENGTH   |
| 28 | daily             |    1167 |  1171 | FREQUENCY  |
| 29 | Norvasc           |    1174 |  1180 | DRUG       |
| 30 | 10 mg             |    1182 |  1186 | STRENGTH   |
| 31 | daily             |    1188 |  1192 | FREQUENCY  |
| 32 | Lexapro           |    1195 |  1201 | DRUG       |
| 33 | 20 mg             |    1203 |  1207 | STRENGTH   |
| 34 | daily             |    1209 |  1213 | FREQUENCY  |
| 35 | aspirin           |    1216 |  1222 | DRUG       |
| 36 | 81 mg             |    1224 |  1228 | STRENGTH   |
| 37 | daily             |    1230 |  1234 | FREQUENCY  |
| 38 | Senna             |    1237 |  1241 | DRUG       |
| 39 | 2                 |    1243 |  1243 | DOSAGE     |
| 40 | tablets           |    1245 |  1251 | FORM       |
| 41 | p.o               |    1253 |  1255 | ROUTE      |
| 42 | q                 |    1258 |  1258 | FREQUENCY  |
| 43 | Neurontin         |    1266 |  1274 | DRUG       |
| 44 | 400 mg            |    1276 |  1281 | STRENGTH   |
| 45 | p.o               |    1283 |  1285 | ROUTE      |
| 46 | t.i.d             |    1288 |  1292 | FREQUENCY  |
| 47 | Percocet          |    1296 |  1303 | DRUG       |
| 48 | 5/325 mg          |    1305 |  1312 | STRENGTH   |
| 49 | 2                 |    1314 |  1314 | DOSAGE     |
| 50 | tablets           |    1316 |  1322 | FORM       |
| 51 | q.4 h             |    1324 |  1328 | FREQUENCY  |
| 52 | magnesium citrate |    1339 |  1355 | DRUG       |
| 53 | 1                 |    1357 |  1357 | DOSAGE     |
| 54 | bottle            |    1359 |  1364 | FORM       |
| 55 | p.o               |    1366 |  1368 | ROUTE      |
| 56 | insulin           |    1402 |  1408 | DRUG       |
| 57 | Wellbutrin        |    1411 |  1420 | DRUG       |
| 58 | 100 mg            |    1422 |  1427 | STRENGTH   |
| 59 | p.o               |    1429 |  1431 | ROUTE      |
| 60 | daily             |    1434 |  1438 | FREQUENCY  |
| 61 | Bactrim DS        |    1445 |  1454 | DRUG       |
| 62 | b.i.d             |    1456 |  1460 | FREQUENCY  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_posology_langtest_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.1.0+|
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