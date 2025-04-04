---
layout: model
title: Pipeline to Resolve Medication Codes
author: John Snow Labs
name: medication_resolver_pipeline
date: 2024-02-27
tags: [resolver, rxnorm, medication, ndc, snomed, ade, umls, pipeline, en, licensed]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

A pretrained resolver pipeline to extract medications and resolve their adverse reactions (ADE), RxNorm, UMLS, NDC, SNOMED CT codes, and action/treatments in clinical text.

Action/treatments are available for branded medication, and SNOMED codes are available for non-branded medication.

This pipeline can be used as Lightpipeline (with `annotate/fullAnnotate`). You can use `medication_resolver_transform_pipeline` for Spark transform.

## Predicted Entities

`DRUG`, `DOSAGE`, `FREQUENCY`, `ROUTE`, `STRENGTH`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/medication_resolver_pipeline_en_5.2.1_3.0_1709055651634.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/medication_resolver_pipeline_en_5.2.1_3.0_1709055651634.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

medication_resolver_pipeline = PretrainedPipeline("medication_resolver_pipeline", "en", "clinical/models")

text = """The patient was prescribed Amlodopine Vallarta 10-320mg, Eviplera. The other patient is given Lescol 40 MG and Everolimus 1.5 mg tablet."""

result = med_resolver_pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val med_resolver_pipeline = new PretrainedPipeline("medication_resolver_pipeline", "en", "clinical/models")

val result = med_resolver_pipeline.fullAnnotate("""The patient was prescribed Amlodopine Vallarta 10-320mg, Eviplera. The other patient is given Lescol 40 MG and Everolimus 1.5 mg tablet.""")

```
</div>

## Results

```bash
+----------------------------+---------+---------------------------+-------+--------------------------+------------------------------------------+--------+---------+-----------+-------------+
|chunk                       |ner_label|ADE                        |RxNorm |Action                    |Treatment                                 |UMLS    |SNOMED_CT|NDC_Product|NDC_Package  |
+----------------------------+---------+---------------------------+-------+--------------------------+------------------------------------------+--------+---------+-----------+-------------+
|Amlodopine Vallarta 10-320mg|DRUG     |Gynaecomastia              |722131 |NONE                      |NONE                                      |C1949334|425838008|00093-7693 |00093-7693-56|
|Eviplera                    |DRUG     |Anxiety                    |217010 |Inhibitory Bone Resorption|Osteoporosis                              |C0720318|NONE     |NONE       |NONE         |
|Lescol 40 MG                |DRUG     |NONE                       |103919 |Hypocholesterolemic       |Heterozygous Familial Hypercholesterolemia|C0353573|NONE     |00078-0234 |00078-0234-05|
|Everolimus 1.5 mg tablet    |DRUG     |Acute myocardial infarction|2056895|NONE                      |NONE                                      |C4723581|NONE     |00054-0604 |00054-0604-21|
+----------------------------+---------+---------------------------+-------+--------------------------+------------------------------------------+--------+---------+-----------+-------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|medication_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.4 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- TextMatcherInternalModel
- ChunkMergeModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperFilterer
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
- ResolverMerger
- ResolverMerger
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- Finisher
