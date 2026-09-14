---
layout: model
title: Sentence Entity Resolver for SNOMED CT (Body Structures) (sbiobert_base_cased_mli_onnx embeddings) - Pipeline
author: John Snow Labs
name: sbiobertresolve_snomed_bodyStructure_pipeline_20260901
date: 2026-09-12
tags: [en, entity_resolution, licensed, clinical, snomed, pipeline, sbiobert, bodystructure]
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

This pipeline extracts clinical entities from text and maps them to SNOMED CT body structure concepts using `sbiobert_base_cased_mli_onnx` embeddings.

Wraps the `sbiobertresolve_snomed_bodyStructure_20260901` resolver, trained on SNOMED CT US Edition 20260901.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_bodyStructure_pipeline_20260901_en_6.4.1_3.4_1789225274122.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_bodyStructure_pipeline_20260901_en_6.4.1_3.4_1789225274122.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_bodyStructure_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient is a 30-year-old female with coronary artery disease and swelling affecting the kidney and lower limb."]]).toDF("text")
result = snomed_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

snomed_pipeline = nlp.PretrainedPipeline("sbiobertresolve_snomed_bodyStructure_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient is a 30-year-old female with coronary artery disease and swelling affecting the kidney and lower limb."]]).toDF("text")
result = snomed_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_bodyStructure_pipeline_20260901", "en", "clinical/models")

val data = Seq("The patient is a 30-year-old female with coronary artery disease and swelling affecting the kidney and lower limb.").toDF("text")
val result = snomed_pipeline.transform(data)

```
</div>

## Results

```bash
| chunk           | label    |   snomed_code | resolution      | all_codes                                                                                                                                                                                                             | all_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:----------------|:---------|--------------:|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| coronary artery | BodyPart |      41801008 | coronary artery | 41801008:::119204004:::360487004:::55537005:::110554000:::48955001:::1343313006:::57627008:::280515006:::713317004:::110755001:::57396003:::360511005:::1373794005:::244252004:::110553006:::69105007                 | coronary artery:::coronary artery part:::segment of coronary artery:::ostium of coronary artery:::coronary artery and coronary artery, cs:::coronary valve:::structure of lumen of coronary artery:::coronary ligament:::coronary plexus:::structure of wall of coronary artery:::aorta and coronary artery, cs:::structure of circumflex coronary artery:::segment of circumflex coronary artery:::ostium of coronary intermediate artery:::structure of coronary intermediate artery:::coronary artery and myocardium, cs:::carotid artery structure |
| kidney          | BodyPart |      64033007 | kidney          | 64033007:::119219003:::84924000:::50403003:::72333003:::30737000:::74033008:::58471003:::303402001:::363530009:::363529004:::54018001:::29704000:::279371005:::16097006:::27788008:::116358006:::363531008:::91678002 | kidney:::kidney part:::renal segment:::renal cortex:::capillary of kidney:::medulla of kidney:::hilum of kidney:::renal tubule:::renal vessels:::structure of region of kidney:::structure of layer of kidney:::nephron:::parenchyma of kidney:::renal collecting system structure:::renal pyramid:::renal tubular neck:::vein of kidney:::structure of pole of kidney:::lateral border of kidney                                                                                                                                                      |
| lower limb      | BodyPart |      61685007 | lower limb      | 61685007:::30021000:::63337009:::128263001:::120575009:::69548008:::48077000:::37822005:::32032005:::27033000:::82094008:::127951001:::281394001:::39278005:::62736007:::264079000                                    | lower limb:::lower leg:::lower trunk:::lower body:::lower limb part:::lower body part:::lower jaw:::lower back structure:::lower lip:::lower abdomen structure:::lower respiratory structure:::lower extremity region:::lower zone of lung:::lower respiratory spaces:::lower eyelid:::lower pole artery                                                                                                                                                                                                                                               |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_bodyStructure_pipeline_20260901|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.4 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel