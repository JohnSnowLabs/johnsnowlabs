---
layout: model
title: Sentence Entity Resolver for SNOMED CT (Conditions) (sbiobert_base_cased_mli_onnx embeddings) - Pipeline
author: John Snow Labs
name: sbiobertresolve_snomed_conditions_pipeline_20260901
date: 2026-09-12
tags: [en, entity_resolution, licensed, clinical, snomed, pipeline, sbiobert, conditions]
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

This pipeline extracts clinical entities from text and maps them to SNOMED CT condition/disorder concepts using `sbiobert_base_cased_mli_onnx` embeddings. Wraps the `sbiobertresolve_snomed_conditions_20260901` resolver, trained on SNOMED CT US Edition 20260901.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_conditions_pipeline_20260901_en_6.4.1_3.4_1789217950604.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_conditions_pipeline_20260901_en_6.4.1_3.4_1789217950604.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_conditions_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient has a history of type 2 diabetes mellitus and essential hypertension. She was admitted with an acute myocardial infarction and later diagnosed with hyperlipidemia."]]).toDF("text")
result = snomed_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

snomed_pipeline = nlp.PretrainedPipeline("sbiobertresolve_snomed_conditions_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient has a history of type 2 diabetes mellitus and essential hypertension. She was admitted with an acute myocardial infarction and later diagnosed with hyperlipidemia."]]).toDF("text")
result = snomed_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_conditions_pipeline_20260901", "en", "clinical/models")

val data = Seq("The patient has a history of type 2 diabetes mellitus and essential hypertension. She was admitted with an acute myocardial infarction and later diagnosed with hyperlipidemia.").toDF("text")
val result = snomed_pipeline.transform(data)

```
</div>

## Results

```bash
| chunk                    | label          |   snomed_code | resolution               | all_codes                                                                                                                                                                                                                 | all_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:-------------------------|:---------------|--------------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| type 2 diabetes mellitus | Diabetes       |      44054006 | type 2 diabetes mellitus | 44054006:::199230006:::422014003:::8801005:::73211009:::422099009:::443694000:::421326000:::237601000:::761000119102:::422166005:::237599002:::1531000119102:::368591000119109:::368051000119109:::422034002              | type 2 diabetes mellitus:::pre-existing type 2 diabetes mellitus:::disorder due to type 2 diabetes mellitus:::secondary diabetes mellitus:::diabetes mellitus:::disorder of eye due to type 2 diabetes mellitus:::uncontrolled type 2 diabetes mellitus:::disorder of nervous system due to type 2 diabetes mellitus:::secondary endocrine diabetes mellitus:::diabetic dyslipidemia due to type 2 diabetes mellitus:::peripheral circulatory disorder due to type 2 diabetes mellitus:::insulin treated type 2 diabetes mellitus:::dermopathy due to type 2 diabetes mellitus:::cheiropathy due to type 2 diabetes mellitus:::hyperglycaemia due to type 2 diabetes mellitus:::retinopathy due to type 2 diabetes mellitus |
| essential hypertension   | Hypertension   |      59621000 | essential hypertension   | 59621000:::371125006:::38341003:::697929007:::19769006:::31992008:::429457004:::194788005:::78975002:::1356877007:::48146000:::845891000000103:::703232003:::23130000:::65518004:::89242004:::56218007:::1110081000000100 | essential hypertension:::labile essential hypertension:::hypertensive disorder:::intermittent hypertension:::high-renin essential hypertension:::secondary hypertension:::systolic essential hypertension:::endocrine hypertension:::accelerated essential hypertension:::stable hypertension:::diastolic hypertension:::resistant hypertension:::glucocorticoid-sensitive hypertension:::episodic hypertension:::labile diastolic hypertension:::accelerated secondary hypertension:::systolic hypertension:::primary ocular hypertension                                                                                                                                                                                  |
| myocardial infarction    | Heart_Disease  |      22298006 | myocardial infarction    | 22298006:::380001000004106:::57054005:::466635291000119109:::194856005:::164865005:::429731003:::194857001:::401303003:::54329005:::428196007:::16837681000119104:::73795002:::65547006:::432504007:::418044006           | myocardial infarction:::subendocardial myocardial infarction:::acute myocardial infarction:::myocardial infarction with coronary microvascular dysfunction:::subsequent myocardial infarction:::ecg: myocardial infarction:::anterior myocardial infarction on ecg:::subsequent myocardial infarction of anterior wall:::stemi - st elevation myocardial infarction:::acute anterior myocardial infarction:::mixed myocardial ischaemia and infarction:::type 2 myocardial infarction:::acute inferior myocardial infarction:::acute inferolateral myocardial infarction:::cerebral infarction:::myocardial infarction in recovery phase                                                                                    |
| hyperlipidemia           | Hyperlipidemia |      55822004 | hyperlipidemia           | 55822004:::190774002:::129589009:::267434003:::402727002:::129590000:::238089003:::3744001:::238088006:::398796005:::1264212004                                                                                           | hyperlipidemia:::hyperlipidemia, group a:::endogenous hyperlipidemia:::multiple-type hyperlipidemia:::secondary hyperlipidemia:::exogenous hyperlipidemia:::secondary combined hyperlipidemia:::hyperlipoproteinemia:::primary combined hyperlipidemia:::remnant hyperlipidemia:::hyperlipoproteinemia (a)                                                                                                                                                                                                                                                                                                                                                                                                                  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_conditions_pipeline_20260901|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.7 GB|

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