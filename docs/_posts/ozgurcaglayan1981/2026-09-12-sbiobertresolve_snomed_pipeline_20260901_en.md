---
layout: model
title: Sentence Entity Resolver for SNOMED CT (All Concepts) (sbiobert_base_cased_mli_onnx embeddings) - Pipeline
author: John Snow Labs
name: sbiobertresolve_snomed_pipeline_20260901
date: 2026-09-12
tags: [en, entity_resolution, licensed, clinical, snomed, pipeline, sbiobert, general]
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

This pipeline extracts clinical entities from text and maps them to the full, domain-unrestricted set of active SNOMED CT concepts using `sbiobert_base_cased_mli_onnx` embeddings.

Wraps the `sbiobertresolve_snomed_20260901` resolver, trained on SNOMED CT US Edition 20260901.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_pipeline_20260901_en_6.4.1_3.4_1789231454808.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_pipeline_20260901_en_6.4.1_3.4_1789231454808.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient with inflammatory bowel disease presented with dyspnea and abdominal pain. She underwent a laparoscopic appendectomy and was started on aspirin."]]).toDF("text")
result = snomed_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

snomed_pipeline = nlp.PretrainedPipeline("sbiobertresolve_snomed_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient with inflammatory bowel disease presented with dyspnea and abdominal pain. She underwent a laparoscopic appendectomy and was started on aspirin."]]).toDF("text")
result = snomed_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_pipeline_20260901", "en", "clinical/models")

val data = Seq("The patient with inflammatory bowel disease presented with dyspnea and abdominal pain. She underwent a laparoscopic appendectomy and was started on aspirin.").toDF("text")
val result = snomed_pipeline.transform(data)

```
</div>

## Results

```bash
| chunk                      | label                     |   snomed_code | resolution                 | all_codes                                                                                                                                                                                                                                                                | all_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:---------------------------|:--------------------------|--------------:|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| inflammatory bowel disease | Disease_Syndrome_Disorder |      24526004 | inflammatory bowel disease | 24526004:::9281000146109:::6382002:::1300120005:::1300124001:::700104004:::128999004:::373407002:::1162893000:::788718000:::10743008:::82196007:::608844008:::397173003:::397172008:::403878007:::128139000:::737195007:::50440006:::1144956000:::1187638005:::274897005 | inflammatory bowel disease:::inflammatory bowel disease suspected:::chronic inflammatory small bowel disease:::alpi-related inflammatory bowel disease:::trim22-related inflammatory bowel disease:::management of inflammatory bowel disease:::inflammatory disorder of digestive tract:::inflammatory disorder of digestive system:::bowen's disease:::iritis co-occurrent with inflammatory bowel disease:::functional bowel disease:::ischaemic bowel disease:::history of inflammatory bowel disease:::crohn's disease of intestine:::gastrointestinal crohn's disease:::bowen's disease of arm:::inflammatory disease:::crohn disease of upper gastrointestinal tract:::granulomatous colitis:::vasculitis due to inflammatory bowel disease:::inflammation of intestine:::clonal bowen's disease |
| dyspnea                    | Symptom                   |     267036007 | dyspnea                    | 267036007:::60845006:::25209001:::34560001:::59265000:::870535009:::1023001:::386614005:::90701007:::161939006:::390871002:::30744009:::62744007                                                                                                                         | dyspnea:::exertional dyspnea:::inspiratory dyspnea:::expiratory dyspnea:::paroxysmal dyspnea:::chronic dyspnea:::apnea:::oligopnea:::secondary apnea:::dyspnea on moderate exertion:::dyspnea on strenuous exertion:::platypnea:::orthopnea                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| abdominal pain             | Symptom                   |      21522001 | abdominal pain             | 21522001:::83132003:::364630006:::162042000:::247358007:::438506002:::102614006:::102613000:::14700001000004102:::9991008:::162046002:::1332010007:::28221000119103:::35611005:::111985007:::307199009:::73645008:::737306007:::29695002:::275406005                     | abdominal pain:::upper abdominal pain:::abdominal pain characteristic:::abdominal wall pain:::abdominal pain type:::visceral abdominal pain:::generalized abdominal pain:::localized abdominal pain:::intractable abdominal pain:::colicky abdominal pain:::central abdominal pain:::site of abdominal pain:::abdominal muscle pain:::abdominal rebound pain:::chronic abdominal pain:::psychosomatic abdominal pain:::visceral pain:::chronic visceral pain:::throbbing pain:::appendicular pain                                                                                                                                                                                                                                                                                                       |
| laparoscopic appendectomy  | Procedure                 |       6025007 | laparoscopic appendectomy  | 6025007:::307581005:::708819001:::1220546008:::174041007:::46569000:::235314005:::708876004:::1390003:::708627007:::80146002:::1220549001:::45595009:::42843004:::1255832001                                                                                             | laparoscopic appendectomy:::laparoscopic interval appendectomy:::laparoscopic omentectomy:::laparoscopic jejunectomy:::laparoscopic emergency appendectomy:::laparoscopic-assisted abdominoperineal resection:::inversion appendectomy:::robot assisted laparoscopic appendectomy:::laparoscopic-assisted sigmoidectomy:::laparoscopic excision of small intestine:::appendectomy:::laparoscopic ileectomy:::laparoscopic cholecystectomy:::laparoscopic adrenalectomy:::laparoscopic anorectoplasty                                                                                                                                                                                                                                                                                                    |
| aspirin                    | Drug_Ingredient           |     387458008 | aspirin                    | 387458008:::432909005:::135800003:::717854002:::7947003:::431463004:::405742008:::417980006:::426365001:::405743003:::407136004:::412566001:::25796002:::312452009:::26047008:::405748007:::87303007:::319796006:::398767009:::390882005:::785413006                     | aspirin:::aspirin given:::aspirin indicated:::aspirin therapy:::aspirin-containing product:::administration of aspirin:::aspirin therapy finding:::contains aspirin:::aspirin, buffered:::aspirin therapy location:::aspirin specific ige:::buffered aspirin-containing product:::aluminium aspirin:::aspirin prophylaxis:::aspirin tolerance test:::already on aspirin:::cephapirin:::aspirin- and dipyridamole-containing product:::aspirin- and glycine-containing product:::referral to gp - aspirin management:::aspirin-containing product in oromucosal dose form                                                                                                                                                                                                                                |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_pipeline_20260901|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.2 GB|

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