---
layout: model
title: Smoking Usage For Classification
author: John Snow Labs
name: genericclassifier_smoking_mpnet_wip
date: 2024-07-01
tags: [smoking, en, clinical, licensed, mpnet]
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

The Smoking Usage classifier utilizes [MPNET embeddings](https://sparknlp.org/2023/08/29/mpnet_embedding_all_mpnet_base_v2_by_sentence_transformers_en.html) within a robust classifier architecture.
This model, trained on various datasets, provides accurate label assignments and confidence scores for its predictions. Utilizing MPNET embedding technology, it excels in comprehensive text analysis and offers valuable insights into alcohol usage within the provided texts. The primary goal of the model is to categorize texts into two main label categories: 'Current_Smoker' and 'Others.'

- `Current_Smoker`: This category encompasses statements indicating the person's current smoking usage or situations where information regarding this matter is provided or available.

- `Others`: This category encompasses statements indicating the absence of current smoking usage or situations where the information on this matter is unknown or not provided.

## Predicted Entities

`Current_Smoker`, `Others`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/genericclassifier_smoking_mpnet_wip_en_5.3.3_3.0_1719842097697.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/genericclassifier_smoking_mpnet_wip_en_5.3.3_3.0_1719842097697.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
      
generic_classifier = GenericClassifierModel.pretrained('genericclassifier_smoking_mpnet_wip', 'en', 'clinical/models')\
    .setInputCols("features")\
    .setOutputCol("prediction")\

pipeline = Pipeline(stages=[
        document_assembler,
        sent_embd,
        features_asm,
        generic_classifier])

text_list = [
    """Mr. John Smith, a 45-year-old truck driver, visited the clinic with enduring symptoms of cough and breathlessness, which have progressively worsened over recent months. He denies any significant past medical history, although he is a current smoker, consuming ten cigarettes daily for the last two decades.""",  
    """History of Present Illness: 52-year-old teacher Mrs. Sarah Johnson arrived to the clinic complaining of a chronic cough and dyspnea that had been becoming worse over the previous few months. She is a current smoker, and has smoked for the past 30 years, averaging a pack of cigarettes every day.""",
    """Pulmonary Function Tests: showed restricted airflow and decreased FEV1 and FEV1/FVC ratios, which are indicators of chronic obstructive pulmonary disease (COPD). Diagnosis: Smoking-related chronic obstructive pulmonary disease (COPD)""",
    """Ms. Jane Doe, a 60-year-old retired teacher, presented to the emergency department complaining of severe abdominal pain and vomiting. She has a history of gallstones but has been asymptomatic for years. Currently, she does not smoke or drink alcohol, focusing on a healthy lifestyle.""",
    """On admission, he reported feeling anxious, agitated, and excessive sweating but denied nausea, vomiting, headache, auditory, visual, or tactile hallucinations. The system review was otherwise unfavorable. He denied smoking and using illegal drugs, and he was not taking any medication.""",
]

df = spark.createDataFrame(text_list, StringType()).toDF("text")

result = pipeline.fit(df).transform(df)

result.select("text", "prediction.result").show(truncate=100)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
        
val sent_emb = MPNetEmbeddings.pretrained("mpnet_embedding_all_mpnet_base_v2_by_sentence_transformers", "en")
    .setInputCols(["document"])
    .setOutputCol("sentence_embeddings")

val features_asm = new FeaturesAssembler()
    .setInputCols(["sentence_embeddings"])
    .setOutputCol("features")

val generic_classifier = GenericClassifierModel.pretrained("genericclassifier_smoking_mpnet_wip", "en", "clinical/models")
    .setInputCols(["features"])
    .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sent_emb,
    features_asm,
    generic_classifier    
])

val data = Seq([
    """Mr. John Smith, a 45-year-old truck driver, visited the clinic with enduring symptoms of cough and breathlessness, which have progressively worsened over recent months. He denies any significant past medical history, although he is a current smoker, consuming ten cigarettes daily for the last two decades.""",  
    """History of Present Illness: 52-year-old teacher Mrs. Sarah Johnson arrived to the clinic complaining of a chronic cough and dyspnea that had been becoming worse over the previous few months. She is a current smoker, and has smoked for the past 30 years, averaging a pack of cigarettes every day.""",
    """Pulmonary Function Tests: showed restricted airflow and decreased FEV1 and FEV1/FVC ratios, which are indicators of chronic obstructive pulmonary disease (COPD). Diagnosis: Smoking-related chronic obstructive pulmonary disease (COPD)""",
    """Ms. Jane Doe, a 60-year-old retired teacher, presented to the emergency department complaining of severe abdominal pain and vomiting. She has a history of gallstones but has been asymptomatic for years. Currently, she does not smoke or drink alcohol, focusing on a healthy lifestyle.""",
    """On admission, he reported feeling anxious, agitated, and excessive sweating but denied nausea, vomiting, headache, auditory, visual, or tactile hallucinations. The system review was otherwise unfavorable. He denied smoking and using illegal drugs, and he was not taking any medication.""",
]).toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+----------------+
|                                                                                                text|          result|
+----------------------------------------------------------------------------------------------------+----------------+
|Mr. John Smith, a 45-year-old truck driver, visited the clinic with enduring symptoms of cough an...|[Current_Smoker]|
|History of Present Illness: 52-year-old teacher Mrs. Sarah Johnson arrived to the clinic complain...|[Current_Smoker]|
|Pulmonary Function Tests: showed restricted airflow and decreased FEV1 and FEV1/FVC ratios, which...|[Current_Smoker]|
|Ms. Jane Doe, a 60-year-old retired teacher, presented to the emergency department complaining of...|        [Others]|
|On admission, he reported feeling anxious, agitated, and excessive sweating but denied nausea, vo...|        [Others]|
+----------------------------------------------------------------------------------------------------+----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|genericclassifier_smoking_mpnet_wip|
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

Current_Smoker       0.91      1.00      0.95        10
        Others       1.00      0.98      0.99        45
      accuracy          -         -      0.98        55
     macro-avg       0.95      0.99      0.97        55
  weighted-avg       0.98      0.98      0.98        55
```
