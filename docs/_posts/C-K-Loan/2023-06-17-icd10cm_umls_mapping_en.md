---
layout: model
title: ICD10 to UMLS Code Mapping
author: John Snow Labs
name: icd10cm_umls_mapping
date: 2023-06-17
tags: [en, licensed, icd10cm, umls, pipeline, chunk_mapping]
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
  databricks_link: https://marketplace.databricks.com/details/0ee92a5c-35f1-40c9-a7b3-0282e67d9bd1/John-Snow-Labs_-ICD10CM-to-UMLS-Code-Mapper

---

## Description

This pretrained pipeline maps ICD10CM codes to UMLS codes without using any text data. You’ll just feed white space-delimited ICD10CM codes and it will return the corresponding UMLS codes as a list. If there is no mapping, the original code is returned with no mapping.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.1.Code_Mapping_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_umls_mapping_en_4.4.4_3.0_1686979219249.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_umls_mapping_en_4.4.4_3.0_1686979219249.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

pipeline = PretrainedPipeline("icd10cm_umls_mapping", "en", "clinical/models")

result = pipeline.fullAnnotate(['M8950', 'R822', 'R0901'])
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("icd10cm_umls_mapping", "en", "clinical/models")

val result = pipeline.fullAnnotate(['M8950', 'R822', 'R0901'])
```


{:.nlu-block}
```python
import nlu
nlu.load("en.icd10cm.umls.mapping").predict("""Put your text here.""")
```

</div>



## Results

```bash
|   | icd10cm_code | umls_code |
|--:|-------------:|----------:|
| 0 |        M8950 |  C4721411 |
| 1 |         R822 |  C0159076 |
| 2 |        R0901 |  C0004044 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_umls_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|956.6 KB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ChunkMapperModel