---
layout: model
title: Diseases and Syndromes to UMLS Code Pipeline
author: John Snow Labs
name: umls_disease_syndrome_resolver_pipeline
date: 2023-03-30
tags: [en, licensed, umls, pipeline]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline maps entities (Diseases and Syndromes) with their corresponding UMLS CUI codes. You’ll just feed your text and it will return the corresponding UMLS codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_disease_syndrome_resolver_pipeline_en_4.3.2_3.2_1680190919515.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_disease_syndrome_resolver_pipeline_en_4.3.2_3.2_1680190919515.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
|Compatibility:|Healthcare NLP 4.3.2+|
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