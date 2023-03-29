---
layout: model
title: Legal Law Area Prediction Classifier in German
author: John Snow Labs
name: legclf_law_area_prediction_german
date: 2023-03-29
tags: [de, licensed, classification, legal, tensorflow]
task: Text Generation
language: de
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

This is a Multiclass classification model which identifies law area labels(civil_law, penal_law, public_law, social_law) in German-based Court Cases.

## Predicted Entities

`civil_law`, `penal_law`, `public_law`, `social_law`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_law_area_prediction_german_de_1.0.0_3.0_1680091124408.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_law_area_prediction_german_de_1.0.0_3.0_1680091124408.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

docClassifier = legal.ClassifierDLModel.pretrained("legclf_law_area_prediction_german", "de", "legal/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("category")

nlpPipeline = nlp.Pipeline(stages=[
      document_assembler, 
      embeddings,
      docClassifier
])

df = spark.createDataFrame([["Demnach erkennt das Bundesgericht: 1. Auf die Beschwerde wird nicht eingetreten. 2. Das Gesuch um unentgeltliche Rechtspflege und Verbeiständung wird abgewiesen. 3. Es werden keine Kosten erhoben. 4. Dieses Urteil wird den Parteien und dem Kantonsgericht des Kantons Schwyz, 1. Rekurskammer, schriftlich mitgeteilt. Lausanne, 21. Oktober 2008 Im Namen der II. zivilrechtlichen Abteilung des Schweizerischen Bundesgerichts Der Präsident: Der Gerichtsschreiber: Raselli von Roten"]]).toDF("text")

model = nlpPipeline.fit(df)
result = model.transform(df)

result.select("text", "category.result").show(truncate=100)
```

</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+-----------+
|                                                                                                text|     result|
+----------------------------------------------------------------------------------------------------+-----------+
|Demnach erkennt das Bundesgericht: 1. Auf die Beschwerde wird nicht eingetreten. 2. Das Gesuch um...|[civil_law]|
+----------------------------------------------------------------------------------------------------+-----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_law_area_prediction_german|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|de|
|Size:|22.4 MB|

## References

Train dataset available [here](https://huggingface.co/datasets/rcds/legal_criticality_prediction)

## Benchmarking

```bash
label         precision  recall  f1-score  support 
civil_law     0.94       0.94    0.94      1058    
penal_law     0.99       0.93    0.96      929     
public_law    0.92       0.96    0.94      965     
social_law    0.99       0.99    0.99      1003    
accuracy      -          -       0.96      3955    
macro-avg     0.96       0.96    0.96      3955    
weighted-avg  0.96       0.96    0.96      3955    
```
