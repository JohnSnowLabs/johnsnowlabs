---
layout: model
title: Clinical Drugs to UMLS Code Mapping
author: John Snow Labs
name: umls_drug_resolver_pipeline
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

This pretrained pipeline maps entities (Clinical Drugs) with their corresponding UMLS CUI codes. You’ll just feed your text and it will return the corresponding UMLS codes.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_drug_resolver_pipeline_en_4.4.4_3.4_1687527853632.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_drug_resolver_pipeline_en_4.4.4_3.4_1687527853632.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline= PretrainedPipeline("umls_drug_resolver_pipeline", "en", "clinical/models")
pipeline.annotate("The patient was given Adapin 10 MG, coumadn 5 mg")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline= PretrainedPipeline("umls_drug_resolver_pipeline", "en", "clinical/models")
val pipeline.annotate("The patient was given Adapin 10 MG, coumadn 5 mg")
```


{:.nlu-block}
```python
import nlu
nlu.load("en.map_entity.umls_drug_resolver").predict("""The patient was given Adapin 10 MG, coumadn 5 mg""")
```

</div>


## Results

```bash
+------------+---------+---------+
|chunk       |ner_label|umls_code|
+------------+---------+---------+
|Adapin 10 MG|DRUG     |C2930083 |
|coumadn 5 mg|DRUG     |C2723075 |
+------------+---------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_drug_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.6 GB|

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