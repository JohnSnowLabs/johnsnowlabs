---
layout: model
title: Legal Multilabel Classifier on Online Terms of Service
author: John Snow Labs
name: legmulticlf_online_terms_of_service_english
date: 2023-04-26
tags: [en, licensed, multilabel, classification, legal, tensorflow]
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

This is the Multi-Label Text Classification model that can be used to identify potentially unfair clauses in online Terms of Service. The classes are as follows:

     - Arbitration 
     - Choice_of_law
     - Content_removal
     - Jurisdiction
     - Limitation_of_liability
     - Other
     - Unilateral_change
     - Unilateral_termination

## Predicted Entities

`Arbitration`, `Choice_of_law`, `Content_removal`, `Jurisdiction`, `Limitation_of_liability`, `Other`, `Unilateral_change`, `Unilateral_termination`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legmulticlf_online_terms_of_service_english_en_1.0.0_3.0_1682519205970.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legmulticlf_online_terms_of_service_english_en_1.0.0_3.0_1682519205970.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler() \
        .setInputCol('text')\
        .setOutputCol('document')

tokenizer = nlp.Tokenizer() \
        .setInputCols(['document'])\
        .setOutputCol('token')

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base", "en") \
        .setInputCols(['document', 'token'])\
        .setOutputCol("embeddings")

embeddingsSentence = nlp.SentenceEmbeddings() \
        .setInputCols(['document', 'embeddings'])\
        .setOutputCol('sentence_embeddings')\
        .setPoolingStrategy('AVERAGE')

classifierdl = nlp.MultiClassifierDLModel.pretrained('legmulticlf_online_terms_of_service_english', 'en', 'legal/models')
         .setInputCols(["sentence_embeddings"])\
         .setOutputCol("class")
  
clf_pipeline = nlp.Pipeline(stages=[document_assembler, 
                                    tokenizer, 
                                    embeddings, 
                                    embeddingsSentence, 
                                    classifierdl])

df = spark.createDataFrame([["We are not responsible or liable for (and have no obligation to verify) any wrong or misspelled email address or inaccurate or wrong (mobile) phone number or credit card number."]]).toDF("text")

model = clf_pipeline.fit(df)
result = model.transform(df)

result.select("text", "class.result").show(truncate=False)
```

</div>

## Results

```bash
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
|sentence                                                                                                                                                                         |result                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
|We are not responsible or liable for (and have no obligation to verify) any wrong or misspelled email address or inaccurate or wrong (mobile) phone number or credit card number.|[Limitation_of_liability]|
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legmulticlf_online_terms_of_service_english|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|13.9 MB|

## References

Train dataset available [here](https://huggingface.co/datasets/joelito/online_terms_of_service)

## Benchmarking

```bash
label                    precision  recall  f1-score  support 
Arbitration              1.00       0.50    0.67      4       
Choice_of_law            0.67       0.67    0.67      3       
Content_removal          1.00       0.67    0.80      3       
Jurisdiction             0.80       1.00    0.89      4       
Limitation_of_liability  0.73       0.73    0.73      15      
Other                    0.86       0.89    0.88      28      
Unilateral_change        0.86       1.00    0.92      6       
Unilateral_termination   1.00       0.80    0.89      5       
micro-avg                0.84       0.82    0.83      68      
macro-avg                0.86       0.78    0.81      68      
weighted-avg             0.85       0.82    0.83      68      
samples-avg              0.80       0.82    0.81      68      
```