---
layout: model
title: Sentence Entity Resolver for SNOMED CT (Drugs) (sbiobert_base_cased_mli_onnx embeddings) - Pipeline
author: John Snow Labs
name: sbiobertresolve_snomed_drug_pipeline_20260901
date: 2026-09-12
tags: [en, entity_resolution, licensed, clinical, snomed, pipeline, sbiobert, drug]
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

This pipeline extracts clinical entities from text and maps them to SNOMED CT drug/substance concepts using `sbiobert_base_cased_mli_onnx` embeddings. Wraps the `sbiobertresolve_snomed_drug_20260901` resolver, trained on SNOMED CT US Edition 20260901.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_drug_pipeline_20260901_en_6.4.1_3.4_1789219656182.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_drug_pipeline_20260901_en_6.4.1_3.4_1789219656182.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_drug_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD."]]).toDF("text")
result = snomed_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

snomed_pipeline = nlp.PretrainedPipeline("sbiobertresolve_snomed_drug_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD."]]).toDF("text")
result = snomed_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_drug_pipeline_20260901", "en", "clinical/models")

val data = Seq("John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and lansoprazole for his GORD.").toDF("text")
val result = snomed_pipeline.transform(data)

```
</div>

## Results

```bash
| chunk        | label   |   snomed_code | resolution   | all_codes                                                                                                                                                                                                                                                                                | all_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:-------------|:--------|--------------:|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| aspirin      | DRUG    |     387458008 | aspirin      | 387458008:::7947003:::426365001:::412566001:::25796002:::87303007:::319796006:::398767009:::785413006:::358427004:::735135008:::51622009:::9913005:::373444002:::424039006:::398649009:::370337008:::259699009:::398683002:::130699009:::713473008                                       | aspirin:::aspirin-containing product:::aspirin, buffered:::buffered aspirin-containing product:::aluminium aspirin:::cephapirin:::aspirin- and dipyridamole-containing product:::aspirin- and glycine-containing product:::aspirin-containing product in oromucosal dose form:::aspirin-containing product in oral dose form:::aspirin dl-lysine:::adenase:::arachidic acid:::atorvastatin:::peroxyacetic acid-containing product:::aspirin- and carisoprodol-containing product:::cephapirin-containing product:::antianemia agent:::aspirin- and meprobamate-containing product:::astacin:::spirapril                                  |
| paracetamol  | DRUG    |     387517004 | paracetamol  | 387517004:::1285524005:::90332006:::395833008:::18712002:::724182003:::59034000:::417551008:::391704009:::387201009:::423801005:::398663003:::412499001:::322998004:::398826009:::398918002:::1285523004:::35281007:::86223002:::372699006:::423936008:::96251009:::39815009:::763002008 | paracetamol:::propacetamol:::paracetamol-containing product:::piracetam:::phenacemide:::paracetamol crystal:::trometamol:::acetamide:::acemetacin:::phenindamine:::isometheptene- and paracetamol-containing product:::paracetamol- and salicylamide-containing product:::paracetamol- and pseudoephedrine-containing product:::piracetam-containing product:::butalbital- and paracetamol-containing product:::methionine- and paracetamol-containing product:::propacetamol hydrochloride:::acetophenazine:::protaminase:::pentamidine:::diphenhydramine- and paracetamol-containing product:::crotetamide:::clorazepate:::carfentanil |
| amoxicillin  | DRUG    |     372687004 | amoxicillin  | 372687004:::27658006:::427483001:::117147001:::387170002:::373276005:::442859000:::373298001:::372873001:::387544009:::372786004:::387266001:::31087008:::373515001:::372868007:::785686003:::96068000:::43048003:::41332001:::373274008:::387543003:::82885001:::412439003:::58883005   | amoxicillin:::amoxicillin-containing product:::amoxicillin sodium:::almecillin:::ampicillin:::cloxacillin:::amifloxacin:::aminopenicillin:::dicloxacillin:::flucloxacillin:::clindamycin:::amikacin:::ampicillin-containing product:::meticillin:::oxacillin:::amoxicillin anhydrous:::amoxicillin trihydrate:::amfomycin:::amimycin:::acylaminopenicillin:::temocillin:::colistimethate:::moxifloxacin:::clindamycin-containing product                                                                                                                                                                                                 |
| lansoprazole | DRUG    |     386888004 | lansoprazole | 386888004:::108666007:::441863009:::716069007:::372549002:::395774003:::396047003:::387137007:::422225001:::785533007:::387325003:::715182007:::395978007:::387562000:::96102004:::363554004:::442011001:::395772004:::55944008:::317331009:::96126002:::386983007:::116087001           | lansoprazole:::lansoprazole-containing product:::dexlansoprazole:::brexpiprazole:::dapiprazole:::loprazolam:::esomeprazole:::omeprazole:::rabeprazole:::lansoprazole-containing product in oromucosal dose form:::clotrimazole:::aripiprazole lauroxil:::clomethiazole:::lamotrigine:::carnidazole:::tolazoline:::loprazolam mesylate:::lofepramine:::niridazole:::esomeprazole-containing product:::cambendazole:::alprazolam:::cilostazol                                                                                                                                                                                              |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_drug_pipeline_20260901|
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