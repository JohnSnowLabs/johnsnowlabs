---
layout: model
title: Pipeline for Snomed Concept, Aux Concepts Version
author: John Snow Labs
name: snomed_auxConcepts_resolver_pipeline
date: 2024-03-11
tags: [licensed, en, snomed, pipeline, resolver, auxconcepts]
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

This pipeline extracts clinical entities and concepts to maps their corresponding SNOMED (CT version) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_auxConcepts_resolver_pipeline_en_5.3.0_3.2_1710201441291.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_auxConcepts_resolver_pipeline_en_5.3.0_3.2_1710201441291.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

resolver_pipeline = PretrainedPipeline("snomed_auxConcepts_resolver_pipeline", "en", "clinical/models")

result = resolver_pipeline.fullAnnotate("""This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val resolver_pipeline = PretrainedPipeline("snomed_auxConcepts_resolver_pipeline", "en", "clinical/models")

val result = resolver_pipeline.fullAnnotate("""This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, COPD, gastritis, and TIA. He initially presented to Braintree with a nonspecific ST-T abnormality and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of occlusion of the mid left anterior descending coronary artery lesion, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine, possibly secondary to a vagal reaction.""")

```
</div>

## Results

```bash

+-----------------------+---------------+-----------+-----------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                  chunk|          label|snomed_code|             resolution|                                         all_codes|                                   all_resolutions|                                    all_aux_labels|
+-----------------------+---------------+-----------+-----------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                tobacco|        Smoking|   57264008|                tobacco|57264008:::102407002:::39953003:::159882006:::1...|tobacco:::tobacco smoke:::tobacco - substance::...|Organism:::Substance:::Substance:::Social Conte...|
|            nonspecific|       Modifier|   10003008|           non-specific|10003008:::261992003:::863956004:::300844001:::...|non-specific:::non-biological:::non-sterile:::n...|Qualifier Value:::Qualifier Value:::Qualifier V...|
|cardiac catheterization|      Procedure|   41976001|cardiac catheterization|41976001:::705923009:::721968000:::467735004:::...|cardiac catheterization:::cardiac catheter:::ca...|Procedure:::Physical Object:::Record Artifact::...|
|               atropine|Drug_Ingredient|   73949004|               atropine|73949004:::105075009:::349945006:::410493009:::...|atropine:::atropine measurement:::oral atropine...|Pharma/Biol Product:::Procedure:::Clinical Drug...|
|                 fluids|Drug_Ingredient|  118431008|               iv fluid|118431008:::82449006:::47625008:::261841005:::2...|iv fluid:::iv catheter:::iv route:::iv/c:::iv/r...|Substance:::Physical Object:::Qualifier Value::...|
|               dopamine|Drug_Ingredient|   59187003|               dopamine|59187003:::412383006:::37484001:::32779004:::41...|dopamine:::dopamine agent:::dopamine receptor::...|Pharma/Biol Product:::Substance:::Substance:::P...|
+-----------------------+---------------+-----------+-----------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_auxConcepts_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.6 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel