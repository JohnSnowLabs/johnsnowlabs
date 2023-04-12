---
layout: model
title: Legal Multilabel Classifier on Covid-19 exceptions
author: John Snow Labs
name: legmulticlf_covid19_exceptions_english
date: 2023-04-12
tags: [lecensed, legal, classification, en, multilabel, licensed, tensorflow]
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

This is the Multi-Label Text Classification model that can be used to identify up to 6 classes to facilitate analysis, discovery and comparison of legal texts related to COVID-19 exception measures. The classes are as follows:

- Closures/lockdown
- Government_oversight
- Restrictions_of_daily_liberties       
- Restrictions_of_fundamental_rights_and_civil_liberties       
- State_of_Emergency       
- Suspension_of_international_cooperation_and_commitments

## Predicted Entities

`Closures/lockdown`, `Government_oversight`, `Restrictions_of_daily_liberties`, `Restrictions_of_fundamental_rights_and_civil_liberties`, `State_of_Emergency`, `Suspension_of_international_cooperation_and_commitments`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legmulticlf_covid19_exceptions_english_en_1.0.0_3.0_1681315675753.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legmulticlf_covid19_exceptions_english_en_1.0.0_3.0_1681315675753.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

classifierdl = nlp.MultiClassifierDLModel.pretrained("legmulticlf_covid19_exceptions_english", "en", "legal/models")
  
clf_pipeline = nlp.Pipeline(stages=[document_assembler, 
                                    tokenizer, 
                                    embeddings, 
                                    embeddingsSentence, 
                                    classifierdl])

df = spark.createDataFrame([["First, we must protect the NHS’s ability to cope. We must be confident that we are able to provide sufficient critical care and specialist treatment right across the UK. The NHS staff have been incredible. We must continue to support them as much as we can."]]).toDF("text")

model = clf_pipeline.fit(df)
result = model.transform(df)

result.select("text", "class.result").show(truncate=False)
```

</div>

## Results

```bash
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
|text                                                                                                                                                                                                                                                             |result                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
|First, we must protect the NHS’s ability to cope. We must be confident that we are able to provide sufficient critical care and specialist treatment right across the UK. The NHS staff have been incredible. We must continue to support them as much as we can.|[Government_oversight]|
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legmulticlf_covid19_exceptions_english|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|13.9 MB|

## References

Train dataset available [here](https://huggingface.co/datasets/joelito/covid19_emergency_event)

## Benchmarking

```bash
label                                                    precision  recall  f1-score  support 
Closures/lockdown                                        1.00       0.60    0.75      10      
Government_oversight                                     0.88       1.00    0.94      22      
Restrictions_of_daily_liberties                          0.83       0.95    0.89      21      
Restrictions_of_fundamental_rights_and_civil_liberties   1.00       0.88    0.93      8       
State_of_Emergency                                       1.00       0.89    0.94      28      
Suspension_of_international_cooperation_and_commitments  1.00       1.00    1.00      2       
micro-avg                                                0.92       0.90    0.91      91      
macro-avg                                                0.95       0.89    0.91      91      
weighted-avg                                             0.93       0.90    0.91      91      
samples-avg                                              0.91       0.91    0.91      91      
```