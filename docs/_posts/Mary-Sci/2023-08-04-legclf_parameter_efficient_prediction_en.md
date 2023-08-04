---
layout: model
title: Legal Parameter Efficiency Prediction in Domain-Specific Documents
author: John Snow Labs
name: legclf_parameter_efficient_prediction
date: 2023-08-04
tags: [en, licensed, classification, legal, tensorflow]
task: Text Classification
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalBertForSequenceClassification
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a multiclass classification model trained to estimate parameter efficiency in legal domain-specific documents. The model demonstrates remarkable proficiency in predicting `business`, `constitutional-law`, `contract-law`, `copyright`, `criminal-law`, `employment`, `liability`, `privacy`, `tax-law`, `trademark` classes for a wide variety of legal issues.

## Predicted Entities

`business`, `constitutional-law`, `contract-law`, `copyright`, `criminal-law`, `employment`, `liability`, `privacy`, `tax-law`, `trademark`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_parameter_efficient_prediction_en_1.0.0_3.0_1691135028509.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_parameter_efficient_prediction_en_1.0.0_3.0_1691135028509.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
  
document_assembler = nlp.DocumentAssembler() \
    .setInputCol('text') \
    .setOutputCol('document')

tokenizer = nlp.Tokenizer() \
    .setInputCols(['document']) \
    .setOutputCol('token')

sequenceClassifier = legal.BertForSequenceClassification.pretrained("legclf_parameter_efficient_prediction", "en", "legal/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("class")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])

# couple of simple examples
example = spark.createDataFrame([["I have been helping a nonprofit by developing a piece of software that they needed. The software is more-or-less built to their specs in a 'functional' way, but I wrote 100% of the code: they are not programmers. Anyhow, we didn't make any kind of contract at the beginning verbally or otherwise. Who owns the copyright to all of this? Do they have any rights to it at all for providing 'ideas'?"]]).toDF("text")

result = pipeline.fit(example).transform(example)

# result is a DataFrame
result.select("text", "class.result").show(truncate=100)
```

</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+-----------+
|                                                                                                text|     result|
+----------------------------------------------------------------------------------------------------+-----------+
|I have been helping a nonprofit by developing a piece of software that they needed. The software ...|[copyright]|
+----------------------------------------------------------------------------------------------------+-----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_parameter_efficient_prediction|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|en|
|Size:|410.1 MB|
|Case sensitive:|true|
|Max sentence length:|512|

## References

Train dataset available [here](https://huggingface.co/datasets/jonathanli/law-stack-exchange)

## Benchmarking

```bash
label               precision  recall  f1-score  support
business            0.50       0.24    0.32      17      
constitutional-law  0.94       0.68    0.79      25      
contract-law        0.88       0.85    0.86      91      
copyright           0.91       0.97    0.94      151     
criminal-law        0.80       0.91    0.85      75      
employment          0.74       0.93    0.82      30      
liability           0.67       0.31    0.42      13      
privacy             0.77       0.82    0.79      28      
tax-law             0.93       0.78    0.85      32      
trademark           0.89       0.91    0.90      44      
accuracy            -          -       0.86      506     
macro-avg           0.80       0.74    0.75      506     
weighted-avg        0.85       0.86    0.85      506     
```
