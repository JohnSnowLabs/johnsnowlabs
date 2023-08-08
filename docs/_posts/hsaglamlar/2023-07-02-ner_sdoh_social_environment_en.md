---
layout: model
title: Extract Social Environment Entities from Social Determinants of Health Texts
author: John Snow Labs
name: ner_sdoh_social_environment
date: 2023-07-02
tags: [chidhood_event, legal, social, sdoh, social_determinants, violence, en, public_health, licensed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

SDOH NER model is designed to detect and label social determinants of health (SDOH) social environment entities within text data. Social determinants of health are crucial factors that influence individuals' health outcomes, encompassing various social, economic, and environmental elements. The model has been trained using advanced machine-learning techniques on a diverse range of text sources. The model's accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results. Here are the labels of the SDOH NER model with their description:

- `Chidhood_Event`: Childhood events mentioned by the patient. "childhood trauma, childhood abuse, etc."
- `Legal_Issues`: Issues that have legal implications. "legal issues, legal problems, detention, in prison, etc."
- `Social_Exclusion`: Absence or lack of rights or accessibility to services or goods that are expected of the majority of the population. "social exclusion, social isolation, gender discrimination, etc."
- `Social_Support`: he presence of friends, family or other people to turn to for comfort or help.  "social support, live with family, etc."
- `Violence_Or_Abuse`: Episodes of abuse or violence experienced and reported by the patient. "domestic violence, sexual abuse, etc."

## Predicted Entities

`Chidhood_Event`, `Legal_Issues`, `Social_Exclusion`, `Social_Support`, `Violence_Or_Abuse`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_NER.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_social_environment_en_4.4.4_3.0_1688322410202.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_social_environment_en_4.4.4_3.0_1688322410202.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from pyspark.sql.types import StringType

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_sdoh_social_environment", "en", "clinical/models")\
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

sample_texts = ["He is the primary caregiver.",
"There is some evidence of abuse.",
"She stated that she was in a safe environment in prison, but that her siblings lived in an unsafe neighborhood, she was very afraid for them and witnessed their ostracism by other people.",
"Medical history: Jane was born in a low - income household and experienced significant trauma during her childhood, including physical abuse and emotional abuse."]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_sdoh_social_environment", "en", "clinical/models")
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

val data = Seq(Array("He is the primary caregiver.",
"There is some evidence of abuse.",
"She stated that she was in a safe environment in prison, but that her siblings lived in an unsafe neighborhood, she was very afraid for them and witnessed their ostracism by other people.",
"Medical history: Jane was born in a low - income household and experienced significant trauma during her childhood, including physical abuse and emotional abuse.")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------------------------+-----+---+-----------------+
|chunk                      |begin|end|ner_label        |
+---------------------------+-----+---+-----------------+
|primary caregiver          |10   |26 |Social_Support   |
|abuse                      |26   |30 |Violence_Or_Abuse|
|in prison                  |46   |54 |Legal_Issues     |
|ostracism                  |161  |169|Social_Exclusion |
|trauma during her childhood|87   |113|Chidhood_Event   |
|physical abuse             |126  |139|Violence_Or_Abuse|
|emotional abuse            |145  |159|Violence_Or_Abuse|
+---------------------------+-----+---+-----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_sdoh_social_environment|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|850.8 KB|
|Dependencies:|embeddings_clinical|

## References

Internal SDOH Project

## Benchmarking

```bash
            label  precision    recall  f1-score   support
   Chidhood_Event       0.88      0.74      0.81        31
     Legal_Issues       0.86      0.90      0.88        42
 Social_Exclusion       0.85      0.82      0.84        28
   Social_Support       0.95      0.92      0.93       667
Violence_Or_Abuse       0.88      0.81      0.84        89
        micro-avg       0.93      0.90      0.91       857
        macro-avg       0.89      0.84      0.86       857
     weighted-avg       0.93      0.90      0.91       857
```