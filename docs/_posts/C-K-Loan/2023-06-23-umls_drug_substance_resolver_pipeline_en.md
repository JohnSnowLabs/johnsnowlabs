---
layout: model
title: Drug Substance to UMLS Code Pipeline
author: John Snow Labs
name: umls_drug_substance_resolver_pipeline
date: 2023-06-23
tags: [licensed, clinical, en, umls, pipeline, drug, subtance]
task: Chunk Mapping
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline maps entities (Drug Substances) with their corresponding UMLS CUI codes. You’ll just feed your text and it will return the corresponding UMLS codes.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_drug_substance_resolver_pipeline_en_4.4.4_3.4_1687514231635.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_drug_substance_resolver_pipeline_en_4.4.4_3.4_1687514231635.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("umls_drug_substance_resolver_pipeline", "en", "clinical/models")

result = pipeline.annotate("The patient was given  metformin, lenvatinib and Magnesium hydroxide 100mg/1ml")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("umls_drug_substance_resolver_pipeline", "en", "clinical/models")

val result = pipeline.annotate("The patient was given  metformin, lenvatinib and Magnesium hydroxide 100mg/1ml")
```


</div>

## Results

```bash
+-----------------------------+---------+---------+
|chunk                        |ner_label|umls_code|
+-----------------------------+---------+---------+
|metformin                    |DRUG     |C0025598 |
|lenvatinib                   |DRUG     |C2986924 |
|Magnesium hydroxide 100mg/1ml|DRUG     |C1134402 |
+-----------------------------+---------+---------+
```


{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_drug_substance_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|5.1 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperFilterer
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
- ResolverMerger