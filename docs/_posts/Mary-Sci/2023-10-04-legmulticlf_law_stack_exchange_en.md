---
layout: model
title: Legal Multilabel Classifier on Law Stack Exchange
author: John Snow Labs
name: legmulticlf_law_stack_exchange
date: 2023-10-04
tags: [licensed, legal, en, classification, multilabel, tensorflow]
task: Text Classification
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MultiClassifierDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is the Multi-Label Text Classification model that can be used to identify 30+ classes to facilitate analysis, discovery, and comparison of legal texts in English related to Law Stack Exchange.

## Predicted Entities

`business`, `california`, `canada`, `civil-law`, `constitutional-law`, `consumer-protection`, `contract-law`, `copyright`, `corporate-law`, `criminal-law`, `employment`, `england-and-wales`, `european-union`, `fraud`, `gdpr`, `germany`, `intellectual-property`, `international`, `internet`, `landlord`, `legal-terms`, `liability`, `licensing`, `police`, `privacy`, `property`, `real-estate`, `rental-property`, `software`, `tax-law`, `terms-of-service`, `trademark`, `traffic`, `united-kingdom`, `united-states`, `us-constitution`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legmulticlf_law_stack_exchange_en_1.0.0_3.0_1696431033425.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legmulticlf_law_stack_exchange_en_1.0.0_3.0_1696431033425.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document") \
    .setCleanupMode("shrink")

embeddings = nlp.InstructorEmbeddings.pretrained("instructor_large", "en") \
    .setInstruction("Represent for multilabel classification:") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence_embeddings")

classifierdl = nlp.MultiClassifierDLModel.pretrained('legmulticlf_law_stack_exchange', 'en', 'legal/models') \
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("class")

  
clf_pipeline = nlp.Pipeline(stages=[document_assembler, 
                                    embeddings, 
                                    classifierdl])

df = spark.createDataFrame([["I've seen this label on coke cans at one point, and I was wondering: is this legally enforceable?If it's not, is it possible for a retailer in any way to disallow the resale of an item purchased?Something like, I don't know, maybe a license you have to agree to in order to be allowed to purchase said item?This comes in the larger context of these new tech releases (GPUs, consoles) and how the producers/retailers could legally prevent scalpers."]]).toDF("text")

model = clf_pipeline.fit(df)
result = model.transform(df)

result.select("text", "class.result").show(truncate=False)
```

</div>

## Results

```bash
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
|text                                                                                                                                                                                                                                                                                                                                                                                                                                                           |result                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
|I've seen this label on coke cans at one point, and I was wondering: is this legally enforceable?If it's not, is it possible for a retailer in any way to disallow the resale of an item purchased?Something like, I don't know, maybe a license you have to agree to in order to be allowed to purchase said item?This comes in the larger context of these new tech releases (GPUs, consoles) and how the producers/retailers could legally prevent scalpers.|[contract-law, business]|
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legmulticlf_law_stack_exchange|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|14.0 MB|

## References

Train dataset available [here](https://huggingface.co/datasets/ymoslem/Law-StackExchange)

## Benchmarking

```bash
label                  precision  recall  f1-score  support 
business               1.00       0.82    0.90      51      
california             1.00       1.00    1.00      74     
canada                 1.00       0.97    0.99      74      
civil-law              0.98       0.94    0.96      52      
constitutional-law     1.00       1.00    1.00      53      
consumer-protection    1.00       0.86    0.92      28      
contract-law           0.98       0.89    0.94      199     
copyright              0.94       0.97    0.95      246     
corporate-law          1.00       0.88    0.94      26      
criminal-law           0.92       0.95    0.94      198     
employment             1.00       1.00    1.00      83      
england-and-wales      0.96       0.99    0.97      93      
european-union         0.91       0.93    0.92      72      
fraud                  1.00       0.97    0.99      39      
gdpr                   1.00       1.00    1.00      87      
germany                1.00       1.00    1.00      44      
intellectual-property  0.82       0.93    0.87      89      
international          0.91       1.00    0.95      71      
internet               0.96       0.96    0.96      83      
landlord               0.97       0.94    0.96      36      
legal-terms            1.00       1.00    1.00      56      
liability              1.00       0.93    0.96      42      
licensing              0.99       0.92    0.95      73      
police                 0.98       1.00    0.99      51      
privacy                1.00       0.83    0.90      69      
property               0.89       0.97    0.93      32      
real-estate            1.00       0.97    0.98      32      
rental-property        1.00       1.00    1.00      41      
software               0.92       0.83    0.87      69      
tax-law                1.00       1.00    1.00      38      
terms-of-service       0.96       0.96    0.96      25      
trademark              1.00       1.00    1.00      45      
traffic                1.00       1.00    1.00      30      
united-kingdom         0.97       0.94    0.96      161     
united-states          0.77       0.87    0.81      644     
us-constitution        1.00       0.95    0.98      43      
micro avg              0.92       0.93    0.93      3149    
macro avg              0.97       0.95    0.96      3149    
weighted avg           0.92       0.93    0.93      3149    
samples avg            0.92       0.94    0.92      3149    
```