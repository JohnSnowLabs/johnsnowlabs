---
layout: model
title: Sentence Entity Resolver for SNOMED CT (All Concepts) (mpnet_embeddings_biolord_2023_c embeddings) - Pipeline
author: John Snow Labs
name: biolordresolve_snomed_pipeline_20260901
date: 2026-09-12
tags: [en, entity_resolution, licensed, clinical, snomed, pipeline, biolord, general]
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

This pipeline extracts clinical entities from text and maps them to the full, domain-unrestricted set of active SNOMED CT concepts using `mpnet_embeddings_biolord_2023_c` embeddings.

Wraps the `biolordresolve_snomed_20260901` resolver, trained on SNOMED CT US Edition 20260901.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_pipeline_20260901_en_6.4.1_3.4_1789232864057.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_pipeline_20260901_en_6.4.1_3.4_1789232864057.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("biolordresolve_snomed_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient with inflammatory bowel disease presented with dyspnea and abdominal pain. She underwent a laparoscopic appendectomy and was started on aspirin."]]).toDF("text")
result = snomed_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

snomed_pipeline = nlp.PretrainedPipeline("biolordresolve_snomed_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient with inflammatory bowel disease presented with dyspnea and abdominal pain. She underwent a laparoscopic appendectomy and was started on aspirin."]]).toDF("text")
result = snomed_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("biolordresolve_snomed_pipeline_20260901", "en", "clinical/models")

val data = Seq("The patient with inflammatory bowel disease presented with dyspnea and abdominal pain. She underwent a laparoscopic appendectomy and was started on aspirin.").toDF("text")
val result = snomed_pipeline.transform(data)

```
</div>

## Results

```bash
| chunk                      | label                     |   snomed_code | resolution                 | all_codes                                                                                                                                                                                                                                       | all_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:---------------------------|:--------------------------|--------------:|:---------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| inflammatory bowel disease | Disease_Syndrome_Disorder |      24526004 | inflammatory bowel disease | 24526004:::1396343004:::64226004:::1187638005:::43752006:::50440006:::397173003:::34000006:::52457000:::64766004:::396336000:::54597004:::418130002                                                                                             | inflammatory bowel disease:::inflammatory bowel disease unclassified:::colitis:::enteritis of intestine:::inflammation of small intestine and colon:::cc - crohn's colitis:::crohn disease of intestine:::crohn disease:::ileitis:::colitis gravis:::acute and chronic colitis:::chronic colitis:::colorectitis                                                                                                                                                                                          |
| dyspnea                    | Symptom                   |     267036007 | dyspnea                    | 267036007:::297216006:::230145002:::248549001:::23141003:::60845006:::870535009:::399322006:::248550001                                                                                                                                         | dyspnea:::increasing breathlessness:::difficulty breathing:::labored breathing:::gasping for breath:::soboe - shortness of breath on exertion:::chronic dyspnea:::air hunger:::can't breathe deeply enough                                                                                                                                                                                                                                                                                               |
| abdominal pain             | Symptom                   |      21522001 | abdominal pain             | 21522001:::9991008:::271681002:::102614006:::73063007:::438506002:::162042000:::247358007:::162046002:::54586004:::116290004:::371102005:::102613000:::443503005:::304542004:::410716004                                                        | abdominal pain:::abdominal colic:::belly ache:::generalised abdominal pain:::colicky pain:::visceral abdominal pain:::abdominal wall pain:::abdominal pain type:::central abdominal pain:::lower abdominal pain:::acute abdominal pain:::generalised colicky abdominal pain:::localised abdominal pain:::periumbilical abdominal pain:::nonspecific abdominal pain:::colicky                                                                                                                             |
| laparoscopic appendectomy  | Procedure                 |       6025007 | laparoscopic appendectomy  | 6025007:::307581005:::708876004:::174041007:::80146002:::440588003:::235313004:::82730006:::1156321000:::174045003:::174036004                                                                                                                  | laparoscopic appendectomy:::laparoscopic interval appendectomy:::robot assisted laparoscopic appendectomy:::laparoscopic emergency appendectomy:::appendectomy:::endoscopic procedure on appendix:::non-emergency appendectomy:::incidental appendectomy:::history of laparoscopic appendectomy:::interval appendicectomy:::emergency appendicectomy                                                                                                                                                     |
| aspirin                    | Drug_Ingredient           |     387458008 | aspirin                    | 387458008:::7947003:::426365001:::25796002:::10876551000119102:::60526005:::292044008:::412566001:::417980006:::295135004:::717854002:::255637000:::431463004:::418281004:::774656009:::405748007:::293586001:::8132009:::135800003:::350312004 | aspirin:::aspirin-containing product:::buffered aspirin:::aluminum aspirin:::aspirin poisoning:::acetyl salicylate:::aspirin adverse reaction:::buffered aspirin-containing product:::contains aspirin:::aspirin overdose:::aspirin therapy:::salicylate:::administration of aspirin:::do not take anything containing aspirin while taking this medicine:::aspirin only product:::already on aspirin:::aspirin allergy:::magnesium acetylsalicylate:::aspirin indicated:::product containing salicylate |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_snomed_pipeline_20260901|
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
- MPNetEmbeddings
- SentenceEntityResolverModel