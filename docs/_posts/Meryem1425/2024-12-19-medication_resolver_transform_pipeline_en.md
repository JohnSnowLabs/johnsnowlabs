---
layout: model
title: Pipeline to Resolve Medication Codes(Transform)
author: John Snow Labs
name: medication_resolver_transform_pipeline
date: 2024-12-19
tags: [licensed, en, resolver, snomed, umls, rxnorm, ndc, ade, pipeline]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

A pretrained resolver pipeline to extract medications and resolve their adverse reactions (ADE), RxNorm, UMLS, NDC, SNOMED CT codes, and action/treatments in clinical text.

Action/treatments are available for branded medication, and SNOMED codes are available for non-branded medication.

This pipeline can be used with Spark transform. You can use `medication_resolver_pipeline` as Lightpipeline (with `annotate/fullAnnotate`).

## Predicted Entities

`DRUG`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/medication_resolver_transform_pipeline_en_5.5.1_3.2_1734636623226.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/medication_resolver_transform_pipeline_en_5.5.1_3.2_1734636623226.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

medication_resolver_pipeline = PretrainedPipeline("medication_resolver_transform_pipeline", "en", "clinical/models")

text = """The patient was prescribed Amlodopine Vallarta 10-320mg, Eviplera.
The other patient is given Lescol 40 MG and Everolimus 1.5 mg tablet."""

data = spark.createDataFrame([[text]]).toDF("text")

result = medication_resolver_pipeline.transform(data)

```

{:.jsl-block}
```python

medication_resolver_pipeline = nlp.PretrainedPipeline("medication_resolver_transform_pipeline", "en", "clinical/models")

text = """The patient was prescribed Amlodopine Vallarta 10-320mg, Eviplera.
The other patient is given Lescol 40 MG and Everolimus 1.5 mg tablet."""

data = spark.createDataFrame([[text]]).toDF("text")

result = medication_resolver_pipeline.transform(data)


```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val medication_resolver_pipeline = new PretrainedPipeline("medication_resolver_transform_pipeline", "en", "clinical/models")

val data = Seq("""The patient was prescribed Amlodopine Vallarta 10-320mg, Eviplera.
The other patient is given Lescol 40 MG and Everolimus 1.5 mg tablet.""").toDS.toDF("text")

val result = medication_resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash


+----------------------------+---------+---------------------------+-------+--------------------------+------------------------------------------+--------+----------------+-----------+-------------+
|chunk                       |ner_label|ADE                        |RxNorm |Action                    |Treatment                                 |UMLS    |SNOMED_CT       |NDC_Product|NDC_Package  |
+----------------------------+---------+---------------------------+-------+--------------------------+------------------------------------------+--------+----------------+-----------+-------------+
|Amlodopine Vallarta 10-320mg|DRUG     |Gynaecomastia              |722131 |NONE                      |NONE                                      |C1949334|1153435009      |00093-7693 |00093-7693-56|
|Eviplera                    |DRUG     |Anxiety                    |217010 |Inhibitory Bone Resorption|Osteoporosis                              |C0720318|NONE            |NONE       |NONE         |
|Lescol 40 MG                |DRUG     |NONE                       |103919 |Hypocholesterolemic       |Heterozygous Familial Hypercholesterolemia|C0353573|NONE            |00078-0234 |00078-0234-05|
|Everolimus 1.5 mg tablet    |DRUG     |Acute myocardial infarction|2056895|NONE                      |NONE                                      |C4723581|1029521000202102|00054-0604 |00054-0604-21|
+----------------------------+---------+---------------------------+-------+--------------------------+------------------------------------------+--------+----------------+-----------+-------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|medication_resolver_transform_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.3 GB|

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
- Doc2Chunk
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- Doc2Chunk
- ChunkMapperModel
- Finisher