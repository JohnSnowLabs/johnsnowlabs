---
layout: model
title: Diseases and Syndromes to UMLS Code Pipeline
author: John Snow Labs
name: umls_disease_syndrome_resolver_pipeline
date: 2023-06-23
tags: [en, licensed, umls, pipeline]
task: Pipeline Healthcare
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

This pretrained pipeline maps entities (Diseases and Syndromes) with their corresponding UMLS CUI codes. You’ll just feed your text and it will return the corresponding UMLS codes.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_disease_syndrome_resolver_pipeline_en_4.4.4_3.4_1687523214656.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_disease_syndrome_resolver_pipeline_en_4.4.4_3.4_1687523214656.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline= PretrainedPipeline("umls_disease_syndrome_resolver_pipeline", "en", "clinical/models")
pipeline.annotate("A 34-year-old female with a history of poor appetite, gestational diabetes mellitus, acyclovir allergy and polyuria")

```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline= PretrainedPipeline("umls_disease_syndrome_resolver_pipeline", "en", "clinical/models")
val pipeline.annotate("A 34-year-old female with a history of poor appetite, gestational diabetes mellitus, acyclovir allergy and polyuria")

```


{:.nlu-block}
```python
import nlu
nlu.load("en.map_entity.umls_disease_syndrome_resolver").predict("""A 34-year-old female with a history of poor appetite, gestational diabetes mellitus, acyclovir allergy and polyuria""")
```

</div>



## Results

```bash
+-----------------------------+---------+---------+
|chunk                        |ner_label|umls_code|
+-----------------------------+---------+---------+
|poor appetite                |PROBLEM  |C0003123 |
|gestational diabetes mellitus|PROBLEM  |C0085207 |
|acyclovir allergy            |PROBLEM  |C0571297 |
|polyuria                     |PROBLEM  |C0018965 |
+-----------------------------+---------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_disease_syndrome_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.4 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- ChunkMergeModel
- ChunkMapperModel
- ChunkMapperFilterer
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
- ResolverMerger