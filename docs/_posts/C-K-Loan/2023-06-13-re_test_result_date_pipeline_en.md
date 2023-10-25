---
layout: model
title: RE Pipeline between Tests, Results, and Dates
author: John Snow Labs
name: re_test_result_date_pipeline
date: 2023-06-13
tags: [licensed, clinical, relation_extraction, tests, results, dates, en]
task: Relation Extraction
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [re_test_result_date](https://nlp.johnsnowlabs.com/2021/02/24/re_test_result_date_en.html) model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/re_test_result_date_pipeline_en_4.4.4_3.2_1686665254277.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/re_test_result_date_pipeline_en_4.4.4_3.2_1686665254277.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("re_test_result_date_pipeline", "en", "clinical/models")

pipeline.fullAnnotate("He was advised chest X-ray or CT scan after checking his SpO2 which was <= 93%")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("re_test_result_date_pipeline", "en", "clinical/models")

pipeline.fullAnnotate("He was advised chest X-ray or CT scan after checking his SpO2 which was <= 93%")
```


{:.nlu-block}
```python
import nlu
nlu.load("en.relation.date_test_result.pipeline").predict("""He was advised chest X-ray or CT scan after checking his SpO2 which was <= 93%""")
```

</div>



## Results

```bash
| index | relations    | entity1      | chunk1              | entity2      |  chunk2 |
|-------|--------------|--------------|---------------------|--------------|---------|
| 0     | O            | TEST         | chest X-ray         | MEASUREMENTS |  93%    | 
| 1     | O            | TEST         | CT scan             | MEASUREMENTS |  93%    |
| 2     | is_result_of | TEST         | SpO2                | MEASUREMENTS |  93%    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|re_test_result_date_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- PerceptronModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- DependencyParserModel
- RelationExtractionModel