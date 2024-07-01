---
layout: model
title: Alcohol Usage For Classification
author: John Snow Labs
name: genericclassifier_alcohol_mpnet_wip
date: 2024-07-01
tags: [licenced, en, clinical, mpnet, alcohol, licensed]
task: Text Classification
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
annotator: GenericClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The Alcohol Usage classifier utilizes [MPNET embeddings](https://sparknlp.org/2023/08/29/mpnet_embedding_all_mpnet_base_v2_by_sentence_transformers_en.html) within a robust classifier architecture.
This model, trained on various datasets, provides accurate label assignments and confidence scores for its predictions. Utilizing MPNET embedding technology, it excels in comprehensive text analysis and offers valuable insights into alcohol usage within the provided texts. The primary goal of the model is to categorize texts into two main label categories: 'Current_Drinker' and 'Others.'

- `Current_Drinker`: This category encompasses statements indicating the person's current alcohol usage or situations where information regarding this matter is provided or available.

- `Others`: This category encompasses statements indicating the absence of current alcohol usage or situations where the information on this matter is unknown or not provided.

## Predicted Entities

`Current_Drinker`, `Others`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/genericclassifier_alcohol_mpnet_wip_en_5.3.3_3.0_1719841584956.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/genericclassifier_alcohol_mpnet_wip_en_5.3.3_3.0_1719841584956.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
        
sent_embd = MPNetEmbeddings.pretrained("mpnet_embedding_all_mpnet_base_v2_by_sentence_transformers", 'en')\
    .setInputCols(["document"])\
    .setOutputCol("sentence_embeddings")\

features_asm = FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")
      
generic_classifier = GenericClassifierModel.pretrained('genericclassifier_alcohol_mpnet_wip', 'en', 'clinical/models')\
    .setInputCols("features")\
    .setOutputCol("prediction")\

pipeline = Pipeline(stages=[
        document_assembler,
        sent_embd,
        features_asm,
        generic_classifier])

text_list = [
             "The patient, with a history of COPD and alcohol dependence, was initially admitted due to a COPD exacerbation and community-acquired pneumonia. The situation was further complicated by alcohol withdrawal. He was later transferred to another facility for treatment of left hand cellulitis, which raised concerns for necrotizing fasciitis.",
             "Until recently, the patient had maintained stability on his antidepressant regimen. However, he experienced a notable worsening of depressive symptoms last week, leading him to engage in heavy binge drinking as an ineffective way to suppress his emotional distress and feelings of despair.",
             "Ms. Jane Doe, a 60-year-old retired teacher, presented to the emergency department complaining of severe abdominal pain and vomiting. She has a history of gallstones but has been asymptomatic for years. Currently, she does not smoke or drink alcohol, focusing on a healthy lifestyle.",
             "Mr. John Smith, a 45-year-old accountant, came to the clinic reporting intense chest pain and shortness of breath. He has a history of hypertension but has managed it well with medication. He currently does not smoke or drink alcohol, maintaining a healthy lifestyle.",
               ]

df = spark.createDataFrame(text_list, StringType()).toDF("text")

result = pipeline.fit(df).transform(df)

result.select("text", "prediction.result").show(truncate=100)
```
```scala
val document_assembler = new DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
        
val sent_emb = MPNetEmbeddings.pretrained("mpnet_embedding_all_mpnet_base_v2_by_sentence_transformers", 'en')\
    .setInputCols(["document"])\
    .setOutputCol("sentence_embeddings")\

val features_asm = new FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

val generic_classifier = GenericClassifierModel.pretrained("genericclassifier_alcohol_mpnet_wip", 'en', 'clinical/models')\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sent_emb,
    features_asm,
    generic_classifier    
])

val data = Seq("The patient, with a history of COPD and alcohol dependence, was initially admitted due to a COPD exacerbation and community-acquired pneumonia. The situation was further complicated by alcohol withdrawal. He was later transferred to another facility for treatment of left hand cellulitis, which raised concerns for necrotizing fasciitis.",
             "Until recently, the patient had maintained stability on his antidepressant regimen. However, he experienced a notable worsening of depressive symptoms last week, leading him to engage in heavy binge drinking as an ineffective way to suppress his emotional distress and feelings of despair.",
             "Ms. Jane Doe, a 60-year-old retired teacher, presented to the emergency department complaining of severe abdominal pain and vomiting. She has a history of gallstones but has been asymptomatic for years. Currently, she does not smoke or drink alcohol, focusing on a healthy lifestyle.",
             "Mr. John Smith, a 45-year-old accountant, came to the clinic reporting intense chest pain and shortness of breath. He has a history of hypertension but has managed it well with medication. He currently does not smoke or drink alcohol, maintaining a healthy lifestyle.").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+-----------------+
|                                                                                                text|           result|
+----------------------------------------------------------------------------------------------------+-----------------+
|The patient, with a history of COPD and alcohol dependence, was initially admitted due to a COPD ...|[Current_Drinker]|
|Until recently, the patient had maintained stability on his antidepressant regimen. However, he e...|[Current_Drinker]|
|Ms. Jane Doe, a 60-year-old retired teacher, presented to the emergency department complaining of...|         [Others]|
|Mr. John Smith, a 45-year-old accountant, came to the clinic reporting intense chest pain and sho...|         [Others]|
+----------------------------------------------------------------------------------------------------+-----------------+  
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|genericclassifier_alcohol_mpnet_wip|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[features]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|3.4 MB|

## Benchmarking

```bash
                 precision    recall  f1-score   support
Current_Drinker       0.92      1.00      0.96        44
         Others       1.00      0.64      0.78        11
       accuracy          -         -      0.93        55
      macro-avg       0.96      0.82      0.87        55
   weighted-avg       0.93      0.93      0.92        55
```
