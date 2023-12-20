---
layout: model
title: Social Determinants of Healthcare for Mental Health Classifier
author: John Snow Labs
name: bert_sequence_classifier_sdoh_mental_health
date: 2023-12-20
tags: [licenced, sdoh, en, clinical, social_determinants_of_heathcare, public_health, mental_health, licensed, tensorflow]
task: Text Classification
language: en
edition: Healthcare NLP 5.1.4
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The Mental Health classifier employs [MedicalBertForSequenceClassification embeddings](https://sparknlp.org/2022/07/18/biobert_pubmed_base_cased_v1.2_en_3_0.html) within a robust classifier architecture. Trained on a diverse dataset, this model provides accurate label assignments and confidence scores for its predictions. The primary goal of this model is to categorize text into two key labels: 'Mental_Disorder' and 'No_Or_Not_Mentioned'.

- `Mental_Disorder`: It encompasses a wide range of mental health conditions that affect a person's mood, thinking, behavior, and overall psychological well-being.

- `No_Or_Not_Mentioned`: The patient doesn’t have mental health problems or it is not mentioned in the clinical notes.

## Predicted Entities

`Mental_Disorder`, `No_Or_Not_Mentioned`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_SEQUENCE_CLASSIFICATION/){:.button.button-orange}
[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_sdoh_mental_health_en_5.1.4_3.0_1703076463310.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_sdoh_mental_health_en_5.1.4_3.0_1703076463310.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_sdoh_mental_health", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
                            document_assembler,
                            tokenizer,
                            sequenceClassifier
                            ])

sample_texts= [ "John, a 45-year-old man, was diagnosed with bipolar disorder, a mental disorder characterized by alternating periods of elevated mood (mania) and depression. His treatment plan involved a combination of mood stabilizing medication and regular therapy sessions. With proper management and support, John learned to better understand and cope with his condition, leading to improved stability and overall well-being.",
                "Lisa, a 28-year-old woman, was diagnosed with generalized anxiety disorder (GAD), a mental disorder characterized by excessive worry and persistent anxiety.",
                "Mark, a 35-year-old man, sought medical help for symptoms of attention-deficit/hyperactivity disorder (ADHD), a neurodevelopmental disorder characterized by inattention, hyperactivity, and impulsivity. After a comprehensive evaluation, Mark was diagnosed with ADHD, and his healthcare provider recommended a multimodal treatment approach. ",
                "Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy.",
                "She reported occasional respiratory symptoms, such as wheezing and shortness of breath, but had no signs of a mental disorder. Her healthcare provider assessed her lung function, reviewed her medication regimen, and provided personalized asthma education. ",
                "During the appointment, her healthcare provider assessed her joint function, reviewed her medication regimen, and discussed the importance of adherence. They also discussed the benefits of regular exercise, maintaining a healthy weight, and using assistive devices when needed to support Anna's joint health. ",       
            ]

sample_data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(sample_data).transform(sample_data)

result.select("text", "prediction.result").show(truncate=100)
```
```scala
val documenter = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_sdoh_mental_health", "en", "clinical/models")
    .setInputCols(Array("document","token"))
    .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(documenter, tokenizer, sequenceClassifier))

val data = Seq(Array("John, a 45-year-old man, was diagnosed with bipolar disorder, a mental disorder characterized by alternating periods of elevated mood (mania) and depression. His treatment plan involved a combination of mood stabilizing medication and regular therapy sessions. With proper management and support, John learned to better understand and cope with his condition, leading to improved stability and overall well-being.",
                     "Lisa, a 28-year-old woman, was diagnosed with generalized anxiety disorder (GAD), a mental disorder characterized by excessive worry and persistent anxiety.",
                     "Mark, a 35-year-old man, sought medical help for symptoms of attention-deficit/hyperactivity disorder (ADHD), a neurodevelopmental disorder characterized by inattention, hyperactivity, and impulsivity. After a comprehensive evaluation, Mark was diagnosed with ADHD, and his healthcare provider recommended a multimodal treatment approach. ",
                     "Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy.",
                     "She reported occasional respiratory symptoms, such as wheezing and shortness of breath, but had no signs of a mental disorder. Her healthcare provider assessed her lung function, reviewed her medication regimen, and provided personalized asthma education. ",
                     "During the appointment, her healthcare provider assessed her joint function, reviewed her medication regimen, and discussed the importance of adherence. They also discussed the benefits of regular exercise, maintaining a healthy weight, and using assistive devices when needed to support Anna's joint health. ",
                    )).toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+---------------------+
|                                                                                                text|               result|
+----------------------------------------------------------------------------------------------------+---------------------+
|John, a 45-year-old man, was diagnosed with bipolar disorder, a mental disorder characterized by ...|    [Mental_Disorder]|
|Lisa, a 28-year-old woman, was diagnosed with generalized anxiety disorder (GAD), a mental disord...|    [Mental_Disorder]|
|Mark, a 35-year-old man, sought medical help for symptoms of attention-deficit/hyperactivity diso...|    [Mental_Disorder]|
|Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatm...|[No_Or_Not_Mentioned]|
|She reported occasional respiratory symptoms, such as wheezing and shortness of breath, but had n...|[No_Or_Not_Mentioned]|
|During the appointment, her healthcare provider assessed her joint function, reviewed her medicat...|[No_Or_Not_Mentioned]|
+----------------------------------------------------------------------------------------------------+---------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_sdoh_mental_health|
|Compatibility:|Healthcare NLP 5.1.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|406.4 MB|
|Case sensitive:|false|
|Max sentence length:|512|

## References

Trained with the in-house dataset

## Benchmarking

```bash
              label  precision    recall  f1-score   support
    Mental_Disorder   0.903226  0.845921  0.873635       331
No_Or_Not_Mentioned   0.923653  0.953632  0.938403       647
           accuracy          -         -  0.917178       978
          macro-avg   0.913439  0.899777  0.906019       978
       weighted-avg   0.916739  0.917178  0.916483       978
```