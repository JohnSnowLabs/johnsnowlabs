---
layout: model
title: Sentence Entity Resolver for SNOMED CT (Clinical Findings) (sbiobert_base_cased_mli_onnx embeddings) - Pipeline
author: John Snow Labs
name: sbiobertresolve_snomed_findings_pipeline_20260901
date: 2026-09-12
tags: [en, entity_resolution, licensed, clinical, snomed, pipeline, sbiobert, findings]
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

This pipeline extracts clinical entities from text and maps them to SNOMED CT clinical finding concepts using `sbiobert_base_cased_mli_onnx` embeddings. Wraps the `sbiobertresolve_snomed_findings_20260901` resolver, trained on SNOMED CT US Edition 20260901.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_findings_pipeline_20260901_en_6.4.1_3.4_1789217312902.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_findings_pipeline_20260901_en_6.4.1_3.4_1789217312902.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_findings_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient presented with recurrent fevers. Clinically she appeared cachectic with hepatosplenomegaly. Laboratory results confirmed pancytopenia."]]).toDF("text")
result = snomed_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

snomed_pipeline = nlp.PretrainedPipeline("sbiobertresolve_snomed_findings_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient presented with recurrent fevers. Clinically she appeared cachectic with hepatosplenomegaly. Laboratory results confirmed pancytopenia."]]).toDF("text")
result = snomed_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_findings_pipeline_20260901", "en", "clinical/models")

val data = Seq("The patient presented with recurrent fevers. Clinically she appeared cachectic with hepatosplenomegaly. Laboratory results confirmed pancytopenia.").toDF("text")
val result = snomed_pipeline.transform(data)

```
</div>

## Results

```bash
| chunk              | label      |   snomed_code | resolution         | all_codes                                                                                                                                                                                                                                                                              | all_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:-------------------|:-----------|--------------:|:-------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fevers             | VS_Finding |     386661006 | fever              | 386661006:::77957000:::271751000:::248435007:::271754008:::186694006:::704425001:::416113008:::271750004:::41348000:::271753002:::81472005:::240499000:::42136008:::1078287008:::111950007:::274640006:::248449003:::240453002:::103001002:::186774005                                 | fever:::intermittent fever:::sustained fever:::prolonged fever:::crisis of fever:::sweating fever:::chronic fever:::disorder characterized by fever:::gradual rise of fever:::piry fever:::irregular fever:::ossa fever:::sepik fever:::swinging fever:::recurrent fever:::artificial fever:::fever with rigors:::central fever:::oroya fever:::feels feverish:::boutonneuse fever                                                                                                                                                                                                                                    |
| cachectic          | Symptom    |     238108007 | cachectic          | 238108007:::422003001:::284529003:::788876001:::240128005:::288517002:::89476005:::298389007:::281583001:::231439009:::298744008:::280994000:::286933003:::284670008:::29740003:::441971000124107:::2492009:::716749005:::201139004:::441951000124102:::50805004:::84946008:::95868006 | cachectic:::cachexia associated with aids:::cardiac cachexia:::malignant cachexia:::muscle cachexia:::wasting disease:::pituitary cachexia:::wasting of neck:::nutritional wasting:::toxic confusional state:::wasting of arm:::chronic confusional state:::confusional state:::nutritionally compromised:::severe malnutrition:::chronic disease-related malnutrition:::malnutrition:::cancer-related fatigue:::cachectic alopecia:::starvation-related malnutrition:::tongue wasting:::extreme exhaustion:::heat exhaustion                                                                                         |
| hepatosplenomegaly | Symptom    |      36760000 | hepatosplenomegaly | 36760000:::16294009:::19058002:::191382009:::80378000:::240630008:::190794006:::80515008:::36752001:::58639003:::240793000:::275598004:::94701003:::413808003:::27503000:::714254003:::127120007:::66789005:::51244008:::56338005:::123671009:::169149008                              | hepatosplenomegaly:::splenomegaly:::congestive splenomegaly:::chronic congestive splenomegaly:::neonatal hepatosplenomegaly:::tropical splenomegaly syndrome:::gaucher splenomegaly:::hepatomegaly:::congenital splenomegaly:::neutropenic splenomegaly:::schistosomal splenomegaly:::hepatosplenomegalic lipoidosis:::mottled spleen:::ventriculomegaly:::constitutional hepatic dysfunction:::abdominal organomegaly:::hepatic lymphadenopathy:::hepatocellular jaundice:::splenic disorder:::fibrosis of spleen:::adrenal gland cytomegaly:::isotope scan spleen abnormal                                          |
| pancytopenia       | Symptom    |     127034005 | pancytopenia       | 127034005:::736024007:::5876000:::124961001:::417672002:::302215000:::38970002:::183005:::267524009:::267534000:::1396820003:::2897005:::51624005:::721119004:::48788004:::154826009:::415005004:::74576004:::768556005:::416902009:::191347008:::234487003:::371074009                | pancytopenia:::drug induced pancytopenia:::pancytopenia - acquired:::reticulocytopenia:::granulocytopenia:::thrombocytopenia:::splenic pancytopenia syndrome:::autoimmune pancytopenia:::pancytopenia with malformation:::primary thrombocytopenia:::intermittent thrombocytopenia:::immune thrombocytopenia:::dilutional thrombocytopenia:::pseudothrombocytopenia:::cyclic thrombocytopenia:::secondary thrombocytopenia:::panleukopenia:::acquired thrombocytopenia:::ataxia pancytopenia syndrome:::uraemic thrombocytopenia:::periodic neutropenia:::mediterranean thrombocytopenia:::radiation thrombocytopenia |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_findings_pipeline_20260901|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.8 GB|

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