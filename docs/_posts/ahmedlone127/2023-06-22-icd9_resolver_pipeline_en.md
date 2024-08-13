---
layout: model
title: Pipeline to Resolve ICD-9-CM Codes
author: John Snow Labs
name: icd9_resolver_pipeline
date: 2023-06-22
tags: [en, licensed, clinical, resolver, pipeline, chunk_mapping, icd9]
task: Chunk Mapping
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"

deploy:
  sagemaker_link: 
  snowflake_link: 
  databricks_link: https://marketplace.databricks.com/details/c2469843-c104-4201-9db5-ba1542823448/John-Snow-Labs_Extract-Clinical-Findings-and-the-corresponding-ICD-9-codes

---

## Description

This pretrained pipeline maps entities with their corresponding ICD-9-CM codes. You’ll just feed your text and it will return the corresponding ICD-9-CM codes.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd9_resolver_pipeline_en_4.4.4_3.0_1687425221307.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd9_resolver_pipeline_en_4.4.4_3.0_1687425221307.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

{% if page.deploy %}
## Available as Private API Endpoint

{:.tac}
{% include display_platform_information.html %}
{% endif %}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("icd9_resolver_pipeline", "en", "clinical/models")

text= "A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years and anisakiasis. Also, it was reported that fetal and neonatal hemorrhage."

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("icd9_resolver_pipeline", "en", "clinical/models")

val result = pipeline.fullAnnotate("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years and anisakiasis. Also, it was reported that fetal and neonatal hemorrhage.")
```


{:.nlu-block}
```python
import nlu
nlu.load("en.resolve.icd9.pipeline").predict("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years and anisakiasis. Also, it was reported that fetal and neonatal hemorrhage.""")
```

</div>



## Results

```bash
|chunk                        |ner_chunk|icd9_code|
+-----------------------------+---------+---------+
|gestational diabetes mellitus|PROBLEM  |V12.21   |
|anisakiasis                  |PROBLEM  |127.1    |
|fetal and neonatal hemorrhage|PROBLEM  |772      |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd9_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|

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