---
layout: model
title: Extract Community Condition Entities from Social Determinants of Health Texts (LangTest)
author: John Snow Labs
name: ner_sdoh_community_condition_langtest
date: 2023-09-06
tags: [en, licensed, ner, clinical, sdoh, langtest]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

SDOH NER model is designed to detect and label social determinants of health (SDOH) community condition-related entities within text data. Social determinants of health are crucial factors that influence individuals' health outcomes, encompassing various social, economic, and environmental elements. 
The model has been trained using advanced machine-learning techniques on a diverse range of text sources. The model's accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results. This model is the version of [ner_sdoh_community_condition](https://nlp.johnsnowlabs.com/2023/07/02/ner_sdoh_community_condition_en.html) model augmented with `langtest` library.

Definitions of Predicted Entities:

Here are the labels of the SDOH NER model with their description:

- `Community_Safety`: safety of the neighborhood or places of study or work. "dangerous neighborhood, safe area, etc."
- `Environmental_Condition`: Conditions of the environment where people live. "pollution, air quality, noisy environment, etc."
- `Food_Insecurity`: Food insecurity is defined as a lack of consistent access to enough food for every person in a household to live an active, healthy life. "food insecurity, scarcity of protein, lack of food, etc."
- `Housing`: Conditions of the patient’s living spaces. "homeless, housing, small apartment, etc."
- `Transportation`: mentions of accessibility to transportation means. "car, bus, train, etc."

## Predicted Entities

`Community_Safety`, `Environmental_Condition`, `Food_Insecurity`, `Housing`, `Transportation`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_community_condition_langtest_en_5.1.0_3.0_1693992405127.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_community_condition_langtest_en_5.1.0_3.0_1693992405127.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_sdoh_community_condition_langtest", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])

sample_texts = [["He is currently experiencing financial stress due to job insecurity, and he lives in a small apartment in a low-income neighbourhood with limited access to green spaces and outdoor recreational activities. There is air pollution in the living area."], ["Patient reports difficulty for affording healthy food and relies on cheaper, processed options. He lives in an unsafe neighborhood. He lives alone"], ["She reports her husband and sons provide transportation to medical appts and do her grocery shopping."], ["He lives with his family, in his own house in a remote town, with a monthly income of $1200 per month. Due to lack of transportation, he is unable to access healthcare. "]]
             
data = spark.createDataFrame(sample_texts).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_sdoh_community_condition_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
))

val data = Seq(Array("He is currently experiencing financial stress due to job insecurity, and he lives in a small apartment in a low-income neighbourhood with limited access to green spaces and outdoor recreational activities. There is air pollution in the living area.", "Patient reports difficulty for affording healthy food and relies on cheaper, processed options. He lives in an unsafe neighborhood. He lives alone", "She reports her husband and sons provide transportation to medical appts and do her grocery shopping.", "He lives with his family, in his own house in a remote town, with a monthly income of $1200 per month. Due to lack of transportation, he is unable to access healthcare. ")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------------------------+-----------------------+
|chunk                          |ner_label              |
+-------------------------------+-----------------------+
|apartment                      |Housing                |
|low-income neighbourhood       |Community_Safety       |
|green spaces                   |Environmental_Condition|
|outdoor recreational activities|Environmental_Condition|
|pollution                      |Environmental_Condition|
|healthy food                   |Food_Insecurity        |
|unsafe neighborhood            |Community_Safety       |
|lives alone                    |Housing                |
|transportation                 |Transportation         |
|own house                      |Housing                |
|transportation                 |Transportation         |
+-------------------------------+-----------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_sdoh_community_condition_langtest|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.7 MB|

## References

Internal SDOH Project

## Benchmarking

```bash
label                      precision  recall  f1-score  support 
B-Community_Safety         0.88       0.94    0.91      16      
B-Environmental_Condition  1.00       1.00    1.00      16      
B-Food_Insecurity          0.87       0.93    0.90      14      
B-Housing                  0.90       0.89    0.89      172     
B-Transportation           0.87       0.84    0.85      31      
I-Community_Safety         0.91       1.00    0.95      21      
I-Environmental_Condition  1.00       1.00    1.00      12      
I-Food_Insecurity          0.92       0.86    0.89      14      
I-Housing                  0.97       0.86    0.91      251     
I-Transportation           0.53       0.80    0.64      10      
micro-avg                  0.92       0.88    0.90      557     
macro-avg                  0.89       0.91    0.89      557     
weighted-avg               0.93       0.88    0.90      557 
```
