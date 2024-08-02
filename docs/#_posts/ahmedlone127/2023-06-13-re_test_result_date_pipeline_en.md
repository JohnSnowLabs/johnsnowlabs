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
spark_version: 3.0
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/re_test_result_date_pipeline_en_4.4.4_3.0_1686651964962.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/re_test_result_date_pipeline_en_4.4.4_3.0_1686651964962.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
|   | sentence | entity1_begin | entity1_end |      chunk1 | entity1 | entity2_begin | entity2_end |      chunk2 |     entity2 |      relation | confidence |
|--:|---------:|--------------:|------------:|------------:|--------:|--------------:|------------:|------------:|------------:|--------------:|-----------:|
| 0 |        0 |             0 |           1 |          He |  Gender |            15 |          25 | chest X-ray |        Test | is_finding_of |  0.9991597 |
| 1 |        0 |             0 |           1 |          He |  Gender |            30 |          36 |     CT scan |        Test | is_finding_of |        1.0 |
| 2 |        0 |            15 |          25 | chest X-ray |    Test |            30 |          36 |     CT scan |        Test | is_finding_of |        1.0 |
| 3 |        0 |            30 |          36 |     CT scan |    Test |            53 |          55 |         his |      Gender | is_finding_of |        1.0 |
| 4 |        0 |            30 |          36 |     CT scan |    Test |            57 |          60 |        SpO2 |        Test | is_finding_of |        1.0 |
| 5 |        0 |            53 |          55 |         his |  Gender |            57 |          60 |        SpO2 |        Test |    is_date_of |    0.98956 |
| 6 |        0 |            53 |          55 |         his |  Gender |            75 |          77 |         93% | Test_Result |    is_date_of |  0.9999974 |
| 7 |        0 |            57 |          60 |        SpO2 |    Test |            75 |          77 |         93% | Test_Result |  is_result_of | 0.92868817 |
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