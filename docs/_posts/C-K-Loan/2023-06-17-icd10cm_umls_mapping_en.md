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
---

## Description

This pretrained pipeline maps ICD10CM codes to UMLS codes without using any text data. You’ll just feed white space-delimited ICD10CM codes and it will return the corresponding UMLS codes as a list. If there is no mapping, the original code is returned with no mapping.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_umls_mapping_en_4.4.4_3.0_1686979219249.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_umls_mapping_en_4.4.4_3.0_1686979219249.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
{'icd10cm': ['M89.50', 'R82.2', 'R09.01'],
'umls': ['C4721411', 'C0159076', 'C0004044']}
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