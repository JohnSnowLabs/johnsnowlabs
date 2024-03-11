---
layout: model
title: Pipeline for SNOMED Drug Sentence Entity Resolver
author: John Snow Labs
name: snomed_drug_resolver_pipeline
date: 2024-03-11
tags: [licensed, en, entity_resolution, clinical, pipeline, snomed, drug]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This advanced pipeline extracts drug entities from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding SNOMED codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_drug_resolver_pipeline_en_5.3.0_3.2_1710173059882.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_drug_resolver_pipeline_en_5.3.0_3.2_1710173059882.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("snomed_drug_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""John's doctor prescribed aspirin for his heart condition,
along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and
lansoprazole for his GORD on 2023-12-01.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("snomed_drug_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""John's doctor prescribed aspirin for his heart condition,
along with paracetamol for his fever and headache, amoxicillin for his tonsilitis and
lansoprazole for his GORD on 2023-12-01.""")

```
</div>

## Results

```bash
|    | chunks       |   begin |   end | entities   |      Code | description   | resolutions                                                                                                                                                                                                                                                                                                                                                                                                       | all_codes                                                                                                                                                                                              |
|---:|:-------------|--------:|------:|:-----------|----------:|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | aspirin      |      25 |    31 | DRUG       |   7947003 | aspirin       | aspirin:::oral aspirin:::aspirin, buffered:::buffered aspirin product:::aluminium aspirin:::aspirin and glycine:::aspirin - chemical:::cephapirin:::aspirin- and dipyridamole-containing product:::aspirin-containing product in oromucosal dose form:::rectal form aspirin                                                                                                                                       | 7947003:::358427004:::426365001:::412566001:::25796002:::398767009:::387458008:::87303007:::319796006:::785413006:::350314003                                                                          |
|  1 | paracetamol  |      69 |    79 | DRUG       | 387517004 | paracetamol   | paracetamol:::paracetamol product:::oral form paracetamol:::parenteral form paracetamol:::piracetam:::rectal form paracetamol:::phenacemide:::sulphacetamide:::butalbital and paracetamol product:::paracetamol and salicylamide product:::diphenhydramine + paracetamol:::isometheptene + paracetamol:::caffeine + paracetamol:::paracetamol and pseudoephedrine product:::aspartame:::acemetacin:::phenindamine | 387517004:::90332006:::437876006:::437818001:::322998004:::437858004:::18712002:::372676007:::398826009:::398663003:::423936008:::423801005:::350309002:::412499001:::398791000:::329906008:::36909007 |
|  2 | amoxicillin  |     109 |   119 | DRUG       |  27658006 | amoxicillin   | amoxicillin:::oral amoxicillin:::amoxicillin sodium:::oral ampicillin:::almecillin:::ampicillin:::parenteral amoxicillin:::cloxacillin:::amifloxacin:::amoxicillin and clavulanate:::aminopenicillin:::dicloxacillin:::flucloxacillin                                                                                                                                                                             | 27658006:::350162003:::427483001:::350164002:::117147001:::31087008:::350163008:::68422006:::442859000:::734844004:::90704004:::8416000:::387544009                                                    |
|  3 | lansoprazole |     144 |   155 | DRUG       | 108666007 | lansoprazole  | lansoprazole:::oral form lansoprazole:::dexlansoprazole:::brexpiprazole:::dapiprazole:::loprazolam:::esomeprazole:::omeprazole:::parenteral form lansoprazole:::rabeprazole:::lansoprazole-containing product in oromucosal dose form:::clotrimazole:::aripiprazole lauroxil:::clomethiazole:::lamotrigine:::rabeprazole product:::carnidazole                                                                    | 108666007:::437961004:::441863009:::716069007:::108840006:::321119005:::317331009:::25673006:::437976007:::422225001:::785533007:::5797005:::715182007:::354039005:::96195007:::421279008:::96102004   |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_drug_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.4 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- TextMatcherInternalModel
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