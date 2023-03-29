---
layout: model
title: Legal Law Area Prediction Classifier in French
author: John Snow Labs
name: legclf_law_area_prediction_french
date: 2023-03-29
tags: [fr, licensed, classification, legal, tensorflow]
task: Text Classification
language: fr
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

This is a Multiclass classification model which identifies law area labels(civil_law, penal_law, public_law, social_law) in French-based Court Cases.

## Predicted Entities

`civil_law`, `penal_law`, `public_law`, `social_law`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_law_area_prediction_french_fr_1.0.0_3.0_1680094841099.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_law_area_prediction_french_fr_1.0.0_3.0_1680094841099.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

docClassifier = legal.ClassifierDLModel.pretrained("legclf_law_area_prediction_french", "fr", "legal/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("category")

nlpPipeline = nlp.Pipeline(stages=[
      document_assembler, 
      embeddings,
      docClassifier
])

df = spark.createDataFrame([["par ces motifs, le Juge unique prononce : 1. Le recours est irrecevable. 2. Il n'est pas perçu de frais judiciaires. 3. Le présent arrêt est communiqué aux parties, au Tribunal administratif fédéral et à l'Office fédéral des assurances sociales. Lucerne, le 2 juin 2016 Au nom de la IIe Cour de droit social du Tribunal fédéral suisse Le Juge unique : Meyer Le Greffier : Cretton"]]).toDF("text")

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
|par ces motifs, le Juge unique prononce : 1. Le recours est irrecevable. 2. Il n'est pas perçu de...|[social_law]|
+----------------------------------------------------------------------------------------------------+------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_law_area_prediction_french|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|fr|
|Size:|22.3 MB|

## References

Train dataset available [here](https://huggingface.co/datasets/rcds/legal_criticality_prediction)

## Benchmarking

```bash
label         precision  recall  f1-score  support 
civil_law     0.93       0.91    0.92      613     
penal_law     0.94       0.96    0.95      579     
public_law    0.92       0.91    0.92      605     
social_law    0.97       0.98    0.97      478     
accuracy      -          -       0.94      2275    
macro-avg     0.94       0.94    0.94      2275    
weighted-avg  0.94       0.94    0.94      2275    
```