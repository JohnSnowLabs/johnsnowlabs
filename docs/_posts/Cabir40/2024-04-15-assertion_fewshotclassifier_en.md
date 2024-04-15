---
layout: model
title: Few-Shot Assertion Model
author: John Snow Labs
name: assertion_fewshotclassifier
date: 2024-04-15
tags: [en, licensed]
task: Assertion Status
language: en
edition: Healthcare NLP 5.3.2
spark_version: 3.0
supported: true
annotator: FewShotAssertionClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Assign assertion status to clinical entities

## Predicted Entities

`absent`, `present`, `conditional`, `associated_with_someone_else`, `hypothetical`, `possible`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_fewshotclassifier_en_5.3.2_3.0_1713190012506.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_fewshotclassifier_en_5.3.2_3.0_1713190012506.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
#define pipeline
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

large_few_assertion = FewShotAssertionClassifierModel().pretrained("assertion_fewshotclassifier","en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("assertion_fewshot")

pipeline = sparknlp.base.Pipeline()\
    .setStages([
        document_assembler, 
        large_few_assertion
])

texts = [
    ["Her former vascular malformation:no arteriovenous malformations are identified ; there is no evidence of recurrence of her former vascular malformation."],   
    ["Hypertension:includes hypertension and chronic obstructive pulmonary disease."]
]

spark_df = spark.createDataFrame(texts).toDF("text")

results = pipeline.fit(spark_df).transform(spark_df)

#show results
results.select("assertion_fewshot").show(truncate=False)
```
```scala
val documentAssembler = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val large_few_assertion = FewShotAssertionClassifierModel().pretrained("assertion_fewshotclassifier", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("assertion_fewshot")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, 
    large_few_assertion
))

val texts = Seq(Array(
    "Her former vascular malformation:no arteriovenous malformations are identified ; there is no evidence of recurrence of her former vascular malformation.",
    "Hypertension:includes hypertension and chronic obstructive pulmonary disease."
)).toDF("text")

data = spark.createDataFrame(texts).toDF("text")

results = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
|result                                                                                                                                                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|[{category, 0, 151, absent, {absent_confidence -> 0.55019414, confidence -> 0.55019414, present_confidence -> 0.22024022, hypothetical_confidence -> 0.013334909, associated_with_someone_else_confidence -> 0.052178495, possible_confidence -> 0.1299262, conditional_confidence -> 0.034126014}, []}]    |
|[{category, 0, 76, conditional, {absent_confidence -> 0.17233582, confidence -> 0.34774542, present_confidence -> 0.113161795, hypothetical_confidence -> 0.17757988, associated_with_someone_else_confidence -> 0.13231324, possible_confidence -> 0.056863878, conditional_confidence -> 0.34774542}, []}]|
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_fewshotclassifier|
|Compatibility:|Healthcare NLP 5.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|403.6 MB|
|Case sensitive:|false|

## References

Trained with an augmented version of the i2b2 dataset.