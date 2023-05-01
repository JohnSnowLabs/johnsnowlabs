---
layout: model
title: Legal Multilabel Classifier on Covid-19 Exceptions (French)
author: John Snow Labs
name: legmulticlf_covid19_exceptions_french
date: 2023-04-13
tags: [fr, legal, multilabel, classification, licensed, tensorflow]
task: Text Classification
language: fr
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

This is the Multi-Label Text Classification model that can be used to identify up to 7 classes to facilitate analysis, discovery, and comparison of legal texts in French related to COVID-19 exception measures. The classes are as follows:

- Army_mobilization    
- Closures/lockdown   
- Government_oversight       
- Restrictions_of_daily_liberties    
- Restrictions_of_fundamental_rights_and_civil_liberties       
- State_of_Emergency          
- Suspension_of_international_cooperation_and_commitments

## Predicted Entities

`Army_mobilization`, `Closures/lockdown`, `Government_oversight`, `Restrictions_of_daily_liberties`, `Restrictions_of_fundamental_rights_and_civil_liberties`, `State_of_Emergency`, `Suspension_of_international_cooperation_and_commitments`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legmulticlf_covid19_exceptions_french_fr_1.0.0_3.0_1681406840199.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legmulticlf_covid19_exceptions_french_fr_1.0.0_3.0_1681406840199.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text")\
    .setOutputCol("document")

embeddings = nlp.BertSentenceEmbeddings.pretrained("sent_bert_use_cmlm_multi_base_br", "xx") \
    .setInputCols("document") \
    .setOutputCol("sentence_embeddings")

classifierdl = nlp.MultiClassifierDLModel.pretrained("legmulticlf_covid19_exceptions_french", "fr", "legal/models") \
    .setInputCols(["sentence_embeddings"])
    .setOutputCol("class")

clf_pipeline = nlp.Pipeline(
    stages=[document_assembler, 
            embeddings, 
            classifierdl])

df = spark.createDataFrame([["Par dérogation à l'alinéa 1er, sont autorisés :- les cérémonies funéraires, mais uniquement en présence de 15 personnes maximum, et sans possibilité d'exposition du corps ;"]]).toDF("text")

model = clf_pipeline.fit(df)
result = model.transform(df)

result.select("text", "class.result").show(truncate=False)
```

</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
|text                                                                                                                                                                        |result                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
|Par dérogation à l'alinéa 1er, sont autorisés :- les cérémonies funéraires, mais uniquement en présence de 15 personnes maximum, et sans possibilité d'exposition du corps ;|[Restrictions_of_fundamental_rights_and_civil_liberties, Restrictions_of_daily_liberties]|
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legmulticlf_covid19_exceptions_french|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|fr|
|Size:|14.0 MB|

## References

Train dataset available [here](https://huggingface.co/datasets/joelito/covid19_emergency_event)

## Benchmarking

```bash
label                                                    precision  recall  f1-score  support 
Army_mobilization                                        1.00       1.00    1.00      11      
Closures/lockdown                                        0.71       0.86    0.77      84      
Government_oversight                                     1.00       0.67    0.80      3       
Restrictions_of_daily_liberties                          0.72       0.73    0.73      75      
Restrictions_of_fundamental_rights_and_civil_liberties   0.65       0.66    0.65      47      
State_of_Emergency                                       0.81       0.74    0.77      53      
Suspension_of_international_cooperation_and_commitments  1.00       0.33    0.50      6       
micro-avg                                                0.73       0.76    0.75      279     
macro-avg                                                0.84       0.71    0.75      279     
weighted-avg                                             0.74       0.76    0.74      279     
samples-avg                                              0.75       0.80    0.74      279     
```