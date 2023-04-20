---
layout: model
title: Legal Multilabel Classifier on Covid-19 Exceptions (Italian)
author: John Snow Labs
name: legmulticlf_covid19_exceptions_italian
date: 2023-04-20
tags: [it, licensed, legal, multilabel, classification, tensorflow]
task: Text Classification
language: it
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

This is the Multi-Label Text Classification model that can be used to identify up to 5 classes to facilitate analysis, discovery, and comparison of legal texts in Italian related to COVID-19 exception measures. The classes are as follows:

 -  Closures/lockdown     
 -  Government_oversight    
 -  Restrictions_of_daily_liberties      
 -  Restrictions_of_fundamental_rights_and_civil_liberties      
 -  State_of_Emergency

## Predicted Entities

`Closures/lockdown`, `Government_oversight`, `Restrictions_of_daily_liberties`, `Restrictions_of_fundamental_rights_and_civil_liberties`, `State_of_Emergency`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legmulticlf_covid19_exceptions_italian_it_1.0.0_3.0_1681985472330.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legmulticlf_covid19_exceptions_italian_it_1.0.0_3.0_1681985472330.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"]) \
    .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_bert_base_italian_xxl_cased", "it") \
    .setInputCols(["document", "token"])\
    .setOutputCol("embeddings")

embeddingsSentence = nlp.SentenceEmbeddings() \
    .setInputCols(["document", "embeddings"])\
    .setOutputCol("sentence_embeddings")\
    .setPoolingStrategy("AVERAGE")
    
multilabelClfModel = nlp.MultiClassifierDLModel.pretrained('legmulticlf_covid19_exceptions_italian', 'it', "legal/models") \
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("class")

clf_pipeline = nlp.Pipeline(
    stages=[document_assembler, 
            tokenizer,
            embeddings, 
            embeddingsSentence,
            multilabelClfModel])

df = spark.createDataFrame([["Al di fuori di tale ultima ipotesi, secondo le raccomandazioni impartite dal Ministero della salute, occorre provvedere ad assicurare la corretta applicazione di misure preventive quali lavare frequentemente le mani con acqua e detergenti comuni."]]).toDF("text")

model = clf_pipeline.fit(df)
result = model.transform(df)

result.select("text", "class.result").show(truncate=False)
```

</div>

## Results

```bash
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------+
|text                                                                                                                                                                                                                                                  |result                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------+
|Al di fuori di tale ultima ipotesi, secondo le raccomandazioni impartite dal Ministero della salute, occorre provvedere ad assicurare la corretta applicazione di misure preventive quali lavare frequentemente le mani con acqua e detergenti comuni.|[Restrictions_of_daily_liberties]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legmulticlf_covid19_exceptions_italian|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|it|
|Size:|13.9 MB|

## References

Train dataset available [here](https://huggingface.co/datasets/joelito/covid19_emergency_event)

## Benchmarking

```bash
label                                                   precision  recall  f1-score  support 
Closures/lockdown                                       0.88       0.94    0.91      47      
Government_oversight                                    1.00       0.50    0.67      4       
Restrictions_of_daily_liberties                         0.88       0.79    0.83      28      
Restrictions_of_fundamental_rights_and_civil_liberties  0.62       0.62    0.62      16      
State_of_Emergency                                      0.67       1.00    0.80      6       
micro-avg                                               0.82       0.83    0.83      101     
macro-avg                                               0.81       0.77    0.77      101     
weighted-avg                                            0.83       0.83    0.83      101     
samples-avg                                             0.81       0.84    0.81      101     
```