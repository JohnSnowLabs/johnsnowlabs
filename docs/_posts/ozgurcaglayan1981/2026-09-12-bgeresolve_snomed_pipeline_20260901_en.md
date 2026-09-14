---
layout: model
title: Sentence Entity Resolver for SNOMED CT (All Concepts) (bge_base_en_v1_5_onnx embeddings) - Pipeline
author: John Snow Labs
name: bgeresolve_snomed_pipeline_20260901
date: 2026-09-12
tags: [en, entity_resolution, licensed, clinical, snomed, pipeline, bge, general]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts clinical entities from text and maps them to the full, domain-unrestricted set of active SNOMED CT concepts using `bge_base_en_v1_5_onnx` embeddings.

Wraps the `bgeresolve_snomed_20260901` resolver, trained on SNOMED CT US Edition 20260901.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_snomed_pipeline_20260901_en_6.4.1_3.4_1789233283259.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_snomed_pipeline_20260901_en_6.4.1_3.4_1789233283259.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("bgeresolve_snomed_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient with inflammatory bowel disease presented with dyspnea and abdominal pain. She underwent a laparoscopic appendectomy and was started on aspirin."]]).toDF("text")
result = snomed_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

snomed_pipeline = nlp.PretrainedPipeline("bgeresolve_snomed_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient with inflammatory bowel disease presented with dyspnea and abdominal pain. She underwent a laparoscopic appendectomy and was started on aspirin."]]).toDF("text")
result = snomed_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("bgeresolve_snomed_pipeline_20260901", "en", "clinical/models")

val data = Seq("The patient with inflammatory bowel disease presented with dyspnea and abdominal pain. She underwent a laparoscopic appendectomy and was started on aspirin.").toDF("text")
val result = snomed_pipeline.transform(data)

```
</div>

## Results

```bash
| chunk                      | label                     |   snomed_code | resolution                 | all_codes                                                                                                                                                                                                                                                    | all_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:---------------------------|:--------------------------|--------------:|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| inflammatory bowel disease | Disease_Syndrome_Disorder |      24526004 | inflammatory bowel disease | 24526004:::34000006:::1197732001:::397173003:::397172008:::700104004:::9281000146109:::128999004:::50440006:::6382002:::64766004:::64226004:::608844008:::373407002:::128139000:::7620006:::95544006:::1187638005                                            | inflammatory bowel disease:::crohns disease:::colorectal crohn disease:::crohn disease of intestine:::gastrointestinal crohn disease:::management of inflammatory bowel disease:::inflammatory bowel disease suspected:::inflammatory disorder of digestive tract:::crohn disease of colon:::chronic inflammatory small bowel disease:::ulcerative colitis:::colitis:::history of inflammatory bowel disease:::inflammatory disorder of digestive system:::inflammatory disease:::crohn disease of large bowel:::inflammatory diarrhea:::inflammation of intestine     |
| dyspnea                    | Symptom                   |     267036007 | dyspnea                    | 267036007:::719415004:::34560001:::25209001:::870535009:::60845006:::161938003:::161940008:::719413006:::161939006:::161941007:::422177004:::390871002:::59265000:::248548009                                                                                | dyspnea:::dyspnea care:::expiratory dyspnea:::inspiratory dyspnea:::chronic dyspnea:::dyspnea on exertion:::dyspnea absent:::dyspnea on mild exertion:::dyspnea care management:::dyspnea on moderate exertion:::dyspnea at rest:::dyspnea with acquired immunodeficiency syndrome:::dyspnea on strenuous exertion:::paroxysmal dyspnea:::nocturnal dyspnea                                                                                                                                                                                                            |
| abdominal pain             | Symptom                   |      21522001 | abdominal pain             | 21522001:::271681002:::43364001:::43478001:::116290004:::162042000:::54586004:::438506002:::247358007:::28221000119103:::1332010007:::9991008:::83132003:::102614006:::51197009:::364630006:::309737007:::102613000:::247362001:::162046002                  | abdominal pain:::stomach pain:::abdominal discomfort:::abdominal tenderness:::acute abdominal pain:::abdominal wall pain:::lower abdominal pain:::visceral abdominal pain:::type of abdominal pain:::abdominal muscle pain:::site of abdominal pain:::colicky abdominal pain:::upper abdominal pain:::generalized abdominal pain:::stomach cramps:::abdominal pain characteristic:::abdominal pain in pregnancy:::localized abdominal pain:::pain on abdominal wall movement:::central abdominal pain                                                                  |
| laparoscopic appendectomy  | Procedure                 |       6025007 | laparoscopic appendectomy  | 6025007:::80146002:::174041007:::1156321000:::307581005:::17041004:::49586007:::708876004:::174036004:::8613002:::428251008:::1220549001                                                                                                                     | laparoscopic appendectomy:::appendectomy:::laparoscopic emergency appendectomy:::history of laparoscopic appendectomy:::laparoscopic interval appendectomy:::appendicotomy:::appendicocecostomy:::laparoscopic appendectomy using robotic assistance:::emergency appendectomy:::appendix operation:::history of appendectomy:::laparoscopic ileectomy                                                                                                                                                                                                                  |
| aspirin                    | Drug_Ingredient           |     387458008 | aspirin                    | 387458008:::432909005:::135800003:::25796002:::717854002:::312452009:::7947003:::293586001:::431463004:::417980006:::292044008:::315045009:::774656009:::405742008:::418194009:::426365001:::412569008:::319796006:::424102008:::405748007:::131531000119103 | aspirin:::aspirin given:::aspirin indicated:::aluminium aspirin:::aspirin therapy:::aspirin prophylaxis:::aspirin-containing product:::aspirin allergy:::administration of aspirin:::contains aspirin:::aspirin adverse reaction:::advice about taking aspirin:::aspirin only product:::aspirin therapy finding:::contains an aspirin-like medicine:::buffered aspirin:::aspirin- and caffeine-containing product:::aspirin- and dipyridamole-containing product:::aspirin- and paracetamol-containing product:::already on aspirin:::long-term current use of aspirin |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_snomed_pipeline_20260901|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.0 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- Chunk2Doc
- BGEEmbeddings
- SentenceEntityResolverModel