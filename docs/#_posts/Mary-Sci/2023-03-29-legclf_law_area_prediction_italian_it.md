---
layout: model
title: Legal Law Area Prediction Classifier (Italian)
author: John Snow Labs
name: legclf_law_area_prediction_italian
date: 2023-03-29
tags: [it, licensed, classification, legal, tensorflow]
task: Text Classification
language: it
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalClassifierDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a Multiclass classification model which identifies law area labels(civil_law, penal_law, public_law, social_law) in Italian-based Court Cases.

## Predicted Entities

`civil_law`, `penal_law`, `public_law`, `social_law`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_law_area_prediction_italian_it_1.0.0_3.0_1680095983817.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_law_area_prediction_italian_it_1.0.0_3.0_1680095983817.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler() \
     .setInputCol("text") \
     .setOutputCol("document")

embeddings = nlp.BertSentenceEmbeddings.pretrained("sent_bert_multi_cased", "xx")\
    .setInputCols(["document"]) \
    .setOutputCol("sentence_embeddings")

docClassifier = legal.ClassifierDLModel.pretrained("legclf_law_area_prediction_italian", "it", "legal/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("category")

nlpPipeline = nlp.Pipeline(stages=[
      document_assembler, 
      embeddings,
      docClassifier
])

df = spark.createDataFrame([["Per questi motivi, il Tribunale federale pronuncia: 1. Nella misura in cui è ammissibile, il ricorso è respinto. 2. Le spese giudiziarie di fr. 1'000.-- sono poste a carico dei ricorrenti. 3. Comunicazione al patrocinatore dei ricorrenti, al Consiglio di Stato, al Gran Consiglio, al Tribunale amministrativo del Cantone Ticino e all'Ufficio federale dello sviluppo territoriale."]]).toDF("text")

model = nlpPipeline.fit(df)
result = model.transform(df)

result.select("text", "category.result").show(truncate=100)
```

</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+------------+
|                                                                                                text|      result|
+----------------------------------------------------------------------------------------------------+------------+
|Per questi motivi, il Tribunale federale pronuncia: 1. Nella misura in cui è ammissibile, il rico...|[public_law]|
+----------------------------------------------------------------------------------------------------+------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_law_area_prediction_italian|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|it|
|Size:|22.3 MB|

## References

Train dataset available [here](https://huggingface.co/datasets/rcds/legal_criticality_prediction)

## Benchmarking

```bash
label         precision  recall  f1-score  support 
civil_law     0.86       0.86    0.86      58      
penal_law     0.85       0.82    0.83      55      
public_law    0.79       0.79    0.79      52      
social_law    0.93       0.96    0.94      68      
accuracy      -          -       0.86      233     
macro-avg     0.86       0.86    0.86      233     
weighted-avg  0.86       0.86    0.86      233     
```