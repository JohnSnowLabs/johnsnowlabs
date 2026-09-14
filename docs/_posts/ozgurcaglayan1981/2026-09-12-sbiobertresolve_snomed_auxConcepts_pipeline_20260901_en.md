---
layout: model
title: Sentence Entity Resolver for SNOMED CT (Auxiliary Concepts) (sbiobert_base_cased_mli_onnx embeddings) - Pipeline
author: John Snow Labs
name: sbiobertresolve_snomed_auxConcepts_pipeline_20260901
date: 2026-09-12
tags: [en, entity_resolution, licensed, clinical, snomed, pipeline, sbiobert, auxconcepts]
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

This pipeline extracts clinical entities from text and maps them to SNOMED CT auxiliary/descriptive concepts using `sbiobert_base_cased_mli_onnx` embeddings. Wraps the `sbiobertresolve_snomed_auxConcepts_20260901` resolver, trained on SNOMED CT US Edition 20260901.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_auxConcepts_pipeline_20260901_en_6.4.1_3.4_1789216745061.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_auxConcepts_pipeline_20260901_en_6.4.1_3.4_1789216745061.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_auxConcepts_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["She underwent an appendectomy for appendicitis. Post-operatively, she was started on penicillin. An echocardiogram showed normal left ventricle function."]]).toDF("text")
result = snomed_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

snomed_pipeline = nlp.PretrainedPipeline("sbiobertresolve_snomed_auxConcepts_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["She underwent an appendectomy for appendicitis. Post-operatively, she was started on penicillin. An echocardiogram showed normal left ventricle function."]]).toDF("text")
result = snomed_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_auxConcepts_pipeline_20260901", "en", "clinical/models")

val data = Seq("She underwent an appendectomy for appendicitis. Post-operatively, she was started on penicillin. An echocardiogram showed normal left ventricle function.").toDF("text")
val result = snomed_pipeline.transform(data)

```
</div>

## Results

```bash
| chunk          | label           |   snomed_code | resolution     | all_codes                                                                                                                                                                                                                                                    | all_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:---------------|:----------------|--------------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| appendectomy   | Procedure       |      80146002 | appendectomy   | 80146002:::17041004:::82730006:::174045003:::6025007:::235314005:::51113007:::1299000:::49586007:::42332004:::49438003:::6801000:::39126001:::22324003:::54357003:::55588008:::174036004:::307583008:::119954001                                             | appendectomy:::appendicotomy:::secondary appendectomy:::interval appendectomy:::endoscopic appendectomy:::inversion appendectomy:::appendicolysis:::excision of appendiceal stump:::appendicocaecostomy:::appendicostomy:::appendectomy and drainage:::mesenterectomy:::angiectomy:::jejunectomy:::enterectomy:::abdominal arteriectomy:::emergency appendectomy:::cecectomy:::adenoidectomy                                                                                                                                               |
| penicillin     | Drug_Ingredient |     764146007 | penicillin     | 764146007:::372725003:::323389000:::79744009:::9330003:::890458001:::387545005:::52627000:::387084009:::391818008:::373298001:::373291007:::86848007:::373218000:::42993004:::372836004:::387246005:::96072001:::300041008:::39359008:::78507004:::373284009 | penicillin:::penicillin v:::penicillin g:::penicillinase:::penicillin measurement:::penicillin-containing product:::pivampicillin:::penicillinase measurement:::phenethicillin:::benethamine penicillin:::aminopenicillin:::natural penicillin:::penicillin amidase:::antipseudomonal penicillin:::penicillium:::piperacillin:::procaine penicillin g:::pivampicillin-containing product:::penicillin prophylaxis:::penicillin v-containing product:::penicillin g-containing product:::extended spectrum penicillin                       |
| echocardiogram | Test            |      40701008 | echocardiogram | 40701008:::1354543009:::433232009:::433236007:::16310003:::105376000:::439238004:::401000009:::1297086000:::252420009:::390791001:::468366005:::425789000:::830078000:::433231002:::830079008:::86599005:::61518007                                          | echocardiogram:::ventricular echocardiography:::epicardial echocardiography:::transthoracic echocardiography:::echography:::transoesophageal echocardiogram:::echocardiography test interpretation:::echocardiogram requested:::echoendoscope:::intravascular echocardiography:::referral for echocardiography:::echocardiographic recording paper:::transluminal intracardiac echocardiography:::velocity vector echocardiography:::contrast echocardiography:::speckle tracking echocardiography:::echoplacentogram:::echography, a-mode |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_auxConcepts_pipeline_20260901|
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
- BertSentenceEmbeddings
- SentenceEntityResolverModel