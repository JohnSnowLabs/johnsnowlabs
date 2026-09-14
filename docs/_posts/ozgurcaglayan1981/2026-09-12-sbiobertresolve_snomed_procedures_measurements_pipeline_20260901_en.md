---
layout: model
title: Sentence Entity Resolver for SNOMED CT (Procedures and Measurements) (sbiobert_base_cased_mli_onnx embeddings) - Pipeline
author: John Snow Labs
name: sbiobertresolve_snomed_procedures_measurements_pipeline_20260901
date: 2026-09-12
tags: [en, entity_resolution, licensed, clinical, snomed, pipeline, sbiobert, procedure_measurements]
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

This pipeline extracts clinical entities from text and maps them to SNOMED CT procedure and measurement concepts using `sbiobert_base_cased_mli_onnx` embeddings. Wraps the `sbiobertresolve_snomed_procedures_measurements_20260901` resolver, trained on SNOMED CT US Edition 20260901.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_procedures_measurements_pipeline_20260901_en_6.4.1_3.4_1789219118103.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_procedures_measurements_pipeline_20260901_en_6.4.1_3.4_1789219118103.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_procedures_measurements_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient underwent a laparoscopic cholecystectomy and appendectomy. Laboratory testing showed an elevated white blood cell count."]]).toDF("text")
result = snomed_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

snomed_pipeline = nlp.PretrainedPipeline("sbiobertresolve_snomed_procedures_measurements_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient underwent a laparoscopic cholecystectomy and appendectomy. Laboratory testing showed an elevated white blood cell count."]]).toDF("text")
result = snomed_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_procedures_measurements_pipeline_20260901", "en", "clinical/models")

val data = Seq("The patient underwent a laparoscopic cholecystectomy and appendectomy. Laboratory testing showed an elevated white blood cell count.").toDF("text")
val result = snomed_pipeline.transform(data)

```
</div>

## Results

```bash
| chunk                        | label     |   snomed_code | resolution                   | all_codes                                                                                                                                                                                                                                                         | all_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:-----------------------------|:----------|--------------:|:-----------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| laparoscopic cholecystectomy | Procedure |      45595009 | laparoscopic cholecystectomy | 45595009:::450500003:::440581009:::450499007:::67557008:::1137453008:::449334003:::38102005:::89967006:::1137372009:::174497004:::302619004:::1220546008:::1137362006:::1351803006:::6402000:::88748005:::708632008:::1162442001:::439712000:::6025007:::45993005 | laparoscopic cholecystectomy:::laparoscopic cholecystostomy:::laparoscopic cholecystenterostomy:::laparoscopic subtotal cholecystectomy:::laparoscopic cholecystectomy with exploration of common duct:::robot assisted laparoscopic cholecystectomy:::endoscopic choledocholithotomy:::cholecystectomy:::thoreck operation, partial cholecystectomy:::robot assisted laparoscopic partial cholecystectomy:::partial cholecystectomy and exploration of common bile duct:::cholecystectomy and exploration of bile duct:::laparoscopic jejunectomy:::robot assisted laparoscopic cholecystectomy and exploration of common bile duct:::laparoscopic cholecystectomy with intraoperative fluoroscopic cholangiography with contrast:::choledochectomy:::cholecystolithotomy:::laparoscopic incision and exploration of common bile duct:::laparoscopic hepatic cystectomy:::cholecystectomy with exploration of common bile duct and choledochoenterostomy:::laparoscopic appendicectomy:::cholecystectomy with exploration of common duct |
| appendectomy                 | Procedure |      80146002 | appendectomy                 | 80146002:::17041004:::82730006:::174045003:::6025007:::235314005:::51113007:::1299000:::49586007:::42332004:::49438003:::6801000:::39126001:::22324003:::54357003:::55588008:::174036004:::307583008:::119954001                                                  | appendectomy:::appendicotomy:::secondary appendectomy:::interval appendectomy:::endoscopic appendectomy:::inversion appendectomy:::appendicolysis:::excision of appendiceal stump:::appendicocaecostomy:::appendicostomy:::appendectomy and drainage:::mesenterectomy:::angiectomy:::jejunectomy:::enterectomy:::abdominal arteriectomy:::emergency appendectomy:::cecectomy:::adenoidectomy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Laboratory testing           | Test      |      15220000 | laboratory test              | 15220000:::386344002:::108252007:::16488004:::266753000:::410343006:::67664000:::18699002:::410394004:::117337005:::431561000124105:::56377008:::428995007:::57501001:::127789004:::252318005:::252511003:::33526004:::59615004                                   | laboratory test:::laboratory data interpretation:::laboratory procedures:::laboratory reporting:::referral for laboratory tests:::laboratory findings case management:::laboratory calculation:::clinical laboratory specimen identification:::laboratory findings surveillance:::calculated laboratory test method:::monitoring of laboratory results:::laboratory ratio determination:::receiving of specimen in laboratory:::laboratory reporting, cum sum:::laboratory procedure categorized by method:::immunology laboratory test:::clinical immunological test:::laboratory reporting, electronic:::laboratory test order by laboratory initiative                                                                                                                                                                                                                                                                                                                                                                                 |
| white blood cell count       | Test      |        767002 | white blood cell count       | 767002:::252305002:::165511009:::44190001:::391558003:::42396003:::302560003:::250300004:::88308000:::6289009:::252306001:::19957009:::250305009:::118218001:::47616002:::250273000:::252276003                                                                   | white blood cell count:::white blood cell test:::differential white blood cell count:::white blood cell morphology:::total white blood cell count:::white blood cell estimate:::percentage differential white blood cells:::white blood cell enzyme activity:::blood cell count:::white blood cell histogram evaluation:::white blood cell cytochemistry:::white blood cell enzyme determination:::white blood cell membrane antigen:::cell count:::white blood cell localisation, whole body:::white blood cell age:::blood cell analysis                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_procedures_measurements_pipeline_20260901|
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
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel