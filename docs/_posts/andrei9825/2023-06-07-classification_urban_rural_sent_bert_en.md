---
layout: model
title: Urban_Rural_Med_Classifier
author: John Snow Labs
name: classification_urban_rural_sent_bert
date: 2023-06-07
tags: [en, licensed, tensorflow]
task: Text Classification
language: en
edition: Healthcare NLP 4.3.1
spark_version: 3.2
supported: true
engine: tensorflow
annotator: ClassifierDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This classifier effectively distinguishes between urban and rural areas, providing insights on healthcare accessibility and trends among patients residing in different geographical densities. Its applications range from understanding health disparities to optimizing resource allocation in healthcare services.

## Predicted Entities

`Urban`, `Rural`, `Other/Unknown`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/classification_urban_rural_sent_bert_en_4.3.1_3.2_1686159677184.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/classification_urban_rural_sent_bert_en_4.3.1_3.2_1686159677184.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
sentence_embeddings = classification_geography_DBiM_all_merged.model("classification_urban_rural_sent_bert", 'en','clinical/models')\
    .setInputCols(["document"])\
    .setOutputCol("sentence_embeddings")

features_asm = FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

generic_classifier = GenericClassifierModel.pretrained("genericclassifier_sdoh_economics_binary_sbiobert_cased_mli", 'en', 'clinical/models')\
    .setInputCols(["features"])\
    .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler,
    sentence_embeddings,
    features_asm,
    generic_classifier    
])

text_list = ["Jane is a 13-year-old Hindu female who was admitted to the hospital due to complaints of shortness of breath and chest pain. She has a history of being overweight and having a poor diet, as well as being physically inactive. Jane lives with her middle-class parents in an urban area and is currently not attending school due to her health condition."]
     
df = spark.createDataFrame(text_list, StringType()).toDF("text")

result = pipeline.fit(df).transform(df)

result.select("text", "class.result").show(truncate=100)
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|classification_urban_rural_sent_bert|
|Compatibility:|Healthcare NLP 4.3.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|52.0 MB|
|Dependencies:|sent_bert_base_case_embeddings|

## References

Proprietary JSL dataset.

## Sample text from the training dataset

Jane is a 13-year-old Hindu female who was admitted to the hospital due to complaints of shortness of breath and chest pain. She has a history of being overweight and having a poor diet, as well as being physically inactive. Jane lives with her middle-class parents in an urban area and is currently not attending school due to her health condition.

## Benchmarking

```bash
| Label         | TP  | FP  | FN  | Precision  | Recall     | F1         |
|---------------|-----|-----|-----|------------|------------|------------|
| Other/Unknown | 62  | 5   | 4   | 0.92537314 | 0.93939394 | 0.93233085 |
| Rural         | 43  | 1   | 9   | 0.97727275 | 0.8269231  | 0.8958333  |
| Urban         | 41  | 13  | 6   | 0.7592593  | 0.87234044 | 0.81188124 |
| Total         | 146 | 19  | 19  | -          | -          | -          |

 

| Averages      | Precision  | Recall     | F1        |
|---------------|------------|------------|-----------|
| Macro-average | 0.8873017  | 0.87955254 | 0.8834101 |
| Micro-average | 0.8848485  | 0.8848485  | 0.8848485 |
```