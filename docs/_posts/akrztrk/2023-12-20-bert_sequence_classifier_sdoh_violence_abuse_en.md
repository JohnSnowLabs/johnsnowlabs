---
layout: model
title: Social Determinants of Healthcare for Violence and Abuse Classifier
author: John Snow Labs
name: bert_sequence_classifier_sdoh_violence_abuse
date: 2023-12-20
tags: [sdoh, en, clinical, social_determinants_of_heathcare, public_health, violence, abuse, licensed, tensorflow]
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

The Violence and Abuse classifier employs [MedicalBertForSequenceClassification embeddings](https://sparknlp.org/2022/07/18/biobert_pubmed_base_cased_v1.2_en_3_0.html) within a robust classifier architecture. Trained on a diverse dataset, this model provides accurate label assignments and confidence scores for its predictions. The primary goal of this model is to categorize text into four key labels: `Domestic_Violence_Abuse`, `Personal_Violence_Abuse`, `No_Violence_Abuse` and `Unknown`.

- `Domestic_Violence_Abuse`:This category refers to a pattern of behavior in any relationship that is aimed at gaining or maintaining power and control over an intimate partner or family member.

- `Personal_Violence_Abuse`: This category encompasses any form of violence or abuse that is directed towards an individual, whether admitted by the perpetrator or recognized by the victim.

- `No_Violence_Abuse`: This category denotes the complete absence of violence and abuse in any form.

- `Unknown`: This category covers when the nature or type of violence or abuse within a given text cannot be clearly identified or defined.

## Predicted Entities

`Domestic_Violence_Abuse`, `Personal_Violence_Abuse`, `No_Violence_Abuse`, `Unknown`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_SEQUENCE_CLASSIFICATION/){:.button.button-orange}
[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_sdoh_violence_abuse_en_5.1.4_3.0_1703086100729.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_sdoh_violence_abuse_en_5.1.4_3.0_1703086100729.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_sdoh_violence_abuse", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("prediction")

pipeline = Pipeline(
        stages=[
            document_assembler,
            tokenizer,
            sequenceClassifier
            ])

sample_texts = [
                ["Repeated visits for fractures, with vague explanations suggesting potential family-related trauma."],
                ["Patient presents with multiple bruises in various stages of healing, suggestive of repeated physical abuse."],
                ["There are no reported instances or documented episodes indicating the patient poses a risk of violence."] ,
                ["Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy."]
                ]

sample_data = spark.createDataFrame(sample_texts).toDF("text")

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

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_sdoh_violence_abuse", "en", "clinical/models")
    .setInputCols(Array("document","token"))
    .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(documenter, tokenizer, sequenceClassifier))

val data = Seq(Array("Repeated visits for fractures, with vague explanations suggesting potential family-related trauma.",
                     "Patient presents with multiple bruises in various stages of healing, suggestive of repeated physical abuse.",
                     "There are no reported instances or documented episodes indicating the patient poses a risk of violence." ,
                     "Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy.",
                    )).toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+-------------------------+
|                                                                                                text|                   result|
+----------------------------------------------------------------------------------------------------+-------------------------+
|  Repeated visits for fractures, with vague explanations suggesting potential family-related trauma.|[Domestic_Violence_Abuse]|
|Patient presents with multiple bruises in various stages of healing, suggestive of repeated physi...|[Personal_Violence_Abuse]|
|There are no reported instances or documented episodes indicating the patient poses a risk of vio...|      [No_Violence_Abuse]|
|Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatm...|                [Unknown]|
+----------------------------------------------------------------------------------------------------+-------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_sdoh_violence_abuse|
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
Domestic_Violence_Abuse   0.921687  0.905325  0.913433       169
      No_Violence_Abuse   0.978417  0.860759  0.915825       158
Personal_Violence_Abuse   0.889908  0.858407  0.873874       226
                Unknown   0.937500  0.975610  0.956175       738
               accuracy          -         -  0.931836      1291
              macro-avg   0.931878  0.900025  0.914827      1291
           weighted-avg   0.932106  0.931836  0.931234      1291
```